import React, { useState } from 'react';
import { Quiz, QuizQuestion } from '../../types/quiz';
import { Play, Edit3, Trash2, Plus, Check, HelpCircle, Code, Clock, Sparkles } from 'lucide-react';

interface QuizEditorModalProps {
  isOpen: boolean;
  onClose: () => void;
  quiz: Quiz;
  onStartLiveSession: (quiz: Quiz) => void;
}

export function QuizEditorModal({
  isOpen,
  onClose,
  quiz,
  onStartLiveSession
}: QuizEditorModalProps) {
  const [questions, setQuestions] = useState<QuizQuestion[]>(quiz.questions);
  const [editingIndex, setEditingIndex] = useState<number | null>(null);

  if (!isOpen) return null;

  const handleSaveQuestion = (index: number, updatedQ: QuizQuestion) => {
    const next = [...questions];
    next[index] = updatedQ;
    setQuestions(next);
    setEditingIndex(null);
  };

  const handleDeleteQuestion = (index: number) => {
    if (questions.length === 1) return; // keep at least 1
    const next = questions.filter((_, i) => i !== index);
    setQuestions(next);
  };

  const handleAddQuestion = () => {
    const newQ: QuizQuestion = {
      question: "Yangi savol matnini kiriting...",
      type: "single_choice",
      options: ["Variant A", "Variant B", "Variant C", "Variant D"],
      correctOptionIndex: 0,
      explanation: "Tushuntirish matni...",
      lessonId: quiz.lessonIds[0] || 1,
      durationSeconds: 20
    };
    setQuestions([...questions, newQ]);
    setEditingIndex(questions.length);
  };

  const handleStartGame = () => {
    const updatedQuiz = { ...quiz, questions };
    onStartLiveSession(updatedQuiz);
    onClose();
  };

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-slate-900/80 backdrop-blur-md animate-fadeIn">
      <div className="bg-white dark:bg-slate-900 rounded-3xl shadow-2xl border border-slate-200 dark:border-slate-800 w-full max-w-4xl overflow-hidden flex flex-col max-h-[92vh]">
        
        {/* Header */}
        <div className="p-6 bg-gradient-to-r from-blue-600 via-indigo-600 to-purple-600 text-white flex items-center justify-between">
          <div>
            <div className="flex items-center gap-2 text-xs font-semibold text-blue-100 uppercase tracking-wider mb-1">
              <Sparkles className="w-4 h-4 text-yellow-300" /> AI Quiz Tahrirlagich
            </div>
            <h2 className="text-xl font-bold">{quiz.title}</h2>
            <p className="text-blue-100 text-xs mt-0.5">
              Jami {questions.length} ta savol tayyorlandi. Boshlashdan oldin tahrirlashingiz yoki saqlashingiz mumkin.
            </p>
          </div>

          <button
            onClick={onClose}
            className="text-white/80 hover:text-white p-2 rounded-full hover:bg-white/10 transition"
          >
            ✕
          </button>
        </div>

        {/* Questions List */}
        <div className="p-6 overflow-y-auto flex-1 space-y-4">
          {questions.map((q, idx) => {
            const isEditing = editingIndex === idx;

            return (
              <div
                key={idx}
                className="p-5 rounded-2xl border border-slate-200 dark:border-slate-800 bg-slate-50/50 dark:bg-slate-800/40 space-y-3"
              >
                <div className="flex items-start justify-between gap-4">
                  <div className="flex items-center gap-2">
                    <span className="w-7 h-7 rounded-lg bg-blue-600 text-white font-bold text-xs flex items-center justify-center shrink-0">
                      {idx + 1}
                    </span>
                    <span className="text-xs font-semibold text-slate-500 dark:text-slate-400">
                      {q.lessonId}-darsdan
                    </span>
                  </div>

                  <div className="flex items-center gap-2">
                    <button
                      onClick={() => setEditingIndex(isEditing ? null : idx)}
                      className="p-2 rounded-lg bg-white dark:bg-slate-700 text-slate-600 dark:text-slate-200 hover:text-blue-600 text-xs font-semibold flex items-center gap-1 border border-slate-200 dark:border-slate-600 transition"
                    >
                      <Edit3 className="w-3.5 h-3.5" />
                      {isEditing ? 'Yopish' : 'Tahrirlash'}
                    </button>
                    <button
                      onClick={() => handleDeleteQuestion(idx)}
                      className="p-2 rounded-lg bg-rose-50 text-rose-600 hover:bg-rose-100 text-xs font-semibold border border-rose-200 transition"
                    >
                      <Trash2 className="w-3.5 h-3.5" />
                    </button>
                  </div>
                </div>

                {isEditing ? (
                  /* Edit Form */
                  <div className="space-y-3 pt-2">
                    <div>
                      <label className="block text-[11px] font-semibold text-slate-600 mb-1">Savol Matni</label>
                      <input
                        type="text"
                        value={q.question}
                        onChange={(e) => {
                          const updated = { ...q, question: e.target.value };
                          handleSaveQuestion(idx, updated);
                        }}
                        className="w-full px-3 py-2 rounded-xl border border-slate-300 dark:border-slate-700 text-xs font-semibold bg-white dark:bg-slate-800"
                      />
                    </div>

                    <div className="grid grid-cols-2 gap-2">
                      {q.options.map((opt, optIdx) => (
                        <div key={optIdx} className="flex items-center gap-2">
                          <input
                            type="radio"
                            name={`correct-${idx}`}
                            checked={q.correctOptionIndex === optIdx}
                            onChange={() => handleSaveQuestion(idx, { ...q, correctOptionIndex: optIdx })}
                            className="w-4 h-4 text-emerald-600"
                          />
                          <input
                            type="text"
                            value={opt}
                            onChange={(e) => {
                              const newOpts = [...q.options] as [string, string, string, string];
                              newOpts[optIdx] = e.target.value;
                              handleSaveQuestion(idx, { ...q, options: newOpts });
                            }}
                            className={`flex-1 px-3 py-1.5 rounded-lg border text-xs bg-white dark:bg-slate-800 ${
                              q.correctOptionIndex === optIdx
                                ? 'border-emerald-500 ring-1 ring-emerald-500'
                                : 'border-slate-200 dark:border-slate-700'
                            }`}
                          />
                        </div>
                      ))}
                    </div>

                    <div>
                      <label className="block text-[11px] font-semibold text-slate-600 mb-1">Tushuntirish</label>
                      <input
                        type="text"
                        value={q.explanation}
                        onChange={(e) => handleSaveQuestion(idx, { ...q, explanation: e.target.value })}
                        className="w-full px-3 py-1.5 rounded-xl border border-slate-300 dark:border-slate-700 text-xs bg-white dark:bg-slate-800"
                      />
                    </div>
                  </div>
                ) : (
                  /* Display Preview */
                  <div>
                    <h4 className="font-bold text-slate-800 dark:text-slate-100 text-sm mb-3">
                      {q.question}
                    </h4>

                    <div className="grid grid-cols-1 md:grid-cols-2 gap-2">
                      {q.options.map((opt, optIdx) => {
                        const isCorrect = q.correctOptionIndex === optIdx;

                        return (
                          <div
                            key={optIdx}
                            className={`p-2.5 rounded-xl border text-xs flex items-center justify-between font-medium ${
                              isCorrect
                                ? 'border-emerald-500 bg-emerald-50 dark:bg-emerald-950/40 text-emerald-900 dark:text-emerald-200 font-bold'
                                : 'border-slate-200 dark:border-slate-700 bg-white dark:bg-slate-800 text-slate-700 dark:text-slate-300'
                            }`}
                          >
                            <span>
                              {String.fromCharCode(65 + optIdx)}: {opt}
                            </span>
                            {isCorrect && (
                              <span className="px-2 py-0.5 bg-emerald-600 text-white text-[10px] font-bold rounded-full flex items-center gap-1">
                                <Check className="w-3 h-3" /> To'g'ri
                              </span>
                            )}
                          </div>
                        );
                      })}
                    </div>

                    {q.explanation && (
                      <div className="mt-2 p-2.5 rounded-xl bg-blue-50/70 dark:bg-blue-950/30 text-blue-800 dark:text-blue-200 text-xs flex items-start gap-2">
                        <HelpCircle className="w-4 h-4 text-blue-500 shrink-0 mt-0.5" />
                        <span><strong>Tushuntirish:</strong> {q.explanation}</span>
                      </div>
                    )}
                  </div>
                )}
              </div>
            );
          })}

          <button
            onClick={handleAddQuestion}
            className="w-full py-3 rounded-2xl border-2 border-dashed border-slate-300 dark:border-slate-700 hover:border-purple-500 text-slate-600 dark:text-slate-400 hover:text-purple-600 font-bold text-xs flex items-center justify-center gap-2 transition"
          >
            <Plus className="w-4 h-4" /> Yangi Savol Qo'shish
          </button>
        </div>

        {/* Footer Actions */}
        <div className="p-5 bg-slate-50 dark:bg-slate-900 border-t border-slate-200 dark:border-slate-800 flex items-center justify-between">
          <button
            onClick={onClose}
            className="px-4 py-2.5 text-xs font-medium text-slate-600 hover:text-slate-800 dark:text-slate-400"
          >
            Keyinroq o'ynash
          </button>

          <button
            onClick={handleStartGame}
            className="px-8 py-3 bg-gradient-to-r from-emerald-500 via-teal-600 to-blue-600 text-white rounded-2xl font-extrabold text-sm shadow-xl hover:from-emerald-600 hover:to-blue-700 transition flex items-center gap-2"
          >
            <Play className="w-5 h-5 fill-white" />
            🎮 Jonli O'yinni Boshlash (PIN Yaratish)
          </button>
        </div>
      </div>
    </div>
  );
}
