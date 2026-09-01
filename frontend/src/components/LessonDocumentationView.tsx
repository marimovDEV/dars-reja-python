import React, { useState } from 'react';
import { 
  Printer, 
  Copy, 
  Check, 
  Edit3, 
  FileText, 
  Clock, 
  CheckCircle2, 
  Calendar, 
  Download, 
  Eye, 
  Paperclip, 
  HelpCircle, 
  BookOpen, 
  Trash2,
  Plus,
  Target,
  Code,
  Users,
  Sparkles,
  ExternalLink,
  Tag,
  List
} from 'lucide-react';
import { Lesson, LessonStatus, LessonMaterial } from '../types';
import { MarkdownDocRenderer } from './MarkdownDocRenderer';
import { TableOfContents } from './TableOfContents';
import { CodeBlock } from './CodeBlock';
import { DocCallout } from './DocCallout';

interface LessonDocumentationViewProps {
  lesson: Lesson;
  onUpdateStatus: (lessonId: string, status: LessonStatus) => void;
  onOpenEditModal: (lesson: Lesson) => void;
  onPreviewMaterial: (material: LessonMaterial) => void;
  onAddMaterial: (lessonId: string) => void;
  onDeleteLesson: (lessonId: string) => void;
  notionSettings?: any;
  onOpenSyncModal?: () => void;
}

export const LessonDocumentationView: React.FC<LessonDocumentationViewProps> = ({
  lesson,
  onUpdateStatus,
  onOpenEditModal,
  onPreviewMaterial,
  onAddMaterial,
  onDeleteLesson,
  notionSettings,
  onOpenSyncModal,
}) => {
  // 6 TA ASOSIY TABLAR
  const [activeTab, setActiveTab] = useState<'docs' | 'code' | 'practice' | 'homework' | 'quiz' | 'resources'>('docs');
  const [copied, setCopied] = useState(false);
  const [selectedQuizAnswers, setSelectedQuizAnswers] = useState<Record<string, number>>({});
  const [mobileTocOpen, setMobileTocOpen] = useState(false);

  const handleQuizSelect = (quizId: string, optionIdx: number) => {
    setSelectedQuizAnswers(prev => ({
      ...prev,
      [quizId]: optionIdx
    }));
  };

  const handleCopyDoc = () => {
    navigator.clipboard.writeText(lesson.content || '');
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  };

  const handlePrint = () => {
    window.print();
  };

  const handleDelete = () => {
    if (window.confirm("Haqiqatan ham ushbu dars rejasini o'chirmoqchimisiz?")) {
      onDeleteLesson(lesson.id);
    }
  };

  const isExam = lesson.lessonNumber % 12 === 0;

  return (
    <main 
      id="lesson-documentation-view"
      className="flex-1 bg-slate-50 dark:bg-[#070A12] text-slate-800 dark:text-slate-200 font-['Inter',sans-serif] overflow-y-auto h-screen flex flex-col"
    >
      {/* Top sticky action banner */}
      <div 
        id="doc-header-actionbar"
        className="sticky top-0 z-30 bg-white/90 dark:bg-[#0B0F19]/90 backdrop-blur-md border-b border-slate-200 dark:border-slate-800/80 px-6 py-3 flex flex-wrap items-center justify-between gap-3 shadow-xs"
      >
        <div className="flex items-center gap-3">
          <span className={`px-3 py-1 rounded-full text-[11px] font-bold tracking-wider uppercase ${isExam ? 'bg-amber-500 text-white' : 'bg-blue-600 text-white'}`}>
            {isExam ? `🎓 IMTIHON (${lesson.lessonNumber}-DARS)` : `${lesson.lessonNumber}-DARS DOKUMENTATSIYASI`}
          </span>
          <span className="text-xs text-slate-500 dark:text-slate-400 font-medium hidden sm:inline-block">
            Progress: <strong className="text-slate-900 dark:text-white font-bold">{lesson.lessonNumber} / 72</strong> dars
          </span>
        </div>

        <div className="flex items-center gap-2">
          {/* Mobile TOC Button */}
          <button
            onClick={() => setMobileTocOpen(!mobileTocOpen)}
            className="lg:hidden flex items-center gap-1.5 px-3 py-1.5 text-xs font-semibold text-slate-700 dark:text-slate-200 bg-slate-100 dark:bg-slate-800 rounded-lg"
          >
            <List className="w-4 h-4 text-blue-500" />
            <span>Mundarija</span>
          </button>

          {/* Status selector */}
          <div className="flex items-center bg-slate-100 dark:bg-slate-800/80 p-0.5 rounded-lg border border-slate-200 dark:border-slate-700/60">
            {(['planned', 'pending', 'completed'] as LessonStatus[]).map((st) => (
              <button
                key={st}
                onClick={() => onUpdateStatus(lesson.id, st)}
                className={`px-2.5 py-1 rounded-md text-[11px] font-bold transition-all ${
                  lesson.status === st 
                    ? st === 'completed'
                      ? 'bg-emerald-600 text-white shadow-xs'
                      : st === 'pending'
                      ? 'bg-amber-500 text-white shadow-xs'
                      : 'bg-blue-600 text-white shadow-xs'
                    : 'text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-white'
                }`}
              >
                {st === 'completed' ? 'Tugallandi' : st === 'pending' ? 'Jarayonda' : 'Reja'}
              </button>
            ))}
          </div>

          <button
            onClick={() => onOpenEditModal(lesson)}
            className="flex items-center gap-1.5 px-3 py-1.5 text-xs font-medium text-slate-700 dark:text-slate-200 bg-slate-100 dark:bg-slate-800 hover:bg-slate-200 dark:hover:bg-slate-700 rounded-lg transition-colors"
          >
            <Edit3 className="w-3.5 h-3.5 text-slate-500" />
            <span className="hidden sm:inline">Tahrirlash</span>
          </button>

          <button
            onClick={handleCopyDoc}
            className="flex items-center gap-1.5 px-3 py-1.5 text-xs font-medium text-slate-700 dark:text-slate-200 bg-slate-100 dark:bg-slate-800 hover:bg-slate-200 dark:hover:bg-slate-700 rounded-lg transition-colors"
          >
            {copied ? <Check className="w-3.5 h-3.5 text-emerald-500" /> : <Copy className="w-3.5 h-3.5 text-slate-500" />}
            <span className="hidden sm:inline">{copied ? 'Nusxalandi!' : 'Nusxalash'}</span>
          </button>

          <button
            onClick={handlePrint}
            className="p-1.5 text-slate-600 dark:text-slate-400 hover:bg-slate-100 dark:hover:bg-slate-800 rounded-lg transition-colors"
            title="Chop etish"
          >
            <Printer className="w-4 h-4" />
          </button>

          <button
            onClick={handleDelete}
            className="p-1.5 text-rose-500 hover:bg-rose-50 dark:hover:bg-rose-950/40 rounded-lg transition-colors"
            title="O'chirish"
          >
            <Trash2 className="w-4 h-4" />
          </button>
        </div>
      </div>

      {/* Main Layout Area */}
      <div className="max-w-7xl w-full mx-auto p-6 md:p-10 flex gap-10 flex-1">
        
        {/* Central Documentation Column (Max 900px) */}
        <div className="flex-1 max-w-[900px] space-y-8 mx-auto lg:mx-0">
          
          {/* HERO HEADER */}
          <header className="space-y-4 border-b border-slate-200 dark:border-slate-800 pb-8">
            <div className="flex flex-wrap items-center gap-2">
              <span className="px-2.5 py-1 rounded-md text-xs font-extrabold bg-blue-100 dark:bg-blue-950 text-blue-700 dark:text-blue-300">
                {lesson.lessonNumber}-DARS
              </span>
              <div className="flex items-center gap-1.5 text-xs font-medium text-slate-500 dark:text-slate-400">
                <Clock className="w-3.5 h-3.5 text-amber-500" />
                <span>O'qish vaqti: ~25 daqiqa</span>
              </div>
              <span className="text-slate-300 dark:text-slate-700">•</span>
              <div className="flex items-center gap-1 text-xs text-slate-500 dark:text-slate-400">
                <Tag className="w-3.5 h-3.5 text-blue-500" />
                <span>Python, Backend, Amaliyot</span>
              </div>
            </div>

            <h1 className="text-3xl md:text-4xl font-extrabold text-slate-900 dark:text-white tracking-tight leading-tight">
              {lesson.title}
            </h1>

            <p className="text-base text-slate-600 dark:text-slate-300 leading-relaxed font-sans">
              {lesson.description || lesson.goal || `${lesson.title} bo'yicha to'liq va amaliy ko'rsatmalarni o'z ichiga olgan rasmiy o'quv dokumentatsiyasi.`}
            </p>

            {/* Progress Bar */}
            <div className="pt-2">
              <div className="flex items-center justify-between text-xs text-slate-500 mb-1.5 font-medium">
                <span>Kurs bo'yicha o'zlashtirish</span>
                <span className="font-bold text-blue-600 dark:text-blue-400">{Math.round((lesson.lessonNumber / 72) * 100)}% ({lesson.lessonNumber} / 72 dars)</span>
              </div>
              <div className="w-full h-2 bg-slate-200 dark:bg-slate-800 rounded-full overflow-hidden">
                <div 
                  className="h-full bg-gradient-to-r from-blue-600 to-indigo-500 rounded-full transition-all duration-300"
                  style={{ width: `${(lesson.lessonNumber / 72) * 100}%` }}
                />
              </div>
            </div>
          </header>

          {/* 6 MAIN TABS */}
          <nav className="flex items-center gap-2 border-b border-slate-200 dark:border-slate-800 pb-2 overflow-x-auto scrollbar-none">
            {[
              { id: 'docs', label: '📖 Dokumentatsiya' },
              { id: 'code', label: '💻 Kod misollari' },
              { id: 'practice', label: '🧪 Amaliyot' },
              { id: 'homework', label: '🏠 Uyga vazifa' },
              { id: 'quiz', label: '❓ Savollar' },
              { id: 'resources', label: '📎 Fayllar va resurslar' },
            ].map((tab) => {
              const isActive = activeTab === tab.id;
              return (
                <button
                  key={tab.id}
                  onClick={() => setActiveTab(tab.id as any)}
                  className={`px-4 py-2.5 rounded-xl text-xs font-bold whitespace-nowrap transition-all ${
                    isActive
                      ? 'bg-blue-600 text-white shadow-md shadow-blue-600/20'
                      : 'bg-white dark:bg-slate-900 text-slate-700 dark:text-slate-300 border border-slate-200 dark:border-slate-800 hover:bg-slate-100 dark:hover:bg-slate-800'
                  }`}
                >
                  {tab.label}
                </button>
              );
            })}
          </nav>

          {/* TAB 1: DOKUMENTATSIYA (MARKDOWN RENDERER) */}
          {activeTab === 'docs' && (
            <article className="bg-white dark:bg-[#0B101D] rounded-2xl p-6 md:p-10 border border-slate-200 dark:border-slate-800/80 shadow-md">
              <MarkdownDocRenderer content={lesson.content} />
            </article>
          )}

          {/* TAB 2: KOD MISOLLARI */}
          {activeTab === 'code' && (
            <section className="bg-white dark:bg-[#0B101D] rounded-2xl p-6 md:p-8 border border-slate-200 dark:border-slate-800/80 shadow-md space-y-6">
              <div className="flex items-center gap-2 text-lg font-bold text-slate-900 dark:text-white border-b border-slate-200 dark:border-slate-800 pb-3">
                <Code className="w-5 h-5 text-blue-500" />
                <h2>💻 KOD MISOLLARI VA QATORMA-QATOR IZOHLAR</h2>
              </div>

              {lesson.codeExamples && lesson.codeExamples.length > 0 ? (
                lesson.codeExamples.map((c, idx) => (
                  <div key={c.id || idx} className="space-y-3">
                    <h3 className="text-sm font-bold text-slate-900 dark:text-white">{c.title}</h3>
                    <CodeBlock code={c.code} language={c.language} />
                    {c.explanation && (
                      <DocCallout type="tip" title="Line-by-Line Izoh:">
                        <div className="whitespace-pre-line text-xs font-sans leading-relaxed">
                          {c.explanation}
                        </div>
                      </DocCallout>
                    )}
                  </div>
                ))
              ) : (
                <div className="text-sm text-slate-400 italic">Kod misollari kiritilmagan.</div>
              )}
            </section>
          )}

          {/* TAB 3: AMALIYOT */}
          {activeTab === 'practice' && (
            <section className="bg-white dark:bg-[#0B101D] rounded-2xl p-6 md:p-8 border border-slate-200 dark:border-slate-800/80 shadow-md space-y-6">
              <div className="flex items-center gap-2 text-lg font-bold text-slate-900 dark:text-white border-b border-slate-200 dark:border-slate-800 pb-3">
                <Sparkles className="w-5 h-5 text-purple-500" />
                <h2>🧪 SINFDAGI VA MUSTAQIL AMALIY TOPSHIRIQ LAR</h2>
              </div>

              <div className="space-y-5">
                <DocCallout type="practice" title="1-Topshiriq — Oson">
                  Darsda o'tilgan asosiy tushunchalar bo'yicha 1-sodda amaliy mashqni yozing va konsolda tekshiring.
                </DocCallout>

                <DocCallout type="info" title="2-Topshiriq — O'rta">
                  Berilgan shartli operatorlar va algoritmik mantiqni birlashtiruvchi amaliy masala yeching.
                </DocCallout>

                <DocCallout type="warning" title="3-Topshiriq — Murakkab">
                  Real loyihaga yaqin kichik algoritm yoki funksionallikni yaratish va xatolarni tahlil qilish.
                </DocCallout>
              </div>
            </section>
          )}

          {/* TAB 4: UYGA VAZIFA */}
          {activeTab === 'homework' && (
            <section className="bg-white dark:bg-[#0B101D] rounded-2xl p-6 md:p-8 border border-slate-200 dark:border-slate-800/80 shadow-md space-y-6">
              <div className="flex items-center gap-2 text-lg font-bold text-slate-900 dark:text-white border-b border-slate-200 dark:border-slate-800 pb-3">
                <CheckCircle2 className="w-5 h-5 text-emerald-500" />
                <h2>🏠 UYGA VAZIFA VA TOPSHIRISH TALABLARI</h2>
              </div>

              <DocCallout type="homework" title="Uyga Vazifa Topshirig'i:">
                <div className="whitespace-pre-line font-medium text-slate-800 dark:text-slate-200 text-sm">
                  {lesson.homework || 'Uyga vazifa biriktirilmagan.'}
                </div>
              </DocCallout>

              <div className="p-5 bg-slate-50 dark:bg-slate-900/60 rounded-xl border border-slate-200 dark:border-slate-800 text-sm space-y-2">
                <div className="font-bold text-slate-900 dark:text-white">Uyga vazifa topshirish talabi:</div>
                <ul className="list-disc list-inside space-y-1 text-slate-600 dark:text-slate-300 text-xs">
                  <li>Kod <code>.py</code> faylida bo'lsin;</li>
                  <li>Fayl nomi: <code>{lesson.lessonNumber}_dars_homework.py</code>;</li>
                  <li>Tushunarli o'zgaruvchi nomlari ishlatilsin;</li>
                  <li>Kodda kamida bitta izoh (#) yozilsin.</li>
                </ul>
              </div>
            </section>
          )}

          {/* TAB 5: SAVOLLAR & TESTLAR */}
          {activeTab === 'quiz' && (
            <section className="bg-white dark:bg-[#0B101D] rounded-2xl p-6 md:p-8 border border-slate-200 dark:border-slate-800/80 shadow-md space-y-6">
              <div className="flex items-center gap-2 text-lg font-bold text-slate-900 dark:text-white border-b border-slate-200 dark:border-slate-800 pb-3">
                <HelpCircle className="w-5 h-5 text-amber-500" />
                <h2>❓ TEKSHIRISH SAVOLLARI VA TESTLAR</h2>
              </div>

              {lesson.quizQuestions && lesson.quizQuestions.length > 0 ? (
                <div className="space-y-4">
                  {lesson.quizQuestions.map((q, idx) => {
                    const selected = selectedQuizAnswers[q.id];
                    const isAnswered = selected !== undefined;
                    const isCorrect = selected === q.correctIndex;

                    return (
                      <div key={q.id || idx} className="p-4 rounded-xl border border-slate-200 dark:border-slate-800 space-y-3 bg-slate-50/50 dark:bg-slate-900/40">
                        <div className="text-sm font-bold text-slate-900 dark:text-white">
                          {idx + 1}. {q.question}
                        </div>

                        <div className="grid grid-cols-1 sm:grid-cols-2 gap-2">
                          {q.options.map((opt, optIdx) => {
                            let btnStyle = "border-slate-200 dark:border-slate-700 hover:bg-slate-100 dark:hover:bg-slate-800 text-slate-700 dark:text-slate-300";
                            if (isAnswered) {
                              if (optIdx === q.correctIndex) {
                                btnStyle = "bg-emerald-600 text-white font-bold border-emerald-600 shadow-xs";
                              } else if (selected === optIdx) {
                                btnStyle = "bg-rose-600 text-white font-bold border-rose-600";
                              }
                            }

                            return (
                              <button
                                key={optIdx}
                                onClick={() => handleQuizSelect(q.id, optIdx)}
                                className={`p-3 rounded-lg border text-left text-xs font-medium transition-all ${btnStyle}`}
                              >
                                <span className="font-bold mr-1.5">{String.fromCharCode(65 + optIdx)})</span>
                                {opt}
                              </button>
                            );
                          })}
                        </div>

                        {isAnswered && (
                          <div className={`p-3 rounded-lg text-xs border ${isCorrect ? 'bg-emerald-50 text-emerald-800 border-emerald-200 dark:bg-emerald-950/40 dark:text-emerald-200' : 'bg-rose-50 text-rose-800 border-rose-200 dark:bg-rose-950/40 dark:text-rose-200'}`}>
                            <span className="font-bold">{isCorrect ? "✅ To'g'ri javob!" : "❌ Noto'g'ri javob."} </span>
                            <span>{q.explanation}</span>
                          </div>
                        )}
                      </div>
                    );
                  })}
                </div>
              ) : (
                <div className="text-sm text-slate-400 italic">Savollar mavjud emas.</div>
              )}
            </section>
          )}

          {/* TAB 6: FAYLLAR VA RESURSLAR */}
          {activeTab === 'resources' && (
            <section className="bg-white dark:bg-[#0B101D] rounded-2xl p-6 md:p-8 border border-slate-200 dark:border-slate-800/80 shadow-md space-y-6">
              <div className="flex items-center justify-between border-b border-slate-200 dark:border-slate-800 pb-3">
                <div className="flex items-center gap-2 text-lg font-bold text-slate-900 dark:text-white">
                  <Paperclip className="w-5 h-5 text-blue-500" />
                  <h2>📎 FAYLLAR VA RESURSLAR</h2>
                </div>
                <button
                  onClick={() => onAddMaterial(lesson.id)}
                  className="flex items-center gap-1 text-xs font-bold text-blue-600 dark:text-blue-400 hover:underline"
                >
                  <Plus className="w-3.5 h-3.5" />
                  <span>Resurs qo'shish</span>
                </button>
              </div>

              <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
                <div className="p-4 rounded-xl border border-slate-200 dark:border-slate-800 flex items-center justify-between bg-slate-50/50 dark:bg-slate-900/40">
                  <div className="flex items-center gap-3">
                    <FileText className="w-7 h-7 text-rose-500 shrink-0" />
                    <div>
                      <div className="text-xs font-bold text-slate-900 dark:text-white">📄 PDF Konspekt</div>
                      <div className="text-[11px] text-slate-500">{lesson.lessonNumber}_dars_konspekt.pdf</div>
                    </div>
                  </div>
                </div>

                <div className="p-4 rounded-xl border border-slate-200 dark:border-slate-800 flex items-center justify-between bg-slate-50/50 dark:bg-slate-900/40">
                  <div className="flex items-center gap-3">
                    <Code className="w-7 h-7 text-emerald-500 shrink-0" />
                    <div>
                      <div className="text-xs font-bold text-slate-900 dark:text-white">💻 GitHub Kodlari</div>
                      <div className="text-[11px] text-slate-500">github.com/dars-reja/{lesson.lessonNumber}</div>
                    </div>
                  </div>
                </div>

                <div className="p-4 rounded-xl border border-slate-200 dark:border-slate-800 flex items-center justify-between bg-slate-50/50 dark:bg-slate-900/40">
                  <div className="flex items-center gap-3">
                    <ExternalLink className="w-7 h-7 text-purple-500 shrink-0" />
                    <div>
                      <div className="text-xs font-bold text-slate-900 dark:text-white">🎬 HD Video Darslik</div>
                      <div className="text-[11px] text-slate-500">YouTube / Drive video yozuvi</div>
                    </div>
                  </div>
                </div>
              </div>
            </section>
          )}

        </div>

        {/* Right Sticky Table of Contents Column (Desktop) */}
        {activeTab === 'docs' && (
          <div className="hidden lg:block">
            <TableOfContents content={lesson.content} />
          </div>
        )}

      </div>

      {/* Mobile Table of Contents Modal Drawer */}
      {mobileTocOpen && activeTab === 'docs' && (
        <div className="fixed inset-0 z-50 bg-slate-900/60 backdrop-blur-xs flex justify-end lg:hidden animate-fadeIn">
          <div className="w-80 max-w-[85vw] bg-white dark:bg-slate-900 h-full p-6 shadow-2xl flex flex-col justify-between overflow-y-auto">
            <div>
              <div className="flex items-center justify-between border-b border-slate-200 dark:border-slate-800 pb-3 mb-4">
                <div className="flex items-center gap-2 font-bold text-sm text-slate-900 dark:text-white">
                  <List className="w-4 h-4 text-blue-500" /> Mundarija
                </div>
                <button
                  onClick={() => setMobileTocOpen(false)}
                  className="p-1 rounded-lg text-slate-400 hover:text-slate-600 dark:hover:text-slate-200 cursor-pointer"
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
              className="mt-6 w-full py-2.5 bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-300 font-bold text-xs rounded-xl cursor-pointer"
            >
              Yopish
            </button>
          </div>
        </div>
      )}
    </main>
  );
};
