# ⏰ 64. Celery Beat va Rejalashtirilgan Vazifalar — Dars dokumentatsiyasi

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
