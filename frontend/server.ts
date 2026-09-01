import express from 'express';
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';
import {
  getSettings,
  saveSettings,
  testConnection,
  getPreview,
  syncLessons
} from './src/notion/notionService';
import { scrapeNotionPage, saveLessons } from './src/notion/notionScraper';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const app = express();
const PORT = 5005;
const DATA_FILE = path.join(__dirname, 'src', 'data', 'lessons.json');

app.use(express.json());

// Enable CORS for development
app.use((req, res, next) => {
  res.header('Access-Control-Allow-Origin', '*');
  res.header('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, OPTIONS');
  res.header('Access-Control-Allow-Headers', 'Origin, X-Requested-With, Content-Type, Accept');
  if (req.method === 'OPTIONS') {
    return res.sendStatus(200);
  }
  next();
});

// Helper to read database
const readLessons = () => {
  try {
    if (!fs.existsSync(DATA_FILE)) {
      return [];
    }
    const data = fs.readFileSync(DATA_FILE, 'utf8');
    return JSON.parse(data);
  } catch (err) {
    console.error('Error reading database file:', err);
    return [];
  }
};

// Helper to write database
const writeLessons = (lessons: any[]) => {
  try {
    fs.writeFileSync(DATA_FILE, JSON.stringify(lessons, null, 2), 'utf8');
    return true;
  } catch (err) {
    console.error('Error writing database file:', err);
    return false;
  }
};

// GET /api/lessons - fetch all lessons
app.get('/api/lessons', (req, res) => {
  const lessons = readLessons();
  res.json(lessons);
});

// POST /api/lessons - create a new lesson
app.post('/api/lessons', (req, res) => {
  const lessons = readLessons();
  const newLesson = req.body;
  
  // Basic validation
  if (!newLesson.title || !newLesson.date) {
    return res.status(400).json({ error: 'Title and Date are required' });
  }

  // Ensure ID uniqueness
  if (!newLesson.id) {
    newLesson.id = `les-${Date.now()}`;
  }
  
  lessons.push(newLesson);
  writeLessons(lessons);
  res.status(201).json(newLesson);
});

// PUT /api/lessons/:id - update a lesson's full details
app.put('/api/lessons/:id', (req, res) => {
  const lessons = readLessons();
  const id = req.params.id;
  const updatedLesson = req.body;

  const index = lessons.findIndex((l: any) => l.id === id);
  if (index === -1) {
    return res.status(404).json({ error: 'Lesson not found' });
  }

  lessons[index] = { ...lessons[index], ...updatedLesson };
  writeLessons(lessons);
  res.json(lessons[index]);
});

// PUT /api/lessons/:id/status - update only the status
app.put('/api/lessons/:id/status', (req, res) => {
  const lessons = readLessons();
  const id = req.params.id;
  const { status } = req.body;

  if (!status) {
    return res.status(400).json({ error: 'Status is required' });
  }

  const index = lessons.findIndex((l: any) => l.id === id);
  if (index === -1) {
    return res.status(404).json({ error: 'Lesson not found' });
  }

  lessons[index].status = status;
  writeLessons(lessons);
  res.json(lessons[index]);
});

// DELETE /api/lessons/:id - delete a lesson
app.delete('/api/lessons/:id', (req, res) => {
  const lessons = readLessons();
  const id = req.params.id;

  const index = lessons.findIndex((l: any) => l.id === id);
  if (index === -1) {
    return res.status(404).json({ error: 'Lesson not found' });
  }

  const deleted = lessons.splice(index, 1);
  writeLessons(lessons);
  res.json({ message: 'Lesson deleted successfully', deleted: deleted[0] });
});

// --- NOTION SYNC API ENDPOINTS ---

// GET /api/notion/status - returns integration status
app.get('/api/notion/status', (req, res) => {
  const settings = getSettings();
  res.json(settings);
});

// POST /api/notion/test-connection - test notion url connection
app.post('/api/notion/test-connection', async (req, res) => {
  const { notionUrl } = req.body;
  if (!notionUrl) {
    return res.status(400).json({ error: 'Notion URL manzili talab etiladi.' });
  }

  try {
    const connInfo = await testConnection(notionUrl);
    res.json(connInfo);
  } catch (err: any) {
    res.status(500).json({ error: err.message || 'Ulanishda xatolik.' });
  }
});

// POST /api/notion/preview - fetch preview of changes
app.post('/api/notion/preview', async (req, res) => {
  const { notionUrl } = req.body;
  if (!notionUrl) {
    return res.status(400).json({ error: 'Notion URL manzili talab etiladi.' });
  }

  try {
    const previewData = await getPreview(notionUrl);
    res.json(previewData);
  } catch (err: any) {
    res.status(500).json({ error: err.message || 'Preview yuklashda xatolik.' });
  }
});

// POST /api/notion/sync - perform sync of lessons
app.post('/api/notion/sync', async (req, res) => {
  const { notionUrl, mode, previewData } = req.body;
  if (!notionUrl || !mode || !previewData) {
    return res.status(400).json({ error: 'Url, mode va previewData maydonlari talab etiladi.' });
  }

  try {
    const updatedLessons = await syncLessons(notionUrl, mode, previewData);
    res.json({ success: true, lessonsCount: updatedLessons.length });
  } catch (err: any) {
    res.status(500).json({ error: err.message || 'Sinxronlashda xatolik.' });
  }
});

// DELETE /api/notion/disconnect - reset settings
app.delete('/api/notion/disconnect', (req, res) => {
  const reset = saveSettings({
    notionUrl: '',
    sourceType: 'none',
    sourceName: ''
  });
  if (reset) {
    res.json({ success: true, message: 'Notion ulanishi muvaffaqiyatli uzildi.' });
  } else {
    res.status(500).json({ error: 'Sozlamalarni tozalab bo‘lmadi.' });
  }
});

// --- NOTION SCRAPER (Norasmiy API) ---

// POST /api/scrape - Notion sahifani scrape qilish
app.post('/api/scrape', async (req, res) => {
  const { notionUrl, mode } = req.body;
  if (!notionUrl) {
    return res.status(400).json({ error: 'Notion URL manzili talab etiladi.' });
  }

  try {
    console.log(`\n🚀 Scraping boshlandi: ${notionUrl}`);
    const result = await scrapeNotionPage(notionUrl);

    if (!result.success) {
      return res.status(500).json({
        error: 'Scraping muvaffaqiyatsiz tugadi.',
        errors: result.errors
      });
    }

    // Darslarni saqlash
    const savedLessons = saveLessons(result.lessons, mode || 'merge');

    // Sozlamalarni yangilash
    saveSettings({
      notionUrl,
      sourceType: 'page',
      sourceName: `Scraped (${result.lessons.length} dars)`,
      lastSyncTime: new Date().toLocaleString('uz-UZ'),
      lessonsSynced: result.lessons.length,
      documentsSynced: 0
    });

    res.json({
      success: true,
      lessonsCount: result.lessons.length,
      totalPages: result.totalPages,
      errors: result.errors,
      duration: result.duration
    });
  } catch (err: any) {
    console.error('Scrape API xatoligi:', err);
    res.status(500).json({ error: err.message || 'Scraping xatoligi.' });
  }
});

// Serve frontend build in production
const distPath = path.join(__dirname, 'dist');
if (fs.existsSync(distPath)) {
  app.use(express.static(distPath));
  app.get('*', (req, res) => {
    res.sendFile(path.join(distPath, 'index.html'));
  });
}

app.listen(PORT, () => {
  console.log(`Backend server is running at http://localhost:${PORT}`);
});
