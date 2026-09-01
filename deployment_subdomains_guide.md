# Subdomenlar va Serverni Sozlash Bo'yicha Aniq Qo'llanma (`marimovdev.uz`)

Ushbu hujjat siz sotib olgan **`marimovdev.uz`** domenini 3 ta alohida ilovaga (subdomenlar) to'g'ri taqsimlash va Linux serverda (Nginx / SSL / Certbot) ulash bo'yicha to'liq bosqichma-bosqich yo'riqnomadir.

---

## 🌐 Subdomenlar Tuzilmasi

| Domen / Subdomen | Vazifasi va Kontenti | Port / Backend Service |
| :--- | :--- | :--- |
| **`python.marimovdev.uz`** | **Dars Reja & Guruhlar Boshqaruvi** (Python Backend kursi, Notion sync, 72-darslik va guruhlar) | Vite Frontend (Port 3005) + Django REST API (Port 5005) |
| **`game.marimovdev.uz`** | **AI Quiz Arena (Alohida Standalone Dastur)** (Kahoot-uslubidagi jonli o'quvchi va o'qituvchi arena portali) | Vite Standalone Portal (Port 3005) + Socket.IO Engine (Port 5006) |
| **`marimovdev.uz`** | **Shaxsiy Portfoliogiz** (Sizning shaxsiy portfoliolingiz va loyihalaringiz taqdimoti) | Portfoliolingiz statik serveri yoki alohida porti |

---

## 🛠 1. DNS Sozlamalari (Domen Provayder Panelingizda)

Domen sotib olgan panellingizda (masalan, UzCloud, Webname, Cloudflare yoki Namecheap) quyidagi **A record** larni serveringizning umumiy IP manziliga yo'naltiring:

```text
Type   Name       Value (Server IP)     TTL
A      @          194.xxx.xxx.xxx       Automatic
A      python     194.xxx.xxx.xxx       Automatic
A      game       194.xxx.xxx.xxx       Automatic
```

---

## 📄 2. Nginx Konfiguratsiya Fayli (`/etc/nginx/sites-available/marimovdev.conf`)

Linux (Ubuntu/Debian) serveringizda Nginx sozlamalari faylini yaratasiz:

```nginx
# 1. python.marimovdev.uz — Dars Reja va Python Backend Kursi
server {
    server_name python.marimovdev.uz;

    # Frontend (Vite)
    location / {
        proxy_pass http://127.0.0.1:3005;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
        proxy_cache_bypass $http_upgrade;
    }

    # Django REST API (Backend)
    location /api/ {
        proxy_pass http://127.0.0.1:5005/api/;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}

# 2. game.marimovdev.uz — Standalone AI Quiz Arena Dasturi
server {
    server_name game.marimovdev.uz;

    # Standalone Quiz Frontend
    location / {
        proxy_pass http://127.0.0.1:3005;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
        proxy_cache_bypass $http_upgrade;
    }

    # Socket.IO Real-Time Engine
    location /socket.io/ {
        proxy_pass http://127.0.0.1:5006/socket.io/;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "Upgrade";
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
}

# 3. marimovdev.uz — Shaxsiy Portfolio Saytingiz
server {
    server_name marimovdev.uz www.marimovdev.uz;

    location / {
        # Portfoliolingiz turgan papka yoki alohida port
        root /var/www/portfolio;
        index index.html index.htm;
        try_files $uri $uri/ /index.html;
    }
}
```

---

## 🔒 3. Bepul SSL Sertifikat (HTTPS) Olish (Certbot)

Terminalda bitta buyruq bilan barcha 3 ta domen uchun SSL (HTTPS) sertifikatini faollashtirasiz:

```bash
sudo certbot --nginx -d marimovdev.uz -d www.marimovdev.uz -d python.marimovdev.uz -d game.marimovdev.uz
```

---

## 🚀 4. PM2 Orqali Fondagi Servislarni Boshqarish

Serveringiz har doim to'xtovsiz ishlashi uchun PM2 bilan servislarni ishga tushirasiz:

```bash
# 1. Django Backend serverini ishga tushirish (Port 5005)
pm2 start "python manage.py runserver 0.0.0.0:5005" --name "django-backend" --cwd "/var/www/dars-reja/backend"

# 2. Express + Socket.IO engine serverini ishga tushirish (Port 5006)
pm2 start "npx tsx server.ts" --name "socket-quiz-engine" --cwd "/var/www/dars-reja/frontend"

# 3. Vite Frontend dev/prod serverini ishga tushirish (Port 3005)
pm2 start "npm run dev -- --port 3005 --host 0.0.0.0" --name "vite-frontend" --cwd "/var/www/dars-reja/frontend"

# Sozlamalarni saqlash
pm2 save
pm2 startup
```

---

### ✨ Natijada:
1. `python.marimovdev.uz` orqali kirsangiz — **Dars reja, guruhlar va hujjatlar** tizimi ochiladi.
2. `game.marimovdev.uz` orqali kirsangiz — **AI Quiz Arena** alohida ilova sifatida avtomatik ochiladi.
3. `marimovdev.uz` orqali kirsangiz — **Shaxsiy portfolio** saytingiz ochiladi.
