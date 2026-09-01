import os
import re
import json
import time
import requests
from typing import List, Dict, Any, Optional

SETTINGS_FILE = os.path.join(os.path.dirname(__file__), "..", "frontend", "src", "data", "settings.json")
LESSONS_FILE = os.path.join(os.path.dirname(__file__), "..", "frontend", "src", "data", "lessons.json")
BACKUP_FILE = os.path.join(os.path.dirname(__file__), "..", "frontend", "src", "data", "lessons.json.backup")
ENV_FILE = os.path.join(os.path.dirname(__file__), "..", "frontend", ".env")

def get_token_v2() -> str:
    token = os.getenv("NOTION_TOKEN_V2", "")
    if not token and os.path.exists(ENV_FILE):
        with open(ENV_FILE, "r", encoding="utf-8") as f:
            for line in f:
                if line.startswith("NOTION_TOKEN_V2="):
                    token = line.strip().split("=", 1)[1].strip()
                    break
    return token

def extract_page_id(url: str) -> str:
    cleaned = url.split("?")[0].split("#")[0]
    match = re.search(r"([a-f0-9]{32})", cleaned, re.IGNORECASE)
    if match:
        return match.group(1)
    
    uuid_match = re.search(r"([a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12})", cleaned, re.IGNORECASE)
    if uuid_match:
        return uuid_match.group(1).replace("-", "")
    
    segments = [s for s in cleaned.split("/") if s]
    if segments:
        last = segments[-1]
        parts = last.split("-")
        if len(parts[-1]) == 32:
            return parts[-1]
    
    raise ValueError(f"Notion URL'dan ID topib bo'lmadi: {url}")

def format_uuid(id_hex: str) -> str:
    if "-" in id_hex:
        return id_hex
    return f"{id_hex[:8]}-{id_hex[8:12]}-{id_hex[12:16]}-{id_hex[16:20]}-{id_hex[20:]}"

def fetch_page_chunk(page_id: str, token_v2: str) -> Dict[str, Any]:
    formatted_id = format_uuid(page_id)
    url = "https://www.notion.so/api/v3/loadPageChunk"
    headers = {
        "Content-Type": "application/json",
        "Cookie": f"token_v2={token_v2};",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    payload = {
        "pageId": formatted_id,
        "limit": 100,
        "cursor": {"stack": []},
        "chunkNumber": 0,
        "verticalColumns": False
    }
    
    res = requests.post(url, json=payload, headers=headers, timeout=15)
    res.raise_for_status()
    data = res.json()
    return data.get("recordMap", {})

def extract_text_from_title(title_prop: Any) -> str:
    if not title_prop:
        return ""
    if isinstance(title_prop, list):
        res = []
        for item in title_prop:
            if isinstance(item, list) and item:
                res.append(str(item[0]))
            else:
                res.append(str(item))
        return "".join(res)
    return str(title_prop)

def get_block_val(record_map: Dict[str, Any], block_id: str) -> Optional[Dict[str, Any]]:
    block_dict = record_map.get("block", {})
    entry = block_dict.get(block_id, {})
    if not entry:
        return None
    val = entry.get("value", {})
    if isinstance(val, dict) and "value" in val:
        return val["value"]
    return val if isinstance(val, dict) else None

def get_rich_text(block_data: Dict[str, Any]) -> str:
    if not block_data:
        return ""
    props = block_data.get("properties", {})
    if "title" in props:
        return extract_text_from_title(props["title"])
    if "caption" in props:
        return extract_text_from_title(props["caption"])
    return ""

def parse_block_recursive(block_id: str, record_map: Dict[str, Any], indent: int = 0) -> str:
    bd = get_block_val(record_map, block_id)
    if not bd:
        return ""
    
    b_type = bd.get("type", "text")
    text = get_rich_text(bd)
    prefix = "  " * indent
    lines = []
    
    if b_type == "header":
        lines.append(f"\n# {text}")
    elif b_type == "sub_header":
        lines.append(f"\n## {text}")
    elif b_type == "sub_sub_header":
        lines.append(f"\n### {text}")
    elif b_type == "text":
        lines.append(f"{prefix}{text}" if text else "")
    elif b_type == "bulleted_list":
        lines.append(f"{prefix}- {text}")
    elif b_type == "numbered_list":
        lines.append(f"{prefix}1. {text}")
    elif b_type == "to_do":
        checked = bd.get("properties", {}).get("checked", [["No"]])[0][0] == "Yes"
        chk_str = "x" if checked else " "
        lines.append(f"{prefix}- [{chk_str}] {text}")
    elif b_type == "code":
        lang = bd.get("properties", {}).get("language", [["python"]])[0][0]
        lines.append(f"\n```{lang}\n{text}\n```")
    elif b_type == "quote":
        lines.append(f"{prefix}> {text}")
    elif b_type == "callout":
        lines.append(f"{prefix}> 💡 {text}")
    elif b_type == "divider":
        lines.append("\n---\n")
    elif b_type == "toggle":
        lines.append(f"\n**{text}**")
    elif b_type in ["image", "file", "pdf", "video"]:
        src = bd.get("properties", {}).get("source")
        file_url = extract_text_from_title(src) if src else ""
        if not file_url and bd.get("format", {}).get("display_source"):
            file_url = bd["format"]["display_source"]
        if b_type == "image":
            lines.append(f"\n![rasm]({file_url})\n")
        else:
            lines.append(f"📎 [{text or 'fayl'}]({file_url})")
    else:
        if text:
            lines.append(f"{prefix}{text}")

    child_ids = bd.get("content", [])
    for cid in child_ids:
        child_md = parse_block_recursive(cid, record_map, indent + 1 if b_type != "toggle" else indent)
        if child_md:
            lines.append(child_md)

    return "\n".join(lines)

def scrape_single_notion_page(url: str) -> Optional[Dict[str, Any]]:
    token = get_token_v2()
    page_id = extract_page_id(url)
    record_map = fetch_page_chunk(page_id, token)
    
    block_ids = list(record_map.get("block", {}).keys())
    if not block_ids:
        return None
    
    page_block = get_block_val(record_map, block_ids[0])
    title = get_rich_text(page_block) or "Nomsiz dars"
    content_ids = page_block.get("content", []) if page_block else []
    
    md_blocks = []
    for cid in content_ids:
        md = parse_block_recursive(cid, record_map)
        if md:
            md_blocks.append(md)
            
    full_md = "\n".join(md_blocks)
    
    # Uy vazifasini ajratish
    lines = full_md.split("\n")
    hw_lines = []
    in_hw = False
    for line in lines:
        low = line.lower().strip()
        if "uyga vazifa" in low or "homework" in low or "vazifa" in low:
            in_hw = True
            continue
        if in_hw and (low.startswith("# ") or low.startswith("## ")):
            in_hw = False
        if in_hw and line.strip():
            hw_lines.append(line)
            
    # Dars raqamini title'dan ajratish
    num_match = re.search(r"(\d+)", title)
    num = int(num_match.group(1)) if num_match else 1
    
    clean_title = re.sub(r"^\d+[-–.\s]*(dars|DARS)?\s*[-–:.\s]*", "", title, flags=re.IGNORECASE).strip() or title
    
    return {
        "id": f"les-python-{num}-{int(time.time()*1000)}",
        "lessonNumber": num,
        "title": clean_title,
        "date": "",
        "time": "14:00 - 16:00",
        "status": "planned",
        "description": clean_title,
        "content": f"### Dars Konspekti\n\n{full_md}",
        "homework": "\n".join(hw_lines).strip() or "Berilmagan.",
        "materials": [],
        "tasks": []
    }

def save_lessons_to_json(lessons: List[Dict[str, Any]], mode: str = "merge") -> List[Dict[str, Any]]:
    existing = []
    if os.path.exists(LESSONS_FILE):
        try:
            with open(LESSONS_FILE, "r", encoding="utf-8") as f:
                existing = json.load(f)
            with open(BACKUP_FILE, "w", encoding="utf-8") as f:
                json.dump(existing, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print("Backup error:", e)
            
    if mode == "replace":
        final_lessons = lessons
    else:
        final_lessons = list(existing)
        for new_les in lessons:
            idx = next((i for i, l in enumerate(final_lessons) if l.get("lessonNumber") == new_les.get("lessonNumber")), -1)
            if idx != -1:
                final_lessons[idx] = {**final_lessons[idx], **new_les}
            else:
                final_lessons.append(new_les)
                
    final_lessons.sort(key=lambda x: x.get("lessonNumber", 0))
    
    with open(LESSONS_FILE, "w", encoding="utf-8") as f:
        json.dump(final_lessons, f, ensure_ascii=False, indent=2)
        
    return final_lessons
