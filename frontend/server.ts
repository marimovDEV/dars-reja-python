import express from 'express';
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';
import { createServer } from 'http';
import { Server } from 'socket.io';
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

// Create HTTP server for Express + Socket.IO
const httpServer = createServer(app);
const io = new Server(httpServer, {
  cors: {
    origin: '*',
    methods: ['GET', 'POST']
  }
});

// In-Memory Live Quiz Arena Game State
interface Player {
  socketId: string;
  nickname: string;
  score: number;
  streak: number;
  lastAnswerIndex: number | null;
  lastAnswerTimeMs: number | null;
  lastPointsEarned: number;
}

interface GameSession {
  code: string;
  hostSocketId: string;
  quiz: any;
  status: 'lobby' | 'countdown' | 'question' | 'stats' | 'finished';
  currentQuestionIndex: number;
  players: Map<string, Player>; // key: socketId
  answersReceived: number;
  timerInterval?: any;
}

const gameSessions = new Map<string, GameSession>();

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
  
  if (!newLesson.title || !newLesson.date) {
    return res.status(400).json({ error: 'Title and Date are required' });
  }

  if (!newLesson.id) {
    newLesson.id = `les-${Date.now()}`;
  }
  
  lessons.push(newLesson);
  writeLessons(lessons);
  res.status(201).json(newLesson);
});

// PUT /api/lessons/:id - update a lesson
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

// PUT /api/lessons/:id/status - update status
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

// DELETE /api/lessons/:id - delete lesson
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
app.get('/api/notion/status', (req, res) => {
  const settings = getSettings();
  res.json(settings);
});

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

    const savedLessons = saveLessons(result.lessons, mode || 'merge');

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

// ============================================================================
// SOCKET.IO REAL-TIME QUIZ ARENA ENGINE
# ============================================================================

io.on('connection', (socket) => {
  console.log(`⚡ Client connected to Socket.IO: ${socket.id}`);

  // Host creates a session PIN
  socket.on('host:create-session', ({ code, quiz }) => {
    const session: GameSession = {
      code,
      hostSocketId: socket.id,
      quiz,
      status: 'lobby',
      currentQuestionIndex: 0,
      players: new Map(),
      answersReceived: 0
    };
    gameSessions.set(code, session);
    socket.join(code);
    socket.emit('host:session-created', { code, quiz });
    console.log(`🎮 Session created PIN: ${code} for Quiz: ${quiz.title}`);
  });

  // Player joins with code & nickname
  socket.on('player:join-session', ({ code, nickname }) => {
    const session = gameSessions.get(code);
    if (!session) {
      socket.emit('player:error', { message: 'Sessiya topilmadi yoki PIN kod noto\'g\'ri' });
      return;
    }
    if (session.status !== 'lobby') {
      socket.emit('player:error', { message: 'O\'yin allaqachon boshlangan' });
      return;
    }

    const player: Player = {
      socketId: socket.id,
      nickname,
      score: 0,
      streak: 0,
      lastAnswerIndex: null,
      lastAnswerTimeMs: null,
      lastPointsEarned: 0
    };

    session.players.set(socket.id, player);
    socket.join(code);

    socket.emit('player:joined', { code, nickname, sessionTitle: session.quiz.title });

    // Broadcast player list update to Host
    const playerList = Array.from(session.players.values()).map(p => ({
      socketId: p.socketId,
      nickname: p.nickname,
      score: p.score
    }));

    io.to(session.hostSocketId).emit('host:player-list-update', {
      players: playerList,
      totalCount: playerList.length
    });
  });

  // Host starts the game
  socket.on('host:start-game', ({ code }) => {
    const session = gameSessions.get(code);
    if (!session) return;

    session.status = 'countdown';
    session.currentQuestionIndex = 0;

    io.to(code).emit('game:countdown-start', { duration: 3 });

    setTimeout(() => {
      sendQuestionToAll(session);
    }, 3000);
  });

  // Helper to send current question
  function sendQuestionToAll(session: GameSession) {
    session.status = 'question';
    session.answersReceived = 0;

    // Reset player round answers
    session.players.forEach(p => {
      p.lastAnswerIndex = null;
      p.lastAnswerTimeMs = null;
      p.lastPointsEarned = 0;
    });

    const question = session.quiz.questions[session.currentQuestionIndex];
    if (!question) {
      finishGame(session);
      return;
    }

    const durationSec = question.durationSeconds || 20;

    // Send full details to Host
    io.to(session.hostSocketId).emit('host:question-started', {
      questionIndex: session.currentQuestionIndex,
      totalQuestions: session.quiz.questions.length,
      question,
      durationSec,
      totalPlayers: session.players.size
    });

    // Send question without showing correct answer to Players
    io.to(session.code).emit('player:question-started', {
      questionIndex: session.currentQuestionIndex,
      totalQuestions: session.quiz.questions.length,
      questionText: question.question,
      options: question.options,
      durationSec
    });
  }

  // Player submits answer
  socket.on('player:submit-answer', ({ code, optionIndex, responseTimeMs }) => {
    const session = gameSessions.get(code);
    if (!session || session.status !== 'question') return;

    const player = session.players.get(socket.id);
    if (!player || player.lastAnswerIndex !== null) return; // already answered

    const question = session.quiz.questions[session.currentQuestionIndex];
    const isCorrect = optionIndex === question.correctOptionIndex;

    player.lastAnswerIndex = optionIndex;
    player.lastAnswerTimeMs = responseTimeMs;

    // Points calculation
    let points = 0;
    if (isCorrect) {
      player.streak += 1;
      const basePoints = 1000;
      const durationSec = question.durationSeconds || 20;
      const timeFactor = Math.max(0, 1 - (responseTimeMs / (durationSec * 1000)));
      const timeBonus = Math.round(basePoints * 0.5 * timeFactor);
      
      let streakBonus = 0;
      if (player.streak >= 3) streakBonus = 500;
      else if (player.streak >= 2) streakBonus = 200;

      points = basePoints + timeBonus + streakBonus;
      player.score += points;
    } else {
      player.streak = 0;
    }

    player.lastPointsEarned = points;
    session.answersReceived += 1;

    socket.emit('player:answer-received', {
      isCorrect,
      pointsEarned: points,
      totalScore: player.score,
      streak: player.streak
    });

    // Notify Host of progress
    io.to(session.hostSocketId).emit('host:answer-received-update', {
      answersCount: session.answersReceived,
      totalPlayers: session.players.size
    });

    // If all players answered, close question early!
    if (session.answersReceived >= session.players.size) {
      closeQuestion(session);
    }
  });

  // Host manual or automatic close question
  socket.on('host:close-question', ({ code }) => {
    const session = gameSessions.get(code);
    if (session) closeQuestion(session);
  });

  function closeQuestion(session: GameSession) {
    if (session.status !== 'question') return;
    session.status = 'stats';

    const question = session.quiz.questions[session.currentQuestionIndex];

    // Compute option counts
    const optionCounts = [0, 0, 0, 0];
    session.players.forEach(p => {
      if (p.lastAnswerIndex !== null && p.lastAnswerIndex >= 0 && p.lastAnswerIndex < 4) {
        optionCounts[p.lastAnswerIndex] += 1;
      }
    });

    // Compute leaderboard (Top 5)
    const leaderboard = Array.from(session.players.values())
      .sort((a, b) => b.score - a.score)
      .map((p, idx) => ({
        rank: idx + 1,
        socketId: p.socketId,
        nickname: p.nickname,
        score: p.score,
        lastPoints: p.lastPointsEarned,
        streak: p.streak
      }));

    io.to(session.hostSocketId).emit('host:question-result', {
      questionIndex: session.currentQuestionIndex,
      correctOptionIndex: question.correctOptionIndex,
      explanation: question.explanation,
      optionCounts,
      leaderboard: leaderboard.slice(0, 5)
    });

    // Send rank feedback to individual players
    leaderboard.forEach((item) => {
      io.to(item.socketId).emit('player:round-summary', {
        rank: item.rank,
        score: item.score,
        pointsEarned: item.lastPoints,
        streak: item.streak
      });
    });
  }

  // Host moves to next question
  socket.on('host:next-question', ({ code }) => {
    const session = gameSessions.get(code);
    if (!session) return;

    session.currentQuestionIndex += 1;
    if (session.currentQuestionIndex >= session.quiz.questions.length) {
      finishGame(session);
    } else {
      sendQuestionToAll(session);
    }
  });

  function finishGame(session: GameSession) {
    session.status = 'finished';

    const finalLeaderboard = Array.from(session.players.values())
      .sort((a, b) => b.score - a.score)
      .map((p, idx) => ({
        rank: idx + 1,
        nickname: p.nickname,
        score: p.score
      }));

    io.to(session.code).emit('game:finished', {
      podium: finalLeaderboard.slice(0, 3),
      leaderboard: finalLeaderboard
    });
  }

  socket.on('disconnect', () => {
    console.log(`🔌 Client disconnected: ${socket.id}`);
  });
});

httpServer.listen(PORT, () => {
  console.log(`Backend server + Socket.IO is running at http://localhost:${PORT}`);
});
