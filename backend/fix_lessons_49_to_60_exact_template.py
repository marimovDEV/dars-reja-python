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

EXACT_49_TO_60_LESSONS = {
    49: {
        "title": "49-dars — DRF kirish va Serializers",
        "content": """# 🚀 49. DRF kirish va Serializers — Dars dokumentatsiyasi

`Django REST Framework (DRF)` va `Serializers` — Django loyihasida **RESTful API lar yaratish va Python complex tiplarini/modellarni JSON shakliga (va aksincha) aylantirish** uchun ishlatiladi.

Bu mavzu orqali:

- `pip install djangorestframework` va `INSTALLED_APPS` ga `'rest_framework'` qo'shish;
- `serializers.Serializer` sinfi;
- Serialization (Model -> JSON) va Deserialization (JSON -> Model);
- `serializer.is_valid()`, `serializer.data`, `serializer.validated_data`

mumkin.

---

## Dars maqsadi

Bu dars oxirida o‘quvchi:

- DRF arxitekturasini tushunish va loyihaga ulash;
- Custom `Serializer` yozib ma'lumotlarni JSON shakliga o'tkazish;
- Kiritilgan JSON ma'lumotlarni tekshirish (*Validation*)

ni mustaqil bajara oladi.

## Kerakli bilimlar

Bu darsni tushunish uchun:

- 37-dars: HTTP va REST API;
- 43-dars: Django Models

bilinishi kerak.

---

# 1. Asosiy tushuncha

`DRF va Serializer` nima ekanini sodda tilda tushuntiramiz.

Masalan:

> `Serializer` — bu tarjimon. U Django model obyektini brauzer yoki mobil ilovalar tushunadigan JSON matniga o'tkazadi (Serialization) hamda kelgan JSON ni qayta obyektga aylantiradi (Deserialization).

Muhim qoida:

```python
from rest_framework import serializers

class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    age = serializers.IntegerField()
```

---

# 2. Birinchi sodda misol

```python
from rest_framework import serializers

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    age = serializers.IntegerField()

student = Student("Ali", 20)
serializer = StudentSerializer(student)
print("JSON Data:", serializer.data)
```

Natija:

```text
JSON Data: {'name': 'Ali', 'age': 20}
```

---

# 3. Asosiy Serializer Metodlari Jadvali

| Metod / Atribut | Vazifasi | Misol |
|---|---|---|
| `serializer.data` | Serializatsiya bo'lgan JSON lug'atini olish | `print(serializer.data)` |
| `serializer.is_valid()` | Deserializatsiyada ma'lumot to'g'riligini tekshirish | `if serializer.is_valid():` |
| `serializer.validated_data` | Tekshirilgan toza ma'lumotlar lug'ati | `data = serializer.validated_data` |
| `serializer.save()` | Bazaga saqlash yoki yangilash | `serializer.save()` |

---

# 4. Batafsil misol — Validation

```python
class CourseSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    price = serializers.IntegerField()

    def validate_price(self, value):
        if value < 0:
            raise serializers.ValidationError("Narx manfiy bo'lishi mumkin emas!")
        return value
```

---

# 6. Ko‘p uchraydigan xatolar

## Xato 1: is_valid() chaqirmasdan validated_data ga murojaat qilish

Noto‘g‘ri:

```python
serializer = StudentSerializer(data=request.data)
print(serializer.validated_data)  # AssertionError!
```

To‘g‘ri:

```python
serializer = StudentSerializer(data=request.data)
if serializer.is_valid():
    print(serializer.validated_data)
```

---

# 7. Sinfdagi amaliy topshiriqlar

## 1-topshiriq — Oson

**Vazifa:** `ProductSerializer` yaratib, `title`, `price` va `stock` maydonlarini e'lon qiling.

## 2-topshiriq — O‘rta

**Vazifa:** `validate_title` metodi orqali sarlavha uzunligi kamida 3 ta harf bo'lishini tekshiring.

---

# 8. Uyga vazifa

1. `49_dars_drf_serializers.py` faylini yarating;
2. `UserSerializer` yozib email manzil `@gmail.com` bilan tugashini tekshiruvchi validator qo'shing;
3. Kodni GitHub'ga saqlang.

---

# 9. Tekshirish savollari

1. Serialization va Deserialization ning farqi nima?
2. `serializer.data` va `serializer.validated_data` farqi nimada?
3. DRF nimasi bilan oddiy Django Views dan afzal?

---

# 10. Qisqa xulosa

Bu darsda:

- `Django REST Framework (DRF)`;
- `serializers.Serializer sinfi`;
- `is_valid() va custom validatorlar`

ni o‘rgandik.

Keyingi darsda: **ModelSerializer**.

---

# Resurslar va fayllar

- 📄 Konspekt: `49_dars_konspekt.pdf`
- 💻 Kodlar: `github.com/dars-reja/49-dars`
- 🎬 Video: `youtube.com/watch?v=dars49`
- 📝 Qo‘shimcha mashqlar: `python.uz/mashq49`
""",
        "code": "from rest_framework import serializers\n\nclass BookSerializer(serializers.Serializer):\n    title = serializers.CharField(max_length=200)\n    author = serializers.CharField(max_length=100)\n    price = serializers.IntegerField()\n\nprint('DRF Serializer sinfi e\\'lon qilindi.')",
        "code_exp": "- DRF dagi standart Serializer yordamida obyektni JSON ga tayyorlash kodi.",
        "quiz_q": "Python ob'ektini JSON matn formatiga o'tkazish jarayoni nima deyiladi?",
        "quiz_opts": ["Deserialization", "Serialization", "Compilation", "Parsing"],
        "quiz_ans": 1,
        "quiz_exp": "Serialization — Python model/obyektini JSON ma'lumot shakliga aylantirishdir."
    },

    50: {
        "title": "50-dars — ModelSerializer",
        "content": """# ⚡ 50. ModelSerializer — Dars dokumentatsiyasi

`ModelSerializer` — DRF'da **Django Model sinflari asosida avtomatik Serializer yaratish va kodingizni keskin qisqartirish** uchun ishlatiladi.

Bu mavzu orqali:

- `serializers.ModelSerializer`;
- `class Meta` ichida `model = MyModel` va `fields = '__all__'` yoki `fields = ['id', 'title']`;
- `read_only_fields` va `extra_kwargs` sozlamalari

mumkin.

---

## Dars maqsadi

Bu dars oxirida o‘quvchi:

- Django modellari asosida bir necha qatorda tezkor Serializer yozish;
- `fields` ro'yxatini to'g mezon belgilash;
- `read_only_fields` yordamida avtomatik ID va yaratilgan vaqtlarni himoyalash

ni mustaqil bajara oladi.

---

# 1. Asosiy tushuncha

```python
from rest_framework import serializers
from .models import Course

class CourseModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'
```
""",
        "code": "from rest_framework import serializers\nfrom lessons_app.models import Lesson\n\nclass LessonModelSerializer(serializers.ModelSerializer):\n    class Meta:\n        model = Lesson\n        fields = ['id', 'title', 'lesson_number', 'created_at']\n\nprint('ModelSerializer muvaffaqiyatli tuzildi.')",
        "code_exp": "- Lesson modeli maydonlarini avtomatik o'quvchi ModelSerializer kodi.",
        "quiz_q": "ModelSerializer da barcha maydonlarni avtomatik serializatsiya qilish uchun fields ga nima yoziladi?",
        "quiz_opts": ["fields = '*'", "fields = '__all__'", "fields = 'all'", "fields = True"],
        "quiz_ans": 1,
        "quiz_exp": "fields = '__all__' modeli ichidagi barcha maydonlarni avtomatik qo'shadi."
    },

    51: {
        "title": "51-dars — DRF APIView va Response",
        "content": """# 🎛️ 51. DRF APIView va Response — Dars dokumentatsiyasi

`APIView` va `Response` — DRF'da **klassga asoslangan (Class-Based) API ko'rinishlarini yozish hamda moslashuvchan JSON javoblar qaytarish** uchun ishlatiladi.

Bu mavzu orqali:

- `from rest_framework.views import APIView`;
- `from rest_framework.response import Response`;
- `from rest_framework import status`;
- `def get(self, request):` va `def post(self, request):` metodlari

mumkin.

---

# 1. Asosiy tushuncha

```python
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class StudentListAPIView(APIView):
    def get(self, request):
        return Response({"message": "API Response OK"}, status=status.HTTP_200_OK)
```
""",
        "code": "from rest_framework.views import APIView\nfrom rest_framework.response import Response\nfrom rest_framework import status\n\nclass HealthCheckView(APIView):\n    def get(self, request):\n        return Response({'status': 'Server Active'}, status=status.HTTP_200_OK)\n\nprint('APIView klassi tayyor.')",
        "code_exp": "- HTTP GET so'roviga status=200 bilan JSON qaytaruvchi APIView kodi.",
        "quiz_q": "DRF da moslashuvchan JSON obyektini status kodi bilan qaytaruvchi sinf qaysi?",
        "quiz_opts": ["HttpResponse", "JsonResponse", "Response", "APIResponse"],
        "quiz_ans": 2,
        "quiz_exp": "DRF dagi Response sinfi so'rov beruvchi formatiga mos JSON/HTML qaytaradi."
    },

    52: {
        "title": "52-dars — Generic Views va Mixins",
        "content": """# 🧩 52. Generic Views va Mixins — Dars dokumentatsiyasi

`Generic Views` va `Mixins` — DRF'da **standart CRUD operatsiyalarini bir-ikki qator kod bilan tayyor taqdim etuvchi klasslar** hisoblanadi.

Bu mavzu orqali:

- `ListAPIView`, `CreateAPIView`, `RetrieveAPIView`, `UpdateAPIView`, `DestroyAPIView`;
- `ListCreateAPIView` va `RetrieveUpdateDestroyAPIView`;
- `queryset = MyModel.objects.all()` va `serializer_class = MySerializer`

mumkin.

---

# 1. Asosiy tushuncha

```python
from rest_framework.generics import ListCreateAPIView
from .models import Course
from .serializers import CourseSerializer

class CourseListCreateAPIView(ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
```
""",
        "code": "from rest_framework.generics import ListCreateAPIView\n# class LessonListCreateView(ListCreateAPIView):\n#     queryset = Lesson.objects.all()\n#     serializer_class = LessonSerializer\nprint('Generic ListCreateAPIView shabloni tayyor.')",
        "code_exp": "- Ro'yxat o'qish (GET) va yangi qo'shish (POST) ni bajaruvchi Generic View.",
        "quiz_q": "GET (ro'yxat) va POST (yaratish) amallarini birga bajaruvchi DRF Generic View qaysi?",
        "quiz_opts": ["ListAPIView", "CreateAPIView", "ListCreateAPIView", "ModelViewSet"],
        "quiz_ans": 2,
        "quiz_exp": "ListCreateAPIView bir vaqtda ro'yxatni beradi va yangi obyekt yaratishni ta'minlaydi."
    },

    53: {
        "title": "53-dars — ViewSets va Routers",
        "content": """# 🗺️ 53. ViewSets va Routers — Dars dokumentatsiyasi

`ViewSets` va `Routers` — DRF'da **barcha CRUD operatsiyalari va uning URL yo'nalishlarini (urls.py) bir joyda avtomatik shakllantirish** uchun ishlatiladi.

Bu mavzu orqali:

- `viewsets.ModelViewSet`;
- `routers.DefaultRouter()` va `router.register('courses', CourseViewSet)`;
- URL lar: `/courses/` (GET, POST) va `/courses/{id}/` (GET, PUT, PATCH, DELETE)

mumkin.

---

# 1. Asosiy tushuncha

```python
# views.py
from rest_framework import viewsets

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

# urls.py
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('courses', CourseViewSet)
```
""",
        "code": "from rest_framework import viewsets\nfrom rest_framework.routers import DefaultRouter\n\n# router = DefaultRouter()\n# router.register('lessons', LessonViewSet)\nprint('ModelViewSet va DefaultRouter sozlamalari tayyor.')",
        "code_exp": "- DRF router va ViewSet yordamida to'liq CRUD ni bir qatorda ulash kodi.",
        "quiz_q": "DRF da barcha 5 ta CRUD yo'nalishlarini avtomatik ulovchi sinf qaysi?",
        "quiz_opts": ["APIView", "ModelViewSet", "GenericAPIView", "ViewSetRouter"],
        "quiz_ans": 1,
        "quiz_exp": "ModelViewSet 5 ta standart CRUD metodlarini tayyor holga keltiradi."
    },

    54: {
        "title": "54-dars — Pagination va Filtering",
        "content": """# 📄 54. Pagination va Filtering — Dars dokumentatsiyasi

`Pagination` va `Filtering` — API dan keladigan **minglab ma'lumotlarni sahifalarga bo'lish hamda qidiruv/saralash amallarini bajarish** uchun ishlatiladi.

Bu mavzu orqali:

- `PageNumberPagination` va `LimitOffsetPagination`;
- `django-filter` kutubxonasi va `DjangoFilterBackend`;
- `SearchFilter` (`search_fields = ['title', 'content']`) va `OrderingFilter`

mumkin.

---

# 1. Asosiy tushuncha

```python
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
```
""",
        "code": "from rest_framework.pagination import PageNumberPagination\n\nclass CustomPagination(PageNumberPagination):\n    page_size = 5\n    max_page_size = 50\n\nprint('Pagination klassi tayyor.')",
        "code_exp": "- Har bir sahifada 5 ta ma'lumot beruvchi PageNumberPagination kodi.",
        "quiz_q": "DRF da matn bo'yicha qidiruv funksiyasini ulash uchun qaysi filter ishlatiladi?",
        "quiz_opts": ["DjangoFilterBackend", "SearchFilter", "OrderingFilter", "TextFilter"],
        "quiz_ans": 1,
        "quiz_exp": "SearchFilter filtri ?search=query so'rovlari bo'yicha qidiruvni ta'minlaydi."
    },

    55: {
        "title": "55-dars — User Authentication (Session vs Token)",
        "content": """# 🔑 55. User Authentication (Session vs Token) — Dars dokumentatsiyasi

`Authentication` — DRF'da **tizimga kirgan foydalanuvchini aniqlash (Session vs Token) va ularga mos huquqlar berish** uchun ishlatiladi.

Bu mavzu orqali:

- `SessionAuthentication` (Cookie va Session ID);
- `TokenAuthentication` va `authtoken` jadvali;
- Token yaratish: `python manage.py drf_create_token username`

mumkin.

---

# 1. Asosiy tushuncha

```python
# settings.py
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ]
}
```
""",
        "code": "# settings.py\n# REST_FRAMEWORK = {\n#     'DEFAULT_AUTHENTICATION_CLASSES': [\n#         'rest_framework.authentication.TokenAuthentication',\n#     ]\n# }\nprint('TokenAuthentication sozlamasi tayyor.')",
        "code_exp": "- Token tipidagi autentifikatsiyani DRF sozlamalariga kiritish kodi.",
        "quiz_q": "Mobil ilovalar va REST API lar uchun qaysi autentifikatsiya turi afzal hisoblanadi?",
        "quiz_opts": ["SessionAuthentication", "TokenAuthentication / JWT", "BasicAuth", "CookieAuth"],
        "quiz_ans": 1,
        "quiz_exp": "Token/JWT autentifikatsiyasi stateless bo'lib, mobil va SPA ilovalari uchun mos tushadi."
    },

    56: {
        "title": "56-dars — JWT Auth (SimpleJWT)",
        "content": """# 🔐 56. JWT Auth (SimpleJWT) — Dars dokumentatsiyasi

`JWT (JSON Web Token)` va `djangorestframework-simplejwt` — **Access Token va Refresh Token lar yordamida eng zamonaviy va xavfsiz autentifikatsiya** o'rnatish uchun ishlatiladi.

Bu mavzu orqali:

- Access Token (qisqa muddatli, masalan 5 min) va Refresh Token (uzun muddatli, masalan 1 kun);
- `TokenObtainPairView` (`/api/token/`) va `TokenRefreshView` (`/api/token/refresh/`);
- HTTP Header: `Authorization: Bearer <access_token>`

mumkin.

---

# 1. Asosiy tushuncha

```python
# urls.py
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
```
""",
        "code": "from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView\n\n# urlpatterns = [\n#     path('api/token/', TokenObtainPairView.as_view()),\n#     path('api/token/refresh/', TokenRefreshView.as_view()),\n# ]\nprint('JWT SimpleJWT marshrutlari tayyor.')",
        "code_exp": "- Access va Refresh token beruvchi SimpleJWT ko'rinishlari.",
        "quiz_q": "JWT token so'rov headerida qanday prefiks bilan yuboriladi?",
        "quiz_opts": ["Token <token>", "Bearer <token>", "Auth <token>", "Jwt <token>"],
        "quiz_ans": 1,
        "quiz_exp": "Authorization: Bearer <access_token> formati standart hisoblanadi."
    },

    57: {
        "title": "57-dars — Permissions va Throttling",
        "content": """# 🛡️ 57. Permissions va Throttling — Dars dokumentatsiyasi

`Permissions` va `Throttling` — **API resurslariga kirish huquqlarini cheklash (IsAuthenticated) hamda so'rovlar sonini me'yorlashtirish (Rate Limit)** uchun ishlatiladi.

Bu mavzu orqali:

- `AllowAny`, `IsAuthenticated`, `IsAdminUser`, `IsAuthenticatedOrReadOnly`;
- Throttling (Rate limiting): `AnonRateThrottle` va `UserRateThrottle`;
- `settings.py` ichida `'DEFAULT_THROTTLE_RATES': {'anon': '100/day', 'user': '1000/day'}`

mumkin.

---

# 1. Asosiy tushuncha

```python
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

class ProfileView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        return Response({"user": request.user.username})
```
""",
        "code": "from rest_framework.permissions import IsAuthenticatedOrReadOnly\n\n# class LessonViewSet(viewsets.ModelViewSet):\n#     permission_classes = [IsAuthenticatedOrReadOnly]\nprint('Permission sozlamasi e\\'lon qilindi.')",
        "code_exp": "- O'qish hamma uchun ochiq, tahrirlash esa faqat login qilganlar uchun ruhiyati.",
        "quiz_q": "Faqat ro'yxatdan o'tgan foydalanuvchilarga ruxsat beruvchi permission qaysi?",
        "quiz_opts": ["AllowAny", "IsAuthenticated", "IsAdminUser", "IsOwner"],
        "quiz_ans": 1,
        "quiz_exp": "IsAuthenticated faqat login qilgan foydalanuvchilar kirishiga ruxsat beradi."
    },

    58: {
        "title": "58-dars — Custom Permissions",
        "content": """# 🎭 58. Custom Permissions — Dars dokumentatsiyasi

`Custom Permissions` — DRF'da **xususiy mantiqiy huquqlar yaratish (masalan: Faqat muallif o'z postini tahrirlay olsin)** uchun ishlatiladi.

Bu mavzu orqali:

- `permissions.BasePermission` sinfidan voris olish;
- `has_permission(self, request, view)` (Umumiy kirish);
- `has_object_permission(self, request, view, obj)` (Obyekt darajasida kirish)

mumkin.

---

# 1. Asosiy tushuncha

```python
from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user
```
""",
        "code": "from rest_framework import permissions\n\nclass IsAuthorOrReadOnly(permissions.BasePermission):\n    def has_object_permission(self, request, view, obj):\n        if request.method in permissions.SAFE_METHODS:\n            return True\n        return obj.author == request.user\n\nprint('Custom Permission klassi yaratildi.')",
        "code_exp": "- Obyekt muallifi ekanligini tekshiruvchi Custom Permission kodi.",
        "quiz_q": "Obyekt darajasidagi huquqni tekshiruvchi permission metodi qaysi?",
        "quiz_opts": ["has_permission", "has_object_permission", "check_object", "can_access"],
        "quiz_ans": 1,
        "quiz_exp": "has_object_permission joriy obj obyekti ustida huquqni tekshiradi."
    },

    59: {
        "title": "59-dars — DRF Swagger va Redoc (drf-spectacular)",
        "content": """# 📑 59. DRF Swagger va Redoc (drf-spectacular) — Dars dokumentatsiyasi

`drf-spectacular` — DRF loyihasi uchun **interaktiv va avtomatik API hujjatlarini (Swagger UI va Redoc) yaratish** uchun ishlatiladi.

Bu mavzu orqali:

- `pip install drf-spectacular`;
- `SPECTACULAR_SETTINGS` va `DEFAULT_SCHEMA_CLASS`;
- Swagger UI (`/api/schema/swagger-ui/`) va Redoc (`/api/schema/redoc/`) interfeyslari

mumkin.

---

# 1. Asosiy tushuncha

```python
# urls.py
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]
```
""",
        "code": "from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView\n\n# urlpatterns = [\n#     path('api/schema/', SpectacularAPIView.as_view()),\n#     path('api/swagger/', SpectacularSwaggerView.as_view(url_name='schema')),\n# ]\nprint('Swagger UI va OpenAPI schema sozlandi.')",
        "code_exp": "- OpenAPI schema va Swagger UI interfeysini ulash kodi.",
        "quiz_q": "API larni interaktiv brauzerda sinash va hujjatlashtirish vositasi qaysi?",
        "quiz_opts": ["Swagger UI / Redoc", "Postman Desktop", "Django Admin", "Debug Toolbar"],
        "quiz_ans": 0,
        "quiz_exp": "Swagger UI va Redoc OpenAPI bolar asosida interaktiv vizual hujjat yaratadi."
    },

    60: {
        "title": "60-dars — 5-modul imtihoni",
        "content": """# 🎓 60. 5-modul imtihoni — Dars dokumentatsiyasi

`5-modul imtihoni` — 49-darsdan 59-darsgacha o'rganilgan **DRF, Serializers, APIView, ViewSets, JWT Auth, Permissions va Swagger ko'nikmalarini sinash** uchun o'tkaziladi.

---

## Imtihon Tartibi (100 ballik shkala)

- **Nazariy Testlar (20 ball)**: 49-59 darslar bo'yicha 10 ta test;
- **Amaliy Masalalar (50 ball)**: 3 ta murakkab DRF REST API va JWT Auth topshirig'i;
- **PEP8 Standart va Kod Sifati (20 ball)**: Izohlar va to'g'ri nomlash;
- **Vaqt va Intizom (10 ball)**: 2 soat ichida topshirish.

---

# 1. Imtihon Kod Shabloni

```python
def module_5_exam():
    print("====================================")
    print("   5-MODUL IMTIHONI KODI BAJARILDI  ")
    print("====================================")

module_5_exam()
```
""",
        "code": "def exam_solution_5():\n    print('5-Modul (Django REST Framework va JWT Auth) Imtihon topshirig\\'i bajarildi.')\n\nexam_solution_5()",
        "code_exp": "- `1-3 qatorlar` — 5-modul imtihon topshirig'i bajarilish funksiyasi.",
        "quiz_q": "5-modul imtihonida maksimal ball nechaga teng?",
        "quiz_opts": ["50 ball", "80 ball", "100 ball", "120 ball"],
        "quiz_ans": 2,
        "quiz_exp": "Imtihon 100 ballik shkala bo'yicha baholanadi."
    }
}

def update_49_to_60():
    print("==================================================================")
    print("🚀 49-DARSDAN 60-DARSGACHA BO'LGAN HUJJATLAR TO'G'RILANMOQDA...")
    print("==================================================================")

    all_lessons = list(Lesson.objects.all().order_by('lesson_number'))

    for num in range(49, 61):
        item_data = EXACT_49_TO_60_LESSONS[num]
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
        if num in EXACT_49_TO_60_LESSONS:
            ex = EXACT_49_TO_60_LESSONS[num]
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
    print("✨ 49-DARSDAN 60-DARSGACHA BO'LGAN DARSLAR SHABLON BO'YICHA TO'G'RILANDI!")
    print("==================================================================")

if __name__ == "__main__":
    update_49_to_60()
