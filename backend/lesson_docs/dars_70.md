# 🌐 70. Server Sozlash (Nginx, Gunicorn, VPS) — Dars dokumentatsiyasi

Loyiha tayyor bo'lgach, uni butun dunyo foydalanishi uchun bulutli serverga (**VPS - Virtual Private Server**, masalan: DigitalOcean, AWS, Hetzner) joylashtirish (**Deployment**) kerak.

Production arxitekturasi:
1. **Nginx**: Reverse Proxy web-server (Statik fayllar va SSL sertifikat uchun).
2. **Gunicorn**: WSGI HTTP Server (Python/Django ilovasini runs qiladi).
3. **Systemd**: Gunicorn dasturini fonda uzluksiz ushlab turuvchi Linux servisi.

---

# Production Arxitekturasi

```
Client (Brauzer) ---> Nginx (Port 80/443) ---> Gunicorn (WSGI) ---> Django App
```

**Nginx Config Misoli:**
```nginx
server {
    listen 80;
    server_name mydomain.com;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
    }

    location /static/ {
        alias /var/www/myproject/static/;
    }
}
```

---

# 10. Qisqa xulosa

Bu darsda Linux VPS serverini sozlash, Nginx va Gunicorn bilan Django loyihasini Production ga chiqarish o'rganildi.
