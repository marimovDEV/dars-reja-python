import React, { useState } from 'react';
import { Group, GroupFormData } from '../types/group';
import { Users, Plus, Calendar, Clock, Send, FileText, CheckCircle2, ChevronRight, Sparkles, BookOpen } from 'lucide-react';

interface GroupSelectModalProps {
  isOpen: boolean;
  onClose: () => void;
  groups: Group[];
  activeGroupId: string | null;
  onSelectGroup: (groupId: string) => void;
  onCreateGroup: (data: GroupFormData) => Promise<void>;
}

export function GroupSelectModal({
  isOpen,
  onClose,
  groups,
  activeGroupId,
  onSelectGroup,
  onCreateGroup
}: GroupSelectModalProps) {
  const [activeTab, setActiveTab] = useState<'select' | 'create'>(groups.length === 0 ? 'create' : 'select');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  // Form state
  const [name, setName] = useState('');
  const [startDate, setStartDate] = useState(new Date().toISOString().split('T')[0]);
  const [scheduleDays, setScheduleDays] = useState('Dush / Chor / Juma');
  const [scheduleTime, setScheduleTime] = useState('14:00 - 16:00');
  const [studentCount, setStudentCount] = useState<number | ''>('');
  const [telegramLink, setTelegramLink] = useState('');
  const [notes, setNotes] = useState('');

  if (!isOpen) return null;

  const handleSubmitCreate = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!name.trim()) {
      setError("Guruh nomini kiriting");
      return;
    }
    if (!startDate) {
      setError("Boshlanish sanasini kiriting");
      return;
    }

    setLoading(true);
    setError(null);
    try {
      await onCreateGroup({
        name: name.trim(),
        startDate,
        scheduleDays,
        scheduleTime,
        studentCount: studentCount ? Number(studentCount) : undefined,
        telegramLink: telegramLink.trim() || undefined,
        notes: notes.trim() || undefined
      });
      // Reset form
      setName('');
      setStudentCount('');
      setTelegramLink('');
      setNotes('');
      onClose();
    } catch (err: any) {
      setError(err.message || "Guruh yaratishda xatolik yuz berdi");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-slate-900/80 backdrop-blur-md animate-fadeIn">
      <div className="bg-white dark:bg-slate-900 rounded-3xl shadow-2xl border border-slate-200 dark:border-slate-800 w-full max-w-2xl overflow-hidden flex flex-col max-h-[90vh]">
        
        {/* Header */}
        <div className="p-6 bg-gradient-to-r from-blue-600 via-indigo-600 to-violet-600 text-white relative">
          <div className="flex items-center justify-between">
            <div className="flex items-center gap-3">
              <div className="p-3 bg-white/15 backdrop-blur-md rounded-2xl">
                <Users className="w-7 h-7 text-white" />
              </div>
              <div>
                <h2 className="text-xl font-bold">Guruhni Tanlang yoki Yaratish</h2>
                <p className="text-blue-100 text-xs mt-0.5">Har bir guruh uchun dars rejasi va kalendar avtomatik shakllanadi</p>
              </div>
            </div>
            {groups.length > 0 && activeGroupId && (
              <button
                onClick={onClose}
                className="text-white/80 hover:text-white p-2 rounded-full hover:bg-white/10 transition"
              >
                ✕
              </button>
            )}
          </div>

          {/* Navigation Tabs */}
          <div className="flex gap-2 mt-6 p-1.5 bg-black/20 backdrop-blur-md rounded-xl">
            <button
              onClick={() => setActiveTab('select')}
              disabled={groups.length === 0}
              className={`flex-1 py-2 px-4 rounded-lg font-medium text-xs transition flex items-center justify-center gap-2 ${
                activeTab === 'select'
                  ? 'bg-white text-blue-600 shadow-md'
                  : 'text-white/80 hover:text-white hover:bg-white/10 disabled:opacity-50'
              }`}
            >
              <BookOpen className="w-4 h-4" />
              Mavjud Guruhlar ({groups.length})
            </button>
            <button
              onClick={() => setActiveTab('create')}
              className={`flex-1 py-2 px-4 rounded-lg font-medium text-xs transition flex items-center justify-center gap-2 ${
                activeTab === 'create'
                  ? 'bg-white text-blue-600 shadow-md'
                  : 'text-white/80 hover:text-white hover:bg-white/10'
              }`}
            >
              <Plus className="w-4 h-4" />
              Yangi Guruh Yaratish
            </button>
          </div>
        </div>

        {/* Content Body */}
        <div className="p-6 overflow-y-auto flex-1">
          {error && (
            <div className="mb-4 p-3.5 bg-rose-50 border border-rose-200 text-rose-700 rounded-xl text-xs flex items-center gap-2 dark:bg-rose-950/30 dark:border-rose-800 dark:text-rose-300">
              ⚠️ {error}
            </div>
          )}

          {activeTab === 'select' ? (
            <div className="space-y-3">
              {groups.length === 0 ? (
                <div className="text-center py-8 text-slate-500">
                  Hali hech qanday guruh yaratilmagan.
                </div>
              ) : (
                groups.map(group => {
                  const isSelected = group.id === activeGroupId;
                  const progressPercent = Math.round((group.completedCount / (group.totalLessons || 72)) * 100);

                  return (
                    <div
                      key={group.id}
                      onClick={() => {
                        onSelectGroup(group.id);
                        onClose();
                      }}
                      className={`p-4 rounded-2xl border transition cursor-pointer flex items-center justify-between group ${
                        isSelected
                          ? 'border-blue-500 bg-blue-50/60 dark:bg-blue-950/30 dark:border-blue-500/70 shadow-sm'
                          : 'border-slate-200 dark:border-slate-800 hover:border-blue-300 dark:hover:border-blue-700 hover:bg-slate-50 dark:hover:bg-slate-800/40'
                      }`}
                    >
                      <div className="space-y-1.5 flex-1 pr-4">
                        <div className="flex items-center gap-2">
                          <h3 className="font-semibold text-slate-800 dark:text-slate-100 group-hover:text-blue-600 dark:group-hover:text-blue-400 transition">
                            {group.name}
                          </h3>
                          {isSelected && (
                            <span className="px-2 py-0.5 text-[10px] font-bold bg-blue-600 text-white rounded-full flex items-center gap-1">
                              <CheckCircle2 className="w-3 h-3" /> Faol
                            </span>
                          )}
                        </div>

                        <div className="flex flex-wrap items-center gap-x-4 gap-y-1 text-xs text-slate-500 dark:text-slate-400">
                          <span className="flex items-center gap-1">
                            <Calendar className="w-3.5 h-3.5 text-blue-500" />
                            Boshlanish: {group.startDate}
                          </span>
                          <span className="flex items-center gap-1">
                            <Clock className="w-3.5 h-3.5 text-indigo-500" />
                            {group.scheduleDays} ({group.scheduleTime})
                          </span>
                          {group.studentCount ? (
                            <span className="flex items-center gap-1">
                              <Users className="w-3.5 h-3.5 text-emerald-500" />
                              {group.studentCount} o'quvchi
                            </span>
                          ) : null}
                        </div>

                        {/* Current topic & progress bar */}
                        <div className="pt-2">
                          <div className="flex items-center justify-between text-xs mb-1">
                            <span className="font-medium text-slate-700 dark:text-slate-300">
                              📌 Joriy: <strong className="text-blue-600 dark:text-blue-400">{group.currentLessonNumber}-dars</strong> ({group.currentLessonTitle})
                            </span>
                            <span className="font-semibold text-slate-600 dark:text-slate-400">
                              {progressPercent}%
                            </span>
                          </div>
                          <div className="w-full h-1.5 bg-slate-200 dark:bg-slate-700 rounded-full overflow-hidden">
                            <div
                              className="h-full bg-gradient-to-r from-blue-500 to-emerald-500 transition-all duration-500"
                              style={{ width: `${progressPercent}%` }}
                            />
                          </div>
                        </div>
                      </div>

                      <div className="pl-2">
                        <div className="p-2 rounded-xl bg-slate-100 dark:bg-slate-800 text-slate-400 group-hover:text-blue-600 group-hover:bg-blue-100 dark:group-hover:bg-blue-900/40 transition">
                          <ChevronRight className="w-5 h-5" />
                        </div>
                      </div>
                    </div>
                  );
                })
              )}
            </div>
          ) : (
            <form onSubmit={handleSubmitCreate} className="space-y-4">
              <div>
                <label className="block text-xs font-semibold text-slate-700 dark:text-slate-300 mb-1">
                  Guruh Nomi <span className="text-rose-500">*</span>
                </label>
                <input
                  type="text"
                  required
                  placeholder="Masalan: Python Backend — 101-guruh"
                  value={name}
                  onChange={e => setName(e.target.value)}
                  className="w-full px-3.5 py-2.5 rounded-xl border border-slate-300 dark:border-slate-700 bg-white dark:bg-slate-800 text-slate-800 dark:text-slate-100 text-xs focus:ring-2 focus:ring-blue-500 outline-none"
                />
              </div>

              <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                <div>
                  <label className="block text-xs font-semibold text-slate-700 dark:text-slate-300 mb-1">
                    Boshlanish Sanasi <span className="text-rose-500">*</span>
                  </label>
                  <input
                    type="date"
                    required
                    value={startDate}
                    onChange={e => setStartDate(e.target.value)}
                    className="w-full px-3.5 py-2.5 rounded-xl border border-slate-300 dark:border-slate-700 bg-white dark:bg-slate-800 text-slate-800 dark:text-slate-100 text-xs focus:ring-2 focus:ring-blue-500 outline-none"
                  />
                  <p className="text-[10px] text-slate-500 mt-1">72 ta dars sanasi shu kundan boshlab hisoblanadi</p>
                </div>

                <div>
                  <label className="block text-xs font-semibold text-slate-700 dark:text-slate-300 mb-1">
                    Dars Kunlari <span className="text-rose-500">*</span>
                  </label>
                  <select
                    value={scheduleDays}
                    onChange={e => setScheduleDays(e.target.value)}
                    className="w-full px-3.5 py-2.5 rounded-xl border border-slate-300 dark:border-slate-700 bg-white dark:bg-slate-800 text-slate-800 dark:text-slate-100 text-xs focus:ring-2 focus:ring-blue-500 outline-none"
                  >
                    <option value="Dush / Chor / Juma">Dush / Chor / Juma (Toq kunlar)</option>
                    <option value="Sesh / Pay / Shan">Sesh / Pay / Shan (Juft kunlar)</option>
                    <option value="Har kuni">Har kuni</option>
                  </select>
                </div>
              </div>

              <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                <div>
                  <label className="block text-xs font-semibold text-slate-700 dark:text-slate-300 mb-1">
                    Dars Vaqti <span className="text-rose-500">*</span>
                  </label>
                  <select
                    value={scheduleTime}
                    onChange={e => setScheduleTime(e.target.value)}
                    className="w-full px-3.5 py-2.5 rounded-xl border border-slate-300 dark:border-slate-700 bg-white dark:bg-slate-800 text-slate-800 dark:text-slate-100 text-xs focus:ring-2 focus:ring-blue-500 outline-none"
                  >
                    <option value="14:00 - 16:00">14:00 - 16:00 (Kunduzgi)</option>
                    <option value="09:00 - 11:00">09:00 - 11:00 (Ertalabki)</option>
                    <option value="16:00 - 18:00">16:00 - 18:00 (Kechki)</option>
                    <option value="18:30 - 20:30">18:30 - 20:30 (Kechki 2)</option>
                  </select>
                </div>

                <div>
                  <label className="block text-xs font-semibold text-slate-700 dark:text-slate-300 mb-1">
                    O'quvchilar Soni (Ixtiyoriy)
                  </label>
                  <input
                    type="number"
                    min="1"
                    placeholder="Masalan: 18"
                    value={studentCount}
                    onChange={e => setStudentCount(e.target.value ? Number(e.target.value) : '')}
                    className="w-full px-3.5 py-2.5 rounded-xl border border-slate-300 dark:border-slate-700 bg-white dark:bg-slate-800 text-slate-800 dark:text-slate-100 text-xs focus:ring-2 focus:ring-blue-500 outline-none"
                  />
                </div>
              </div>

              <div>
                <label className="block text-xs font-semibold text-slate-700 dark:text-slate-300 mb-1">
                  Telegram Guruh Havolasi (Ixtiyoriy)
                </label>
                <input
                  type="url"
                  placeholder="https://t.me/guruh_linki"
                  value={telegramLink}
                  onChange={e => setTelegramLink(e.target.value)}
                  className="w-full px-3.5 py-2.5 rounded-xl border border-slate-300 dark:border-slate-700 bg-white dark:bg-slate-800 text-slate-800 dark:text-slate-100 text-xs focus:ring-2 focus:ring-blue-500 outline-none"
                />
              </div>

              <div>
                <label className="block text-xs font-semibold text-slate-700 dark:text-slate-300 mb-1">
                  Izoh (Ixtiyoriy)
                </label>
                <textarea
                  rows={2}
                  placeholder="Guruh haqida qo'shimcha ma'lumot..."
                  value={notes}
                  onChange={e => setNotes(e.target.value)}
                  className="w-full px-3.5 py-2.5 rounded-xl border border-slate-300 dark:border-slate-700 bg-white dark:bg-slate-800 text-slate-800 dark:text-slate-100 text-xs focus:ring-2 focus:ring-blue-500 outline-none"
                />
              </div>

              <div className="pt-2 flex justify-end gap-3">
                {groups.length > 0 && (
                  <button
                    type="button"
                    onClick={() => setActiveTab('select')}
                    className="px-4 py-2.5 text-xs font-medium text-slate-600 hover:text-slate-800 dark:text-slate-400 dark:hover:text-slate-200"
                  >
                    Bekor qilish
                  </button>
                )}
                <button
                  type="submit"
                  disabled={loading}
                  className="px-6 py-2.5 bg-gradient-to-r from-blue-600 to-indigo-600 text-white rounded-xl font-semibold text-xs shadow-md hover:from-blue-700 hover:to-indigo-700 transition disabled:opacity-50 flex items-center gap-2"
                >
                  <Sparkles className="w-4 h-4" />
                  {loading ? 'Yaratilmoqda...' : 'Yangi Guruhni Yaratish'}
                </button>
              </div>
            </form>
          )}
        </div>
      </div>
    </div>
  );
}
