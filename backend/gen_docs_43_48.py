#!/usr/bin/env python3
"""Generate lesson docs 43-48 (Django continuation and Module 4 Exam)."""
import os

DOCS_DIR = os.path.join(os.path.dirname(__file__), "lesson_docs")

lessons = {}

# 43-DARS
lessons[43] = """# 🗄️ 43. Django Models va Migrations — Dars dokumentatsiyasi

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
"""

# 44-DARS
lessons[44] = """# 👑 44. Django Admin Panel — Dars dokumentatsiyasi

Django ning eng kuchli afzalliklaridan biri — bu tayyor, avtomatik yaratiluvchi va xavfsiz **Admin Panel**ining mavjudligidir. Admin panel ma'lumotlar bazasidagi ma'lumotlarni grafik interfeys (GUI) orqali boshqarish imkonini beradi.

Admin panelga kirish uchun **Superuser (Super-foydalanuvchi)** yaratiladi va modellarni `admin.py` faylida ro'yxatdan o'tkaziladi.

---

# Admin Paneldan Foydalanish

```bash
# Superuser yaratish
python manage.py createsuperuser
```

**Modellarni `admin.py` da ro'yxatdan o'tkazish:**
```python
# main/admin.py
from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'created_at')
    search_fields = ('title',)
```

---

# 10. Qisqa xulosa

Bu darsda Django Admin Paneli va modellarni boshqarish o'rganildi.
"""

# 45-DARS
lessons[45] = """# ⚡ 45. Django ORM CRUD — Dars dokumentatsiyasi

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
"""

# 46-DARS
lessons[46] = """# 📝 46. Django Forms va ModelForms — Dars dokumentatsiyasi

Foydalanuvchilar tomonidan kiritilgan ma'lumotlarni HTML formalari orqali qabul qilish, ularni xavfsizlik (XSS, CSRF) bo'yicha tekshirish va bazaga saqlash uchun Django **Forms va ModelForms** mexanizmlaridan foydalanadi.

---

# ModelForm Misoli

```python
# main/forms.py
from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'price']
```

**View ichida ishlatilishi:**
```python
def add_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save() # Bazaga saqlaydi
```

---

# 10. Qisqa xulosa

Bu darsda Django Forms, ModelForms va ma'lumotlar validatsiyasi o'rganildi.
"""

# 47-DARS
lessons[47] = """# 🔗 47. Django ORM Munosabatlar (FK, M2M) — Dars dokumentatsiyasi

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
"""

# 48-DARS
lessons[48] = """# 🎓 48. 4-modul imtihoni — Dars dokumentatsiyasi

4-modul imtihoni — HTTP, REST API, Git, GitHub, `venv`, `pip` va **Django Backend Freymvorki** (MVT, URLs, Views, Templates, Models, Admin, ORM CRUD, Forms, Relationships) bo'yicha to'liq bilimlarni sinaydi.

---

# Imtihon Topshiriqlari

1. **Django App va Models**: `Blog` nomli ilova yaratib, `Post` va `Comment` (ForeignKey) mezonlarini tuzing va migratsiya qiling.
2. **Admin & ORM**: Modelni admin panelga qo'shing va ORM orqali 5 ta post qo'shib, filter so'rovi yozing.
3. **Views & Forms**: Post qo'shish uchun `ModelForm` va u bilan ishlovchi `create_post` ko'rinishini (View) yarating.

---

# 10. Qisqa xulosa

Ushbu imtihon Django backend freymvorkining asosiy qismini yakunlaydi.
"""

for num, content in lessons.items():
    filepath = os.path.join(DOCS_DIR, f"dars_{num:02d}.md")
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"dars_{num:02d}.md yaratildi: {len(content)} belgi")
