import React, { useState, useEffect } from 'react';
import { io, Socket } from 'socket.io-client';
import confetti from 'canvas-confetti';
import { quizAudio } from '../../services/QuizAudioService';
import { Users, Play, ArrowRight, Trophy, Volume2, VolumeX, CheckCircle2, Clock, Sparkles } from 'lucide-react';
import { Quiz } from '../../types/quiz';

interface QuizHostViewProps {
  quiz: Quiz;
  onExit: () => void;
}

export function QuizHostView({ quiz, onExit }: QuizHostViewProps) {
  const [socket, setSocket] = useState<Socket | null>(null);
  const [sessionCode, setSessionCode] = useState<string>('');
  const [gameState, setGameState] = useState<'lobby' | 'countdown' | 'question' | 'stats' | 'finished'>('lobby');
  const [players, setPlayers] = useState<{ socketId: string; nickname: string; score: number }[]>([]);
  
  const [countdown, setCountdown] = useState<number>(3);
  const [currentQuestionIndex, setCurrentQuestionIndex] = useState<number>(0);
  const [currentQuestion, setCurrentQuestion] = useState<any>(null);
  const [timerLeft, setTimerLeft] = useState<number>(20);
  const [answersCount, setAnswersCount] = useState<number>(0);

  // Result stats
  const [optionCounts, setOptionCounts] = useState<number[]>([0, 0, 0, 0]);
  const [leaderboard, setLeaderboard] = useState<any[]>([]);
  const [finalPodium, setFinalPodium] = useState<any[]>([]);
  
  const [isMuted, setIsMuted] = useState<boolean>(false);

  useEffect(() => {
    // Generate 6 digit PIN
    const pin = Math.floor(100000 + Math.random() * 900000).toString();
    setSessionCode(pin);

    // Initialize Socket.IO connection
    const newSocket = io(window.location.origin, { transports: ['websocket', 'polling'] });
    setSocket(newSocket);

    newSocket.on('connect', () => {
      newSocket.emit('host:create-session', { code: pin, quiz });
    });

    newSocket.on('host:player-list-update', ({ players }) => {
      setPlayers(players);
      quizAudio.playCorrect(); // Small chime when player joins
    });

    newSocket.on('game:countdown-start', ({ duration }) => {
      setGameState('countdown');
      setCountdown(duration);
    });

    newSocket.on('host:question-started', ({ questionIndex, question, durationSec }) => {
      setGameState('question');
      setCurrentQuestionIndex(questionIndex);
      setCurrentQuestion(question);
      setTimerLeft(durationSec);
      setAnswersCount(0);
      quizAudio.playQuestionStart();
    });

    newSocket.on('host:answer-received-update', ({ answersCount }) => {
      setAnswersCount(answersCount);
    });

    newSocket.on('host:question-result', ({ correctOptionIndex, explanation, optionCounts, leaderboard }) => {
      setGameState('stats');
      setOptionCounts(optionCounts);
      setLeaderboard(leaderboard);
      quizAudio.playCorrect();
    });

    newSocket.on('game:finished', ({ podium, leaderboard }) => {
      setGameState('finished');
      setFinalPodium(podium);
      setLeaderboard(leaderboard);
      quizAudio.playFanfare();

      // Trigger Confetti!
      try {
        confetti({
          particleCount: 150,
          spread: 80,
          origin: { y: 0.6 }
        });
      } catch (e) {}
    });

    return () => {
      newSocket.disconnect();
    };
  }, []);

  // 3-2-1 Countdown timer tick
  useEffect(() => {
    if (gameState === 'countdown' && countdown > 0) {
      const timer = setTimeout(() => {
        quizAudio.playTick();
        setCountdown(prev => prev - 1);
      }, 1000);
      return () => clearTimeout(timer);
    }
  }, [gameState, countdown]);

  // Question countdown timer tick
  useEffect(() => {
    if (gameState === 'question' && timerLeft > 0) {
      const timer = setTimeout(() => {
        if (timerLeft <= 5) quizAudio.playTick();
        setTimerLeft(prev => prev - 1);
      }, 1000);
      return () => clearTimeout(timer);
    } else if (gameState === 'question' && timerLeft === 0 && socket) {
      socket.emit('host:close-question', { code: sessionCode });
    }
  }, [gameState, timerLeft]);

  const toggleMute = () => {
    const next = !isMuted;
    setIsMuted(next);
    quizAudio.setMuted(next);
  };

  const handleStartGame = () => {
    if (socket && sessionCode) {
      socket.emit('host:start-game', { code: sessionCode });
    }
  };

  const handleNextQuestion = () => {
    if (socket && sessionCode) {
      socket.emit('host:next-question', { code: sessionCode });
    }
  };

  const colors = [
    { bg: 'bg-rose-500 hover:bg-rose-600', border: 'border-rose-600', text: 'text-white', shape: '🔺' },
    { bg: 'bg-blue-600 hover:bg-blue-700', border: 'border-blue-700', text: 'text-white', shape: '🟦' },
    { bg: 'bg-amber-500 hover:bg-amber-600', border: 'border-amber-600', text: 'text-white', shape: '🟡' },
    { bg: 'bg-emerald-600 hover:bg-emerald-700', border: 'border-emerald-700', text: 'text-white', shape: '🟢' }
  ];

  return (
    <div className="min-h-screen bg-slate-950 text-white flex flex-col justify-between font-sans select-none overflow-hidden relative">
      
      {/* Top Navbar */}
      <div className="p-4 px-8 bg-slate-900/80 border-b border-slate-800 flex items-center justify-between z-20 backdrop-blur-md">
        <div className="flex items-center gap-3">
          <div className="w-10 h-10 rounded-2xl bg-gradient-to-tr from-purple-600 to-indigo-600 flex items-center justify-center font-black text-xl shadow-lg">
            🎮
          </div>
          <div>
            <h1 className="font-extrabold text-base tracking-tight text-white">{quiz.title}</h1>
            <p className="text-xs text-purple-300 font-semibold flex items-center gap-1">
              <Sparkles className="w-3 h-3 text-yellow-300" /> AI Quiz Arena Live
            </p>
          </div>
        </div>

        <div className="flex items-center gap-4">
          <button
            onClick={toggleMute}
            className="p-2.5 rounded-xl bg-slate-800 text-slate-300 hover:text-white transition"
          >
            {isMuted ? <VolumeX className="w-5 h-5 text-rose-400" /> : <Volume2 className="w-5 h-5 text-emerald-400" />}
          </button>
          
          <button
            onClick={onExit}
            className="px-4 py-2 bg-slate-800 hover:bg-rose-600 text-white text-xs font-bold rounded-xl transition"
          >
            Chiqish
          </button>
        </div>
      </div>

      {/* Main Dynamic Game Area */}
      <div className="flex-1 flex flex-col items-center justify-center p-6 relative z-10">
        
        {/* LOBBY STATE */}
        {gameState === 'lobby' && (
          <div className="text-center space-y-8 max-w-3xl w-full animate-fadeIn">
            {/* PIN Code Banner */}
            <div className="p-8 rounded-3xl bg-gradient-to-r from-purple-600 via-indigo-600 to-blue-600 shadow-2xl border border-white/20 text-center relative overflow-hidden">
              <div className="text-xs font-extrabold uppercase tracking-widest text-purple-200 mb-1">
                Telefon orqali qo'shilish uchun PIN kod
              </div>
              <div className="text-6xl md:text-7xl font-black tracking-widest text-yellow-300 drop-shadow-md my-2">
                {sessionCode || '...'}
              </div>
              <div className="text-xs font-semibold text-white/80">
                Manzil: <strong className="text-white underline">{window.location.host}</strong>
              </div>
            </div>

            {/* Players Count & Grid */}
            <div className="space-y-4">
              <div className="flex items-center justify-between text-sm font-bold text-slate-300 px-2">
                <span className="flex items-center gap-2">
                  <Users className="w-5 h-5 text-indigo-400" /> Qatnashchilar ({players.length})
                </span>
                {players.length === 0 && (
                  <span className="text-xs text-amber-400 font-semibold animate-pulse">
                    O'quvchilar PIN kodni kiritishini kuting...
                  </span>
                )}
              </div>

              <div className="grid grid-cols-2 md:grid-cols-4 gap-3 max-h-48 overflow-y-auto p-3 bg-slate-900/60 rounded-2xl border border-slate-800">
                {players.map((p, idx) => (
                  <div
                    key={p.socketId}
                    className="p-3 rounded-xl bg-purple-950/60 border border-purple-800/60 text-purple-200 text-xs font-bold flex items-center gap-2 animate-scaleUp"
                  >
                    <span className="w-6 h-6 rounded-full bg-purple-600 text-white text-[10px] flex items-center justify-center">
                      {idx + 1}
                    </span>
                    <span className="truncate">{p.nickname}</span>
                  </div>
                ))}
              </div>
            </div>

            {/* Start Button */}
            <button
              onClick={handleStartGame}
              disabled={players.length === 0}
              className="w-full py-4 bg-gradient-to-r from-emerald-500 to-teal-600 hover:from-emerald-600 hover:to-teal-700 text-white font-extrabold text-lg rounded-2xl shadow-xl transition disabled:opacity-50 flex items-center justify-center gap-3"
            >
              <Play className="w-6 h-6 fill-white" /> O'yinni Boshlash ({players.length} o'quvchi)
            </button>
          </div>
        )}

        {/* COUNTDOWN STATE */}
        {gameState === 'countdown' && (
          <div className="flex flex-col items-center justify-center text-center animate-scaleUp">
            <div className="text-91xl text-9xl font-black text-transparent bg-clip-text bg-gradient-to-r from-yellow-300 via-amber-400 to-rose-500 drop-shadow-2xl animate-bounce">
              {countdown > 0 ? countdown : 'GET READY!'}
            </div>
            <p className="text-xl font-bold text-purple-300 mt-4">O'yin boshlanmoqda...</p>
          </div>
        )}

        {/* QUESTION STATE */}
        {gameState === 'question' && currentQuestion && (
          <div className="w-full max-w-4xl space-y-8 animate-fadeIn">
            {/* Question Top Bar */}
            <div className="flex items-center justify-between text-xs font-bold text-slate-400">
              <span className="px-3 py-1 bg-purple-950 text-purple-300 rounded-full border border-purple-800">
                Savol {currentQuestionIndex + 1} / {quiz.questions.length}
              </span>

              {/* Timer ring */}
              <div className={`w-16 h-16 rounded-full border-4 flex items-center justify-center font-black text-xl shadow-lg ${
                timerLeft <= 5
                  ? 'border-rose-500 text-rose-500 animate-ping'
                  : 'border-indigo-500 text-indigo-400'
              }`}>
                {timerLeft}s
              </div>

              <span className="px-3 py-1 bg-blue-950 text-blue-300 rounded-full border border-blue-800">
                {answersCount} / {players.length} javob keldi
              </span>
            </div>

            {/* Question Title */}
            <div className="p-8 rounded-3xl bg-slate-900 border border-slate-800 shadow-2xl text-center">
              <h2 className="text-2xl md:text-3xl font-extrabold text-white leading-snug">
                {currentQuestion.question}
              </h2>
            </div>

            {/* 4 Choices Grid */}
            <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
              {currentQuestion.options.map((opt: string, idx: number) => {
                const col = colors[idx % colors.length];

                return (
                  <div
                    key={idx}
                    className={`p-5 rounded-2xl ${col.bg} border-b-4 ${col.border} text-white font-extrabold text-base flex items-center gap-4 shadow-lg transition transform hover:scale-[1.02]`}
                  >
                    <span className="text-2xl">{col.shape}</span>
                    <span className="flex-1">{opt}</span>
                  </div>
                );
              })}
            </div>
          </div>
        )}

        {/* STATS & RESULT STATE */}
        {gameState === 'stats' && currentQuestion && (
          <div className="w-full max-w-4xl space-y-6 animate-fadeIn">
            <h2 className="text-xl font-bold text-center text-white">
              {currentQuestion.question}
            </h2>

            {/* Bar Chart of Answers */}
            <div className="grid grid-cols-4 gap-4 items-end h-48 p-4 bg-slate-900 rounded-2xl border border-slate-800">
              {currentQuestion.options.map((opt: string, idx: number) => {
                const count = optionCounts[idx] || 0;
                const isCorrect = idx === currentQuestion.correctOptionIndex;
                const maxCount = Math.max(...optionCounts, 1);
                const heightPercent = Math.round((count / maxCount) * 100);

                return (
                  <div key={idx} className="flex flex-col items-center gap-2 h-full justify-end">
                    <span className="font-bold text-xs text-slate-300">{count} ta</span>
                    <div
                      className={`w-full rounded-t-xl transition-all duration-700 flex items-center justify-center font-bold text-xs ${
                        isCorrect ? 'bg-emerald-500 text-white' : 'bg-slate-700 text-slate-400'
                      }`}
                      style={{ height: `${Math.max(15, heightPercent)}%` }}
                    >
                      {isCorrect && '✓'}
                    </div>
                    <span className="text-[11px] font-semibold text-slate-400 truncate max-w-full">
                      {colors[idx].shape}
                    </span>
                  </div>
                );
              })}
            </div>

            {/* Explanation box */}
            {currentQuestion.explanation && (
              <div className="p-4 rounded-2xl bg-blue-950/60 border border-blue-800 text-blue-200 text-xs">
                💡 <strong>Tushuntirish:</strong> {currentQuestion.explanation}
              </div>
            )}

            {/* Top 5 Leaderboard Preview */}
            <div className="p-4 rounded-2xl bg-slate-900 border border-slate-800 space-y-2">
              <h3 className="text-xs font-extrabold uppercase text-purple-400 tracking-wider">
                🏆 Top-5 Reyting
              </h3>
              <div className="space-y-1.5">
                {leaderboard.map((item, idx) => (
                  <div
                    key={item.socketId}
                    className="p-2.5 rounded-xl bg-slate-800/70 border border-slate-700 flex items-center justify-between text-xs font-bold"
                  >
                    <span className="flex items-center gap-2">
                      <span className="w-5 h-5 rounded bg-purple-600 text-white flex items-center justify-center text-[10px]">
                        #{idx + 1}
                      </span>
                      <span>{item.nickname}</span>
                    </span>
                    <span className="text-yellow-400">{item.score} ball</span>
                  </div>
                ))}
              </div>
            </div>

            <button
              onClick={handleNextQuestion}
              className="w-full py-4 bg-gradient-to-r from-blue-600 to-indigo-600 hover:from-blue-700 hover:to-indigo-700 text-white font-extrabold text-base rounded-2xl shadow-xl transition flex items-center justify-center gap-2"
            >
              Keyingi Savol <ArrowRight className="w-5 h-5" />
            </button>
          </div>
        )}

        {/* FINISHED / PODIUM STATE */}
        {gameState === 'finished' && (
          <div className="w-full max-w-2xl text-center space-y-8 animate-scaleUp">
            <div className="inline-flex items-center gap-2 px-4 py-2 rounded-full bg-purple-900/60 border border-purple-700 text-yellow-300 font-extrabold text-sm">
              <Trophy className="w-5 h-5 text-yellow-400" /> O'YIN YAKUNLANDI!
            </div>

            {/* 3D Podium */}
            <div className="flex items-end justify-center gap-4 h-64">
              {/* 2nd Place */}
              {finalPodium[1] && (
                <div className="flex flex-col items-center flex-1 animate-fadeIn">
                  <div className="font-bold text-xs text-slate-300 mb-1">{finalPodium[1].nickname}</div>
                  <div className="text-xs text-yellow-400 font-semibold mb-2">{finalPodium[1].score} ball</div>
                  <div className="w-full h-40 bg-gradient-to-t from-slate-700 to-slate-500 rounded-t-2xl flex flex-col items-center justify-center font-black text-2xl shadow-xl">
                    🥈 2
                  </div>
                </div>
              )}

              {/* 1st Place */}
              {finalPodium[0] && (
                <div className="flex flex-col items-center flex-1 animate-fadeIn">
                  <div className="font-bold text-sm text-yellow-300 mb-1">{finalPodium[0].nickname}</div>
                  <div className="text-xs text-yellow-400 font-bold mb-2">{finalPodium[0].score} ball</div>
                  <div className="w-full h-52 bg-gradient-to-t from-yellow-500 to-amber-400 rounded-t-2xl flex flex-col items-center justify-center font-black text-3xl shadow-2xl text-amber-950">
                    👑 1
                  </div>
                </div>
              )}

              {/* 3rd Place */}
              {finalPodium[2] && (
                <div className="flex flex-col items-center flex-1 animate-fadeIn">
                  <div className="font-bold text-xs text-slate-300 mb-1">{finalPodium[2].nickname}</div>
                  <div className="text-xs text-yellow-400 font-semibold mb-2">{finalPodium[2].score} ball</div>
                  <div className="w-full h-32 bg-gradient-to-t from-amber-700 to-amber-600 rounded-t-2xl flex flex-col items-center justify-center font-black text-2xl shadow-lg">
                    🥉 3
                  </div>
                </div>
              )}
            </div>

            <button
              onClick={onExit}
              className="px-8 py-3.5 bg-gradient-to-r from-purple-600 to-indigo-600 hover:from-purple-700 text-white font-extrabold text-sm rounded-2xl shadow-xl transition"
            >
              Chiqish va Dars Rejasiga Qaytish
            </button>
          </div>
        )}

      </div>
    </div>
  );
}
