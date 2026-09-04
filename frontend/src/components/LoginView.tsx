import React, { useState } from 'react';
import { BookOpen, Lock, User, AlertCircle, Loader2 } from 'lucide-react';

interface LoginViewProps {
  onLogin: (role?: 'admin' | 'student', groupData?: any) => void;
}

export const LoginView: React.FC<LoginViewProps> = ({ onLogin }) => {
  const [loginType, setLoginType] = useState<'admin' | 'student'>('student');
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    setError('');
    
    if (!username.trim() || !password.trim()) {
      setError('Iltimos, barcha maydonlarni to‘ldiring.');
      return;
    }

    setLoading(true);

    fetch('/api/auth/login', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ username: username.trim(), password: password.trim() })
    })
      .then(async (res) => {
        if (!res.ok) {
          const errData = await res.json().catch(() => ({}));
          throw new Error(errData.error || 'Login yoki parol noto‘g‘ri.');
        }
        return res.json();
      })
      .then((data) => {
        localStorage.setItem('dars_rejasi_logged_in', 'true');
        localStorage.setItem('dars_rejasi_user_role', data.role);

        if (data.role === 'student' && data.group) {
          localStorage.setItem('dars_rejasi_active_group_id', data.group.id);
          localStorage.setItem('dars_rejasi_group_name', data.group.name);
        }
        onLogin(data.role, data.group);
      })
      .catch((err) => {
        // Fallback for offline admin
        if (username.trim() === 'ogabek' && password === 'marimov') {
          localStorage.setItem('dars_rejasi_logged_in', 'true');
          localStorage.setItem('dars_rejasi_user_role', 'admin');
          onLogin('admin');
        } else {
          setError(err.message || 'Login yoki parol noto‘g‘ri.');
          setLoading(false);
        }
      });
  };

  return (
    <div className="min-h-screen w-full flex items-center justify-center bg-slate-50 dark:bg-slate-950 p-4 font-sans transition-colors duration-200">
      <div className="w-full max-w-md bg-white dark:bg-slate-900 rounded-3xl shadow-2xl border border-slate-200 dark:border-slate-800 overflow-hidden p-8 text-xs text-left animate-fadeIn">
        
        {/* Header Logo */}
        <div className="flex flex-col items-center mb-6 text-center">
          <div className="w-14 h-14 rounded-2xl bg-gradient-to-r from-blue-600 to-indigo-600 flex items-center justify-center text-white shadow-lg shadow-blue-500/20 mb-3 animate-float">
            <BookOpen className="w-7 h-7" />
          </div>
          <h1 className="text-xl font-extrabold text-slate-900 dark:text-white tracking-tight">marimovdev — Dars Reja</h1>
          <p className="text-xs text-slate-500 dark:text-slate-400 mt-1">
            Guruhlar va O'quvchilar Darslik Portali
          </p>
        </div>

        {/* Dual Login Mode Tabs */}
        <div className="grid grid-cols-2 gap-1.5 p-1 bg-slate-100 dark:bg-slate-800/80 rounded-2xl mb-6">
          <button
            type="button"
            onClick={() => { setLoginType('student'); setError(''); }}
            className={`py-2 px-3 rounded-xl font-bold text-xs transition-all ${
              loginType === 'student'
                ? 'bg-blue-600 text-white shadow-md'
                : 'text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-white'
            }`}
          >
            🎓 O'quvchi (Guruh) Kirishi
          </button>
          <button
            type="button"
            onClick={() => { setLoginType('admin'); setError(''); }}
            className={`py-2 px-3 rounded-xl font-bold text-xs transition-all ${
              loginType === 'admin'
                ? 'bg-blue-600 text-white shadow-md'
                : 'text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-white'
            }`}
          >
            👨‍🏫 O'qituvchi (Admin)
          </button>
        </div>

        {error && (
          <div className="mb-4 p-3 rounded-xl bg-rose-50 dark:bg-rose-950/30 border border-rose-200 dark:border-rose-900/40 text-rose-600 dark:text-rose-400 flex items-center gap-2">
            <AlertCircle className="w-4 h-4 shrink-0" />
            <span className="font-semibold">{error}</span>
          </div>
        )}

        <form onSubmit={handleSubmit} className="space-y-4">
          <div>
            <label className="block font-bold text-slate-700 dark:text-slate-300 mb-1">
              {loginType === 'student' ? 'Guruh Logini (masalan: FN1):' : 'O\'qituvchi Logini:'}
            </label>
            <div className="relative">
              <User className="w-4 h-4 absolute left-3.5 top-1/2 -translate-y-1/2 text-slate-400" />
              <input
                type="text"
                placeholder={loginType === 'student' ? 'Guruh nomini kiriting' : 'ogabek'}
                value={username}
                onChange={(e) => setUsername(e.target.value)}
                className="w-full pl-10 pr-4 py-3 bg-slate-50 dark:bg-slate-800 border border-slate-200 dark:border-slate-700 rounded-xl text-slate-800 dark:text-slate-200 font-medium focus:outline-none focus:ring-2 focus:ring-blue-500 transition-all placeholder-slate-400"
                required
              />
            </div>
          </div>

          <div>
            <label className="block font-bold text-slate-700 dark:text-slate-300 mb-1">
              Maxfiy parol:
            </label>
            <div className="relative">
              <Lock className="w-4 h-4 absolute left-3.5 top-1/2 -translate-y-1/2 text-slate-400" />
              <input
                type="password"
                placeholder={loginType === 'student' ? 'Guruh parolini kiriting' : 'marimov'}
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                className="w-full pl-10 pr-4 py-3 bg-slate-50 dark:bg-slate-800 border border-slate-200 dark:border-slate-700 rounded-xl text-slate-800 dark:text-slate-200 font-medium focus:outline-none focus:ring-2 focus:ring-blue-500 transition-all placeholder-slate-400"
                required
              />
            </div>
          </div>

          <button
            type="submit"
            disabled={loading}
            className="w-full py-3.5 bg-gradient-to-r from-blue-600 to-indigo-600 hover:from-blue-700 hover:to-indigo-700 disabled:opacity-70 text-white font-extrabold rounded-xl shadow-lg transition-all text-xs cursor-pointer mt-6 btn-3d flex items-center justify-center gap-2"
          >
            {loading ? (
              <>
                <Loader2 className="w-4 h-4 animate-spin" />
                <span>Tekshirilmoqda...</span>
              </>
            ) : (
              <span>Tizimga Kirish</span>
            )}
          </button>
        </form>

        <div className="mt-8 pt-4 border-t border-slate-100 dark:border-slate-800/80 text-center text-[11px] text-slate-400 dark:text-slate-500 font-medium">
          🔒 O'quvchilar faqat o'z guruhida <span className="text-emerald-500 font-bold">✅ O'tildi</span> deb belgilangan darslarni o'qishlari mumkin.
        </div>

      </div>
    </div>
  );
};
