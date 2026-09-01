/**
 * API and Socket.IO configuration helper for Vercel + AHost deployment.
 * Supports VITE_API_URL and VITE_SOCKET_URL environment variables on Vercel,
 * while seamlessly falling back to local dev ports (5005 & 5006).
 */

export const getSocketUrl = (): string => {
  if (import.meta.env.VITE_SOCKET_URL) {
    return import.meta.env.VITE_SOCKET_URL;
  }
  if (typeof window !== 'undefined' && window.location.port === '3005') {
    return `http://${window.location.hostname}:5006`;
  }
  return typeof window !== 'undefined' ? window.location.origin : '';
};

export const getApiUrl = (path: string): string => {
  const baseUrl = import.meta.env.VITE_API_URL || '';
  const cleanPath = path.startsWith('/') ? path : `/${path}`;
  return `${baseUrl}${cleanPath}`;
};
