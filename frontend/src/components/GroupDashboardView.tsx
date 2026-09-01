import React from 'react';
import { Group } from '../types/group';
import { Users, Calendar, Clock, ExternalLink, ArrowRight, Plus, Sparkles, BookOpen, CheckCircle2, TrendingUp } from 'lucide-react';

interface GroupDashboardViewProps {
  groups: Group[];
  activeGroupId: string | null;
  onSelectGroup: (groupId: string) => void;
  onOpenCreateModal: () => void;
  onDeleteGroup?: (groupId: string) => void;
}

export function GroupDashboardView({
  groups,
  activeGroupId,
  onSelectGroup,
  onOpenCreateModal,
  onDeleteGroup
}: GroupDashboardViewProps) {
  return (
    <div className="p-6 max-w-7xl mx-auto space-y-6">
      {/* Header Banner */}
      <div className="p-8 rounded-3xl bg-gradient-to-r from-blue-600 via-indigo-600 to-purple-600 text-white shadow-xl relative overflow-hidden">
        <div className="absolute right-0 top-0 translate-x-8 -translate-y-8 opacity-10 pointer-events-none">
          <Users className="w-96 h-96 text-white" />
        </div>

        <div className="relative z-10 flex flex-col md:flex-row md:items-center justify-between gap-6">
          <div>
            <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-white/20 backdrop-blur-md text-xs font-semibold mb-3">
              <Sparkles className="w-3.5 h-3.5" /> Guruhlar Monitori
            </div>
            <h1 className="text-3xl font-extrabold tracking-tight">O'quv Guruhlaringiz</h1>
            <p className="text-blue-100 text-sm mt-1 max-w-xl">
              Barcha guruhlarning qaysi darsda/mavzuda ekanligini real-vaqt rejimida kuzatib boring va dars rejasiga o'ting.
            </p>
          </div>

          <button
            onClick={onOpenCreateModal}
            className="px-5 py-3 bg-white text-blue-600 font-bold rounded-2xl shadow-lg hover:bg-blue-50 transition flex items-center gap-2 shrink-0 text-sm"
          >
            <Plus className="w-5 h-5" /> Yangi Guruh Yaratish
          </button>
        </div>
      </div>

      {/* Grid of Groups */}
      {groups.length === 0 ? (
        <div className="text-center py-16 bg-white dark:bg-slate-900 rounded-3xl border border-slate-200 dark:border-slate-800 shadow-sm p-8">
          <Users className="w-16 h-16 text-slate-300 dark:text-slate-700 mx-auto mb-4" />
          <h3 className="text-lg font-bold text-slate-800 dark:text-slate-200">Hali hech qanday guruh mavjud emas</h3>
          <p className="text-sm text-slate-500 max-w-md mx-auto mt-1 mb-6">
            Dars rejasini guruhlar kesimida kuzatib borish uchun birinchi guruhingizni yarating.
          </p>
          <button
            onClick={onOpenCreateModal}
            className="px-6 py-2.5 bg-blue-600 text-white rounded-xl text-xs font-semibold shadow-md hover:bg-blue-700 transition inline-flex items-center gap-2"
          >
            <Plus className="w-4 h-4" /> Birinchi Guruhni Yaratish
          </button>
        </div>
      ) : (
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {groups.map(group => {
            const isSelected = group.id === activeGroupId;
            const progressPercent = Math.round((group.completedCount / (group.totalLessons || 72)) * 100);

            return (
              <div
                key={group.id}
                className={`bg-white dark:bg-slate-900 rounded-3xl border transition-all duration-300 shadow-sm hover:shadow-md flex flex-col justify-between overflow-hidden relative group ${
                  isSelected
                    ? 'border-blue-500 ring-2 ring-blue-500/20 dark:border-blue-500/80'
                    : 'border-slate-200 dark:border-slate-800 hover:border-blue-300 dark:hover:border-blue-700'
                }`}
              >
                <div className="p-6 space-y-4">
                  {/* Top Bar */}
                  <div className="flex items-start justify-between gap-3">
                    <div>
                      <h3 className="font-bold text-lg text-slate-800 dark:text-slate-100 group-hover:text-blue-600 dark:group-hover:text-blue-400 transition">
                        {group.name}
                      </h3>
                      <div className="flex items-center gap-2 mt-1 text-xs text-slate-500 dark:text-slate-400">
                        <Calendar className="w-3.5 h-3.5 text-blue-500" />
                        <span>Boshlanish: {group.startDate}</span>
                      </div>
                    </div>

                    {isSelected ? (
                      <span className="px-2.5 py-1 bg-blue-600 text-white text-[11px] font-bold rounded-full flex items-center gap-1 shrink-0">
                        <CheckCircle2 className="w-3 h-3" /> Faol
                      </span>
                    ) : (
                      <button
                        onClick={() => onSelectGroup(group.id)}
                        className="px-2.5 py-1 bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-300 hover:bg-blue-100 hover:text-blue-600 dark:hover:bg-blue-900/50 text-[11px] font-semibold rounded-full transition shrink-0"
                      >
                        Tanlash
                      </button>
                    )}
                  </div>

                  {/* Details Pills */}
                  <div className="grid grid-cols-2 gap-2 text-xs">
                    <div className="p-2.5 rounded-xl bg-slate-50 dark:bg-slate-800/50 border border-slate-100 dark:border-slate-800">
                      <div className="text-[10px] text-slate-400 font-medium">Dars Kunlari</div>
                      <div className="font-semibold text-slate-700 dark:text-slate-200 truncate flex items-center gap-1.5 mt-0.5">
                        <Clock className="w-3.5 h-3.5 text-indigo-500 shrink-0" />
                        <span className="truncate">{group.scheduleDays}</span>
                      </div>
                    </div>

                    <div className="p-2.5 rounded-xl bg-slate-50 dark:bg-slate-800/50 border border-slate-100 dark:border-slate-800">
                      <div className="text-[10px] text-slate-400 font-medium">O'quvchilar</div>
                      <div className="font-semibold text-slate-700 dark:text-slate-200 truncate flex items-center gap-1.5 mt-0.5">
                        <Users className="w-3.5 h-3.5 text-emerald-500 shrink-0" />
                        <span>{group.studentCount || 0} ta</span>
                      </div>
                    </div>
                  </div>

                  {/* Current Lesson Badge */}
                  <div className="p-4 rounded-2xl bg-gradient-to-br from-blue-50 to-indigo-50 dark:from-blue-950/30 dark:to-indigo-950/30 border border-blue-100 dark:border-blue-900/50">
                    <div className="text-[11px] font-semibold text-blue-600 dark:text-blue-400 uppercase tracking-wider mb-1 flex items-center justify-between">
                      <span>Joriy Mavzu</span>
                      <span className="font-bold">{group.currentLessonNumber} / {group.totalLessons || 72}-dars</span>
                    </div>
                    <div className="font-bold text-slate-800 dark:text-slate-100 text-sm line-clamp-1">
                      {group.currentLessonTitle}
                    </div>

                    {/* Progress Bar */}
                    <div className="mt-3">
                      <div className="flex justify-between text-[11px] font-medium text-slate-500 dark:text-slate-400 mb-1">
                        <span>O'tilgan darslar</span>
                        <span>{progressPercent}%</span>
                      </div>
                      <div className="w-full h-2 bg-slate-200 dark:bg-slate-800 rounded-full overflow-hidden">
                        <div
                          className="h-full bg-gradient-to-r from-blue-500 via-indigo-500 to-emerald-500 rounded-full transition-all duration-500"
                          style={{ width: `${progressPercent}%` }}
                        />
                      </div>
                    </div>
                  </div>

                  {/* Telegram Link if available */}
                  {group.telegramLink && (
                    <a
                      href={group.telegramLink}
                      target="_blank"
                      rel="noopener noreferrer"
                      className="inline-flex items-center gap-1.5 text-xs text-blue-600 dark:text-blue-400 hover:underline font-medium"
                    >
                      <ExternalLink className="w-3.5 h-3.5" /> Telegram Guruhga o'tish
                    </a>
                  )}
                </div>

                {/* Card Footer */}
                <div className="px-6 py-3.5 bg-slate-50 dark:bg-slate-800/40 border-t border-slate-100 dark:border-slate-800 flex items-center justify-between">
                  <button
                    onClick={() => onSelectGroup(group.id)}
                    className="text-xs font-bold text-blue-600 dark:text-blue-400 hover:text-blue-700 transition flex items-center gap-1"
                  >
                    Dars Rejasini Ochish <ArrowRight className="w-3.5 h-3.5" />
                  </button>

                  {onDeleteGroup && (
                    <button
                      onClick={() => {
                        if (confirm(`"${group.name}" guruhini o'chirishni tasdiqlaysizmi?`)) {
                          onDeleteGroup(group.id);
                        }
                      }}
                      className="text-[11px] text-rose-500 hover:text-rose-700 font-medium transition"
                    >
                      O'chirish
                    </button>
                  )}
                </div>
              </div>
            );
          })}
        </div>
      )}
    </div>
  );
}
