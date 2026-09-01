import React, { useState, useEffect } from 'react';
import { io, Socket } from 'socket.io-client';
import { quizAudio } from '../../services/QuizAudioService';
import { Flame, CheckCircle2, XCircle, Trophy, Volume2, VolumeX, Sparkles, Send } from 'lucide-react';

interface QuizPlayerViewProps {
  onExit: () => void;
}

export function QuizPlayerView({ onExit }: QuizPlayerViewProps) {
  const [socket, setSocket] = useState<Socket | null>(null);
  const [pinCode, setPinCode] = useState<string>('');
  const [nickname, setNickname] = useState<string>('');
  const [error, setError] = useState<string | null>(null);

  const [gameState, setGameState] = useState<'join' | 'waiting' | 'question' | 'answered' | 'result' | 'finished'>('join');
  const [sessionTitle, setSessionTitle] = useState<string>('');
  
  const [questionText, setQuestionText] = useState<string>('');
  const [options, setOptions] = useState<string[]>([]);
  const [questionIndex, setQuestionIndex] = useState<number>(0);
  const [totalQuestions, setTotalQuestions] = useState<number>(0);
  const [timerLeft, setTimerLeft] = useState<number>(20);
  const [startTime, setStartTime] = useState<number>(0);

  // Player stats
  const [selectedOption, setSelectedOption] = useState<number | null>(null);
  const [isCorrect, setIsCorrect] = useState<boolean | null>(null);
  const [pointsEarned, setPointsEarned] = useState<number>(0);
  const [totalScore, setTotalScore] = useState<number>(0);
  const [streak, setStreak] = useState<number>(0);
  const [rank, setRank] = useState<number>(1);
  const [isMuted, setIsMuted] = useState<boolean>(false);

  useEffect(() => {
    const newSocket = io(window.location.origin, { transports: ['websocket', 'polling'] });
    setSocket(newSocket);

    newSocket.on('player:joined', ({ code, nickname, sessionTitle }) => {
      setGameState('waiting');
      setSessionTitle(sessionTitle);
      setError(null);
      quizAudio.playCorrect();
    });

    newSocket.on('player:error', ({ message }) => {
      setError(message);
    });

    newSocket.on('game:countdown-start', () => {
      setGameState('waiting');
    });

    newSocket.on('player:question-started', ({ questionIndex, totalQuestions, questionText, options, durationSec }) => {
      setGameState('question');
      setQuestionIndex(questionIndex);
      setTotalQuestions(totalQuestions);
      setQuestionText(questionText);
      setOptions(options);
      setTimerLeft(durationSec);
      setSelectedOption(null);
      setIsCorrect(null);
      setStartTime(Date.now());
      quizAudio.playQuestionStart();
    });

    newSocket.on('player:answer-received', ({ isCorrect, pointsEarned, totalScore, streak }) => {
      setGameState('answered');
      setIsCorrect(isCorrect);
      setPointsEarned(pointsEarned);
      setTotalScore(totalScore);
      setStreak(streak);

      if (isCorrect) quizAudio.playCorrect();
      else quizAudio.playIncorrect();
    });

    newSocket.on('player:round-summary', ({ rank, score, pointsEarned, streak }) => {
      setGameState('result');
      setRank(rank);
      setTotalScore(score);
      setPointsEarned(pointsEarned);
      setStreak(streak);
    });

    newSocket.on('game:finished', ({ leaderboard }) => {
      setGameState('finished');
      const myInfo = leaderboard.find((p: any) => p.nickname === nickname);
      if (myInfo) setRank(myInfo.rank);
      quizAudio.playFanfare();
    });

    return () => {
      newSocket.disconnect();
    };
  }, [nickname]);

  // Question timer
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
    if (!pinCode.trim() || !nickname.trim()) {
      setError("PIN va Ismingizni kiriting");
      return;
    }
    if (socket) {
      socket.emit('player:join-session', { code: pinCode.trim(), nickname: nickname.trim() });
    }
  };

  const handleSubmitAnswer = (optionIdx: number) => {
    if (selectedOption !== null || !socket) return;
    setSelectedOption(optionIdx);
    const responseTimeMs = Date.now() - startTime;
    socket.emit('player:submit-answer', { code: pinCode, optionIndex: optionIdx, responseTimeMs });
  };

  const toggleMute = () => {
    const next = !isMuted;
    setIsMuted(next);
    quizAudio.setMuted(next);
  };

  const shapes = ['🔺', '🟦', '🟡', '🟢'];
  const colors = [
    'bg-rose-500 hover:bg-rose-600 border-rose-700',
    'bg-blue-600 hover:bg-blue-700 border-blue-800',
    'bg-amber-500 hover:bg-amber-600 border-amber-700',
    'bg-emerald-600 hover:bg-emerald-700 border-emerald-800'
  ];

  return (
    <div className="min-h-screen bg-slate-950 text-white flex flex-col justify-between p-4 font-sans select-none overflow-hidden">
      
      {/* Top Header */}
      <div className="flex items-center justify-between p-2">
        <div className="flex items-center gap-2">
          <span className="text-xl">📱</span>
          <span className="font-extrabold text-sm text-purple-300">Quiz Arena</span>
        </div>

        <div className="flex items-center gap-2">
          <button onClick={toggleMute} className="p-2 rounded-lg bg-slate-800 text-slate-300">
            {isMuted ? <VolumeX className="w-4 h-4 text-rose-400" /> : <Volume2 className="w-4 h-4 text-emerald-400" />}
          </button>
          <button onClick={onExit} className="px-3 py-1 bg-slate-800 text-xs font-bold rounded-lg text-slate-300">
            Chiqish
          </button>
        </div>
      </div>

      {/* Main Dynamic View */}
      <div className="flex-1 flex flex-col items-center justify-center">
        
        {/* 1. JOIN FORM STATE */}
        {gameState === 'join' && (
          <form onSubmit={handleJoin} className="w-full max-w-sm p-6 bg-slate-900 rounded-3xl border border-slate-800 space-y-4 shadow-2xl animate-scaleUp">
            <div className="text-center space-y-1">
              <h2 className="text-2xl font-black text-white">Quizga Qo'shilish</h2>
              <p className="text-xs text-slate-400">O'qituvchi ekranidagi 6-xonali PIN kodni kiriting</p>
            </div>

            {error && (
              <div className="p-3 bg-rose-950/60 border border-rose-800 text-rose-300 rounded-xl text-xs">
                ⚠️ {error}
              </div>
            )}

            <div>
              <label className="block text-xs font-bold text-slate-400 mb-1">PIN KOD</label>
              <input
                type="text"
                maxLength={6}
                placeholder="Masalan: 849201"
                value={pinCode}
                onChange={e => setPinCode(e.target.value)}
                className="w-full text-center py-3 text-2xl font-black tracking-widest bg-slate-800 border border-slate-700 rounded-2xl text-yellow-300 outline-none focus:ring-2 focus:ring-purple-500"
              />
            </div>

            <div>
              <label className="block text-xs font-bold text-slate-400 mb-1">ISMINGIZ (NIKNEYM)</label>
              <input
                type="text"
                placeholder="Ismingizni kiriting"
                value={nickname}
                onChange={e => setNickname(e.target.value)}
                className="w-full text-center py-3 text-base font-bold bg-slate-800 border border-slate-700 rounded-2xl text-white outline-none focus:ring-2 focus:ring-purple-500"
              />
            </div>

            <button
              type="submit"
              className="w-full py-3.5 bg-gradient-to-r from-purple-600 to-indigo-600 hover:from-purple-700 text-white font-extrabold text-sm rounded-2xl shadow-xl transition flex items-center justify-center gap-2"
            >
              <Send className="w-4 h-4" /> Testga Qo'shilish
            </button>
          </form>
        )}

        {/* 2. WAITING ROOM STATE */}
        {gameState === 'waiting' && (
          <div className="text-center space-y-4 max-w-sm animate-fadeIn">
            <div className="w-20 h-20 rounded-full bg-purple-600/30 border-2 border-purple-500 flex items-center justify-center text-4xl mx-auto animate-pulse">
              🎯
            </div>
            <h2 className="text-2xl font-black text-white">{nickname}, Siz o'yindasiz!</h2>
            <p className="text-xs text-purple-300">
              O'qituvchi o'yinni boshlashini kuting. Ekrandan savollarni kuzatib boring!
            </p>
          </div>
        )}

        {/* 3. QUESTION STATE (4 Large Colored Buttons) */}
        {gameState === 'question' && (
          <div className="w-full max-w-md space-y-4 animate-scaleUp">
            <div className="flex items-center justify-between text-xs font-bold text-slate-400 px-1">
              <span>{nickname}</span>
              <span className="text-yellow-400 font-extrabold">⏱ {timerLeft}s</span>
              <span>{totalScore} ball</span>
            </div>

            <div className="p-4 rounded-2xl bg-slate-900 border border-slate-800 text-center font-bold text-sm text-white min-h-16 flex items-center justify-center">
              {questionText}
            </div>

            <div className="grid grid-cols-2 gap-3 h-64">
              {options.map((opt, idx) => (
                <button
                  key={idx}
                  onClick={() => handleSubmitAnswer(idx)}
                  className={`rounded-2xl ${colors[idx]} border-b-4 text-white font-black text-xl flex flex-col items-center justify-center p-4 active:scale-95 transition shadow-lg`}
                >
                  <span className="text-3xl mb-1">{shapes[idx]}</span>
                  <span className="text-xs font-extrabold line-clamp-2">{opt}</span>
                </button>
              ))}
            </div>
          </div>
        )}

        {/* 4. ANSWERED STATE */}
        {gameState === 'answered' && (
          <div className="text-center space-y-4 animate-scaleUp">
            <div className={`w-24 h-24 rounded-full flex items-center justify-center text-5xl mx-auto ${
              isCorrect ? 'bg-emerald-500/20 text-emerald-400 border-2 border-emerald-500' : 'bg-rose-500/20 text-rose-400 border-2 border-rose-500'
            }`}>
              {isCorrect ? '✓' : '✕'}
            </div>
            <h2 className="text-2xl font-black">
              {isCorrect ? "To'g'ri Javob! ✨" : "Noto'g'ri Javob ❌"}
            </h2>
            <p className="text-xs text-slate-400">
              O'qituvchidan savol yakunlanishini kuting...
            </p>
          </div>
        )}

        {/* 5. ROUND RESULT STATE */}
        {gameState === 'result' && (
          <div className="w-full max-w-xs p-6 bg-slate-900 rounded-3xl border border-slate-800 text-center space-y-4 animate-scaleUp shadow-2xl">
            <div className="text-xs font-bold text-purple-400 uppercase tracking-wider">
              Natijangiz
            </div>

            <div className="text-4xl font-black text-yellow-300">
              +{pointsEarned} <span className="text-xs font-semibold text-slate-400">ball</span>
            </div>

            <div className="p-3 rounded-2xl bg-slate-800 flex items-center justify-between text-xs font-bold">
              <span className="text-slate-400">O'rningiz:</span>
              <span className="text-purple-300 text-sm">#{rank} - o'rin</span>
            </div>

            {streak >= 2 && (
              <div className="p-2.5 rounded-xl bg-amber-500/20 border border-amber-500/50 text-amber-300 text-xs font-bold flex items-center justify-center gap-1.5 animate-bounce">
                <Flame className="w-4 h-4 text-amber-400 fill-amber-400" />
                {streak} ta ketma-ket to'g'ri! (Streak bonus 🔥)
              </div>
            )}
          </div>
        )}

        {/* 6. FINISHED STATE */}
        {gameState === 'finished' && (
          <div className="text-center space-y-4 max-w-xs animate-scaleUp">
            <Trophy className="w-20 h-20 text-yellow-400 mx-auto" />
            <h2 className="text-3xl font-black text-white">O'yin Tugadi!</h2>
            <div className="p-4 rounded-2xl bg-slate-900 border border-slate-800 space-y-2">
              <div className="text-xs text-slate-400">Sizning Yakuniy Natijangiz:</div>
              <div className="text-3xl font-black text-yellow-300">{totalScore} ball</div>
              <div className="text-sm font-bold text-purple-300">#{rank} - o'rin</div>
            </div>
          </div>
        )}

      </div>
    </div>
  );
}
