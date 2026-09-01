import React, { useState, useEffect } from 'react';
import { X, RefreshCw, CheckCircle2, AlertTriangle, HelpCircle, Loader2 } from 'lucide-react';
import { NotionPreviewResponse } from '../notion/notionTypes';

interface NotionSyncModalProps {
  isOpen: boolean;
  onClose: () => void;
  notionUrl: string;
  onSyncComplete: () => void;
}

export const NotionSyncModal: React.FC<NotionSyncModalProps> = ({
  isOpen,
  onClose,
  notionUrl,
  onSyncComplete
}) => {
  const [step, setStep] = useState<'loading' | 'preview' | 'syncing' | 'success'>('loading');
  const [previewData, setPreviewData] = useState<NotionPreviewResponse | null>(null);
  const [error, setError] = useState<string>('');
  
  // Sync mode and confirmation states
  const [syncMode, setSyncMode] = useState<'merge' | 'replace'>('merge');
  const [confirmInput, setConfirmInput] = useState('');
  const [showConfirmError, setShowConfirmError] = useState(false);

  // Fetch Notion preview data on open
  useEffect(() => {
    if (isOpen && notionUrl) {
      setStep('loading');
      setError('');
      setPreviewData(null);

      fetch('/api/notion/preview', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ notionUrl })
      })
        .then(res => {
          if (!res.ok) return res.json().then(e => { throw new Error(e.error); });
          return res.json();
        })
        .then((data: NotionPreviewResponse) => {
          setPreviewData(data);
          setStep('preview');
        })
        .catch(err => {
          console.error(err);
          setError(err.message || 'Notion ma‘lumotlarini yuklab bo‘lmadi. Sozlamalarni tekshiring.');
          setStep('preview'); // transition to show error
        });
    }
  }, [isOpen, notionUrl]);

  if (!isOpen) return null;

  const handleStartSync = () => {
    if (!previewData) return;

    if (syncMode === 'replace' && confirmInput.trim().toUpperCase() !== 'ROZIMAN') {
      setShowConfirmError(true);
      return;
    }

    setStep('syncing');
    setError('');

    // Try scraper endpoint first for full content extraction
    fetch('/api/scrape', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        notionUrl,
        mode: syncMode
      })
    })
      .then(res => {
        if (!res.ok) {
          // Fallback to standard Notion sync if scraper is not applicable
          return fetch('/api/notion/sync', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ notionUrl, mode: syncMode, previewData })
          }).then(r => r.json());
        }
        return res.json();
      })
      .then(() => {
        setStep('success');
      })
      .catch(err => {
        console.error(err);
        setError(err.message || 'Sinxronlash jarayonida xatolik yuz berdi.');
        setStep('preview');
      });
  };

  const handleFinalize = () => {
    onSyncComplete();
    onClose();
    // Reset state
    setStep('loading');
    setPreviewData(null);
    setError('');
    setSyncMode('merge');
    setConfirmInput('');
    setShowConfirmError(false);
  };

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center bg-slate-900/60 backdrop-blur-xs p-4 font-sans text-xs text-left">
      <div className="bg-white dark:bg-slate-900 w-full max-w-3xl rounded-2xl shadow-2xl border border-slate-200 dark:border-slate-800 overflow-hidden flex flex-col max-h-[90vh]">
        
        {/* Header */}
        <div className="px-6 py-4 border-b border-slate-200 dark:border-slate-800 flex items-center justify-between bg-slate-50/50 dark:bg-slate-900/50">
          <div>
            <h2 className="text-sm font-bold text-slate-950 dark:text-white">Notion sinxronlash oynasi</h2>
            <p className="text-[10px] text-slate-500 dark:text-slate-400 mt-0.5">Notion sahifa yoki bazasi bilan dars rejasini sinxronlash</p>
          </div>
          {step !== 'syncing' && (
            <button 
              onClick={onClose}
              className="p-1.5 rounded-lg hover:bg-slate-100 dark:hover:bg-slate-800 text-slate-500 hover:text-slate-700 dark:hover:text-slate-300 transition-colors"
            >
              <X className="w-5 h-5" />
            </button>
          )}
        </div>

        {/* Content Body */}
        <div className="flex-1 overflow-y-auto p-6">
          
          {step === 'loading' && (
            <div className="flex flex-col items-center justify-center py-12 text-slate-500">
              <Loader2 className="w-10 h-10 text-blue-600 animate-spin mb-3" />
              <span className="font-semibold text-slate-750 dark:text-slate-350 text-sm">Notion ma'lumotlari tahlil qilinmoqda...</span>
              <p className="text-[10px] text-slate-400 mt-1">Notion sahifa/database dars rejasi va hujjatlar ro‘yxati yuklanmoqda</p>
            </div>
          )}

          {step === 'preview' && (
            <div className="space-y-6">
              {error ? (
                <div className="p-4 rounded-xl bg-rose-50 dark:bg-rose-950/30 border border-rose-200 dark:border-rose-900/40 text-rose-600 dark:text-rose-400 space-y-2">
                  <div className="flex items-center gap-2 font-bold">
                    <AlertTriangle className="w-5 h-5 shrink-0" />
                    <span>Yuklashda Xatolik Yuz Berdi!</span>
                  </div>
                  <p>{error}</p>
                </div>
              ) : (
                previewData && (
                  <>
                    {/* Summary row cards */}
                    <div className="grid grid-cols-3 gap-3">
                      <div className="p-3 bg-blue-50/40 dark:bg-blue-950/20 border border-blue-100 dark:border-blue-900/30 rounded-xl">
                        <span className="text-[10px] text-slate-400">Darslar topildi:</span>
                        <p className="text-base font-bold text-blue-600 dark:text-blue-400 mt-0.5">
                          {previewData.summary.lessonsFound} ta
                        </p>
                      </div>
                      <div className="p-3 bg-indigo-50/40 dark:bg-indigo-950/20 border border-indigo-100 dark:border-indigo-900/30 rounded-xl">
                        <span className="text-[10px] text-slate-400">Hujjatlar topildi:</span>
                        <p className="text-base font-bold text-indigo-600 dark:text-indigo-400 mt-0.5">
                          {previewData.summary.documentsFound} ta
                        </p>
                      </div>
                      <div className={`p-3 rounded-xl border ${
                        previewData.summary.warnings.length > 0 
                          ? 'bg-amber-50/40 dark:bg-amber-950/20 border-amber-100 dark:border-amber-900/30' 
                          : 'bg-emerald-50/40 dark:bg-emerald-950/20 border-emerald-100 dark:border-emerald-900/30'
                      }`}>
                        <span className="text-[10px] text-slate-400">Ogohlantirishlar:</span>
                        <p className={`text-base font-bold mt-0.5 ${
                          previewData.summary.warnings.length > 0 ? 'text-amber-600 dark:text-amber-400' : 'text-emerald-600 dark:text-emerald-400'
                        }`}>
                          {previewData.summary.warnings.length} ta
                        </p>
                      </div>
                    </div>

                    {/* Warnings List Card */}
                    {previewData.summary.warnings.length > 0 && (
                      <div className="p-4 bg-amber-50/50 dark:bg-amber-950/25 border border-amber-200 dark:border-amber-900/40 rounded-xl space-y-1.5">
                        <div className="flex items-center gap-2 font-bold text-amber-700 dark:text-amber-400">
                          <AlertTriangle className="w-4 h-4 shrink-0" />
                          <span>Yuklash jarayonidagi ogohlantirishlar:</span>
                        </div>
                        <ul className="list-disc list-inside text-amber-600/90 dark:text-amber-400/90 pl-1 text-[11px] space-y-0.5 max-h-24 overflow-y-auto">
                          {previewData.summary.warnings.map((w, idx) => (
                            <li key={idx}>{w}</li>
                          ))}
                        </ul>
                      </div>
                    )}

                    {/* Sync Mode Selector Card */}
                    <div className="p-4 bg-slate-50 dark:bg-slate-800/40 border border-slate-200 dark:border-slate-800 rounded-xl space-y-4">
                      <h3 className="font-bold text-slate-900 dark:text-slate-200">Sinxronlash rejimi:</h3>
                      <div className="grid grid-cols-1 md:grid-cols-2 gap-3">
                        
                        <label className={`p-3 rounded-xl border flex items-start gap-2.5 cursor-pointer transition-all ${
                          syncMode === 'merge'
                            ? 'border-blue-500 bg-blue-50/20 dark:bg-blue-950/10'
                            : 'border-slate-200 dark:border-slate-800 hover:bg-slate-100/50 dark:hover:bg-slate-800/30'
                        }`}>
                          <input 
                            type="radio" 
                            name="syncMode" 
                            value="merge"
                            checked={syncMode === 'merge'}
                            onChange={() => setSyncMode('merge')}
                            className="mt-1" 
                          />
                          <div>
                            <span className="font-bold text-slate-900 dark:text-slate-200">Darslarni yangilash va qo'shish (Merge)</span>
                            <p className="text-[10px] text-slate-500 dark:text-slate-400 mt-0.5">Mavjud dars rejalar saqlanadi, ustma-ust tushgan dars raqamlari Notion dagilarga almashtiriladi.</p>
                          </div>
                        </label>

                        <label className={`p-3 rounded-xl border flex items-start gap-2.5 cursor-pointer transition-all ${
                          syncMode === 'replace'
                            ? 'border-amber-500 bg-amber-50/20 dark:bg-amber-950/10'
                            : 'border-slate-200 dark:border-slate-800 hover:bg-slate-100/50 dark:hover:bg-slate-800/30'
                        }`}>
                          <input 
                            type="radio" 
                            name="syncMode" 
                            value="replace"
                            checked={syncMode === 'replace'}
                            onChange={() => {
                              setSyncMode('replace');
                              setShowConfirmError(false);
                            }}
                            className="mt-1" 
                          />
                          <div>
                            <span className="font-bold text-slate-900 dark:text-slate-200">Barcha darslarni almashtirish (Replace)</span>
                            <p className="text-[10px] text-slate-500 dark:text-slate-400 mt-0.5">Mavjud reja to'liq o'chirilib, lessons.json faqat Notion dan olingan yangi darslar bilan to'ldiriladi.</p>
                          </div>
                        </label>

                      </div>

                      {/* Overwrite Text verification form */}
                      {syncMode === 'replace' && (
                        <div className="pt-2 border-t border-slate-250 dark:border-slate-800/60 space-y-2">
                          <label className="block text-[11px] text-amber-700 dark:text-amber-400 font-bold">
                            Mavjud darslarni to‘liq o‘chirish uchun quyidagi maydonga "ROZIMAN" so‘zini kiriting:
                          </label>
                          <input 
                            type="text" 
                            value={confirmInput}
                            onChange={(e) => {
                              setConfirmInput(e.target.value);
                              setShowConfirmError(false);
                            }}
                            placeholder="ROZIMAN" 
                            className="px-3 py-1.5 w-full md:w-60 bg-slate-100 dark:bg-slate-800 border border-slate-200 dark:border-slate-700 rounded-lg text-slate-800 dark:text-slate-200 font-bold focus:outline-none focus:ring-1 focus:ring-amber-500"
                          />
                          {showConfirmError && (
                            <p className="text-[10px] text-rose-600 dark:text-rose-450 font-semibold animate-pulse">
                              Tasdiqlash so'zi noto'g'ri. Iltimos "ROZIMAN" deb yozing.
                            </p>
                          )}
                        </div>
                      )}
                    </div>

                    {/* Preview Table */}
                    <div className="border border-slate-200 dark:border-slate-800 rounded-xl overflow-hidden">
                      <div className="max-h-60 overflow-y-auto">
                        <table className="w-full text-[11px]">
                          <thead className="bg-slate-50 dark:bg-slate-800/50 text-slate-700 dark:text-slate-300 border-b border-slate-200 dark:border-slate-800 sticky top-0">
                            <tr>
                              <th className="py-2 px-3 text-left font-bold w-16">Dars #</th>
                              <th className="py-2 px-3 text-left font-bold">Notion Sarlavha (Mavzu)</th>
                              <th className="py-2 px-3 text-left font-bold w-24">Sana</th>
                              <th className="py-2 px-3 text-left font-bold">Konspekt (Nazariya)</th>
                              <th className="py-2 px-3 text-left font-bold w-20">Holati</th>
                            </tr>
                          </thead>
                          <tbody className="divide-y divide-slate-100 dark:divide-slate-800/50 text-slate-600 dark:text-slate-300 bg-white dark:bg-slate-900">
                            {previewData.lessons.map((l, i) => (
                              <tr key={i} className="hover:bg-slate-50/50 dark:hover:bg-slate-800/20">
                                <td className="py-2 px-3 font-semibold text-slate-900 dark:text-white">#{l.lessonNumber}</td>
                                <td className="py-2 px-3 font-medium text-slate-800 dark:text-slate-200">{l.title}</td>
                                <td className="py-2 px-3 text-slate-500 dark:text-slate-400">{l.date || <span className="text-slate-400 italic">bo'sh</span>}</td>
                                <td className="py-2 px-3 truncate max-w-xs text-slate-500 dark:text-slate-400" title={l.description}>{l.description || '-'}</td>
                                <td className="py-2 px-3">
                                  <span className={`px-2 py-0.5 rounded text-[10px] font-bold ${
                                    l.status === 'completed'
                                      ? 'bg-emerald-50 dark:bg-emerald-950/30 text-emerald-600 dark:text-emerald-400'
                                      : l.status === 'pending'
                                      ? 'bg-amber-50 dark:bg-amber-950/30 text-amber-600 dark:text-amber-400'
                                      : 'bg-slate-100 dark:bg-slate-800 text-slate-500 dark:text-slate-400'
                                  }`}>
                                    {l.status === 'completed' ? 'O\'tildi' : l.status === 'pending' ? 'Navbatda' : 'Reja'}
                                  </span>
                                </td>
                              </tr>
                            ))}
                          </tbody>
                        </table>
                      </div>
                    </div>
                  </>
                )
              )}
            </div>
          )}

          {step === 'syncing' && (
            <div className="flex flex-col items-center justify-center py-12 text-slate-500">
              <Loader2 className="w-10 h-10 text-blue-600 animate-spin mb-3" />
              <span className="font-semibold text-slate-750 dark:text-slate-350 text-sm">Notion ma'lumotlari bazaga saqlanmoqda...</span>
              <p className="text-[10px] text-slate-400 mt-1">Dars rejasi backup qilinib, lessons.json fayliga yozilmoqda</p>
            </div>
          )}

          {step === 'success' && (
            <div className="flex flex-col items-center justify-center py-8 text-center space-y-3">
              <div className="w-14 h-14 rounded-full bg-emerald-100 dark:bg-emerald-950/30 flex items-center justify-center text-emerald-600 dark:text-emerald-400">
                <CheckCircle2 className="w-8 h-8 animate-bounce" />
              </div>
              <div>
                <h3 className="text-sm font-bold text-slate-900 dark:text-white">Sinxronlash Muvaffaqiyatli Yakunlandi!</h3>
                <p className="text-[11px] text-slate-500 dark:text-slate-400 mt-1">
                  Barcha dars rejalar va materiallar Notion tizimidan muvaffaqiyatli olib kelindi va lessons.json bazasiga yozildi.
                </p>
              </div>
            </div>
          )}

        </div>

        {/* Footer actions */}
        <div className="px-6 py-4 border-t border-slate-200 dark:border-slate-800 flex items-center justify-end bg-slate-50/50 dark:bg-slate-900/50">
          {step === 'preview' && (
            <div className="flex gap-3">
              <button
                type="button"
                onClick={onClose}
                className="px-4 py-2 border border-slate-200 dark:border-slate-800 rounded-xl hover:bg-slate-100 dark:hover:bg-slate-800 text-slate-700 dark:text-slate-300 font-bold transition-all cursor-pointer"
              >
                Bekor qilish
              </button>
              {previewData && (
                <button
                  type="button"
                  onClick={handleStartSync}
                  className={`px-5 py-2 font-bold rounded-xl shadow-md transition-all cursor-pointer text-white ${
                    syncMode === 'replace'
                      ? 'bg-amber-600 hover:bg-amber-700 shadow-amber-500/10'
                      : 'bg-blue-600 hover:bg-blue-700 shadow-blue-500/10'
                  }`}
                >
                  Sinxronlashni boshlash
                </button>
              )}
            </div>
          )}

          {step === 'success' && (
            <button
              type="button"
              onClick={handleFinalize}
              className="px-5 py-2 bg-blue-600 hover:bg-blue-700 text-white font-bold rounded-xl shadow-md shadow-blue-500/10 transition-all cursor-pointer"
            >
              Dashboardga qaytish
            </button>
          )}

          {step === 'loading' && (
            <button
              type="button"
              onClick={onClose}
              className="px-5 py-2 bg-slate-100 hover:bg-slate-250 dark:bg-slate-800 dark:hover:bg-slate-750 text-slate-700 dark:text-slate-200 font-bold rounded-xl transition-all cursor-pointer"
            >
              Yopish
            </button>
          )}
        </div>

      </div>
    </div>
  );
};
