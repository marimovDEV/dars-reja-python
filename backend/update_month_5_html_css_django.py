import os
import sys
import django

# Setup Django Environment
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from lessons_app.models import Lesson

DOCS_DIR = os.path.join(os.path.dirname(__file__), "lesson_docs")
os.makedirs(DOCS_DIR, exist_ok=True)

LESSONS_MONTH_5 = [
    {
        "lesson_number": 49,
        "title": "49-dars — HTML5 Asoslari va Semantik Teglar",
        "goal": "Veb sahifalarning strukturasi, HTML5 semantik teglari (header, nav, main, section, footer), forma va kirish inputlarini yaratish.",
        "description": "Frontend dasturlashning asosi bo'lgan HTML5 teglari. Veb sahifa skeletini qurish, sarlavhalar, paragraflar, jadvallar va formalarni to'g'ri shakllantirish.",
        "content": """# 🌐 49. HTML5 Asoslari va Semantik Teglar — Dars dokumentatsiyasi

Veb ilovalar va saytlarning ko'rinishi hamda strukturasi **HTML5 (HyperText Markup Language)** yordamida hosil qilinadi. Har bir backend dasturchi Django yoki boshqa freymvorklarda ishlashdan oldin frontendning asosiy skeletini mukammal tushunishi shart.

---

## Bu mavzu orqali nimalar qilish mumkin

- Veb sahifa tayanch HTML strukturasi (`<!DOCTYPE html>`, `<html>`, `<head>`, `<body>`) ni tuzish;
- Semantik teglar (`<header>`, `<nav>`, `<main>`, `<article>`, `<aside>`, `<footer>`) bilan ishlash;
- Matnlar, sarlavhalar (`<h1>`-`<h6>`), ro'yxatlar (`<ul>`, `<ol>`) va havolalar (`<a>`) yaratish;
- HTML formalari (`<form>`, `<input>`, `<select>`, `<button>`) orqali foydalanuvchidan ma'lumot qabul qilish.

---

## Asosiy HTML5 Teglar

```html
<!DOCTYPE html>
<html lang="uz">
<head>
    <meta charset="UTF-8">
    <title>Mening Birinchi Veb Saytim</title>
</head>
<body>
    <header>
        <h1>Veb Dasturlash Kursi</h1>
        <nav>
            <a href="#home">Bosh sahifa</a> |
            <a href="#about">Biz haqimizda</a>
        </nav>
    </header>

    <main>
        <section>
            <h2>HTML5 Nima?</h2>
            <p>HTML — bu veb sahifalarning strukturaviy karkasidir.</p>
        </section>

        <section>
            <h2>Ro'yxatdan O'tish Formasi</h2>
            <form action="/submit" method="POST">
                <label for="username">Ismingiz:</label>
                <input type="text" id="username" name="username" required>
                <button type="submit">Yuborish</button>
            </form>
        </section>
    </main>

    <footer>
        <p>© 2026 MarimovDev. Barcha huquqlar himoyalangan.</p>
    </footer>
</body>
</html>
```

Keyingi **50-dars: CSS3 Styling, Flexbox va Grid Layout** da saytga chiroyli visual bezak berishni o'rganamiz.
"""
    },
    {
        "lesson_number": 50,
        "title": "50-dars — CSS3 Styling, Flexbox va Grid Layout",
        "goal": "CSS3 stil berish qoidalari, Selektorlar, Box Model, Flexbox va CSS Grid yordamida elementlarni moslashuvchan va chiroyli joylashtirish.",
        "description": "Veb sahifalarni bezash, ranglar, shriftlar, margin/padding o'lchamlari va Flexbox/Grid texnologiyalari orqali zamonaviy dizayn yaratish.",
        "content": """# 🎨 50. CSS3 Styling, Flexbox va Grid Layout — Dars dokumentatsiyasi

**CSS3 (Cascading Style Sheets)** — bu HTML teglarga ko'rinish, rang, shrift va joylashuv tartibini (layout) berish uchun ishlatiladigan uslublar tilidir.

---

## Asosiy CSS va Flexbox Misoli

```css
/* Asosiy uslublar */
body {
    font-family: 'Inter', sans-serif;
    background-color: #f8fafc;
    color: #0f172a;
    margin: 0;
    padding: 0;
}

/* Flexbox Konteyner */
.card-container {
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 20px;
    padding: 40px;
}

.card {
    background: #ffffff;
    border-radius: 12px;
    padding: 24px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
    flex: 1;
}
```

Keyingi **51-dars: Bootstrap 5 Framework** da tayyor dizayn komponentlari bilan ishlashni o'rganamiz.
"""
    },
    {
        "lesson_number": 51,
        "title": "51-dars — Bootstrap 5 Framework va Tayyor Komponentlar",
        "goal": "Bootstrap 5 CSS freymvorkini CDN orqali ulash, Grid tizimi (container, row, col), Navbar, Cards, Modals va Buttons komponentlaridan foydalanish.",
        "description": "Tezkor va zamonaviy frontend yaratish uchun eng ommabop Bootstrap 5 freymvorki. Tayyor klasslar yordamida 10 barobar tezroq veb sahifa yig'ish.",
        "content": """# 🚀 51. Bootstrap 5 Framework — Dars dokumentatsiyasi

**Bootstrap 5** — bu tezkor va moslashuvchan (responsive) veb saytlar yaratish uchun eng ommabop tayyor CSS va JS freymvorkidir.

---

## Bootstrap 5 CDN va HTML Strukturasi

```html
<!DOCTYPE html>
<html lang="uz">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bootstrap 5 Sayt</title>
    <!-- Bootstrap 5 CSS CDN -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
    <div class="container my-5">
        <div class="row g-4">
            <div class="col-md-6">
                <div class="card shadow-sm border-0 p-4">
                    <h3 class="text-primary font-bold">Python Backend</h3>
                    <p class="text-muted">Bootstrap 5 grid tizimi orqali tayyorlangan karta.</p>
                    <button class="btn btn-primary w-100">Batafsil</button>
                </div>
            </div>
        </div>
    </div>
</body>
</html>
```

Keyingi **52-dars: Responsive Web Design va Frontend Loyiha** da mobil qurilmalarga mos sayt yig'ishni o'rganamiz.
"""
    },
    {
        "lesson_number": 52,
        "title": "52-dars — Responsive Web Design va Mobile Layout",
        "goal": "Media queries (@media), mobile-first tamoyili va Bootstrap responsive sinflari orqali barcha qurilmalarga mos sayt yaratish.",
        "description": "Smartfon, planshet va kompyuter ekranlariga birdek moslashuvchi zamonaviy Responsive Frontend loyihasini yakunlash va Django'ga tayyorlash.",
        "content": """# 📱 52. Responsive Web Design va Mobile Layout — Dars dokumentatsiyasi

Mobil moslashuvchanlik (**Responsive Design**) — foydalanuvchi qaysi qurilmadan kirmasin (telefon, planshet yoki monitor) sayt ko'rinishining qulay saqlanishidir.

---

## CSS Media Queries Misoli

```css
/* Mobil qurilmalar uchun (max-width: 768px) */
@media (max-width: 768px) {
    .sidebar {
        display: none;
    }
    .main-content {
        width: 100%;
        padding: 15px;
    }
}
```

Keyingi **53-dars: Django Frameworkga Kirish** da ushbu HTML/CSS shablonlarni Django freymvorkiga ulashni boshlaymiz.
"""
    },
    {
        "lesson_number": 53,
        "title": "53-dars — Django Frameworkga Kirish va Loyiha Strukturasi",
        "goal": "Django freymvorki, django-admin startproject, manage.py buyruqlari, settings.py sozlamalari hamda serverni runserver orqali yoqish.",
        "description": "Python'dagi eng kuchli Full-Stack va REST API freymvorki bo'lgan Django bilan tanishuv. Loyiha papkalari strukturasi va dastlabki server diagnostikasi.",
        "content": """# ⚙️ 53. Django Frameworkga Kirish — Dars dokumentatsiyasi

**Django** — bu Python dasturlash tilida yozilgan, "batteries-included" (barcha imkoniyatlari tayyor) tamoyiliga asoslangan eng kuchli va xavfsiz veb freymvorkdir.

---

## Django Loyihasini Yaratish Buyruqlari

```bash
# 1. Virtual muhit yaratish va faollashtirish
python -m venv venv
source venv/bin/activate  # Linux/Mac

# 2. Django o'rnatish
pip install django

# 3. Yangi Django loyihasi yaratish
django-admin startproject config .

# 4. Serverni ishga tushirish
python manage.py runserver
```

Keyingi **54-dars: Django Apps, MVT Arxitekturasi va First View** da Django ilovalari va sahifa ko'rinishlarini o'rganamiz.
"""
    },
    {
        "lesson_number": 54,
        "title": "54-dars — Django Apps va MVT (Model-View-Template) Arxitekturasi",
        "goal": "Django MVT (Model-View-Template) modeli, python manage.py startapp orqali ilovalar yaratish va urls.py hamda views.py muloqoti.",
        "description": "Django ilovalarini modulli tashkil etish. Function-Based Views (FBV) yordamida birinchi HTTP so'rovlariga javob qaytarish.",
        "content": """# 🏛 54. Django Apps va MVT Arxitekturasi — Dars dokumentatsiyasi

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
"""
    },
    {
        "lesson_number": 55,
        "title": "55-dars — Django Templates (DTL), Variable va Filterlar",
        "goal": "Django Template Language (DTL), HTML fayllarga ma'lumot uzatish, {{ variable }}, {% if %}, {% for %} sikllari hamda Template Inheritance ({% extends %}).",
        "description": "Dinamik HTML sahifalar yaratish. Asosiy `base.html` shablonidan barcha ichki sahifalarga meros olish va kod takrorlanishining oldini olish.",
        "content": """# 📝 55. Django Templates (DTL) — Dars dokumentatsiyasi

**Django Template Language (DTL)** — Python ma'lumotlarini HTML sahifalar ichida dinamik render qilish va sikllar hamda shartlarni ishlatish imkonini beradi.

---

## DTL Shablon Merosxo'rligi (base.html va index.html)

```html
<!-- templates/base.html -->
<!DOCTYPE html>
<html lang="uz">
<head>
    <title>{% block title %}Mening Saytim{% endblock %}</title>
</head>
<body>
    <header><h1>MarimovDev Portal</h1></header>
    <main>
        {% block content %}{% endblock %}
    </main>
</body>
</html>

<!-- templates/index.html -->
{% extends 'base.html' %}

{% block content %}
<h2>Darslar Ro'yxati</h2>
<ul>
    {% for course in courses %}
        <li>{{ course.name }} - <b>{{ course.price }} so'm</b></li>
    {% endfor %}
</ul>
{% endblock %}
```

Keyingi **56-dars: Django Static Files & Media** da CSS va rasmlarni ulanishini o'rganamiz.
"""
    },
    {
        "lesson_number": 56,
        "title": "56-dars — Django Static Files & Media Fayllar bilan Ishlash",
        "goal": "STATIC_URL, STATICFILES_DIRS, MEDIA_URL, MEDIA_ROOT sozlamalari, HTML shablonlarga {% load static %} orqali CSS va rasmlarni ulash.",
        "description": "Django loyihada statik CSS/JS fayllarni va foydalanuvchilar tomonidan yuklanadigan rasm hamda fayllarni (Media) to'g'ri joylashtirish.",
        "content": """# 🖼 56. Django Static Files & Media Fayllar — Dars dokumentatsiyasi

Django loyihalarda CSS, JavaScript va fayllar **Static**, foydalanuvchilar yuklaydigan rasmlar esa **Media** fayllar deb yuritiladi.

---

## settings.py Sozlamalari

```python
# Static files (CSS, JavaScript, Images)
STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static']

# Media files (Foydalanuvchi rasmlari)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

Keyingi **57-dars: Django Forms va Validatsiya** da formalarni tekshirishni o'rganamiz.
"""
    },
    {
        "lesson_number": 57,
        "title": "57-dars — Django Forms, CSRF Token va Validatsiya",
        "goal": "Django Forms (forms.Form, forms.ModelForm), {% csrf_token %} xavfsizlik kaliti, form.is_valid() va xatoliklar validatsiyasi.",
        "description": "Foydalanuvchilardan ma'lumotlarni xavfsiz qabul qilish. CSRF hujumlaridan himoyalanish hamda kiritilgan ma'lumotlarni serverda tekshirish.",
        "content": """# 🔐 57. Django Forms va Validatsiya — Dars dokumentatsiyasi

Django formalari ma'lumotlarni qabul qilish, tozalash (sanitize) va bazaga saqlashdan oldin xatoliklarni tekshirishni (validation) avtomatlashtiradi.

---

## Django ModelForm Misoli

```python
# main/forms.py
from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['full_name', 'email', 'phone']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }
```

Keyingi **58-dars: Django Models, Migrations va ORM So'rovlari** da bazalar bilan ishlashni o'rganamiz.
"""
    },
    {
        "lesson_number": 58,
        "title": "58-dars — Django Models, Migrations va ORM So'rovlari",
        "goal": "models.Model sinfi, Field turlari (CharField, IntegerField, ForeignKey), makemigrations, migrate buyruqlari hamda ORM CRUD amallari.",
        "description": "Django ORM (Object-Relational Mapping) orqali SQL yozmasdan ma'lumotlar bazasi jadvallarini boshqarish va qidiruv so'rovlarini bajarish.",
        "content": """# 🗄 58. Django Models va ORM — Dars dokumentatsiyasi

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
"""
    },
    {
        "lesson_number": 59,
        "title": "59-dars — Django Admin Panel va ModelAdmin Sozlamalari",
        "goal": "python manage.py createsuperuser, admin.py faylida modellarni ro'yxatdan o'tkazish, list_display, search_fields va list_filter sozlamalari.",
        "description": "Django'ning eng mashhur xususiyati — tayyor Admin Panel (CMS). Sayt administratorlari uchun qulay boshqaruv interfeysini sozlash.",
        "content": """# ⚙️ 59. Django Admin Panel — Dars dokumentatsiyasi

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
"""
    },
    {
        "lesson_number": 60,
        "title": "60-dars — 5-Modul Imtihoni va Full-Stack Web Sayt Loyihasi",
        "goal": "HTML5/CSS3/Bootstrap 5 frontend shablonlarini Django MVT, Models, Forms va Admin paneliga to'liq integratsiya qilib, mukammal veb sayt loyihasini topshirish.",
        "description": "5-modul bo'yicha amaliy imtihon: Onlayn Kurslar / Yangiliklar Portali Full-Stack veb ilovasi loyihasini noldan muvaffaqiyatli yakunlash.",
        "content": """# 🎓 60. 5-Modul Imtihoni va Full-Stack Web Sayt — Dars dokumentatsiyasi

Ushbu imtihon 49-darsdan 59-darsgacha o'rganilgan **HTML, CSS, Bootstrap 5 va Django MVT Full-Stack Web Dasturlash** ko'nikmalarini amalda sinash uchun o'tkaziladi.

---

## Imtihon Loyihasi: "Dinamik Full-Stack Portal"

### Talablar:
1. **Frontend**: Bootstrap 5 va HTML5/CSS3 yordamida moslashuvchan (responsive) `base.html`, `index.html` va `detail.html` sahifalarini tuzish;
2. **Django MVT**: Barcha static fayllar va shablonlarni DTL orqali integratsiya qilish;
3. **Database & ORM**: Obyektlar uchun Django Model va Migrations tayyorlash;
4. **Forms**: Foydalanuvchilar so'rov qoldirishi uchun Django ModelForm tayyorlash va CSRF validatsiyasini sozlash;
5. **Admin Panel**: ModelAdmin sozlamalari bilan qulay CMS panel yaratish.

Muvaffaqiyatlar yor bo'lsin!
"""
    }
]

def main():
    print("🚀 5-OY (49-60 DARSLAR) HTML/CSS/BOOTSTRAP + DJANGO CURRICULUM UPDATE STARTING...")
    
    for item in LESSONS_MONTH_5:
        num = item["lesson_number"]
        filename = f"dars_{num:02d}.md"
        filepath = os.path.join(DOCS_DIR, filename)

        # 1. Write Markdown File
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(item["content"])

        # 2. Update DB Lesson object
        lesson_obj, created = Lesson.objects.update_or_create(
            lesson_number=num,
            defaults={
                "lesson_id": f"les-100unique-{num}",
                "title": item["title"],
                "goal": item["goal"],
                "description": item["description"],
                "content": item["content"],
                "status": "planned",
                "homework": f"{item['title']} bo'yicha amaliy topshiriqlarni bajarish va kodingizni GitHub'ga joylash."
            }
        )
        status_str = "Created" if created else "Updated"
        print(f"✅ [{status_str}] Lesson {num}: {item['title']}")

    print("✨ MONTH 5 HTML/CSS/BOOTSTRAP + DJANGO CURRICULUM UPDATED SUCCESSFULLY!")

if __name__ == "__main__":
    main()
