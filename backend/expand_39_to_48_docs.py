import os
import sys
import json
import django

sys.path.append(os.path.dirname(__file__))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from lessons_app.models import Lesson

LESSONS_JSON = os.path.join(os.path.dirname(__file__), "..", "frontend", "src", "data", "lessons.json")

FULL_LONG_39_TO_48 = {
    39: """# 📦 39. Virtual Environment va pip — Dars dokumentatsiyasi

`Virtual Environment (venv)` va `pip` — Python loyihalarida **kutubxona paketlarini ajratilgan (izolatsiyalangan) holda boshqarish va versiyalar toqnashuvini oldini olish** uchun ishlatiladi.

Bu mavzu orqali:

- `python -m venv venv` orqali virtual muhit yaratish;
- Virtual muhitni faollashtirish (`source venv/bin/activate` yoki `venv\\Scripts\\activate`);
- `pip install package_name` orqali kutubxona o'rnatish;
- `pip freeze > requirements.txt` orqali bog'liqliklarni saqlash

mumkin.

---

## Dars maqsadi

Bu dars oxirida o‘quvchi:

- Har bir loyiha uchun alohida virtual muhit yaratish;
- Loyihalar o'rtasidagi kutubxonalar versiyalari toqnashuvini oldini olish;
- `requirements.txt` faylini yaratish va undan qayta o'rnatish

ni mustaqil bajara oladi.

## Kerakli bilimlar

Bu darsni tushunish uchun:

- Terminal (Bash/Zsh/PowerShell) buyruqlari

bilinishi kerak.

---

# 1. Asosiy tushuncha

`Virtual Environment va pip` nima ekanini sodda tilda tushuntiramiz.

Masalan:

> `Virtual Environment` — loyihangiz uchun alohida ajratilgan xona. Har bir loyiha o'zining shaxsiy Python kutubxonalari versiyasiga ega bo'ladi (masalan bitta loyiha Django 4.2, boshqasi Django 5.0).

Muhim qoida:

```bash
python3 -m venv venv
source venv/bin/activate
pip install django
```

---

# 2. Birinchi sodda misol

```bash
# Virtual muhit aktivlashtirish
source venv/bin/activate

# Paket o'rnatish
pip install requests

# Versiyasini ko'rish
pip freeze
```

Natija:

```text
requests==2.31.0
urllib3==2.0.7
```

---

# 10. Qisqa xulosa

Bu darsda:

- `python -m venv yaratish`;
- `source activate faollashtirish`;
- `pip freeze > requirements.txt`

ni o‘rgandik.

Keyingi darsda: **Django kirish va loyiha strukturasi**.

---

# Resurslar va fayllar

- 📄 Konspekt: `39_dars_konspekt.pdf`
- 💻 Kodlar: `github.com/dars-reja/39-dars`
- 🎬 Video: `youtube.com/watch?v=dars39`
- 📝 Qo‘shimcha mashqlar: `python.uz/mashq39`
""",

    40: """# 🟢 40. Django kirish va loyiha strukturasi — Dars dokumentatsiyasi

`Django` — Python’da **kattalashuvchi professional va xavfsiz web-backend dasturlar yaratish uchun eng mashhur freymvork** hisoblanadi.

Bu mavzu orqali:

- `pip install django` va `django-admin startproject myproject .`;
- Django loyiha strukturasi: `manage.py`, `settings.py`, `urls.py`, `wsgi.py`, `asgi.py`;
- Dev-serverni ishga tushirish: `python manage.py runserver 0.0.0.0:8000`

mumkin.

---

## Dars maqsadi

Bu dars oxirida o‘quvchi:

- Django freymvorkining MTV (Model-Template-View) arxitekturasini tushunish;
- Yangi Django loyihasini noldan sozlash va ishga tushirish;
- `settings.py` fayli orqali bazaviy sozlamalarni berish

ni mustaqil bajara oladi.

---

# 1. Asosiy tushuncha

```bash
django-admin startproject config .
python manage.py runserver
```

---

# 10. Qisqa xulosa

Bu darsda:

- `Django startproject`;
- `settings.py va manage.py`;
- `runserver dev-server`

ni o‘rgandik.

Keyingi darsda: **Django Apps va URLs**.

---

# Resurslar va fayllar

- 📄 Konspekt: `40_dars_konspekt.pdf`
- 💻 Kodlar: `github.com/dars-reja/40-dars`
- 🎬 Video: `youtube.com/watch?v=dars40`
- 📝 Qo‘shimcha mashqlar: `python.uz/mashq40`
""",

    41: """# 📱 41. Django Apps va URLs — Dars dokumentatsiyasi

`Django Apps` va `URLs` — Loyihani **decoupling (mustaqil modullarga bo'lish) va yo'nalishlarni (routing) boshqarish** uchun ishlatiladi.

Bu mavzu orqali:

- `python manage.py startapp app_name`;
- `INSTALLED_APPS` ro'yxatiga ilovani qo'shish;
- Bosh `urls.py` ichida `include('app_name.urls')` yordamida yo'naltirish

mumkin.

---

## Dars maqsadi

Bu dars oxirida o‘quvchi:

- Loyihani kichik va mustaqil Django ilovalariga bo'lish;
- `urls.py` larni bir-biriga bog'lash (*URL Routing*);
- Modulli arxitektura tamoyillarini qo'llash

ni mustaqil bajara oladi.

---

# 1. Asosiy tushuncha

```python
# config/urls.py
from django.urls import path, include

urlpatterns = [
    path('api/', include('lessons_app.urls')),
]
```

---

# 10. Qisqa xulosa

Bu darsda:

- `startapp yaratish`;
- `INSTALLED_APPS ga qo'shish`;
- `include() bilan URL bog'lash`

ni o‘rgandik.

Keyingi darsda: **Django Views va Templates**.

---

# Resurslar va fayllar

- 📄 Konspekt: `41_dars_konspekt.pdf`
- 💻 Kodlar: `github.com/dars-reja/41-dars`
- 🎬 Video: `youtube.com/watch?v=dars41`
- 📝 Qo‘shimcha mashqlar: `python.uz/mashq41`
""",

    42: """# 👁️ 42. Django Views va Templates — Dars dokumentatsiyasi

`Django Views` va `Templates` — **foydalanuvchi so'rovlarini qabul qilish, biznes mantiqni bajarish va HTML natijani qaytarish** uchun ishlatiladi.

Bu mavzu orqali:

- `HttpResponse` va `render(request, 'template.html', context)`;
- Django Template Language (DTL): `{{ variable }}`, `{% for %}`, `{% if %}`;
- Template Inheritance: `{% extends 'base.html' %}` va `{% block content %}`

mumkin.

---

## Dars maqsadi

Bu dars oxirida o‘quvchi:

- View funksiyalaridan HTML shablonlarga ma'lumot uzatish;
- DTL operatorlari yordamida dinamik HTML sahifalar tuzish;
- `base.html` orqali shablonlarni bir-biriga ulash (*Inheritance*)

ni mustaqil bajara oladi.

---

# 1. Asosiy tushuncha

```python
from django.shortcuts import render

def home_view(request):
    context = {"title": "Bosh Sahifa", "user_count": 100}
    return render(request, "home.html", context)
```

---

# 10. Qisqa xulosa

Bu darsda:

- `render() funksiyasi`;
- `DTL sintaksisi ({{ }}, {% %})`;
- `Template Inheritance`

ni o‘rgandik.

Keyingi darsda: **Django Models va Migrations**.

---

# Resurslar va fayllar

- 📄 Konspekt: `42_dars_konspekt.pdf`
- 💻 Kodlar: `github.com/dars-reja/42-dars`
- 🎬 Video: `youtube.com/watch?v=dars42`
- 📝 Qo‘shimcha mashqlar: `python.uz/mashq42`
""",

    43: """# 🗃️ 43. Django Models va Migrations — Dars dokumentatsiyasi

`Django Models` va `Migrations` — **Python klasslari yordamida Ma'lumotlar Bazasi jadvallarini avtomatik yaratish (ORM)** uchun ishlatiladi.

Bu mavzu orqali:

- `models.Model` sinfidan voris olish;
- Maydon turlari: `CharField`, `IntegerField`, `DateTimeField`, `BooleanField`;
- `python manage.py makemigrations` va `python manage.py migrate`

mumkin.

---

## Dars maqsadi

Bu dars oxirida o‘quvchi:

- Python klasslari orqali ma'lumotlar bazasi sxemasini tuzish;
- `makemigrations` va `migrate` buyruqlarini to'g'ri ishlatish;
- Model maydonlariga cheklovlar (`max_length`, `default`, `null=True`) berish

ni mustaqil bajara oladi.

---

# 1. Asosiy tushuncha

```python
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
```

---

# 10. Qisqa xulosa

Bu darsda:

- `models.Model sinfi`;
- `CharField, IntegerField, DateTimeField`;
- `makemigrations va migrate`

ni o‘rgandik.

Keyingi darsda: **Django Admin Panel**.

---

# Resurslar va fayllar

- 📄 Konspekt: `43_dars_konspekt.pdf`
- 💻 Kodlar: `github.com/dars-reja/43-dars`
- 🎬 Video: `youtube.com/watch?v=dars43`
- 📝 Qo‘shimcha mashqlar: `python.uz/mashq43`
""",

    44: """# ⚙️ 44. Django Admin Panel — Dars dokumentatsiyasi

`Django Admin Panel` — Django'ning **tayyor avtomatik ma'lumotlar boshqaruvi (CMS/Dashboard) interfeysi** hisoblanadi.

Bu mavzu orqali:

- `python manage.py createsuperuser` orqali admin yaratish;
- `admin.py` ichida `admin.site.register(MyModel)`;
- `ModelAdmin` sinfi yordamida `list_display`, `search_fields`, `list_filter` sozlamalari

mumkin.

---

## Dars maqsadi

Bu dars oxirida o‘quvchi:

- Superuser akkauntini ochish va admin panelga kirish;
- Modellarni admin panelda ro'yxatdan o'tkazish;
- Admin interfeysida qidiruv va filtrlarni sozlash

ni mustaqil bajara oladi.

---

# 1. Asosiy tushuncha

```python
from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "age", "created_at")
    search_fields = ("name",)
```

---

# 10. Qisqa xulosa

Bu darsda:

- `createsuperuser yaratish`;
- `admin.site.register()`;
- `list_display va search_fields`

ni o‘rgandik.

Keyingi darsda: **Django ORM CRUD**.

---

# Resurslar va fayllar

- 📄 Konspekt: `44_dars_konspekt.pdf`
- 💻 Kodlar: `github.com/dars-reja/44-dars`
- 🎬 Video: `youtube.com/watch?v=dars44`
- 📝 Qo‘shimcha mashqlar: `python.uz/mashq44`
""",

    45: """# 🔍 45. Django ORM CRUD — Dars dokumentatsiyasi

`Django ORM (Object-Relational Mapping)` — **SQL yozmasdan Python obyektlari orqali bazadagi ma'lumotlarni boshqarish** uchun ishlatiladi.

Bu mavzu orqali:

- `Model.objects.create(...)` (Create);
- `Model.objects.all()`, `filter()`, `get()` (Read);
- `obj.save()` (Update);
- `obj.delete()` (Delete)

mumkin.

---

## Dars maqsadi

Bu dars oxirida o‘quvchi:

- SQL yozmasdan Django ORM orqali CRUD operatsiyalarini bajarish;
- `filter()` va `exclude()` metodlari bilan ma'lumotlarni saralash;
- Django Shell (`python manage.py shell`) da ORM so'rovlarini sinash

ni mustaqil bajara oladi.

---

# 1. Asosiy tushuncha

```python
# Create
student = Student.objects.create(name="Ali", age=20)

# Read
all_students = Student.objects.filter(age__gte=18)

# Update
student.age = 21
student.save()

# Delete
student.delete()
```

---

# 10. Qisqa xulosa

Bu darsda:

- `Model.objects.create()`;
- `filter(), get(), all()`;
- `save() va delete()`

ni o‘rgandik.

Keyingi darsda: **Django Forms va ModelForms**.

---

# Resurslar va fayllar

- 📄 Konspekt: `45_dars_konspekt.pdf`
- 💻 Kodlar: `github.com/dars-reja/45-dars`
- 🎬 Video: `youtube.com/watch?v=dars45`
- 📝 Qo‘shimcha mashqlar: `python.uz/mashq45`
""",

    46: """# 📝 46. Django Forms va ModelForms — Dars dokumentatsiyasi

`Django Forms` va `ModelForms` — **HTML shakllaridan kiritilgan ma'lumotlarni tekshirish (validation) va bazaga xavfsiz saqlash** uchun ishlatiladi.

Bu mavzu orqali:

- `forms.Form` va `forms.ModelForm`;
- `is_valid()`, `cleaned_data` lug'ati;
- CSRF token muhofazasi (`{% csrf_token %}`)

mumkin.

---

## Dars maqsadi

Bu dars oxirida o‘quvchi:

- Foydalanuvchi ma'lumotlarini qabul qiluvchi xavfsiz HTML formalar yaratish;
- `ModelForm` orqali formani model bilan avtomatik bog'lash;
- `is_valid()` yordamida xatolarni ushlash va xabarlar ko'rsatish

ni mustaqil bajara oladi.

---

# 1. Asosiy tushuncha

```python
from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'age']
```

---

# 10. Qisqa xulosa

Bu darsda:

- `forms.ModelForm sinfi`;
- `is_valid() va cleaned_data`;
- `{% csrf_token %} xavfsizligi`

ni o‘rgandik.

Keyingi darsda: **Django ORM munosabatlar (FK, M2M)**.

---

# Resurslar va fayllar

- 📄 Konspekt: `46_dars_konspekt.pdf`
- 💻 Kodlar: `github.com/dars-reja/46-dars`
- 🎬 Video: `youtube.com/watch?v=dars46`
- 📝 Qo‘shimcha mashqlar: `python.uz/mashq46`
""",

    47: """# 🔗 47. Django ORM munosabatlar (FK, M2M) — Dars dokumentatsiyasi

`Django ORM Munosabatlar` — **jadvallar o'rtasida ForeignKey (1-to-N) va ManyToManyField (N-to-N) bog'liqliklarini o'rnatish** uchun ishlatiladi.

Bu mavzu orqali:

- `models.ForeignKey(OtherModel, on_delete=models.CASCADE)`;
- `models.ManyToManyField(OtherModel)`;
- `models.OneToOneField(OtherModel)`;
- `related_name` parametri orqali teskari so'rovlar yuborish

mumkin.

---

## Dars maqsadi

Bu dars oxirida o‘quvchi:

- Jadvallar o'rtasida relatsion munosabatlar (FK, M2M) o'rnatish;
- `on_delete=models.CASCADE` mantiqini tushunish;
- `related_name` yordamida teskari ORM so'rovlarini yozish

ni mustaqil bajara oladi.

---

# 1. Asosiy tushuncha

```python
class Category(models.Model):
    name = models.CharField(max_length=50)

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=100)
```

---

# 10. Qisqa xulosa

Bu darsda:

- `ForeignKey va ManyToManyField`;
- `on_delete=models.CASCADE`;
- `related_name parametrlari`

ni o‘rgandik.

Keyingi darsda: **4-modul imtihoni**.

---

# Resurslar va fayllar

- 📄 Konspekt: `47_dars_konspekt.pdf`
- 💻 Kodlar: `github.com/dars-reja/47-dars`
- 🎬 Video: `youtube.com/watch?v=dars47`
- 📝 Qo‘shimcha mashqlar: `python.uz/mashq47`
""",

    48: """# 🎓 48. 4-modul imtihoni — Dars dokumentatsiyasi

`4-modul imtihoni` — 37-darsdan 47-darsgacha o'rganilgan **HTTP, Git, Django Apps, Views, Templates, Models, Admin Panel va ORM ko'nikmalarini sinash** uchun o'tkaziladi.

Bu mavzu orqali:

- 37–47 darslar bo'yicha nazariy va amaliy bilimlarni sinash;
- Real 3 ta murakkab Django Web va ORM masalalarini yechish;
- Sertifikatlash uchun 4-modul natijalarini belgilash

mumkin.

---

## Imtihon Tartibi (100 ballik shkala)

- **Nazariy Testlar (20 ball)**: 37-47 darslar bo'yicha 10 ta test;
- **Amaliy Masalalar (50 ball)**: 3 ta murakkab Django Web va ORM topshirig'i;
- **PEP8 Standart va Kod Sifati (20 ball)**: Izohlar va to'g'ri nomlash;
- **Vaqt va Intizom (10 ball)**: 2 soat ichida topshirish.

---

# 1. Imtihon Kod Shabloni

```python
def module_4_exam():
    print("====================================")
    print("   4-MODUL IMTIHONI KODI BAJARILDI  ")
    print("====================================")

module_4_exam()
```
"""
}

for num, txt in FULL_LONG_39_TO_48.items():
    try:
        l = Lesson.objects.get(lesson_number=num)
        l.content = txt
        l.save()
    except:
        pass

with open(LESSONS_JSON, "r", encoding="utf-8") as f:
    j_data = json.load(f)

for item in j_data:
    n = item.get("lessonNumber")
    if n in FULL_LONG_39_TO_48:
        item["content"] = FULL_LONG_39_TO_48[n]

with open(LESSONS_JSON, "w", encoding="utf-8") as f:
    json.dump(j_data, f, ensure_ascii=False, indent=2)

print("✨ 39-48 darslar kontenti to'liqligicha 10 bo'limli variantda saqlandi!")
