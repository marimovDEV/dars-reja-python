# 📁 45. Media, Fayllar, Lokatsiya va Kontakt Yuborish — Dars dokumentatsiyasi

Telegram botlarda foydalanuvchining telefon raqamini olish (`request_contact=True`) hamda yetkazib berish manzili uchun geografik lokatsiyasini (`request_location=True`) olish juda qulay.

---

## Misol — Kontakt va Lokatsiya so'rash

```python
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

contact_geo_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📱 Telefon raqamni yuborish", request_contact=True)],
        [KeyboardButton(text="📍 Geolokatsiyani yuborish", request_location=True)]
    ],
    resize_keyboard=True
)
```

Keyingi **46-dars: Telegram Web App (Mini Apps) Integratsiyasi** da bot ichida zamonaviy veb ilovalarni ochishni o'rganamiz.
