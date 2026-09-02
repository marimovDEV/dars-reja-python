# 🛡 43. Aiogram Middleware va Majburiy Obuna Tekshiruvi — Dars dokumentatsiyasi

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
