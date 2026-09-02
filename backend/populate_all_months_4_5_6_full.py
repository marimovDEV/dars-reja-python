import os
import sys
import django

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from lessons_app.models import Lesson
from populate_month_6_and_all import generate_full_markdown, DOCS_DIR

LESSONS_63_TO_72 = [
    # 63-DARS
    {
        "number": 63,
        "emoji": "🏗️",
        "title": "DRF Class-Based Views (CBV) va Generic Views",
        "intro": """Katta REST API loyihalarida Function-Based Views (FBV) ishlatish kod takrorlanishiga olib kelishi mumkin. Django REST Framework-da **Class-Based Views (CBV)**, **Generic Views** va **ViewSets** arxitekturasidan foydalanib, 50 qatorli CRUD API kodini atigi 5 qatorga qisqartirish mumkin.

Ushbu darsda biz `APIView`, `ListCreateAPIView`, `RetrieveUpdateDestroyAPIView` va `ModelViewSet` yordamida professional va toza API arxitekturasini qurishni o'rganamiz.""",
        "abilities": [
            "APIView sinfidan foydalanib klass shaklidagi handlerlar yozish",
            "Generic Views (ListCreateAPIView, RetrieveUpdateDestroyAPIView) dan foydalanish",
            "ModelViewSet va SimpleRouter yordamida avtomatik URL routing yaratish",
            "get_queryset() va get_serializer_class() metodlarini overriding qilish"
        ],
        "goals": [
            "FBV va CBV o'rtasidagi farq hamda afzalliklarni aniq tushunadi",
            "ModelViewSet yordamida 1 daqiqada to'liq CRUD API ni taqdim etadi",
            "DefaultRouter orqali URL larni avtomatik generatsiya qiladi",
            "Koddagi takrorlanishlarni (DRY) yo'qotadi"
        ],
        "prereqs": ["61-dars (DRF Intro)", "62-dars (DRF Serializers)"],
        "terms": [
            ("APIView", "DRF dagi barcha klassli ko'rinishlarning tayanch sinfi bo'lib, HTTP metodlariga alohida metod sifatida ishlov beradi."),
            ("Generic Views", "Ma'lumotlar bazasi bilan ishlash bo'yicha ko'p uchraydigan standart vazifalarni (List, Create, Retrieve, Update, Destroy) tayyor bajaruvchi sinflar to'plami."),
            ("ModelViewSet", "Bitta klass ichida barcha 5 ta CRUD amallarini mujassamlashtirgan eng yuqori darajali DRF sinfi.")
        ],
        "syntax_code": """from rest_framework.viewsets import ModelViewSet
from .models import Course
from .serializers import CourseSerializer

class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer""",
        "syntax_explanation": "ModelViewSet klassi atigi 4 qatorda GET (list), POST (create), GET (detail), PUT (update), DELETE (destroy) amallarining barchasini tayyorlab beradi.",
        "table_rows": [
            ["APIView", "Past darajali CBV", "class MyView(APIView)", "def get(self, request):", "request o'rniga self.request deb yozmaslik"],
            ["ListCreateAPIView", "Ro'yxat va Yaratish", "queryset, serializer_class", "class L(ListCreateAPIView):", "queryset berishni unutish"],
            ["RetrieveUpdateDestroyAPIView", "Bitta obyekt CRUD", "queryset, serializer_class", "class D(RetrieveUpdateDestroyAPIView):", "pk o'rniga boshqa kwarg berish"],
            ["ModelViewSet", "To'liq CRUD ViewSet", "queryset, serializer_class", "class V(ModelViewSet):", "Routerga ulashni unutish"]
        ],
        "examples": [
            {
                "name": "APIView bilan GET va POST",
                "code": """from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializer

class BookListAPIView(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)""",
                "explanation": "APIView sinfida HTTP metodlari get(), post() kabi alohida funksiyalar shaklida yoziladi.",
                "context": "Custom va murakkab biznes mantiq talab etilganda."
            },
            {
                "name": "Generic ListCreateAPIView",
                "code": """from rest_framework.generics import ListCreateAPIView
from .models import Book
from .serializers import BookSerializer

class BookListCreate(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer""",
                "explanation": "ListCreateAPIView ro'yxatni olish va yangisini yaratishni avtomatik bajaradi.",
                "context": "Standart CRUD ro'yxatlarida."
            },
            {
                "name": "Generic RetrieveUpdateDestroyAPIView",
                "code": """from rest_framework.generics import RetrieveUpdateDestroyAPIView

class BookDetail(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer""",
                "explanation": "ID bo'yicha olish, yangilash va o'chirishni avtomatlashtirish.",
                "context": "Bitta obyektga ishlov berishda."
            },
            {
                "name": "ModelViewSet va DefaultRouter",
                "code": """# views.py
from rest_framework.viewsets import ModelViewSet
from .models import Book
from .serializers import BookSerializer

class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# urls.py
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('books', BookViewSet)
urlpatterns = router.urls""",
                "explanation": "ModelViewSet va Router yordamida barcha URL va metodlarni avtomatik ulash.",
                "context": "Professional REST API loyihalarida."
            },
            {
                "name": "get_queryset() ni dinamik override qilish",
                "code": """class UserBooksView(ListCreateAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        user = self.request.user
        return Book.objects.filter(owner=user)""",
                "explanation": "Faqat tizimga kirgan foydalanuvchining kitoblarini filtrlab qaytarish.",
                "context": "Foydalanuvchiga mos ma'lumotlarni saralashda."
            },
            {
                "name": "get_serializer_class() orqali turlicha serializer ishlatish",
                "code": """class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return CourseListSerializer
        return CourseDetailSerializer""",
                "explanation": "Ro'yxatda qisqa, batafsil sahifada to'liq serializer uzatish.",
                "context": "Optimizatsiya va tezlikni oshirishda."
            },
            {
                "name": "ViewSet ichida Custom Action yaratish",
                "code": """from rest_framework.decorators import action

class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    @action(detail=True, methods=['post'])
    def publish(self, request, pk=None):
        book = self.get_object()
        book.is_published = True
        book.save()
        return Response({'status': 'Kitob nashr etildi'})""",
                "explanation": "@action dekoratori orqali ViewSet ga qo'shimcha custom endpoint qo'shish.",
                "context": "Maxsus harakatlarni (publish, archive, send) bajarishda."
            },
            {
                "name": "ReadOnlyModelViewSet",
                "code": """from rest_framework.viewsets import ReadOnlyModelViewSet

class ReadOnlyCategoryViewSet(ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer""",
                "explanation": "Faqat o'qish uchun (GET list va GET detail) xizmat qiladigan xavfsiz ViewSet.",
                "context": "Ochiq katalog va ma'lumotnomalarda."
            }
        ],
        "real_project_title": "To'liq Loyiha: Router va ViewSet bilan E-Commerce API",
        "real_project_code": """from rest_framework.viewsets import ModelViewSet
from rest_framework.routers import DefaultRouter
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Order
from .serializers import OrderSerializer

class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

    @action(detail=True, methods=['post'])
    def cancel(self, request, pk=None):
        order = self.get_object()
        order.status = 'cancelled'
        order.save()
        return Response({'message': 'Buyurtma bekor qilindi'})""",
        "real_project_explanation": "Ushbu loyihada foydalanuvchilar buyurtmalarini boshqarish va bekor qilish aksiyasi yozilgan.",
        "errors": [
            {
                "title": "ViewSet ni path() ga router-siz noto'g'ri ulash",
                "wrong": "path('books/', BookViewSet.as_view())",
                "reason": "ViewSet oddiy view emas, u as_view({'get': 'list', 'post': 'create'}) shaklida yoki Router orqali ulanishi shart.",
                "correct": "router.register('books', BookViewSet)\npath('', include(router.urls))",
                "fix": "Router orqali ro'yxatdan o'tkazing."
            },
            {
                "title": "Generic View da queryset yoki serializer_class belgilamaslik",
                "wrong": "class MyView(ListCreateAPIView):\n    pass",
                "reason": "Generic viewlar qaysi model va serializer bilan ishlashini bilmaydi va AssertionError beradi.",
                "correct": "class MyView(ListCreateAPIView):\n    queryset = Book.objects.all()\n    serializer_class = BookSerializer",
                "fix": "`queryset` va `serializer_class` ga mos qiymatlarni bering."
            },
            {
                "title": "self.request o'rniga request deb murojaat qilish",
                "wrong": "class MyView(APIView):\n    def get_queryset(self):\n        user = request.user",
                "reason": "Klass metodlari ichida request obyektiga `self.request` orqali kiriladi.",
                "correct": "class MyView(APIView):\n    def get_queryset(self):\n        user = self.request.user",
                "fix": "`self.request` deb yozing."
            },
            {
                "title": "@action da detail=True/False ni noto'g'ri berish",
                "wrong": "@action(detail=False)\ndef cancel(self, request, pk=None): ...",
                "reason": "Bitta obyektga (pk bo'yicha) tegishli harakat uchun detail=True bo'lishi kerak.",
                "correct": "@action(detail=True)\ndef cancel(self, request, pk=None): ...",
                "fix": "Bitta obyekt uchun `detail=True` qiling."
            }
        ],
        "tasks": {
            "easy": "Article modeli uchun ListCreateAPIView sinfini yarating.",
            "medium": "Product modeli uchun ModelViewSet yaratib, uni DefaultRouter orqali ulaganingizni ko'rsating.",
            "hard": "OrderViewSet yaratib, unda `@action(detail=True)` orqali buyurtma holatini 'payed' ga o'tkazuvchi funksiya yozing."
        },
        "homework": [
            "Loyihangizdagi barcha FBV larni ModelViewSet arxitekturasiga o'tkazing",
            "DefaultRouter orqali URL larni sozlang",
            "Custom @action metodlarini qo'shing",
            "Postman orqali barcha CRUD amallarini test qiling",
            "Kodlarni GitHub ga yuklang"
        ],
        "quiz_questions": [
            {"question": "ModelViewSet ichida qaysi 5 ta CRUD harakatlari mavjud?", "answer": "list, create, retrieve, update, destroy."},
            {"question": "DefaultRouter nima uchun kerak?", "answer": "ViewSet lar uchun standart RESTful URL larni avtomatik tayyorlash uchun."},
            {"question": "Generic Views da get_queryset() funksiyasining vazifasi nima?", "answer": "So'rovga mos keladigan obyektlar ro'yxatini dinamik filtrlash va qaytarish."},
            {"question": "@action dekoratorida detail=True nimani bildiradi?", "answer": "Ushbu aksiya bitta muayyan obyekt (ID/pk) uchun mo'ljallanganligini bildiradi."},
            {"question": "ReadOnlyModelViewSet bilan ModelViewSet o'rtasidagi farq nima?", "answer": "ReadOnlyModelViewSet faqat GET (list, retrieve) amallariga ruxsat beradi."}
        ],
        "summary": [
            "DRF Class-Based Views (APIView)",
            "Generic Views (ListCreateAPIView, RetrieveUpdateDestroyAPIView)",
            "ModelViewSet va DefaultRouter arxitekturasi",
            "Custom Actions (@action) bilan ishlash"
        ],
        "next_lesson_title": "DRF Authentication va Permissions",
        "resources": [
            "📄 DRF Class Based Views: https://www.django-rest-framework.org/api-guide/views/",
            "📄 DRF ViewSets: https://www.django-rest-framework.org/api-guide/viewsets/",
            "💻 Kodlar: github.com/dars-reja/63-dars",
            "🎬 Video dars: youtube.com/watch?v=drf63"
        ]
    }
]

print("Populating lesson 63 data...")
for data in LESSONS_63_TO_72:
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

print("Script execution done!")
