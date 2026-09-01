// Notion sahifasini xom ko'rinishda tekshirish
import { NotionAPI } from 'notion-client';
import dotenv from 'dotenv';
import path from 'path';
import fs from 'fs';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
dotenv.config({ path: path.join(__dirname, '..', '.env') });

const notion = new NotionAPI({ authToken: process.env.NOTION_TOKEN_V2 || '' });
const pageId = '369974cc61a9800bbc9befb0502f0818';

console.log(`🔍 Sahifa yuklanmoqda...\n`);

try {
  const recordMap = await notion.getPage(pageId);
  
  // RecordMap'ning asosiy kalitlarini ko'rsatish
  console.log('RecordMap top-level keys:', Object.keys(recordMap));
  
  // Birinchi 3 ta blokni to'liq ko'rsatish
  const blockIds = Object.keys(recordMap.block || {});
  console.log(`\nJami bloklar: ${blockIds.length}`);
  
  for (let i = 0; i < Math.min(5, blockIds.length); i++) {
    const bid = blockIds[i];
    const block = recordMap.block[bid];
    console.log(`\n--- Block ${i} (${bid.slice(0,12)}...) ---`);
    console.log(JSON.stringify(block, null, 2).slice(0, 800));
  }

  // JSON faylga saqlash
  const outPath = path.join(__dirname, 'notion_raw_dump.json');
  // Faqat birinchi 20 blokni saqlash (hajm uchun)
  const subset: any = { block: {} };
  for (let i = 0; i < Math.min(20, blockIds.length); i++) {
    subset.block[blockIds[i]] = recordMap.block[blockIds[i]];
  }
  fs.writeFileSync(outPath, JSON.stringify(subset, null, 2), 'utf8');
  console.log(`\n📁 Xom ma'lumot saqlandi: ${outPath}`);

} catch (err: any) {
  console.error('❌ Xatolik:', err.message);
  console.error(err);
}
