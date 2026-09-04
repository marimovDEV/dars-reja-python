import React from 'react';
import { Lock, ShieldAlert, BookOpen } from 'lucide-react';
import { Lesson } from '../types';

interface LockedLessonViewProps {
  lesson: Lesson;
  groupName?: string;
}

export const LockedLessonView: React.FC<LockedLessonViewProps> = ({ lesson, groupName }) => {
  return (
    <div className="min-h-[75vh] flex flex-col items-center justify-center p-6 text-center animate-fadeIn font-sans">
      <div className="w-full max-w-lg p-8 rounded-3xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 shadow-2xl space-y-6 card-3d">
        <div className="w-20 h-20 rounded-3xl bg-gradient-to-tr from-amber-500 to-rose-500 flex items-center justify-center text-white shadow-xl mx-auto animate-float3D">
          <Lock className="w-10 h-10" />
        </div>

        <div className="space-y-2">
          <span className="px-3 py-1 rounded-full text-xs font-black bg-amber-100 dark:bg-amber-950/60 text-amber-700 dark:text-amber-300 uppercase tracking-wider">
            🔒 QULFLANGAN DARS
          </span>
          <h2 className="text-2xl font-black text-slate-900 dark:text-white leading-tight">
            {lesson.lessonNumber}-dars: {lesson.title}
          </h2>
          <p className="text-xs text-slate-500 dark:text-slate-400 font-medium">
            {groupName ? `${groupName} guruhida` : 'Guruhda'} ushbu dars hali o'tildi deb belgilangani yo'q.
          </p>
        </div>

        <div className="p-4 rounded-2xl bg-amber-50 dark:bg-amber-950/30 border border-amber-200 dark:border-amber-900/40 text-xs text-amber-800 dark:text-amber-300 text-left space-y-2 font-medium">
          <div className="flex items-center gap-2 font-bold text-amber-900 dark:text-amber-200">
            <ShieldAlert className="w-4 h-4 shrink-0 text-amber-500" />
            <span>O'quvchilar uchun qoida:</span>
          </div>
          <p className="leading-relaxed">
            Ushbu darsning dokumentatsiyasi, kodlari va barcha topshiriqlari guruh o'qituvchisi darsni <strong className="text-emerald-600 dark:text-emerald-400">✅ O'tildi</strong> deb belgilagach avtomatik tarzda ochiladi.
          </p>
        </div>
      </div>
    </div>
  );
};
