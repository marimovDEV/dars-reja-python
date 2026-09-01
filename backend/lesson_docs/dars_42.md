# 🖼️ 42. Django Views va Templates — Dars dokumentatsiyasi

**Views (`views.py`)** — bu foydalanuvchining so'rovini (`HttpRequest`) qabul qilib, kerakli mantiqiy amallarni bajaruvchi hamda javob (`HttpResponse` yoki HTML Template) qaytaruvchi funksiya yoki klassdir.

**Templates** — bu ma'lumotlarni foydalanuvchiga HTML shaklida ko'rsatish uchun mo'ljallangan va Django Template Language (DTL) bilan boyitilgan shablonlar papkasidir.

---

# Kod misoli — Views va Template

```python
# main/views.py
from django.shortcuts import render
from django.http import HttpResponse

def home_page(request):
    context = {"title": "Bosh Sahifa", "user_name": "Ali"}
    return render(request, "main/home.html", context)
```

**DTL (Django Template Language) HTML ichida:**
```html
<!-- main/templates/main/home.html -->
<h1>Xush kelibsiz, {{ user_name }}!</h1>
```

---

# 10. Qisqa xulosa

Bu darsda Django Views va HTML Templates (DTL) mexanizmi o'rganildi.
