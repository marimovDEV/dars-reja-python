# 🔍 38. Aiogram Handlerlar va Message Filterlari — Dars dokumentatsiyasi

Telegram botlarda kelayotgan xabarlar juda xilma-xil bo'ladi: matnlar, rasmlar, audio, fayllar va stikerlar. Ushbu xabarlarni to'g'ri filtrlash va har biriga mos javob berish uchun **Aiogram 3 Filterlari** va **Routerlar** ishlatiladi.

---

## Bu mavzu orqali nimalar qilish mumkin

- `Router` yordamida bot kodini bir nechta fayllarga modulli bo'lish;
- Magic Filter (`F`) orqali xabarlarni shartli ushlash;
- Rasm (`F.photo`), fayl (`F.document`) va stikerlarni ajratish;
- Regex va sarlavha bo'yicha filtrlash.

---

## Asosiy tushunchalar va atamalar

## Router nima?

> **Router** — bu katta bot loyihalarida handlerlarni mantiqiy papka va fayllarga bo'lib boshqarish imkonini beruvchi Aiogram 3 moduli.

## Magic Filter (F) nima?

> **Magic Filter (F)** — bu Aiogram 3'dagi qisqa va qulay obyekt bo'lib, xabar xossalarini (masalan `F.text == 'Salom'`) oson filtrlashni ta'minlaydi.

---

## Misol — Router va Filterlar bilan ishlash

```python
from aiogram import Router, F, types
from aiogram.filters import Command

router = Router()

# Matn tengligini tekshirish
@router.message(F.text == "Salom")
async def text_salom(message: types.Message):
    await message.answer("Vaalaykum assalom!")

# Rasm kelganda ushlash
@router.message(F.photo)
async def photo_handler(message: types.Message):
    await message.answer("Siz rasm yubordingiz! Rasm qabul qilindi.")

# Fayl kelganda ushlash
@router.message(F.document)
async def doc_handler(message: types.Message):
    await message.answer(f"Fayl nomi: {message.document.file_name}")
```

Keyingi **39-dars: Reply va Inline Klaviaturalar bilan Ishlash** da Telegram tugmalarini yaratish va loyihaga ulashni o'rganamiz.
