import React, { useState } from 'react';
import { 
  BookOpen, 
  Search, 
  CheckCircle2, 
  Clock, 
  Calendar, 
  Plus, 
  ChevronRight, 
  Upload, 
  Settings,
  Users,
  Grid,
  Gamepad2,
  Sparkles,
  CheckSquare,
  Check,
  Moon,
  Sun
} from 'lucide-react';
import { Lesson, LessonStatus } from '../types';
import { Group } from '../types/group';

interface LessonSidebarProps {
  lessons: Lesson[];
  selectedLessonId: string;
  onSelectLesson: (id: string) => void;
  onOpenAddModal: () => void;
  onOpenImportModal: () => void;
  onOpenSettings: () => void;
  onLogout?: () => void;
  // Group props
  groups: Group[];
  activeGroup: Group | null;
  onOpenGroupSelectModal: () => void;
  onOpenGroupDashboard: () => void;
  // Quiz props
  onOpenAIQuizGenerator?: () => void;
  onOpenPlayerView?: () => void;
  onBatchUpdateStatus?: (lessonIds: string[], status: LessonStatus) => void;
  // Theme props
  isDarkMode?: boolean;
  onToggleDarkMode?: () => void;
  // Auth role
  userRole?: 'admin' | 'student';
}

export const LessonSidebar: React.FC<LessonSidebarProps> = ({
  lessons,
  selectedLessonId,
  onSelectLesson,
  onOpenAddModal,
  onOpenImportModal,
  onOpenSettings,
  onLogout,
  groups,
  activeGroup,
  onOpenGroupSelectModal,
  onOpenGroupDashboard,
  onOpenAIQuizGenerator,
  onOpenPlayerView,
  onBatchUpdateStatus,
  isDarkMode,
  onToggleDarkMode,
  userRole = 'admin'
}) => {
  const [searchQuery, setSearchQuery] = useState('');
  const [selectedStatus, setSelectedStatus] = useState<string>('all');
  const [isBatchMode, setIsBatchMode] = useState<boolean>(false);
  const [batchSelectedIds, setBatchSelectedIds] = useState<string[]>([]);

  // Filter lessons
  const filteredLessons = lessons.filter(lesson => {
    const matchesSearch = 
      lesson.title.toLowerCase().includes(searchQuery.toLowerCase()) ||
      lesson.lessonNumber.toString().includes(searchQuery) ||
      (lesson.description && lesson.description.toLowerCase().includes(searchQuery.toLowerCase()));
    
    const matchesStatus = selectedStatus === 'all' || lesson.status === selectedStatus;

    return matchesSearch && matchesStatus;
  }).sort((a, b) => a.lessonNumber - b.lessonNumber);

  // Statistics
  const completedCount = lessons.filter(l => l.status === 'completed').length;
  const currentCount = lessons.filter(l => l.status === 'current' || l.status === 'pending').length;
  const plannedCount = lessons.filter(l => l.status === 'planned').length;
  const totalLessons = lessons.length;

  return (
    <aside 
      id="lesson-sidebar"
      className="w-full md:w-80 lg:w-96 bg-white dark:bg-slate-900 border-r border-slate-200 dark:border-slate-800 flex flex-col h-screen select-none shrink-0"
    >
      {/* Group Selector Header Banner */}
      <div className="p-3 bg-gradient-to-r from-blue-600 to-indigo-600 text-white border-b border-blue-700">
        <div className="flex items-center justify-between gap-2">
          <button
            onClick={onOpenGroupSelectModal}
            className="flex-1 text-left flex items-center gap-2 p-1.5 rounded-xl hover:bg-white/10 transition group"
          >
            <div className="p-2 rounded-lg bg-white/20 text-white">
              <Users className="w-4 h-4" />
            </div>
            <div className="min-w-0 flex-1">
              <div className="text-[10px] text-blue-100 font-semibold uppercase tracking-wider flex items-center gap-1">
                Faol Guruh <ChevronRight className="w-3 h-3 group-hover:translate-x-0.5 transition" />
              </div>
              <div className="font-bold text-xs truncate">
                {activeGroup ? activeGroup.name : 'Guruhni Tanlash'}
              </div>
            </div>
          </button>

          <button
            onClick={onOpenGroupDashboard}
            title="Guruhlar Monitori (Dashboard)"
            className="p-2 rounded-xl bg-white/15 hover:bg-white/25 text-white transition shrink-0 flex items-center justify-center"
          >
            <Grid className="w-4 h-4" />
          </button>
        </div>
      </div>

      {/* Top Header Controls */}
      <div id="sidebar-header" className="p-4 border-b border-slate-100 dark:border-slate-800">
        <div className="flex items-center justify-between mb-3">
          <div className="flex items-center gap-2.5">
            <div className="w-9 h-9 rounded-xl bg-blue-600 flex items-center justify-center text-white shadow-sm shadow-blue-500/30">
              <BookOpen className="w-4 h-4" />
            </div>
            <div>
              <h1 className="font-bold text-slate-900 dark:text-white text-sm tracking-tight flex items-center gap-1.5">
                Darslar Rejasi
              </h1>
              <p className="text-[11px] text-slate-500 dark:text-slate-400 font-medium">
                {activeGroup ? `${activeGroup.name} darslari` : 'Standart Darslar'}
              </p>
            </div>
          </div>

          <div className="flex items-center gap-1.5">
            {onToggleDarkMode && (
              <button
                onClick={onToggleDarkMode}
                title={isDarkMode ? "Yorug' rejimga o'tish" : "Tungi rejimga (Dark Mode) o'tish"}
                className="w-8 h-8 rounded-lg bg-slate-100 hover:bg-slate-200 dark:bg-slate-800 dark:hover:bg-slate-700 text-amber-500 dark:text-yellow-400 flex items-center justify-center transition-all shadow-xs cursor-pointer"
              >
                {isDarkMode ? <Sun className="w-4 h-4" /> : <Moon className="w-4 h-4 text-purple-600" />}
              </button>
            )}
            <button
              onClick={onOpenSettings}
              title="Sozlamalar (Notion)"
              className="w-8 h-8 rounded-lg bg-slate-50 hover:bg-slate-100 dark:bg-slate-800 dark:hover:bg-slate-750 text-slate-600 dark:text-slate-300 flex items-center justify-center transition-colors shadow-xs cursor-pointer"
            >
              <Settings className="w-4 h-4" />
            </button>
            <button
              onClick={onOpenImportModal}
              title="Notion'dan import qilish"
              className="w-8 h-8 rounded-lg bg-slate-50 hover:bg-slate-100 dark:bg-slate-800 dark:hover:bg-slate-750 text-slate-600 dark:text-slate-300 flex items-center justify-center transition-colors shadow-xs cursor-pointer"
            >
              <Upload className="w-4 h-4" />
            </button>
            <button
              id="add-new-lesson-btn"
              onClick={onOpenAddModal}
              title="Yangi dars qo'shish"
              className="w-8 h-8 rounded-lg bg-blue-50 dark:bg-blue-950/60 hover:bg-blue-600 text-blue-600 hover:text-white dark:text-blue-400 dark:hover:text-white flex items-center justify-center transition-colors shadow-xs cursor-pointer"
            >
              <Plus className="w-4 h-4" />
            </button>
          </div>
        </div>

        {/* Search Bar */}
        <div className="relative mb-3">
          <Search className="w-4 h-4 absolute left-3 top-1/2 -translate-y-1/2 text-slate-400" />
          <input 
            type="text"
            placeholder="Dars yoki raqam boyicha qidirish..."
            value={searchQuery}
            onChange={(e) => setSearchQuery(e.target.value)}
            className="w-full pl-9 pr-3 py-2 bg-slate-50 dark:bg-slate-800 border border-slate-200 dark:border-slate-700 rounded-xl text-xs text-slate-800 dark:text-slate-200 focus:outline-none focus:ring-2 focus:ring-blue-500/50"
          />
        </div>

        {/* Status Filter Badges */}
        <div className="flex items-center gap-1 overflow-x-auto pb-1 no-scrollbar text-[11px]">
          <button
            onClick={() => setSelectedStatus('all')}
            className={`px-2.5 py-1 rounded-lg font-medium whitespace-nowrap transition-colors ${
              selectedStatus === 'all' 
                ? 'bg-slate-900 text-white dark:bg-slate-100 dark:text-slate-900 font-semibold' 
                : 'bg-slate-100 text-slate-600 hover:bg-slate-200 dark:bg-slate-800 dark:text-slate-400'
            }`}
          >
            Barchasi ({totalLessons})
          </button>
          <button
            onClick={() => setSelectedStatus('completed')}
            className={`px-2.5 py-1 rounded-lg font-medium whitespace-nowrap transition-colors flex items-center gap-1 ${
              selectedStatus === 'completed' 
                ? 'bg-emerald-600 text-white font-semibold' 
                : 'bg-emerald-50 text-emerald-700 hover:bg-emerald-100 dark:bg-emerald-950/40 dark:text-emerald-400'
            }`}
          >
            <CheckCircle2 className="w-3 h-3" />
            O'tildi ({completedCount})
          </button>
          <button
            onClick={() => setSelectedStatus('current')}
            className={`px-2.5 py-1 rounded-lg font-medium whitespace-nowrap transition-colors flex items-center gap-1 ${
              selectedStatus === 'current' 
                ? 'bg-blue-600 text-white font-semibold' 
                : 'bg-blue-50 text-blue-700 hover:bg-blue-100 dark:bg-blue-950/40 dark:text-blue-400'
            }`}
          >
            <Clock className="w-3 h-3" />
            Jarayonda ({currentCount})
          </button>
          <button
            onClick={() => setSelectedStatus('planned')}
            className={`px-2.5 py-1 rounded-lg font-medium whitespace-nowrap transition-colors flex items-center gap-1 ${
              selectedStatus === 'planned' 
                ? 'bg-slate-700 text-white font-semibold' 
                : 'bg-slate-100 text-slate-600 hover:bg-slate-200 dark:bg-slate-800 dark:text-slate-400'
            }`}
          >
            <Calendar className="w-3 h-3" />
            Reja ({plannedCount})
          </button>
        </div>

        {/* Batch Selection Mode Toggle Bar */}
        <div className="flex items-center justify-between mt-2 pt-2 border-t border-slate-100 dark:border-slate-800">
          <button
            type="button"
            onClick={() => {
              setIsBatchMode(!isBatchMode);
              setBatchSelectedIds([]);
            }}
            className={`px-2.5 py-1 rounded-lg text-[11px] font-bold transition flex items-center gap-1.5 cursor-pointer ${
              isBatchMode 
                ? 'bg-purple-600 text-white shadow-xs' 
                : 'bg-slate-100 hover:bg-slate-200 dark:bg-slate-800 dark:hover:bg-slate-750 text-slate-700 dark:text-slate-300'
            }`}
          >
            <CheckSquare className="w-3.5 h-3.5 text-yellow-300" />
            {isBatchMode ? "Yopish" : "☑️ Ko'plab Tanlash Rejimi"}
          </button>

          {isBatchMode && (
            <div className="flex items-center gap-2 text-[11px]">
              <button
                type="button"
                onClick={() => {
                  if (batchSelectedIds.length === filteredLessons.length) {
                    setBatchSelectedIds([]);
                  } else {
                    setBatchSelectedIds(filteredLessons.map(l => l.id));
                  }
                }}
                className="text-purple-600 dark:text-purple-400 font-extrabold hover:underline cursor-pointer"
              >
                {batchSelectedIds.length === filteredLessons.length ? 'Tozalash' : 'Barchasini tanlash'}
              </button>
              <span className="text-slate-300 dark:text-slate-700">|</span>
              <span className="font-extrabold text-purple-600 dark:text-purple-400">{batchSelectedIds.length} ta</span>
            </div>
          )}
        </div>
      </div>

      {/* Batch Actions Floating Panel */}
      {isBatchMode && batchSelectedIds.length > 0 && (
        <div className="mx-3 mt-2 p-2.5 bg-purple-950/30 border border-purple-800/80 rounded-2xl flex flex-col gap-2 animate-fadeIn shadow-lg">
          <div className="flex items-center justify-between text-[11px] font-extrabold text-purple-200">
            <span>Tanlangan {batchSelectedIds.length} ta dars:</span>
            <button 
              onClick={() => setBatchSelectedIds([])}
              className="text-purple-400 hover:text-purple-200 font-bold"
            >
              Tozalash
            </button>
          </div>
          
          <div className="grid grid-cols-3 gap-1.5">
            <button
              onClick={() => {
                if (onBatchUpdateStatus) {
                  onBatchUpdateStatus(batchSelectedIds, 'completed');
                  setBatchSelectedIds([]);
                }
              }}
              className="py-1.5 px-2 bg-emerald-600 hover:bg-emerald-700 text-white text-[10px] font-black rounded-xl transition flex items-center justify-center gap-1 shadow-xs cursor-pointer"
            >
              <CheckCircle2 className="w-3 h-3" /> ✅ O'tildi
            </button>

            <button
              onClick={() => {
                if (onBatchUpdateStatus) {
                  onBatchUpdateStatus(batchSelectedIds, 'current');
                  setBatchSelectedIds([]);
                }
              }}
              className="py-1.5 px-2 bg-blue-600 hover:bg-blue-700 text-white text-[10px] font-black rounded-xl transition flex items-center justify-center gap-1 shadow-xs cursor-pointer"
            >
              <Clock className="w-3 h-3" /> 🔄 Jarayonda
            </button>

            <button
              onClick={() => {
                if (onBatchUpdateStatus) {
                  onBatchUpdateStatus(batchSelectedIds, 'planned');
                  setBatchSelectedIds([]);
                }
              }}
              className="py-1.5 px-2 bg-slate-700 hover:bg-slate-800 text-white text-[10px] font-black rounded-xl transition flex items-center justify-center gap-1 shadow-xs cursor-pointer"
            >
              <Calendar className="w-3 h-3" /> 📅 Reja
            </button>
          </div>
        </div>
      )}

      {/* Lesson List */}
      <div id="lessons-scroll-area" className="flex-1 overflow-y-auto p-2 space-y-1.5">
        {filteredLessons.length === 0 ? (
          <div className="p-8 text-center text-slate-400 dark:text-slate-500 text-xs">
            Darslar topilmadi
          </div>
        ) : (
          filteredLessons.map((lesson) => {
            const isSelected = lesson.id === selectedLessonId;

            return (
              <div
                key={lesson.id}
                onClick={() => onSelectLesson(lesson.id)}
                className={`p-3 rounded-xl cursor-pointer transition-all duration-300 group border active:scale-[0.98] ${
                  isSelected
                    ? 'bg-gradient-to-r from-blue-50 to-purple-50/80 dark:from-blue-950/60 dark:to-purple-950/40 border-blue-300 dark:border-blue-700 shadow-md translate-x-1'
                    : 'bg-transparent hover:bg-slate-100/80 dark:hover:bg-slate-800/80 border-transparent hover:translate-x-1.5'
                }`}
              >
                <div className="flex items-start gap-3">
                  {/* Batch Select Checkbox */}
                  {isBatchMode && (
                    <div 
                      onClick={(e) => {
                        e.stopPropagation();
                        if (batchSelectedIds.includes(lesson.id)) {
                          setBatchSelectedIds(batchSelectedIds.filter(id => id !== lesson.id));
                        } else {
                          setBatchSelectedIds([...batchSelectedIds, lesson.id]);
                        }
                      }}
                      className={`w-5 h-5 mt-2.5 rounded-lg border flex items-center justify-center cursor-pointer transition shrink-0 ${
                        batchSelectedIds.includes(lesson.id)
                          ? 'bg-purple-600 border-purple-600 text-white shadow-xs'
                          : 'border-slate-300 dark:border-slate-700 bg-white dark:bg-slate-800'
                      }`}
                    >
                      {batchSelectedIds.includes(lesson.id) && <Check className="w-3.5 h-3.5 stroke-[3]" />}
                    </div>
                  )}

                  {/* Lesson Number Badge */}
                  <div
                    className={`w-10 h-10 rounded-lg flex flex-col items-center justify-center shrink-0 font-bold transition-all ${
                      isSelected
                        ? 'bg-blue-600 text-white shadow-xs shadow-blue-600/30'
                        : lesson.status === 'completed'
                        ? 'bg-emerald-50 text-emerald-700 dark:bg-emerald-950/60 dark:text-emerald-400 border border-emerald-200 dark:border-emerald-800'
                        : lesson.status === 'current'
                        ? 'bg-blue-50 text-blue-700 dark:bg-blue-950/60 dark:text-blue-400 border border-blue-200 dark:border-blue-800'
                        : 'bg-slate-100 text-slate-700 dark:bg-slate-800 dark:text-slate-300 border border-slate-200 dark:border-slate-700'
                    }`}
                  >
                    <span className="text-[9px] uppercase font-semibold leading-none opacity-80">Dars</span>
                    <span className="text-sm leading-tight">{lesson.lessonNumber}</span>
                  </div>

                  {/* Title & metadata */}
                  <div className="flex-1 min-w-0">
                    <div className="flex items-center justify-between gap-1.5 mb-1">
                      <span className="text-[10px] font-semibold text-slate-500 dark:text-slate-400 truncate">
                        {lesson.date}
                      </span>
                      
                      {/* Status indicator pill */}
                      {userRole === 'student' && lesson.status !== 'completed' ? (
                        <span className="inline-flex items-center gap-0.5 text-[10px] font-extrabold text-amber-600 dark:text-amber-400 bg-amber-50 dark:bg-amber-950/60 px-1.5 py-0.2 rounded shrink-0">
                          🔒 Qulflangan
                        </span>
                      ) : (
                        <>
                          {lesson.status === 'completed' && (
                            <span className="inline-flex items-center gap-0.5 text-[10px] font-semibold text-emerald-600 dark:text-emerald-400 bg-emerald-50 dark:bg-emerald-950/50 px-1.5 py-0.2 rounded shrink-0">
                              <CheckCircle2 className="w-2.5 h-2.5" />
                              O'tildi
                            </span>
                          )}
                          {(lesson.status === 'current' || lesson.status === 'pending') && (
                            <span className="inline-flex items-center gap-0.5 text-[10px] font-semibold text-blue-600 dark:text-blue-400 bg-blue-50 dark:bg-blue-950/50 px-1.5 py-0.2 rounded shrink-0 font-bold">
                              <Clock className="w-2.5 h-2.5" />
                              Jarayonda
                            </span>
                          )}
                          {lesson.status === 'planned' && (
                            <span className="inline-flex items-center gap-0.5 text-[10px] font-semibold text-slate-500 dark:text-slate-400 bg-slate-100 dark:bg-slate-800 px-1.5 py-0.2 rounded shrink-0">
                              <Calendar className="w-2.5 h-2.5" />
                              Reja
                            </span>
                          )}
                        </>
                      )}
                    </div>

                    <h3 className={`text-xs font-semibold leading-snug line-clamp-2 ${
                      isSelected 
                        ? 'text-blue-900 dark:text-blue-200' 
                        : 'text-slate-800 dark:text-slate-200'
                    }`}>
                      {lesson.title}
                    </h3>

                    <div className="flex items-center justify-between text-[11px] text-slate-400 dark:text-slate-500 mt-1.5">
                      <span className="truncate">{lesson.time || 'Vaqt belgilanmagan'}</span>
                      <span className="flex items-center gap-1 text-[10px]">
                        {lesson.materials && lesson.materials.length > 0 && (
                          <span className="bg-slate-100 dark:bg-slate-800 px-1 rounded text-slate-600 dark:text-slate-300">
                            📎 {lesson.materials.length} fayl
                          </span>
                        )}
                        <ChevronRight className={`w-3.5 h-3.5 transition-transform ${isSelected ? 'text-blue-600 translate-x-0.5' : 'text-slate-300 opacity-0 group-hover:opacity-100'}`} />
                      </span>
                    </div>
                  </div>
                </div>
              </div>
            );
          })
        )}
      </div>

      {/* Footer info */}
      <div className="p-3 border-t border-slate-100 dark:border-slate-800 bg-slate-50/70 dark:bg-slate-900/50 flex items-center justify-between text-xs text-slate-500">
        <div className="flex flex-col text-left">
          <span className="font-semibold text-slate-700 dark:text-slate-300">
            {activeGroup ? activeGroup.name : 'Standart Darslar'}
          </span>
          <span className="text-[10px] text-slate-400">
            {activeGroup ? `${activeGroup.completedCount}/72 dars o'tildi` : 'Guruh tanlanmagan'}
          </span>
        </div>
        {onLogout && (
          <button
            onClick={onLogout}
            className="px-2.5 py-1 rounded bg-rose-50 hover:bg-rose-600 dark:bg-rose-950/20 text-rose-600 hover:text-white dark:text-rose-400 border border-rose-200 dark:border-rose-900/50 text-[10px] font-bold flex items-center gap-1 transition-all cursor-pointer"
          >
            Chiqish
          </button>
        )}
      </div>
    </aside>
  );
};
