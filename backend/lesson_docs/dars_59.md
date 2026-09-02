# ⚙️ 59. Django Admin Panel — Dars dokumentatsiyasi

Django avtomatik tarzda ma'lumotlarni tahrirlash va ko'rish uchun tayyor **Admin Panel** beradi.

---

## admin.py Sozlamasi

```python
from django.contrib import admin
from .models import Course

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'created_at')
    search_fields = ('title',)
    list_filter = ('created_at',)
```

Keyingi **60-dars: 5-Modul Imtihoni va Full-Stack Web Sayt Loyihasi** da o'rganilgan barcha bilimlarni bitta loyihaga birlashtiramiz.
