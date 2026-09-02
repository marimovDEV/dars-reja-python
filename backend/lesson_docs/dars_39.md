# ⌨️ 39. Reply va Inline Klaviaturalar bilan Ishlash — Dars dokumentatsiyasi

Foydalanuvchi bot bilan muloqot qilishini osonlashtirish uchun **Klaviaturalar (Keyboards)** ishlatiladi. Telegram botlarda 2 xil klaviatura turi bor:
1. **Reply Keyboard** — chat pastida paydo bo'ladi.
2. **Inline Keyboard** — xabarning aynan ostida paydo bo'ladi.

---

## Misol — Reply va Inline Keyboard yaratish

```python
from aiogram.types import (
    ReplyKeyboardMarkup, KeyboardButton,
    InlineKeyboardMarkup, InlineKeyboardButton
)

# 1. Reply Keyboard
main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📚 Kurslar"), KeyboardButton(text="📞 Aloqa")],
        [KeyboardButton(text="⚙️ Sozlamalar")]
    ],
    resize_keyboard=True
)

# 2. Inline Keyboard
inline_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="🌐 Saytga o'tish", url="https://marimovdev.uz")],
        [InlineKeyboardButton(text="✅ Tasdiqlash", callback_data="confirm_btn")]
    ]
)
```

Keyingi **40-dars: Callback Query va CallbackData Factory** da Inline tugmalar bosilganda ularga javob berishni o'rganamiz.
