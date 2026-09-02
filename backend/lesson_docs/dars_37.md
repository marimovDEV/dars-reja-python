# 🤖 37. Telegram Bot va Aiogram 3.x Asoslari — Dars dokumentatsiyasi

Telegram Botlari bugungi kunda biznes, o'quv markazlar, internet-do'konlar va avtomatlashtirish tizimlarining ajralmas qismiga aylandi. Python dasturlash tilida Telegram bot yaratish uchun eng tezkor, zamonaviy va mukammal vosita **Aiogram 3.x** kutubxonasi hisoblanadi.

Ushbu dars davomida biz Telegram Bot API qanday ishlashini, BotFather yordamida bot yaratishni va Python'da `asyncio` hamda `Aiogram 3` yordamida asinxron botni ishga tushirishni noldan o'rganamiz.

---

## Bu mavzu orqali nimalar qilish mumkin

- BotFather orqali yangi Telegram Bot yaratish va API Token olish;
- Python'da `aiogram` kutubxonasini o'rnatish va sozlash;
- `Bot` va `Dispatcher` obyeqtlari bilan ishlash;
- `/start` va `/help` buyruqlariga javob beradigan asinxron handler yozish;
- Long Polling rejimida botni uzluksiz ishga tushirish.

---

## Dars maqsadi

Bu dars oxirida o'quvchi:

- Telegram Bot API va webhook/polling arxitekturasini tushunadi;
- BotFather orqali bot sozlamalarini boshqara oladi;
- `aiogram3` yordamida asinxron bot loyihasi kodi arxitekturasini qura oladi;
- Dastlabki `/start` buyrug'iga matnli va formatlangan javob qaytarishni mustaqil bajara oladi.

---

## Kerakli oldingi bilimlar

Bu darsni tushunish uchun:

- 1-12 darslar (Python asoslari va sintaksisi);
- 16-18 darslar (Funktsiyalar va modullar);
- 30-dars (Asinxron Python va `asyncio` tushunchasi)

bilinishi kerak.

---

## Asosiy tushunchalar va atamalar

## Telegram Bot API nima?

> **Telegram Bot API** — bu Telegram serverlari bilan HTTP/HTTPS protokoli orqali muloqot qilish imkonini beruvchi rasmiy interfeys.

## Aiogram 3.x nima?

> **Aiogram 3.x** — bu Python dasturlash tili uchun mo'ljallangan, to'liq asinxron (`asyncio`) va juda tezkor Telegram Bot frameworki.

## Dispatcher nima?

> **Dispatcher (dp)** — bu Telegram'dan kelayotgan barcha voqea va xabarlarni (updates) tegishli funksiyalar (handlerlar)ga yo'naltiruvchi markaziy marshrutizator.

## Bot Token nima?

> **Bot Token** — bu BotFather tomonidan beriladigan va Telegram Bot API bilan xavfsiz muloqot qilishni ta'minlaydigan maxsus maxfiy kalit.

---

## Sintaksis va uning izohi

```python
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

# 1. Bot va Dispatcher obyeqtlarini yaratish
bot = Bot(token="BOT_TOKENINGIZNI_YOZING")
dp = Dispatcher()

# 2. Command handler yaratish
@dp.message(Command("start"))
async def start_handler(message: types.Message):
    await message.answer("Assalomu alaykum! Aiogram 3 botiga xush kelibsiz!")

# 3. Asinxron asosiy funksiya
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
```

---

## Jadvallar

| Obyekt / Metod | Vazifasi | Parametrlari | Misol | Ko'p uchraydigan xatosi |
|---|---|---|---|---|
| `Bot(token)` | Bot obyektini yaratadi | `token`, `parse_mode` | `Bot(token=TOKEN)` | Tokenda bo'sh joy qoldirish |
| `Dispatcher()` | Voqealarni boshqaradi | Yo'q | `dp = Dispatcher()` | Bir nechta dp yaratish |
| `@dp.message()` | Xabarlarga ishlov beradi | `filters` | `@dp.message(Command('start'))` | `async` belgisini unutish |
| `message.answer()` | Xabarga javob qaytaradi | `text`, `parse_mode` | `await message.answer('Salom')` | `await` qo'ymaslik |
| `dp.start_polling()` | Botni ishga tushiradi | `bot` | `await dp.start_polling(bot)` | `asyncio.run()` siz chaqirish |

---

## Misollar

### Misol 1 — Aiogram 3 o'rnatish va token o'zgaruvchisi

```python
# Terminalda bajariladigan buyruq:
# pip install aiogram

import os

BOT_TOKEN = "123456789:ABCdefGHIjklMNOpqrsTUVwxyZ"
print("Aiogram 3 tayyor!")
```

### Misol 2 — Birinchi /start buyrug'i

```python
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

BOT_TOKEN = "123456789:ABCdefGHIjklMNOpqrsTUVwxyZ"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!")

async def main():
    print("Bot ishga tushdi...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
```

### Misol 3 — HTML formatlash bilan javob berish

```python
@dp.message(Command("info"))
async def cmd_info(message: types.Message):
    text = "<b>Aiogram 3 Bot</b>\n<i>Versiya: 3.x</i>\n<u>Muallif: Python Dasturchi</u>"
    await message.answer(text, parse_mode="HTML")
```

### Misol 4 — Eco Bot (Xabarni qayta yuborish)

```python
@dp.message()
async def echo_handler(message: types.Message):
    await message.answer(f"Siz yozdingiz: {message.text}")
```

---

## Real loyiha misoli

```python
import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart, Command

BOT_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN_HERE"

logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def command_start_handler(message: types.Message):
    user_name = message.from_user.first_name
    await message.answer(
        f"👋 Assalomu alaykum, <b>{user_name}</b>!\n\n"
        f"🤖 Bu sizning birinchi professional <b>Aiogram 3.x</b> botingiz.",
        parse_mode="HTML"
    )

@dp.message(Command("help"))
async def command_help_handler(message: types.Message):
    await message.answer(
        "🛠 <b>Mavjud buyruqlar:</b>\n"
        "/start - Botni ishga tushirish\n"
        "/help - Yordam oynasi",
        parse_mode="HTML"
    )

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
```

---

## Ko'p uchraydigan xatolar

## Xato 1: await kalit so'zini unutib qoldirish

Noto'g'ri:
```python
message.answer("Salom")  # Coroutine hech qachon bajarilmaydi!
```

To'g'ri:
```python
await message.answer("Salom")
```

---

## 3 darajali amaliy topshiriqlar

## 1-topshiriq — Oson
BotFather'dan yangi bot yaratib token oling va `/start` buyrug'iga foydalanuvchi ismini chiqaruvchi kod yozing.

## 2-topshiriq — O'rta
`/help` va `/about` buyruqlarini qo'shing va HTML teglari yordamida chiroyli formatlang.

## 3-topshiriq — Murakkab
Foydalanuvchi yuborgan har qanday matnli xabarni teskari tartibda qaytaruvchi asinxron bot tuzing.

---

## Uyga vazifa

1. `aiogram` va `python-dotenv` kutubxonalarini o'rnating;
2. `.env` faylida `BOT_TOKEN`ni xavfsiz saqlang;
3. `/start` buyrug'iga foydalanuvchining ID raqami va nikneymini qaytaruvchi bot yozing;
4. Noto'g'ri buyruq kiritilganda yordam matnini chiqaruvchi handler tayyorlang;
5. Botni konsolda xatoliklarsiz ishga tushiring.

---

## Test savollari

1. Aiogram 3.x nechani Python versiyasini va qanday arxitekturani talab qiladi?
2. BotFather'dan bot yaratganda qanday ma'lumot olinadi?
3. Aiogram'da voqealarni marshrutlash uchun qaysi obyekt javobgar?
4. `message.answer()` va `message.reply()` o'rtasidagi asosiy farq nima?
5. `asyncio.run()` funksiyasi nima vazifani bajaradi?

## Javoblar

**1.** Python 3.8+ va to'liq asinxron (`asyncio`) arxitekturani talab qiladi.
**2.** Bot username va Telegram Bot API bilan muloqot qilish uchun HTTP Token olinadi.
**3.** `Dispatcher` (va Router) obyekti xabarlar hamda hodisalarni tegishli handlerlarga yo'naltiradi.
**4.** `message.answer()` oddiy yangi xabar yuboradi, `message.reply()` esa foydalanuvchi xabariga javob (quote) sifatida yuboradi.
**5.** Asinxron hodisalar siklini (event loop) ishga tushiradi va asosiy coroutine'ni yakunlaydi.

---

## Qisqa xulosa

- Aiogram 3 — asinxron va zamonaviy Telegram Bot frameworki;
- `Bot` va `Dispatcher` botning asosiy o'zagini tashkil qiladi;
- Barcha handler funksiyalar `async def` bilan yozilishi va `await` orqali chaqirilishi shart.

Keyingi **38-dars: Aiogram Handlerlar va Message Filterlari** da Telegram xabarlarini filtrlash va matn, rasm hamda fayllarni ushlashni o'rganamiz.

---

## Qo'shimcha resurslar

- 📄 Rasmiy hujjat: https://docs.aiogram.dev/
- 📄 Telegram Bot API: https://core.telegram.org/bots/api
- 💻 Kodlar: `github.com/dars-reja/37-dars`
- 🎬 Video dars: `youtube.com/watch?v=aiogram37`
