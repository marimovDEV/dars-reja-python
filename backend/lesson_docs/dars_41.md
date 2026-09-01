# 🧩 41. Django Apps va URLs — Dars dokumentatsiyasi

Django loyihalari kichik va mustaqil modullardan — **Apps (Ilovalar)** dan tashkil topadi. Masalan, e-commerce loyihasida `users`, `products`, `orders`, `blog` kabi alohida app'lar bo'ladi. Bu modulizm kodingizni toza va tartibli saqlashga xizmat qiladi.

**URLs (`urls.py`)** esa foydalanuvchi brauzerga kiritgan manzilni (URL) mos keluvchi mantig'iy funksiyaga (View) yo'naltirish (routing) vazifasini bajaradi.

---

# App Yaratish va Ulash

```bash
# Yangi App yaratish
python manage.py startapp main
```

**`settings.py` ichiga ulaymiz:**
```python
INSTALLED_APPS = [
    # ...
    'main',
]
```

**App ichida `urls.py` yaratib asosiy URLs ga ulaymiz (`include`):**
```python
# myproject/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
]
```

---

# 10. Qisqa xulosa

Bu darsda Django ilovalari (`apps`) va URL marshrutlash (`routing`) tushunchalari o'rganildi.
