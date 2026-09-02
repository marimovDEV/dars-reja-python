# 🏛 54. Django Apps va MVT Arxitekturasi — Dars dokumentatsiyasi

Django ilovalari **MVT (Model - View - Template)** arxitekturasiga tayanadi:
- **Model**: Ma'lumotlar bazasi strukturasi.
- **View**: Biznes mantiq va so'rovlarni qayta ishlash.
- **Template**: Foydalanuvchiga ko'rinadigan HTML sahifa.

---

## Django App va First View Misoli

```python
# 1. Terminalda ilova yaratish:
# python manage.py startapp main

# main/views.py
from django.shortcuts import render
from django.http import HttpResponse

def home_view(request):
    return HttpResponse("<h1>Django MVT Sahifasiga Xush Kelibsiz!</h1>")
```

Keyingi **55-dars: Django Templates (DTL)** da dynamic HTML sahifalar tayyorlashni o'rganamiz.
