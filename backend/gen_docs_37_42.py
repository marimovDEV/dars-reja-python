#!/usr/bin/env python3
"""Generate lesson docs 37-42 with full 19-section documentation template."""
import os

DOCS_DIR = os.path.join(os.path.dirname(__file__), "lesson_docs")

lessons = {}

# 37-DARS
lessons[37] = """# 🌐 37. HTTP, REST API va Web asoslari — Dars dokumentatsiyasi

Zamonaviy veb va mobil dasturlar (Frontend, Mobile App, Backend) o'zaro **HTTP (Hypertext Transfer Protocol)** protokoli orqali muloqot qiladi. Backend dasturchining asosiy vazifasi — mijoz (client/brauzer) yuborgan so'rovlarga to'g'ri javob beruvchi server va **REST API** interfeyslarini qurishdir.

**REST (Representational State Transfer)** — bu veb-xizmatlarni (Web Services) loyihalashtirish uchun ishlatiladigan eng mashhur me'moriy uslub (architectural style) hisoblanadi.

Ushbu darsda siz HTTP so'rov turlari (`GET`, `POST`, `PUT`, `DELETE`), so'rov sarlavhalari (`Headers`), javob kodlari (`Status Codes: 200, 201, 400, 404, 500`) va REST API tamoyillarini o'rganasiz.

---

## Bu mavzu orqali nimalar qilish mumkin

- Client-Server (Mijoz-Server) arxitekturasini tushunish;
- HTTP So'rov metodlaridan (`GET`, `POST`, `PUT`, `PATCH`, `DELETE`) to'g'ri foydalanish;
- HTTP Status Kodlarining guruhlanishini va ma'nolarini bilish;
- RESTful API resurs yo'nalishlarini (Endpoints) to'g'ri loyihalashtirish (`/api/v1/users/`);
- API javoblarini JSON formatida shakllantirish.

---

## Dars maqsadi

Bu dars oxirida o'quvchi:

- HTTP so'rov-javob siklini (Request-Response Cycle) tushunish;
- REST API mezonlari va prinsiplarini bilish;
- Status kodlarini to mezon holatda ishlatish;
- Postman yoki cURL orqali API so'rovlarini sinash

ni mustaqil bajara oladi.

---

## Kerakli oldingi bilimlar

- 23-dars: JSON va requests;
- 31-dars: SQL va ma'lumotlar bazasi.

---

# 1. Asosiy tushunchalar va atamalar

## Client-Server Arxitekturasi nima?

> **Client** (brauzer, mobil ilova) so'rov yuboradi, **Server** (Django/FastAPI) so'rovni qayta ishlab javob (Response) qaytaradi.

## REST API nima?

> HTTP protokoli ustiga qurilgan, resurslarga URL orqali murojaat qiluvchi va ma'lumotlarni asosan JSON ko'rinishida uzatuvchi backend interfeysi.

## Endpoint nima?

> Serverdagi muayyan resursga olib boruvchi URL manzil. Masalan: `https://api.site.com/products/`.

---

# 2. HTTP So'rov Metodlari va Status Kodlari

## HTTP Metodlari (Verbs)

| Metod | Vazifasi | Misol |
|---|---|---|
| **`GET`** | Resursni (ma'lumotni) o'qish/olish | `/api/users/` |
| **`POST`** | Yangi resurs yaratish | `/api/users/` (Body bilan) |
| **`PUT`** | Mavjud resursni to'liq yangilash | `/api/users/1/` |
| **`PATCH`** | Resursning ma'lum qismini yangilash | `/api/users/1/` |
| **`DELETE`**| Resursni o'chirish | `/api/users/1/` |

## HTTP Status Kodlari

- **`2xx` (Success)**: `200 OK`, `201 Created` (Yangi resurs yaratildi).
- **`3xx` (Redirection)**: `301 Moved Permanently`, `302 Found`.
- **`4xx` (Client Error)**: `400 Bad Request`, `401 Unauthorized`, `403 Forbidden`, `404 Not Found`.
- **`5xx` (Server Error)**: `500 Internal Server Error`, `502 Bad Gateway`.

---

# 3. Kod misollari (REST API Struct Simulyatsiyasi)

```python
# REST API Endpoint Strukturasi Namunasining Standarti
# GET /api/v1/books/       -> Barcha kitoblarni olish
# POST /api/v1/books/      -> Yangi kitob qo'shish
# GET /api/v1/books/5/     -> ID=5 bo'lgan kitobni olish
# PUT /api/v1/books/5/     -> ID=5 kitobni to'liq o'zgartirish
# DELETE /api/v1/books/5/  -> ID=5 kitobni o'chirish
```

---

# 10. Qisqa xulosa

Bu darsda Web arxitekturasi, HTTP protokoli, Status kodlar va REST API tamoyillari o'rganildi.
"""

# 38-DARS
lessons[38] = """# 🐙 38. Git va GitHub — Dars dokumentatsiyasi

**Git** — bu dastur kodingizning barcha o'zgarishlar tarixini kuzatib boruvchi va saqlovchi dunyodagi eng mashhur **Versiyalarni Boshqarish Tizimi (VCS - Version Control System)** dir. U dasturchiga istalgan vaqtda kodning avvalgi holatiga qaytish yoki bir vaqtning o'zida bir nechta versiya (branches) ustida ishlash imkoniyatini beradi.

**GitHub** — bu Git repozitoriylarini bulutda saqlash, boshqa dasturchilar bilan birgalikda (teamwork) loyiha ustida ishlash va kodlarni ulashish uchun mo'ljallangan veb-platformadir.

---

## Bu mavzu orqali nimalar qilish mumkin

- Kompyuterda yangi Git repozitoriysi yaratish (`git init`);
- Kod o'zgarishlarini kuzatish (`git status`, `git add`, `git commit`);
- Tarmoqlar (`branches`) yaratish va ularni birlashtirish (`git merge`);
- Loyihani GitHub bulutli omboriga yuklash (`git push`) va u yerdan yuklab olish (`git clone`, `git pull`).

---

## Dars maqsadi

Bu dars oxirida o'quvchi:

- Git va GitHub o'rtasidagi farqni bilish;
- Asosiy Git buyruqlarini terminalda ishlatish;
- `.gitignore` fayli orqali keraksiz fayllarni (masalan `venv`, `.env`) berkitish;
- Loyihani GitHub platformasiga joylay olish

ni mustaqil bajara oladi.

---

## Kerakli oldingi bilimlar

- 1-dars: Terminal va dasturlash muhiti.

---

# 1. Asosiy Git Buyruqlari Jadvali

| Buyruq | Vazifasi |
|---|---|
| `git init` | Joriy papkada yangi local Git repozitoriy yaratadi |
| `git status` | O'zgartirilgan va kuzatuvdagi fayllar holatini ko'rsatadi |
| `git add .` | Barcha o'zgarishlarni keshga (staging area) qo'shadi |
| `git commit -m "msg"` | O'zgarishlarni izoh bilan xotiraga muhrlaydi |
| `git branch` | Mavjud tarmoqlarni ko'rsatadi |
| `git checkout -b name`| Yangi tarmoq yaratib unga o'tadi |
| `git push origin main` | Kodni GitHub omboriga yuklaydi |
| `git pull origin main` | GitHub dan so'nggi o'zgarishlarni yuklab oladi |

---

# 2. Amaliy Ish Ketma-ketligi (Workflow)

```bash
# 1. Repozitoriy yaratish
git init

# 2. Fayllarni belgilash va commit qilish
git add .
git commit -m "Initial commit: Project setup"

# 3. GitHub repozitoriyasiga ulash
git remote add origin https://github.com/username/project.git

# 4. Kodni GitHub ga push qilish
git branch -M main
git push -u origin main
```

---

# 10. Qisqa xulosa

Bu darsda Git versiyalar boshqaruvi tizimi, asosiy buyruqlar va GitHub bilan ishlash o'rganildi.
"""

# 39-DARS
lessons[39] = """# 📦 39. Virtual Environment va pip — Dars dokumentatsiyasi

Har bir Python loyihasi har xil tashqi kutubxonalarga va hatto u kutubxonalarning har xil versiyalariga bog'liq bo'lishi mumkin. Masalan, 1-loyiha `Django 4.2` ishlatishi, 2-loyiha esa `Django 5.0` ishlatishi mumkin. 

Kutubxonalarni kompyuterga global o'rnatish loyihalar o'rtasida **versiyalar toqnashuviga (dependency conflict)** olib keladi.

**Virtual Environment (`venv`)** — bu har bir loyiha uchun alohida, izolyatsiyalangan (ajratilgan) Python muhitini yaratish vositasidir. **`pip`** esa Python uchun paket va kutubxonalarni o'rnatuvchi menejerdir.

---

## Bu mavzu orqali nimalar qilish mumkin

- Har bir loyiha uchun alohida `venv` yaratish va uni faollashtirish (activate);
- `pip` yordamida tashqi kutubxonalarni o mezon qilish, yangilash va o'chirish;
- `requirements.txt` fayli orqali loyiha bog'liqliklarini eksport va import qilish.

---

# Asosiy Buyruqlar

```bash
# 1. Virtual Muhit yaratish
python -m venv venv

# 2. Muhitni faollashtirish (Activate)
# Mac/Linux:
source venv/bin/activate
# Windows:
# venv\Scripts\activate

# 3. Paket o'rnatish
pip install django

# 4. Bog'liqliklar ro'yxatini faylga saqlash
pip freeze > requirements.txt

# 5. Boshqa kompyuterda fayldan o'rnatish
pip install -r requirements.txt
```

---

# 10. Qisqa xulosa

Bu darsda izolyatsiyalangan virtual muhit (`venv`), paketlar menejeri (`pip`) va `requirements.txt` bilan ishlash o'rganildi.
"""

# 40-DARS
lessons[40] = """# 🟢 40. Django Kirish va Loyiha Strukturasi — Dars dokumentatsiyasi

**Django** — bu Python tilida yozilgan, "tayyor batareyalarga ega" (batteries-included), yuqori darajali eng mashhur Web Freymvorkdir. U tezkor, xavfsiz va kengayuvchan (scalable) backend tizimlar va veb-saytlar yaratish uchun ishlatiladi.

Django **MVT (Model-View-Template)** me'moriy namunasiga asoslangan.

Ushbu darsda siz Django freymvorkini o'rnatish, yangi loyiha yaratish (`django-admin startproject`) va loyihaning standart fayllar strukturasi bilan tanishasiz.

---

## Django Loyiha Fayllar Strukturasi

- **`manage.py`**: Loyihani boshqarish (serverni runs qilish, migratsiyalar) buyruqlari skripti.
- **`settings.py`**: Loyihaning barcha asosiy sozlamalari (baza, o'rnatilgan ilovalar, vaqt zonasi).
- **`urls.py`**: Saytning URL manzil (routing) xaritasi.
- **`wsgi.py` / `asgi.py`**: Web-serverlar bilan ishlash uchun interfeys fayllari.

---

# Birinchi Loyihani Yaratish

```bash
# 1. Django o'rnatish
pip install django

# 2. Loyiha yaratish
django-admin startproject myproject .

# 3. Development Serverni ishga tushirish
python manage.py runserver
```

---

# 10. Qisqa xulosa

Bu darsda Django freymvorki, MVT arxitekturasi va loyihani ishga tushirish o'rganildi.
"""

# 41-DARS
lessons[41] = """# 🧩 41. Django Apps va URLs — Dars dokumentatsiyasi

Django loyihalari kichik va mustaqil modullardan — **Apps (Ilovalar)** dan tashkil topadi. Masalan, e-commerce loyihasida `users`, `products`, `orders`, `blog` kabi alohida app'lar bo'ladi. Bu modulizm kodingizni toza va tartibli saqlashga xizmat qiladi.

**URLs (`urls.py`)** esa foydalanuvchi brauzerga kiritgan manzilni (URL) mos keluvchi mantig'iy funksiyaga (View) yo'naltirish (routing) vazifasini bajaradi.

---

# App Yaratish va Ulash

```bash
# Yangi App yaratish
python manage.py startapp main
```

**`settings.py` ichiga ulaymiz:**
```python
INSTALLED_APPS = [
    # ...
    'main',
]
```

**App ichida `urls.py` yaratib asosiy URLs ga ulaymiz (`include`):**
```python
# myproject/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
]
```

---

# 10. Qisqa xulosa

Bu darsda Django ilovalari (`apps`) va URL marshrutlash (`routing`) tushunchalari o'rganildi.
"""

# 42-DARS
lessons[42] = """# 🖼️ 42. Django Views va Templates — Dars dokumentatsiyasi

**Views (`views.py`)** — bu foydalanuvchining so'rovini (`HttpRequest`) qabul qilib, kerakli mantiqiy amallarni bajaruvchi hamda javob (`HttpResponse` yoki HTML Template) qaytaruvchi funksiya yoki klassdir.

**Templates** — bu ma'lumotlarni foydalanuvchiga HTML shaklida ko'rsatish uchun mo'ljallangan va Django Template Language (DTL) bilan boyitilgan shablonlar papkasidir.

---

# Kod misoli — Views va Template

```python
# main/views.py
from django.shortcuts import render
from django.http import HttpResponse

def home_page(request):
    context = {"title": "Bosh Sahifa", "user_name": "Ali"}
    return render(request, "main/home.html", context)
```

**DTL (Django Template Language) HTML ichida:**
```html
<!-- main/templates/main/home.html -->
<h1>Xush kelibsiz, {{ user_name }}!</h1>
```

---

# 10. Qisqa xulosa

Bu darsda Django Views va HTML Templates (DTL) mexanizmi o'rganildi.
"""

for num, content in lessons.items():
    filepath = os.path.join(DOCS_DIR, f"dars_{num:02d}.md")
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"dars_{num:02d}.md yaratildi: {len(content)} belgi")
