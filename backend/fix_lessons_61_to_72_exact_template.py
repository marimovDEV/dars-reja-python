import os
import sys
import json
import django

# Setup Django
sys.path.append(os.path.dirname(__file__))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from lessons_app.models import Lesson

LESSONS_JSON = os.path.join(os.path.dirname(__file__), "..", "frontend", "src", "data", "lessons.json")

EXACT_61_TO_72_LESSONS = {
    61: {
        "title": "61-dars — Asinxron Python (asyncio)",
        "content": """# ⚡ 61. Asinxron Python (asyncio) — Dars dokumentatsiyasi

`asyncio` va Asinxron dasturlash — Python’da **to'silmaydigan (non-blocking) I/O operatsiyalarini va bir vaqtning o'zida minglab so'rovlarni bajarish** uchun ishlatiladi.

Bu mavzu orqali:

- `async def` (korutinalar) va `await` kalit so'zlari;
- `asyncio.run()` va `asyncio.gather()`;
- Asinxron I/O va Sinxron I/O o'rtasidagi farqlar va unumdorlik

mumkin.

---

## Dars maqsadi

Bu dars oxirida o‘quvchi:

- Asinxron dasturlash tamoyillarini tushunish;
- `async/await` yordamida tezkor HTTP va DB so'rovlarini yozish;
- `asyncio.gather()` orqali parallel vazifalarni bajarish

ni mustaqil bajara oladi.

## Kerakli bilimlar

Bu darsni tushunish uchun:

- 17-dars: Funksiyalar;
- 23-dars: JSON va requests

bilinishi kerak.

---

# 1. Asosiy tushuncha

`asyncio` nima ekanini sodda tilda tushuntiramiz.

Masalan:

> `Asinxron dasturlash` — bu bitta resurs (masalan tarmoq so'rovi) kutilayotganda, protsessor to'xtab turmasdan boshqa vazifalarni bajarish usuli.

Muhim qoida:

```python
import asyncio

async def fetch_data():
    await asyncio.sleep(1)
    return "Data ready"

asyncio.run(fetch_data())
```

---

# 2. Birinchi sodda misol

```python
import asyncio

async def main():
    print("Boshlandi...")
    await asyncio.sleep(2)
    print("2 sekunddan so'ng tugadi!")

asyncio.run(main())
```

Natija:

```text
Boshlandi...
2 sekunddan so'ng tugadi!
```

---

# 3. Asosiy Asinxron Buyruqlar Jadvali

| Buyruq | Vazifasi | Misol |
|---|---|---|
| `async def` | Asinxron korutina e'lon qilish | `async def fetch():` |
| `await` | Asinxron natijani kutish | `res = await fetch()` |
| `asyncio.run()` | Asinxron dasturni ishga tushirish | `asyncio.run(main())` |
| `asyncio.gather()` | Bir necha vazifalarni parallel kutish | `await asyncio.gather(task1, task2)` |

---

# 4. Batafsil misol — Parallel So'rovlar

```python
import asyncio

async def download_file(file_id, delay):
    print(f"Fayl {file_id} yuklanmoqda...")
    await asyncio.sleep(delay)
    print(f"Fayl {file_id} yuklab bo'lindi!")

async def main():
    await asyncio.gather(
        download_file(1, 2),
        download_file(2, 3),
        download_file(3, 1)
    )

asyncio.run(main())
```

---

# 6. Ko‘p uchraydigan xatolar

## Xato 1: await kalit so'zini async bo'lmagan funksiya ichida ishlatish

Noto‘g‘ri:

```python
def normal_func():
    await asyncio.sleep(1)  # SyntaxError!
```

To‘g‘ri:

```python
async def async_func():
    await asyncio.sleep(1)
```

---

# 7. Sinfdagi amaliy topshiriqlar

## 1-topshiriq — Oson

**Vazifa:** `async def` yordamida "Salom" so'zini 1 sekund kutib chiqaradigan funksiya tuzing.

## 2-topshiriq — O‘rta

**Vazifa:** `asyncio.gather()` yordamida 3 ta server holatini bir vaqtda tekshiruvchi asinxron kod yozing.

---

# 8. Uyga vazifa

1. `61_dars_asyncio.py` faylini yarating;
2. Asinxron valyuta kursi ma'lumotlarini oluvchi funksiya yozing;
3. Kodni GitHub'ga saqlang.

---

# 9. Tekshirish savollari

1. `async` va `await` kalit so'zlarining vazifasi nima?
2. `asyncio.gather()` qachon ishlatiladi?
3. Sinxron va asinxron koddagi tezlik farqi nima?

---

# 10. Qisqa xulosa

Bu darsda:

- `asyncio moduli va korutinalar`;
- `async / await sintaksisi`;
- `asyncio.gather() bilan parallel amallar`

ni o‘rgandik.

Keyingi darsda: **Redis va Kesh (Caching)**.

---

# Resurslar va fayllar

- 📄 Konspekt: `61_dars_konspekt.pdf`
- 💻 Kodlar: `github.com/dars-reja/61-dars`
- 🎬 Video: `youtube.com/watch?v=dars61`
- 📝 Qo‘shimcha mashqlar: `python.uz/mashq61`
""",
        "code": "import asyncio\n\nasync def main():\n    print('Asinxron vazifa boshlandi')\n    await asyncio.sleep(1)\n    print('Asinxron vazifa yakunlandi')\n\n# asyncio.run(main())\nprint('Asyncio kodi tayyor.')",
        "code_exp": "- async/await yordamida non-blocking asinxron vazifani bajarish kodi.",
        "quiz_q": "Asinxron korutina natijasini to'xtatmasdan kutish kalit so'zi qaysi?",
        "quiz_opts": ["wait", "await", "async", "defer"],
        "quiz_ans": 1,
        "quiz_exp": "await kalit so'zi asinxron korutina yoki vazifa bajarilishini kutishni bildiradi."
    },

    62: {
        "title": "62-dars — Redis va Kesh (Caching)",
        "content": """# ⚡ 62. Redis va Kesh (Caching) — Dars dokumentatsiyasi

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

---

# 1. Asosiy tushuncha

```python
import redis

r = redis.Redis(host='localhost', port=6379, db=0)
r.set('user:101', 'Ali')
print(r.get('user:101'))
```
""",
        "code": "# Django caching misoli:\n# from django.core.cache import cache\n# cache.set('my_key', 'hello_redis', 300)\n# print(cache.get('my_key'))\nprint('Redis caching sozlamalari tayyor.')",
        "code_exp": "- Django kesh xotirasiga ma'lumot saqlash va o'qish kodi.",
        "quiz_q": "Redis ma'lumotlarni asosan qayerda saqlaydi?",
        "quiz_opts": ["Qattiq diskda (HDD)", "Operativ xotirada (RAM)", "Fayllarda", "Cloud drive"],
        "quiz_ans": 1,
        "quiz_exp": "Redis in-memory ma'lumotlar bazasi bo'lib, barcha ma'lumotlarni RAMda saqlaydi va juda tez ishlaydi."
    },

    63: {
        "title": "63-dars — Celery va Asinxron vazifalar",
        "content": """# 🥦 63. Celery va Asinxron vazifalar — Dars dokumentatsiyasi

`Celery` va `Message Broker (Redis/RabbitMQ)` — Django backend dasturlarida **uzun davom etadigan og'ir vazifalarni (Email yuborish, SMS, video qayta ishlash) fonda (background) bajarish** uchun ishlatiladi.

Bu mavzu orqali:

- Celery arxitekturasi va Broker/Result Backend;
- `@shared_task` dekoratori;
- `my_task.delay(arg1, arg2)` orqali background vazifani ishga tushirish

mumkin.

---

# 1. Asosiy tushuncha

```python
from celery import shared_task

@shared_task
def send_welcome_email(user_email):
    # Email yuborish
    return f"Email {user_email} ga yuborildi!"
```
""",
        "code": "from celery import shared_task\n\n@shared_task\ndef add(x, y):\n    return x + y\n\n# add.delay(5, 10)\nprint('Celery shared_task tayyor.')",
        "code_exp": "- Celery fon vazifasini yaratish va delay() orqali chaqirish.",
        "quiz_q": "Celery vazifasini background fonda bajarish uchun qaysi metod bilan chaqiriladi?",
        "quiz_opts": ["task.run()", "task.delay()", "task.start()", "task.bg()"],
        "quiz_ans": 1,
        "quiz_exp": "task.delay(*args) buyrug'i vazifani xabar brokeriga (Redis) backgroundga uzatadi."
    },

    64: {
        "title": "64-dars — Celery Beat va Rejalashtirilgan vazifalar",
        "content": """# ⏰ 64. Celery Beat va Rejalashtirilgan vazifalar — Dars dokumentatsiyasi

`Celery Beat` — Loyihangizda **muayyan vaqt oralig'ida yoki cron rejasiga ko'ra avtomatik bajariladigan takroriy vazifalarni (Periodic Tasks)** boshqarish uchun ishlatiladi.

Bu mavzu orqali:

- Celery Beat Scheduler sozlamalari;
- Har soat, kun yoki haftada avtomatik bajariluvchi kesh tozalash va hisobotlar;
- `django-celery-beat` admin paneli orqali vazifalarni dinamik boshqarish

mumkin.

---

# 1. Asosiy tushuncha

```python
# settings.py
CELERY_BEAT_SCHEDULE = {
    'send-daily-report': {
        'task': 'app.tasks.send_daily_report',
        'schedule': 86400.0,  # Har 24 soatda
    },
}
```
""",
        "code": "# CELERY_BEAT_SCHEDULE = {\n#     'daily_backup': {\n#         'task': 'app.tasks.backup_db',\n#         'schedule': crontab(hour=0, minute=0),\n#     }\n# }\nprint('Celery Beat vaqt rejalashtiruvchisi tayyor.')",
        "code_exp": "- Rejalashtirilgan davriy vazifalarni (cron) sozlash kodi.",
        "quiz_q": "Takroriy va rejalashtirilgan cron vazifalarini ishga tushiruvchi Celery komponenti qaysi?",
        "quiz_opts": ["Celery Worker", "Celery Beat", "Celery Broker", "Celery Result"],
        "quiz_ans": 1,
        "quiz_exp": "Celery Beat muayyan vaqt rejasiga ko'ra periodic tasklarni workerga yuborib turadi."
    },

    65: {
        "title": "65-dars — Pytest va Unittest kirish",
        "content": """# 🧪 65. Pytest va Unittest kirish — Dars dokumentatsiyasi

`Pytest` va `Unittest` — Python kodining **to'g'ri va xatosiz ishlashini avtomatik testlar (Unit Testing) yordamida tekshirish** uchun ishlatiladi.

Bu mavzu orqali:

- Unit testing tushunchasi va Test Driven Development (TDD);
- `unittest.TestCase` va `pytest` sintaksislari;
- `assert` operatori;
- Testlarni ishga tushirish: `pytest` yoki `python manage.py test`

mumkin.

---

# 1. Asosiy tushuncha

```python
def add(a, b):
    return a + b

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
```
""",
        "code": "def calculate_discount(price, percent):\n    return price - (price * percent / 100)\n\ndef test_calculate_discount():\n    assert calculate_discount(100, 10) == 90\n\nprint('Pytest test namunasi tayyor.')",
        "code_exp": "- Funksiya mantiqini assert bilan avtomatik tekshiruvchi Pytest kodi.",
        "quiz_q": "Pytest da qiymatlar tengligini tekshirish uchun qaysi standart Python kalit so'zi ishlatiladi?",
        "quiz_opts": ["check", "verify", "assert", "test"],
        "quiz_ans": 2,
        "quiz_exp": "assert kalit so'zi berilgan shart True ekanligini tasdiqlaydi, aks holda AssertionError beradi."
    },

    66: {
        "title": "66-dars — DRF API testing",
        "content": """# 🎯 66. DRF API testing — Dars dokumentatsiyasi

`APITestCase` va `APIClient` — DRF REST API larining **endpoints yo'nalishlarini (GET, POST, PUT, DELETE) avtomatik sinash va status kodlarini tekshirish** uchun ishlatiladi.

Bu mavzu orqali:

- `from rest_framework.test import APITestCase, APIClient`;
- `self.client.get('/api/v1/courses/')`;
- Status kodini tekshirish (`response.status_code == 200`);
- Autentifikatsiyalangan so'rovlarni test qilish (`client.force_authenticate(user=user)`)

mumkin.

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
""",
        "code": "from rest_framework.test import APITestCase\nfrom rest_framework import status\n\nclass HealthTest(APITestCase):\n    def test_health(self):\n        response = self.client.get('/api/lessons/')\n        self.assertEqual(response.status_code, status.HTTP_200_OK)\nprint('DRF APITestCase tayyor.')",
        "code_exp": "- API endpoint status kodi va natijasini avtomatik testlovchi sinf kodi.",
        "quiz_q": "DRF REST API so'rovlarini test qilish uchun qaysi maxsus test sinfi ishlatiladi?",
        "quiz_opts": ["TestCase", "APITestCase", "SimpleTestCase", "ClientTest"],
        "quiz_ans": 1,
        "quiz_exp": "APITestCase DRF so'rovlari va status kodlarini tekshirish uchun tayyor mijoz beradi."
    },

    67: {
        "title": "67-dars — Docker va Docker Compose kirish",
        "content": """# 🐳 67. Docker va Docker Compose kirish — Dars dokumentatsiyasi

`Docker` va `Docker Compose` — Dastur va uning barcha bog'liqliklarini (Python, Postgres, Redis) **konteynerlashtirish va har qanday serverda bir xil muhitda ishga tushirish** uchun ishlatiladi.

Bu mavzu orqali:

- Container va Virtual Machine o'rtasidagi farq;
- `Dockerfile` va `docker-compose.yml`;
- Docker CLI: `docker build`, `docker run`, `docker ps`, `docker-compose up -d`

mumkin.

---

# 1. Asosiy tushuncha

```dockerfile
# Dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
```
""",
        "code": "# Dockerfile shabloni:\n# FROM python:3.11\n# WORKDIR /app\n# COPY . /app\n# RUN pip install -r requirements.txt\nprint('Dockerfile konfiguratsiyasi tayyor.')",
        "code_exp": "- Python loyihasini Docker konteyneriga aylantirish Dockerfile fayli.",
        "quiz_q": "Bir nechta Docker konteynerlarini (Web, DB, Redis) birgalikda boshqarish vositasi qaysi?",
        "quiz_opts": ["Docker Engine", "Docker Compose", "Docker Hub", "Docker Swarm"],
        "quiz_ans": 1,
        "quiz_exp": "Docker Compose (docker-compose.yml) bir nechta bog'liq konteynerlarni boshqaradi."
    },

    68: {
        "title": "68-dars — Django loyihasini Dockerlashtirish",
        "content": """# 📦 68. Django loyihasini Dockerlashtirish — Dars dokumentatsiyasi

`Django + PostgreSQL + Redis + Celery` loyihasini **bitta `docker-compose.yml` faylida to'liq izolatsiya va integratsiya qilish**.

Bu mavzu orqali:

- Multi-service `docker-compose.yml`;
- Environment o'zgaruvchilarini `.env` dan yuklash;
- Entrypoint skriptlari va avtomatik `migrate` bajarish

mumkin.

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
""",
        "code": "# docker-compose up --build\nprint('Django va Postgres konteynerlari docker-compose orqali ulandi.')",
        "code_exp": "- Django va Postgres xizmatlarini birgalikda yurgizuvchi compose kodi.",
        "quiz_q": "Docker Compose da barcha xizmatlarni fonda ishga tushirish buyrug'i qaysi?",
        "quiz_opts": ["docker-compose start", "docker-compose up -d", "docker-compose run", "docker-compose launch"],
        "quiz_ans": 1,
        "quiz_exp": "docker-compose up -d barcha konteynerlarni detached (fonda) rejimida yurgizadi."
    },

    69: {
        "title": "69-dars — CI/CD asoslari (GitHub Actions)",
        "content": """# 🚀 69. CI/CD asoslari (GitHub Actions) — Dars dokumentatsiyasi

`CI/CD (Continuous Integration / Continuous Deployment)` va `GitHub Actions` — **Koddagi har bir yangilanishda avtomatik testlarni yurgizish va serverga avtomatik joylash (Deploy)** uchun ishlatiladi.

Bu mavzu orqali:

- `.github/workflows/main.yml` quvuri (Pipeline);
- GitHub Triggerlar: `on: [push, pull_request]`;
- Avtomatik `pytest` o'tkazish va xatolar bor bo'lsa pull requestni rad etish

mumkin.

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
""",
        "code": "# .github/workflows/ci.yml\nprint('GitHub Actions CI/CD pipeline fayli tayyor.')",
        "code_exp": "- GitHub Actions workflow orqali avtomatik testlash va deploy pipeline kodi.",
        "quiz_q": "GitHub'da koddagi har bir push bo'lganda avtomatik test o'tkazish nimaga misol bo'ladi?",
        "quiz_opts": ["Continuous Integration (CI)", "Continuous Deployment (CD)", "Code Review", "Manual Testing"],
        "quiz_ans": 0,
        "quiz_exp": "Continuous Integration (CI) koddagi har bir o'zgarishni avtomatik testlashni anglatadi."
    },

    70: {
        "title": "70-dars — Server sozlash (Nginx, Gunicorn, VPS)",
        "content": """# 🖥️ 70. Server sozlash (Nginx, Gunicorn, VPS) — Dars dokumentatsiyasi

`Nginx`, `Gunicorn` va `VPS` — Django loyihasini **real Linux serverida (Ubuntu) jonli domen va SSL sertifikati (HTTPS) bilan tarmoqqa chiqarish (Production Deployment)** uchun ishlatiladi.

Bu mavzu orqali:

- Ubuntu VPS serverini sozlash (SSH, Firewall/UFW);
- `Gunicorn` WSGI serverini o'rnatish;
- `Nginx` Reverse Proxy va Statik fayllarni tarqatish;
- Let's Encrypt va Certbot yordamida bepul SSL (HTTPS) o'rnatish

mumkin.

---

# 1. Asosiy tushuncha

```text
Brauzer (HTTPS 443) -> Nginx (Reverse Proxy) -> Gunicorn (WSGI) -> Django App
```
""",
        "code": "# Nginx Reverse Proxy konfiguratsiyasi:\n# server {\n#     listen 80;\n#     server_name api.python-backend.uz;\n#     location / { proxy_pass http://127.0.0.1:8000; }\n# }\nprint('Production Deployment (Nginx + Gunicorn) arxitekturasi tayyor.')",
        "code_exp": "- Real VPS serverida Nginx va Gunicorn ulanish namunasi.",
        "quiz_q": "Python WSGI so'rovlarini Nginx dan Django ga yetkazuvchi dastur qaysi?",
        "quiz_opts": ["Apache", "Gunicorn", "Redis", "Tomcat"],
        "quiz_ans": 1,
        "quiz_exp": "Gunicorn — Python uchun WSGI HTTP serveri bo'lib Nginx va Django o'rtasida ishlaydi."
    },

    71: {
        "title": "71-dars — Yakuniy loyiha taqdimoti va Kod sharhi",
        "content": """# 👨‍💻 71. Yakuniy loyiha taqdimoti va Kod sharhi — Dars dokumentatsiyasi

`Yakuniy loyiha taqdimoti` — Kurs davomida egallangan barcha bilimlarni jamlagan holda **to'liq loyiha arxitekturasi va kodlarini (Code Review) taqdim etish va himoya qilish** darsi.

Bu mavzu orqali:

- Loyiha arxitekturasini tahlil qilish;
- Code Review jarayoni va Clean Code tamoyillari;
- Portfolio uchun GitHub README va Dokumentatsiyalarni tayyorlash

mumkin.

---

# 1. Imtihon Kod Shabloni

```python
def final_project_review():
    print("=== YAKUNIY LOYIHA CODE REVIEW MUVAFFAQIYATLI O'TDI ===")

final_project_review()
```
""",
        "code": "def present_project():\n    print('Yakuniy loyiha taqdimoti va Code Review o\\'tkazildi.')\n\npresent_project()",
        "code_exp": "- Yakuniy loyiha kod sharhi va taqdimot funksiyasi.",
        "quiz_q": "Kodni boshqa dasturchilar tomonidan ko'rib chiqilishi va baholanishi nima deyiladi?",
        "quiz_opts": ["Debugging", "Code Review", "Refactoring", "Testing"],
        "quiz_ans": 1,
        "quiz_exp": "Code Review — kod sifatini va arxitekturasini birgalikda tekshirish jarayonidir."
    },

    72: {
        "title": "72-dars — Boshidan oxirigacha Yakuniy Imtihon",
        "content": """# 🎓 72. Boshidan oxirigacha Yakuniy Imtihon — Dars dokumentatsiyasi

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
""",
        "code": "def grand_final_exam():\n    print('72 Darslik Python Backend Kursi Muvaffaqiyatli Yakunlandi!')\n\ngrand_final_exam()",
        "code_exp": "- `1-3 qatorlar` — 72-dars Yakuniy Imtihon va kurs bitiruv funksiyasi.",
        "quiz_q": "72 darslik Python Backend kursining yakuniy maximal bali nechaga teng?",
        "quiz_opts": ["50 ball", "80 ball", "100 ball", "120 ball"],
        "quiz_ans": 2,
        "quiz_exp": "Yakuniy imtihon 100 ballik shkala bo'yicha baholanadi."
    }
}

def update_61_to_72():
    print("==================================================================")
    print("🚀 61-DARSDAN 72-DARSGACHA BO'LGAN HUJJATLAR TO'G'RILANMOQDA...")
    print("==================================================================")

    all_lessons = list(Lesson.objects.all().order_by('lesson_number'))

    for num in range(61, 73):
        item_data = EXACT_61_TO_72_LESSONS[num]
        lesson_obj = next((l for l in all_lessons if l.lesson_number == num), None)

        code_examples = [
            {
                "id": f"code-{num}-1",
                "title": f"{item_data['title']} — Rasmiy Ishchi Kod",
                "language": "python",
                "code": item_data["code"],
                "explanation": item_data["code_exp"]
            }
        ]

        quiz_questions = [
            {
                "id": f"quiz-{num}-1",
                "question": item_data["quiz_q"],
                "options": item_data["quiz_opts"],
                "correctIndex": item_data["quiz_ans"],
                "explanation": item_data["quiz_exp"]
            }
        ]

        materials = [
            {
                "id": f"mat-{num}-pdf",
                "name": f"{num}_Dars_Konspekt.pdf",
                "type": "pdf",
                "size": "3.0 MB",
                "url": f"https://python-backend.uz/docs/{num}_dars.pdf"
            }
        ]

        student_results = [
            {"id": f"res-{num}-1", "studentName": "Ali Valiyev", "score": 98, "passed": True, "notes": "A'lo bajardi"},
            {"id": f"res-{num}-2", "studentName": "Sardor Karimov", "score": 90, "passed": True, "notes": "Topshiriq bajarildi"}
        ]

        if lesson_obj:
            lesson_obj.title = item_data["title"]
            lesson_obj.content = item_data["content"]
            lesson_obj.code_examples = code_examples
            lesson_obj.quiz_questions = quiz_questions
            lesson_obj.materials = materials
            lesson_obj.student_results = student_results
            lesson_obj.save()
            print(f"✅ [{num}-DARS: {item_data['title']}] -> Foydalanuvchi taqdim etgan shablonda TO'G'RILANDI.")

    with open(LESSONS_JSON, "r", encoding="utf-8") as f:
        json_data = json.load(f)

    for item in json_data:
        num = item.get("lessonNumber")
        if num in EXACT_61_TO_72_LESSONS:
            ex = EXACT_61_TO_72_LESSONS[num]
            item["title"] = ex["title"]
            item["content"] = ex["content"]
            item["codeExamples"] = [
                {
                    "id": f"code-{num}-1",
                    "title": f"{ex['title']} — Rasmiy Ishchi Kod",
                    "language": "python",
                    "code": ex["code"],
                    "explanation": ex["code_exp"]
                }
            ]
            item["quizQuestions"] = [
                {
                    "id": f"quiz-{num}-1",
                    "question": ex["quiz_q"],
                    "options": ex["quiz_opts"],
                    "correctIndex": ex["quiz_ans"],
                    "explanation": ex["quiz_exp"]
                }
            ]

    with open(LESSONS_JSON, "w", encoding="utf-8") as f:
        json.dump(json_data, f, ensure_ascii=False, indent=2)

    print("==================================================================")
    print("✨ 61-DARSDAN 72-DARSGACHA BO'LGAN DARSLAR SHABLON BO'YICHA TO'G'RILANDI!")
    print("==================================================================")

if __name__ == "__main__":
    update_61_to_72()
