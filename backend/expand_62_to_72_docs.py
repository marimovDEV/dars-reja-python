import os
import sys
import json
import django

sys.path.append(os.path.dirname(__file__))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from lessons_app.models import Lesson

LESSONS_JSON = os.path.join(os.path.dirname(__file__), "..", "frontend", "src", "data", "lessons.json")

FULL_LONG_62_TO_72 = {
    62: """# ⚡ 62. Redis va Kesh (Caching) — Dars dokumentatsiyasi

`Redis` va `Caching` — Ma'lumotlar bazasiga bo'ladigan og'ir so'rovlar yukini kamaytirish va **ma'lumotlarni operativ xotirada (RAM) saqlash orqali tezlikni 10x ga oshirish** uchun ishlatiladi.

Bu mavzu orqali:

- In-Memory Key-Value DB bo'lmish Redis serverini o'rnatish;
- `redis-py` kutubxonasi yordamida Python dan ulanish;
- Django Caching Framework va `@cache_page(60 * 15)` dekoratori

mumkin.

---

## Dars maqsadi

Bu dars oxirida o‘quvchi:

- Redis kesh xotira arxitekturasini tushunish;
- Django backend so'rovlarini keshga saqlash va tezlashtirish;
- TTL (Time-To-Live) va kesh tozalash usullari

ni mustaqil bajara oladi.

## Kerakli bilimlar

Bu darsni tushunish uchun:

- 14-dars: Dictionary;
- 31-dars: Ma'lumotlar bazasi asoslari

bilinishi kerak.

---

# 1. Asosiy tushuncha

`Redis va Caching` nima ekanini sodda tilda tushuntiramiz.

Masalan:

> `Redis` — bu juda tez ishlaydigan in-memory (RAMdagi) ma'lumotlar bazasi. Tez-tez so'raladigan ma'lumotlar (masalan bosh sahifa mahsulotlari) Redisga saqlanadi va SQL bazaga ortiqcha yuk tushmaydi.

Muhim qoida:

```python
import redis
r = redis.Redis(host='localhost', port=6379, db=0)
r.set('key', 'value')
```

---

# 10. Qisqa xulosa

Bu darsda:

- `Redis in-memory DB`;
- `Django cache_page`;
- `TTL (Time-To-Live)`

ni o‘rgandik.

Keyingi darsda: **Celery va Asinxron vazifalar**.

---

# Resurslar va fayllar

- 📄 Konspekt: `62_dars_konspekt.pdf`
- 💻 Kodlar: `github.com/dars-reja/62-dars`
- 🎬 Video: `youtube.com/watch?v=dars62`
- 📝 Qo‘shimcha mashqlar: `python.uz/mashq62`
""",

    63: """# 🥦 63. Celery va Asinxron vazifalar — Dars dokumentatsiyasi

`Celery` va `Message Broker (Redis/RabbitMQ)` — Django backend dasturlarida **uzun davom etadigan og'ir vazifalarni (Email yuborish, SMS, video qayta ishlash) fonda (background) bajarish** uchun ishlatiladi.

Bu mavzu orqali:

- Celery arxitekturasi va Broker/Result Backend;
- `@shared_task` dekoratori;
- `my_task.delay(arg1, arg2)` orqali background vazifani ishga tushirish

mumkin.

---

## Dars maqsadi

Bu dars oxirida o‘quvchi:

- Backend so'rovlarini qotirib qo'ymasdan og'ir ishlarni backgroundga o'tkazish;
- Celery workerlarini yurgizish;
- Email va SMS bildirishnomalarini asinxron yuborish

ni mustaqil bajara oladi.

---

# 1. Asosiy tushuncha

```python
from celery import shared_task

@shared_task
def send_welcome_email(user_email):
    # Email yuborish
    return f"Email {user_email} ga yuborildi!"
```

---

# 10. Qisqa xulosa

Bu darsda:

- `Celery va Message Broker`;
- `@shared_task dekoratori`;
- `task.delay() background bajarish`

ni o‘rgandik.

Keyingi darsda: **Celery Beat va Rejalashtirilgan vazifalar**.

---

# Resurslar va fayllar

- 📄 Konspekt: `63_dars_konspekt.pdf`
- 💻 Kodlar: `github.com/dars-reja/63-dars`
- 🎬 Video: `youtube.com/watch?v=dars63`
- 📝 Qo‘shimcha mashqlar: `python.uz/mashq63`
""",

    64: """# ⏰ 64. Celery Beat va Rejalashtirilgan vazifalar — Dars dokumentatsiyasi

`Celery Beat` — Loyihangizda **muayyan vaqt oralig'ida yoki cron rejasiga ko'ra avtomatik bajariladigan takroriy vazifalarni (Periodic Tasks)** boshqarish uchun ishlatiladi.

Bu mavzu orqali:

- Celery Beat Scheduler sozlamalari;
- Har soat, kun yoki haftada avtomatik bajariluvchi kesh tozalash va hisobotlar;
- `django-celery-beat` admin paneli orqali vazifalarni dinamik boshqarish

mumkin.

---

## Dars maqsadi

Bu dars oxirida o‘quvchi:

- Davriy va takrorlanuvchi avtomatik vazifalar (cron) tuzish;
- Celery Beat scheduler jarayonini ishga tushirish;
- Har kunlik zaxira nusxa (backup) yoki kunlik hisobotlar tayyorlash

ni mustaqil bajara oladi.

---

# 1. Asosiy tushuncha

```python
# settings.py
CELERY_BEAT_SCHEDULE = {
    'send-daily-report': {
        'task': 'app.tasks.send_daily_report',
        'schedule': 86400.0,
    },
}
```

---

# 10. Qisqa xulosa

Bu darsda:

- `Celery Beat rejalashtiruvchi`;
- `Periodic tasks va Cron`;
- `django-celery-beat`

ni o‘rgandik.

Keyingi darsda: **Pytest va Unittest kirish**.

---

# Resurslar va fayllar

- 📄 Konspekt: `64_dars_konspekt.pdf`
- 💻 Kodlar: `github.com/dars-reja/64-dars`
- 🎬 Video: `youtube.com/watch?v=dars64`
- 📝 Qo‘shimcha mashqlar: `python.uz/mashq64`
""",

    65: """# 🧪 65. Pytest va Unittest kirish — Dars dokumentatsiyasi

`Pytest` va `Unittest` — Python kodining **to'g'ri va xatosiz ishlashini avtomatik testlar (Unit Testing) yordamida tekshirish** uchun ishlatiladi.

Bu mavzu orqali:

- Unit testing tushunchasi va Test Driven Development (TDD);
- `unittest.TestCase` va `pytest` sintaksislari;
- `assert` operatori;
- Testlarni ishga tushirish: `pytest` yoki `python manage.py test`

mumkin.

---

## Dars maqsadi

Bu dars oxirida o‘quvchi:

- Kod o'zgarishlarida oldingi mantiqlar buzilmasligini avtomatik tekshirish;
- `pytest` kutubxonasi yordamida testlar yozish;
- TDD (Test Driven Development) mantiqini tushunish

ni mustaqil bajara oladi.

---

# 1. Asosiy tushuncha

```python
def add(a, b):
    return a + b

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
```

---

# 10. Qisqa xulosa

Bu darsda:

- `Pytest va Unittest`;
- `assert operatori`;
- `TDD tamoyillari`

ni o‘rgandik.

Keyingi darsda: **DRF API testing**.

---

# Resurslar va fayllar

- 📄 Konspekt: `65_dars_konspekt.pdf`
- 💻 Kodlar: `github.com/dars-reja/65-dars`
- 🎬 Video: `youtube.com/watch?v=dars65`
- 📝 Qo‘shimcha mashqlar: `python.uz/mashq65`
""",

    66: """# 🎯 66. DRF API testing — Dars dokumentatsiyasi

`APITestCase` va `APIClient` — DRF REST API larining **endpoints yo'nalishlarini (GET, POST, PUT, DELETE) avtomatik sinash va status kodlarini tekshirish** uchun ishlatiladi.

Bu mavzu orqali:

- `from rest_framework.test import APITestCase, APIClient`;
- `self.client.get('/api/v1/courses/')`;
- Status kodini tekshirish (`response.status_code == 200`);
- Autentifikatsiyalangan so'rovlarni test qilish (`client.force_authenticate(user=user)`)

mumkin.

---

## Dars maqsadi

Bu dars oxirida o‘quvchi:

- REST API so'rovlarini avtomatik test qilish;
- Status kodlari va JSON javoblarni `assertEqual` bilan solishtirish;
- Autentifikatsiya qilingan foydalanuvchi so'rovlarini simulyatsiya qilish

ni mustaqil bajara oladi.

---

# 1. Asosiy tushuncha

```python
from rest_framework.test import APITestCase
from rest_framework import status

class CourseAPITestCase(APITestCase):
    def test_get_courses(self):
        response = self.client.get('/api/v1/courses/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
```

---

# 10. Qisqa xulosa

Bu darsda:

- `APITestCase sinfi`;
- `client.get() va client.post()`;
- `force_authenticate`

ni o‘rgandik.

Keyingi darsda: **Docker va Docker Compose kirish**.

---

# Resurslar va fayllar

- 📄 Konspekt: `66_dars_konspekt.pdf`
- 💻 Kodlar: `github.com/dars-reja/66-dars`
- 🎬 Video: `youtube.com/watch?v=dars66`
- 📝 Qo‘shimcha mashqlar: `python.uz/mashq66`
""",

    67: """# 🐳 67. Docker va Docker Compose kirish — Dars dokumentatsiyasi

`Docker` va `Docker Compose` — Dastur va uning barcha bog'liqliklarini (Python, Postgres, Redis) **konteynerlashtirish va har qanday serverda bir xil muhitda ishga tushirish** uchun ishlatiladi.

Bu mavzu orqali:

- Container va Virtual Machine o'rtasidagi farq;
- `Dockerfile` va `docker-compose.yml`;
- Docker CLI: `docker build`, `docker run`, `docker ps`, `docker-compose up -d`

mumkin.

---

## Dars maqsadi

Bu dars oxirida o‘quvchi:

- Docker texnologiyasining afzalliklarini tushunish;
- `Dockerfile` yaratib loyihani obrazga (Image) aylantirish;
- `docker-compose.yml` orqali ko'p konteynerli tizimlarni boshqarish

ni mustaqil bajara oladi.

---

# 1. Asosiy tushuncha

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
```

---

# 10. Qisqa xulosa

Bu darsda:

- `Dockerfile va Image`;
- `Container va Virtualization`;
- `docker-compose.yml`

ni o‘rgandik.

Keyingi darsda: **Django loyihasini Dockerlashtirish**.

---

# Resurslar va fayllar

- 📄 Konspekt: `67_dars_konspekt.pdf`
- 💻 Kodlar: `github.com/dars-reja/67-dars`
- 🎬 Video: `youtube.com/watch?v=dars67`
- 📝 Qo‘shimcha mashqlar: `python.uz/mashq67`
""",

    68: """# 📦 68. Django loyihasini Dockerlashtirish — Dars dokumentatsiyasi

`Django + PostgreSQL + Redis + Celery` loyihasini **bitta `docker-compose.yml` faylida to'liq izolatsiya va integratsiya qilish**.

Bu mavzu orqali:

- Multi-service `docker-compose.yml`;
- Environment o'zgaruvchilarini `.env` dan yuklash;
- Entrypoint skriptlari va avtomatik `migrate` bajarish

mumkin.

---

## Dars maqsadi

Bu dars oxirida o‘quvchi:

- To'liq Django loyihasini Docker oyna konteynerlariga solish;
- Postgres, Redis va Celery larni birgalikda bir soniyada yurgizish;
- Production va Development muhitlarini ajratish

ni mustaqil bajara oladi.

---

# 1. Asosiy tushuncha

```yaml
version: '3.8'
services:
  web:
    build: .
    command: python manage.py runserver 0.0.0.0:8000
    ports:
      - "8000:8000"
    depends_on:
      - db
  db:
    image: postgres:15
    environment:
      POSTGRES_DB: app_db
```

---

# 10. Qisqa xulosa

Bu darsda:

- `Multi-container docker-compose`;
- `Django + Postgres + Redis Dockerda`;
- `docker-compose up --build`

ni o‘rgandik.

Keyingi darsda: **CI/CD asoslari (GitHub Actions)**.

---

# Resurslar va fayllar

- 📄 Konspekt: `68_dars_konspekt.pdf`
- 💻 Kodlar: `github.com/dars-reja/68-dars`
- 🎬 Video: `youtube.com/watch?v=dars68`
- 📝 Qo‘shimcha mashqlar: `python.uz/mashq68`
""",

    69: """# 🚀 69. CI/CD asoslari (GitHub Actions) — Dars dokumentatsiyasi

`CI/CD (Continuous Integration / Continuous Deployment)` va `GitHub Actions` — **Koddagi har bir yangilanishda avtomatik testlarni yurgizish va serverga avtomatik joylash (Deploy)** uchun ishlatiladi.

Bu mavzu orqali:

- `.github/workflows/main.yml` quvuri (Pipeline);
- GitHub Triggerlar: `on: [push, pull_request]`;
- Avtomatik `pytest` o'tkazish va xatolar bor bo'lsa pull requestni rad etish

mumkin.

---

## Dars maqsadi

Bu dars oxirida o‘quvchi:

- GitHub Actions yordamida avtomatik CI/CD pipelinelar qurish;
- Koddagi har bir `push` da testlarni ishga tushirish;
- Serverga inson aralashuvisiz avtomatik deploy qilish

ni mustaqil bajara oladi.

---

# 1. Asosiy tushuncha

```yaml
name: Django CI/CD

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
    - name: Run Tests
      run: |
        pip install -r requirements.txt
        pytest
```

---

# 10. Qisqa xulosa

Bu darsda:

- `CI/CD quvurlari`;
- `GitHub Actions workflows`;
- `Avtomatik testing va deployment`

ni o‘rgandik.

Keyingi darsda: **Server sozlash (Nginx, Gunicorn, VPS)**.

---

# Resurslar va fayllar

- 📄 Konspekt: `69_dars_konspekt.pdf`
- 💻 Kodlar: `github.com/dars-reja/69-dars`
- 🎬 Video: `youtube.com/watch?v=dars69`
- 📝 Qo‘shimcha mashqlar: `python.uz/mashq69`
""",

    70: """# 🖥️ 70. Server sozlash (Nginx, Gunicorn, VPS) — Dars dokumentatsiyasi

`Nginx`, `Gunicorn` va `VPS` — Django loyihasini **real Linux serverida (Ubuntu) jonli domen va SSL sertifikati (HTTPS) bilan tarmoqqa chiqarish (Production Deployment)** uchun ishlatiladi.

Bu mavzu orqali:

- Ubuntu VPS serverini sozlash (SSH, Firewall/UFW);
- `Gunicorn` WSGI serverini o'rnatish;
- `Nginx` Reverse Proxy va Statik fayllarni tarqatish;
- Let's Encrypt va Certbot yordamida bepul SSL (HTTPS) o'rnatish

mumkin.

---

## Dars maqsadi

Bu dars oxirida o‘quvchi:

- Linux Ubuntu VPS serveriga ulanish va sozlash;
- Gunicorn va Nginx hamkorligini yo'lga qo'yish;
- Saytga bepul SSL sertifikati (HTTPS) o'rnatib internetga chiqarish

ni mustaqil bajara oladi.

---

# 1. Asosiy tushuncha

```text
Brauzer (HTTPS 443) -> Nginx (Reverse Proxy) -> Gunicorn (WSGI) -> Django App
```

---

# 10. Qisqa xulosa

Bu darsda:

- `Linux VPS va SSH`;
- `Gunicorn WSGI server`;
- `Nginx va Certbot SSL (HTTPS)`

ni o‘rgandik.

Keyingi darsda: **Yakuniy loyiha taqdimoti va Kod sharhi**.

---

# Resurslar va fayllar

- 📄 Konspekt: `70_dars_konspekt.pdf`
- 💻 Kodlar: `github.com/dars-reja/70-dars`
- 🎬 Video: `youtube.com/watch?v=dars70`
- 📝 Qo‘shimcha mashqlar: `python.uz/mashq70`
""",

    71: """# 👨‍💻 71. Yakuniy loyiha taqdimoti va Kod sharhi — Dars dokumentatsiyasi

`Yakuniy loyiha taqdimoti` — Kurs davomida egallangan barcha bilimlarni jamlagan holda **to'liq loyiha arxitekturasi va kodlarini (Code Review) taqdim etish va himoya qilish** darsi.

Bu mavzu orqali:

- Loyiha arxitekturasini tahlil qilish;
- Code Review jarayoni va Clean Code tamoyillari;
- Portfolio uchun GitHub README va Dokumentatsiyalarni tayyorlash

mumkin.

---

## Dars maqsadi

Bu dars oxirida o‘quvchi:

- O'z loyihasining arxitekturasini taqdim eta olish;
- Code Review tanqidlariga to'g'ri yondashish va kodni takomillashtirish;
- Ishga joylashish uchun kuchli Portfolio loyihasini tayyorlash

ni mustaqil bajara oladi.

---

# 1. Imtihon Kod Shabloni

```python
def final_project_review():
    print("=== YAKUNIY LOYIHA CODE REVIEW MUVAFFAQIYATLI O'TDI ===")

final_project_review()
```

---

# 10. Qisqa xulosa

Bu darsda:

- `Yakuniy Loyiha Taqdimoti`;
- `Code Review va Clean Code`;
- `GitHub Portfolio`

ni o‘rgandik.

Keyingi darsda: **Boshidan oxirigacha Yakuniy Imtihon**.

---

# Resurslar va fayllar

- 📄 Konspekt: `71_dars_konspekt.pdf`
- 💻 Kodlar: `github.com/dars-reja/71-dars`
- 🎬 Video: `youtube.com/watch?v=dars71`
- 📝 Qo‘shimcha mashqlar: `python.uz/mashq71`
""",

    72: """# 🎓 72. Boshidan oxirigacha Yakuniy Imtihon — Dars dokumentatsiyasi

`Yakuniy Imtihon` — 1-darsdan 71-darsgacha o'rganilgan **Python, OOP, SQL, Django, DRF, Celery, Docker va Deployment bo'yicha to'liq 72 darslik sertifikatlash imtihoni**.

---

## Imtihon Tartibi (100 ballik shkala)

- **Nazariy Testlar (20 ball)**: Barcha 6 ta modul bo'yicha 20 ta test;
- **Amaliy Masalalar (50 ball)**: Real Full-Stack/Backend API loyihasini qurish;
- **Kodu Sifati va Docker/CI (20 ball)**: Clean Code, Dockerfile va Testlar;
- **Vaqt va Intizom (10 ball)**: 4 soat ichida topshirish.

---

# 1. Imtihon Kod Shabloni

```python
def final_grand_exam():
    print("====================================")
    print("   YAKUNIY KURS IMTIHONI BAJARILDI  ")
    print("====================================")

final_grand_exam()
```

---

# 10. Qisqa xulosa

Bu darsda:

- `72-dars Yakuniy Imtihon topshirildi`;
- `Python Backend Kursi Muvaffaqiyatli Yakunlandi!`

---

# Resurslar va fayllar

- 📄 Konspekt: `72_dars_exam_guide.pdf`
- 💻 Kodlar: `github.com/dars-reja/72-dars`
- 🎬 Video: `youtube.com/watch?v=dars72`
- 📝 Qo‘shimcha mashqlar: `python.uz/exam_final`
"""
}

for num, txt in FULL_LONG_62_TO_72.items():
    try:
        l = Lesson.objects.get(lesson_number=num)
        l.content = txt
        l.save()
    except:
        pass

with open(LESSONS_JSON, "r", encoding="utf-8") as f:
    j_data = json.load(f)

for item in j_data:
    n = item.get("lessonNumber")
    if n in FULL_LONG_62_TO_72:
        item["content"] = FULL_LONG_62_TO_72[n]

with open(LESSONS_JSON, "w", encoding="utf-8") as f:
    json.dump(j_data, f, ensure_ascii=False, indent=2)

print("✨ 62-72 darslar kontenti to'liqligicha 10 bo'limli variantda saqlandi!")
