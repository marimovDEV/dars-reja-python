import React from 'react';
import { Info, AlertTriangle, AlertCircle, Lightbulb, Sparkles, CheckSquare } from 'lucide-react';

export type CalloutType = 'info' | 'warning' | 'error' | 'tip' | 'practice' | 'homework';

interface DocCalloutProps {
  type?: CalloutType;
  title?: string;
  children: React.ReactNode;
}

export const DocCallout: React.FC<DocCalloutProps> = ({
  type = 'info',
  title,
  children,
}) => {
  const configs = {
    info: {
      border: 'border-l-4 border-l-blue-500 border-slate-200 dark:border-slate-800 bg-blue-50/50 dark:bg-blue-950/20 text-blue-950 dark:text-blue-200',
      icon: Info,
      iconColor: 'text-blue-500',
      defaultTitle: 'MUHIM ESLATMA'
    },
    warning: {
      border: 'border-l-4 border-l-amber-500 border-slate-200 dark:border-slate-800 bg-amber-50/50 dark:bg-amber-950/20 text-amber-950 dark:text-amber-200',
      icon: AlertTriangle,
      iconColor: 'text-amber-500',
      defaultTitle: 'OGOHLANTIRISH'
    },
    error: {
      border: 'border-l-4 border-l-rose-500 border-slate-200 dark:border-slate-800 bg-rose-50/50 dark:bg-rose-950/20 text-rose-950 dark:text-rose-200',
      icon: AlertCircle,
      iconColor: 'text-rose-500',
      defaultTitle: "KO'P UCHRAYDIGAN XATO"
    },
    tip: {
      border: 'border-l-4 border-l-emerald-500 border-slate-200 dark:border-slate-800 bg-emerald-50/50 dark:bg-emerald-950/20 text-emerald-950 dark:text-emerald-200',
      icon: Lightbulb,
      iconColor: 'text-emerald-500',
      defaultTitle: 'FOYDALI MASLAHAT'
    },
    practice: {
      border: 'border-l-4 border-l-purple-500 border-slate-200 dark:border-slate-800 bg-purple-50/50 dark:bg-purple-950/20 text-purple-950 dark:text-purple-200',
      icon: Sparkles,
      iconColor: 'text-purple-500',
      defaultTitle: 'AMALIY TOPSHIRIQ'
    },
    homework: {
      border: 'border-l-4 border-l-indigo-500 border-slate-200 dark:border-slate-800 bg-indigo-50/50 dark:bg-indigo-950/20 text-indigo-950 dark:text-indigo-200',
      icon: CheckSquare,
      iconColor: 'text-indigo-500',
      defaultTitle: 'UYGA VAZIFA'
    }
  };

  const cfg = configs[type] || configs.info;
  const Icon = cfg.icon;

  return (
    <div className={`my-5 p-4 rounded-xl border ${cfg.border} shadow-xs space-y-1.5 transition-all`}>
      <div className="flex items-center gap-2 font-bold text-xs uppercase tracking-wider">
        <Icon className={`w-4 h-4 ${cfg.iconColor} shrink-0`} />
        <span>{title || cfg.defaultTitle}</span>
      </div>
      <div className="text-sm leading-relaxed font-sans font-normal opacity-90 pl-6">
        {children}
      </div>
    </div>
  );
};
