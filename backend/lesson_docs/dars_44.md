# ⚙️ 44. Bot Admin Paneli va Xabarlar Tarqatish — Dars dokumentatsiyasi

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
