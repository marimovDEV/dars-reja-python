# 🟢 40. Django Kirish va Loyiha Strukturasi — Dars dokumentatsiyasi

**Django** — bu Python tilida yozilgan, "tayyor batareyalarga ega" (batteries-included), yuqori darajali eng mashhur Web Freymvorkdir. U tezkor, xavfsiz va kengayuvchan (scalable) backend tizimlar va veb-saytlar yaratish uchun ishlatiladi.

Django **MVT (Model-View-Template)** me'moriy namunasiga asoslangan.

Ushbu darsda siz Django freymvorkini o'rnatish, yangi loyiha yaratish (`django-admin startproject`) va loyihaning standart fayllar strukturasi bilan tanishasiz.

---

## Django Loyiha Fayllar Strukturasi

- **`manage.py`**: Loyihani boshqarish (serverni runs qilish, migratsiyalar) buyruqlari skripti.
- **`settings.py`**: Loyihaning barcha asosiy sozlamalari (baza, o'rnatilgan ilovalar, vaqt zonasi).
- **`urls.py`**: Saytning URL manzil (routing) xaritasi.
- **`wsgi.py` / `asgi.py`**: Web-serverlar bilan ishlash uchun interfeys fayllari.

---

# Birinchi Loyihani Yaratish

```bash
# 1. Django o'rnatish
pip install django

# 2. Loyiha yaratish
django-admin startproject myproject .

# 3. Development Serverni ishga tushirish
python manage.py runserver
```

---

# 10. Qisqa xulosa

Bu darsda Django freymvorki, MVT arxitekturasi va loyihani ishga tushirish o'rganildi.
