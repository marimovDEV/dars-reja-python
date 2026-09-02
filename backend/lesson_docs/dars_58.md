# 🗄 58. Django Models va ORM — Dars dokumentatsiyasi

**Django ORM** — ma'lumotlar bazasi jadvallarini Python sinflari (`models.Model`) ko'rinishida ta'riflash va obyektlar orqali SQL so'rovlarini bajarish imkonini beradi.

---

## Django Model va ORM So'rovlari

```python
# main/models.py
from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

# ORM CRUD So'rovlari:
# 1. Yaratish: Course.objects.create(title="Python", price=500000)
# 2. Olish: Course.objects.filter(price__gte=100000)
```

Keyingi **59-dars: Django Admin Panel va ModelAdmin Sozlamalari** da tayyor CMS panelni sozlashni o'rganamiz.
