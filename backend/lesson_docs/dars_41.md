# 📝 41. FSM (Finite State Machine) va Form-Bosqichlar — Dars dokumentatsiyasi

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
