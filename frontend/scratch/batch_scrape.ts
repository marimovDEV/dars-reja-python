// Barcha Notion sahifalarni batch scrape qilish
import { NotionAPI } from 'notion-client';
import dotenv from 'dotenv';
import path from 'path';
import fs from 'fs';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
dotenv.config({ path: path.join(__dirname, '..', '.env') });

const LESSONS_FILE = path.join(__dirname, '..', 'src', 'data', 'lessons.json');
const BACKUP_FILE = path.join(__dirname, '..', 'src', 'data', 'lessons.json.backup');

// ===== BARCHA URL'LAR =====
const URLS = [
  "https://app.notion.com/p/1-Dars-Python-Umumiy-Tushunchalari-va-Ishchi-Muhitni-Sozlash-3f69ce67fdb64ac296e765daae7b2455",
  "https://app.notion.com/p/2-Dars-Python-Sintaksisi-Kommentariya-va-O-zgaruvchilar-37cf8eae7de94d3c9d6be3ad8a4c3a46",
  "https://app.notion.com/p/3-Dars-Ma-lumot-Turlari-Data-Types-va-type-funksiyasi-9b87363145914ad3a8c0d340265243d5",
  "https://app.notion.com/p/4-Dars-Type-Casting-va-input-bilan-ishlash-ba896f06db5b41379985b832c06896c2",
  "https://app.notion.com/p/5-Dars-Python-Operatorlari-901df35f77fa44728cd1ca8962018dbb",
  "https://app.notion.com/p/6-Dars-Taqqoslash-Operatorlari-va-Shart-Operatorlari-if-elif-else-999bbe100069409da4ab81d15c46c951",
  "https://app.notion.com/p/7-Dars-Mantiqiy-Operatorlar-and-or-not-va-Murakkab-Shartlar-ef24495c197840e38bb913630c545e01",
  "https://app.notion.com/p/8-Dars-String-str-bo-yicha-Amallar-va-Metodlar-b740e0f01e7b46a59e4e729b46c45007",
  "https://app.notion.com/p/9-Dars-List-list-va-List-Amallari-11c60494b7534f3c915839780a20e26b",
  "https://app.notion.com/p/Dars-Math-List-va-String-amallari-Takrorlash-va-mustahkamlash-09d37ba2f14147b796faa35ad16fd423",
  "https://app.notion.com/p/1c94b8cd24df48dd90c2f7a9943df849",
  "https://app.notion.com/p/1-dars-366974cc61a980cf918ed9e714b024c5",
  "https://app.notion.com/p/2-dars-366974cc61a98044b537c12f1dee0474",
  "https://app.notion.com/p/3-dars-367974cc61a980f4b7ffff9e65c804b5",
  "https://app.notion.com/p/4-dars-367974cc61a98080804bdb26cab42aee",
  "https://app.notion.com/p/5-dars-367974cc61a980fca1d2c16b24afc08c",
  "https://app.notion.com/p/6-dars-367974cc61a98032a266d6c03f408f3e",
  "https://app.notion.com/p/7-dars-367974cc61a98040a89cc85a51f2a80f",
  "https://app.notion.com/p/8-dars-367974cc61a9806cb958caddc81a8237",
  "https://app.notion.com/p/list-367974cc61a9804fa47aeecc1f9dcd93",
  "https://app.notion.com/p/p-26-gmail-orqali-registratsiya-369974cc61a9806a88acd98a50b8f0b9",
  "https://app.notion.com/p/P27-Guruh-Aiogram-3-Routerlar-bilan-ishlash-369974cc61a9800bbc9befb0502f0818",
  "https://app.notion.com/p/p-28-django-templates-36a974cc61a9804ab5c6f0fc47268c19",
  "https://app.notion.com/p/p-26-36c974cc61a980989e64da73f224ff6e",
  "https://app.notion.com/p/p-26-Django-Gmail-orqali-tasdiqlash-Registratsiya-Login-va-Logout-To-liq-Qo-llanma-36c974cc61a9808fbe68df1905ba1409",
  "https://app.notion.com/p/p-28-36f974cc61a980c7bf2cc73ae454b114",
  "https://app.notion.com/p/Django-Loyihani-0-dan-yaratish-Models-va-CRUD-Amaliyoti-372974cc61a9800a97e8f679fbe79977",
  "https://app.notion.com/p/Django-REST-Framework-DRF-Noldan-API-yaratish-To-liq-Qo-llanma-373974cc61a98075b57ecec92ed61f74",
  "https://app.notion.com/p/p-29-dict-Python-Dictionary-Lug-at-Ma-lumotlar-bilan-ishlash-To-liq-Qo-llanma-373974cc61a9803e8995c323fea1e4db",
  "https://app.notion.com/p/Django-da-Xavfsizlik-Ro-yxatdan-o-tish-Login-va-Logout-tizimi-374974cc61a980f48dc8c0fd418b6745",
  "https://app.notion.com/p/Django-da-Xavfsizlik-login_required-orqali-saytni-himoyalash-374974cc61a9803eb169eb720aa6efce",
  "https://app.notion.com/p/Django-REST-Framework-DRF-POST-PUT-va-DELETE-To-liq-CRUD-amaliyoti-375974cc61a98028b15bd13878b2f1c9",
  "https://app.notion.com/p/Django-REST-Framework-Swagger-orqali-API-Dokumentatsiya-yaratish-375974cc61a98036a2bcea5309d1ae62",
  "https://app.notion.com/p/Django-REST-Framework-API-Xavfsizligi-va-Token-Authentication-377974cc61a980c1a0ddca43e35a1513",
  "https://app.notion.com/p/Python-da-JSON-fayllar-bilan-ishlash-O-quvchilar-uchun-qo-llanma-377974cc61a9800d93e4daa51a3f59d0",
  "https://app.notion.com/p/Ha-albatta-O-sha-ishlatiladigan-mijozning-kompyuterida-bu-3-ta-dastur-birinchi-marta-va-faqat-b-377974cc61a980b8b3c9d45cf42ad2ea",
  "https://app.notion.com/p/Django-Loyihasini-Serverga-Yuklash-Nginx-Gunicorn-SQLite-37a974cc61a9802997d9fb900b4b1f15",
  "https://app.notion.com/p/requests-Moduli-Bilan-Ishlash-Python-ni-Internetga-Ulash-To-liq-Qo-llanma-37a974cc61a9804b82ecf3619a392b32",
  "https://app.notion.com/p/Python-da-Terminal-va-Virtual-Muhit-venv-bilan-ishlash-37a974cc61a98014a2d8cb41306927d0",
  "https://app.notion.com/p/Django-Super-Dars-Noldan-Sayt-Yaratish-CRUD-Gmail-orqali-Tasdiqlash-37b974cc61a9806fb782c45b0a5d28f4",
  "https://app.notion.com/p/Sanalar-bilan-ishlash-va-Web-Scraping-Veb-saytlardan-ma-lumot-yig-ish-37c974cc61a9804d8607c4371da98a8a",
  "https://app.notion.com/p/Django-REST-Framework-DRF-API-Yaratish-Asoslari-37d974cc61a980ada869d24da24ac207",
  "https://app.notion.com/p/Python-da-Funksiyalar-def-Kodni-Qayta-Ishlatish-37e974cc61a9803faa2edb8384935d1e",
  "https://app.notion.com/p/MEGA-DARS-Django-da-0-dan-100-gacha-loyiha-HTML-CRUD-REST-API-380974cc61a980d6a5fedca9cd4a04a7",
  "https://app.notion.com/p/Regex-Muntazam-ifodalar-Matnlar-ichidan-xazina-qidirish-383974cc61a980ef91ecdb1950cba8ab",
  "https://app.notion.com/p/Rekursiv-va-Lambda-Funksiyalar-Qo-llanma-383974cc61a9805a9450e6fc67261734",
  "https://app.notion.com/p/1-qism-Lambda-Funksiyalar-bo-yicha-mashqlar-1-5-383974cc61a980fdb677cb2acf1f97af",
  "https://app.notion.com/p/Funksiyalar-bo-yicha-50-ta-Amaliy-Masalalar-To-plami-384974cc61a9809e9fc0f9ef08ad089c",
  "https://app.notion.com/p/Python-da-Funksiyalar-To-liq-va-Sodda-Qo-llanma-385974cc61a9807eb75fec68eb4da68d",
  "https://app.notion.com/p/Tashqi-API-lar-bilan-ishlash-Telegram-Bot-va-Django-ga-ulash-387974cc61a98000b498c1faaa931607",
  "https://app.notion.com/p/Django-REST-Framework-DRF-API-Yaratish-va-Uning-To-liq-Mantiqi-387974cc61a980068e04e3e689edb0c0",
  "https://app.notion.com/p/1-QISM-JWT-JSON-Web-Token-nima-va-u-nega-kerak-387974cc61a980ac94f3f02c3bd95d8e",
  "https://app.notion.com/p/MEGA-QO-LLANMA-Zamonaviy-Aqlli-Blog-API-Loyihasi-0-dan-100-gacha-389974cc61a9805793b9f3d3902eccdd",
  "https://app.notion.com/p/OOP-Obyektga-Yo-naltirilgan-Dasturlash-asoslari-1-dars-38a974cc61a98073b61cf2d6ec4df67d",
  "https://app.notion.com/p/OOP-Obyektga-Yo-naltirilgan-Dasturlash-2-dars-38c974cc61a98093a123ec666abe128f",
  "https://app.notion.com/p/Yakuniy-Loyihalar-Soddalashtirilgan-va-Osonlashtirilgan-variant-38c974cc61a980d98523feef965c60a6",
  "https://app.notion.com/p/OOP-Asoslari-bo-yicha-10-ta-Amaliy-Mashq-38c974cc61a980a4b892d83a6e724715",
  "https://app.notion.com/p/OOP-Asoslari-3-dars-Enkapsulatsiya-va-Polimorfizm-38f974cc61a9806eba21e255e28bb342",
  "https://app.notion.com/p/OOP-Amaliy-Mashqlar-Inkapsulyatsiya-va-Polimorfizm-38f974cc61a980138ee3f1fe0dd8e2cc",
  "https://app.notion.com/p/OOP-Asoslari-4-dars-Ichki-Sinflar-va-Sehrli-Metodlar-Yakuniy-dars-391974cc61a9808984bdd0eb46d61fcb",
  "https://app.notion.com/p/OOP-bo-yicha-Umumiy-Yakuniy-Mashqlar-20-ta-391974cc61a9801d9f47cc99b182acfd",
  "https://app.notion.com/p/Python-va-PostgreSQL-muhitini-o-rnatish-1-dars-393974cc61a9804eb436ca5d30684f45",
  "https://app.notion.com/p/Ma-lumotlar-Bazasi-Database-bilan-tanishuv-1-dars-SQLite-393974cc61a980f9a0acfb985b485880",
  "https://app.notion.com/p/Ma-lumotlar-Bazasi-SQLite-2-dars-Tahrirlash-O-chirish-va-Qidirish-396974cc61a980e7be59d5fed25581cc",
  "https://app.notion.com/p/PostgreSQL-va-Python-psycopg2-To-liq-CRUD-Amaliyoti-39f974cc61a980acb320fba6846303ad",
  "https://app.notion.com/p/Python-Dasturlash-Asoslari-To-liq-Qo-llanma-3a0974cc61a9807995b8d6dbd6ff53d5",
  "https://app.notion.com/p/Dars-Konspekti-PostgreSQL-Yakuniy-Dars-Internet-Do-kon-Arxitekturasi-3a1974cc61a98019b795e5d7d8071de8",
  "https://app.notion.com/p/PYTHON-STRING-MATN-METODLARI-TO-LIQ-QO-LLANMASI-3a4974cc61a980068271d94ca71e64a3",
  "https://app.notion.com/p/3-OYLIK-YAKUNIY-IMTIHON-3a4974cc61a9802fb25ce2732b048ffa",
  "https://app.notion.com/p/3a4974cc61a9803ba5f6f2d3c6fc38b8",
  "https://app.notion.com/p/4-OY-1-DARS-Aiogram-3-x-orqali-Telegram-Bot-yaratish-O-quvchi-qo-llanmasi-3a6974cc61a980fb9d2dcfcb42d8a1fa",
  "https://app.notion.com/p/O-QUVCHI-QO-LLANMASI-Aiogram-3-x-da-Tugmalar-Keyboard-3ab974cc61a9807cbbe4e85fbcb95b22",
  "https://app.notion.com/p/Aiogram-3-x-da-Botga-Xotira-berish-FSM-3ad974cc61a9802986fbd163f7c83bde",
  "https://app.notion.com/p/TO-LIQ-O-QUVCHI-QO-LLANMASI-Aiogram-botni-SQLite-bazasiga-ulash-va-Admin-Panel-yaratish-3af974cc61a980d4a1dce4d09556bf61",
  "https://app.notion.com/p/7-DARS-PYTHONDA-LIST-RO-YXAT-TO-LIQ-QO-LLANMA-3b2974cc61a98068b80fff19472a10a5",
  "https://app.notion.com/p/O-QUVCHI-QO-LLANMASI-Admindan-barchaga-xabar-tarqatish-Broadcasting-3b2974cc61a9802db04ce26fe901cfea",
  "https://app.notion.com/p/P-30-GURUHI-UCHUN-IMTIHON-SAVOLLARI-100-ball-3b4974cc61a9807bad74e993e885091e",
  "https://app.notion.com/p/TO-LIQ-O-QUVCHI-QO-LLANMASI-Guruhlarda-qoidabuzarlarni-jazolash-Ban-Mute-va-Unmute-3b4974cc61a9804193c8c2468bb66fe9",
  "https://app.notion.com/p/MEGA-LOYIHA-Aiogram-3-va-SQLite-To-liq-Dokumentatsiya-3b6974cc61a980e5bc5edee83ce374d1",
  "https://app.notion.com/p/3b6974cc61a980bd87e7c1b2d5d25a85",
  "https://app.notion.com/p/LIST-RO-YXAT-MAVZUSI-BO-YICHA-25-TA-MASALA-3b6974cc61a980cfac38e81716b55281",
  "https://app.notion.com/p/PYTHONDA-LIST-RO-YXAT-TO-LIQ-DOKUMENTATSIYA-3b6974cc61a98056af2ef0d05e7317bf",
  "https://app.notion.com/p/3bc974cc61a9804188a6d087752c03e7",
  "https://app.notion.com/p/3bc974cc61a9808790a2d10782dd7695",
  "https://app.notion.com/p/Telegram-Bot-Architecture-va-Message-bilan-ishlash-3bc974cc61a980b081d1edf88ebb4e67",
  "https://app.notion.com/p/6-DARS-Telegram-Mini-Shop-To-liq-CRUD-va-Rasm-yuborish-3bc974cc61a9803380e5c7dc60dddfe9",
  "https://app.notion.com/p/10-ta-sodda-masala-3bd974cc61a980a58f94f4f1cda60102",
  "https://app.notion.com/p/Uyga-vazifa-3bd974cc61a98040b371e9119321c533",
  "https://app.notion.com/p/Amaliyot-Telegram-Inspector-Bot-3be974cc61a980f28039fee69e65a736",
  "https://app.notion.com/p/P-29-2-DARS-3be974cc61a980f594fddd7c8d2f3b86",
  "https://app.notion.com/p/3be974cc61a980c1a4dff460c6be9ff1",
  "https://app.notion.com/p/P-30-Uyga-vazifa-3bf974cc61a980a897afd402c80289ff",
  "https://app.notion.com/p/P-29-BUGUNGI-DARS-3bf974cc61a980f8aff0efdc0924d679",
  "https://app.notion.com/p/if-else-elif-misollar-3c0974cc61a98038be56eb126c107d87",
  "https://app.notion.com/p/3c0974cc61a980179423e47c0918ab88",
  "https://app.notion.com/p/DICTIONARY-Lug-at-va-get-metodiga-oid-10-ta-masala-3c0974cc61a980998ee7cb762d79ed16",
  "https://app.notion.com/p/if-elif-el-3c0974cc61a980b39b27c934b77a1e3e",
  "https://app.notion.com/p/LIGI-Universal-Tarjimon-Bot-Google-Translate-Inline-Buttons-3c1974cc61a9805fb411d0dd705c8d6d",
  "https://app.notion.com/p/P-30-Dictionary-20-ta-masala-3c2974cc61a98041acc3d9d76a0f2737",
  "https://app.notion.com/p/Python-da-for-sikli-Loop-3c2974cc61a980f584ddd3d10073ab55",
  "https://app.notion.com/p/Oson-daraja-Yagona-for-sikli-va-range-3c2974cc61a9809ab25fdeea17068846",
  "https://app.notion.com/p/for-3c2974cc61a9800cad28ef23bfee7972",
  "https://app.notion.com/p/dict-3c2974cc61a980909eb8d8f785d550c2",
  "https://app.notion.com/p/3c4974cc61a98055850fc33530d52054",
  "https://app.notion.com/p/Python-random-Dars-dokumentatsiyasi-3c4974cc61a980a1a72bfa49c7d83952",
  "https://app.notion.com/p/Python-datetime-Dars-dokumentatsiyasi-3c4974cc61a980389109ecd38fec9421",
  "https://app.notion.com/p/Python-str-string-metodlari-bo-yicha-qisqa-qo-llanma-3c4974cc61a9805eb837e62b003bd25d",
  "https://app.notion.com/p/String-bilan-ishlash-bo-yicha-aralash-30-ta-masala-3c5974cc61a980669f2ce1ae40b16aac",
  "https://app.notion.com/p/Telegram-Botni-Serverga-Deploy-qilish-3c6974cc61a9804896d5dde09bdc9266",
  "https://app.notion.com/p/HTML-1-DARS-3c6974cc61a98052b936ee274a5edab8",
  "https://app.notion.com/p/Python-da-fayllar-bilan-ishlash-3c7974cc61a980f79ecbd8968038d804",
  "https://app.notion.com/p/Uyga-vazifa-Python-Fayllar-bilan-ishlash-3c7974cc61a9807eb060d7b8263de602",
  "https://app.notion.com/p/P-29-HTML-uyga-vazifa-3c7974cc61a98022b6fbfe37b75d4f93",
  "https://app.notion.com/p/P-29-CSS-3c8974cc61a9805abee6ce425b102395",
  "https://app.notion.com/p/3c9974cc61a98010b5b9e9155aea5679",
  "https://app.notion.com/p/DJANGO-1-3ca974cc61a980288b71c12b74091ea2",
  "https://app.notion.com/p/Function-20-ta-masala-3cb974cc61a980dfb8e4d9069d7a13a1",
  "https://app.notion.com/p/2d1974cc61a98068aa61e3b9dcc929dc",
];

// ===== HELPER FUNCTIONS =====
const extractPageId = (url: string): string => {
  const cleaned = url.split('?')[0].split('#')[0];
  const match = cleaned.match(/([a-f0-9]{32})/i);
  if (match) return match[1];
  const uuidMatch = cleaned.match(/([a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12})/i);
  if (uuidMatch) return uuidMatch[1].replace(/-/g, '');
  const segments = cleaned.split('/').filter(Boolean);
  const last = segments[segments.length - 1] || '';
  const parts = last.split('-');
  const lastPart = parts[parts.length - 1];
  if (lastPart && /^[a-f0-9]{32}$/i.test(lastPart)) return lastPart;
  throw new Error(`ID ajratib bo'lmadi: ${url}`);
};

const extractTextFromValue = (value: any): string => {
  if (!value) return '';
  if (Array.isArray(value)) {
    return value.map((segment: any) => {
      if (Array.isArray(segment)) return segment[0] || '';
      return String(segment);
    }).join('');
  }
  return String(value);
};

const getBlockValue = (blockMap: any, blockId: string): any => {
  const entry = blockMap.block?.[blockId];
  if (!entry) return null;
  if (entry.value?.value) return entry.value.value;
  if (entry.value) return entry.value;
  return entry;
};

const getRichText = (blockData: any): string => {
  if (!blockData) return '';
  const props = blockData.properties;
  if (!props) return '';
  if (props.title) return extractTextFromValue(props.title);
  if (props.caption) return extractTextFromValue(props.caption);
  return '';
};

// ===== BLOCK → MARKDOWN =====
interface SimpleBlock {
  type: string;
  text: string;
  language?: string;
  checked?: boolean;
  fileUrl?: string;
  children: SimpleBlock[];
}

const parseBlockSimple = (blockId: string, blockMap: any): SimpleBlock => {
  const bd = getBlockValue(blockMap, blockId);
  if (!bd) return { type: 'unknown', text: '', children: [] };

  const type = bd.type || 'text';
  const text = getRichText(bd);
  const block: SimpleBlock = { type, text, children: [] };

  if (type === 'code') block.language = bd.properties?.language?.[0]?.[0] || 'python';
  if (type === 'to_do') block.checked = bd.properties?.checked?.[0]?.[0] === 'Yes';
  if (['image', 'file', 'pdf', 'video'].includes(type)) {
    const src = bd.properties?.source;
    if (src) block.fileUrl = extractTextFromValue(src);
    if (bd.format?.display_source) block.fileUrl = bd.format.display_source;
  }

  const childIds: string[] = bd.content || [];
  for (const cid of childIds) {
    block.children.push(parseBlockSimple(cid, blockMap));
  }
  return block;
};

const blockToMd = (b: SimpleBlock, indent = 0): string => {
  const pfx = '  '.repeat(indent);
  const lines: string[] = [];

  switch (b.type) {
    case 'header': lines.push(`\n# ${b.text}`); break;
    case 'sub_header': lines.push(`\n## ${b.text}`); break;
    case 'sub_sub_header': lines.push(`\n### ${b.text}`); break;
    case 'text': lines.push(b.text ? `${pfx}${b.text}` : ''); break;
    case 'bulleted_list': lines.push(`${pfx}- ${b.text}`); break;
    case 'numbered_list': lines.push(`${pfx}1. ${b.text}`); break;
    case 'to_do': lines.push(`${pfx}- [${b.checked ? 'x' : ' '}] ${b.text}`); break;
    case 'code': lines.push(`\n\`\`\`${b.language || ''}\n${b.text}\n\`\`\``); break;
    case 'quote': lines.push(`${pfx}> ${b.text}`); break;
    case 'callout': lines.push(`${pfx}> 💡 ${b.text}`); break;
    case 'divider': lines.push('\n---\n'); break;
    case 'toggle':
      lines.push(`\n**${b.text}**`);
      b.children.forEach(c => lines.push(blockToMd(c, indent)));
      return lines.join('\n');
    case 'image': lines.push(`\n![rasm](${b.fileUrl || ''})\n`); break;
    case 'file': case 'pdf': lines.push(`📎 [${b.text || 'fayl'}](${b.fileUrl || ''})`); break;
    default: if (b.text) lines.push(`${pfx}${b.text}`);
  }

  if (b.type !== 'toggle') {
    b.children.forEach(c => lines.push(blockToMd(c, indent + 1)));
  }
  return lines.join('\n');
};

// ===== MAIN BATCH SCRAPER =====
const notion = new NotionAPI({ authToken: process.env.NOTION_TOKEN_V2 || '' });

interface LessonResult {
  lessonNumber: number;
  title: string;
  content: string;
  homework: string;
  tasks: any[];
  materials: any[];
  status: string;
}

const scrapePage = async (url: string, index: number): Promise<LessonResult | null> => {
  try {
    const pageId = extractPageId(url);
    const recordMap = await notion.getPage(pageId);
    const blockIds = Object.keys(recordMap.block || {});
    if (blockIds.length === 0) return null;

    const pageBlock = getBlockValue(recordMap, blockIds[0]);
    const title = getRichText(pageBlock) || `${index + 1}-dars`;
    const contentIds: string[] = pageBlock?.content || [];

    // Parse blocks to markdown
    const blocks = contentIds
      .map(cid => parseBlockSimple(cid, recordMap))
      .filter(b => b.type !== 'unknown');
    
    const markdown = blocks.map(b => blockToMd(b)).join('\n');

    // Detect homework
    const lines = markdown.split('\n');
    let hwLines: string[] = [];
    let inHw = false;
    for (const line of lines) {
      const low = line.toLowerCase().trim();
      if (low.includes('uyga vazifa') || low.includes('homework') || low.includes('vazifa')) {
        inHw = true;
        continue;
      }
      if (inHw && (low.startsWith('# ') || low.startsWith('## '))) {
        inHw = false;
      }
      if (inHw && line.trim()) {
        hwLines.push(line);
      }
    }

    // Detect lesson number from title
    const numMatch = title.match(/(\d+)/);
    const num = numMatch ? parseInt(numMatch[1], 10) : index + 1;

    return {
      lessonNumber: num,
      title: title.replace(/^\d+[-–.\s]*(dars|DARS)?\s*[-–:.\s]*/i, '').trim() || title,
      content: `### Dars Konspekti\n\n${markdown}`,
      homework: hwLines.join('\n').trim() || 'Berilmagan.',
      tasks: [],
      materials: [],
      status: 'planned',
    };
  } catch (err: any) {
    return null;
  }
};

// ===== RUN =====
console.log(`\n🚀 BATCH SCRAPING BOSHLANDI`);
console.log(`📋 Jami sahifalar: ${URLS.length}\n`);

const startTime = Date.now();
const results: LessonResult[] = [];
const errors: string[] = [];

for (let i = 0; i < URLS.length; i++) {
  const url = URLS[i];
  const shortName = url.split('/p/')[1]?.split('?')[0]?.slice(0, 50) || url;
  
  process.stdout.write(`  [${i + 1}/${URLS.length}] ${shortName}...`);

  try {
    const result = await scrapePage(url, i);
    if (result) {
      results.push(result);
      console.log(` ✅ "${result.title.slice(0, 40)}"`);
    } else {
      console.log(` ⚠️ Bo'sh sahifa`);
      errors.push(`Bo'sh: ${shortName}`);
    }
  } catch (err: any) {
    console.log(` ❌ ${err.message}`);
    errors.push(`Xato: ${shortName} — ${err.message}`);
  }

  // Rate limiting — 400ms kutish
  await new Promise(r => setTimeout(r, 400));
}

// Sort by lesson number
results.sort((a, b) => a.lessonNumber - b.lessonNumber);

// Fix duplicate lesson numbers
const seen = new Set<number>();
let nextNum = 1;
for (const r of results) {
  if (seen.has(r.lessonNumber)) {
    while (seen.has(nextNum)) nextNum++;
    r.lessonNumber = nextNum;
  }
  seen.add(r.lessonNumber);
  nextNum = r.lessonNumber + 1;
}

// Convert to Lesson format
const lessons = results.map(r => ({
  id: `les-notion-${r.lessonNumber}-${Date.now()}`,
  lessonNumber: r.lessonNumber,
  title: r.title,
  date: '',
  time: '14:00 - 16:00',
  status: r.status,
  description: r.title,
  content: r.content,
  homework: r.homework,
  materials: r.materials,
  tasks: r.tasks,
}));

// Backup existing
if (fs.existsSync(LESSONS_FILE)) {
  fs.copyFileSync(LESSONS_FILE, BACKUP_FILE);
  console.log('\n💾 Mavjud darslar backup qilindi.');
}

// Save
fs.writeFileSync(LESSONS_FILE, JSON.stringify(lessons, null, 2), 'utf8');

const duration = ((Date.now() - startTime) / 1000).toFixed(1);
console.log(`\n${'='.repeat(50)}`);
console.log(`✅ TAYYOR!`);
console.log(`📚 ${lessons.length} ta dars muvaffaqiyatli olindi`);
console.log(`❌ ${errors.length} ta xato`);
console.log(`⏱  Umumiy vaqt: ${duration} soniya`);
console.log(`💾 Saqlandi: ${LESSONS_FILE}`);
console.log(`${'='.repeat(50)}\n`);

if (errors.length > 0) {
  console.log('Xatolar:');
  errors.forEach(e => console.log(`  - ${e}`));
}
