# 🗄️ 43. Django Models va Migrations — Dars dokumentatsiyasi

**Models (`models.py`)** — bu Django ORM ning eng muhim va markaziy qismidir. Model — bu ma'lumotlar bazasidagi jadvalning Python klassi ko'rinishidagi shaklidir. Model klassining har bir atributi jadvalning bir ustuniga (column) mos keladi.

**Migrations (Migratsiyalar)** — bu siz Python modelida qilgan o'zgarishlaringizni (yangi model qo'shish, ustun o'chirish yoki o'zgartirish) ma'lumotlar bazasidagi haqiqiy SQL so'rovlariga o'girib uzatuvchi mexanizmdir.

---

## Bu mavzu orqali nimalar qilish mumkin

- Python klassi yordamida ma'lumotlar bazasi jadvallarini yaratish;
- Har xil turdagi model maydonlarini (`CharField`, `IntegerField`, `DateTimeField`, `BooleanField`) qo'llash;
- `makemigrations` va `migrate` buyruqlari bilan bazani sinxronlash.

---

# Kod misoli — Models va Migrations

```python
# main/models.py
from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=200)
    price = models.DecimalField(max_max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
```

**Migratsiya Buyruqlari:**
```bash
# 1. Migratsiya faylini yaratish
python manage.py makemigrations

# 2. Bazaga tadbiq etish (SQL ni runs qilish)
python manage.py migrate
```

---

# 10. Qisqa xulosa

Bu darsda Django Models va Migratsiyalar mexanizmi o'rganildi.
