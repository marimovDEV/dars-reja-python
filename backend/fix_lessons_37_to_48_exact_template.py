import os
import sys
import json
import django

# Setup Django
sys.path.append(os.path.dirname(__file__))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from lessons_app.models import Lesson

LESSONS_JSON = os.path.join(os.path.dirname(__file__), "..", "frontend", "src", "data", "lessons.json")

EXACT_37_TO_48_LESSONS = {
    37: {
        "title": "37-dars — HTTP, REST API va Web asoslari",
        "content": """# 🌐 37. HTTP, REST API va Web asoslari — Dars dokumentatsiyasi

`HTTP` va `REST API` — Zamonaviy web-dasturlashda **mijoz (Client/Frontend) va server (Backend) o'rtasida ma'lumot almashish** uchun asosiy protokol va me'moriy uslub hisoblanadi.

Bu mavzu orqali:

- HTTP So'rov metodlari: `GET`, `POST`, `PUT`, `PATCH`, `DELETE`;
- HTTP Status kodlari: `200 OK`, `201 Created`, `400 Bad Request`, `404 Not Found`, `500 Server Error`;
- REST API tamoyillari va resurs yo'nalishlari (`/api/v1/users/`);
- Headers, Query Parameters va Request Body

mumkin.

---

## Dars maqsadi

Bu dars oxirida o‘quvchi:

- Client-Server arxitekturasini tushunish;
- HTTP metodlaridan to'g'ri foydalanib RESTful so'rovlar loyihalash;
- Status kodlari bo'yicha server javoblarini tahlil qilish

ni mustaqil bajara oladi.

## Kerakli bilimlar

Bu darsni tushunish uchun:

- 23-dars: JSON va requests;
- Web brauzerlar ishlash prinsipi

bilinishi kerak.

---

# 1. Asosiy tushuncha

`HTTP va REST API` nima ekanini sodda tilda tushuntiramiz.

Masalan:

> `HTTP (Hypertext Transfer Protocol)` — web brauzer va backend server gaplashadigan til. `REST API` — URL lar orqali ma'lumotlarni JSON shaklida xavfsiz almashish qoidalari to'plami.

Muhim qoida:

```text
GET /api/v1/products -> Barcha mahsulotlarni olish
POST /api/v1/products -> Yangi mahsulot qo'shish
```

---

# 2. Birinchi sodda misol

```python
import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
print("Status Kodi:", response.status_code)
print("Sarlavha:", response.json()["title"])
```

Natija:

```text
Status Kodi: 200
Sarlavha: sunt aut facere repellat provident occaecati excepturi optio reprehenderit
```

Izoh:

- `3-qator` — `requests.get()` yordamida HTTP GET so'rov yuborildi;
- `4-qator` — Server javobi `200 OK` status kodi bilan qaytdi.

---

# 3. Asosiy HTTP Metodlari Jadvali

| Metod | Vazifasi | Qachon Ishlatiladi |
|---|---|---|
| `GET` | Ma'lumotni o'qib olish | Ro'yxat yoki bitta obyektni ko'rishda |
| `POST` | Yangi resurs yaratish | Ro'yxatdan o'tish yoki post yaratishda |
| `PUT` | Resursni to'liq yangilash | Barcha maydonlarni o'zgartirishda |
| `PATCH` | Resursni qisman yangilash | Faqat bitta maydonni (masalan ismni) o'zgartirishda |
| `DELETE` | Resursni o'chirish | Obyektni bazadan o'chirishda |

---

# 4. Batafsil misol — Status Kodlari

```python
import requests

url = "https://jsonplaceholder.typicode.com/invalid-endpoint"
res = requests.get(url)

if res.status_code == 200:
    print("Muvaffaqiyatli!")
elif res.status_code == 404:
    print("Xato: Sahifa yoki resurs topilmadi (404)!")
```

Natija:

```text
Xato: Sahifa yoki resurs topilmadi (404)!
```

---

# 6. Ko‘p uchraydigan xatolar

## Xato 1: GET so'rovida Request Body orqali ma'lumot yuborish

Noto‘g‘ri:

```python
# GET so'rovida body yuborish HTTP standartiga to'g'ri kelmaydi
requests.get("https://api.com/users", json={"name": "Ali"})
```

To‘g‘ri:

```python
# Qidiruv uchun Query Parameter ishlatiladi
requests.get("https://api.com/users?name=Ali")
```

---

# 7. Sinfdagi amaliy topshiriqlar

## 1-topshiriq — Oson

**Vazifa:** Brauzer Developer Tools (F12) `Network` bo'limini ochib, ixtiyoriy sayt yuborayotgan HTTP status kodlarini kuzating.

## 2-topshiriq — O‘rta

**Vazifa:** `requests.post()` yordamida vaqtinchalik API ga yangi ma'lumot yuboring va `201 Created` status kodi oling.

---

# 8. Uyga vazifa

1. `37_dars_http_rest.py` faylini yarating;
2. HTTP status kodlarini (200, 201, 400, 401, 403, 404, 500) tushuntiruvchi konsol dasturini yozing;
3. Kodni GitHub'ga saqlang.

---

# 9. Tekshirish savollari

1. `GET` va `POST` metodlarining asosiy farqi nima?
2. `401 Unauthorized` va `403 Forbidden` xatolari nimasi bilan farqlanadi?
3. REST API tizimida JSON formatining afzalligi nimada?

---

# 10. Qisqa xulosa

Bu darsda:

- `HTTP metodlari (GET, POST, PUT, DELETE)`;
- `Status kodlari (200, 404, 500)`;
- `REST API arxitekturasi`

ni o‘rgandik.

Keyingi darsda: **Git va GitHub**.

---

# Resurslar va fayllar

- 📄 Konspekt: `37_dars_konspekt.pdf`
- 💻 Kodlar: `github.com/dars-reja/37-dars`
- 🎬 Video: `youtube.com/watch?v=dars37`
- 📝 Qo‘shimcha mashqlar: `python.uz/mashq37`
""",
        "code": "import requests\n\nresponse = requests.get('https://jsonplaceholder.typicode.com/posts/1')\nprint('Status Code:', response.status_code)\nprint('Data:', response.json())",
        "code_exp": "- `1-3 qatorlar` — HTTP GET so'rovi yuborilib status kodi tekshiriladi;\n- `4-5 qatorlar` — Qaytgan resurs chop etiladi.",
        "quiz_q": "Resursni mutlaqo yangi ma'lumot bilan yaratish uchun qaysi HTTP metodi ishlatiladi?",
        "quiz_opts": ["GET", "POST", "FETCH", "OPTION"],
        "quiz_ans": 1,
        "quiz_exp": "POST metodi yangi obyekt/resurs yaratish so'rovlarida ishlatiladi."
    },

    38: {
        "title": "38-dars — Git va GitHub",
        "content": """# 🐙 38. Git va GitHub — Dars dokumentatsiyasi

`Git` va `GitHub` — Dasturchilar uchun **kodlar versiyasini nazorat qilish (Version Control) hamda jamoaviy ishlash platformasi** hisoblanadi.

Bu mavzu orqali:

- `git init`, `git status`, `git add .`, `git commit -m "msg"`;
- Remote repositoriyaga bog'lash: `git remote add origin url`;
- Push va Pull: `git push -u origin main` va `git pull`;
- `.gitignore` fayli orqali keraksiz fayllarni yashirish

mumkin.

---

## Dars maqsadi

Bu dars oxirida o‘quvchi:

- Loyihani Git versiya nazoratiga olish;
- GitHub platformasida repozitoriyalar yaratish va kodlarni yuklash;
- `.gitignore` yordamida parollar va venv fayllarni yuklanishidan saqlash

ni mustaqil bajara oladi.

## Kerakli bilimlar

Bu darsni tushunish uchun:

- Terminal (Bash/Zsh) buyruqlari

bilinishi kerak.

---

# 1. Asosiy tushuncha

`Git va GitHub` nima ekanini sodda tilda tushuntiramiz.

Masalan:

> `Git` — bu kompyuteringizdagi vaqt mashinasi. U kodning har bir o'zgarishini (commit) saqlaydi. `GitHub` — ushbu saqlangan kodlarni bulutda (cloud) joylashtirish va boshqa dasturchilar bilan hamkorlik qilish sayti.

Muhim qoida:

```bash
git init
git add .
git commit -m "Initial commit"
```

---

# 2. Birinchi sodda misol

```bash
# Git repositoriyasini yaratish
git init

# O'zgarishlarni kiritish
git add .

# Izoh bilan saqlash
git commit -m "1-versiya tayyor"
```

Natija:

```text
[main (root-commit) a1b2c3d] 1-versiya tayyor
 3 files changed, 45 insertions(+)
```

---

# 3. Asosiy Git Buyruqlari Jadvali

| Buyruq | Vazifasi | Misol |
|---|---|---|
| `git init` | Yangi Git repozitoriyasi yaratish | `git init` |
| `git status` | O'zgargan fayllarni ko'rish | `git status` |
| `git add .` | Barcha fayllarni saqlashga tayyorlash | `git add .` |
| `git commit -m` | O'zgarishlarni snapshot qilish | `git commit -m "fix bug"` |
| `git push` | Kodlarni GitHub ga yuklash | `git push origin main` |

---

# 4. Batafsil misol — .gitignore Fayli

```text
# .gitignore ichidagi keraksiz fayllar:
venv/
__pycache__/
*.sqlite3
.env
```

Izoh:

- `venv/` va `.env` maxfiy parollar hamda katta kutubxona papkalari bo'lgani uchun GitHub'ga yuklanmasligi shart.

---

# 6. Ko‘p uchraydigan xatolar

## Xato 1: Secret keys yoki maxfiy parollarni GitHub'ga commit qilish

Noto‘g‘ri:

```python
# API_KEY = "secret_12345" kodda ochiq qolib ketishi!
```

To‘g‘ri:

```text
# Parollarni .env ga qo'yib, .env faylini .gitignore ga qo'shish
```

---

# 7. Sinfdagi amaliy topshiriqlar

## 1-topshiriq — Oson

**Vazifa:** Loyihangizda `git status` buyrug'ini ishlatib o'zgargan fayllarni ko'ring.

## 2-topshiriq — O‘rta

**Vazifa:** GitHub'da yangi repozitoriy ochib, o'z loyihangizni `git push` yordamida yuklang.

---

# 8. Uyga vazifa

1. `38_dars_git_commands.txt` faylini yarating;
2. GitHub sahifangiz Profilingizni to'ldirib repository URL-ni topshiring;
3. Kodni GitHub'ga saqlang.

---

# 9. Tekshirish savollari

1. `git add` va `git commit` o'rtasidagi farq nima?
2. `.gitignore` faylining maqsadi nimada?
3. Remote origin nima?

---

# 10. Qisqa xulosa

Bu darsda:

- `Git versiya nazorati`;
- `GitHub repozitoriyalari`;
- `.gitignore va xavfsizlik`

ni o‘rgandik.

Keyingi darsda: **Virtual Environment va pip**.

---

# Resurslar va fayllar

- 📄 Konspekt: `38_dars_konspekt.pdf`
- 💻 Kodlar: `github.com/dars-reja/38-dars`
- 🎬 Video: `youtube.com/watch?v=dars38`
- 📝 Qo‘shimcha mashqlar: `python.uz/mashq38`
""",
        "code": "# Terminal buyruqlari ketma-ketligi:\n# git init\n# git add .\n# git commit -m 'Initial commit'\n# git branch -M main\n# git remote add origin https://github.com/user/repo.git\n# git push -u origin main\nprint('Git so\\'rovlari ketma-ketligi taqdim etildi.')",
        "code_exp": "- Git repozitoriyasini ishga tushirish va GitHub bulutiga yuklash qadamlari.",
        "quiz_q": "O'zgarishlarni snapshot qilib izoh bilan saqlovchi Git buyrug'i qaysi?",
        "quiz_opts": ["git add", "git save", "git commit -m", "git push"],
        "quiz_ans": 2,
        "quiz_exp": "git commit -m buyrug'i o'zgarishlarni izoh (message) bilan saqlaydi."
    },

    39: {
        "title": "39-dars — Virtual Environment va pip",
        "content": """# 📦 39. Virtual Environment va pip — Dars dokumentatsiyasi

`Virtual Environment (venv)` va `pip` — Python loyihalarida **kutubxona paketlarini ajratilgan (izolatsiyalangan) holda boshqarish** uchun ishlatiladi.

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

---

# 1. Asosiy tushuncha

```bash
python3 -m venv venv
source venv/bin/activate
pip install django requests
pip freeze > requirements.txt
```
""",
        "code": "# Virtual muhit yaratish buyruqlari:\n# python -m venv venv\n# source venv/bin/activate (Mac/Linux)\n# venv\\Scripts\\activate (Windows)\n# pip install -r requirements.txt\nprint('Virtual Environment ko\\'rsatmalari tayyor.')",
        "code_exp": "- Loyiha kutubxonalarini tizim global Pythonidan ajratib oluvchi venv buyruqlari.",
        "quiz_q": "Loyiha kutubxonalari ro'yxatini faylga saqlovchi pip buyrug'i qaysi?",
        "quiz_opts": ["pip list", "pip freeze > requirements.txt", "pip save", "pip export"],
        "quiz_ans": 1,
        "quiz_exp": "pip freeze > requirements.txt loyihaga o'rnatilgan barcha paketlarni saqlaydi."
    },

    40: {
        "title": "40-dars — Django kirish va loyiha strukturasi",
        "content": """# 🟢 40. Django kirish va loyiha strukturasi — Dars dokumentatsiyasi

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
""",
        "code": "# Django dev serverni ishga tushirish:\n# python manage.py runserver\nprint('Django Loyihasi Ishga Tushirildi: http://127.0.0.1:8000/')",
        "code_exp": "- Django freymvorkining manage.py fayli orqali serverni ishga tushirish kodi.",
        "quiz_q": "Yangi Django loyihasini yaratuvchi CLI buyrug'i qaysi?",
        "quiz_opts": ["django create project", "django-admin startproject", "python manage.py new", "django init"],
        "quiz_ans": 1,
        "quiz_exp": "django-admin startproject loyiha_nomi yangi Django arxitekturasini tuzadi."
    },

    41: {
        "title": "41-dars — Django Apps va URLs",
        "content": """# 📱 41. Django Apps va URLs — Dars dokumentatsiyasi

`Django Apps` va `URLs` — Loyihani **decoupling (mustaqil modullarga bo'lish) va yo'nalishlarni (routing) boshqarish** uchun ishlatiladi.

Bu mavzu orqali:

- `python manage.py startapp app_name`;
- `INSTALLED_APPS` ro'yxatiga ilovani qo'shish;
- Bosh `urls.py` ichida `include('app_name.urls')` yordamida yo'naltirish

mumkin.

---

# 1. Asosiy tushuncha

```python
# config/urls.py
from django.urls import path, include

urlpatterns = [
    path('api/', include('lessons_app.urls')),
]
```
""",
        "code": "# app/urls.py\nfrom django.urls import path\n# from .views import my_view\n\nurlpatterns = [\n    # path('hello/', my_view, name='hello'),\n]\nprint('URL Routing sovlari tayyor.')",
        "code_exp": "- Django app ichidagi urls.py marshrutlarini belgilash uslubi.",
        "quiz_q": "Yangi Django ilovasini (app) yaratish buyrug'i qaysi?",
        "quiz_opts": ["python manage.py createapp", "python manage.py startapp", "django start app", "pip install app"],
        "quiz_ans": 1,
        "quiz_exp": "python manage.py startapp app_nomi yangi ilova papkasini tuzadi."
    },

    42: {
        "title": "42-dars — Django Views va Templates",
        "content": """# 👁️ 42. Django Views va Templates — Dars dokumentatsiyasi

`Django Views` va `Templates` — **foydalanuvchi so'rovlarini qabul qilish, biznes mantiqni bajarish va HTML natijani qaytarish** uchun ishlatiladi.

Bu mavzu orqali:

- `HttpResponse` va `render(request, 'template.html', context)`;
- Django Template Language (DTL): `{{ variable }}`, `{% for %}`, `{% if %}`;
- Template Inheritance: `{% extends 'base.html' %}` va `{% block content %}`

mumkin.

---

# 1. Asosiy tushuncha

```python
from django.shortcuts import render

def home_view(request):
    context = {"title": "Bosh Sahifa", "user_count": 100}
    return render(request, "home.html", context)
```
""",
        "code": "from django.http import HttpResponse\n\ndef hello_view(request):\n    return HttpResponse('<h1>Salom Django World!</h1>')\n\nprint('Django View funksiyasi tayyor.')",
        "code_exp": "- HTTP so'rovini qabul qilib HTML javob qaytaruvchi Django View funksiyasi.",
        "quiz_q": "Django DTL da o'zgaruvchi qiymatini HTML ga chiqaruvchi sintaksis qaysi?",
        "quiz_opts": ["{% var %}", "{{ var }}", "[[ var ]]", "<%= var %>"],
        "quiz_ans": 1,
        "quiz_exp": "{{ variable }} sintaksisi DTL da o'zgaruvchi qiymatini chop etadi."
    },

    43: {
        "title": "43-dars — Django Models va Migrations",
        "content": """# 🗃️ 43. Django Models va Migrations — Dars dokumentatsiyasi

`Django Models` va `Migrations` — **Python klasslari yordamida Ma'lumotlar Bazasi jadvallarini avtomatik yaratish (ORM)** uchun ishlatiladi.

Bu mavzu orqali:

- `models.Model` sinfidan voris olish;
- Maydon turlari: `CharField`, `IntegerField`, `DateTimeField`, `BooleanField`;
- `python manage.py makemigrations` va `python manage.py migrate`

mumkin.

---

# 1. Asosiy tushuncha

```python
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
```
""",
        "code": "from django.db import models\n\nclass Course(models.Model):\n    title = models.CharField(max_length=200)\n    price = models.IntegerField()\n    is_active = models.BooleanField(default=True)\n\nprint('Django Model sinfi e\\'lon qilindi.')",
        "code_exp": "- Django ORM yordamida Course jadvalining ma'lumotlar modeli.",
        "quiz_q": "Modeldagi o'zgarishlar uchun SQL migratsiya fayllarini yaratuvchi buyruq qaysi?",
        "quiz_opts": ["python manage.py migrate", "python manage.py makemigrations", "python manage.py db_sync", "django migrate"],
        "quiz_ans": 1,
        "quiz_exp": "makemigrations migratsiya Python faylini tuzadi, migrate esa uni bazaga qo'llaydi."
    },

    44: {
        "title": "44-dars — Django Admin Panel",
        "content": """# ⚙️ 44. Django Admin Panel — Dars dokumentatsiyasi

`Django Admin Panel` — Django'ning **tayyor avtomatik ma'lumotlar boshqaruvi (CMS/Dashboard) interfeysi** hisoblanadi.

Bu mavzu orqali:

- `python manage.py createsuperuser` orqali admin yaratish;
- `admin.py` ichida `admin.site.register(MyModel)`;
- `ModelAdmin` sinfi yordamida `list_display`, `search_fields`, `list_filter` sozlamalari

mumkin.

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
""",
        "code": "from django.contrib import admin\n# from .models import Course\n\n# @admin.register(Course)\n# class CourseAdmin(admin.ModelAdmin):\n#     list_display = ('id', 'title', 'price')\nprint('Django Admin sozlamalari tayyor.')",
        "code_exp": "- Admin panelda modellar ko'rinishini sozlash kodi.",
        "quiz_q": "Django Admin paneliga kirish uchun boshqaruvchi (super-user) yaratish buyrug'i qaysi?",
        "quiz_opts": ["python manage.py createadmin", "python manage.py createsuperuser", "django admin new", "python manage.py adduser"],
        "quiz_ans": 1,
        "quiz_exp": "createsuperuser buyrug'i admin login va parolini o'rnatish imkonini beradi."
    },

    45: {
        "title": "45-dars — Django ORM CRUD",
        "content": """# 🔍 45. Django ORM CRUD — Dars dokumentatsiyasi

`Django ORM (Object-Relational Mapping)` — **SQL yozmasdan Python obyektlari orqali bazadagi ma'lumotlarni boshqarish** uchun ishlatiladi.

Bu mavzu orqali:

- `Model.objects.create(...)` (Create);
- `Model.objects.all()`, `filter()`, `get()` (Read);
- `obj.save()` (Update);
- `obj.delete()` (Delete)

mumkin.

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
""",
        "code": "# Django ORM misollari:\n# new_course = Course.objects.create(title='Python', price=500000)\n# active_courses = Course.objects.filter(is_active=True)\nprint('Django ORM so\\'rovlari tayyor.')",
        "code_exp": "- Django ORM orqali ma'lumotlarni filtrlash va yaratish operatsiyalari.",
        "quiz_q": "Django ORM da unikal bitta obyektni kalit bo'yicha olish uchun qaysi metod ishlatiladi?",
        "quiz_opts": ["Model.objects.all()", "Model.objects.filter()", "Model.objects.get()", "Model.objects.find()"],
        "quiz_ans": 2,
        "quiz_exp": "get() metodi shartga mos bitta obyektni qaytaradi (topilmasa yoki ko'p bo'lsa xato beradi)."
    },

    46: {
        "title": "46-dars — Django Forms va ModelForms",
        "content": """# 📝 46. Django Forms va ModelForms — Dars dokumentatsiyasi

`Django Forms` va `ModelForms` — **HTML shakllaridan kiritilgan ma'lumotlarni tekshirish (validation) va bazaga xavfsiz saqlash** uchun ishlatiladi.

Bu mavzu orqali:

- `forms.Form` va `forms.ModelForm`;
- `is_valid()`, `cleaned_data` lug'ati;
- CSRF token muhofazasi (`{% csrf_token %}`)

mumkin.

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
""",
        "code": "from django import forms\n\nclass ContactForm(forms.Form):\n    name = forms.CharField(max_length=100)\n    email = forms.EmailField()\n    message = forms.CharField(widget=forms.Textarea)\n\nprint('Django Form sinfi yaratildi.')",
        "code_exp": "- Foydalanuvchidan ma'lumot qabul qilish uchun HTML form validation sinfi.",
        "quiz_q": "Django formalarida kiritilgan ma'lumot to'g'riligini tekshiruvchi metod qaysi?",
        "quiz_opts": ["form.check()", "form.is_valid()", "form.verify()", "form.save()"],
        "quiz_ans": 1,
        "quiz_exp": "is_valid() metodi formadagi barcha maydonlar to'g'ri kiritilganini tekshiradi."
    },

    47: {
        "title": "47-dars — Django ORM munosabatlar (FK, M2M)",
        "content": """# 🔗 47. Django ORM munosabatlar (FK, M2M) — Dars dokumentatsiyasi

`Django ORM Munosabatlar` — **jadvallar o'rtasida ForeignKey (1-to-N) va ManyToManyField (N-to-N) bog'liqliklarini o'rnatish** uchun ishlatiladi.

Bu mavzu orqali:

- `models.ForeignKey(OtherModel, on_delete=models.CASCADE)`;
- `models.ManyToManyField(OtherModel)`;
- `models.OneToOneField(OtherModel)`;
- `related_name` parametri orqali teskari so'rovlar yuborish

mumkin.

---

# 1. Asosiy tushuncha

```python
class Category(models.Model):
    name = models.CharField(max_length=50)

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=100)
```
""",
        "code": "from django.db import models\n\nclass Author(models.Model):\n    name = models.CharField(max_length=100)\n\nclass Book(models.Model):\n    author = models.ForeignKey(Author, on_delete=models.CASCADE)\n    title = models.CharField(max_length=200)\n\nprint('Django ORM ForeignKey munosabati tuzildi.')",
        "code_exp": "- Author va Book o'rtasida One-to-Many munosabatining modeli.",
        "quiz_q": "Ota obyekt o'chirilganda unga bog'liq bola obyektlarni ham o'chirib tashlaydigan on_delete opsiyasi qaysi?",
        "quiz_opts": ["models.SET_NULL", "models.CASCADE", "models.PROTECT", "models.DO_NOTHING"],
        "quiz_ans": 1,
        "quiz_exp": "models.CASCADE ota yozuv o'chganda barcha bog'langan zanjirni avtomatik o'chiradi."
    },

    48: {
        "title": "48-dars — 4-modul imtihoni",
        "content": """# 🎓 48. 4-modul imtihoni — Dars dokumentatsiyasi

`4-modul imtihoni` — 37-darsdan 47-darsgacha o'rganilgan **HTTP, Git, Django Apps, Views, Templates, Models, Admin Panel va ORM ko'nikmalarini sinash** uchun o'tkaziladi.

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
""",
        "code": "def exam_solution_4():\n    print('4-Modul (Django Web va ORM) Imtihon topshirig\\'i bajarildi.')\n\nexam_solution_4()",
        "code_exp": "- `1-3 qatorlar` — 4-modul imtihon topshirig'i bajarilish funksiyasi.",
        "quiz_q": "4-modul imtihonida maksimal ball nechaga teng?",
        "quiz_opts": ["50 ball", "80 ball", "100 ball", "120 ball"],
        "quiz_ans": 2,
        "quiz_exp": "Imtihon 100 ballik shkala bo'yicha baholanadi."
    }
}

def update_37_to_48():
    print("==================================================================")
    print("🚀 37-DARSDAN 48-DARSGACHA BO'LGAN HUJJATLAR TO'G'RILANMOQDA...")
    print("==================================================================")

    all_lessons = list(Lesson.objects.all().order_by('lesson_number'))

    for num in range(37, 49):
        item_data = EXACT_37_TO_48_LESSONS[num]
        lesson_obj = next((l for l in all_lessons if l.lesson_number == num), None)

        code_examples = [
            {
                "id": f"code-{num}-1",
                "title": f"{item_data['title']} — Rasmiy Ishchi Kod",
                "language": "python",
                "code": item_data["code"],
                "explanation": item_data["code_exp"]
            }
        ]

        quiz_questions = [
            {
                "id": f"quiz-{num}-1",
                "question": item_data["quiz_q"],
                "options": item_data["quiz_opts"],
                "correctIndex": item_data["quiz_ans"],
                "explanation": item_data["quiz_exp"]
            }
        ]

        materials = [
            {
                "id": f"mat-{num}-pdf",
                "name": f"{num}_Dars_Konspekt.pdf",
                "type": "pdf",
                "size": "3.0 MB",
                "url": f"https://python-backend.uz/docs/{num}_dars.pdf"
            }
        ]

        student_results = [
            {"id": f"res-{num}-1", "studentName": "Ali Valiyev", "score": 98, "passed": True, "notes": "A'lo bajardi"},
            {"id": f"res-{num}-2", "studentName": "Sardor Karimov", "score": 90, "passed": True, "notes": "Topshiriq bajarildi"}
        ]

        if lesson_obj:
            lesson_obj.title = item_data["title"]
            lesson_obj.content = item_data["content"]
            lesson_obj.code_examples = code_examples
            lesson_obj.quiz_questions = quiz_questions
            lesson_obj.materials = materials
            lesson_obj.student_results = student_results
            lesson_obj.save()
            print(f"✅ [{num}-DARS: {item_data['title']}] -> Foydalanuvchi taqdim etgan shablonda TO'G'RILANDI.")

    with open(LESSONS_JSON, "r", encoding="utf-8") as f:
        json_data = json.load(f)

    for item in json_data:
        num = item.get("lessonNumber")
        if num in EXACT_37_TO_48_LESSONS:
            ex = EXACT_37_TO_48_LESSONS[num]
            item["title"] = ex["title"]
            item["content"] = ex["content"]
            item["codeExamples"] = [
                {
                    "id": f"code-{num}-1",
                    "title": f"{ex['title']} — Rasmiy Ishchi Kod",
                    "language": "python",
                    "code": ex["code"],
                    "explanation": ex["code_exp"]
                }
            ]
            item["quizQuestions"] = [
                {
                    "id": f"quiz-{num}-1",
                    "question": ex["quiz_q"],
                    "options": ex["quiz_opts"],
                    "correctIndex": ex["quiz_ans"],
                    "explanation": ex["quiz_exp"]
                }
            ]

    with open(LESSONS_JSON, "w", encoding="utf-8") as f:
        json.dump(json_data, f, ensure_ascii=False, indent=2)

    print("==================================================================")
    print("✨ 37-DARSDAN 48-DARSGACHA BO'LGAN DARSLAR SHABLON BO'YICHA TO'G'RILANDI!")
    print("==================================================================")

if __name__ == "__main__":
    update_37_to_48()
