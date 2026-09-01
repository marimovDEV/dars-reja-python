import React, { useState } from 'react';
import { Quiz, QuizGenConfig, QuizQuestion } from '../../types/quiz';
import { Sparkles, Check, BookOpen, Clock, Code, HelpCircle, Layers, Flame, ArrowRight, Loader2 } from 'lucide-react';
import { Lesson } from '../../types';

interface AIQuizGeneratorModalProps {
  isOpen: boolean;
  onClose: () => void;
  lessons: Lesson[];
  onQuizGenerated: (quiz: Quiz) => void;
}

export function AIQuizGeneratorModal({
  isOpen,
  onClose,
  lessons,
  onQuizGenerated
}: AIQuizGeneratorModalProps) {
  const [selectedLessonIds, setSelectedLessonIds] = useState<number[]>([1, 2, 3]);
  const [questionCount, setQuestionCount] = useState<number>(10);
  const [difficulty, setDifficulty] = useState<'easy' | 'medium' | 'hard' | 'mixed'>('mixed');
  const [includeCode, setIncludeCode] = useState<boolean>(true);
  const [loading, setLoading] = useState<boolean>(false);
  const [error, setError] = useState<string | null>(null);

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

  const handleGenerate = async () => {
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

      // Save to backend DB
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

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-slate-900/80 backdrop-blur-md animate-fadeIn">
      <div className="bg-white dark:bg-slate-900 rounded-3xl shadow-2xl border border-slate-200 dark:border-slate-800 w-full max-w-3xl overflow-hidden flex flex-col max-h-[90vh]">
        
        {/* Header */}
        <div className="p-6 bg-gradient-to-r from-purple-600 via-indigo-600 to-blue-600 text-white relative">
          <div className="flex items-center justify-between">
            <div className="flex items-center gap-3">
              <div className="p-3 bg-white/20 backdrop-blur-md rounded-2xl">
                <Sparkles className="w-7 h-7 text-yellow-300 animate-pulse" />
              </div>
              <div>
                <h2 className="text-xl font-bold">AI Bilan Quiz Yaratish</h2>
                <p className="text-purple-100 text-xs mt-0.5">
                  Darslar dokumentatsiyasidan avtomatik animatsiyali test yaratish
                </p>
              </div>
            </div>
            <button
              onClick={onClose}
              className="text-white/80 hover:text-white p-2 rounded-full hover:bg-white/10 transition"
            >
              ✕
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

          {/* Section 1: Lesson Selection Checkboxes */}
          <div>
            <div className="flex items-center justify-between mb-2">
              <label className="text-xs font-bold text-slate-800 dark:text-slate-200 flex items-center gap-1.5">
                <BookOpen className="w-4 h-4 text-purple-500" />
                1. Darslarni Belgilang ({selectedLessonIds.length} ta tanlandi)
              </label>
              <div className="flex gap-2 text-[11px]">
                <button
                  type="button"
                  onClick={selectAllLessons}
                  className="text-purple-600 dark:text-purple-400 font-semibold hover:underline"
                >
                  Barchasini tanlash
                </button>
                <span className="text-slate-300">|</span>
                <button
                  type="button"
                  onClick={clearLessons}
                  className="text-slate-400 hover:underline"
                >
                  Tozalash
                </button>
              </div>
            </div>

            <div className="grid grid-cols-2 md:grid-cols-3 gap-2 max-h-48 overflow-y-auto p-2 bg-slate-50 dark:bg-slate-800/50 rounded-2xl border border-slate-200 dark:border-slate-800">
              {lessons.map(l => {
                const isChecked = selectedLessonIds.includes(l.lessonNumber);
                return (
                  <div
                    key={l.id}
                    onClick={() => toggleLesson(l.lessonNumber)}
                    className={`p-2.5 rounded-xl border text-xs cursor-pointer transition flex items-center gap-2 select-none ${
                      isChecked
                        ? 'border-purple-500 bg-purple-50 dark:bg-purple-950/40 text-purple-900 dark:text-purple-200 font-medium'
                        : 'border-slate-200 dark:border-slate-700 bg-white dark:bg-slate-800 text-slate-700 dark:text-slate-300 hover:border-slate-300'
                    }`}
                  >
                    <div className={`w-4 h-4 rounded flex items-center justify-center text-white shrink-0 ${
                      isChecked ? 'bg-purple-600' : 'border border-slate-300 dark:border-slate-600'
                    }`}>
                      {isChecked && <Check className="w-3 h-3" />}
                    </div>
                    <span className="truncate">
                      <strong>{l.lessonNumber}-dars:</strong> {l.title}
                    </span>
                  </div>
                );
              })}
            </div>
          </div>

          {/* Section 2: Quiz Configurations */}
          <div className="space-y-4">
            <h3 className="text-xs font-bold text-slate-800 dark:text-slate-200 flex items-center gap-1.5">
              <Layers className="w-4 h-4 text-indigo-500" />
              2. Quiz Sozlamalari
            </h3>

            <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
              {/* Question count */}
              <div>
                <label className="block text-[11px] font-semibold text-slate-600 dark:text-slate-400 mb-1">
                  Savollar Soni
                </label>
                <div className="grid grid-cols-4 gap-1">
                  {[5, 10, 15, 20].map(cnt => (
                    <button
                      key={cnt}
                      type="button"
                      onClick={() => setQuestionCount(cnt)}
                      className={`py-2 rounded-xl text-xs font-bold transition ${
                        questionCount === cnt
                          ? 'bg-purple-600 text-white shadow-sm'
                          : 'bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-300 hover:bg-slate-200'
                      }`}
                    >
                      {cnt} ta
                    </button>
                  ))}
                </div>
              </div>

              {/* Difficulty */}
              <div>
                <label className="block text-[11px] font-semibold text-slate-600 dark:text-slate-400 mb-1">
                  Qiyinlik Darajasi
                </label>
                <select
                  value={difficulty}
                  onChange={(e: any) => setDifficulty(e.target.value)}
                  className="w-full px-3 py-2 bg-slate-100 dark:bg-slate-800 border border-slate-200 dark:border-slate-700 rounded-xl text-xs font-semibold text-slate-800 dark:text-slate-200 outline-none"
                >
                  <option value="easy">Oson (Asosiy tushunchalar)</option>
                  <option value="medium">O'rta (Standard)</option>
                  <option value="hard">Murakkab (Amaliy muammolar)</option>
                  <option value="mixed">Aralash (Tavsiya etiladi)</option>
                </select>
              </div>

              {/* Code questions toggle */}
              <div>
                <label className="block text-[11px] font-semibold text-slate-600 dark:text-slate-400 mb-1">
                  Kodli Savollar
                </label>
                <button
                  type="button"
                  onClick={() => setIncludeCode(!includeCode)}
                  className={`w-full py-2 px-3 rounded-xl text-xs font-semibold flex items-center justify-between transition ${
                    includeCode
                      ? 'bg-indigo-50 dark:bg-indigo-950/50 border border-indigo-200 dark:border-indigo-800 text-indigo-700 dark:text-indigo-300'
                      : 'bg-slate-100 dark:bg-slate-800 text-slate-500'
                  }`}
                >
                  <span className="flex items-center gap-1">
                    <Code className="w-3.5 h-3.5" /> Kod misollari
                  </span>
                  <span>{includeCode ? 'Yoqilgan' : 'O\'chirilgan'}</span>
                </button>
              </div>
            </div>
          </div>
        </div>

        {/* Footer Actions */}
        <div className="p-5 bg-slate-50 dark:bg-slate-900 border-t border-slate-200 dark:border-slate-800 flex items-center justify-between">
          <div className="text-xs text-slate-500">
            * AI faqat tanlangan darslar dokumentatsiyasidan test yaratadi.
          </div>

          <div className="flex gap-3">
            <button
              type="button"
              onClick={onClose}
              className="px-4 py-2.5 text-xs font-medium text-slate-600 hover:text-slate-800 dark:text-slate-400"
            >
              Bekor qilish
            </button>
            <button
              type="button"
              disabled={loading}
              onClick={handleGenerate}
              className="px-6 py-2.5 bg-gradient-to-r from-purple-600 via-indigo-600 to-blue-600 text-white rounded-xl font-bold text-xs shadow-lg hover:from-purple-700 hover:to-blue-700 transition disabled:opacity-50 flex items-center gap-2"
            >
              {loading ? (
                <>
                  <Loader2 className="w-4 h-4 animate-spin" />
                  AI Test Yaratmoqda...
                </>
              ) : (
                <>
                  <Sparkles className="w-4 h-4 text-yellow-300" />
                  Quiz Yaratish <ArrowRight className="w-4 h-4" />
                </>
              )}
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}
