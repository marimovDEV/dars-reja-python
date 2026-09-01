# 🧪 65. Pytest va Unittest Kirish — Dars dokumentatsiyasi

Dastur hajmi kattalashgani sari, har bir yangi funksionallik qo'shilganda eski kodingiz buzilmaganligiga ishonch hosil qilish uchun qo'lda tekshirish imkonsiz bo'lib qoladi.

**Avtomatlashtirilgan Testlash (Automated Testing)** — bu kodning to'g'ri ishlayotganini avtomatik ravishda tekshiruvchi test ssenariylarini yozishdir.

Python'da **`unittest`** (standart kutubxona) va **`pytest`** (eng ommabop, qulay va kuchli freymvork) ishlatiladi.

---

# Kod misoli — Pytest va Unittest

```python
# 1. Unittest Misoli
import unittest

def add(a, b):
    return a + b

class TestMath(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)

# 2. Pytest Misoli (Qisqa va zamonaviy)
def test_addition():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
```

---

# 10. Qisqa xulosa

Bu darsda Unit Testing, `unittest` va `pytest` freymvorklari o'rganildi.
