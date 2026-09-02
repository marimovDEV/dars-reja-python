# 🌐 46. Telegram Web App (Mini Apps) Integratsiyasi — Dars dokumentatsiyasi

**Telegram Web App (Mini Apps)** — bu Telegram ilovasi ichidan chiqmasdan to'liq veb-sayt va do'kon interfeysini ochish imkonini beruvchi eng zamonaviy texnologiyadir.

---

## Misol — Web App Tugmasini Ulash

```python
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

webapp_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(
            text="🛒 Onlayn Do'konni Ochish",
            web_app=WebAppInfo(url="https://python.marimovdev.uz")
        )]
    ]
)
```

Keyingi **47-dars: Webhook Integratsiyasi va Serverga Deploy Qilish** da botni 24/7 rejimida Linux serverga joylashni o'rganamiz.
