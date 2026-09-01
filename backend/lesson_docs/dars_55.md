# 🔑 55. User Authentication (Session vs Token) — Dars dokumentatsiyasi

**Authentication (Autentifikatsiya)** — bu so'rov yuborgan foydalanuvchining shaxsini (kimligini) aniqlash jarayoni.

Veb-ishda ikkita asosiy autentifikatsiya usuli ishlatiladi:
1. **Session-Based Auth**: Odatda monolit veb-saytlar (HTML/Cookies) uchun.
2. **Token-Based Auth**: REST API va Mobil ilovalar uchun. Har bir so'rov bilan birga maxsus **Token** uzatiladi.

---

# Token Authentication Misoli

```python
# settings.py
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ]
}

# Terminalda token generator app qo'shish:
# INSTALLED_APPS = [..., 'rest_framework.authtoken']
```

---

# 10. Qisqa xulosa

Bu darsda Autentifikatsiya turlari (Session va Token Auth) o'rganildi.
