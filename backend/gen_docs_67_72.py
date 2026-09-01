#!/usr/bin/env python3
"""Generate lesson docs 67-72 (DevOps, Docker, Deployment & Final Exam)."""
import os

DOCS_DIR = os.path.join(os.path.dirname(__file__), "lesson_docs")

lessons = {}

# 67-DARS
lessons[67] = """# 🐳 67. Docker va Docker Compose Kirish — Dars dokumentatsiyasi

"Mening kompyuterimda ishlayotgandi, lekin serverda ishlamadi" degan muammo dasturchilar orasida eng ko'p uchraydi.

**Docker** — bu ilovalarni ularning barcha bog'liqliklari (Python versiyasi, kutubxonalar, OS sozlamalari) bilan birga izolyatsiyalangan **Konteynerlar (Containers)** ichida qadoqlash va istalgan serverda bir xil barqarorlikda ishga tushirish texnologiyasidir (Konteynerlashtirish).

**Docker Compose** — bu bir nechta konteynerlarni (masalan: Django Web + PostgreSQL Baza + Redis Kesh + Celery Worker) bitta fayl orqali birgalikda boshqarish vositasidir.

---

# Kod misoli — Dockerfile va docker-compose.yml

```dockerfile
# Dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
```

```yaml
# docker-compose.yml
version: '3.8'
services:
  web:
    build: .
    ports:
      - "8000:8000"
    volumes:
      - .:/app
```

---

# 10. Qisqa xulosa

Bu darsda Docker konteynerlashtirish, Images, Containers va Docker Compose asoslari o'rganildi.
"""

# 68-DARS
lessons[68] = """# 🐳 68. Django Loyihasini Dockerlashtirish — Dars dokumentatsiyasi

Ushbu darsda haqiqiy Django loyihasini Docker va Docker Compose yordamida to'liq konteynerlashtiramiz. Loyiha tarkibida Django Web ilovasi, PostgreSQL bazasi, Redis kesh serveri hamda Celery asinxron ishchisi bo'ladi.

---

# Kod misoli — Multi-container Docker Compose

```yaml
version: '3.8'

services:
  db:
    image: postgres:15
    environment:
      POSTGRES_DB: mydb
      POSTGRES_USER: myuser
      POSTGRES_PASSWORD: mypassword

  redis:
    image: redis:7-alpine

  web:
    build: .
    command: python manage.py runserver 0.0.0.0:8000
    volumes:
      - .:/app
    ports:
      - "8000:8000"
    depends_on:
      - db
      - redis
```

---

# 10. Qisqa xulosa

Bu darsda Django + Postgres + Redis ilovalarini Docker Compose bilan konteynerlashtirish o'rganildi.
"""

# 69-DARS
lessons[69] = """# 🔄 69. CI/CD Asoslari (GitHub Actions) — Dars dokumentatsiyasi

**CI/CD (Continuous Integration / Continuous Deployment)** — bu koddagi har bir yangi o'zgarish va commit bajarilganda, avtomatik ravishda testlarni o'tkazish (CI) hamda kodni production serverga muvaffaqiyatli joylashtirish (CD) jarayonidir.

**GitHub Actions** — bu GitHub repozitoriysi ichida avtomatik pipeline va workflow larni (test, build, deploy) ishga tushiruvchi ommabop vositadir.

---

# Kod misoli — `.github/workflows/main.yml`

```yaml
name: Django CI/CD Pipeline

on:
  push:
    branches: [ "main" ]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      - name: Install Dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt
      - name: Run Tests
        run: |
          pytest
```

---

# 10. Qisqa xulosa

Bu darsda CI/CD tamoyili va GitHub Actions bilan avtomatik testlash o'rganildi.
"""

# 70-DARS
lessons[70] = """# 🌐 70. Server Sozlash (Nginx, Gunicorn, VPS) — Dars dokumentatsiyasi

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
"""

# 71-DARS
lessons[71] = """# 👨‍💻 71. Yakuniy Loyiha Taqdimoti va Code Review — Dars dokumentatsiyasi

Ushbu darsda o'quvchilar kurs davomida olgan barcha bilimlarini (Python, OOP, SQL/PostgreSQL, Django, DRF, JWT, Docker, CI/CD) birlashtirgan holda yaratgan **Yakuniy Real Backend Loyihasi (Portfolio Project)** ni taqdim etishadi.

Shuningdek, kod tozaligi (**Clean Code**), arxitektura to'g'riligi va xavfsizlik bo'yicha **Code Review (Kod Sharhi)** o'tkaziladi.

---

# Code Review Mezonlari

1. **Kod Tozaligi (Clean Code)**: PEP8 standartlari, tushunarli o'zgaruvchi va funksiya nomlari.
2. **Xavfsizlik (Security)**: Parollar, tokenlar va maxfiy kalitlar `.env` faylida berkitilganligi.
3. **Arxitektura va Testlar**: Modullik, API testlar mavjudligi va Docker sozlamalari.

---

# 10. Qisqa xulosa

Bu darsda loyihalar taqdimoti va professional Code Review jarayoni o'tkazildi.
"""

# 72-DARS
lessons[72] = """# 🏆 72. Boshidan Oxirigacha Yakuniy Imtihon — Dars dokumentatsiyasi

Ushbu yakuniy imtihon 1-darsdan 71-darsgacha o'tilgan barcha 6 ta modul bilimlari bo'yicha to'liq sintetik sinovdir.

---

# Imtihon Qismlari

1. **Nazariy va Savol-Javob (30 Ball)**: Python, OOP, SQL, Django, REST API, Docker, CI/CD bo'yicha 15 ta chuqurlashtirilgan savol.
2. **Amaliy Topshiriq (50 Ball)**: E-Commerce REST API loyihasini 3 soat ichida noldan yozish (Auth, Models, CRUD, Docker, Swagger).
3. **Loyiha Himoyasi (20 Ball)**: Yozilgan koddagi arxitektura va mantiqiy savollarga javob berish.

---

# 10. Qisqa xulosa

Tabriklaymiz! Siz ushbu imtihon bilan Python Backend Developer kursini muvaffaqiyatli yakunladingiz!
"""

for num, content in lessons.items():
    filepath = os.path.join(DOCS_DIR, f"dars_{num:02d}.md")
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"dars_{num:02d}.md yaratildi: {len(content)} belgi")
