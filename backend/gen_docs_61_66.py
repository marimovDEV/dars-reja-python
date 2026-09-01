#!/usr/bin/env python3
"""Generate lesson docs 61-66 (Advanced Python & DevOps module 6) with full 19-section documentation template."""
import os

DOCS_DIR = os.path.join(os.path.dirname(__file__), "lesson_docs")

lessons = {}

# 61-DARS
lessons[61] = """# ⚡ 61. Asinxron Python (asyncio) — Dars dokumentatsiyasi

Standart Python kodi **sinxron (synchronous)** ishlaydi, ya'ni bitta operatsiya (masalan, tarmoq so'rovi yoki fayldan o'qish) tugamaguncha keyingi kod kutib turadi (blocking I/O).

**Asinxron Dasturlash (`asyncio`)** — bu vaqt oluvchi I/O operatsiyalari (Network, Database, File) bajarilayotganda protsessor vaqtini zoye ketkazmasdan, boshqa vazifalarni parallel ravishda bajarish imkonini beruvchi texnologiyadir.

Python 3.5+ versiyalarida asinxronlik **`async`** va **`await`** kalit so'zlari hamda **Event Loop (Hodisalar Sikli)** orqali amalga oshiriladi.

---

## Bu mavzu orqali nimalar qilish mumkin

- Sinxron (blocking) va Asinxron (non-blocking) kod o'rtasidagi farqni tushunish;
- `async def` yordamida korutinalar (coroutines) yaratish;
- `await` yordamida asinxron operatsiyalarni kutish;
- `asyncio.gather()` orqali yuzlab tarmoq so'rovlarini bir vaqtda parallel bajarish.

---

# Kod misoli — asyncio bilan Parallel So'rovlar

```python
import asyncio
import time

async def fetch_data(id, delay):
    print(f"Task {id} boshlandi...")
    await asyncio.sleep(delay) # Non-blocking sleep
    print(f"Task {id} tugadi!")
    return f"Natija {id}"

async def main():
    # Parallel bajarish
    results = await asyncio.gather(
        fetch_data(1, 2),
        fetch_data(2, 3),
        fetch_data(3, 1)
    )
    print("Barcha natijalar:", results)

start = time.time()
asyncio.run(main())
print(f"Jami ketgan vaqt: {time.time() - start:.2f} soniya") # 3 soniya (sinxron bo'lsa 6 sec bo'lardi)
```

---

# 10. Qisqa xulosa

Bu darsda Asinxron dasturlash, Event Loop, `async/await` va `asyncio` moduli o'rganildi.
"""

# 62-DARS
lessons[62] = """# 🚀 62. Redis va Kesh (Caching) — Dars dokumentatsiyasi

Har bir so'rov kelganda ma'lumotlar bazasiga (PostgreSQL) murojaat qilish va murakkab hisob-kitoblarni qayta bajarish loyihaning sekinlashishiga olib keladi.

**Kesh (Caching)** — bu tez-tez so'raladigan va kam o'zgaradigan ma mezonlarni juda tezkor xotiraga (RAM) saqlab qo'yish mexanizmidir.

**Redis (Remote Dictionary Server)** — bu xotirada (In-Memory) Key-Value formatida ishlovchi ultra-tezkor ma mezonlar bazasidir. U kesh saqlash, seanslar boshqaruvi va xabarlar navbati (Message Broker) uchun ishlatiladi.

---

# Kod misoli — Django va Redis Caching

```python
# settings.py
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.redis.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/1',
    }
}

# views.py
from django.core.cache import cache
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Product

class ProductListCachedView(APIView):
    def get(self, request):
        data = cache.get("all_products")
        if not data:
            print("DB dan o'qilmoqda...")
            products = Product.objects.all()
            data = list(products.values())
            cache.set("all_products", data, timeout=60*15) # 15 minut keshda turadi
        else:
            print("Keshdan (Redis) o'qildi!")
        return Response(data)
```

---

# 10. Qisqa xulosa

Bu darsda Kesh (Caching) konseptsiyasi, Redis In-Memory DB va Django Caching o'rganildi.
"""

# 63-DARS
lessons[63] = """# ⚙️ 63. Celery va Asinxron Vazifalar — Dars dokumentatsiyasi

Veb-saytda ba'zi amaliyotlar (masalan: foydalanuvchiga PDF fayl yaratib berish, email yuborish, videoni qayta ishlash) uzoq vaqt oladi. Agar bu amallar so'rov-javob siklida (Request-Response) bajarilsa, foydalanuvchi sahifa yuklanishini kutib qoladi.

**Celery** — bu orqa fonda (background tasks) vaqt oluvchi og'ir vazifalarni asinxron bajaruvchi maxsus vazifalar navbati (Distributed Task Queue) tizimidir. Celery ma'lumotlar almashinuvi uchun **Redis** yoki **RabbitMQ** dan broker sifatida foydalanadi.

---

# Kod misoli — Celery Task Yaratish

```python
# myproject/celery.py
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
app = Celery('myproject')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

# main/tasks.py
from celery import shared_task
import time

@shared_task
def send_welcome_email(user_email):
    time.sleep(5) # Email yuborish simulyatsiyasi
    print(f"Email yuborildi: {user_email}")
    return True

# View ichida chaqirish:
# send_welcome_email.delay("user@mail.com") # Orqa fonda (background) ishlaydi!
```

---

# 10. Qisqa xulosa

Bu darsda Celery vazifalar navbati va background tasks arxitekturasi o'rganildi.
"""

# 64-DARS
lessons[64] = """# ⏰ 64. Celery Beat va Rejalashtirilgan Vazifalar — Dars dokumentatsiyasi

Ba'zi vazifalar ma'lum bir rejalashtirilgan vaqt oralig'ida (masalan: har kuni kechasi soat 00:00 da bazani backup qilish, har soatda ob-havo ma'lumotlarini yangilash, har oy boshida billing hisoblash) avtomatik ishga tushishi kerak.

**Celery Beat** — bu Linux cron job kabi rejalashtirilgan vazifalarni (Periodic Tasks) ko'rsatilgan vaqt jadvali bo'yicha avtomatik Celery ga topshiruvchi scheduler vositasidir.

---

# Kod misoli — Periodic Task Sozlanishi

```python
# settings.py
from celery.schedules import crontab

CELERY_BEAT_SCHEDULE = {
    'daily_backup_task': {
        'task': 'main.tasks.make_database_backup',
        'schedule': crontab(hour=0, minute=0), # Har kuni yarim tunda
    },
    'every_10_minutes': {
        'task': 'main.tasks.update_rates',
        'schedule': 600.0, # Har 10 minutda (600 sek)
    },
}
```

---

# 10. Qisqa xulosa

Bu darsda Celery Beat va vaqt bo'yicha rejalashtirilgan davriy vazifalar (Periodic Tasks) o'rganildi.
"""

# 65-DARS
lessons[65] = """# 🧪 65. Pytest va Unittest Kirish — Dars dokumentatsiyasi

Dastur hajmi kattalashgani sari, har bir yangi funksionallik qo'shilganda eski kodingiz buzilmaganligiga ishonch hosil qilish uchun qo'lda tekshirish imkonsiz bo'lib qoladi.

**Avtomatlashtirilgan Testlash (Automated Testing)** — bu kodning to'g'ri ishlayotganini avtomatik ravishda tekshiruvchi test ssenariylarini yozishdir.

Python'da **`unittest`** (standart kutubxona) va **`pytest`** (eng ommabop, qulay va kuchli freymvork) ishlatiladi.

---

# Kod misoli — Pytest va Unittest

```python
# 1. Unittest Misoli
import unittest

def add(a, b):
    return a + b

class TestMath(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)

# 2. Pytest Misoli (Qisqa va zamonaviy)
def test_addition():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
```

---

# 10. Qisqa xulosa

Bu darsda Unit Testing, `unittest` va `pytest` freymvorklari o'rganildi.
"""

# 66-DARS
lessons[66] = """# 🧪 66. DRF API Testing — Dars dokumentatsiyasi

Backend REST API larni testlash — bu so'rov yuborilganda kutilgan Status kodi (`200`, `201`, `400`) va JSON javob tuzilishi qaytayotganini avtomatik tekshirish demakdir.

Django REST Framework o'zining **`APITestCase`** va **`APIClient`** maxsus vositalarini taqdim etadi.

---

# Kod misoli — DRF APITestCase

```python
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Product

class ProductAPITest(APITestCase):
    def setUp(self):
        self.product = Product.objects.create(title="Test Product", price=100)

    def test_get_product_list(self):
        url = reverse('product-list') # API endpoint URL
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_product(self):
        url = reverse('product-list')
        data = {"title": "New Product", "price": 150}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
```

---

# 10. Qisqa xulosa

Bu darsda DRF API larni avtomatik testlash (`APITestCase`, `APIClient`) o'rganildi.
"""

for num, content in lessons.items():
    filepath = os.path.join(DOCS_DIR, f"dars_{num:02d}.md")
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"dars_{num:02d}.md yaratildi: {len(content)} belgi")
