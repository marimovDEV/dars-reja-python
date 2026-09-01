import React, { useState, useRef } from 'react';
import { X, UploadCloud, FileText, CheckCircle2, AlertTriangle, ArrowLeft, Loader2 } from 'lucide-react';
import { Lesson } from '../types';
import { parseCSVLessons, parseMarkdownLessons } from '../utils/importParser';

interface ImportLessonsModalProps {
  isOpen: boolean;
  onClose: () => void;
  onImport: (importedLessons: Lesson[], overwrite: boolean) => void;
  currentLessonsCount: number;
}

export const ImportLessonsModal: React.FC<ImportLessonsModalProps> = ({
  isOpen,
  onClose,
  onImport,
  currentLessonsCount
}) => {
  const [activeTab, setActiveTab] = useState<'upload' | 'guide'>('upload');
  const [dragActive, setDragActive] = useState(false);
  const [file, setFile] = useState<File | null>(null);
  const [parsedLessons, setParsedLessons] = useState<Lesson[]>([]);
  const [error, setError] = useState<string>('');
  const [isParsing, setIsParsing] = useState(false);
  
  // Import Options
  const [importMode, setImportMode] = useState<'append' | 'overwrite'>('append');
  const [showConfirmOverwrite, setShowConfirmOverwrite] = useState(false);

  const fileInputRef = useRef<HTMLInputElement>(null);

  if (!isOpen) return null;

  // Handlers for drag & drop
  const handleDrag = (e: React.DragEvent) => {
    e.preventDefault();
    e.stopPropagation();
    if (e.type === "dragenter" || e.type === "dragover") {
      setDragActive(true);
    } else if (e.type === "dragleave") {
      setDragActive(false);
    }
  };

  const processFile = (selectedFile: File) => {
    setError('');
    setParsedLessons([]);
    
    const extension = selectedFile.name.split('.').pop()?.toLowerCase();
    if (extension !== 'csv' && extension !== 'md' && extension !== 'txt') {
      setError('Faqat .csv, .md yoki .txt kengaytmali fayllar qo‘llab-quvvatlanadi.');
      return;
    }

    setFile(selectedFile);
    setIsParsing(true);

    const reader = new FileReader();
    reader.onload = (e) => {
      const text = e.target?.result as string;
      try {
        let lessons: Lesson[] = [];
        if (extension === 'csv') {
          lessons = parseCSVLessons(text);
        } else {
          lessons = parseMarkdownLessons(text);
        }

        if (lessons.length === 0) {
          setError('Fayldan hech qanday dars ma‘lumotlari topilmadi. Sarlavhalarni yo‘riqnomaga muvofiq tekshiring.');
        } else {
          setParsedLessons(lessons);
        }
      } catch (err) {
        console.error(err);
        setError('Faylni tahlil qilishda (parsing) xatolik yuz berdi. Fayl formatini tekshiring.');
      } finally {
        setIsParsing(false);
      }
    };
    reader.readAsText(selectedFile);
  };

  const handleDrop = (e: React.DragEvent) => {
    e.preventDefault();
    e.stopPropagation();
    setDragActive(false);

    if (e.dataTransfer.files && e.dataTransfer.files[0]) {
      processFile(e.dataTransfer.files[0]);
    }
  };

  const handleFileInputChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    if (e.target.files && e.target.files[0]) {
      processFile(e.target.files[0]);
    }
  };

  const triggerFileInput = () => {
    fileInputRef.current?.click();
  };

  const handleReset = () => {
    setFile(null);
    setParsedLessons([]);
    setError('');
    setShowConfirmOverwrite(false);
  };

  const handleImportSubmit = () => {
    if (parsedLessons.length === 0) return;
    
    if (importMode === 'overwrite' && !showConfirmOverwrite) {
      setShowConfirmOverwrite(true);
      return;
    }

    onImport(parsedLessons, importMode === 'overwrite');
    handleReset();
    onClose();
  };

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center bg-slate-900/60 backdrop-blur-xs p-4 font-sans text-xs text-left">
      <div className="bg-white dark:bg-slate-900 w-full max-w-3xl rounded-2xl shadow-2xl border border-slate-200 dark:border-slate-800 overflow-hidden flex flex-col max-h-[90vh]">
        
        {/* Header */}
        <div className="px-6 py-4 border-b border-slate-200 dark:border-slate-800 flex items-center justify-between bg-slate-50/50 dark:bg-slate-900/50">
          <div>
            <h2 className="text-sm font-bold text-slate-950 dark:text-white">Notion dars rejasini import qilish</h2>
            <p className="text-[11px] text-slate-500 dark:text-slate-400 mt-0.5">Dars rejalarni CSV yoki Markdown fayllari orqali yuklash</p>
          </div>
          <button 
            onClick={onClose}
            className="p-1.5 rounded-lg hover:bg-slate-100 dark:hover:bg-slate-800 text-slate-500 hover:text-slate-700 dark:hover:text-slate-300 transition-colors"
          >
            <X className="w-5 h-5" />
          </button>
        </div>

        {/* Tab Buttons (only visible if not previewing parsed results) */}
        {parsedLessons.length === 0 && (
          <div className="flex border-b border-slate-200 dark:border-slate-800 px-6">
            <button
              onClick={() => setActiveTab('upload')}
              className={`py-3 px-4 font-bold border-b-2 transition-all ${
                activeTab === 'upload' 
                  ? 'border-blue-600 text-blue-600 dark:text-blue-400' 
                  : 'border-transparent text-slate-500 hover:text-slate-800 dark:hover:text-slate-200'
              }`}
            >
              Fayl yuklash
            </button>
            <button
              onClick={() => setActiveTab('guide')}
              className={`py-3 px-4 font-bold border-b-2 transition-all ${
                activeTab === 'guide' 
                  ? 'border-blue-600 text-blue-600 dark:text-blue-400' 
                  : 'border-transparent text-slate-500 hover:text-slate-800 dark:hover:text-slate-200'
              }`}
            >
              Notion qo'llanmasi
            </button>
          </div>
        )}

        {/* Content Body */}
        <div className="flex-1 overflow-y-auto p-6">
          {parsedLessons.length > 0 ? (
            /* PREVIEW PARSED LESSONS VIEW */
            <div className="space-y-6">
              <div className="p-3 bg-emerald-50 dark:bg-emerald-950/20 border border-emerald-200 dark:border-emerald-900/30 rounded-xl flex items-start gap-2.5 text-emerald-700 dark:text-emerald-400">
                <CheckCircle2 className="w-4 h-4 mt-0.5 shrink-0" />
                <div>
                  <span className="font-bold">Fayl muvaffaqiyatli o‘qildi!</span>
                  <p className="text-[11px] text-emerald-600/80 dark:text-emerald-400/80 mt-0.5">
                    Fayldan <strong>{parsedLessons.length} ta dars rejasi</strong> aniqlandi. Quyida ularning ro‘yxati berilgan:
                  </p>
                </div>
              </div>

              {/* Import Options Card */}
              <div className="p-4 bg-slate-50 dark:bg-slate-800/40 border border-slate-200 dark:border-slate-800 rounded-xl space-y-4">
                <h3 className="font-bold text-slate-900 dark:text-slate-200">Import qilish rejimi:</h3>
                <div className="grid grid-cols-1 md:grid-cols-2 gap-3">
                  <label className={`p-3 rounded-xl border flex items-start gap-2.5 cursor-pointer transition-all ${
                    importMode === 'append'
                      ? 'border-blue-500 bg-blue-50/20 dark:bg-blue-950/10'
                      : 'border-slate-200 dark:border-slate-800 hover:bg-slate-100/50 dark:hover:bg-slate-800/30'
                  }`}>
                    <input 
                      type="radio" 
                      name="importMode" 
                      value="append"
                      checked={importMode === 'append'}
                      onChange={() => setImportMode('append')}
                      className="mt-1" 
                    />
                    <div>
                      <span className="font-bold text-slate-900 dark:text-slate-200">Ro‘yxat oxiriga qo‘shish (Append)</span>
                      <p className="text-[10px] text-slate-500 dark:text-slate-400 mt-0.5">Yangi darslar mavjud darslar oxiriga ketma-ketlikda qo‘shiladi.</p>
                    </div>
                  </label>

                  <label className={`p-3 rounded-xl border flex items-start gap-2.5 cursor-pointer transition-all ${
                    importMode === 'overwrite'
                      ? 'border-amber-500 bg-amber-50/20 dark:bg-amber-950/10'
                      : 'border-slate-200 dark:border-slate-800 hover:bg-slate-100/50 dark:hover:bg-slate-800/30'
                  }`}>
                    <input 
                      type="radio" 
                      name="importMode" 
                      value="overwrite"
                      checked={importMode === 'overwrite'}
                      onChange={() => {
                        setImportMode('overwrite');
                        setShowConfirmOverwrite(false);
                      }}
                      className="mt-1" 
                    />
                    <div>
                      <span className="font-bold text-slate-900 dark:text-slate-200">Mavjud darslarni o‘chirish (Overwrite)</span>
                      <p className="text-[10px] text-slate-500 dark:text-slate-400 mt-0.5">Mavjud darslaringiz o‘chirilib, faqat yangi import qilingan darslar qoladi.</p>
                    </div>
                  </label>
                </div>

                {importMode === 'overwrite' && showConfirmOverwrite && (
                  <div className="p-3 bg-rose-50 dark:bg-rose-950/30 border border-rose-200 dark:border-rose-900/40 rounded-xl flex items-start gap-2.5 text-rose-700 dark:text-rose-400 text-[11px] animate-pulse">
                    <AlertTriangle className="w-4 h-4 mt-0.5 shrink-0" />
                    <div>
                      <span className="font-bold">Diqqat: Tasdiqlash talab etiladi!</span>
                      <p className="mt-0.5">Tizimdagi mavjud <strong>{currentLessonsCount} ta dars</strong> butunlay o'chib ketadi. Ushbu amalni tasdiqlash uchun quyidagi tugmani bosing.</p>
                    </div>
                  </div>
                )}
              </div>

              {/* Parsed List Table */}
              <div className="border border-slate-200 dark:border-slate-800 rounded-xl overflow-hidden">
                <div className="max-h-60 overflow-y-auto">
                  <table className="w-full text-[11px]">
                    <thead className="bg-slate-50 dark:bg-slate-800/50 text-slate-700 dark:text-slate-300 border-b border-slate-200 dark:border-slate-800 sticky top-0">
                      <tr>
                        <th className="py-2 px-3 text-left font-bold w-16">Dars #</th>
                        <th className="py-2 px-3 text-left font-bold">Mavzu nomi (Sarlavha)</th>
                        <th className="py-2 px-3 text-left font-bold w-24">Sana</th>
                        <th className="py-2 px-3 text-left font-bold">Tavsif (Mavzu)</th>
                      </tr>
                    </thead>
                    <tbody className="divide-y divide-slate-100 dark:divide-slate-800/50 text-slate-600 dark:text-slate-300 bg-white dark:bg-slate-900">
                      {parsedLessons.map((l, i) => (
                        <tr key={i} className="hover:bg-slate-50/50 dark:hover:bg-slate-800/20">
                          <td className="py-2 px-3 font-semibold text-slate-900 dark:text-white">#{l.lessonNumber}</td>
                          <td className="py-2 px-3 font-medium text-slate-800 dark:text-slate-200">{l.title}</td>
                          <td className="py-2 px-3 text-slate-500 dark:text-slate-400">{l.date || <span className="text-slate-400 italic">belgilanmagan</span>}</td>
                          <td className="py-2 px-3 truncate max-w-xs text-slate-500 dark:text-slate-400" title={l.description}>{l.description || '-'}</td>
                        </tr>
                      ))}
                    </tbody>
                  </table>
                </div>
              </div>
            </div>
          ) : (
            /* UPLOAD & GUIDE VIEW */
            <div>
              {activeTab === 'upload' ? (
                <div className="space-y-6">
                  {/* File Upload drag-drop area */}
                  <div
                    onDragEnter={handleDrag}
                    onDragOver={handleDrag}
                    onDragLeave={handleDrag}
                    onDrop={handleDrop}
                    onClick={triggerFileInput}
                    className={`border-2 border-dashed rounded-2xl p-10 flex flex-col items-center justify-center cursor-pointer transition-all ${
                      dragActive
                        ? 'border-blue-500 bg-blue-50/10 dark:bg-blue-950/10'
                        : 'border-slate-300 dark:border-slate-800 hover:border-slate-400 dark:hover:border-slate-700 bg-slate-50/30 dark:bg-slate-900/20'
                    }`}
                  >
                    <input
                      ref={fileInputRef}
                      type="file"
                      onChange={handleFileInputChange}
                      accept=".csv,.md,.txt"
                      className="hidden"
                    />
                    
                    {isParsing ? (
                      <div className="flex flex-col items-center py-4">
                        <Loader2 className="w-10 h-10 text-blue-600 animate-spin mb-2" />
                        <span className="font-semibold text-slate-600 dark:text-slate-300">Fayl tahlil qilinmoqda (parsing)...</span>
                      </div>
                    ) : (
                      <>
                        <UploadCloud className="w-12 h-12 text-slate-400 dark:text-slate-600 mb-3" />
                        <span className="font-bold text-slate-800 dark:text-slate-200 text-sm">Faylni sudrab tashlang yoki yuklang</span>
                        <span className="text-slate-400 dark:text-slate-500 text-[10px] mt-1">Notion'dan eksport qilingan .csv, .md yoki .txt fayllari</span>
                        <div className="flex flex-wrap gap-2.5 mt-4 justify-center">
                          <button
                            type="button"
                            className="px-4 py-1.5 bg-slate-100 hover:bg-slate-200 dark:bg-slate-800 dark:hover:bg-slate-750 text-slate-700 dark:text-slate-200 font-bold rounded-xl transition-all"
                          >
                            Faylni tanlash
                          </button>
                          <button
                            id="demo-csv-btn"
                            type="button"
                            onClick={(e) => {
                              e.stopPropagation();
                              const demoCSV = `Dars raqami,Sarlavha,Sana,Tavsif,Uyga vazifa,Holat,Vaqt\n1,Demo Dars 1 (CSV),2026-09-01,CSV orqali yuklangan demo dars,1-vazifa,completed,14:00 - 16:00\n2,Demo Dars 2 (CSV),2026-09-02 -> 2026-09-03,Sana oralig'ini test qilish,2-vazifa,pending,14:00 - 16:00\n3,Demo Dars 3 (CSV),,Sanasiz dars,3-vazifa,planned,14:00 - 16:00`;
                              setFile(new File([], "demo_lessons.csv"));
                              setParsedLessons(parseCSVLessons(demoCSV));
                            }}
                            className="px-3 py-1.5 bg-blue-50 hover:bg-blue-600 hover:text-white dark:bg-blue-950/40 text-blue-600 dark:text-blue-400 font-bold rounded-xl transition-all cursor-pointer"
                          >
                            Demo CSV
                          </button>
                          <button
                            id="demo-md-btn"
                            type="button"
                            onClick={(e) => {
                              e.stopPropagation();
                              const demoMD = `### 1-dars — Demo MD Dars 1\n**Mavzu:** Markdown orqali import qilingan dars\n**Amaliyot:** Amaliy mashg'ulot 1\n**Uyga vazifa:** MD topshiriq 1\n\n### 2-dars — Demo MD Dars 2\n**Mavzu:** Qo'shimcha dars\n**Amaliyot:** Amaliy mashg'ulot 2\n**Uyga vazifa:** MD topshiriq 2`;
                              setFile(new File([], "demo_lessons.md"));
                              setParsedLessons(parseMarkdownLessons(demoMD));
                            }}
                            className="px-3 py-1.5 bg-indigo-50 hover:bg-indigo-600 hover:text-white dark:bg-indigo-950/40 text-indigo-600 dark:text-indigo-400 font-bold rounded-xl transition-all cursor-pointer"
                          >
                            Demo MD
                          </button>
                        </div>
                      </>
                    )}
                  </div>

                  {error && (
                    <div className="p-3 rounded-xl bg-rose-50 dark:bg-rose-950/30 border border-rose-200 dark:border-rose-900/40 text-rose-600 dark:text-rose-400 flex items-center gap-2">
                      <AlertTriangle className="w-4.5 h-4.5 shrink-0" />
                      <span>{error}</span>
                    </div>
                  )}

                  <div className="text-slate-400 dark:text-slate-500 text-[10px] space-y-1 text-center">
                    <p>• CSV formatida ustunlar nomi: "Dars raqami", "Sarlavha", "Sana", "Tavsif", "Uyga vazifa" bo'lishi tavsiya etiladi.</p>
                    <p>• Markdown formatida darslar "### 1-dars — Sarlavha" ko'rinishida ajratilishi lozim.</p>
                  </div>
                </div>
              ) : (
                /* GUIDE TAB */
                <div className="space-y-5 text-slate-700 dark:text-slate-300 text-xs">
                  <div>
                    <h3 className="font-bold text-slate-950 dark:text-white mb-2 text-[13px]">1. Notion Database Ustunlari (CSV uchun)</h3>
                    <p className="mb-2">Notion'da jadval yaratishda ustun nomlari va turlarini quyidagicha belgilang:</p>
                    <div className="border border-slate-200 dark:border-slate-800 rounded-xl overflow-hidden">
                      <table className="w-full text-[10px]">
                        <thead className="bg-slate-50 dark:bg-slate-800/50 text-slate-700 dark:text-slate-300 border-b border-slate-200 dark:border-slate-800">
                          <tr>
                            <th className="py-1.5 px-3 text-left">Ustun nomi (UZ)</th>
                            <th className="py-1.5 px-3 text-left">Property Type</th>
                            <th className="py-1.5 px-3 text-left">Tushuntirish</th>
                          </tr>
                        </thead>
                        <tbody className="divide-y divide-slate-100 dark:divide-slate-800/50">
                          <tr>
                            <td className="py-1.5 px-3 font-semibold">Dars raqami</td>
                            <td className="py-1.5 px-3">Number</td>
                            <td className="py-1.5 px-3">1, 2, 3 tartib raqami</td>
                          </tr>
                          <tr>
                            <td className="py-1.5 px-3 font-semibold">Sarlavha (Nomi)</td>
                            <td className="py-1.5 px-3">Title</td>
                            <td className="py-1.5 px-3">Dars mavzusi sarlavhasi</td>
                          </tr>
                          <tr>
                            <td className="py-1.5 px-3 font-semibold">Sana</td>
                            <td className="py-1.5 px-3">Date</td>
                            <td className="py-1.5 px-3">Notion sanasi (masalan, 2026-09-01)</td>
                          </tr>
                          <tr>
                            <td className="py-1.5 px-3 font-semibold">Tavsif (Mavzu)</td>
                            <td className="py-1.5 px-3">Text</td>
                            <td className="py-1.5 px-3">Qisqa konspekt yoki mavzu tafsiloti</td>
                          </tr>
                          <tr>
                            <td className="py-1.5 px-3 font-semibold">Uyga vazifa</td>
                            <td className="py-1.5 px-3">Text</td>
                            <td className="py-1.5 px-3">Uyga topshiriq matni</td>
                          </tr>
                        </tbody>
                      </table>
                    </div>
                  </div>

                  <div>
                    <h3 className="font-bold text-slate-950 dark:text-white mb-1.5 text-[13px]">2. Notion'dan eksport qilish tartibi</h3>
                    <ol className="list-decimal list-inside space-y-1 pl-1">
                      <li>Notion Database sahifasida yuqori o'ngdagi uchta nuqta menyusini oching.</li>
                      <li><strong>Export</strong> buyrug'ini tanlang.</li>
                      <li>Formatni <strong>Markdown & CSV</strong> qilib sozlashingiz kifoya. Eksport qilingan ZIP arxivni ochib, ichidagi CSV faylini dasturga yuklang.</li>
                    </ol>
                  </div>
                </div>
              )}
            </div>
          )}
        </div>

        {/* Footer actions */}
        <div className="px-6 py-4 border-t border-slate-200 dark:border-slate-800 flex items-center justify-between bg-slate-50/50 dark:bg-slate-900/50">
          {parsedLessons.length > 0 ? (
            <>
              <button
                type="button"
                onClick={handleReset}
                className="px-4 py-2 border border-slate-200 dark:border-slate-800 rounded-xl hover:bg-slate-100 dark:hover:bg-slate-800 text-slate-700 dark:text-slate-300 font-bold transition-all flex items-center gap-1.5 cursor-pointer"
              >
                <ArrowLeft className="w-4 h-4" />
                <span>Qayta yuklash</span>
              </button>
              <button
                type="button"
                onClick={handleImportSubmit}
                className={`px-5 py-2 font-bold rounded-xl shadow-md transition-all cursor-pointer text-white ${
                  importMode === 'overwrite'
                    ? 'bg-amber-600 hover:bg-amber-700 shadow-amber-500/10'
                    : 'bg-blue-600 hover:bg-blue-700 shadow-blue-500/10'
                }`}
              >
                {importMode === 'overwrite' && showConfirmOverwrite 
                  ? 'O‘chirishni tasdiqlash va Import' 
                  : 'Import qilishni tasdiqlash'}
              </button>
            </>
          ) : (
            <>
              <span className="text-[10px] text-slate-400 dark:text-slate-500">Mavjud darslar soni: {currentLessonsCount} ta</span>
              <button
                type="button"
                onClick={onClose}
                className="px-5 py-2 bg-slate-100 hover:bg-slate-200 dark:bg-slate-800 dark:hover:bg-slate-750 text-slate-700 dark:text-slate-200 font-bold rounded-xl transition-all cursor-pointer"
              >
                Yopish
              </button>
            </>
          )}
        </div>

      </div>
    </div>
  );
};
