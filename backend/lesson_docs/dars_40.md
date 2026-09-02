# 🖱 40. Callback Query va CallbackData Factory — Dars dokumentatsiyasi

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
