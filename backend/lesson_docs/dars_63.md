# ⚙️ 63. Celery va Asinxron Vazifalar — Dars dokumentatsiyasi

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
