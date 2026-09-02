import os
import sys
import django

# Setup Django Environment
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from lessons_app.models import Lesson

DOCS_DIR = os.path.join(os.path.dirname(__file__), "lesson_docs")
os.makedirs(DOCS_DIR, exist_ok=True)

LESSONS_MONTH_4 = [
    {
        "lesson_number": 37,
        "title": "37-dars — Telegram Bot va Aiogram 3.x Asoslari",
        "goal": "Telegram Bot API arxitekturasi, BotFather orqali Bot yaratish, Bot va Dispatcher obyektlari, Asynchronous Python (asyncio) bilan ishlash va birinchi /start komandasini ishga tushirish.",
        "description": "Aiogram 3.x kutubxonasi asosida asinxron Telegram botlarni noldan yaratish, BotFather orqali API Token olish va birinchi asinxron ishlovchini sozlash.",
        "content": """# 🤖 37. Telegram Bot va Aiogram 3.x Asoslari — Dars dokumentatsiyasi

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
    text = "<b>Aiogram 3 Bot</b>\\n<i>Versiya: 3.x</i>\\n<u>Muallif: Python Dasturchi</u>"
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
        f"👋 Assalomu alaykum, <b>{user_name}</b>!\\n\\n"
        f"🤖 Bu sizning birinchi professional <b>Aiogram 3.x</b> botingiz.",
        parse_mode="HTML"
    )

@dp.message(Command("help"))
async def command_help_handler(message: types.Message):
    await message.answer(
        "🛠 <b>Mavjud buyruqlar:</b>\\n"
        "/start - Botni ishga tushirish\\n"
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
"""
    },
    {
        "lesson_number": 38,
        "title": "38-dars — Aiogram Handlerlar va Message Filterlari",
        "goal": "Routerlar bilan kodni modullarga bo'lish, MagicFilter (F) yordamida matnlar, rasmlar, fayllar hamda stikerlarni filtrlash va ushlash.",
        "description": "Aiogram 3 da Router va Filterlar tushunchasi. Har xil turdagi kontentlarni (photo, video, document, text) ajratib olish va qayta ishlash.",
        "content": """# 🔍 38. Aiogram Handlerlar va Message Filterlari — Dars dokumentatsiyasi

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
"""
    },
    {
        "lesson_number": 39,
        "title": "39-dars — Reply va Inline Klaviaturalar bilan Ishlash",
        "goal": "ReplyKeyboardMarkup va InlineKeyboardMarkup obyeqtlari orqali foydalanuvchilar uchun qulay tugmali interfeys yaratish.",
        "description": "Telegram botlarda pasdki Reply tugmalar hamda xabar ostidagi Inline tugmalarni yaratish, ularni razmerlash (resize_keyboard) va ketma-ket joylashtirish.",
        "content": """# ⌨️ 39. Reply va Inline Klaviaturalar bilan Ishlash — Dars dokumentatsiyasi

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
"""
    },
    {
        "lesson_number": 40,
        "title": "40-dars — Callback Query va CallbackData Factory",
        "goal": "Inline tugmalar bosilganda CallbackQuery hodisasini ushlash, callback.answer() orqali bildirishnoma chiqarish va tipizatsiyalangan CallbackData yaratish.",
        "description": "Inline tugmalar bosilganda xabarni tahrirlash (edit_text), pop-up xabar chiqarish va CallbackData prefikslari orqali dinamik ma'lumotlar uzatish.",
        "content": """# 🖱 40. Callback Query va CallbackData Factory — Dars dokumentatsiyasi

Inline tugmalar bosilganda Telegram serverga xabar emas, balki **CallbackQuery** hodisasi yuboriladi. U bilan to'g'ri ishlash bot interfeysini dinamik va tezkor qiladi.

---

## Misol — Callback Query va CallbackData

```python
from aiogram import F, types
from aiogram.filters.callback_data import CallbackData

class CourseCallback(CallbackData, prefix="course"):
    course_id: int
    action: str

@dp.callback_query(CourseCallback.filter(F.action == "buy"))
async def buy_course(callback: types.CallbackQuery, callback_data: CourseCallback):
    await callback.answer("Buyurtma qabul qilindi!", show_alert=True)
    await callback.message.edit_text(f"Siz {callback_data.course_id}-IDli kursni tanladingiz.")
```

Keyingi **41-dars: FSM (Finite State Machine) va Form-Bosqichlar** da foydalanuvchilar bilan bosqichma-bosqich so'rovnoma o'tkazishni o'rganamiz.
"""
    },
    {
        "lesson_number": 41,
        "title": "41-dars — FSM (Finite State Machine) va Form-Bosqichlar",
        "goal": "Aiogram FSM (Finite State Machine) yordamida foydalanuvchidan ism, yosh, telefon raqami va ma'lumotlarni bosqichma-bosqich yig'ish.",
        "description": "StatesGroup, State, FSMContext obyektlari. Hodisalar ketma-ketligi, state.set_state(), state.update_data() va state.clear() metodlari.",
        "content": """# 📝 41. FSM (Finite State Machine) va Form-Bosqichlar — Dars dokumentatsiyasi

Foydalanuvchidan ro'yxatdan o'tish yoki buyurtma berishda bosqichma-bosqich ma'lumot yig'ish uchun **FSM (Chekli Avtomatlar Tizimi)** ishlatiladi.

---

## Misol — FSM So'rovnomasi

```python
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram import types, Router, F

class RegisterForm(StatesGroup):
    name = State()
    age = State()
    phone = State()

router = Router()

@router.message(F.text == "/register")
async def start_reg(message: types.Message, state: FSMContext):
    await state.set_state(RegisterForm.name)
    await message.answer("Ismingizni kiriting:")

@router.message(RegisterForm.name)
async def process_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(RegisterForm.age)
    await message.answer("Yoshingizni kiriting:")

@router.message(RegisterForm.age)
async def process_age(message: types.Message, state: FSMContext):
    data = await state.get_data()
    name = data.get("name")
    await message.answer(f"Rahmat! Ism: {name}, Yosh: {message.text}")
    await state.clear()
```

Keyingi **42-dars: Botni Ma'lumotlar Bazasiga Ulash (aiosqlite & SQLAlchemy)** da yig'ilgan ma'lumotlarni bazada saqlashni o'rganamiz.
"""
    },
    {
        "lesson_number": 42,
        "title": "42-dars — Botni Ma'lumotlar Bazasiga Ulash (aiosqlite & SQLAlchemy)",
        "goal": "Aiogram botni aiosqlite yoki SQLAlchemy asinxron ORM orqali SQLite/PostgreSQL bazalariga ulash hamda foydalanuvchilar bazasini tuzish.",
        "description": "Asinxron ma'lumotlar bazasi so'rovlari. Users jadvalini yaratish, yangi foydalanuvchini bazaga qo'shish va takroriy kirishlarni tekshirish.",
        "content": """# 🗄 42. Botni Ma'lumotlar Bazasiga Ulash — Dars dokumentatsiyasi

Telegram bot foydalanuvchilari va ularning ma'lumotlarini qayta yuklanganda ham saqlab qolish uchun **aiosqlite** kabi asinxron ma'lumotlar bazasi kutubxonasi ishlatiladi.

---

## Misol — aiosqlite bilan ishlash

```python
import aiosqlite

async def init_db():
    async with aiosqlite.connect("bot_database.db") as db:
        await db.execute(\"\"\"
            CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY,
                full_name TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        \"\"\")
        await db.commit()

async def add_user(user_id: int, full_name: str):
    async with aiosqlite.connect("bot_database.db") as db:
        await db.execute(
            "INSERT OR IGNORE INTO users (user_id, full_name) VALUES (?, ?)",
            (user_id, full_name)
        )
        await db.commit()
```

Keyingi **43-dars: Aiogram Middleware va Majburiy Obuna Tekshiruvi** da barcha xabarlar oldidan tekshiruvlarni joylashtirishni o'rganamiz.
"""
    },
    {
        "lesson_number": 43,
        "title": "43-dars — Aiogram Middleware va Majburiy Obuna Tekshiruvi",
        "goal": "BaseMiddleware sinfidan foydalanib xabarlarni qamrab oluvchi va majburiy Telegram kanaliga obunani tekshiruvchi middleware yaratish.",
        "description": "Outer va Inner middleware. Botga yozgan foydalanuvchining ma'lum bir kanalga obuna bo'lganligini bot.get_chat_member() orqali avtomatik tekshirish va kirishni cheklash.",
        "content": """# 🛡 43. Aiogram Middleware va Majburiy Obuna Tekshiruvi — Dars dokumentatsiyasi

**Middleware** — kelayotgan xabarlar handlerlarga yetib bormasdan oldin ularni ushlab, tekshiruvdan o'tkazuvchi oraliq qatlamdir. U yordamida kanalga obunani tekshirish, foydalanuvchini bloklash yoki log yozish mumkin.

---

## Misol — Majburiy Kanal Obunasini Tekshirish Middleware

```python
from aiogram import BaseMiddleware
from aiogram.types import Message
from typing import Callable, Dict, Any

CHANNEL_ID = "@my_telegram_channel"

class CheckSubMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[Message, Dict[str, Any]], Any],
        event: Message,
        data: Dict[str, Any]
    ) -> Any:
        bot = data["bot"]
        member = await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=event.from_user.id)
        if member.status in ["left", "kicked"]:
            await event.answer(f"Botdan foydalanish uchun {CHANNEL_ID} kanaliga obuna bo'ling!")
            return
        return await handler(event, data)
```

Keyingi **44-dars: Bot Admin Paneli va Xabarlar Tarqatish (Broadcasting)** da admin funksiyalarini yaratishni o'rganamiz.
"""
    },
    {
        "lesson_number": 44,
        "title": "44-dars — Bot Admin Paneli va Xabarlar Tarqatish (Broadcasting)",
        "goal": "Bot adminlari uchun maxsus boshqaruv paneli, foydalanuvchilar statistikasini ko'rish hamda barchaga ommaviy xabar yuborish (broadcasting) tizimini yaratish.",
        "description": "IsAdmin filteri, copy_message() metodi yordamida barcha foydalanuvchilarga reklama xabarlarini asinxron siklda xatoliklarni ushlab tarqatish.",
        "content": """# ⚙️ 44. Bot Admin Paneli va Xabarlar Tarqatish — Dars dokumentatsiyasi

Bot egasi va adminlari uchun foydalanuvchilar soni statistikasini ko'rish hamda bazadagi barcha foydalanuvchilarga bildirishnoma tarqatish funksiyasi zarur.

---

## Misol — Xabar Tarqatish (Broadcasting)

```python
from aiogram import Router, F, types, Bot
from aiogram.filters import Command

router = Router()
ADMIN_IDS = [123456789]

@router.message(Command("broadcast"), F.from_user.id.in_(ADMIN_IDS))
async def start_broadcast(message: types.Message, bot: Bot):
    # Nazariy barcha user_id larni bazadan olish
    user_ids = [123456789, 987654321]
    success = 0

    for u_id in user_ids:
        try:
            await bot.send_message(chat_id=u_id, text="📢 Admin e'loni: Yangi darslar joylandi!")
            success += 1
        except Exception:
            pass

    await message.answer(f"Xabar {success} ta foydalanuvchiga muvaffaqiyatli yetkazildi.")
```

Keyingi **45-dars: Media, Fayllar, Lokatsiya va Kontakt Yuborish** da turli fayllar va geografik joylashuvlar bilan ishlashni o'rganamiz.
"""
    },
    {
        "lesson_number": 45,
        "title": "45-dars — Media, Fayllar, Lokatsiya va Kontakt Yuborish",
        "goal": "Telegram Bot orqali Audio, Video, Kruglyash (VideoNote), Hujjatlar, Foydalanuvchi Lokatsiyasi va Telefon kontaktini so'rash hamda ishlov berish.",
        "description": "request_contact, request_location tugmalari, InputFile obyekti va Telegram file_id orqali fayllarni tezkor qayta yuborish mexanizmlari.",
        "content": """# 📁 45. Media, Fayllar, Lokatsiya va Kontakt Yuborish — Dars dokumentatsiyasi

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
"""
    },
    {
        "lesson_number": 46,
        "title": "46-dars — Telegram Web App (Mini Apps) Integratsiyasi",
        "goal": "Telegram Web App (Mini Apps) tugmalarini ulash, bot ichida HTML5/React sahifalarni ochish hamda web_app_data orqali ma'lumot almashish.",
        "description": "WebAppInfo obyekti. Mini App interfeysini ulash, foydalanuvchi savatchasini (Cart) WebApp'da yig'ish va Telegram botga qaytarib topshirish.",
        "content": """# 🌐 46. Telegram Web App (Mini Apps) Integratsiyasi — Dars dokumentatsiyasi

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
"""
    },
    {
        "lesson_number": 47,
        "title": "47-dars — Webhook Integratsiyasi va Serverga Deploy Qilish",
        "goal": "Long Polling va Webhook farqi, SSL sertifikati bilan Webhook o'rnatish, FastAPI/Aiohttp integratsiyasi va Linux VPS serverda Systemd orqali botni 24/7 ishlatish.",
        "description": "Botni Linux (Ubuntu/Debian) serverlariga joylashtirish. Systemd service faylini yaratish, bot avtomatik qayta yoqilishi (restart) hamda xavfsizlik sozlamalari.",
        "content": """# 🚀 47. Webhook Integratsiyasi va Serverga Deploy Qilish — Dars dokumentatsiyasi

Botni sinovdan o'tkazgach, uni kompyuter o'chiq bo'lsa ham 24/7 ishlashi uchun **VPS Serverga (Linux)** joylashtirish va **Systemd Service** sifatida sozlash kerak.

---

## Linux Systemd Service Fayli Misoli (/etc/systemd/system/mybot.service)

```ini
[Unit]
Description=Aiogram 3 Telegram Bot Service
After=network.target

[Service]
User=root
WorkingDirectory=/root/mybot
ExecStart=/root/mybot/venv/bin/python main.py
Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target
```

Keyingi **48-dars: 4-Modul Imtihoni va To'liq Aiogram Bot Loyihasi** da 12 ta darsda o'rganilgan bilimlar bo'yicha yakuniy loyihani bajaramiz.
"""
    },
    {
        "lesson_number": 48,
        "title": "48-dars — 4-Modul Imtihoni va To'liq Aiogram Bot Loyihasi",
        "goal": "4-modul davomida o'rganilgan Aiogram 3, FSM, Keyboards, SQLite database, Middleware va Admin panel bilimlarini sinovdan o'tkazuvchi to'liq amaliy imtihon loyihasini yaratish.",
        "description": "Kompleks Telegram Bot loyihasi: Onlayn Do'kon / Kurslarga Yozilish boti. Foydalanuvchilar ro'yxati, FSM so'rovnoma, savat, admin paneli va statistika.",
        "content": """# 🎓 48. 4-Modul Imtihoni va To'liq Aiogram Bot Loyihasi — Dars dokumentatsiyasi

Ushbu imtihon 37-darsdan 47-darsgacha o'rganilgan **Aiogram 3.x Telegram Bot dasturlash** ko'nikmalarini amalda sinash uchun o'tkaziladi.

---

## Imtihon Topshirig'i: "To'liq Funksional Onlayn Buyurtma Boti"

### Talablar:
1. `/start` bosilganda foydalanuvchini bazaga saqlash hamda Asosiy Menuni chiqarish;
2. **FSM Form**: Yangi foydalanuvchilardan Ism va Telefon raqamini so'rab saqlash;
3. **Katalog & Inline Keyboard**: Mahsulotlar ro'yxatini Inline tugmalar bilan chiqarish;
4. **Middleware**: Faqat rasmiy Telegram kanaliga obuna bo'lgan foydalanuvchilarga botdan foydalanishga ruxsat berish;
5. **Admin Panel**: Admin uchun foydalanuvchilar soni va e'lon yuborish (Broadcasting) funksiyasini yozish.

Muvaffaqiyatlar va omad yor bo'lsin!
"""
    }
]

def main():
    print("🚀 4-OY (37-48 DARSLAR) AIOGRAM TELEGRAM BOT CURRICULUM UPDATE STARTING...")
    
    for item in LESSONS_MONTH_4:
        num = item["lesson_number"]
        filename = f"dars_{num:02d}.md"
        filepath = os.path.join(DOCS_DIR, filename)

        # 1. Write Markdown File
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(item["content"])

        # 2. Update DB Lesson object
        lesson_obj, created = Lesson.objects.update_or_create(
            lesson_number=num,
            defaults={
                "lesson_id": f"les-100unique-{num}",
                "title": item["title"],
                "goal": item["goal"],
                "description": item["description"],
                "content": item["content"],
                "status": "planned" if num > 37 else "current",
                "homework": f"{item['title']} bo'yicha amaliy topshiriqlarni bajarish va kodingizni GitHub'ga joylash."
            }
        )
        status_str = "Created" if created else "Updated"
        print(f"✅ [{status_str}] Lesson {num}: {item['title']}")

    print("✨ MONTH 4 AIOGRAM TELEGRAM BOT CURRICULUM UPDATED SUCCESSFULLY IN DB AND DISK!")

if __name__ == "__main__":
    main()
