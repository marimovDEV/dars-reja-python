import React, { useState, useEffect } from 'react';
import { 
  BookOpen, 
  Copy, 
  Check, 
  Printer, 
  Share2, 
  List, 
  FileText, 
  Code, 
  Target, 
  HelpCircle, 
  Paperclip,
  ExternalLink,
  Sparkles,
  ArrowLeft
} from 'lucide-react';
import { Lesson, LessonMaterial } from '../types';
import { MarkdownDocRenderer } from './MarkdownDocRenderer';
import { TableOfContents } from './TableOfContents';
import { CodeBlock } from './CodeBlock';
import { DocCallout } from './DocCallout';

interface PublicSharedLessonViewProps {
  lessonId: string;
  initialLessons?: Lesson[];
  onBackToApp?: () => void;
}

export const PublicSharedLessonView: React.FC<PublicSharedLessonViewProps> = ({
  lessonId,
  initialLessons = [],
  onBackToApp
}) => {
  const [lesson, setLesson] = useState<Lesson | null>(() => {
    if (initialLessons && initialLessons.length > 0) {
      const found = initialLessons.find(l => l.id === lessonId || l.lessonNumber.toString() === lessonId);
      if (found) return found;
    }
    return null;
  });
  const [loading, setLoading] = useState<boolean>(!lesson);
  const [error, setError] = useState<string | null>(null);
  const [activeTab, setActiveTab] = useState<'docs' | 'code' | 'practice' | 'homework' | 'quiz' | 'resources'>('docs');
  const [copied, setCopied] = useState(false);
  const [linkCopied, setLinkCopied] = useState(false);
  const [mobileTocOpen, setMobileTocOpen] = useState(false);
  const [selectedQuizAnswers, setSelectedQuizAnswers] = useState<Record<string, number>>({});

  useEffect(() => {
    if (lesson) return;
    setLoading(true);
    setError(null);
    
    fetch(`/api/lessons/${lessonId}?t=` + Date.now())
      .then(async (res) => {
        if (!res.ok) {
          const listRes = await fetch('/api/lessons?t=' + Date.now());
          if (listRes.ok) {
            const all: Lesson[] = await listRes.json();
            const match = all.find(l => l.id === lessonId || l.lessonNumber.toString() === lessonId);
            if (match) return match;
          }
          throw new Error("Dars topilmadi yoki o'chirilgan");
        }
        return res.json();
      })
      .then((data: Lesson) => {
        setLesson(data);
        setLoading(false);
      })
      .catch(err => {
        setError(err.message || "Darsni yuklashda xatolik");
        setLoading(false);
      });
  }, [lessonId, lesson]);

  if (loading) {
    return (
      <div className="min-h-screen bg-slate-50 dark:bg-[#070A12] flex flex-col items-center justify-center p-6 text-slate-800 dark:text-slate-200">
        <div className="w-12 h-12 border-4 border-purple-600 border-t-transparent rounded-full animate-spin mb-4" />
        <p className="text-sm font-bold text-slate-600 dark:text-slate-400">Chop etilgan dars yuklanmoqda...</p>
      </div>
    );
  }

  if (error || !lesson) {
    return (
      <div className="min-h-screen bg-slate-50 dark:bg-[#070A12] flex flex-col items-center justify-center p-6 text-center text-slate-800 dark:text-slate-200">
        <div className="w-16 h-16 bg-rose-100 dark:bg-rose-950/60 text-rose-600 dark:text-rose-400 rounded-2xl flex items-center justify-center mb-4">
          ⚠️
        </div>
        <h2 className="text-xl font-bold mb-2">Dars Topilmadi</h2>
        <p className="text-sm text-slate-500 max-w-md mb-6">{error || "Siz so'ragan ulashilgan dars sahifasi mavjud emas."}</p>
        {onBackToApp && (
          <button
            onClick={onBackToApp}
            className="px-5 py-2.5 bg-purple-600 hover:bg-purple-700 text-white font-bold text-xs rounded-xl shadow-lg transition flex items-center gap-2 cursor-pointer"
          >
            <ArrowLeft className="w-4 h-4" /> Bosh Sahifaga Qaytish
          </button>
        )}
      </div>
    );
  }

  const handleCopyLink = () => {
    navigator.clipboard.writeText(window.location.href);
    setLinkCopied(true);
    setTimeout(() => setLinkCopied(false), 2000);
  };

  const handleQuizSelect = (quizId: string, optionIdx: number) => {
    setSelectedQuizAnswers(prev => ({
      ...prev,
      [quizId]: optionIdx
    }));
  };

  return (
    <div className="min-h-screen bg-slate-50 dark:bg-[#070A12] text-slate-800 dark:text-slate-200 font-['Inter',sans-serif] flex flex-col">
      {/* Public Standalone Header */}
      <header className="sticky top-0 z-40 bg-white/90 dark:bg-[#0B0F19]/90 backdrop-blur-md border-b border-slate-200 dark:border-slate-800/80 px-6 py-3.5 flex items-center justify-between shadow-xs">
        <div className="flex items-center gap-3">
          <div className="w-9 h-9 rounded-xl bg-gradient-to-r from-purple-600 to-indigo-600 flex items-center justify-center text-white font-black text-sm shadow-md">
            M
          </div>
          <div>
            <h1 className="font-extrabold text-sm text-slate-900 dark:text-white tracking-tight flex items-center gap-2">
              <span>marimovdev</span>
              <span className="px-2 py-0.5 rounded-full bg-purple-100 dark:bg-purple-950/60 text-purple-700 dark:text-purple-300 text-[10px] uppercase font-bold">
                O'quv Darsi #{lesson.lessonNumber}
              </span>
            </h1>
            <p className="text-[11px] text-slate-500 dark:text-slate-400 font-medium truncate max-w-xs sm:max-w-md">
              {lesson.title}
            </p>
          </div>
        </div>

        <div className="flex items-center gap-2">
          {/* Mobile TOC Button */}
          <button
            onClick={() => setMobileTocOpen(!mobileTocOpen)}
            className="lg:hidden flex items-center gap-1.5 px-3 py-1.5 text-xs font-bold text-slate-700 dark:text-slate-200 bg-slate-100 dark:bg-slate-800 rounded-xl"
          >
            <List className="w-4 h-4 text-purple-500" />
            <span>Mundarija</span>
          </button>

          <button
            onClick={handleCopyLink}
            className="flex items-center gap-1.5 px-3.5 py-2 text-xs font-bold text-white bg-purple-600 hover:bg-purple-700 rounded-xl shadow-md transition cursor-pointer"
          >
            {linkCopied ? <Check className="w-3.5 h-3.5" /> : <Share2 className="w-3.5 h-3.5" />}
            <span>{linkCopied ? "Havola Nusxalandi!" : "Havolani Ulashish"}</span>
          </button>

          {onBackToApp && (
            <button
              onClick={onBackToApp}
              className="px-3.5 py-2 text-xs font-bold text-slate-700 dark:text-slate-300 bg-slate-100 hover:bg-slate-200 dark:bg-slate-800 dark:hover:bg-slate-700 rounded-xl transition cursor-pointer"
            >
              Platformaga Kirish
            </button>
          )}
        </div>
      </header>

      {/* Main Public Content */}
      <main className="max-w-7xl w-full mx-auto p-6 md:p-10 flex gap-10 flex-1">
        <div className="flex-1 min-w-0 space-y-8">
          
          {/* Lesson Hero Header */}
          <div className="p-8 rounded-3xl bg-gradient-to-br from-white to-purple-50/40 dark:from-slate-900/90 dark:to-purple-950/20 border border-slate-200/80 dark:border-slate-800/80 shadow-md space-y-4">
            <div className="flex items-center gap-2">
              <span className="px-3 py-1 rounded-full text-xs font-black bg-purple-600 text-white uppercase tracking-wider">
                {lesson.lessonNumber}-DARS
              </span>
              {lesson.date && (
                <span className="text-xs text-slate-500 dark:text-slate-400 font-semibold">
                  📅 {lesson.date}
                </span>
              )}
            </div>

            <h1 className="text-2xl md:text-3xl font-black text-slate-900 dark:text-white leading-tight">
              {lesson.title}
            </h1>

            {lesson.goal && (
              <p className="text-sm text-slate-600 dark:text-slate-300 font-medium leading-relaxed border-l-4 border-purple-500 pl-4 py-1 bg-purple-50/50 dark:bg-purple-950/30 rounded-r-xl">
                <strong>🎯 Dars maqsadi:</strong> {lesson.goal}
              </p>
            )}
          </div>

          {/* Tab Navigation */}
          <div className="flex items-center gap-2 border-b border-slate-200 dark:border-slate-800 overflow-x-auto pb-1 no-scrollbar text-xs font-bold">
            <button
              onClick={() => setActiveTab('docs')}
              className={`py-2.5 px-4 rounded-xl transition flex items-center gap-1.5 whitespace-nowrap cursor-pointer ${
                activeTab === 'docs' 
                  ? 'bg-purple-600 text-white shadow-md' 
                  : 'text-slate-600 dark:text-slate-400 hover:bg-slate-100 dark:hover:bg-slate-800'
              }`}
            >
              <FileText className="w-4 h-4" /> Dokumentatsiya
            </button>

            {lesson.codeExamples && lesson.codeExamples.length > 0 && (
              <button
                onClick={() => setActiveTab('code')}
                className={`py-2.5 px-4 rounded-xl transition flex items-center gap-1.5 whitespace-nowrap cursor-pointer ${
                  activeTab === 'code' 
                    ? 'bg-purple-600 text-white shadow-md' 
                    : 'text-slate-600 dark:text-slate-400 hover:bg-slate-100 dark:hover:bg-slate-800'
                }`}
              >
                <Code className="w-4 h-4" /> Kod Misollari ({lesson.codeExamples.length})
              </button>
            )}

            {lesson.tasks && lesson.tasks.length > 0 && (
              <button
                onClick={() => setActiveTab('practice')}
                className={`py-2.5 px-4 rounded-xl transition flex items-center gap-1.5 whitespace-nowrap cursor-pointer ${
                  activeTab === 'practice' 
                    ? 'bg-purple-600 text-white shadow-md' 
                    : 'text-slate-600 dark:text-slate-400 hover:bg-slate-100 dark:hover:bg-slate-800'
                }`}
              >
                <Target className="w-4 h-4" /> Amaliy Topshiriqlar ({lesson.tasks.length})
              </button>
            )}

            {lesson.homework && (
              <button
                onClick={() => setActiveTab('homework')}
                className={`py-2.5 px-4 rounded-xl transition flex items-center gap-1.5 whitespace-nowrap cursor-pointer ${
                  activeTab === 'homework' 
                    ? 'bg-purple-600 text-white shadow-md' 
                    : 'text-slate-600 dark:text-slate-400 hover:bg-slate-100 dark:hover:bg-slate-800'
                }`}
              >
                <BookOpen className="w-4 h-4" /> Uyga Vazifa
              </button>
            )}

            {lesson.quizQuestions && lesson.quizQuestions.length > 0 && (
              <button
                onClick={() => setActiveTab('quiz')}
                className={`py-2.5 px-4 rounded-xl transition flex items-center gap-1.5 whitespace-nowrap cursor-pointer ${
                  activeTab === 'quiz' 
                    ? 'bg-purple-600 text-white shadow-md' 
                    : 'text-slate-600 dark:text-slate-400 hover:bg-slate-100 dark:hover:bg-slate-800'
                }`}
              >
                <HelpCircle className="w-4 h-4 text-yellow-300" /> Test Savollari ({lesson.quizQuestions.length})
              </button>
            )}
          </div>

          {/* TAB 1: DOCUMENTATION */}
          {activeTab === 'docs' && (
            <div className="animate-fadeIn">
              <MarkdownDocRenderer content={lesson.content} />
            </div>
          )}

          {/* TAB 2: CODE EXAMPLES */}
          {activeTab === 'code' && lesson.codeExamples && (
            <div className="space-y-6 animate-fadeIn">
              {lesson.codeExamples.map((example, idx) => (
                <div key={idx} className="p-6 rounded-2xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 shadow-sm space-y-3">
                  <h3 className="font-bold text-sm text-slate-900 dark:text-white flex items-center gap-2">
                    <Code className="w-4 h-4 text-purple-500" /> Misol #{idx + 1}: {example.title}
                  </h3>
                  {example.description && <p className="text-xs text-slate-500 dark:text-slate-400">{example.description}</p>}
                  <CodeBlock code={example.code} language={example.language || 'python'} filename={`misol_${idx + 1}.py`} />
                </div>
              ))}
            </div>
          )}

          {/* TAB 3: PRACTICE TASKS */}
          {activeTab === 'practice' && lesson.tasks && (
            <div className="space-y-4 animate-fadeIn">
              {lesson.tasks.map((task, idx) => (
                <div key={idx} className="p-5 rounded-2xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 shadow-sm space-y-2">
                  <span className="px-2.5 py-0.5 rounded-md bg-purple-100 dark:bg-purple-950/60 text-purple-700 dark:text-purple-300 font-extrabold text-[10px] uppercase">
                    Topshiriq #{idx + 1}
                  </span>
                  <h4 className="font-bold text-sm text-slate-900 dark:text-white">{task.title}</h4>
                  <p className="text-xs text-slate-600 dark:text-slate-300 leading-relaxed">{task.description}</p>
                </div>
              ))}
            </div>
          )}

          {/* TAB 4: HOMEWORK */}
          {activeTab === 'homework' && lesson.homework && (
            <div className="p-6 rounded-2xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 shadow-sm space-y-4 animate-fadeIn">
              <h3 className="font-bold text-base text-slate-900 dark:text-white flex items-center gap-2">
                <BookOpen className="w-5 h-5 text-purple-500" /> Uyga Vazifa Topshiriqlari
              </h3>
              <MarkdownDocRenderer content={lesson.homework} />
            </div>
          )}

          {/* TAB 5: QUIZ */}
          {activeTab === 'quiz' && lesson.quizQuestions && (
            <div className="space-y-6 animate-fadeIn">
              {lesson.quizQuestions.map((q, idx) => (
                <div key={q.id || idx} className="p-6 rounded-2xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 shadow-sm space-y-4">
                  <h4 className="font-bold text-sm text-slate-900 dark:text-white">
                    {idx + 1}. {q.question}
                  </h4>
                  <div className="space-y-2">
                    {q.options.map((opt, optIdx) => {
                      const isSelected = selectedQuizAnswers[q.id || idx.toString()] === optIdx;
                      const isCorrect = optIdx === q.correctAnswer;
                      return (
                        <button
                          key={optIdx}
                          onClick={() => handleQuizSelect(q.id || idx.toString(), optIdx)}
                          className={`w-full p-3.5 rounded-xl border text-left text-xs font-semibold transition-all flex items-center justify-between cursor-pointer ${
                            isSelected
                              ? isCorrect
                                ? 'bg-emerald-50 dark:bg-emerald-950/40 border-emerald-500 text-emerald-700 dark:text-emerald-300'
                                : 'bg-rose-50 dark:bg-rose-950/40 border-rose-500 text-rose-700 dark:text-rose-300'
                              : 'bg-slate-50 dark:bg-slate-800/50 border-slate-200 dark:border-slate-700 hover:border-purple-400'
                          }`}
                        >
                          <span>{opt}</span>
                          {isSelected && (isCorrect ? "✅ To'g'ri" : "❌ Noto'g'ri")}
                        </button>
                      );
                    })}
                  </div>
                </div>
              ))}
            </div>
          )}
        </div>

        {/* Right Desktop Table of Contents */}
        {activeTab === 'docs' && (
          <div className="hidden lg:block">
            <TableOfContents content={lesson.content} />
          </div>
        )}
      </main>

      {/* Mobile Drawer */}
      {mobileTocOpen && (
        <div className="fixed inset-0 z-50 bg-slate-900/60 backdrop-blur-xs flex justify-end lg:hidden animate-fadeIn">
          <div className="w-80 max-w-[85vw] bg-white dark:bg-slate-900 h-full p-6 shadow-2xl flex flex-col justify-between overflow-y-auto">
            <div>
              <div className="flex items-center justify-between border-b border-slate-200 dark:border-slate-800 pb-3 mb-4">
                <div className="flex items-center gap-2 font-bold text-sm text-slate-900 dark:text-white">
                  <List className="w-4 h-4 text-purple-500" /> Mundarija
                </div>
                <button
                  onClick={() => setMobileTocOpen(false)}
                  className="p-1 rounded-lg text-slate-400 hover:text-slate-600 dark:hover:text-slate-200"
                >
                  ✕
                </button>
              </div>
              <TableOfContents 
                content={lesson.content} 
                onSelectHeading={() => setMobileTocOpen(false)} 
              />
            </div>
            <button
              onClick={() => setMobileTocOpen(false)}
              className="mt-6 w-full py-2.5 bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-300 font-bold text-xs rounded-xl"
            >
              Yopish
            </button>
          </div>
        </div>
      )}

      <footer className="p-6 border-t border-slate-200 dark:border-slate-800/80 text-center text-xs text-slate-500 dark:text-slate-400">
        © 2026 marimovdev. Barcha huquqlar himoyalangan.
      </footer>
    </div>
  );
};
