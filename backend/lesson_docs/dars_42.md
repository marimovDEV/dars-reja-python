# 🗄 42. Botni Ma'lumotlar Bazasiga Ulash — Dars dokumentatsiyasi

Telegram bot foydalanuvchilari va ularning ma'lumotlarini qayta yuklanganda ham saqlab qolish uchun **aiosqlite** kabi asinxron ma'lumotlar bazasi kutubxonasi ishlatiladi.

---

## Misol — aiosqlite bilan ishlash

```python
import aiosqlite

async def init_db():
    async with aiosqlite.connect("bot_database.db") as db:
        await db.execute("""
            CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY,
                full_name TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
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
