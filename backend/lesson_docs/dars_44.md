# 👑 44. Django Admin Panel — Dars dokumentatsiyasi

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
