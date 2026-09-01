# 🔗 47. Django ORM Munosabatlar (FK, M2M) — Dars dokumentatsiyasi

Django ORM jadvallar o'rtasidagi munosabatlarni klass atributlari orqali oson bog'lash imkonini beradi:
- **`ForeignKey`**: One-to-Many (Masalan: Kategoriya -> Mahsulotlar).
- **`ManyToManyField`**: Many-to-Many (Masalan: Maqola -> Teglar).
- **`OneToOneField`**: One-to-One (Masalan: User -> Profile).

---

# Model Munosabatlari Misoli

```python
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)

class Tag(models.Model):
    name = models.CharField(max_length=50)
    products = models.ManyToManyField(Product)
```

---

# 10. Qisqa xulosa

Bu darsda Django ORM dagi bog mezonlar (ForeignKey, ManyToManyField) o'rganildi.
