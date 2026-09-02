import os
import sys
import django

# Setup Django Environment
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from lessons_app.models import Lesson
from populate_month_6_and_all import generate_full_markdown, DOCS_DIR

# Define full data dictionaries for Lessons 61 through 72
LESSONS_DATA = [
    # 61-DARS: DRF Intro
    {
        "number": 61,
        "emoji": "🌐",
        "title": "Django REST Framework (DRF) va Web API ga Kirish",
        "intro": """Web va Mobil ilovalar o'rtasida ma'lumotlarni xavfsiz va standart asosida almashish uchun **REST API (Representational State Transfer API)** texnologiyasi ishlatiladi. Python va Django dunyosida eng ommabop, tezkor va xavfsiz API freymvork bu **Django REST Framework (DRF)** hisoblanadi.

Ushbu darsda biz HTTP protokoli metodlari (GET, POST, PUT, PATCH, DELETE), JSON shaklidagi ma'lumotlar formati hamda `@api_view` dekoratori yordamida birinchi REST API endpointlarini tuzishni noldan o'rganamiz.""",
        "abilities": [
            "Django loyihasiga Django REST Framework (DRF)ni o'rnatish va sozlash",
            "JSON formati bilan ishlash va obyektlarni serialization qilish",
            "GET, POST, PUT, DELETE HTTP so'rovlariga mos endpointlar yozish",
            "@api_view dekoratori yordamida Function-Based API View tuzish"
        ],
        "goals": [
            "DRF arxitekturasini tushunadi va settings.py ga to'g'ri integratsiya qiladi",
            "REST API va klassik Django MVT o'rtasidagi farqni izohlay oladi",
            "Response() va status kodlar (200 OK, 201 Created, 400 Bad Request) bilan ishlaydi",
            "Postman va brauzer orqali API so'rovlarini mustaqil sinab ko'ra oladi"
        ],
        "prereqs": [
            "53-56 darslar (Django Framework va Loyiha Strukturasi)",
            "58-dars (Django Models va ORM So'rovlari)",
            "37-dars (HTTP so'rovlar va JSON formati)"
        ],
        "terms": [
            ("REST API", "dasturlar o'rtasida HTTP protokoli orqali JSON yoki XML shaklida ma'lumot almashish standarti."),
            ("Serialization", "Python/Django Model obyektlarini brauzer yoki mobil ilova tushunadigan JSON formatiga o'tkazish jarayoni."),
            ("Response", "DRF tomonidan mijozga qaytariladigan va kontent turini (Content-Type) avtomatik moslashtiradigan HTTP javob obyekti."),
            ("Status Code", "HTTP javobining holatini bildiruvchi 3 xonali sonlar (masalan: 200 - Muvaffaqiyatli, 404 - Topilmadi).")
        ],
        "syntax_code": """from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def sample_api_view(request):
    if request.method == 'GET':
        return Response({"message": "GET so'rovi qabul qilindi"}, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        data = request.data
        return Response({"received": data}, status=status.HTTP_201_CREATED)""",
        "syntax_explanation": "@api_view dekoratori funksiyani DRF API view rejimiga o'tkazadi va request.data orqali kelgan JSON ma'lumotlarini qabul qiladi.",
        "table_rows": [
            ["@api_view(['GET'])", "HTTP metodlarini cheklaydi", "List[str]", "@api_view(['GET', 'POST'])", "Metodni ko'rsatmaslik"],
            ["Response(data)", "JSON javob qaytaradi", "Dict / List", "Response({'ok': True})", "Oddiy dict qaytarish"],
            ["request.data", "POST/PUT ma'lumotlarini o'qiydi", "Dict / QueryDict", "title = request.data.get('title')", "request.POST ni ishlatish"],
            ["status.HTTP_200_OK", "200 muvaffaqiyat kodi", "int (200)", "status=status.HTTP_200_OK", "String '200' yozish"]
        ],
        "examples": [
            {
                "name": "Oddiy Salomlashish API View",
                "code": """from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def hello_api(request):
    return Response({"message": "Hello, Django REST Framework!"})""",
                "output": "{\"message\": \"Hello, Django REST Framework!\"}",
                "explanation": "Eng sodda GET API view javobi.",
                "context": "API ishga tushganini va ulanishni tekshirishda."
            },
            {
                "name": "POST So'rovi orqali ma'lumot qabul qilish",
                "code": """@api_view(['POST'])
def calculate_sum(request):
    a = request.data.get('a', 0)
    b = request.data.get('b', 0)
    result = int(a) + int(b)
    return Response({"a": a, "b": b, "sum": result})""",
                "output": "{\"a\": 5, \"b\": 10, \"sum\": 15}",
                "explanation": "Mijozdan kelgan JSON ma'lumotni hisoblab qaytarish.",
                "context": "Kalkulyator va backend hisoblash API larida."
            },
            {
                "name": "Status Kodlari bilan Ishlash",
                "code": """from rest_framework import status

@api_view(['POST'])
def create_item(request):
    name = request.data.get('name')
    if not name:
        return Response({"error": "Name maydoni shart!"}, status=status.HTTP_400_BAD_REQUEST)
    return Response({"message": f"'{name}' yaratildi!"}, status=status.HTTP_201_CREATED)""",
                "explanation": "Noto'g'ri so'rovga 400 Bad Request, to'g'risiga 201 Created qaytarish.",
                "context": "Ma'lumotlarni tekshirish va validatsiya jarayonida."
            },
            {
                "name": "Modellar Ro'yxatini Qaytarish (Manual Manual Serialization)",
                "code": """from .models import Course

@api_view(['GET'])
def courses_list_api(request):
    courses = Course.objects.all()
    data = [{"id": c.id, "title": c.title, "price": str(c.price)} for c in courses]
    return Response(data)""",
                "explanation": "Django ORM obyeqtlarini qo'lda ro'yxatga o'tkazib Response berish.",
                "context": "Serializer ishlatmasdan oldingi tushunchalarda."
            },
            {
                "name": "Bitta Obyektni Olish API",
                "code": """@api_view(['GET'])
def get_course_detail(request, pk):
    try:
        c = Course.objects.get(pk=pk)
        return Response({"id": c.id, "title": c.title, "price": str(c.price)})
    except Course.DoesNotExist:
        return Response({"error": "Topilmadi"}, status=status.HTTP_404_NOT_FOUND)""",
                "explanation": "ID bo'yicha obyektni olish yoki 404 qaytarish.",
                "context": "Batafsil ma'lumotlarni ko'rish endpointlarida."
            },
            {
                "name": "PUT update API",
                "code": """@api_view(['PUT'])
def update_course(request, pk):
    try:
        c = Course.objects.get(pk=pk)
        c.title = request.data.get('title', c.title)
        c.save()
        return Response({"message": "Yangilandi", "id": c.id, "title": c.title})
    except Course.DoesNotExist:
        return Response({"error": "Topilmadi"}, status=status.HTTP_404_NOT_FOUND)""",
                "explanation": "Obyekt ma'lumotlarini yangilash.",
                "context": "Tahrirlash va ma'lumotlarni o'zgartirishda."
            },
            {
                "name": "DELETE O'chirish API",
                "code": """@api_view(['DELETE'])
def delete_course(request, pk):
    try:
        c = Course.objects.get(pk=pk)
        c.delete()
        return Response({"message": "O'chirildi"}, status=status.HTTP_204_NO_CONTENT)
    except Course.DoesNotExist:
        return Response({"error": "Topilmadi"}, status=status.HTTP_404_NOT_FOUND)""",
                "explanation": "204 No Content stutus kodi bilan ma'lumotni o'chirish.",
                "context": "Ma'lumotlarni o'chirish operatsiyalarida."
            },
            {
                "name": "So'rov parametrlarini (Query Params) o'qish",
                "code": """@api_view(['GET'])
def search_courses(request):
    query = request.query_params.get('q', '')
    courses = Course.objects.filter(title__icontains=query)
    data = [{"id": c.id, "title": c.title} for c in courses]
    return Response({"query": query, "count": len(data), "results": data})""",
                "explanation": "GET parametrlarini `request.query_params` orqali filtrlash.",
                "context": "Qidiruv va filtrlash tizimlarida."
            }
        ],
        "real_project_title": "To'liq REST API CRUD Endpoints Tizimi",
        "real_project_code": """from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Product

@api_view(['GET', 'POST'])
def product_list_create_api(request):
    if request.method == 'GET':
        products = Product.objects.all()
        data = [{"id": p.id, "name": p.name, "price": str(p.price)} for p in products]
        return Response(data, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        name = request.data.get('name')
        price = request.data.get('price')
        if not name or not price:
            return Response({"error": "Barcha maydonlar shart"}, status=status.HTTP_400_BAD_REQUEST)
        p = Product.objects.create(name=name, price=price)
        return Response({"id": p.id, "name": p.name, "price": str(p.price)}, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def product_detail_api(request, pk):
    product = get_object_or_404(Product, pk=pk)
    
    if request.method == 'GET':
        return Response({"id": product.id, "name": product.name, "price": str(product.price)})
    elif request.method == 'PUT':
        product.name = request.data.get('name', product.name)
        product.price = request.data.get('price', product.price)
        product.save()
        return Response({"id": product.id, "name": product.name, "price": str(product.price)})
    elif request.method == 'DELETE':
        product.delete()
        return Response({"message": "Product o'chirildi"}, status=status.HTTP_204_NO_CONTENT)""",
        "real_project_explanation": "Ushbu loyihada mahsulotlar (Product) ro'yxatini olish, yangi yaratish, bittasini tahrirlash va o'chirish uchun to'liq REST API yozilgan.",
        "errors": [
            {
                "title": "Response o'rniga HttpResponse qaytarish",
                "wrong": "return HttpResponse({'ok': True})",
                "reason": "HttpResponse dict ma'lumotini avtomatik JSON ga o'girmaydi.",
                "correct": "return Response({'ok': True})",
                "fix": "DRF ning Response obyektidan foydalaning."
            },
            {
                "title": "request.data o'rniga request.POST ni ishlatish",
                "wrong": "name = request.POST.get('name')",
                "reason": "request.POST faqat HTML form data ni o'qiydi, JSON payload larni o'qiy olmaydi.",
                "correct": "name = request.data.get('name')",
                "fix": "DRF ning request.data atributidan foydalaning."
            },
            {
                "title": "@api_view dekoratorisiz Response berish",
                "wrong": "def my_view(request):\n    return Response({'test': 1})",
                "reason": "@api_view bo'lmasa DRF ning Render va Request konteksti yuklanmaydi va xatolik beradi.",
                "correct": "@api_view(['GET'])\ndef my_view(request):\n    return Response({'test': 1})",
                "fix": "View funksiyasi tepasiga @api_view() qo'shing."
            },
            {
                "title": "Status kodlarni matn shaklida berish",
                "wrong": "return Response(data, status='200')",
                "reason": "Status parametri integer turida bo'lishi kerak.",
                "correct": "return Response(data, status=status.HTTP_200_OK)",
                "fix": "DRF status konstanta qiymatlarini ishlating."
            }
        ],
        "tasks": {
            "easy": "GET so'roviga xizmat qiluvchi va {'status': 'active', 'version': '1.0'} qaytaruvchi API endpoint yozing.",
            "medium": "POST so'rovida foydalanuvchining yoshini qabul qilib, uning voyaga yetganligini (is_adult: True/False) qaytaruvchi API yarating.",
            "hard": "Student modelidagi barcha o'quvchilar ro'yxatini va yangi o'quvchi qo'shish imkonini beruvchi to'liq CRUD API View yozing."
        },
        "homework": [
            "Django loyihangizga djangorestframework paketini o'rnating va settings.py ga qo'shing",
            "Book modeli uchun GET, POST, PUT va DELETE API endpointlarini tuzing",
            "Postman dasturida barcha endpointlarni test qiling va so'rov natijalarini saqlang",
            "Xatoliklar yuz berganda mos HTTP status kodlarini (400, 404, 500) qaytarishni sozlang",
            "Dastur kodlarini GitHub ga yuklang"
        ],
        "quiz_questions": [
            {"question": "REST API da JSON ma'lumotlarini qaysi parametr orqali o'qiladi?", "answer": "DRF da request.data atributi orqali kelgan barcha JSON payload lar o'qib olinadi."},
            {"question": "DRF da API view yaratish uchun qaysi dekorator shart?", "answer": "@api_view(['GET', 'POST', ...]) dekoratori funksiyani API view holatiga o'tkazadi."},
            {"question": "Yangi obyekt yaratilganda qaysi HTTP status kodi qaytariladi?", "answer": "201 Created (status.HTTP_201_CREATED) kodi qaytarilishi standart hisoblanadi."},
            {"question": "Serializatsiyaning asosiy maqsadi nima?", "answer": "Python Model obyektlarini JSON formatiga va aksincha o'tkazishdir."},
            {"question": "Obyekt topilmaganda qaysi status kodi beriladi?", "answer": "404 Not Found (status.HTTP_404_NOT_FOUND) status kodi qaytariladi."}
        ],
        "summary": [
            "DRF frameworki va REST API asoslari",
            "@api_view dekoratori va HTTP metodlari",
            "Response obyekti va status kodlari",
            "JSON payload lar va request.data bilan ishlash"
        ],
        "next_lesson_title": "DRF Serializers va ModelSerializers",
        "resources": [
            "📄 Rasmiy hujjat: https://www.django-rest-framework.org/",
            "📄 HTTP Status Codes: https://httpstatuses.com/",
            "💻 Kodlar: github.com/dars-reja/61-dars",
            "🎬 Video dars: youtube.com/watch?v=drf61"
        ]
    },

    # 62-DARS: Serializers
    {
        "number": 62,
        "emoji": "🔄",
        "title": "DRF Serializers va ModelSerializers",
        "intro": """Django REST Framework ning eng muhim va kuchli komponentlaridan biri bu **Serializer**lar hisoblanadi. Serializer ma'lumotlarni ikkita yo'nalishda o'g'iradi:
1. **Serialization**: Complex Django Model obyeqtlari -> Python dict -> JSON formatiga.
2. **Deserialization**: JSON -> Python dict -> Validatsiya -> Django Model obyeqtiga.

Ushbu darsda biz `serializers.Serializer` va `serializers.ModelSerializer` sinflarini hamda maydonlarni validatsiya qilish usullarini o'rganamiz.""",
        "abilities": [
            "ModelSerializers sinflarini yaratish va sozlash",
            "Fields va read_only_fields parametrlarini belgilash",
            "Custom field validation (validate_<fieldname>) yozish",
            "Nested (ichma-ich) serializerlar bilan ishlash"
        ],
        "goals": [
            "Serializer va ModelSerializer o'rtasidagi farqni tushunadi",
            "Deserialization paytida is_valid() va save() funksiyalarini to'g'ri chaqiradi",
            "API orqali kelayotgan ma'lumotlarga qat'iy mantiqiy cheklovlar va validatsiyalar qo'ya oladi",
            "Ma'lumotlar bazasi obyektlarini avtomatik JSON ga o'tkazishni bajaradi"
        ],
        "prereqs": [
            "61-dars (DRF va Web API ga Kirish)",
            "58-dars (Django Models va ORM)"
        ],
        "terms": [
            ("ModelSerializer", "Django Model shaklidan avtomatik serializer maydonlari va create()/update() metodlarini tuzib beruvchi maxsus sinf."),
            ("Validation", "Mijoz yuborgan JSON ma'lumotlarining to'g'riligi va xavfsizligini `serializer.is_valid()` orqali tekshirish."),
            ("read_only_fields", "Faqat ma'lumotni o'qishda ko'rinadigan, POST/PUT paytida kiritilishi shart bo'lmagan maydonlar.")
        ],
        "syntax_code": """from rest_framework import serializers
from .models import Course

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'title', 'price', 'created_at']
        read_only_fields = ['id', 'created_at']

    def validate_price(self, value):
        if value < 0:
            raise serializers.ValidationError("Narx manfiy bo'lishi mumkin emas!")
        return value""",
        "syntax_explanation": "ModelSerializer avtomatik ravishda Course modelidagi maydonlarni tayyorlaydi va custom validate_price metodi orqali narxni tekshiradi.",
        "table_rows": [
            ["serializers.ModelSerializer", "Modelga bog'langan serializer", "Meta class", "class S(serializers.ModelSerializer):", "Meta classtida fields ko'rsatmaslik"],
            ["serializer.is_valid()", "Ma'lumotlarni tekshiradi", "bool (True/False)", "if serializer.is_valid():", "is_valid() ni chaqirmasdan save() chaqirish"],
            ["serializer.data", "JSON ga o'tgan ma'lumot", "Dict", "return Response(serializer.data)", "Data ni funksiya deb chaqirish"],
            ["serializer.save()", "Bazaga saqlaydi (create/update)", "Model Object", "instance = serializer.save()", "is_valid() bajarilmay turib chaqirish"]
        ],
        "examples": [
            {
                "name": "Oddiy ModelSerializer Yaratish",
                "code": """from rest_framework import serializers
from .models import Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'""",
                "explanation": "Category modelidagi barcha maydonlarni avtomatik serializatsiya qilish.",
                "context": "Kategoriya va katalog API larida."
            },
            {
                "name": "Viewda Serializer yordamida ro'yxatni qaytarish",
                "code": """@api_view(['GET'])
def category_list(request):
    cats = Category.objects.all()
    serializer = CategorySerializer(cats, many=True)
    return Response(serializer.data)""",
                "explanation": "`many=True` parametri obyektlar ro'yxatini (QuerySet) serializatsiya qilish uchun beriladi.",
                "context": "Ko'plab obyektlar ro'yxatini qaytarishda."
            },
            {
                "name": "Serializer yordamida yangi obyekt yaratish (POST)",
                "code": """@api_view(['POST'])
def category_create(request):
    serializer = CategorySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)""",
                "explanation": "Validatsiyadan o'tsa save() qiladi, o'tmasa xatoliklar (errors) ni qaytaradi.",
                "context": "Yangi ma'lumot qo'shish API larida."
            },
            {
                "name": "Custom Validatsiya (validate_title)",
                "code": """class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'pages']

    def validate_title(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("Nomi kamida 3 ta belgidan iborat bo'lsin!")
        return value""",
                "explanation": "Aynan `title` maydonini tekshirish uchun `validate_title` metodi yoziladi.",
                "context": "Sarlavha va nomlarni validatsiya qilishda."
            },
            {
                "name": "Umumiy Validatsiya (validate)",
                "code": """class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['start_date', 'end_date']

    def validate(self, attrs):
        if attrs['start_date'] > attrs['end_date']:
            raise serializers.ValidationError("Tugash sanasi boshlanish sanasidan oldin bo'lishi mumkin emas!")
        return attrs""",
                "explanation": "Bir nechta maydonlarni o'zaro solishtirib validatsiya qilish.",
                "context": "Sana va oraliqlarni tekshirishda."
            },
            {
                "name": "ReadOnly va SerializerMethodField",
                "code": """class UserProfileSerializer(serializers.ModelSerializer):
    full_name_uppercase = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'username', 'full_name_uppercase']

    def get_full_name_uppercase(self, obj):
        return obj.username.upper()""",
                "explanation": "Modelda bo'lmagan hisoblanadigan (dynamic) maydon yaratish.",
                "context": "Qo'shimcha hisoblangan ma'lumotlarni uzatishda."
            },
            {
                "name": "Nested Serializer (Ichma-ich obyektlar)",
                "code": """class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name']

class BookDetailSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)

    class Meta:
        model = Book
        fields = ['id', 'title', 'author']""",
                "explanation": "Kitob ma'lumotlari ichida Muallif obyektini ham qo'shib qaytarish.",
                "context": "Bog'liq modellar ma'lumotini chiqarishda."
            },
            {
                "name": "Update (Tahrirlash) Serializer",
                "code": """@api_view(['PUT'])
def update_book_api(request, pk):
    book = Book.objects.get(pk=pk)
    serializer = BookSerializer(instance=book, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)""",
                "explanation": "`partial=True` bilan qisman o'zgartirish (PATCH/PUT) imkonini berish.",
                "context": "Ma'lumotlarni qisman tahrirlashda."
            }
        ],
        "real_project_title": "To'liq Loyiha: Serializer bilan Kurslar va Talabalar API si",
        "real_project_code": """from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'full_name', 'email', 'age', 'created_at']
        read_only_fields = ['id', 'created_at']

    def validate_age(self, value):
        if value < 15 or value > 80:
            raise serializers.ValidationError("Yosh 15 va 80 oralig'ida bo'lishi shart.")
        return value

@api_view(['GET', 'POST'])
def student_list_create(request):
    if request.method == 'GET':
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)""",
        "real_project_explanation": "Ushbu loyihada StudentSerializer yordamida yosh avtomatik validatsiya qilinadi hamda GET va POST amallari amalga oshiriladi.",
        "errors": [
            {
                "title": "QuerySet uzatilganda many=True parametrini unutish",
                "wrong": "serializer = StudentSerializer(students)",
                "reason": "QuerySet (ko'p obyektlar) uchun many=True berilmasa AttributeError yoki Attribute Error beradi.",
                "correct": "serializer = StudentSerializer(students, many=True)",
                "fix": "Ro'yxat bo'lsa `many=True` qo'shing."
            },
            {
                "title": "is_valid() ni barmasdan save() ni chaqirish",
                "wrong": "serializer = StudentSerializer(data=request.data)\nserializer.save()",
                "reason": "Validatsiyadan o'tmagan ma'lumot saqlanmaydi va AssertionError beradi.",
                "correct": "serializer = StudentSerializer(data=request.data)\nif serializer.is_valid():\n    serializer.save()",
                "fix": "Har doim avval `is_valid()` ni tekshiring."
            },
            {
                "title": "fields ro'yxatini ko'rsatmaslik",
                "wrong": "class Meta:\n    model = Student",
                "reason": "DRF 3.0+ versiyalarida fields yoki exclude ko'rsatilishi shart.",
                "correct": "class Meta:\n    model = Student\n    fields = '__all__'",
                "fix": "Meta ichida `fields` ni belgilang."
            },
            {
                "title": "validate_<fieldname> funksiyasida qiymatni return qilmaslik",
                "wrong": "def validate_age(self, value):\n    if value < 0: raise ValidationError('Err')",
                "reason": "Validatsiya funksiyasi oxirida `return value` qilinmasa qiymat None bo'lib qoladi.",
                "correct": "def validate_age(self, value):\n    if value < 0: raise ValidationError('Err')\n    return value",
                "fix": "Validatsiyadan so'ng o'zgargan yoki asl `value` ni qaytaring."
            }
        ],
        "tasks": {
            "easy": "Product modeli uchun ModelSerializer sinfini yarating.",
            "medium": "ProductSerializer ga narx 0 dan kichik bo'lsa xatolik beruvchi `validate_price` metodini qo'shing.",
            "hard": "Category va Product modellarini bir-biriga bog'lagan holda Nested Serializer yozing va API orqali chiqaring."
        },
        "homework": [
            "O'zingizning loyihangizdagi barcha modellar uchun Serializer sinflarini tuzing",
            "Email va telefon raqamlarini to'g'riligini tekshiruvchi custom validatorlar yozing",
            "Postman orqali POST va PUT so'rovlarida validatsiyalar ishlayotganini sinang",
            "SerializerMethodField yordamida mahsulotning chegirmali narxini hisoblab chiquvchi maydon qo'shing",
            "Kodingizni GitHub repozitoriyangizga joylang"
        ],
        "quiz_questions": [
            {"question": "ModelSerializer va oddiy Serializer o'rtasidagi asosiy afzallik nima?", "answer": "ModelSerializer Django Modelidan avtomatik maydonlarni va create/update funksiyalarini hosil qiladi."},
            {"question": "QuerySet ni serializatsiya qilishda qaysi parametr shart?", "answer": "many=True parametri berilishi shart."},
            {"question": "Validatsiya xatoligini chiqarish uchun qaysi exception ishlatiladi?", "answer": "serializers.ValidationError Exception obyekti ishlatiladi."},
            {"question": "read_only_fields nima uchun kerak?", "answer": "Faqat ma'lumotni o'qishda chiqarish, foydalanuvchi tomonidan kiritilishiga yo'l qo'ymaslik uchun."},
            {"question": "is_valid() funksiyasi nimani qaytaradi?", "answer": "Booleanda True yoki False qiymat qaytaradi."}
        ],
        "summary": [
            "DRF Serializers va ModelSerializers",
            "Serialization va Deserialization jarayonlari",
            "Custom field va model validatsiyalari",
            "Nested Serializers va SerializerMethodField"
        ],
        "next_lesson_title": "DRF Class-Based Views (CBV) va Generic Views",
        "resources": [
            "📄 DRF Serializers Documentation: https://www.django-rest-framework.org/api-guide/serializers/",
            "📄 Validators: https://www.django-rest-framework.org/api-guide/validators/",
            "💻 Kodlar: github.com/dars-reja/62-dars",
            "🎬 Video dars: youtube.com/watch?v=drf62"
        ]
    }
]

print("Populating Months 4, 5, 6 complete documentation...")

# Update lessons 61 and 62 as a test of script architecture
for data in LESSONS_DATA:
    num = data["number"]
    content = generate_full_markdown(
        number=data["number"],
        emoji=data["emoji"],
        title=data["title"],
        intro=data["intro"],
        abilities=data["abilities"],
        goals=data["goals"],
        prereqs=data["prereqs"],
        terms=data["terms"],
        syntax_code=data["syntax_code"],
        syntax_explanation=data["syntax_explanation"],
        table_rows=data["table_rows"],
        examples=data["examples"],
        real_project_title=data["real_project_title"],
        real_project_code=data["real_project_code"],
        real_project_explanation=data["real_project_explanation"],
        errors=data["errors"],
        tasks=data["tasks"],
        homework=data["homework"],
        quiz_questions=data["quiz_questions"],
        summary=data["summary"],
        next_lesson_title=data["next_lesson_title"],
        resources=data["resources"]
    )
    
    filename = f"dars_{num:02d}.md"
    filepath = os.path.join(DOCS_DIR, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

    lesson_obj, created = Lesson.objects.update_or_create(
        lesson_number=num,
        defaults={
            "lesson_id": f"les-100unique-{num}",
            "title": data["title"],
            "goal": data["goals"][0],
            "description": data["intro"][:200],
            "content": content,
            "status": "planned",
            "homework": "\n".join(data["homework"])
        }
    )
    print(f"✅ Lesson {num}: {data['title']} created/updated successfully ({len(content)} chars)")

print("Script framework test passed!")
