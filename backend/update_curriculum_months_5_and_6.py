import os
import sys
import django

# Setup Django Environment
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from lessons_app.models import Lesson
from populate_month_6_and_all import generate_full_markdown, DOCS_DIR

print("🚀 Starting curriculum update for Month 5 (49-60) and Month 6 (61-72)...")

# Definition of exact user requested curriculum for Month 5 (49-60) and Month 6 (61-72)
SPECIFIC_LESSONS_DATA = [
    # =========================================================================
    # 📅 5-OY: Django Asoslari va MVT Arxitekturasi (Darslar 49 - 60)
    # =========================================================================
    {
        "number": 49,
        "emoji": "🏛️",
        "title": "Kirish va MVT Arxitekturasi",
        "topic_desc": "Django nima va u qanday ishlaydi. MVT (Model-View-Template) zanjirini hayotiy misollar bilan tushuntirish. django-admin startproject va startapp farqi.",
        "syntax_code": """# Django loyihasini yaratish va ilova qo'shish
django-admin startproject core .
python manage.py startapp main

# settings.py ichida ilovani ro'yxatdan o'tkazish
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Bizning ilova:
    'main',
]""",
        "syntax_explanation": "django-admin startproject butun loyiha konfiguratsiyasini yaratadi, startapp esa mantiqiy modullarni (app) tashkil etadi.",
        "real_project_title": "Birinchi Django MVT Veb Sayti",
        "real_project_code": """from django.http import HttpResponse
from django.shortcuts import render

def home_view(request):
    context = {
        'site_name': 'marimovdev',
        'course_name': 'Django Backend & MVT',
        'students_count': 25
    }
    return render(request, 'home.html', context)""",
        "real_project_explanation": "MVT arxitekturasida View so'rovni qabul qiladi, kontekst ma'lumotlarini Template (home.html) ga uzatadi va foydalanuvchiga HTML sahifa qaytaradi.",
        "next_title": "50-dars: Models va Baza (ORM)"
    },
    {
        "number": 50,
        "emoji": "🗄️",
        "title": "Models va Baza (ORM)",
        "topic_desc": "Jadvallar tuzish. Asosiy urg'u: OneToOne, ForeignKey va ManyToMany bog'lanishlari. makemigrations qanday qilib Python kodini SQL ga o'girishi.",
        "syntax_code": """from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

class Tag(models.Model):
    name = models.CharField(max_length=50)
    books = models.ManyToManyField(Book, related_name='tags')""",
        "syntax_explanation": "ForeignKey birga-ko'p (1:N) bog'lanishni, ManyToMany (N:M) esa ko'pga-ko'p bog'lanishni ma'lumotlar bazasi darajasida yaratadi.",
        "real_project_title": "E-Commerce Mahsulot va Kategoriya Modellari",
        "real_project_code": """from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name""",
        "real_project_explanation": "Product va Category o'rtasida ForeignKey bog'lanishi orqali har bir mahsulot bir kategoriyaga tegishli bo'ladi.",
        "next_title": "51-dars: Templates (DTL)"
    },
    {
        "number": 51,
        "emoji": "📝",
        "title": "Templates (DTL)",
        "topic_desc": "Backend'dagi ma'lumotni HTML ga chiqarish. {% for %}, {% if %} va {{ variable }} sintaksisi. Sahifalarni {% extends 'base.html' %} orqali qismlarga bo'lish.",
        "syntax_code": """{% extends 'base.html' %}

{% block content %}
<h2>{{ category.title }}</h2>
{% if products %}
  <ul>
  {% for product in products %}
    <li>{{ product.name }} — {{ product.price }} so'm</li>
  {% endfor %}
  </ul>
{% else %}
  <p>Mahsulotlar topilmadi.</p>
{% endif %}
{% endblock %}""",
        "syntax_explanation": "DTL (Django Template Language) yordamida backend o'zgaruvchilari va sikl/shart operatorlari HTML ichida dinamik ravishda render qilinadi.",
        "real_project_title": "Base Template va Layout Inheritancesi",
        "real_project_code": """<!-- base.html -->
<!DOCTYPE html>
<html lang="uz">
<head>
  <meta charset="UTF-8">
  <title>{% block title %}marimovdev{% endblock %}</title>
</head>
<body>
  <header><h1>marimovdev O'quv Markazi</h1></header>
  <main>{% block content %}{% endblock %}</main>
  <footer>© 2026 marimovdev</footer>
</body>
</html>""",
        "real_project_explanation": "base.html barcha sahifalar uchun umumiy karkas bo'lib xizmat qiladi, {% extends %} va {% block %} takrorlanishning oldini oladi.",
        "next_title": "52-dars: Views va Routing (URLs)"
    },
    {
        "number": 52,
        "emoji": "🛤️",
        "title": "Views va Routing (URLs)",
        "topic_desc": "Foydalanuvchi manzilga kirganda qaysi funksiya ishlashini belgilash. Dinamik manzillar: <int:id> orqali bitta mahsulotning to'liq sahifasini ochish.",
        "syntax_code": """# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('product/<int:id>/', views.product_detail, name='product_detail'),
]

# views.py
from django.shortcuts import render, get_object_or_404
from .models import Product

def product_detail(request, id):
    product = get_object_or_404(Product, pk=id)
    return render(request, 'detail.html', {'product': product})""",
        "syntax_explanation": "URL dagi <int:id> dinamik parametri funksiyaga id argumenti sifatida uzatiladi va 404 tekshiruvi bajariladi.",
        "real_project_title": "Dinamik URL va Mahsulot Batafsil Sahifasi",
        "real_project_code": """from django.shortcuts import render, get_object_or_404
from .models import Product

def product_detail_view(request, id):
    product = get_object_or_404(Product, pk=id)
    related_products = Product.objects.filter(category=product.category).exclude(id=product.id)[:4]
    return render(request, 'product_detail.html', {
        'product': product,
        'related_products': related_products
    })""",
        "real_project_explanation": "Dinamik URL parametr orqali muayyan mahsulot va unga tegishli turdosh mahsulotlar olinadi va render qilinadi.",
        "next_title": "53-dars: Admin Panel va QuerySet"
    },
    {
        "number": 53,
        "emoji": "⚙️",
        "title": "Admin Panel va QuerySet",
        "topic_desc": "admin.py ni chiroyli sozlash (list_display, search_fields). Bazaga so'rov yuborish: all(), filter(), get(). N+1 muammosi va select_related() haqida qisqacha.",
        "syntax_code": """from django.contrib import admin
from .models import Product, Category

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'price', 'created_at')
    list_filter = ('category', 'created_at')
    search_fields = ('name', 'description')

# QuerySet Optimizatsiyasi (N+1 Muammosini Hal Qilish)
products = Product.objects.select_related('category').all()""",
        "syntax_explanation": "select_related() SQL JOIN so'rovini hosil qilib, N+1 baza so'rovlari muammosining oldini oladi va tizim tezligini 10 barobargacha oshiradi.",
        "real_project_title": "Professional Admin Panel va Optimizatsiyalangan QuerySet",
        "real_project_code": """from django.contrib import admin
from .models import Course, Student

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'get_students_count')
    search_fields = ('title',)

    def get_students_count(self, obj):
        return obj.students.count()
    get_students_count.short_description = "Talabalar Soni"

def get_optimized_courses():
    return Course.objects.prefetch_related('students').all()""",
        "real_project_explanation": "ModelAdmin sinfida list_display va prefetch_related qo'llanilganda backend tezligi va admin panel qulayligi maksimal darajaga yetadi.",
        "next_title": "54-dars: Oddiy Formalar va CSRF"
    },
    {
        "number": 54,
        "emoji": "📩",
        "title": "Oddiy Formalar va CSRF",
        "topic_desc": "HTML <form> orqali ma'lumot jo'natish. Xakerlik hujumlaridan himoyalanish uchun majburiy {% csrf_token %} mantig'i. Ma'lumotni tutib olish (request.POST).",
        "syntax_code": """<!-- contact.html -->
<form method="POST" action="/contact/">
  {% csrf_token %}
  <input type="text" name="username" placeholder="Ismingiz">
  <textarea name="message" placeholder="Xabaringiz"></textarea>
  <button type="submit">Yuborish</button>
</form>

# views.py
def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        msg = request.POST.get('message')
        # Ma'lumotni qayta ishlash...""",
        "syntax_explanation": "{% csrf_token %} xakerlik hujumlari (Cross-Site Request Forgery) dan saqlash uchun maxsus token yaratadi, request.POST esa kelgan HTML forma ma'lumotlarini o'qiydi.",
        "real_project_title": "Fikr va Aloqa Formasini Ishga Tushirish",
        "real_project_code": """from django.shortcuts import render, redirect
from django.http import HttpResponse

def feedback_view(request):
    if request.method == 'POST':
        author = request.POST.get('author')
        content = request.POST.get('content')
        if author and content:
            # Bazaga yoki Telegram botga yuborish
            return redirect('success_page')
    return render(request, 'feedback.html')""",
        "real_project_explanation": "Foydalanuvchilar tomonidan yuborilgan formalar request.POST orqali qabul qilinadi va xavfsiz qayta ishlanadi.",
        "next_title": "55-dars: ModelForms va Create/Read"
    },
    {
        "number": 55,
        "emoji": "📋",
        "title": "ModelForms va Create/Read",
        "topic_desc": "HTML formalarni qo'lda yozmaslik uchun forms.py dan foydalanish. Saytning o'zidan turib ma'lumot qo'shish (Create) va uni ro'yxatda ko'rish (Read).",
        "syntax_code": "# forms.py\nfrom django import forms\nfrom .models import Article\n\nclass ArticleForm(forms.ModelForm):\n    class Meta:\n        model = Article\n        fields = ['title', 'content', 'category']\n\n# views.py\ndef create_article(request):\n    form = ArticleForm(request.POST or None)\n    if form.is_valid():\n        form.save()\n        return redirect('article_list')",
        "syntax_explanation": "ModelForm ma'lumotlar bazasi modelidan avtomatik ravishda HTML va Python validatsiyali formalarni yasaydi.",
        "real_project_title": "E-Commerce Mahsulot Yaratish va Ro'yxatini Ko'rish (Create/Read)",
        "real_project_code": """from django.shortcuts import render, redirect
from .forms import ProductForm
from .models import Product

def product_list_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    
    products = Product.objects.all().order_by('-created_at')
    return render(request, 'products.html', {'form': form, 'products': products})""",
        "real_project_explanation": "ModelForm orqali bitta view funksiyasining o'zida ham yangi mahsulot qo'shish (Create), ham ro'yxatni chiqarish (Read) amalga oshiriladi.",
        "next_title": "56-dars: Update, Delete va Messages"
    },
    {
        "number": 56,
        "emoji": "✏️",
        "title": "Update, Delete va Messages",
        "topic_desc": "Mahsulotni tahrirlash (ichiga eski ma'lumotni joylab berish) va o'chirish. Ish bitgach, ekranga messages.success yordamida Yashil 'Saqlandi' xabarini chiqarish.",
        "syntax_code": """from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Product
from .forms import ProductForm

def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid():
        form.save()
        messages.success(request, "Mahsulot muvaffaqiyatli saqlandi! ✅")
        return redirect('product_list')
    return render(request, 'update.html', {'form': form})""",
        "syntax_explanation": "instance=product parametri forma ichiga mavjud ma'lumotlarni to'ldirib beradi, messages.success esa flash bildirishnoma chiqaradi.",
        "real_project_title": "To'liq CRUD va Flash Xabarnomalar",
        "real_project_code": """from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Product

def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        messages.warning(request, "Mahsulot bazadan o'chirildi! 🗑️")
        return redirect('product_list')
    return render(request, 'confirm_delete.html', {'product': product})""",
        "real_project_explanation": "Mahsulotni tahrirlash va o'chirish jarayonlaridan so'ng ekranga chiroyli xabarlar (Messages Framework) uzatiladi.",
        "next_title": "57-dars: Static va Media fayllar"
    },
    {
        "number": 57,
        "emoji": "🖼️",
        "title": "Static va Media fayllar",
        "topic_desc": "CSS/JS va rasmlar bilan ishlash arxitekturasi. settings.py da MEDIA_URL va MEDIA_ROOT sozlash. Foydalanuvchi yuklagan rasmni ekranda to'g'ri chiqarish.",
        "syntax_code": """# settings.py
STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static']

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# urls.py
from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)""",
        "syntax_explanation": "MEDIA_ROOT foydalanuvchilar yuklagan fayllar va rasmlar diskda qayerda saqlanishini, MEDIA_URL esa brauzerdagi URL manzilini belgilaydi.",
        "real_project_title": "Rasmli Mahsulotlar Galeriyasi va Static Layout",
        "real_project_code": """<!-- template.html -->
{% load static %}
<link rel="stylesheet" href="{% static 'css/style.css' %}">

{% for p in products %}
  <div className="card">
    {% if p.image %}
      <img src="{{ p.image.url }}" alt="{{ p.name }}">
    {% else %}
      <img src="{% static 'images/no-image.png' %}" alt="No Image">
    {% endif %}
    <h3>{{ p.name }}</h3>
  </div>
{% endfor %}""",
        "real_project_explanation": "Static fayllar {% static %} teglar orqali, yuklangan fayllar esa .image.url atributi orqali HTML sahifaga joylashtiriladi.",
        "next_title": "58-dars: Avtorizatsiya (Login/Register)"
    },
    {
        "number": 58,
        "emoji": "🔑",
        "title": "Avtorizatsiya (Login/Register)",
        "topic_desc": "Django'ning tayyor User modeli. O'quvchilarga Ro'yxatdan o'tish formasi (UserCreationForm), Tizimga kirish va chiqish mantig'ini qo'lda yozdirish.",
        "syntax_code": """from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect

def register_view(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        login(request, user)
        return redirect('home')
    return render(request, 'register.html', {'form': form})""",
        "syntax_explanation": "UserCreationForm yangi foydalanuvchini xavfsiz (parolni hashlab) ro'yxatdan o'tkazadi, login() esa uni tizimga kiritadi.",
        "real_project_title": "To'liq Tizimga Kirish va Chiqish Tizimi",
        "real_project_code": """from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect

def login_view(request):
    form = AuthenticationForm(request, data=request.POST or None)
    if form.is_valid():
        user = form.get_user()
        login(request, user)
        return redirect('home')
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')""",
        "real_project_explanation": "AuthenticationForm foydalanuvchining login va parolini tekshirib, login() va logout() orqali seansni boshqaradi.",
        "next_title": "59-dars: Ruxsatlar va Huquqlar"
    },
    {
        "number": 59,
        "emoji": "🛡️",
        "title": "Ruxsatlar va Huquqlar",
        "topic_desc": "Saytdagi yopiq sahifalarga kirmaslik uchun @login_required ishlatish. Faqat post egasigina o'z postini tahrirlay olishi yoki o'chirishini shart operatorida tekshirish.",
        "syntax_code": """from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseForbidden

@login_required(login_url='login')
def edit_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.author != request.user:
        return HttpResponseForbidden("Siz faqat o'z postingizni tahrirlashingiz mumkin!")
    # Tahrirlash mantig'i...""",
        "syntax_explanation": "@login_required avtorizatsiyadan o'tmaganlarni login sahifasiga yo'naltiradi, post.author != request.user esa mualliflik huquqini tekshiradi.",
        "real_project_title": "Foydalanuvchi Shaxsiy Kabineti va Mualliflik Himoyasi",
        "real_project_code": """from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Article

@login_required
def delete_article(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if article.author == request.user or request.user.is_superuser:
        article.delete()
        return redirect('my_articles')
    return render(request, 'error.html', {'message': "Huquqingiz yetarli emas"})""",
        "real_project_explanation": "@login_required va mualliflik tekshiruvi orqali begona shaxslarning ma'lumotlarni o'zgartirishi yoki o'chirishi oldi olinadi.",
        "next_title": "60-dars: Class Based Views (CBV)"
    },
    {
        "number": 60,
        "emoji": "🏆",
        "title": "Class Based Views (CBV)",
        "topic_desc": "Ortiqcha kodlardan qutulish. ListView, DetailView, CreateView orqali 20 qatorlik FBV kodini 3 qatorga tushirish sirlari. (Oraliq loyiha himoyasi).",
        "syntax_code": """from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from .models import Product

class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'
    context_object_name = 'products'

class ProductCreateView(CreateView):
    model = Product
    fields = ['name', 'price', 'category', 'image']
    template_name = 'product_form.html'
    success_url = reverse_lazy('product_list')""",
        "syntax_explanation": "CBV (ListView, CreateView) yordamida standart CRUD ko'rinishlari minimal kod bilan va yuqori optimizatsiyada yoziladi.",
        "real_project_title": "CBV Asosidagi Full-Stack Veb Sayt va Oraliq Himoya Loyihasi",
        "real_project_code": """from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import News

class NewsListView(ListView):
    model = News
    template_name = 'news_list.html'
    paginate_by = 10

class NewsCreateView(LoginRequiredMixin, CreateView):
    model = News
    fields = ['title', 'content', 'image']
    success_url = reverse_lazy('news_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)""",
        "real_project_explanation": "LoginRequiredMixin va CBV sinflari yordamida 5-Modul yakuniy to'liq web sayt loyihasi amalga oshiriladi va himoya qilinadi.",
        "next_title": "61-dars: API va DRF Asoslari"
    },

    # =========================================================================
    # 🚀 6-OY: REST API, Bot Integratsiyasi va Deployment (Darslar 61 - 72)
    # =========================================================================
    {
        "number": 61,
        "emoji": "🌐",
        "title": "API va DRF Asoslari",
        "topic_desc": "API bu ikki xil dastur (Bot va Sayt) gaplashadigan til ekanligi (JSON). djangorestframework o'rnatish. Postman dasturi orqali dastlabki API so'rovlarni yuborish.",
        "syntax_code": """# settings.py
INSTALLED_APPS = [
    ...
    'rest_framework',
]

# views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET', 'POST'])
def test_api(request):
    if request.method == 'POST':
        return Response({"status": "received", "data": request.data})
    return Response({"message": "Hello DRF REST API!"})""",
        "syntax_explanation": "DRF (Django REST Framework) API yaratishni ta'minlaydi, @api_view esa funksiyaga JSON so'rov va javoblarni boshqarish huquqini beradi.",
        "real_project_title": "Birinchi REST API Endpoint va Postman Integratsiyasi",
        "real_project_code": """from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET'])
def get_server_status(request):
    data = {
        'status': 'online',
        'server_time': '2026-09-07 14:00',
        'version': '1.0.0'
    }
    return Response(data, status=status.HTTP_200_OK)""",
        "real_project_explanation": "Postman orqali ushbu GET API endpointiga so'rov yuborilganda server holati JSON ko'rinishida qaytadi.",
        "next_title": "62-dars: Serializers"
    },
    {
        "number": 62,
        "emoji": "🔄",
        "title": "Serializers",
        "topic_desc": "Pythondagi murakkab ORM obyektini JSON'ga tarjima qiluvchi mexanizm. ModelSerializer orqali bazadagi maydonlarni tashqariga ochish.",
        "syntax_code": "# serializers.py\nfrom rest_framework import serializers\nfrom .models import Product\n\nclass ProductSerializer(serializers.ModelSerializer):\n    class Meta:\n        model = Product\n        fields = ['id', 'name', 'price', 'category', 'created_at']",
        "syntax_explanation": "ModelSerializer Django Modelidagi maydonlarni avtomatik ravishda JSON formatiga va aksincha (deserialization) o'tkazadi.",
        "real_project_title": "Product va Category Modellari uchun Serializerlar",
        "real_project_code": """from rest_framework import serializers
from .models import Category, Product

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.title', read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'category', 'category_name', 'created_at']""",
        "real_project_explanation": "serializers.CharField orqali bog'langan Category obyektining nomini ham JSON javobga qo'shish amalga oshiriladi.",
        "next_title": "63-dars: DRF Views (API yozish)"
    },
    {
        "number": 63,
        "emoji": "🛠️",
        "title": "DRF Views (API yozish)",
        "topic_desc": "@api_view(['GET', 'POST']) orqali oddiy API funksiyalar yozish. Ma'lumotlarni qabul qilish, tozalash (is_valid()) va saqlash.",
        "syntax_code": """from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializers import ProductSerializer

@api_view(['GET', 'POST'])
def product_list_create_api(request):
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)""",
        "syntax_explanation": "is_valid() kelayotgan JSON ning to'g'riligini tekshiradi, serializer.save() esa uni bazaga saqlab 201 Created kodi bilan qaytaradi.",
        "real_project_title": "Bitta Mahsulotni Olish, Yangilash va O'chirish API (Detail)",
        "real_project_code": """@api_view(['GET', 'PUT', 'DELETE'])
def product_detail_api(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response({'error': 'Topilmadi'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)""",
        "real_project_explanation": "FBV API View orqali RESTful standartlariga mos to'liq GET, PUT, DELETE operatsiyalari bajariladi.",
        "next_title": "64-dars: ViewSets va Routers"
    },
    {
        "number": 64,
        "emoji": "⚡",
        "title": "ViewSets va Routers",
        "topic_desc": "DRF'ning eng kuchli quroli. ModelViewSet yordamida bitta klass ichida to'liq CRUD (Get, Post, Put, Delete) ni avtomatlashtirish va DefaultRouter ulash.",
        "syntax_code": """# views.py
from rest_framework.viewsets import ModelViewSet
from .models import Product
from .serializers import ProductSerializer

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# urls.py
from rest_framework.routers import DefaultRouter
from django.urls import path, include

router = DefaultRouter()
router.register('products', ProductViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]""",
        "syntax_explanation": "ModelViewSet va DefaultRouter atigi 5 qator kod bilan to'liq REST API CRUD endpointlarini va Swagger avto-hujjatini yaratadi.",
        "real_project_title": "Kategoriya va Mahsulotlar uchun ViewSet Tizimi",
        "real_project_code": """from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    @action(detail=False, methods=['get'])
    def latest(self, request):
        latest_products = Product.objects.order_by('-created_at')[:5]
        serializer = self.get_serializer(latest_products, many=True)
        return Response(serializer.data)""",
        "real_project_explanation": "@action dekoratori orqali ModelViewSet ichiga qo'shimcha custom endpointlar (masalan: /api/products/latest/) qo'shiladi.",
        "next_title": "65-dars: Token Authentication / JWT"
    },
    {
        "number": 65,
        "emoji": "🔑",
        "title": "Token Authentication / JWT",
        "topic_desc": "API'ni himoya qilish. Har bir foydalanuvchiga Token (kalit) berish va xabarlarni faqat shu kalit orqali berish (Bot kelajakda shu kalit orqali saytga kiradi).",
        "syntax_code": """# settings.py
INSTALLED_APPS += ['rest_framework.authtoken']

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ]
}

# So'rov sarlavhasi (Header):
# Authorization: Token 9944b09199c62bcf9418ad846d39d9b7923f6d0f""",
        "syntax_explanation": "TokenAuthentication har bir so'rov sarlavhasidagi Authorization Token mosligini tekshirib, request.user ni avtomatik yuklaydi.",
        "real_project_title": "JWT (JSON Web Token) Integratsiyasi va SimpleJWT",
        "real_project_code": """# urls.py
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]""",
        "real_project_explanation": "JWT orqali Access va Refresh Tokenlar olinadi. Telegram Bot va Mobil ilovalar ushbu token orqali xavfsiz muloqot qiladi.",
        "next_title": "66-dars: Bot va API Ulanishi (Requests)"
    },
    {
        "number": 66,
        "emoji": "🤖",
        "title": "Bot va API Ulanishi (Requests)",
        "topic_desc": "Aiogram bot ichida aiohttp kutubxonasi orqali Django API'ga so'rov yuborish. Saytdagi bazani bot tugmalariga chiroyli qilib olib kelish.",
        "syntax_code": """import aiohttp

async def fetch_products_from_api():
    url = "http://127.0.0.1:8000/api/products/"
    headers = {"Authorization": "Bearer YOUR_JWT_TOKEN"}
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as response:
            if response.status == 200:
                data = await response.json()
                return data
            return []""",
        "syntax_explanation": "Aiogram bot asinxron bo'lganligi uchun aiohttp orqali Django REST API ga HTTP GET so'rov yuborib, JSON ma'lumotlarni o'qiydi.",
        "real_project_title": "Telegram Botda Django API Mahsulotlarini Tugmalarda Chiqarish",
        "real_project_code": """from aiogram import Router, F
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
import aiohttp

router = Router()

@router.message(F.text == "📦 Mahsulotlar")
async def show_products(message: Message):
    async with aiohttp.ClientSession() as session:
        async with session.get("http://127.0.0.1:8000/api/products/") as resp:
            products = await resp.json()
    
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=f"{p['name']} - {p['price']} so'm", callback_data=f"prod_{p['id']}")]
        for p in products
    ])
    await message.answer("Mavjud mahsulotlar ro'yxati:", reply_markup=keyboard)""",
        "real_project_explanation": "Telegram bot Django REST API'ga ulanib, ma'lumotlar bazasidagi barcha mahsulotlarni jonli Inline tugmalarga aylantirib beradi.",
        "next_title": "67-dars: Bot uchun Webhook"
    },
    {
        "number": 67,
        "emoji": "⚓",
        "title": "Bot uchun Webhook",
        "topic_desc": "Botni 'Long Polling' dan qutqarib, 'Webhook' ga o'tkazish. Telegram serveri to'g'ridan-to'g'ri Django manziliga xabar tashlashi (ngrok orqali test qilish).",
        "syntax_code": """# ngrok orqali local hostni HTTPS ga o'tkazish
# ngrok http 8000

# views.py (Django Webhook Handler)
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json

@csrf_exempt
def telegram_webhook(request):
    if request.method == 'POST':
        update = json.loads(request.body.decode('utf-8'))
        # Aiogram bot dispatcheriga uzatish...
        return HttpResponse('OK')
    return HttpResponse('Method not allowed', status=405)""",
        "syntax_explanation": "Webhook rejimida Telegram serveri har bir yangi xabarni darhol Django loyihamizning /webhook/ URL endpointiga POST so'rovi shaklida yuboradi.",
        "real_project_title": "Ngrok va Django + Aiogram Webhook Integratsiyasi",
        "real_project_code": """from aiogram.types import Update
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
async def bot_webhook_view(request):
    if request.method == "POST":
        data = json.loads(request.body)
        update = Update(**data)
        await dp.feed_update(bot=bot, update=update)
        return JsonResponse({"status": "ok"})
    return JsonResponse({"error": "only POST allowed"}, status=400)""",
        "real_project_explanation": "Telegram serveri yuborgan payload feed_update() orqali Aiogram bot handlerlariga uzatiladi va 100% tezkor ishlaydi.",
        "next_title": "68-dars: Bot ichida Django ORM"
    },
    {
        "number": 68,
        "emoji": "🔌",
        "title": "Bot ichida Django ORM",
        "topic_desc": "API ishlatmasdan, bot va saytni bitta loyiha qilib yozish usuli. Bot ichida os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings') orqali bazani ulash.",
        "syntax_code": """# bot.py (Django loyihasi ildizida)
import os
import sys
import django

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()

# Django ORM modellarini endi bemalol ishlatish mumkin:
from main.models import Product, User

products = Product.objects.all()""",
        "syntax_explanation": "django.setup() funksiyasi Django muhitini va barcha ORM modellarini alohida Python skripti (Bot) ichida ishga tushirib beradi.",
        "real_project_title": "Monolit Django + Aiogram Bot (Direct ORM Access)",
        "real_project_code": """import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from asgiref.sync import sync_to_async
from lessons_app.models import Lesson

@sync_to_async
def get_lessons_count():
    return Lesson.objects.count()

# Bot Handler ichida:
count = await get_lessons_count()
print(f"Jami darslar soni: {count}")""",
        "real_project_explanation": "sync_to_async yordamida Django ORM so'rovlari Aiogram bot asinxron muhitida xavfsiz bajariladi.",
        "next_title": "69-dars: Sinxron Boshqaruv"
    },
    {
        "number": 69,
        "emoji": "📢",
        "title": "Sinxron Boshqaruv",
        "topic_desc": "Django Admin panelda maxsus tugma yasab (Admin Actions), barcha bot a'zolariga birdaniga xabar yuborish (Broadcasting) logikasini yozish.",
        "syntax_code": """# admin.py
from django.contrib import admin
from .models import TelegramUser
import requests

@admin.action(description="Tanlangan foydalanuvchilarga xabar yuborish")
def send_telegram_broadcast(modeladmin, request, queryset):
    bot_token = "BOT_TOKENI"
    for user in queryset:
        url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
        requests.post(url, json={"chat_id": user.telegram_id, "text": "Xushxabar! Yangi chegirmalar e'lon qilindi!"})

class TelegramUserAdmin(admin.ModelAdmin):
    list_display = ('telegram_id', 'full_name', 'created_at')
    actions = [send_telegram_broadcast]""",
        "syntax_explanation": "@admin.action dekoratori Django Admin paneliga belgilangan foydalanuvchilar bo'yicha ommaviy harakatlar (Broadcasting) tugmasini qo'shadi.",
        "real_project_title": "Django Admin Panelidan Telegramga Avtomatik Broadcasting",
        "real_project_code": """from django.contrib import admin
from django.contrib import messages
from .models import BotUser
import asyncio

def broadcast_message_action(modeladmin, request, queryset):
    count = 0
    for user in queryset:
        # Telegram API yuborish
        count += 1
    messages.success(request, f"{count} ta foydalanuvchiga xabar yuborildi! 🚀")

broadcast_message_action.short_description = "📢 Bot orqali xabar tarqatish"

@admin.register(BotUser)
class BotUserAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'username', 'date_joined')
    actions = [broadcast_message_action]""",
        "real_project_explanation": "Admin panel belgilangan barcha o'quvchi va foydalanuvchilarga tugma orqali birdaniga xabar tarqatish imkonini beradi.",
        "next_title": "70-dars: PostgreSQL ga o'tish"
    },
    {
        "number": 70,
        "emoji": "🐘",
        "title": "PostgreSQL ga o'tish",
        "topic_desc": "SQLite3 faqat test uchun ekanligi. Windows ga PostgreSQL o'rnatish, psycopg2-binary kutubxonasi orqali Django'ni unga ulash.",
        "syntax_code": """# pip install psycopg2-binary

# settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'marimovdev_db',
        'USER': 'postgres',
        'PASSWORD': 'strong_password',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}""",
        "syntax_explanation": "PostgreSQL sanoat darajasidagi juda tez, xavfsiz va bir vaqtning o'zida ko'plab so'rovlarni birgalikda bajara oladigan relational ma'lumotlar bazasidir.",
        "real_project_title": "SQLite3 dan PostgreSQL Serverga Migratsiya Qilish",
        "real_project_code": """# 1. PostgreSQL ma'lumotlar bazasini yaratish (pgAdmin yoki psql)
# CREATE DATABASE marimovdev_db;

# 2. Django migratsiyalarini o'tkazish
# python manage.py makemigrations
# python manage.py migrate

# 3. Superuser yaratish
# python manage.py createsuperuser""",
        "real_project_explanation": "DATABASES sozlamasi PostgreSQL ga o'tkazilgach, `python manage.py migrate` amali orqali barcha jadvallar PostgreSQL da qayta quriladi.",
        "next_title": "71-dars: Production Muhit va Gunicorn"
    },
    {
        "number": 71,
        "emoji": "🚀",
        "title": "Production Muhit va Gunicorn",
        "topic_desc": "Dasturni serverga moslash: DEBUG = False, ALLOWED_HOSTS = ['*']. Statik fayllarni bitta joyga yig'ish (python manage.py collectstatic). Gunicorn WSGI HTTP Server.",
        "syntax_code": """# settings.py (Production)
DEBUG = False
ALLOWED_HOSTS = ['python.marimovdev.uz', '127.0.0.1']

STATIC_ROOT = BASE_DIR / 'staticfiles'

# Terminalda statik fayllarni yig'ish:
# python manage.py collectstatic --noinput

# Gunicorn serverini ishga tushirish:
# gunicorn core.wsgi:application --bind 0.0.0.0:8000""",
        "syntax_explanation": "DEBUG=False xavfsizlikni ta'minlaydi, collectstatic barcha CSS/JS/Image fayllarni staticfiles papkasiga to'playdi va Gunicorn uni WSGI orqali yuritadi.",
        "real_project_title": "Production Config va Gunicorn WSGI Server Setup",
        "real_project_code": """# gunicorn.service (/etc/systemd/system/gunicorn.service)
[Unit]
Description=gunicorn daemon for marimovdev
After=network.target

[Service]
User=root
WorkingDirectory=/var/www/dars_reja
ExecStart=/var/www/dars_reja/venv/bin/gunicorn --workers 3 --bind 127.0.0.1:5005 config.wsgi:application

[Install]
WantedBy=multi-user.target""",
        "real_project_explanation": "Gunicorn WSGI serveri Python Django ilovasini Linux systemd background servisi sifatida uzluksiz ishlatib beradi.",
        "next_title": "72-dars: Serverga Deploy (Ubuntu VPS)"
    },
    {
        "number": 72,
        "emoji": "🎓",
        "title": "Serverga Deploy (Ubuntu VPS)",
        "topic_desc": "VPS xarid qilish. Linux terminalida muhit ko'tarish, Nginx va Gunicorn orqali loyihani 24/7 ishlaydigan qilish va domenga SSL ulash. Bitiruv Loyihasi Himoyasi.",
        "syntax_code": """# 1. Nginx Reverse Proxy konfiguratsiyasi (/etc/nginx/sites-available/dars_reja)
server {
    server_name python.marimovdev.uz;

    location / {
        proxy_pass http://127.0.0.1:5005;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }

    location /static/ {
        alias /var/www/dars_reja/staticfiles/;
    }
}

# 2. SSL Certbot o'rnatish
# sudo certbot --nginx -d python.marimovdev.uz""",
        "syntax_explanation": "Nginx teskari proksi (Reverse Proxy) sifatida kelayotgan HTTPS so'rovlarini qabul qilib Gunicorn ga uzatadi va SSL sertifikatini ta'minlaydi.",
        "real_project_title": "Full Production VPS Deploy & Bitiruv Loyihasi Himoyasi",
        "real_project_code": """# Final System Health & Deployment Verification
# 1. Systemd status
# systemctl status gunicorn

# 2. Nginx status
# systemctl status nginx

# 3. Domain Check
# curl -I https://python.marimovdev.uz/api/lessons

print("🎉 6-MODUL VA BUTUN DARS REJASI MUVAFFAQIYATLI YAKUNLANDI!")""",
        "real_project_explanation": "Loyiha VPS Ubuntu serverida Nginx, Gunicorn, PostgreSQL, SSL Certbot va Aiogram Bot bilan birga 24/7 rejimida jonli ishga tushirildi va himoya qilindi.",
        "next_title": "Barcha 72 ta darslar muvaffaqiyatli yakunlandi! 🎉"
    }
]

# Standard template generator
for data in SPECIFIC_LESSONS_DATA:
    num = data["number"]
    emoji = data["emoji"]
    title = data["title"]
    topic_desc = data["topic_desc"]
    syntax_code = data["syntax_code"]
    syntax_explanation = data["syntax_explanation"]
    real_project_title = data["real_project_title"]
    real_project_code = data["real_project_code"]
    real_project_explanation = data["real_project_explanation"]
    next_title = data["next_title"]

    abilities = [
        f"{title} texnologiyalarini noldan mukammal egallash",
        f"Loyiha kodida {topic_desc[:60]}... prinsiplarini qo'llash",
        "Amaliy loyihalarda xavfsizlik va optimizatsiya talablariga rioya etish",
        "Koddagi xatoliklarni mustaqil diagnostika qilish va to'g'rilash"
    ]
    
    goals = [
        f"{title} tushunchasining arxitekturaviy mohiyatini teran anglaydi",
        "Amaliy topshiriqlarni standartlarga mos ravishda xatosiz yozadi",
        "Koddagi murakkab mantiqiy va sintaktik xatolarni bartaraf eta oladi",
        "Real loyihalarda ushbu bilimlardan mustaqil foydalana oladi"
    ]

    prereqs = [
        f"{max(1, num-1)}-dars bilimlari va amaliy ko'nikmalari",
        "Python va Django Backend asoslari",
        "Veb texnologiyalar va ma'lumotlar bazasi prinsiplari"
    ]

    terms = [
        (title.split()[0], topic_desc[:80]),
        ("Arxitektura (Architecture)", "dasturiy ta'minot komponentlarining o'zaro tartiblangan muloqot strukturasi."),
        ("Best Practices", "sohada ko'p yillar davomida sinovdan o'tgan eng samarali va xavfsiz dasturlash usullari."),
        ("Optimizatsiya", "dastur tezligi va resurs sarfini yaxshilash jarayoni.")
    ]

    table_rows = [
        ["Core Function / Component", "Asosiy vazifani bajaradi", "Django / Python", f"{title.split()[0]}()", "Konfiguratsiyada unutish"],
        ["Validation Check", "Ma'lumotlarni tekshiradi", "Boolean / Model", "is_valid() / filter()", "Validatsiyasiz bazaga saqlash"],
        ["Result Response", "Natijani qaytaradi", "HTTP / JSON", "Response() / render()", "Xatolik bo'lganda 500 qaytarish"],
        ["Exception Handling", "Xatolikni ushlaydi", "Try-Except", "try: ... except:", "Xatolikni yutib yuborish"]
    ]

    examples = [
        {
            "name": f"{title} — Boshlang'ich Konfiguratsiya va Ishga Tushirish",
            "code": f"# {num}-dars: {title}\nprint('=== {title} ===')\n# {topic_desc}",
            "output": f"=== {title} ===\nSTATUS: Active & Verified",
            "explanation": "Boshlang'ich konfiguratsiya va texnik sozlash.",
            "context": "Loyihaning dastlabki ishga tushirish bosqichida."
        },
        {
            "name": "Mantiqiy Amal va Parametrlarni Tekshirish",
            "code": """def check_system_config(config):
    if config.get('active'):
        return "Tizim muvaffaqiyatli ishlamoqda"
    return "Sozlamalarni tekshiring"

print(check_system_config({'active': True}))""",
            "output": "Tizim muvaffaqiyatli ishlamoqda",
            "explanation": "Parametrlar va sozlamalarning to'g'riligini tekshirish.",
            "context": "Backend mantiqiy jarayonlarida."
        },
        {
            "name": "Ma'lumotlarni Qayta Ishlash va Saqlash",
            "code": """def process_payload(payload):
    processed = {k: str(v).strip() for k, v in payload.items()}
    return processed

print(process_payload({'title': ' Django  ', 'version': 5.0}))""",
            "output": "{'title': 'Django', 'version': '5.0'}",
            "explanation": "Ma'lumotlarni tozalash va standartlashtirish.",
            "context": "Forma va API payload larini tozalashda."
        },
        {
            "name": "Xatoliklarni Usallash (Exception Handling)",
            "code": """def safe_db_query(query_fn):
    try:
        return query_fn()
    except Exception as e:
        return f"Xatolik yuz berdi: {e}"

print(safe_db_query(lambda: 100 / 1))""",
            "output": "100.0",
            "explanation": "Try-except orqali server to'xtab qolishining oldini olish.",
            "context": "Production backend kodlarida."
        },
        {
            "name": "Ro'yxat va Obyektlarni Filtrlash",
            "code": """data = [{'id': 1, 'status': 'completed'}, {'id': 2, 'status': 'planned'}]
completed = [d for d in data if d['status'] == 'completed']
print(completed)""",
            "output": "[{'id': 1, 'status': 'completed'}]",
            "explanation": "Status bo me'yoriy saralash va filtrlash.",
            "context": "QuerySet va ro'yxat chiqarishda."
        },
        {
            "name": "Kesh va Saqlash Mexanizmi",
            "code": """cache = {}
def get_cached_item(key, fetch_fn):
    if key not in cache:
        cache[key] = fetch_fn()
    return cache[key]

print(get_cached_item('lessons', lambda: 72))""",
            "output": "72",
            "explanation": "Kesh orqali qayta so'rovlarni tezlashtirish.",
            "context": "High-load tizimlarda."
        },
        {
            "name": "Loglarni Ro'yxatga Olish (Logging)",
            "code": """import logging
logging.basicConfig(level=logging.INFO)

def log_system_event(msg):
    logging.info(f"[LOG] {msg}")

log_system_event("Dars muvaffaqiyatli bajarildi")""",
            "explanation": "Dastur hodisalari va loglarni ro'yxatga olish.",
            "context": "Production serverlarda diagnostikada."
        },
        {
            "name": "Yakuniy Integratsiya va Natija",
            "code": f"""def final_status():
    return {{
        'lesson': {num},
        'title': '{title}',
        'status': 'Completed',
        'result': '100% Success'
    }}
print(final_status())""",
            "output": f"{{'lesson': {num}, 'title': '{title}', 'status': 'Completed', 'result': '100% Success'}}",
            "explanation": "Dars amaliyotining yakuniy natijasi.",
            "context": "Imtihon va loyiha himoyasida."
        }
    ]

    errors = [
        {
            "title": "Ma'lumotlar validatsiyasini unutish",
            "wrong": "def save(data):\n    db.insert(data)",
            "reason": "Validatsiyasiz kiritilgan ma'lumot bazani va serverni buzishi mumkin.",
            "correct": "def save(data):\n    if data: db.insert(data)",
            "fix": "Har doim kiritilgan ma'lumotlarni tekshiring."
        },
        {
            "title": "Xatolik kelganda dasturni to'xtatib qo'yish",
            "wrong": "res = 10 / 0",
            "reason": "Exception ushlanmasa server to'xtab qoladi.",
            "correct": "try:\n    res = 10 / 0\nexcept ZeroDivisionError:\n    res = 0",
            "fix": "Try-except bloklaridan unumli foydalaning."
        },
        {
            "title": "Kodni bitta katta funksiyada yozish",
            "wrong": "# 500 qatorli bitta funksiya",
            "reason": "O'qish, tushunish va test qilish juda qiyinlashadi.",
            "correct": "# Modulli kichik funksiyalar",
            "fix": "Kodni kichik mantiqiy bo'laklarga ajrating."
        },
        {
            "title": "Loglar yozmaslik",
            "wrong": "print('xato')",
            "reason": "Production serverda print ko'rinmaydi.",
            "correct": "import logging\nlogging.error('xato')",
            "fix": "Logging modulidan foydalaning."
        }
    ]

    tasks = {
        "easy": f"{title} bo'yicha asosiy sintaksis va tayanch funksiyani yozing.",
        "medium": f"{title} imkoniyatlaridan foydalanib, ma'lumotlarni filtrlovchi dastur tuzing.",
        "hard": f"{title} va oldingi darslar bilimlarini birlashtirgan holda to'liq loyiha modulini yozing va test qiling."
    }

    homework = [
        f"{title} mavzusidagi barcha nazariy bilimlarni va koddagi mantiqni takrorlash",
        "Kod misollarini mustaqil ravishda Python va Django'da yozib ishga tushirish",
        "Amaliy topshiriqlarni (oson, o'rta, murakkab) bajarish",
        "Postman / Brauzer / Terminal orqali natijalarni tekshirish",
        "Tayyor kodlarni GitHub repozitoriyasiga push qilish"
    ]

    quiz_questions = [
        {"question": f"{title} ning asosiy vazifasi nimadan iborat?", "answer": f"Ushbu darsda {topic_desc[:100]}... jarayonlarini amalga oshirish o'rgatiladi."},
        {"question": "Dasturda validatsiyaning maqsadi nima?", "answer": "Mijozdan kelgan ma'lumotlar xavfsizligi va to'g'riligini tekshirish."},
        {"question": "Production serverda print o'rniga nima ishlatiladi?", "answer": "Professional Logging moduli va systemd loglari ishlatiladi."},
        {"question": "Koddagi DRY (Don't Repeat Yourself) tamoyili nima?", "answer": "Kodni qayta takrorlamaslik va modullarga bo'lish usuli."},
        {"question": "HTTP 200 OK kodi nimani bildiradi?", "answer": "So'rov muvaffaqiyatli bajarilganligini bildiruvchi kod."}
    ]

    summary = [
        f"{title} texnologiyasi asoslari",
        f"{topic_desc[:80]}...",
        "Amaliy kod misollari va optimizatsiya usullari",
        "Production va deployment talablari"
    ]

    resources = [
        "📄 Rasmiy hujjat: https://docs.djangoproject.com/en/5.0/",
        "📄 DRF hujjatlari: https://www.django-rest-framework.org/",
        f"💻 Kodlar: github.com/dars-reja/{num}-dars",
        f"🎬 Video dars: youtube.com/watch?v=dars{num}"
    ]

    content = generate_full_markdown(
        number=num,
        emoji=emoji,
        title=title,
        intro=f"**{title}** — {topic_desc}\n\nUshbu dars davomida biz ushbu mavzuni eng mayda detallarigacha chuqur va amaliy o'rganamiz. Dars davomida har bir tushuncha qadamma-qadam tushuntiriladi hamda real loyihalar misolida mustahkamlanadi.",
        abilities=abilities,
        goals=goals,
        prereqs=prereqs,
        terms=terms,
        syntax_code=syntax_code,
        syntax_explanation=syntax_explanation,
        table_rows=table_rows,
        examples=examples,
        real_project_title=real_project_title,
        real_project_code=real_project_code,
        real_project_explanation=real_project_explanation,
        errors=errors,
        tasks=tasks,
        homework=homework,
        quiz_questions=quiz_questions,
        summary=summary,
        next_lesson_title=next_title,
        resources=resources
    )

    filename = f"dars_{num:02d}.md"
    filepath = os.path.join(DOCS_DIR, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

    lesson_obj, created = Lesson.objects.update_or_create(
        lesson_number=num,
        defaults={
            "lesson_id": f"les-100unique-{num}",
            "title": f"{title}",
            "goal": goals[0],
            "description": topic_desc,
            "content": content,
            "status": "planned",
            "homework": "\n".join(homework)
        }
    )
    print(f"✅ Lesson {num}: {title} updated in DB and disk ({len(content)} chars)")

print("✨ Month 5 (49-60) and Month 6 (61-72) successfully updated with user requested curriculum!")
