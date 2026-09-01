import React, { useState, useEffect } from 'react';
import { io, Socket } from 'socket.io-client';
import { quizAudio } from '../../services/QuizAudioService';
import { Flame, Trophy, Volume2, VolumeX, Send, Loader2, Sparkles, Gamepad2, ShieldCheck, Zap, CheckCircle2 } from 'lucide-react';
import { getSocketUrl } from '../../config/apiConfig';

interface QuizPlayerViewProps {
  onExit: () => void;
}

export const ARENA_PLAYER_BUTTONS = [
  { shape: '▲', color: '#e21b3c', hoverBg: 'hover:bg-[#c41432]', shadowColor: 'shadow-red-900/50', label: 'A' }, // Red Triangle
  { shape: '◆', color: '#1368ce', hoverBg: 'hover:bg-[#0f54a8]', shadowColor: 'shadow-blue-900/50', label: 'B' }, // Blue Diamond
  { shape: '●', color: '#d89e00', hoverBg: 'hover:bg-[#b58400]', shadowColor: 'shadow-amber-900/50', label: 'C' }, // Yellow Circle
  { shape: '■', color: '#26890c', hoverBg: 'hover:bg-[#1e6d09]', shadowColor: 'shadow-emerald-900/50', label: 'D' }  // Green Square
];

export function QuizPlayerView({ onExit }: QuizPlayerViewProps) {
  const [socket, setSocket] = useState<Socket | null>(null);
  const [pinCode, setPinCode] = useState<string>('');
  const [nickname, setNickname] = useState<string>('');
  const [avatar, setAvatar] = useState<{ emoji: string; name: string } | null>(null);
  const [error, setError] = useState<string | null>(null);

  const [gameState, setGameState] = useState<'join' | 'waiting' | 'question' | 'answered' | 'result' | 'finished'>('join');
  const [sessionTitle, setSessionTitle] = useState<string>('');
  
  const [questionIndex, setQuestionIndex] = useState<number>(0);
  const [totalQuestions, setTotalQuestions] = useState<number>(0);
  const [optionsCount, setOptionsCount] = useState<number>(4);
  const [timerLeft, setTimerLeft] = useState<number>(20);

  // Player round stats
  const [selectedOption, setSelectedOption] = useState<number | null>(null);
  const [isCorrect, setIsCorrect] = useState<boolean | null>(null);
  const [pointsEarned, setPointsEarned] = useState<number>(0);
  const [totalScore, setTotalScore] = useState<number>(0);
  const [streak, setStreak] = useState<number>(0);
  const [rank, setRank] = useState<number>(1);
  const [isMuted, setIsMuted] = useState<boolean>(false);

  const initSocketListeners = (sock: Socket) => {
    sock.on('player:joined', ({ code, nickname, avatar, sessionTitle, reconnected }) => {
      setGameState('waiting');
      setSessionTitle(sessionTitle);
      if (avatar) setAvatar(avatar);
      setError(null);
      quizAudio.playCorrect();
    });

    sock.on('player:error', ({ message }) => {
      setError(message);
    });

    sock.on('game:countdown-start', () => {
      setGameState('waiting');
    });

    sock.on('player:question-started', ({ questionIndex, totalQuestions, optionsCount, durationSec }) => {
      setGameState('question');
      setQuestionIndex(questionIndex);
      setTotalQuestions(totalQuestions);
      setOptionsCount(optionsCount || 4);
      setTimerLeft(durationSec);
      setSelectedOption(null);
      setIsCorrect(null);
      quizAudio.playQuestionStart();
    });

    sock.on('player:answer-received', ({ pointsEarned, totalScore, streak }) => {
      setGameState('answered');
    });

    sock.on('player:round-summary', ({ isCorrect, rank, score, pointsEarned, streak }) => {
      setGameState('result');
      setIsCorrect(isCorrect);
      setRank(rank);
      setTotalScore(score);
      setPointsEarned(pointsEarned);
      setStreak(streak);

      if (isCorrect) quizAudio.playCorrect();
      else quizAudio.playIncorrect();
    });

    sock.on('game:finished', ({ leaderboard }) => {
      setGameState('finished');
      const myInfo = leaderboard.find((p: any) => p.nickname === nickname);
      if (myInfo) setRank(myInfo.rank);
      quizAudio.playFanfare();
    });
  };

  useEffect(() => {
    const newSocket = io(getSocketUrl(), { transports: ['websocket', 'polling'] });
    setSocket(newSocket);
    initSocketListeners(newSocket);

    return () => {
      newSocket.disconnect();
    };
  }, [nickname]);

  // Question countdown
  useEffect(() => {
    if (gameState === 'question' && timerLeft > 0) {
      const timer = setTimeout(() => {
        if (timerLeft <= 5) quizAudio.playTick();
        setTimerLeft(prev => prev - 1);
      }, 1000);
      return () => clearTimeout(timer);
    }
  }, [gameState, timerLeft]);

  const handleJoin = (e: React.FormEvent) => {
    e.preventDefault();
    const cleanPin = pinCode.replace(/\s+/g, '').trim();
    const cleanName = nickname.trim();

    if (!cleanPin || !cleanName) {
      setError("PIN va Ismingizni kiriting");
      return;
    }

    setError(null);
    let activeSocket = socket;
    if (!activeSocket || !activeSocket.connected) {
      activeSocket = io(getSocketUrl(), { transports: ['websocket', 'polling'] });
      setSocket(activeSocket);
      initSocketListeners(activeSocket);
    }

    activeSocket.emit('player:join-session', { code: cleanPin, nickname: cleanName });
  };

  const handleSubmitAnswer = (optionIdx: number) => {
    if (selectedOption !== null || !socket) return;
    setSelectedOption(optionIdx);
    quizAudio.playTick();

    const cleanPin = pinCode.replace(/\s+/g, '').trim();
    socket.emit('player:submit-answer', { code: cleanPin, optionIndex: optionIdx });
  };

  const toggleMute = () => {
    const next = !isMuted;
    setIsMuted(next);
    quizAudio.setMuted(next);
  };

  return (
    <div className="min-h-screen bg-slate-950 text-white flex flex-col justify-between font-sans select-none overflow-hidden relative">
      
      {/* 🌟 Dynamic Animated Floating Background Orbs & Shapes */}
      <div className="absolute -top-32 -left-32 w-96 h-96 bg-purple-600/25 rounded-full blur-3xl pointer-events-none animate-pulse duration-1000" />
      <div className="absolute top-1/3 -right-32 w-96 h-96 bg-indigo-600/20 rounded-full blur-3xl pointer-events-none animate-pulse duration-700" />
      <div className="absolute -bottom-32 left-1/4 w-96 h-96 bg-rose-600/15 rounded-full blur-3xl pointer-events-none" />

      {/* Floating 3D Translucent Shapes */}
      <div className="absolute top-20 left-10 text-4xl text-rose-500/20 animate-bounce duration-1000 pointer-events-none">▲</div>
      <div className="absolute top-40 right-16 text-5xl text-blue-500/20 animate-bounce duration-700 pointer-events-none">◆</div>
      <div className="absolute bottom-24 left-16 text-4xl text-amber-500/20 animate-bounce duration-1000 pointer-events-none">●</div>
      <div className="absolute bottom-32 right-12 text-5xl text-emerald-500/20 animate-bounce duration-700 pointer-events-none">■</div>

      {/* Top Navbar */}
      <header className="p-4 px-6 md:px-12 flex items-center justify-between border-b border-slate-800/80 bg-slate-900/40 backdrop-blur-md relative z-20">
        <div className="flex items-center gap-3">
          <div className="w-10 h-10 rounded-2xl bg-gradient-to-tr from-purple-600 to-indigo-600 flex items-center justify-center font-black text-xl shadow-lg shadow-purple-900/40 animate-pulse">
            🎮
          </div>
          <div>
            <span className="font-extrabold text-base tracking-tight text-white flex items-center gap-2">
              Marimov Game Zone
              {avatar && (
                <span className="px-2 py-0.5 rounded-full text-xs font-black bg-purple-950 text-yellow-300 border border-purple-800 flex items-center gap-1">
                  {avatar.emoji} {avatar.name}
                </span>
              )}
            </span>
          </div>
        </div>

        <div className="flex items-center gap-3">
          <button onClick={toggleMute} className="p-2.5 rounded-xl bg-slate-800/80 hover:bg-slate-700 border border-slate-700 text-slate-300 transition cursor-pointer">
            {isMuted ? <VolumeX className="w-4 h-4 text-rose-400" /> : <Volume2 className="w-4 h-4 text-emerald-400" />}
          </button>
        </div>
      </header>

      {/* Main Responsive Body */}
      <main className="flex-1 flex flex-col items-center justify-center p-4 md:p-8 relative z-10 w-full max-w-5xl mx-auto">
        
        {/* 1. JOIN FORM STATE */}
        {gameState === 'join' && (
          <div className="w-full grid grid-cols-1 md:grid-cols-12 gap-8 items-center animate-scaleUp">
            
            {/* Desktop Left Welcome Hero Banner */}
            <div className="hidden md:flex md:col-span-6 flex-col text-left space-y-4 pr-4">
              <div className="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full bg-purple-950/80 border border-purple-800 text-purple-300 text-xs font-extrabold w-fit">
                <Sparkles className="w-4 h-4 text-yellow-400" /> Jonli Interaktiv Quiz Arena
              </div>

              <h2 className="text-4xl lg:text-5xl font-black text-transparent bg-clip-text bg-gradient-to-r from-white via-slate-100 to-purple-300 leading-tight">
                Bilimingizni Jonli O'yinda Sinang!
              </h2>

              <p className="text-slate-400 text-xs lg:text-sm leading-relaxed font-medium">
                O'qituvchingiz ko'rsatgan PIN kod va o'zingizning nikneymingizni kiriting va do'stlaringiz bilan jonli musobaqalashing!
              </p>

              <div className="flex items-center gap-6 pt-2 text-xs font-bold text-slate-300">
                <span className="flex items-center gap-2">
                  <Zap className="w-4 h-4 text-yellow-400" /> Tezkor Taymer
                </span>
                <span className="flex items-center gap-2">
                  <Flame className="w-4 h-4 text-amber-500" /> Streak Bonusi
                </span>
                <span className="flex items-center gap-2">
                  <Trophy className="w-4 h-4 text-emerald-400" /> Reyting
                </span>
              </div>
            </div>

            {/* Right Join Form Card */}
            <div className="md:col-span-6 w-full max-w-md mx-auto">
              <form onSubmit={handleJoin} className="p-8 bg-slate-900/90 rounded-3xl border border-slate-800/90 shadow-2xl space-y-5 backdrop-blur-xl relative overflow-hidden">
                
                <div className="text-center space-y-1">
                  <div className="w-14 h-14 rounded-2xl bg-gradient-to-tr from-purple-600 to-indigo-600 flex items-center justify-center text-3xl mx-auto shadow-lg mb-3">
                    <Gamepad2 className="w-7 h-7 text-white" />
                  </div>
                  <h3 className="text-2xl font-black text-white">Quizga Qo'shilish</h3>
                  <p className="text-xs text-slate-400">O'qituvchi ekranidagi PIN kodni kiriting</p>
                </div>

                {error && (
                  <div className="p-3.5 bg-rose-950/70 border border-rose-800 text-rose-300 rounded-2xl text-xs font-semibold animate-shake">
                    ⚠️ {error}
                  </div>
                )}

                <div className="space-y-1.5 text-left">
                  <label className="block text-xs font-extrabold uppercase text-slate-400 tracking-wider">PIN KOD</label>
                  <input
                    type="text"
                    maxLength={8}
                    placeholder="849201"
                    value={pinCode}
                    onChange={e => setPinCode(e.target.value)}
                    className="w-full text-center py-3.5 text-2xl font-black tracking-widest bg-slate-800/80 border border-slate-700 rounded-2xl text-yellow-300 outline-none focus:ring-2 focus:ring-purple-500 shadow-inner transition"
                  />
                </div>

                <div className="space-y-1.5 text-left">
                  <label className="block text-xs font-extrabold uppercase text-slate-400 tracking-wider">ISMINGIZ (NIKNEYM)</label>
                  <input
                    type="text"
                    placeholder="Ismingizni kiriting"
                    value={nickname}
                    onChange={e => setNickname(e.target.value)}
                    className="w-full text-center py-3.5 text-base font-bold bg-slate-800/80 border border-slate-700 rounded-2xl text-white outline-none focus:ring-2 focus:ring-purple-500 shadow-inner transition"
                  />
                </div>

                <button
                  type="submit"
                  className="w-full py-4 bg-gradient-to-r from-purple-600 via-indigo-600 to-blue-600 hover:from-purple-700 hover:to-blue-700 text-white font-black text-base rounded-2xl shadow-xl shadow-purple-900/30 transition transform active:scale-95 flex items-center justify-center gap-2 cursor-pointer"
                >
                  <Send className="w-5 h-5" /> Testga Qo'shilish
                </button>
              </form>
            </div>

          </div>
        )}

        {/* 2. WAITING ROOM STATE WITH ANIMAL AVATAR */}
        {gameState === 'waiting' && (
          <div className="text-center space-y-6 max-w-md animate-fadeIn p-8 bg-slate-900/80 rounded-3xl border border-slate-800 backdrop-blur-xl shadow-2xl">
            <div className="w-28 h-28 rounded-full bg-gradient-to-tr from-purple-600/30 to-indigo-600/30 border-2 border-purple-500 flex flex-col items-center justify-center mx-auto shadow-2xl animate-pulse">
              <span className="text-6xl drop-shadow-md">{avatar?.emoji || '🦁'}</span>
            </div>

            <div className="space-y-2">
              <div className="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-purple-950 border border-purple-800 text-yellow-300 text-xs font-black">
                {avatar?.emoji} Personajingiz: {avatar?.name || 'Qahramon'}
              </div>
              <h2 className="text-3xl font-black text-white">{nickname}, Siz O'yindasiz!</h2>
              <p className="text-xs text-purple-300 font-semibold leading-relaxed">
                O'qituvchi ekrandan savolni ko'rsatishini kuting va mos rang/shaklni tanlang!
              </p>
            </div>

            <div className="p-3.5 rounded-2xl bg-purple-950/60 border border-purple-800/60 text-purple-200 text-xs font-bold flex items-center justify-center gap-2">
              <ShieldCheck className="w-4 h-4 text-emerald-400" /> Aloqa Tizimga Muvaffaqiyatli Ulangan
            </div>
          </div>
        )}

        {/* 3. RESPONSIVE ARENA 4-SHAPE BUTTONS WITH HIGH-FEEDBACK TOUCH MICRO-ANIMATIONS */}
        {gameState === 'question' && (
          <div className="w-full max-w-4xl h-[78vh] flex flex-col justify-between animate-scaleUp">
            
            {/* Top Bar */}
            <div className="flex items-center justify-between text-xs font-bold text-slate-300 px-4 py-3 bg-slate-900/90 border border-slate-800 rounded-2xl shadow-lg backdrop-blur-md">
              <span className="flex items-center gap-2">
                <span className="text-xl">{avatar?.emoji || '👤'}</span>
                <span className="font-extrabold text-white">{nickname}</span>
              </span>
              
              <span className="text-yellow-300 font-black text-base tracking-wider bg-slate-800 px-3 py-1 rounded-xl border border-slate-700">
                ⏱ {timerLeft}s
              </span>
              
              <span className="text-purple-300 font-bold">{totalScore} ball</span>
            </div>

            {/* 4 Large Responsive Shape Buttons */}
            <div className="grid grid-cols-1 sm:grid-cols-2 gap-4 flex-1 my-4">
              {ARENA_PLAYER_BUTTONS.slice(0, optionsCount).map((btn, idx) => {
                const isSelected = selectedOption === idx;

                return (
                  <button
                    key={idx}
                    disabled={selectedOption !== null}
                    onClick={() => handleSubmitAnswer(idx)}
                    style={{ backgroundColor: btn.color }}
                    className={`rounded-3xl text-7xl md:text-8xl text-white shadow-2xl flex items-center justify-center transform transition-all duration-150 border-b-8 border-black/30 cursor-pointer relative overflow-hidden ${btn.hoverBg} ${btn.shadowColor} ${
                      isSelected
                        ? 'ring-8 ring-yellow-400 scale-95 border-b-0 brightness-110 animate-pulse'
                        : selectedOption !== null
                        ? 'opacity-40 grayscale'
                        : 'active:scale-95'
                    }`}
                  >
                    <span className="drop-shadow-2xl">{btn.shape}</span>

                    {isSelected && (
                      <div className="absolute inset-0 bg-black/20 flex items-center justify-center">
                        <span className="px-4 py-2 bg-yellow-400 text-slate-900 font-black text-sm rounded-full shadow-2xl flex items-center gap-1 animate-bounce">
                          <CheckCircle2 className="w-5 h-5 text-slate-900" /> Javobingiz Saqlandi!
                        </span>
                      </div>
                    )}
                  </button>
                );
              })}
            </div>
          </div>
        )}

        {/* 4. ANSWER SUBMITTED STATE */}
        {gameState === 'answered' && (
          <div className="text-center space-y-5 max-w-sm animate-scaleUp p-8 bg-slate-900/90 rounded-3xl border border-slate-800 backdrop-blur-xl shadow-2xl">
            <div className="w-24 h-24 rounded-full bg-blue-600/20 border-2 border-blue-500 flex items-center justify-center text-4xl mx-auto">
              <Loader2 className="w-12 h-12 text-blue-400 animate-spin" />
            </div>
            <h2 className="text-3xl font-black text-white">Javob Qabul Qilindi!</h2>
            <p className="text-xs text-slate-400 font-medium">
              Barcha o'quvchilar javob berishini kuting...
            </p>
          </div>
        )}

        {/* 5. ROUND RESULT STATE WITH ANIMAL AVATAR */}
        {gameState === 'result' && (
          <div className="w-full max-w-md p-8 bg-slate-900/90 rounded-3xl border border-slate-800/90 text-center space-y-5 animate-scaleUp shadow-2xl backdrop-blur-xl">
            <div className="flex items-center justify-center gap-2 text-2xl">
              <span>{avatar?.emoji}</span>
              <span className="font-black text-white text-lg">{nickname}</span>
            </div>

            <div className={`w-24 h-24 rounded-full flex items-center justify-center text-5xl mx-auto shadow-xl ${
              isCorrect ? 'bg-emerald-500/20 text-emerald-400 border-2 border-emerald-500' : 'bg-rose-500/20 text-rose-400 border-2 border-rose-500'
            }`}>
              {isCorrect ? '✓' : '✕'}
            </div>

            <h2 className="text-3xl font-black">
              {isCorrect ? "To'g'ri Javob! ✨" : "Noto'g'ri Javob ❌"}
            </h2>

            <div className="text-4xl font-black text-yellow-300 tracking-tight">
              +{pointsEarned} <span className="text-xs font-bold text-slate-400">ball</span>
            </div>

            <div className="p-4 rounded-2xl bg-slate-800/80 border border-slate-700 flex items-center justify-between text-xs font-bold">
              <span className="text-slate-400">Joriy O'rningiz:</span>
              <span className="text-purple-300 text-base font-black">#{rank} - o'rin</span>
            </div>

            {streak >= 2 && (
              <div className="p-3 rounded-2xl bg-amber-500/20 border border-amber-500/50 text-amber-300 text-xs font-extrabold flex items-center justify-center gap-2 animate-bounce">
                <Flame className="w-5 h-5 text-amber-400 fill-amber-400" />
                {streak} ta ketma-ket to'g'ri! (Streak 🔥)
              </div>
            )}
          </div>
        )}

        {/* 6. FINISHED STATE WITH ANIMAL AVATAR */}
        {gameState === 'finished' && (
          <div className="text-center space-y-6 max-w-md animate-scaleUp p-8 bg-slate-900/90 rounded-3xl border border-slate-800 backdrop-blur-xl shadow-2xl">
            <div className="text-6xl mb-2">{avatar?.emoji || '🏆'}</div>
            <Trophy className="w-20 h-20 text-yellow-400 mx-auto drop-shadow-2xl animate-bounce" />
            <h2 className="text-4xl font-black text-white">O'yin Tugadi!</h2>
            <div className="p-6 rounded-2xl bg-slate-800/80 border border-slate-700 space-y-3">
              <div className="text-xs font-bold text-slate-400">Yakuniy Natijangiz:</div>
              <div className="text-4xl font-black text-yellow-300">{totalScore} ball</div>
              <div className="text-base font-extrabold text-purple-300">#{rank} - o'rin</div>
            </div>
          </div>
        )}

      </main>

      {/* Footer */}
      <footer className="p-4 text-center border-t border-slate-800/60 text-xs text-slate-500 font-medium relative z-20">
        © 2026 Marimov Game Zone — <strong className="text-slate-400">game.marimovdev.uz</strong>
      </footer>

    </div>
  );
}
