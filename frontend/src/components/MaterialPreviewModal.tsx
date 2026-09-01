import React, { useState } from 'react';
import { X, FileText, Download, Check, Eye } from 'lucide-react';
import { LessonMaterial } from '../types';

interface MaterialPreviewModalProps {
  material: LessonMaterial | null;
  isOpen: boolean;
  onClose: () => void;
}

export const MaterialPreviewModal: React.FC<MaterialPreviewModalProps> = ({
  material,
  isOpen,
  onClose,
}) => {
  if (!isOpen || !material) return null;

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-slate-900/70 backdrop-blur-xs overflow-y-auto">
      <div 
        id="material-preview-modal"
        className="bg-white dark:bg-slate-900 rounded-2xl shadow-2xl border border-slate-200 dark:border-slate-800 w-full max-w-2xl overflow-hidden animate-in fade-in zoom-in-95 duration-200"
      >
        <div className="px-6 py-4 border-b border-slate-100 dark:border-slate-800 flex items-center justify-between">
          <div className="flex items-center gap-3">
            <div className="w-10 h-10 rounded-lg bg-blue-50 dark:bg-blue-950 flex items-center justify-center text-blue-600 dark:text-blue-400 font-bold uppercase text-xs">
              {material.type}
            </div>
            <div>
              <h2 className="text-sm font-bold text-slate-900 dark:text-white">
                {material.name}
              </h2>
              <p className="text-xs text-slate-400">
                {material.size || '2.4 MB'} • Dars ishlanmasi materiali
              </p>
            </div>
          </div>
          <button
            onClick={onClose}
            className="w-8 h-8 rounded-lg text-slate-400 hover:text-slate-600 hover:bg-slate-100 dark:hover:bg-slate-800 flex items-center justify-center"
          >
            <X className="w-5 h-5" />
          </button>
        </div>

        {/* Mock Document Reader Area */}
        <div className="p-8 bg-slate-50 dark:bg-slate-950/60 flex flex-col items-center justify-center min-h-[260px] text-center border-b border-slate-100 dark:border-slate-800">
          <div className="w-16 h-16 rounded-2xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 flex items-center justify-center text-blue-600 shadow-sm mb-4">
            <FileText className="w-8 h-8" />
          </div>
          <h3 className="text-sm font-semibold text-slate-800 dark:text-slate-200 mb-1">
            {material.name}
          </h3>
          <p className="text-xs text-slate-500 max-w-md">
            Hujjat to'liq tekshirildi va dars talablariga mos holatda tayyorlandi. Siz uni yuklab olishingiz yoki ofis dasturlarida ochishingiz mumkin.
          </p>
        </div>

        <div className="px-6 py-4 bg-white dark:bg-slate-900 flex items-center justify-between text-xs">
          <span className="text-emerald-600 dark:text-emerald-400 flex items-center gap-1 font-medium">
            <Check className="w-4 h-4" /> Fayl foydalanishga tayyor
          </span>
          <div className="flex items-center gap-2">
            <button
              onClick={onClose}
              className="px-3.5 py-1.5 rounded-lg border border-slate-200 dark:border-slate-700 text-slate-600 hover:bg-slate-50 dark:hover:bg-slate-800 font-medium"
            >
              Yopish
            </button>
            <button
              onClick={() => {
                alert(`'${material.name}' yuklab olindi.`);
                onClose();
              }}
              className="px-3.5 py-1.5 rounded-lg bg-blue-600 hover:bg-blue-700 text-white font-semibold flex items-center gap-1.5"
            >
              <Download className="w-4 h-4" />
              Yuklab olish
            </button>
          </div>
        </div>
      </div>
    </div>
  );
};
