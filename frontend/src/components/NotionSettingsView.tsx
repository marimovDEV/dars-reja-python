import React, { useState, useEffect } from 'react';
import { Link2, ShieldCheck, CheckCircle2, AlertTriangle, RefreshCw, Unlink, Loader2, ArrowLeft } from 'lucide-react';
import { NotionSettings } from '../notion/notionTypes';

interface NotionSettingsViewProps {
  onBack: () => void;
  onOpenSyncModal: (url: string) => void;
}

export const NotionSettingsView: React.FC<NotionSettingsViewProps> = ({ onBack, onOpenSyncModal }) => {
  const [notionUrl, setNotionUrl] = useState('');
  const [settings, setSettings] = useState<NotionSettings>({
    notionUrl: '',
    sourceType: 'none',
    sourceName: ''
  });
  
  const [loading, setLoading] = useState(true);
  const [testing, setTesting] = useState(false);
  const [disconnecting, setDisconnecting] = useState(false);
  const [testResult, setTestResult] = useState<{ success: boolean; msg: string } | null>(null);

  // Fetch status on load
  const fetchStatus = () => {
    setLoading(true);
    fetch('/api/notion/status?t=' + Date.now())
      .then(res => res.json())
      .then((data: NotionSettings) => {
        setSettings(data);
        if (data.notionUrl) {
          setNotionUrl(data.notionUrl);
        }
        setLoading(false);
      })
      .catch(err => {
        console.error(err);
        setLoading(false);
      });
  };

  useEffect(() => {
    fetchStatus();
  }, []);

  const handleTestConnection = (e: React.FormEvent) => {
    e.preventDefault();
    if (!notionUrl.trim()) return;

    setTesting(true);
    setTestResult(null);

    fetch('/api/notion/test-connection', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ notionUrl })
    })
      .then(res => {
        if (!res.ok) return res.json().then(e => { throw new Error(e.error); });
        return res.json();
      })
      .then(data => {
        setTestResult({
          success: true,
          msg: `Muvaffaqiyatli bog'landi! Manba turi: ${data.sourceType === 'database' ? 'Ma‘lumotlar bazasi' : 'Oddiy sahifa'}, Nomi: "${data.sourceName}"`
        });
        // Reload settings
        fetch('/api/notion/status?t=' + Date.now())
          .then(res => res.json())
          .then(setSettings);
      })
      .catch(err => {
        setTestResult({
          success: false,
          msg: err.message || 'Ulanishda xatolik yuz berdi. Havola va ruxsatlarni tekshiring.'
        });
      })
      .finally(() => {
        setTesting(false);
      });
  };

  const handleDisconnect = () => {
    if (!window.confirm("Haqiqatdan ham Notion ulanish sozlamalarini o‘chirmoqchimisiz? Darslar va hujjatlaringiz o'chirilmaydi.")) return;

    setDisconnecting(true);
    fetch('/api/notion/disconnect', { method: 'DELETE' })
      .then(res => res.json())
      .then(() => {
        setNotionUrl('');
        setSettings({ notionUrl: '', sourceType: 'none', sourceName: '' });
        setTestResult(null);
      })
      .catch(err => console.error(err))
      .finally(() => {
        setDisconnecting(false);
      });
  };

  if (loading) {
    return (
      <div className="flex-1 flex flex-col items-center justify-center p-12 text-slate-500">
        <Loader2 className="w-8 h-8 text-blue-600 animate-spin mb-2" />
        <span>Sozlamalar yuklanmoqda...</span>
      </div>
    );
  }

  const isConnected = settings.sourceType !== 'none';

  return (
    <div className="flex-1 overflow-y-auto p-6 md:p-8 bg-slate-50 dark:bg-slate-950 font-sans text-xs text-left max-w-4xl mx-auto w-full space-y-6">
      
      {/* Back button header */}
      <div className="flex items-center gap-3">
        <button
          onClick={onBack}
          className="p-1.5 rounded-lg bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 hover:bg-slate-100 dark:hover:bg-slate-800 text-slate-700 dark:text-slate-300 transition-colors cursor-pointer"
        >
          <ArrowLeft className="w-4 h-4" />
        </button>
        <div>
          <h2 className="text-base font-bold text-slate-900 dark:text-white">Notion Integratsiyasi Sozlamalari</h2>
          <p className="text-[10px] text-slate-500 dark:text-slate-400 mt-0.5">Dars materiallarini Notion API yordamida yuklash va yangilash</p>
        </div>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        
        {/* Main forms / Left columns */}
        <div className="md:col-span-2 space-y-6">
          
          {/* Connection URL form */}
          <div className="bg-white dark:bg-slate-900 rounded-2xl p-6 border border-slate-200 dark:border-slate-800 shadow-xs space-y-4">
            <h3 className="text-sm font-bold text-slate-900 dark:text-slate-200 flex items-center gap-1.5">
              <Link2 className="w-4 h-4 text-blue-600" />
              <span>Notion Manbasi URL Havolasi</span>
            </h3>

            <form onSubmit={handleTestConnection} className="space-y-4">
              <div>
                <label className="block text-slate-600 dark:text-slate-400 font-semibold mb-1">
                  Database yoki sahifa URL manzili:
                </label>
                <input
                  type="url"
                  placeholder="https://www.notion.so/workspace/dars-rejasi-e737d9954a7f45a198ab67d30129bc1e"
                  value={notionUrl}
                  onChange={(e) => setNotionUrl(e.target.value)}
                  className="w-full px-3 py-2 bg-slate-50 dark:bg-slate-800 border border-slate-200 dark:border-slate-700 rounded-xl text-slate-800 dark:text-slate-200 focus:outline-none focus:ring-2 focus:ring-blue-500 transition-all"
                  required
                />
              </div>

              <div className="flex gap-3">
                <button
                  type="submit"
                  disabled={testing}
                  className="px-4 py-2 bg-blue-600 hover:bg-blue-700 disabled:bg-blue-600/70 text-white font-bold rounded-xl flex items-center gap-1.5 cursor-pointer shadow-xs"
                >
                  {testing ? (
                    <>
                      <Loader2 className="w-4 h-4 animate-spin" />
                      <span>Ulanmoqda...</span>
                    </>
                  ) : (
                    <span>Ulanishni tekshirish</span>
                  )}
                </button>

                {isConnected && (
                  <button
                    type="button"
                    onClick={handleDisconnect}
                    disabled={disconnecting}
                    className="px-4 py-2 border border-rose-200 dark:border-rose-900/50 hover:bg-rose-600 hover:text-white dark:text-rose-400 dark:hover:text-white text-rose-600 rounded-xl font-bold flex items-center gap-1.5 cursor-pointer transition-colors"
                  >
                    <Unlink className="w-4 h-4" />
                    <span>Ulanishni uzish</span>
                  </button>
                )}
              </div>
            </form>

            {testResult && (
              <div className={`p-4 rounded-xl border flex items-start gap-2.5 ${
                testResult.success
                  ? 'bg-emerald-50 dark:bg-emerald-950/20 border-emerald-200 dark:border-emerald-900/40 text-emerald-700 dark:text-emerald-400'
                  : 'bg-rose-50 dark:bg-rose-950/20 border-rose-200 dark:border-rose-900/40 text-rose-600 dark:text-rose-400'
              }`}>
                {testResult.success ? <CheckCircle2 className="w-4.5 h-4.5 shrink-0 mt-0.5" /> : <AlertTriangle className="w-4.5 h-4.5 shrink-0 mt-0.5" />}
                <span>{testResult.msg}</span>
              </div>
            )}
          </div>

          {/* Security alert card */}
          <div className="bg-blue-50/30 dark:bg-blue-950/10 rounded-2xl p-6 border border-blue-100 dark:border-blue-900/30 flex gap-4">
            <ShieldCheck className="w-8 h-8 text-blue-600 dark:text-blue-400 shrink-0" />
            <div className="space-y-1 text-slate-700 dark:text-slate-350">
              <span className="font-bold text-slate-900 dark:text-white">Havfsizlik kafolati (Security)</span>
              <p className="leading-relaxed">
                Notion Integration API tokeni xavfsizlik nuqtai nazaridan faqat serverning maxfiy `.env` faylida saqlanadi. 
                Brauzer kodingizda yoki tashqi tarmoqda ushbu token hech qachon oshkor qilinmaydi.
              </p>
            </div>
          </div>

        </div>

        {/* Status card / Right columns */}
        <div className="space-y-6">
          
          {/* Status Display Card */}
          <div className="bg-white dark:bg-slate-900 rounded-2xl p-6 border border-slate-200 dark:border-slate-800 shadow-xs space-y-4">
            <h3 className="text-sm font-bold text-slate-900 dark:text-slate-200">Ulanish Holati:</h3>

            {isConnected ? (
              <div className="space-y-4">
                <div className="flex items-center gap-2 font-bold text-emerald-600 dark:text-emerald-400">
                  <CheckCircle2 className="w-5 h-5 shrink-0" />
                  <span>Notion faol ulangan</span>
                </div>

                <div className="border-t border-slate-100 dark:border-slate-800 pt-3 space-y-2 text-slate-600 dark:text-slate-400">
                  <div>
                    <span className="text-[10px] text-slate-400">Ulangan sahifa nomi:</span>
                    <p className="font-bold text-slate-800 dark:text-slate-250 truncate mt-0.5">{settings.sourceName}</p>
                  </div>
                  <div>
                    <span className="text-[10px] text-slate-400">Manba turi:</span>
                    <p className="font-semibold text-slate-750 dark:text-slate-300 mt-0.5">
                      {settings.sourceType === 'database' ? 'Ma‘lumotlar bazasi (Database)' : 'Oddiy sahifa (Page Blocks)'}
                    </p>
                  </div>
                  {settings.lastSyncTime && (
                    <>
                      <div>
                        <span className="text-[10px] text-slate-400">Oxirgi sinxronlash:</span>
                        <p className="font-semibold text-slate-700 dark:text-slate-300 mt-0.5">{settings.lastSyncTime}</p>
                      </div>
                      <div className="grid grid-cols-2 gap-2 pt-1">
                        <div className="p-2 bg-slate-50 dark:bg-slate-800/40 rounded-lg text-center">
                          <span className="text-[10px] text-slate-400">Darslar</span>
                          <p className="text-sm font-bold text-slate-900 dark:text-white mt-0.5">{settings.lessonsSynced || 0}</p>
                        </div>
                        <div className="p-2 bg-slate-50 dark:bg-slate-800/40 rounded-lg text-center">
                          <span className="text-[10px] text-slate-400">Hujjatlar</span>
                          <p className="text-sm font-bold text-slate-900 dark:text-white mt-0.5">{settings.documentsSynced || 0}</p>
                        </div>
                      </div>
                    </>
                  )}
                </div>

                <button
                  type="button"
                  onClick={() => onOpenSyncModal(settings.notionUrl)}
                  className="w-full py-2.5 bg-blue-600 hover:bg-blue-700 text-white font-bold rounded-xl flex items-center justify-center gap-1.5 shadow-md shadow-blue-500/10 cursor-pointer"
                >
                  <RefreshCw className="w-4 h-4" />
                  <span>Notion'dan yangilash</span>
                </button>
              </div>
            ) : (
              <div className="space-y-4">
                <div className="flex items-center gap-2 font-bold text-rose-600 dark:text-rose-400">
                  <AlertTriangle className="w-5 h-5 shrink-0" />
                  <span>Notion ulanmagan</span>
                </div>
                <p className="text-slate-500 dark:text-slate-400 leading-normal">
                  Sinxronlashni boshlash uchun chap tomondagi maydonga Notion sahifa yoki database URL havolasini kiritib, ulanish tugmasini bosing.
                </p>
              </div>
            )}
          </div>

        </div>

      </div>

    </div>
  );
};
