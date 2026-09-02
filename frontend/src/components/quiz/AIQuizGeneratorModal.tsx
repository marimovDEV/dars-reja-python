import React, { useState, useEffect } from 'react';
import { Quiz, QuizQuestion } from '../../types/quiz';
import { Sparkles, Check, BookOpen, Clock, Code, HelpCircle, Layers, Flame, ArrowRight, Loader2, Bookmark, Plus, Trash2, LayoutGrid, CheckCircle } from 'lucide-react';
import { Lesson } from '../../types';

interface AIQuizGeneratorModalProps {
  isOpen: boolean;
  onClose: () => void;
  lessons: Lesson[];
  onQuizGenerated: (quiz: Quiz) => void;
}

export interface QuizTemplate {
  id: string;
  title: string;
  description: string;
  category: string;
  questionCount: number;
  difficulty: 'easy' | 'medium' | 'hard' | 'mixed';
  lessonIds: number[];
  customQuestions?: QuizQuestion[];
}

const DEFAULT_TEMPLATES: QuizTemplate[] = [
  {
    id: 'master-tpl-1-to-23',
    title: '🏆 Marimov Game Zone: 1-darsdan 23-darsgacha Kompleks 30 ta Test',
    description: "1-darsdan 23-darsgacha bo'lgan barcha Python mavzulari (Sintaksis, List/Dict/Set, Funktsiyalar, OOP, Exceptions, File I/O, Decorators) bo'yicha mukammal 30 ta qiyin va amaliy savollar.",
    category: 'Marimov Game Master',
    questionCount: 30,
    difficulty: 'hard',
    lessonIds: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
  },
  {
    id: 'tpl-1',
    title: "🐍 Python Sintaksisi va Boshlang'ich Tushunchalar",
    description: "1-modul: O'zgaruvchilar, ma'lumot turlari, if/else va sikllar bo'yicha 10 ta oson va o'rta savollar.",
    category: 'Python Asoslari',
    questionCount: 10,
    difficulty: 'easy',
    lessonIds: [1, 2, 3, 4, 5, 6]
  },
  {
    id: 'tpl-2',
    title: '⚡ Django Apps, Views, Models & ORM',
    description: "4-modul: Django backend strukturasi, ORM so'rovlari va admin panel bo'yicha 15 ta texnik savol.",
    category: 'Django Backend',
    questionCount: 15,
    difficulty: 'medium',
    lessonIds: [37, 38, 39, 40, 41, 42, 43, 44]
  },
  {
    id: 'tpl-3',
    title: '🚀 REST API, DRF Serializers & Authentication',
    description: "5-modul: DRF, JWT tokenlar, Swagger va ruxsatnomalar bo'yicha 20 ta amaliy savol.",
    category: 'DRF & Security',
    questionCount: 20,
    difficulty: 'hard',
    lessonIds: [49, 50, 51, 52, 53, 54, 55, 56]
  }
];

export function AIQuizGeneratorModal({
  isOpen,
  onClose,
  lessons,
  onQuizGenerated
}: AIQuizGeneratorModalProps) {
  const [activeMode, setActiveMode] = useState<'lessons' | 'templates'>('lessons');

  // Mode 1 State: Lessons
  const [selectedLessonIds, setSelectedLessonIds] = useState<number[]>([1, 2, 3]);
  const [questionCount, setQuestionCount] = useState<number>(10);
  const [difficulty, setDifficulty] = useState<'easy' | 'medium' | 'hard' | 'mixed'>('mixed');
  const [includeCode, setIncludeCode] = useState<boolean>(true);

  // Mode 2 State: Templates
  const [templates, setTemplates] = useState<QuizTemplate[]>(() => {
    try {
      const saved = localStorage.getItem('marimov_quiz_templates');
      return saved ? JSON.parse(saved) : DEFAULT_TEMPLATES;
    } catch {
      return DEFAULT_TEMPLATES;
    }
  });

  const [selectedTemplateId, setSelectedTemplateId] = useState<string>(DEFAULT_TEMPLATES[0].id);
  const [isCreatingTemplate, setIsCreatingTemplate] = useState<boolean>(false);

  // New Template Form State
  const [newTplTitle, setNewTplTitle] = useState('');
  const [newTplDesc, setNewTplDesc] = useState('');
  const [newTplCategory, setNewTplCategory] = useState('Python Backend');
  const [newTplCount, setNewTplCount] = useState<number>(10);
  const [newTplDifficulty, setNewTplDifficulty] = useState<'easy' | 'medium' | 'hard' | 'mixed'>('medium');

  const [loading, setLoading] = useState<boolean>(false);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    if (!isOpen) return;
    const fetchTemplates = async () => {
      try {
        const res = await fetch('/api/quiz-templates');
        if (res.ok) {
          const data = await res.json();
          if (Array.isArray(data) && data.length > 0) {
            setTemplates(data);
            setSelectedTemplateId(data[0].id);
          }
        }
      } catch (e) {
        console.error("Backend templates fetch error:", e);
      }
    };
    fetchTemplates();
  }, [isOpen]);

  useEffect(() => {
    try {
      localStorage.setItem('marimov_quiz_templates', JSON.stringify(templates));
    } catch (e) {}
  }, [templates]);

  if (!isOpen) return null;

  const toggleLesson = (lessonNum: number) => {
    if (selectedLessonIds.includes(lessonNum)) {
      if (selectedLessonIds.length === 1) return; // Keep at least 1
      setSelectedLessonIds(selectedLessonIds.filter(id => id !== lessonNum));
    } else {
      setSelectedLessonIds([...selectedLessonIds, lessonNum].sort((a, b) => a - b));
    }
  };

  const selectAllLessons = () => {
    setSelectedLessonIds(lessons.map(l => l.lessonNumber));
  };

  const clearLessons = () => {
    setSelectedLessonIds([1]);
  };

  // Generate via Mode 1 (Selected Lessons)
  const handleGenerateFromLessons = async () => {
    if (selectedLessonIds.length === 0) {
      setError("Kamida 1 ta darsni belgilang");
      return;
    }

    setLoading(true);
    setError(null);

    try {
      const res = await fetch('/api/ai/quizzes/generate', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          lessonIds: selectedLessonIds,
          questionCount,
          difficulty,
          includeCodeQuestions: includeCode,
          language: 'uz'
        })
      });

      if (!res.ok) {
        const errData = await res.json();
        throw new Error(errData.error || "Quiz yaratishda xatolik yuz berdi");
      }

      const data = await res.json();
      const generatedQuestions: QuizQuestion[] = data.questions;

      const title = `AI Quiz: ${selectedLessonIds.length} ta dars (${questionCount} savol)`;
      const saveRes = await fetch('/api/quizzes', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          title,
          lessonIds: selectedLessonIds,
          questions: generatedQuestions
        })
      });

      const savedQuiz: Quiz = await saveRes.json();
      onQuizGenerated(savedQuiz);
      onClose();
    } catch (err: any) {
      setError(err.message || "AI Generator xatoligi yuz berdi");
    } finally {
      setLoading(false);
    }
  };

  // Generate via Mode 2 (Selected Template)
  const handleGenerateFromTemplate = async () => {
    const tpl = templates.find(t => t.id === selectedTemplateId);
    if (!tpl) {
      setError("Shablon tanlanmadi");
      return;
    }

    setLoading(true);
    setError(null);

    try {
      let finalQuestions: QuizQuestion[] = tpl.customQuestions || [];

      if (finalQuestions.length === 0) {
        const res = await fetch('/api/ai/quizzes/generate', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            lessonIds: tpl.lessonIds.length > 0 ? tpl.lessonIds : [1, 2, 3],
            questionCount: tpl.questionCount,
            difficulty: tpl.difficulty,
            includeCodeQuestions: true,
            language: 'uz'
          })
        });

        if (!res.ok) {
          const errData = await res.json();
          throw new Error(errData.error || "Shablon bo'yicha generator xatosi");
        }

        const data = await res.json();
        finalQuestions = data.questions;
      }

      const saveRes = await fetch('/api/quizzes', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          title: tpl.title,
          lessonIds: tpl.lessonIds,
          questions: finalQuestions
        })
      });

      const savedQuiz: Quiz = await saveRes.json();
      onQuizGenerated(savedQuiz);
      onClose();
    } catch (err: any) {
      setError(err.message || "Shablon generatorida xatolik yuz berdi");
    } finally {
      setLoading(false);
    }
  };

  // Save new custom template to backend DB
  const handleSaveNewTemplate = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!newTplTitle.trim()) {
      setError("Shablon nomini kiriting");
      return;
    }

    const tplPayload: QuizTemplate = {
      id: `custom-tpl-${Date.now()}`,
      title: newTplTitle.trim(),
      description: newTplDesc.trim() || 'O\'qituvchi tomonidan yaratilgan maxsus shablon',
      category: newTplCategory.trim(),
      questionCount: newTplCount,
      difficulty: newTplDifficulty,
      lessonIds: selectedLessonIds.length > 0 ? selectedLessonIds : [1, 2, 3]
    };

    try {
      const res = await fetch('/api/quiz-templates', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(tplPayload)
      });
      if (res.ok) {
        const savedTpl: QuizTemplate = await res.json();
        setTemplates(prev => [savedTpl, ...prev.filter(t => t.id !== savedTpl.id)]);
        setSelectedTemplateId(savedTpl.id);
      } else {
        setTemplates(prev => [tplPayload, ...prev]);
        setSelectedTemplateId(tplPayload.id);
      }
    } catch (err) {
      setTemplates(prev => [tplPayload, ...prev]);
      setSelectedTemplateId(tplPayload.id);
    }

    setIsCreatingTemplate(false);
    setNewTplTitle('');
    setNewTplDesc('');
    setError(null);
  };

  const handleDeleteTemplate = async (id: string, e: React.MouseEvent) => {
    e.stopPropagation();
    try {
      await fetch(`/api/quiz-templates/${id}`, { method: 'DELETE' });
    } catch (e) {}

    const updated = templates.filter(t => t.id !== id);
    setTemplates(updated);
    if (selectedTemplateId === id && updated.length > 0) {
      setSelectedTemplateId(updated[0].id);
    }
  };

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-slate-900/80 backdrop-blur-md animate-fadeIn">
      <div className="bg-white dark:bg-slate-900 rounded-3xl shadow-2xl border border-slate-200 dark:border-slate-800 w-full max-w-3xl overflow-hidden flex flex-col max-h-[92vh]">
        
        {/* Header */}
        <div className="p-6 bg-gradient-to-r from-purple-600 via-indigo-600 to-blue-600 text-white relative">
          <div className="flex items-center justify-between">
            <div className="flex items-center gap-3">
              <div className="p-3 bg-white/20 backdrop-blur-md rounded-2xl">
                <Sparkles className="w-7 h-7 text-yellow-300 animate-pulse" />
              </div>
              <div>
                <h2 className="text-xl font-bold">Quiz Yaratish Paneli</h2>
                <p className="text-purple-100 text-xs mt-0.5">
                  Darsliklar bo'yicha yoki o'zingizning tayyor shablonlaringiz yordamida test yaratish
                </p>
              </div>
            </div>
            <button
              onClick={onClose}
              className="text-white/80 hover:text-white p-2 rounded-full hover:bg-white/10 transition cursor-pointer"
            >
              ✕
            </button>
          </div>

          {/* Mode Switcher Tabs */}
          <div className="flex items-center gap-2 mt-5 p-1 bg-black/20 rounded-2xl backdrop-blur-md">
            <button
              onClick={() => { setActiveMode('lessons'); setError(null); }}
              className={`flex-1 py-2.5 px-4 rounded-xl text-xs font-black transition flex items-center justify-center gap-2 cursor-pointer ${
                activeMode === 'lessons'
                  ? 'bg-white text-purple-950 shadow-lg'
                  : 'text-purple-200 hover:text-white hover:bg-white/10'
              }`}
            >
              <BookOpen className="w-4 h-4" /> 1-usul: Darsliklar Bo'yicha
            </button>

            <button
              onClick={() => { setActiveMode('templates'); setError(null); }}
              className={`flex-1 py-2.5 px-4 rounded-xl text-xs font-black transition flex items-center justify-center gap-2 cursor-pointer ${
                activeMode === 'templates'
                  ? 'bg-white text-purple-950 shadow-lg'
                  : 'text-purple-200 hover:text-white hover:bg-white/10'
              }`}
            >
              <Bookmark className="w-4 h-4 text-yellow-400" /> 2-usul: Shablonlar Bo'yicha
            </button>
          </div>
        </div>

        {/* Content Body */}
        <div className="p-6 overflow-y-auto flex-1 space-y-6">
          {error && (
            <div className="p-3.5 bg-rose-50 border border-rose-200 text-rose-700 rounded-xl text-xs dark:bg-rose-950/30 dark:border-rose-800 dark:text-rose-300">
              ⚠️ {error}
            </div>
          )}

          {/* MODE 1: DARSLIKLAR BO'YICHA */}
          {activeMode === 'lessons' && (
            <div className="space-y-6 animate-fadeIn">
              {/* Lesson Selector */}
              <div>
                <div className="flex items-center justify-between mb-2">
                  <label className="text-xs font-bold text-slate-800 dark:text-slate-200 flex items-center gap-1.5">
                    <BookOpen className="w-4 h-4 text-purple-500" />
                    Darslarni Belgilang ({selectedLessonIds.length} ta tanlandi)
                  </label>
                  <div className="flex gap-2 text-[11px]">
                    <button
                      type="button"
                      onClick={selectAllLessons}
                      className="text-purple-600 dark:text-purple-400 font-semibold hover:underline cursor-pointer"
                    >
                      Barchasini tanlash
                    </button>
                    <span className="text-slate-300">|</span>
                    <button
                      type="button"
                      onClick={clearLessons}
                      className="text-slate-500 font-semibold hover:underline cursor-pointer"
                    >
                      Tozalash
                    </button>
                  </div>
                </div>

                <div className="grid grid-cols-4 sm:grid-cols-6 md:grid-cols-8 gap-2 max-h-44 overflow-y-auto p-3 bg-slate-50 dark:bg-slate-800/50 rounded-2xl border border-slate-200 dark:border-slate-800">
                  {lessons.map(l => {
                    const isSelected = selectedLessonIds.includes(l.lessonNumber);
                    return (
                      <button
                        key={l.id}
                        type="button"
                        onClick={() => toggleLesson(l.lessonNumber)}
                        className={`p-2 rounded-xl text-xs font-bold transition flex items-center justify-center gap-1 cursor-pointer ${
                          isSelected
                            ? 'bg-purple-600 text-white shadow-md shadow-purple-500/20'
                            : 'bg-white dark:bg-slate-800 text-slate-700 dark:text-slate-300 border border-slate-200 dark:border-slate-700 hover:border-purple-400'
                        }`}
                      >
                        <span>{l.lessonNumber}</span>
                        {isSelected && <Check className="w-3 h-3 stroke-[3]" />}
                      </button>
                    );
                  })}
                </div>
              </div>

              {/* Configurations Grid */}
              <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
                <div>
                  <label className="block text-xs font-bold text-slate-800 dark:text-slate-200 mb-2 flex items-center gap-1.5">
                    <Layers className="w-4 h-4 text-blue-500" /> Savollar Soni
                  </label>
                  <div className="grid grid-cols-4 gap-1.5">
                    {[5, 10, 15, 20].map(cnt => (
                      <button
                        key={cnt}
                        type="button"
                        onClick={() => setQuestionCount(cnt)}
                        className={`py-2 rounded-xl text-xs font-extrabold border transition cursor-pointer ${
                          questionCount === cnt
                            ? 'bg-blue-600 text-white border-blue-600 shadow-md'
                            : 'bg-slate-50 dark:bg-slate-800 text-slate-700 dark:text-slate-300 border-slate-200 dark:border-slate-700'
                        }`}
                      >
                        {cnt}
                      </button>
                    ))}
                  </div>
                </div>

                <div>
                  <label className="block text-xs font-bold text-slate-800 dark:text-slate-200 mb-2 flex items-center gap-1.5">
                    <Flame className="w-4 h-4 text-amber-500" /> Qiyinlik Darajasi
                  </label>
                  <select
                    value={difficulty}
                    onChange={e => setDifficulty(e.target.value as any)}
                    className="w-full py-2 px-3 bg-slate-50 dark:bg-slate-800 border border-slate-200 dark:border-slate-700 rounded-xl text-xs font-bold text-slate-800 dark:text-slate-200 outline-none focus:ring-2 focus:ring-purple-500"
                  >
                    <option value="easy">Oson (Asosiy tushunchalar)</option>
                    <option value="medium">O'rta (Mantiqiy savollar)</option>
                    <option value="hard">Murakkab (Chuqur texnik kod)</option>
                    <option value="mixed">Aralash (Barcha darajalar)</option>
                  </select>
                </div>

                <div>
                  <label className="block text-xs font-bold text-slate-800 dark:text-slate-200 mb-2 flex items-center gap-1.5">
                    <Code className="w-4 h-4 text-emerald-500" /> Kodli Savollar
                  </label>
                  <button
                    type="button"
                    onClick={() => setIncludeCode(!includeCode)}
                    className={`w-full py-2 px-3 rounded-xl text-xs font-extrabold border transition flex items-center justify-center gap-2 cursor-pointer ${
                      includeCode
                        ? 'bg-emerald-600 text-white border-emerald-600 shadow-md'
                        : 'bg-slate-50 dark:bg-slate-800 text-slate-700 dark:text-slate-300 border-slate-200 dark:border-slate-700'
                    }`}
                  >
                    {includeCode ? '✓ Kodli savollar mavjud' : '❌ Kodli savolsiz'}
                  </button>
                </div>
              </div>
            </div>
          )}

          {/* MODE 2: SHABLONLAR BO'YICHA */}
          {activeMode === 'templates' && (
            <div className="space-y-5 animate-fadeIn">
              <div className="flex items-center justify-between">
                <div className="text-xs font-bold text-slate-800 dark:text-slate-200 flex items-center gap-1.5">
                  <Bookmark className="w-4 h-4 text-yellow-500" />
                  Mavjud Shablonlar ({templates.length} ta shablon tayyor)
                </div>

                <button
                  type="button"
                  onClick={() => setIsCreatingTemplate(!isCreatingTemplate)}
                  className="px-3 py-1.5 bg-purple-600 hover:bg-purple-700 text-white font-bold text-xs rounded-xl transition flex items-center gap-1 cursor-pointer"
                >
                  <Plus className="w-3.5 h-3.5" />
                  {isCreatingTemplate ? 'Bekor Qilish' : 'Yangi Shablon Yaratish'}
                </button>
              </div>

              {/* Form to create custom template */}
              {isCreatingTemplate && (
                <form onSubmit={handleSaveNewTemplate} className="p-5 bg-purple-950/30 border border-purple-800/80 rounded-2xl space-y-3 animate-scaleUp">
                  <h4 className="text-xs font-black text-purple-300 uppercase tracking-wider">Yangi Shablon Parametrlari</h4>
                  
                  <div>
                    <label className="block text-[11px] font-bold text-slate-400 mb-1">Shablon Nomi</label>
                    <input
                      type="text"
                      placeholder="Masalan: Django REST Framework Maxsus Imtihon"
                      value={newTplTitle}
                      onChange={e => setNewTplTitle(e.target.value)}
                      className="w-full px-3 py-2 bg-slate-800 border border-slate-700 rounded-xl text-xs font-bold text-white outline-none focus:ring-2 focus:ring-purple-500"
                      required
                    />
                  </div>

                  <div>
                    <label className="block text-[11px] font-bold text-slate-400 mb-1">Qisqa Izoh</label>
                    <input
                      type="text"
                      placeholder="Shablon haqida qisqacha ma'lumot..."
                      value={newTplDesc}
                      onChange={e => setNewTplDesc(e.target.value)}
                      className="w-full px-3 py-2 bg-slate-800 border border-slate-700 rounded-xl text-xs bg-white dark:bg-slate-800"
                    />
                  </div>

                  <div className="grid grid-cols-2 gap-3">
                    <div>
                      <label className="block text-[11px] font-bold text-slate-400 mb-1">Savollar Soni</label>
                      <select
                        value={newTplCount}
                        onChange={e => setNewTplCount(parseInt(e.target.value, 10))}
                        className="w-full px-3 py-2 bg-slate-800 border border-slate-700 rounded-xl text-xs font-bold text-white"
                      >
                        <option value={5}>5 ta savol</option>
                        <option value={10}>10 ta savol</option>
                        <option value={15}>15 ta savol</option>
                        <option value={20}>20 ta savol</option>
                      </select>
                    </div>

                    <div>
                      <label className="block text-[11px] font-bold text-slate-400 mb-1">Qiyinlik Darajasi</label>
                      <select
                        value={newTplDifficulty}
                        onChange={e => setNewTplDifficulty(e.target.value as any)}
                        className="w-full px-3 py-2 bg-slate-800 border border-slate-700 rounded-xl text-xs font-bold text-white"
                      >
                        <option value="easy">Oson</option>
                        <option value="medium">O'rta</option>
                        <option value="hard">Murakkab</option>
                        <option value="mixed">Aralash</option>
                      </select>
                    </div>
                  </div>

                  <button
                    type="submit"
                    className="w-full py-2.5 bg-purple-600 hover:bg-purple-700 text-white font-extrabold text-xs rounded-xl shadow-md transition cursor-pointer"
                  >
                    💾 Shablonni Saqlash
                  </button>
                </form>
              )}

              {/* Templates Cards Grid */}
              <div className="grid grid-cols-1 md:grid-cols-2 gap-3.5 max-h-64 overflow-y-auto pr-1">
                {templates.map(tpl => {
                  const isSelected = selectedTemplateId === tpl.id;
                  return (
                    <div
                      key={tpl.id}
                      onClick={() => setSelectedTemplateId(tpl.id)}
                      className={`p-4 rounded-2xl border transition-all cursor-pointer relative flex flex-col justify-between space-y-3 ${
                        isSelected
                          ? 'bg-purple-950/40 border-purple-500 ring-2 ring-purple-500/40 shadow-lg'
                          : 'bg-slate-50/50 dark:bg-slate-800/40 border-slate-200 dark:border-slate-800 hover:border-purple-400'
                      }`}
                    >
                      <div className="flex items-start justify-between gap-2">
                        <div className="flex items-center gap-2">
                          <span className="px-2 py-0.5 rounded-md bg-purple-900/60 border border-purple-700 text-[10px] font-black text-purple-200 uppercase">
                            {tpl.category}
                          </span>
                          <span className="text-[10px] font-bold text-amber-400">
                            {tpl.questionCount} ta savol
                          </span>
                        </div>

                        {tpl.id.startsWith('custom-tpl-') && (
                          <button
                            onClick={e => handleDeleteTemplate(tpl.id, e)}
                            className="text-slate-400 hover:text-rose-500 p-1"
                            title="O'chirish"
                          >
                            <Trash2 className="w-3.5 h-3.5" />
                          </button>
                        )}
                      </div>

                      <div>
                        <h4 className="font-extrabold text-sm text-slate-900 dark:text-white leading-snug">
                          {tpl.title}
                        </h4>
                        <p className="text-xs text-slate-500 dark:text-slate-400 mt-1 line-clamp-2">
                          {tpl.description}
                        </p>
                      </div>

                      <div className="flex items-center justify-between pt-1 text-[11px] font-bold text-purple-400">
                        <span>Qiyinlik: {tpl.difficulty.toUpperCase()}</span>
                        {isSelected && (
                          <span className="flex items-center gap-1 text-emerald-400 font-black">
                            <CheckCircle className="w-4 h-4" /> Tanlangan
                          </span>
                        )}
                      </div>
                    </div>
                  );
                })}
              </div>
            </div>
          )}
        </div>

        {/* Footer Action Button */}
        <div className="p-5 bg-slate-50 dark:bg-slate-900 border-t border-slate-200 dark:border-slate-800 flex items-center justify-between">
          <button
            onClick={onClose}
            className="px-4 py-2.5 text-xs font-semibold text-slate-600 hover:text-slate-800 dark:text-slate-400 cursor-pointer"
          >
            Bekor qilish
          </button>

          <button
            onClick={activeMode === 'lessons' ? handleGenerateFromLessons : handleGenerateFromTemplate}
            disabled={loading}
            className="px-8 py-3.5 bg-gradient-to-r from-purple-600 via-indigo-600 to-blue-600 text-white rounded-2xl font-black text-sm shadow-xl hover:from-purple-700 hover:to-blue-700 disabled:opacity-50 transition flex items-center gap-2 cursor-pointer"
          >
            {loading ? (
              <>
                <Loader2 className="w-5 h-5 animate-spin" />
                <span>AI Quiz Yaratilmoqda...</span>
              </>
            ) : (
              <>
                <Sparkles className="w-5 h-5 text-yellow-300" />
                <span>{activeMode === 'lessons' ? '✨ AI Quiz Yaratish' : '🚀 Shablon Bo\'yicha Boshlash'}</span>
              </>
            )}
          </button>
        </div>
      </div>
    </div>
  );
}
