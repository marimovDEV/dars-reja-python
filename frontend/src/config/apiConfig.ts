/**
 * API and Socket.IO configuration helper for Vercel + AHost deployment.
 * Supports VITE_API_BASE_URL, VITE_SOCKET_URL, and defaults to 'https://api.marimovdev.uz'.
 */

export const getSocketUrl = (): string => {
  if (import.meta.env.VITE_SOCKET_URL) {
    return import.meta.env.VITE_SOCKET_URL;
  }
  if (import.meta.env.VITE_API_BASE_URL) {
    return import.meta.env.VITE_API_BASE_URL;
  }
  if (import.meta.env.VITE_API_URL) {
    return import.meta.env.VITE_API_URL;
  }
  if (typeof window !== 'undefined' && window.location.port === '3005') {
    return `http://${window.location.hostname}:5006`;
  }
  // Production default for Vercel
  if (typeof window !== 'undefined' && window.location.hostname !== 'localhost' && window.location.hostname !== '127.0.0.1') {
    return 'https://api.marimovdev.uz';
  }
  return typeof window !== 'undefined' ? window.location.origin : '';
};

export const getApiUrl = (path: string): string => {
  const baseUrl = import.meta.env.VITE_API_BASE_URL || import.meta.env.VITE_API_URL || (
    typeof window !== 'undefined' && window.location.hostname !== 'localhost' && window.location.hostname !== '127.0.0.1'
      ? 'https://api.marimovdev.uz'
      : ''
  );
  const cleanPath = path.startsWith('/') ? path : `/${path}`;
  return `${baseUrl}${cleanPath}`;
};

// Global Fetch Interceptor to ensure all relative /api requests route to AHost in production
if (typeof window !== 'undefined') {
  const originalFetch = window.fetch;
  window.fetch = function (input: RequestInfo | URL, init?: RequestInit) {
    if (typeof input === 'string' && input.startsWith('/api')) {
      input = getApiUrl(input);
    }
    return originalFetch.call(this, input, init);
  };
}
