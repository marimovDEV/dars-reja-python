# ⚡ 45. Django ORM CRUD — Dars dokumentatsiyasi

**Django ORM (Object-Relational Mapper)** — bu SQL so'rovlarini noldan yozmasdan, Python kodlari (obyektlar) orqali ma'lumotlar bazasi bilan CRUD (Create, Read, Update, Delete) amallarini bajarish imkonini beruvchi vositadir.

---

# Django ORM CRUD Misollari

```python
from main.models import Product

# 1. Create (Qo'shish)
p = Product.objects.create(title="Noutbuk", price=8000000)

# 2. Read (O'qish va Filtrlash)
all_products = Product.objects.all()
cheap_products = Product.objects.filter(price__lt=5000000)
single_product = Product.objects.get(id=1)

# 3. Update (Yangilash)
p.price = 7500000
p.save()

# 4. Delete (O'chirish)
p.delete()
```

---

# 10. Qisqa xulosa

Bu darsda Django ORM orqali bazadagi ma'lumotlar ustida CRUD amallari bajarish o'rganildi.
