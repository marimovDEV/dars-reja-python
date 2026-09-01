import React, { useState } from 'react';
import { X, Plus } from 'lucide-react';
import { Lesson } from '../types';

interface AddLessonModalProps {
  isOpen: boolean;
  onClose: () => void;
  onAdd: (newLesson: Lesson) => void;
  nextLessonNumber: number;
}

export const AddLessonModal: React.FC<AddLessonModalProps> = ({
  isOpen,
  onClose,
  onAdd,
  nextLessonNumber,
}) => {
  if (!isOpen) return null;

  const [lessonNumber, setLessonNumber] = useState<number>(nextLessonNumber);
  const [title, setTitle] = useState('');
  const [date, setDate] = useState(new Date().toISOString().split('T')[0]);
  const [time, setTime] = useState('08:30 - 10:00');
  const [description, setDescription] = useState('');
  const [content, setContent] = useState('');
  const [homework, setHomework] = useState('');

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (!title.trim()) return;

    const newLesson: Lesson = {
      id: `les-${Date.now()}`,
      lessonNumber,
      title: title.trim(),
      date,
      time: time.trim(),
      status: 'planned',
      description: description.trim() || 'Ushbu dars uchun qisqacha tavsif kiritilmagan.',
      content: content.trim() || `### ${lessonNumber}-Dars: ${title}\n\nUshbu dars davomida quyidagi asosiy tushunchalar o'rganiladi:\n\n* Mavzuning dolzarbligi va maqsadlari\n* Asosiy qoidalar va ta'riflar\n* Amaliy misollar`,
      homework: homework.trim() || "Darslikdagi tegishli mavzuni o'qish.",
      materials: [
        {
          id: `m-${Date.now()}`,
          name: `${lessonNumber}-Dars_Taqdimoti.pptx`,
          type: 'pptx',
          size: '1.5 MB'
        }
      ],
      tasks: [
        {
          id: `t-${Date.now()}`,
          title: "1-topshiriq",
          type: 'practical',
          question: `${title} mavzusi bo'yicha amaliy mashq bajaring.`,
          answer: "Tavsiya etilgan kod yozildi."
        }
      ]
    };

    onAdd(newLesson);
    onClose();
  };

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-slate-900/60 backdrop-blur-xs overflow-y-auto">
      <div 
        id="add-lesson-modal-container"
        className="bg-white dark:bg-slate-900 rounded-2xl shadow-xl border border-slate-200 dark:border-slate-800 w-full max-w-xl max-h-[90vh] flex flex-col overflow-hidden animate-in fade-in zoom-in-95 duration-200"
      >
        {/* Header */}
        <div className="px-6 py-4 border-b border-slate-100 dark:border-slate-800 flex items-center justify-between">
          <div>
            <h2 className="text-base font-bold text-slate-900 dark:text-white flex items-center gap-2">
              <Plus className="w-5 h-5 text-blue-600" />
              Yangi Dars Rejasi Qo'shish
            </h2>
            <p className="text-xs text-slate-500">
              Ro'yxatga yangi dars rejasi shablonini kiritish
            </p>
          </div>
          <button
            onClick={onClose}
            className="w-8 h-8 rounded-lg text-slate-400 hover:text-slate-600 hover:bg-slate-100 dark:hover:bg-slate-800 flex items-center justify-center transition-colors"
          >
            <X className="w-5 h-5" />
          </button>
        </div>

        {/* Body */}
        <form onSubmit={handleSubmit} className="p-6 overflow-y-auto space-y-4 text-xs text-left">
          <div className="grid grid-cols-2 gap-3">
            <div>
              <label className="block font-semibold text-slate-700 dark:text-slate-300 mb-1">
                Dars raqami:
              </label>
              <input
                type="number"
                min={1}
                value={lessonNumber}
                onChange={(e) => setLessonNumber(parseInt(e.target.value) || 1)}
                className="w-full px-3 py-2 bg-slate-50 dark:bg-slate-800 border border-slate-200 dark:border-slate-700 rounded-lg text-slate-800 dark:text-slate-200 focus:outline-none focus:ring-2 focus:ring-blue-500"
                required
              />
            </div>
            <div>
              <label className="block font-semibold text-slate-700 dark:text-slate-300 mb-1">
                Vaqt oraliq:
              </label>
              <input
                type="text"
                placeholder="Masalan: 08:30 - 10:00"
                value={time}
                onChange={(e) => setTime(e.target.value)}
                className="w-full px-3 py-2 bg-slate-50 dark:bg-slate-800 border border-slate-200 dark:border-slate-700 rounded-lg text-slate-800 dark:text-slate-200 focus:outline-none focus:ring-2 focus:ring-blue-500"
              />
            </div>
          </div>

          <div>
            <label className="block font-semibold text-slate-700 dark:text-slate-300 mb-1">
              Dars mavzusi va to'liq nomi:
            </label>
            <input
              type="text"
              placeholder="Masalan: Ma'lumotlar bazasi va SQL so'rovlari"
              value={title}
              onChange={(e) => setTitle(e.target.value)}
              className="w-full px-3 py-2 bg-slate-50 dark:bg-slate-800 border border-slate-200 dark:border-slate-700 rounded-lg text-slate-800 dark:text-slate-200 focus:outline-none focus:ring-2 focus:ring-blue-500"
              required
            />
          </div>

          <div className="grid grid-cols-2 gap-3">
            <div>
              <label className="block font-semibold text-slate-700 dark:text-slate-300 mb-1">
                Sana:
              </label>
              <input
                type="date"
                value={date}
                onChange={(e) => setDate(e.target.value)}
                className="w-full px-3 py-2 bg-slate-50 dark:bg-slate-800 border border-slate-200 dark:border-slate-700 rounded-lg text-slate-800 dark:text-slate-200 focus:outline-none focus:ring-2 focus:ring-blue-500"
                required
              />
            </div>
            <div>
              <label className="block font-semibold text-slate-700 dark:text-slate-300 mb-1">
                Qisqacha tavsif:
              </label>
              <input
                type="text"
                placeholder="Dars mazmuni haqida qisqacha..."
                value={description}
                onChange={(e) => setDescription(e.target.value)}
                className="w-full px-3 py-2 bg-slate-50 dark:bg-slate-800 border border-slate-200 dark:border-slate-700 rounded-lg text-slate-800 dark:text-slate-200 focus:outline-none focus:ring-2 focus:ring-blue-500"
              />
            </div>
          </div>

          <div>
            <label className="block font-semibold text-slate-700 dark:text-slate-300 mb-1">
              Dars konspekti / Reja mazmuni:
            </label>
            <textarea
              rows={4}
              placeholder="Dars konspekti yoki rejasini yozing..."
              value={content}
              onChange={(e) => setContent(e.target.value)}
              className="w-full px-3 py-2 bg-slate-50 dark:bg-slate-800 border border-slate-200 dark:border-slate-700 rounded-lg text-slate-800 dark:text-slate-200 focus:outline-none focus:ring-2 focus:ring-blue-500"
            />
          </div>

          <div>
            <label className="block font-semibold text-amber-700 dark:text-amber-400 mb-1">
              Uyga vazifa:
            </label>
            <textarea
              rows={2}
              placeholder="Uy vazifasi topshiriqlari..."
              value={homework}
              onChange={(e) => setHomework(e.target.value)}
              className="w-full px-3 py-2 bg-slate-50 dark:bg-slate-800 border border-slate-200 dark:border-slate-700 rounded-lg text-slate-800 dark:text-slate-200 focus:outline-none focus:ring-2 focus:ring-blue-500"
            />
          </div>

          <div className="pt-4 border-t border-slate-100 dark:border-slate-800 flex items-center justify-end gap-2.5">
            <button
              type="button"
              onClick={onClose}
              className="px-4 py-2 rounded-lg border border-slate-200 dark:border-slate-700 text-slate-700 dark:text-slate-300 font-medium hover:bg-slate-50 dark:hover:bg-slate-800"
            >
              Bekor qilish
            </button>
            <button
              type="submit"
              className="px-4 py-2 rounded-lg bg-blue-600 hover:bg-blue-700 text-white font-semibold flex items-center gap-1.5 shadow-xs"
            >
              <Plus className="w-4 h-4" />
              Rejaga qo'shish
            </button>
          </div>
        </form>
      </div>
    </div>
  );
};
