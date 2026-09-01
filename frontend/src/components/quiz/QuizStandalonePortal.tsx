import React, { useState, useEffect } from 'react';
import { QuizPlayerView } from './QuizPlayerView';
import { QuizHostView } from './QuizHostView';
import { AIQuizGeneratorModal } from './AIQuizGeneratorModal';
import { QuizEditorModal } from './QuizEditorModal';
import { Sparkles, Lock, ShieldCheck, Zap, KeyRound, ArrowRight } from 'lucide-react';
import { Quiz } from '../../types/quiz';
import { Lesson } from '../../types';

interface QuizStandalonePortalProps {
  lessons?: Lesson[];
}

export function QuizStandalonePortal({ lessons = [] }: QuizStandalonePortalProps) {
  const isCreateRoute = typeof window !== 'undefined' && (
    window.location.pathname.endsWith('/create') ||
    window.location.search.includes('mode=create') ||
    window.location.search.includes('create=true')
  );

  const [teacherLoggedIn, setTeacherLoggedIn] = useState<boolean>(() => {
    return localStorage.getItem('game_teacher_logged_in') === 'true';
  });

  const [loginUsername, setLoginUsername] = useState<string>('');
  const [loginPassword, setLoginPassword] = useState<string>('');
  const [loginError, setLoginError] = useState<string | null>(null);

  const [mode, setMode] = useState<'player' | 'host' | 'create_dashboard'>(isCreateRoute ? 'create_dashboard' : 'player');
  const [activeQuiz, setActiveQuiz] = useState<Quiz | null>(null);
  const [isGeneratorOpen, setIsGeneratorOpen] = useState<boolean>(false);
  const [isEditorOpen, setIsEditorOpen] = useState<boolean>(false);

  const defaultLessons: Lesson[] = lessons.length > 0 ? lessons : Array.from({ length: 72 }, (_, i) => ({
    id: `les-${i + 1}`,
    lessonNumber: i + 1,
    title: `${i + 1}-dars: Python Backend`,
    description: `Python Backend darsligi #${i + 1}`,
    status: 'planned' as const,
    date: new Date().toISOString()
  }));

  // Automatic trigger generator if on /create route and logged in
  useEffect(() => {
    if (isCreateRoute && teacherLoggedIn) {
      setIsGeneratorOpen(true);
    }
  }, [isCreateRoute, teacherLoggedIn]);

  const handleTeacherLogin = (e: React.FormEvent) => {
    e.preventDefault();
    if (loginUsername.trim() === 'ogabek' && loginPassword === 'marimov') {
      localStorage.setItem('game_teacher_logged_in', 'true');
      setTeacherLoggedIn(true);
      setLoginError(null);
      setIsGeneratorOpen(true);
    } else {
      setLoginError("Login yoki parol noto'g'ri (Login: ogabek / Parol: marimov)");
    }
  };

  const handleLogoutTeacher = () => {
    localStorage.removeItem('game_teacher_logged_in');
    setTeacherLoggedIn(false);
  };

  // 1. ROOT DOMAIN (https://game.marimovdev.uz/) -> STUDENT ONLY VIEW
  if (!isCreateRoute && mode === 'player') {
    return <QuizPlayerView onExit={() => {}} />;
  }

  // 2. LIVE HOST GAME VIEW
  if (mode === 'host' && activeQuiz) {
    return <QuizHostView quiz={activeQuiz} onExit={() => setMode('create_dashboard')} />;
  }

  // 3. TEACHER /CREATE ROUTE (https://game.marimovdev.uz/create)
  return (
    <div className="min-h-screen bg-slate-950 text-white font-sans flex flex-col justify-between relative overflow-hidden select-none p-4">
      
      {/* Background Glow */}
      <div className="absolute -top-40 -left-40 w-96 h-96 bg-purple-600/20 rounded-full blur-3xl pointer-events-none" />
      <div className="absolute -bottom-40 -right-40 w-96 h-96 bg-indigo-600/20 rounded-full blur-3xl pointer-events-none" />

      {/* Header */}
      <header className="p-4 px-6 flex items-center justify-between border-b border-slate-800 bg-slate-900/40 rounded-2xl backdrop-blur-md">
        <div className="flex items-center gap-3">
          <div className="w-10 h-10 rounded-xl bg-gradient-to-tr from-purple-600 to-indigo-600 flex items-center justify-center font-black text-xl shadow-lg">
            👑
          </div>
          <div>
            <h1 className="font-extrabold text-base tracking-tight text-white flex items-center gap-2">
              O'qituvchi Boshqaruvi
              <span className="px-2 py-0.5 rounded-full text-[10px] font-black uppercase tracking-wider bg-purple-950 text-purple-300 border border-purple-800">
                game.marimovdev.uz/create
              </span>
            </h1>
          </div>
        </div>

        <a
          href="https://game.marimovdev.uz"
          className="px-3 py-1.5 bg-slate-800 hover:bg-slate-700 text-xs font-bold text-slate-300 rounded-xl transition"
        >
          📱 O'quvchi Rejimiga Qaytish
        </a>
      </header>

      {/* Main Area */}
      <main className="flex-1 flex flex-col items-center justify-center p-6 text-center max-w-md mx-auto my-8">
        
        {!teacherLoggedIn ? (
          /* TEACHER LOGIN FORM */
          <form onSubmit={handleTeacherLogin} className="w-full p-8 bg-slate-900/90 rounded-3xl border border-slate-800 shadow-2xl space-y-5 animate-scaleUp">
            <div className="w-16 h-16 rounded-full bg-purple-600/20 border border-purple-500 flex items-center justify-center text-3xl mx-auto">
              <Lock className="w-8 h-8 text-purple-400" />
            </div>

            <div className="space-y-1">
              <h2 className="text-2xl font-black text-white">O'qituvchi Kirishi</h2>
              <p className="text-xs text-slate-400">O'yin yaratish va host rejimini boshlash uchun tizimga kiring</p>
            </div>

            {loginError && (
              <div className="p-3 bg-rose-950/60 border border-rose-800 text-rose-300 rounded-xl text-xs font-semibold">
                ⚠️ {loginError}
              </div>
            )}

            <div className="text-left space-y-1">
              <label className="block text-xs font-bold text-slate-400">LOGIN (USERNAME)</label>
              <input
                type="text"
                placeholder="ogabek"
                value={loginUsername}
                onChange={e => setLoginUsername(e.target.value)}
                className="w-full py-3 px-4 bg-slate-800 border border-slate-700 rounded-2xl text-white font-bold text-sm outline-none focus:ring-2 focus:ring-purple-500"
              />
            </div>

            <div className="text-left space-y-1">
              <label className="block text-xs font-bold text-slate-400">PAROL</label>
              <input
                type="password"
                placeholder="marimov"
                value={loginPassword}
                onChange={e => setLoginPassword(e.target.value)}
                className="w-full py-3 px-4 bg-slate-800 border border-slate-700 rounded-2xl text-white font-bold text-sm outline-none focus:ring-2 focus:ring-purple-500"
              />
            </div>

            <button
              type="submit"
              className="w-full py-3.5 bg-gradient-to-r from-purple-600 to-indigo-600 hover:from-purple-700 text-white font-extrabold text-sm rounded-2xl shadow-xl transition flex items-center justify-center gap-2 cursor-pointer"
            >
              <KeyRound className="w-4 h-4" /> Tizimga Kirish
            </button>
          </form>
        ) : (
          /* AUTHENTICATED TEACHER DASHBOARD */
          <div className="w-full p-8 bg-slate-900/90 rounded-3xl border border-slate-800 shadow-2xl space-y-6 animate-scaleUp">
            <div className="w-16 h-16 rounded-full bg-emerald-500/20 border border-emerald-500 flex items-center justify-center text-3xl mx-auto">
              <ShieldCheck className="w-8 h-8 text-emerald-400" />
            </div>

            <div>
              <h2 className="text-2xl font-black text-white">Xush Kelibsiz, O'qituvchi!</h2>
              <p className="text-xs text-slate-400 mt-1">Siz o'yin yaratish panelidasiz</p>
            </div>

            <button
              onClick={() => setIsGeneratorOpen(true)}
              className="w-full py-4 bg-gradient-to-r from-indigo-600 to-purple-600 hover:from-indigo-700 text-white font-extrabold text-base rounded-2xl shadow-xl transition flex items-center justify-center gap-2 group cursor-pointer"
            >
              <Zap className="w-5 h-5 text-yellow-300" /> AI Quiz Yaratish va Boshlash <ArrowRight className="w-5 h-5 group-hover:translate-x-1 transition-transform" />
            </button>

            <button
              onClick={handleLogoutTeacher}
              className="text-xs text-slate-500 hover:text-rose-400 underline font-semibold transition"
            >
              Tizimdan Chiqish
            </button>
          </div>
        )}

      </main>

      {/* Footer */}
      <footer className="p-4 text-center text-xs text-slate-500 font-medium">
        © 2026 AI Quiz Arena — Teacher Host Portal
      </footer>

      {/* AI Generator Modal */}
      <AIQuizGeneratorModal
        isOpen={isGeneratorOpen}
        onClose={() => setIsGeneratorOpen(false)}
        lessons={defaultLessons}
        onQuizGenerated={(generatedQuiz) => {
          setIsGeneratorOpen(false);
          setActiveQuiz(generatedQuiz);
          setIsEditorOpen(true);
        }}
      />

      {/* Quiz Editor Modal */}
      {activeQuiz && (
        <QuizEditorModal
          isOpen={isEditorOpen}
          onClose={() => setIsEditorOpen(false)}
          quiz={activeQuiz}
          onStartLiveSession={(finalQuiz) => {
            setIsEditorOpen(false);
            setActiveQuiz(finalQuiz);
            setMode('host');
          }}
        />
      )}

    </div>
  );
}
