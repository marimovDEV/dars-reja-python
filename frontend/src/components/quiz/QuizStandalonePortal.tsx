import React, { useState } from 'react';
import { QuizPlayerView } from './QuizPlayerView';
import { QuizHostView } from './QuizHostView';
import { AIQuizGeneratorModal } from './AIQuizGeneratorModal';
import { QuizEditorModal } from './QuizEditorModal';
import { Sparkles, Gamepad2, Users, Trophy, Play, ArrowRight, Zap, ShieldCheck } from 'lucide-react';
import { Quiz } from '../../types/quiz';
import { Lesson } from '../../types';

interface QuizStandalonePortalProps {
  lessons?: Lesson[];
}

export function QuizStandalonePortal({ lessons = [] }: QuizStandalonePortalProps) {
  const [mode, setMode] = useState<'home' | 'player' | 'host'>('home');
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

  if (mode === 'player') {
    return <QuizPlayerView onExit={() => setMode('home')} />;
  }

  if (mode === 'host' && activeQuiz) {
    return <QuizHostView quiz={activeQuiz} onExit={() => setMode('home')} />;
  }

  return (
    <div className="min-h-screen bg-slate-950 text-white font-sans flex flex-col justify-between relative overflow-hidden select-none">
      
      {/* Dynamic Background Effects */}
      <div className="absolute -top-40 -left-40 w-96 h-96 bg-purple-600/20 rounded-full blur-3xl pointer-events-none" />
      <div className="absolute -bottom-40 -right-40 w-96 h-96 bg-indigo-600/20 rounded-full blur-3xl pointer-events-none" />

      {/* Top Header */}
      <header className="p-6 px-8 flex items-center justify-between border-b border-slate-800/80 bg-slate-900/40 backdrop-blur-md relative z-10">
        <div className="flex items-center gap-3">
          <div className="w-11 h-11 rounded-2xl bg-gradient-to-tr from-purple-600 to-indigo-600 flex items-center justify-center font-black text-2xl shadow-xl shadow-purple-900/30">
            🎮
          </div>
          <div>
            <h1 className="font-extrabold text-lg tracking-tight text-white flex items-center gap-2">
              AI Quiz Arena
              <span className="px-2 py-0.5 rounded-full text-[10px] font-black uppercase tracking-wider bg-purple-950 text-purple-300 border border-purple-800">
                Standalone Portal
              </span>
            </h1>
            <p className="text-xs text-slate-400 font-medium">game.marimovdev.uz</p>
          </div>
        </div>

        <a
          href="https://python.marimovdev.uz"
          className="px-4 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 border border-slate-700 text-xs font-bold text-slate-300 transition flex items-center gap-1.5"
        >
          📚 Dars Reja Portaliga O'tish
        </a>
      </header>

      {/* Hero Body */}
      <main className="flex-1 flex flex-col items-center justify-center p-6 text-center max-w-4xl mx-auto relative z-10 my-8">
        
        <div className="inline-flex items-center gap-2 px-4 py-2 rounded-full bg-purple-950/80 border border-purple-800 text-purple-300 text-xs font-extrabold mb-6 animate-pulse">
          <Sparkles className="w-4 h-4 text-yellow-400" /> AI Bilan Jonli Kahoot-Uslubidagi O'yinlar
        </div>

        <h2 className="text-4xl md:text-6xl font-black tracking-tight leading-tight mb-4 text-transparent bg-clip-text bg-gradient-to-r from-white via-slate-100 to-purple-300">
          Bilimingizni Jonli O'yinda Sinang!
        </h2>

        <p className="text-slate-400 text-sm md:text-base max-w-2xl mb-10 leading-relaxed font-medium">
          Sun'iy intellekt tomonidan dars hujjatlaridan avtomatik yaratiladigan interaktiv, musiqa va animatsiyali quiz platformasi.
        </p>

        {/* 2 Main Portal Action Cards */}
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6 w-full max-w-3xl">
          
          {/* Card 1: Student Player Entrance */}
          <div className="p-8 rounded-3xl bg-slate-900/90 border border-purple-900/50 hover:border-purple-500/80 shadow-2xl transition duration-300 flex flex-col items-center justify-between text-center group relative overflow-hidden">
            <div className="w-16 h-16 rounded-2xl bg-gradient-to-tr from-rose-500 to-amber-500 flex items-center justify-center text-3xl mb-4 shadow-lg group-hover:scale-110 transition-transform">
              📱
            </div>

            <div className="space-y-2 mb-6">
              <h3 className="text-2xl font-black text-white">O'quvchilar Uchun</h3>
              <p className="text-xs text-slate-400 leading-relaxed">
                O'qituvchi bergan 6-xonali PIN kodni kiritib, telefoningiz orqali jonli o'yinga ulaning.
              </p>
            </div>

            <button
              onClick={() => setMode('player')}
              className="w-full py-4 bg-gradient-to-r from-rose-500 to-amber-500 hover:from-rose-600 hover:to-amber-600 text-white font-extrabold text-base rounded-2xl shadow-xl transition flex items-center justify-center gap-2 group"
            >
              <Gamepad2 className="w-5 h-5" /> PIN Bilan Kirish <ArrowRight className="w-5 h-5 group-hover:translate-x-1 transition-transform" />
            </button>
          </div>

          {/* Card 2: Teacher Host Entrance */}
          <div className="p-8 rounded-3xl bg-slate-900/90 border border-indigo-900/50 hover:border-indigo-500/80 shadow-2xl transition duration-300 flex flex-col items-center justify-between text-center group relative overflow-hidden">
            <div className="w-16 h-16 rounded-2xl bg-gradient-to-tr from-indigo-500 to-purple-600 flex items-center justify-center text-3xl mb-4 shadow-lg group-hover:scale-110 transition-transform">
              👑
            </div>

            <div className="space-y-2 mb-6">
              <h3 className="text-2xl font-black text-white">O'qituvchi Uchun</h3>
              <p className="text-xs text-slate-400 leading-relaxed">
                AI yordamida soniyalar ichida testlar yarating va proyektor ekranida host rejimini boshlang.
              </p>
            </div>

            <button
              onClick={() => setIsGeneratorOpen(true)}
              className="w-full py-4 bg-gradient-to-r from-indigo-600 to-purple-600 hover:from-indigo-700 hover:to-purple-700 text-white font-extrabold text-base rounded-2xl shadow-xl transition flex items-center justify-center gap-2 group"
            >
              <Zap className="w-5 h-5 text-yellow-300" /> AI Quiz Yaratish & Host <ArrowRight className="w-5 h-5 group-hover:translate-x-1 transition-transform" />
            </button>
          </div>

        </div>

      </main>

      {/* Footer */}
      <footer className="p-6 text-center border-t border-slate-800/60 text-xs text-slate-500 font-medium relative z-10">
        © 2026 AI Quiz Arena — Subdomain Portal: <strong className="text-slate-400">game.marimovdev.uz</strong>
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
