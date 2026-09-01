import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';
import { getNotionClient, isNotionTokenConfigured } from './notionClient';
import { parseDatabaseRow, parsePageBlocks } from './notionParser';
import { NotionSettings, NotionConnectionInfo, NotionPreviewResponse } from './notionTypes';
import { Lesson, LessonMaterial } from '../types';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const SETTINGS_FILE = path.join(__dirname, '..', 'data', 'settings.json');
const LESSONS_FILE = path.join(__dirname, '..', 'data', 'lessons.json');
const BACKUP_FILE = path.join(__dirname, '..', 'data', 'lessons.json.backup');

// Helpers for settings read/write
export const getSettings = (): NotionSettings => {
  try {
    if (!fs.existsSync(SETTINGS_FILE)) {
      return { notionUrl: '', sourceType: 'none', sourceName: '' };
    }
    const data = fs.readFileSync(SETTINGS_FILE, 'utf8');
    return JSON.parse(data);
  } catch (err) {
    console.error('Error reading settings:', err);
    return { notionUrl: '', sourceType: 'none', sourceName: '' };
  }
};

export const saveSettings = (settings: NotionSettings) => {
  try {
    fs.writeFileSync(SETTINGS_FILE, JSON.stringify(settings, null, 2), 'utf8');
    return true;
  } catch (err) {
    console.error('Error saving settings:', err);
    return false;
  }
};

// Extracts 32-character hex ID from Notion URL
export const extractNotionId = (url: string): string | null => {
  if (!url) return null;
  // Notion IDs are 32 chars hex
  const matches = url.match(/([a-f0-9]{32})/i);
  return matches ? matches[1] : null;
};

// Check connection using real Client or Mock client if token is not configured
export const testConnection = async (url: string): Promise<NotionConnectionInfo> => {
  const id = extractNotionId(url);
  if (!id) {
    throw new Error('Notion URL manzili noto‘g‘ri. Havolada 32 xonali ID bo‘lishi lozim.');
  }

  // MOCK Connection Fallback if token is not configured
  if (!isNotionTokenConfigured()) {
    console.log('Using Mock Notion Client (Test Connection)');
    const isDb = url.toLowerCase().includes('v=') || url.toLowerCase().includes('db') || url.toLowerCase().includes('database');
    return {
      success: true,
      sourceType: isDb ? 'database' : 'page',
      sourceName: isDb ? 'Python Kurs Rejasi (Notion Baza - MOCK)' : 'Kurs Rejasi Hujjatlari (Notion Sahifa - MOCK)'
    };
  }

  const client = getNotionClient() as any;
  if (!client) throw new Error('Notion Client initialization failed.');

  try {
    // 1. Try treating as Database
    try {
      const db = await client.databases.retrieve({ database_id: id }) as any;
      const title = db.title.map((t: any) => t.plain_text).join('');
      return { success: true, sourceType: 'database', sourceName: title || 'Notion Baza' };
    } catch (dbErr) {
      // 2. Fall back to Page
      const pg = await client.pages.retrieve({ page_id: id }) as any;
      const props = pg.properties as any;
      const title = props?.title?.title?.map((t: any) => t.plain_text).join('') || 
                    props?.Name?.title?.map((t: any) => t.plain_text).join('') || 
                    'Notion Sahifa';
      return { success: true, sourceType: 'page', sourceName: title };
    }
  } catch (err: any) {
    throw new Error(`Notion bilan ulanib bo‘lmadi: ${err.message || 'Soha ruxsatini va tokeningizni tekshiring.'}`);
  }
};

// Fetch preview data from database or page
export const getPreview = async (url: string): Promise<NotionPreviewResponse> => {
  const id = extractNotionId(url);
  if (!id) {
    throw new Error('Notion URL manzili noto‘g‘ri.');
  }

  // MOCK Preview Fallback
  if (!isNotionTokenConfigured()) {
    console.log('Using Mock Notion Client (Preview)');
    const lessons: Lesson[] = [];
    const isDb = url.toLowerCase().includes('v=') || url.toLowerCase().includes('db') || url.toLowerCase().includes('database');

    if (isDb) {
      // Load 5 sample lessons as demo parsed
      lessons.push(
        {
          id: 'mock-les-1',
          lessonNumber: 1,
          title: 'Notion: Kirish va O‘zgaruvchilar',
          date: '2026-09-01',
          time: '14:00 - 16:00',
          status: 'planned',
          description: 'Notion database orqali import qilingan dars.',
          content: '### Dars Konspekti\n\nNotion database orqali import qilingan dars.',
          homework: '10 turdagi o‘zgaruvchi yozing.',
          materials: [],
          tasks: []
        },
        {
          id: 'mock-les-2',
          lessonNumber: 2,
          title: 'Notion: Arifmetik Amallar',
          date: '2026-09-03',
          time: '14:00 - 16:00',
          status: 'planned',
          description: 'Notion database arifmetika darsi.',
          content: '### Dars Konspekti\n\nArifmetika darsi.',
          homework: 'Ikki son kalkulyatori yozing.',
          materials: [],
          tasks: []
        },
        {
          id: 'mock-les-12',
          lessonNumber: 12,
          title: '1-modul imtihoni (Notion)',
          date: '2026-09-25',
          time: '14:00 - 16:00',
          status: 'planned',
          description: 'Modul nazorati.',
          content: '### Imtihon Tafsilotlari\n\nModul nazorati.',
          homework: 'Takrorlash.',
          materials: [],
          tasks: []
        }
      );
    } else {
      // Page parser mock
      lessons.push(
        {
          id: 'mock-les-block-1',
          lessonNumber: 15,
          title: 'Notion Block: Dictionary asoslari',
          date: '',
          time: '14:00 - 16:00',
          status: 'planned',
          description: 'Lug‘at tushunchasi.',
          content: '### Dars Konspekti\n\nLug‘at tushunchasi.',
          homework: 'Lug‘at yaratish.',
          materials: [],
          tasks: []
        }
      );
    }

    return {
      success: true,
      summary: {
        lessonsFound: lessons.length,
        documentsFound: 2,
        warnings: ['Sana kiritilmagan darslar topildi.']
      },
      lessons,
      documents: [
        { id: 'mock-doc-1', name: 'python_lugat.pdf', type: 'pdf', url: 'https://notion.so/python_lugat.pdf' }
      ],
      warnings: ['Sana kiritilmagan darslar topildi.']
    };
  }

  const client = getNotionClient() as any;
  if (!client) throw new Error('Notion Client initialization failed.');

  const lessons: Lesson[] = [];
  const documents: LessonMaterial[] = [];
  const warnings: string[] = [];
  let sourceType: 'database' | 'page' = 'database';

  try {
    // 1. Try treating as Database
    try {
      const response = await client.databases.query({
        database_id: id,
        page_size: 100 // fetch first 100
      }) as any;
      
      response.results.forEach((page: any, idx: number) => {
        const { lesson, documents: lessonDocs } = parseDatabaseRow(page, idx);
        lessons.push(lesson);
        documents.push(...lessonDocs);
        if (!lesson.date) {
          warnings.push(`${lesson.lessonNumber}-dars uchun sana topilmadi`);
        }
      });
      sourceType = 'database';
    } catch (dbErr) {
      // 2. Treat as Page blocks
      const response = await client.blocks.children.list({
        block_id: id,
        page_size: 100
      }) as any;
      
      const parsed = parsePageBlocks(response.results);
      lessons.push(...parsed.lessons);
      documents.push(...parsed.documents);
      sourceType = 'page';
    }

    return {
      success: true,
      summary: {
        lessonsFound: lessons.length,
        documentsFound: documents.length,
        warnings
      },
      lessons,
      documents,
      warnings
    };
  } catch (err: any) {
    throw new Error(`Notion ma'lumotlarini yuklab bo'lmadi: ${err.message}`);
  }
};

// Sync database and page lessons with existing lessons.json
export const syncLessons = async (
  url: string,
  mode: 'merge' | 'replace',
  previewData: NotionPreviewResponse
): Promise<Lesson[]> => {
  // Read existing lessons
  let existingLessons: Lesson[] = [];
  if (fs.existsSync(LESSONS_FILE)) {
    try {
      existingLessons = JSON.parse(fs.readFileSync(LESSONS_FILE, 'utf8'));
      // Create backup
      fs.writeFileSync(BACKUP_FILE, JSON.stringify(existingLessons, null, 2), 'utf8');
      console.log('Database backup created at:', BACKUP_FILE);
    } catch (err) {
      console.error('Backup creation failed:', err);
    }
  }

  let finalLessons: Lesson[] = [];
  const incoming = previewData.lessons;

  if (mode === 'replace') {
    finalLessons = incoming;
  } else {
    // Merge mode
    finalLessons = [...existingLessons];
    incoming.forEach((newLes) => {
      const idx = finalLessons.findIndex((l) => l.lessonNumber === newLes.lessonNumber);
      if (idx !== -1) {
        // Overwrite
        finalLessons[idx] = { ...finalLessons[idx], ...newLes };
      } else {
        // Append
        finalLessons.push(newLes);
      }
    });
  }

  // Sort sequentially
  finalLessons.sort((a, b) => a.lessonNumber - b.lessonNumber);

  // Write lessons.json database
  fs.writeFileSync(LESSONS_FILE, JSON.stringify(finalLessons, null, 2), 'utf8');

  // Update Settings
  const settings = getSettings();
  const isDb = url.toLowerCase().includes('v=') || url.toLowerCase().includes('db') || url.toLowerCase().includes('database');
  
  saveSettings({
    notionUrl: url,
    sourceType: isDb ? 'database' : 'page',
    sourceName: previewData.summary.lessonsFound > 0 ? (isDb ? 'Notion Baza' : 'Notion Sahifa') : settings.sourceName,
    lastSyncTime: new Date().toLocaleString('uz-UZ'),
    lessonsSynced: previewData.summary.lessonsFound,
    documentsSynced: previewData.summary.documentsFound
  });

  return finalLessons;
};
