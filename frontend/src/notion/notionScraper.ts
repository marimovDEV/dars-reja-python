import { NotionAPI } from 'notion-client';
import dotenv from 'dotenv';
import path from 'path';
import { fileURLToPath } from 'url';
import fs from 'fs';
import { Lesson, LessonTask, LessonMaterial } from '../types';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

// Load .env
dotenv.config({ path: path.join(__dirname, '..', '..', '.env') });

const LESSONS_FILE = path.join(__dirname, '..', 'data', 'lessons.json');
const BACKUP_FILE = path.join(__dirname, '..', 'data', 'lessons.json.backup');

// ============================================================
// 1. NOTION CLIENT (Norasmiy API — token_v2 orqali)
// ============================================================
const getScraperClient = (): NotionAPI => {
  const tokenV2 = process.env.NOTION_TOKEN_V2 || '';
  if (!tokenV2) {
    throw new Error('NOTION_TOKEN_V2 .env faylida topilmadi!');
  }
  return new NotionAPI({
    authToken: tokenV2,
  });
};

// ============================================================
// 2. NOTION ID NI URL DAN OLISH
// ============================================================
export const extractPageId = (url: string): string => {
  // https://www.notion.so/workspace/Page-Title-abc123def456...
  // yoki https://notion.so/abc123def456...
  const cleaned = url.split('?')[0].split('#')[0];
  // Oxirgi 32 xonali hex ID ni olish
  const match = cleaned.match(/([a-f0-9]{32})/i);
  if (match) return match[1];

  // Tire bilan ajratilgan format: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
  const uuidMatch = cleaned.match(/([a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12})/i);
  if (uuidMatch) return uuidMatch[1].replace(/-/g, '');

  // Oxirgi segment olish
  const segments = cleaned.split('/').filter(Boolean);
  const last = segments[segments.length - 1] || '';
  // "Page-Title-abc123..." formatdan ID ni olish
  const parts = last.split('-');
  const lastPart = parts[parts.length - 1];
  if (lastPart && /^[a-f0-9]{32}$/i.test(lastPart)) return lastPart;

  throw new Error(`Notion URL dan ID ajratib bo'lmadi: ${url}`);
};

// ============================================================
// 3. BLOKLARDAN MATN CHIQARISH
// ============================================================
interface BlockContent {
  text: string;
  type: string;
  children?: BlockContent[];
}

const extractTextFromValue = (value: any): string => {
  if (!value) return '';
  // Notion blocks have "title" or "properties.title" arrays
  // Each element is [text, [[format, value]]] or just [text]
  if (Array.isArray(value)) {
    return value.map((segment: any) => {
      if (Array.isArray(segment)) {
        return segment[0] || '';
      }
      return String(segment);
    }).join('');
  }
  return String(value);
};

const getBlockValue = (blockMap: any, blockId: string): any => {
  const entry = blockMap.block?.[blockId];
  if (!entry) return null;
  // Notion norasmiy API: value.value yoki faqat value
  if (entry.value?.value) return entry.value.value;
  if (entry.value) return entry.value;
  return entry;
};

const getRichText = (blockData: any): string => {
  if (!blockData) return '';
  const props = blockData.properties;
  if (!props) return '';

  // "title" property is the main text
  const title = props.title;
  if (title) return extractTextFromValue(title);

  // Some blocks use "caption"
  const caption = props.caption;
  if (caption) return extractTextFromValue(caption);

  return '';
};

// ============================================================
// 4. SAHIFANI REKURSIV PARSE QILISH
// ============================================================
interface ParsedPage {
  title: string;
  blocks: ParsedBlock[];
  childPages: { id: string; title: string }[];
}

interface ParsedBlock {
  id: string;
  type: string;
  text: string;
  level?: number; // heading uchun
  listType?: string;
  checked?: boolean;
  language?: string; // code block uchun
  fileUrl?: string;
  fileName?: string;
  children: ParsedBlock[];
}

const parseBlock = (blockId: string, blockMap: any): ParsedBlock => {
  const blockData = getBlockValue(blockMap, blockId);
  if (!blockData) {
    return { id: blockId, type: 'unknown', text: '', children: [] };
  }

  const type = blockData.type || 'text';
  const text = getRichText(blockData);

  const parsed: ParsedBlock = {
    id: blockId,
    type,
    text,
    children: [],
  };

  // Heading level
  if (type === 'header') parsed.level = 1;
  if (type === 'sub_header') parsed.level = 2;
  if (type === 'sub_sub_header') parsed.level = 3;

  // Code block
  if (type === 'code') {
    parsed.language = blockData.properties?.language?.[0]?.[0] || 'python';
  }

  // Checkbox
  if (type === 'to_do') {
    parsed.checked = blockData.properties?.checked?.[0]?.[0] === 'Yes';
  }

  // File / Image
  if (type === 'image' || type === 'file' || type === 'pdf' || type === 'video') {
    const source = blockData.properties?.source;
    if (source) {
      parsed.fileUrl = extractTextFromValue(source);
    }
    // Notion hosted files
    if (blockData.format?.display_source) {
      parsed.fileUrl = blockData.format.display_source;
    }
    parsed.fileName = text || `file_${blockId.slice(0, 8)}`;
  }

  // Recursively parse child blocks
  const childIds: string[] = blockData.content || [];
  for (const childId of childIds) {
    parsed.children.push(parseBlock(childId, blockMap));
  }

  return parsed;
};

const parsePage = (recordMap: any): ParsedPage => {
  const blockMap = recordMap;
  const blockIds = Object.keys(blockMap.block || {});

  if (blockIds.length === 0) {
    return { title: 'Bo\'sh sahifa', blocks: [], childPages: [] };
  }

  // Birinchi block — sahifa o'zi
  const pageBlockId = blockIds[0];
  const pageBlock = getBlockValue(blockMap, pageBlockId);
  const pageTitle = getRichText(pageBlock) || 'Nomsiz sahifa';

  // Qolgan bloklarni parse qilish
  const contentIds: string[] = pageBlock?.content || [];
  const blocks: ParsedBlock[] = [];
  const childPages: { id: string; title: string }[] = [];

  for (const cid of contentIds) {
    const childBlock = getBlockValue(blockMap, cid);
    if (!childBlock) continue;

    if (childBlock.type === 'page') {
      childPages.push({
        id: cid,
        title: getRichText(childBlock) || 'Nomsiz',
      });
    } else {
      blocks.push(parseBlock(cid, blockMap));
    }
  }

  return { title: pageTitle, blocks, childPages };
};

// ============================================================
// 5. BLOKLARNI MARKDOWN GA AYLANTIRISH
// ============================================================
const blocksToMarkdown = (blocks: ParsedBlock[], indent: number = 0): string => {
  const lines: string[] = [];
  const prefix = '  '.repeat(indent);

  for (const block of blocks) {
    switch (block.type) {
      case 'header':
        lines.push(`\n# ${block.text}`);
        break;
      case 'sub_header':
        lines.push(`\n## ${block.text}`);
        break;
      case 'sub_sub_header':
        lines.push(`\n### ${block.text}`);
        break;
      case 'text':
        if (block.text) lines.push(`${prefix}${block.text}`);
        else lines.push('');
        break;
      case 'bulleted_list':
        lines.push(`${prefix}- ${block.text}`);
        break;
      case 'numbered_list':
        lines.push(`${prefix}1. ${block.text}`);
        break;
      case 'to_do':
        lines.push(`${prefix}- [${block.checked ? 'x' : ' '}] ${block.text}`);
        break;
      case 'code':
        lines.push(`\n\`\`\`${block.language || ''}\n${block.text}\n\`\`\``);
        break;
      case 'quote':
        lines.push(`${prefix}> ${block.text}`);
        break;
      case 'callout':
        lines.push(`${prefix}> 💡 ${block.text}`);
        break;
      case 'divider':
        lines.push('\n---\n');
        break;
      case 'toggle':
        lines.push(`\n<details>\n<summary>${block.text}</summary>\n`);
        if (block.children.length > 0) {
          lines.push(blocksToMarkdown(block.children, indent));
        }
        lines.push('</details>\n');
        break;
      case 'image':
        lines.push(`\n![${block.fileName || 'rasm'}](${block.fileUrl || ''})\n`);
        break;
      case 'file':
      case 'pdf':
        lines.push(`\n📎 [${block.fileName || 'fayl'}](${block.fileUrl || ''})\n`);
        break;
      case 'table':
      case 'table_row':
        if (block.text) lines.push(`| ${block.text} |`);
        break;
      case 'bookmark':
        lines.push(`🔗 [${block.text || 'Havola'}](${block.text})`);
        break;
      default:
        if (block.text) lines.push(`${prefix}${block.text}`);
    }

    // Ichki bloklarni chiqarish (toggle bundan mustasno — yuqorida allaqachon)
    if (block.type !== 'toggle' && block.children.length > 0) {
      lines.push(blocksToMarkdown(block.children, indent + 1));
    }
  }

  return lines.join('\n');
};

// ============================================================
// 6. SAHIFALARNI DARSLIK FORMATIGA AYLANTIRISH
// ============================================================
interface ScrapedLesson {
  title: string;
  markdown: string;
  files: { name: string; url: string }[];
  childPageIds: string[];
}

const extractFilesFromBlocks = (blocks: ParsedBlock[]): { name: string; url: string }[] => {
  const files: { name: string; url: string }[] = [];
  for (const block of blocks) {
    if (block.fileUrl) {
      files.push({ name: block.fileName || 'file', url: block.fileUrl });
    }
    if (block.children.length > 0) {
      files.push(...extractFilesFromBlocks(block.children));
    }
  }
  return files;
};

const scrapeSinglePage = async (notion: NotionAPI, pageId: string): Promise<ScrapedLesson> => {
  const recordMap = await notion.getPage(pageId);
  const parsed = parsePage(recordMap);
  const markdown = blocksToMarkdown(parsed.blocks);
  const files = extractFilesFromBlocks(parsed.blocks);

  return {
    title: parsed.title,
    markdown,
    files,
    childPageIds: parsed.childPages.map(cp => cp.id),
  };
};

// ============================================================
// 7. DARSLIK KATEGORIYASINI ANIQLASH
// ============================================================
interface CategorizedContent {
  theory: string;
  practice: string;
  homework: string;
  tasks: LessonTask[];
}

const categorizeContent = (markdown: string, title: string): CategorizedContent => {
  const lines = markdown.split('\n');
  let currentSection: 'theory' | 'practice' | 'homework' = 'theory';
  const sections: Record<string, string[]> = { theory: [], practice: [], homework: [] };
  const tasks: LessonTask[] = [];
  let taskCount = 0;

  for (const line of lines) {
    const lower = line.toLowerCase().trim();

    // Seksiya aniqlovchilar
    if (lower.includes('amaliyot') || lower.includes('practice') || lower.includes('topshiriq') ||
        lower.includes('mashq') || lower.includes('exercise') || lower.includes('💻')) {
      currentSection = 'practice';
      continue;
    }
    if (lower.includes('uyga vazifa') || lower.includes('homework') || lower.includes('vazifa') ||
        lower.includes('uy ishi') || lower.includes('🏠')) {
      currentSection = 'homework';
      continue;
    }
    if (lower.includes('nazariya') || lower.includes('theory') || lower.includes('mavzu') ||
        lower.includes('tushuncha') || lower.includes('📖') || lower.includes('📋')) {
      currentSection = 'theory';
      continue;
    }

    sections[currentSection].push(line);

    // Topshiriqlarni ajratish (numbered list yoki checkbox)
    if (currentSection === 'practice' && (line.match(/^\d+\./) || line.match(/^- \[/))) {
      taskCount++;
      tasks.push({
        id: `task-scraped-${taskCount}`,
        title: `Topshiriq ${taskCount}`,
        type: 'practical',
        question: line.replace(/^\d+\.\s*/, '').replace(/^- \[.\]\s*/, ''),
      });
    }
  }

  return {
    theory: sections.theory.join('\n').trim(),
    practice: sections.practice.join('\n').trim(),
    homework: sections.homework.join('\n').trim() || 'Berilmagan.',
    tasks,
  };
};

// ============================================================
// 8. ASOSIY SCRAPER FUNKSIYASI
// ============================================================
export interface ScrapeResult {
  success: boolean;
  lessons: Lesson[];
  totalPages: number;
  errors: string[];
  duration: number;
}

export const scrapeNotionPage = async (pageUrl: string): Promise<ScrapeResult> => {
  const startTime = Date.now();
  const errors: string[] = [];
  const lessons: Lesson[] = [];

  try {
    const notion = getScraperClient();
    const pageId = extractPageId(pageUrl);

    console.log(`🔗 Notion sahifaga ulanilmoqda: ${pageId}...`);

    // 1. Asosiy sahifani olish
    const recordMap = await notion.getPage(pageId);
    const mainPage = parsePage(recordMap);

    console.log(`📄 Asosiy sahifa: "${mainPage.title}"`);
    console.log(`📑 Ichki sahifalar soni: ${mainPage.childPages.length}`);

    // 2. Agar ichki sahifalar bo'lsa — har birini dars sifatida olish
    if (mainPage.childPages.length > 0) {
      let lessonNum = 1;

      for (const childPage of mainPage.childPages) {
        try {
          console.log(`  📥 ${lessonNum}/${mainPage.childPages.length}: "${childPage.title}" olinmoqda...`);

          const scraped = await scrapeSinglePage(notion, childPage.id);
          const categorized = categorizeContent(scraped.markdown, scraped.title);

          // Darslik raqamini sarlavhadan aniqlash
          const numMatch = scraped.title.match(/(\d+)/);
          const detectedNum = numMatch ? parseInt(numMatch[1], 10) : lessonNum;

          const content = categorized.theory
            ? `### Dars Konspekti\n\n${categorized.theory}`
            : `### Dars Konspekti\n\n${scraped.markdown}`;

          const materials: LessonMaterial[] = scraped.files.map((f, idx) => ({
            id: `mat-scraped-${detectedNum}-${idx}`,
            name: f.name,
            type: (f.name.split('.').pop()?.toLowerCase() || 'link') as any,
            url: f.url,
          }));

          lessons.push({
            id: `les-scraped-${detectedNum}-${Date.now()}`,
            lessonNumber: detectedNum,
            title: scraped.title.replace(/^\d+[-–.\s]*dars\s*[-–:.\s]*/i, '').trim() || scraped.title,
            date: '',
            time: '14:00 - 16:00',
            status: 'planned',
            description: categorized.theory.slice(0, 200) || scraped.title,
            content,
            homework: categorized.homework,
            materials,
            tasks: categorized.tasks,
          });

          lessonNum++;

          // Notion API rate limit uchun kichik kutish
          await new Promise(resolve => setTimeout(resolve, 350));

        } catch (err: any) {
          const msg = `"${childPage.title}" sahifasini olib bo'lmadi: ${err.message}`;
          console.error(`  ❌ ${msg}`);
          errors.push(msg);
        }
      }
    } else {
      // Ichki sahifalar yo'q — asosiy sahifaning o'zini bitta dars sifatida olish
      const markdown = blocksToMarkdown(mainPage.blocks);
      const categorized = categorizeContent(markdown, mainPage.title);
      const files = extractFilesFromBlocks(mainPage.blocks);

      lessons.push({
        id: `les-scraped-1-${Date.now()}`,
        lessonNumber: 1,
        title: mainPage.title,
        date: '',
        time: '14:00 - 16:00',
        status: 'planned',
        description: categorized.theory.slice(0, 200) || mainPage.title,
        content: `### Dars Konspekti\n\n${categorized.theory || markdown}`,
        homework: categorized.homework,
        materials: files.map((f, idx) => ({
          id: `mat-scraped-1-${idx}`,
          name: f.name,
          type: (f.name.split('.').pop()?.toLowerCase() || 'link') as any,
          url: f.url,
        })),
        tasks: categorized.tasks,
      });
    }

    // 3. Darslarni raqam bo'yicha tartiblash
    lessons.sort((a, b) => a.lessonNumber - b.lessonNumber);

    // Dublikat raqamlarni to'g'irlash
    const seen = new Set<number>();
    for (const lesson of lessons) {
      while (seen.has(lesson.lessonNumber)) {
        lesson.lessonNumber++;
      }
      seen.add(lesson.lessonNumber);
    }

    const duration = Date.now() - startTime;
    console.log(`\n✅ Tayyor! ${lessons.length} ta dars olindi. Vaqt: ${(duration / 1000).toFixed(1)}s`);

    return { success: true, lessons, totalPages: mainPage.childPages.length || 1, errors, duration };

  } catch (err: any) {
    const duration = Date.now() - startTime;
    console.error('❌ Scraping xatoligi:', err.message);
    errors.push(err.message);
    return { success: false, lessons, totalPages: 0, errors, duration };
  }
};

// ============================================================
// 9. SAQLASH
// ============================================================
export const saveLessons = (lessons: Lesson[], mode: 'merge' | 'replace' = 'merge'): Lesson[] => {
  let existingLessons: Lesson[] = [];

  if (fs.existsSync(LESSONS_FILE)) {
    try {
      existingLessons = JSON.parse(fs.readFileSync(LESSONS_FILE, 'utf8'));
      // Backup yaratish
      fs.writeFileSync(BACKUP_FILE, JSON.stringify(existingLessons, null, 2), 'utf8');
      console.log('💾 Backup yaratildi.');
    } catch (err) {
      console.error('Backup xatoligi:', err);
    }
  }

  let finalLessons: Lesson[];

  if (mode === 'replace') {
    finalLessons = lessons;
  } else {
    // Merge — mavjud bo'lmaganlarnigina qo'shish
    finalLessons = [...existingLessons];
    for (const newLesson of lessons) {
      const exists = finalLessons.find(
        l => l.lessonNumber === newLesson.lessonNumber ||
             l.title.toLowerCase().trim() === newLesson.title.toLowerCase().trim()
      );
      if (exists) {
        // Yangilash
        Object.assign(exists, {
          ...newLesson,
          id: exists.id, // ID ni saqlab qolish
          status: exists.status, // Status o'zgarmaydi
        });
      } else {
        finalLessons.push(newLesson);
      }
    }
  }

  finalLessons.sort((a, b) => a.lessonNumber - b.lessonNumber);
  fs.writeFileSync(LESSONS_FILE, JSON.stringify(finalLessons, null, 2), 'utf8');
  console.log(`💾 ${finalLessons.length} ta dars saqlandi.`);

  return finalLessons;
};
