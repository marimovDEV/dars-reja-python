import os
import sys
import json
import django

sys.path.append(os.path.dirname(__file__))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from lessons_app.models import Lesson

LESSONS_JSON = os.path.join(os.path.dirname(__file__), "..", "frontend", "src", "data", "lessons.json")

FULL_LONG_50_TO_60 = {
    50: """# ⚡ 50. ModelSerializer — Dars dokumentatsiyasi

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

## Kerakli bilimlar

Bu darsni tushunish uchun:

- 49-dars: DRF kirish va Serializers

bilinishi kerak.

---

# 1. Asosiy tushuncha

`ModelSerializer` nima ekanini sodda tilda tushuntiramiz.

Masalan:

> `ModelSerializer` — model maydonlarini tahlil qilib, uning uchun mos bo'lgan `CharField`, `IntegerField` larni avtomatik tuzadi hamda `create()` va `update()` metodlarini avtomatik taqdim etadi.

Muhim qoida:

```python
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'
```

---

# 2. Birinchi sodda misol

```python
from rest_framework import serializers

class CourseModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'title', 'price']
```

---

# 10. Qisqa xulosa

Bu darsda:

- `serializers.ModelSerializer`;
- `class Meta (model, fields)`;
- `read_only_fields`

ni o‘rgandik.

Keyingi darsda: **DRF APIView va Response**.

---

# Resurslar va fayllar

- 📄 Konspekt: `50_dars_konspekt.pdf`
- 💻 Kodlar: `github.com/dars-reja/50-dars`
- 🎬 Video: `youtube.com/watch?v=dars50`
- 📝 Qo‘shimcha mashqlar: `python.uz/mashq50`
""",

    51: """# 🎛️ 51. DRF APIView va Response — Dars dokumentatsiyasi

`APIView` va `Response` — DRF'da **klassga asoslangan (Class-Based) API ko'rinishlarini yozish hamda moslashuvchan JSON javoblar qaytarish** uchun ishlatiladi.

Bu mavzu orqali:

- `from rest_framework.views import APIView`;
- `from rest_framework.response import Response`;
- `from rest_framework import status`;
- `def get(self, request):` va `def post(self, request):` metodlari

mumkin.

---

## Dars maqsadi

Bu dars oxirida o‘quvchi:

- Klassga asoslangan APIView ko'rinishlarini yozish;
- `Response` sinfi va HTTP status kodlarini birlashtirish;
- So'rov metodlariga (`GET`, `POST`, `DELETE`) mos mantiqlarni taqsimlash

ni mustaqil bajara oladi.

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

---

# 10. Qisqa xulosa

Bu darsda:

- `APIView sinfi`;
- `Response va status kodlari`;
- `get() va post() metodlari`

ni o‘rgandik.

Keyingi darsda: **Generic Views va Mixins**.

---

# Resurslar va fayllar

- 📄 Konspekt: `51_dars_konspekt.pdf`
- 💻 Kodlar: `github.com/dars-reja/51-dars`
- 🎬 Video: `youtube.com/watch?v=dars51`
- 📝 Qo‘shimcha mashqlar: `python.uz/mashq51`
""",

    52: """# 🧩 52. Generic Views va Mixins — Dars dokumentatsiyasi

`Generic Views` va `Mixins` — DRF'da **standart CRUD operatsiyalarini bir-ikki qator kod bilan tayyor taqdim etuvchi klasslar** hisoblanadi.

Bu mavzu orqali:

- `ListAPIView`, `CreateAPIView`, `RetrieveAPIView`, `UpdateAPIView`, `DestroyAPIView`;
- `ListCreateAPIView` va `RetrieveUpdateDestroyAPIView`;
- `queryset = MyModel.objects.all()` va `serializer_class = MySerializer`

mumkin.

---

## Dars maqsadi

Bu dars oxirida o‘quvchi:

- DRF tayyor Generic View laridan foydalanib CRUD yozish va vaqtni tejash;
- `ListCreateAPIView` va `RetrieveUpdateDestroyAPIView` ni qo'llash;
- `queryset` va `serializer_class` atributlarini to'g'ri o'rnatish

ni mustaqil bajara oladi.

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

---

# 10. Qisqa xulosa

Bu darsda:

- `Generic Views (ListCreateAPIView)`;
- `RetrieveUpdateDestroyAPIView`;
- `queryset va serializer_class`

ni o‘rgandik.

Keyingi darsda: **ViewSets va Routers**.

---

# Resurslar va fayllar

- 📄 Konspekt: `52_dars_konspekt.pdf`
- 💻 Kodlar: `github.com/dars-reja/52-dars`
- 🎬 Video: `youtube.com/watch?v=dars52`
- 📝 Qo‘shimcha mashqlar: `python.uz/mashq52`
""",

    53: """# 🗺️ 53. ViewSets va Routers — Dars dokumentatsiyasi

`ViewSets` va `Routers` — DRF'da **barcha CRUD operatsiyalari va uning URL yo'nalishlarini (urls.py) bir joyda avtomatik shakllantirish** uchun ishlatiladi.

Bu mavzu orqali:

- `viewsets.ModelViewSet`;
- `routers.DefaultRouter()` va `router.register('courses', CourseViewSet)`;
- URL lar: `/courses/` (GET, POST) va `/courses/{id}/` (GET, PUT, PATCH, DELETE)

mumkin.

---

## Dars maqsadi

Bu dars oxirida o‘quvchi:

- `ModelViewSet` orqali to'liq CRUD ni bir necha qatorda yaratish;
- `DefaultRouter` yordamida barcha URL larni avtomatik shakllantirish;
- DRF ning eng samarali va toza arxitektura tamoyilini egallash

ni mustaqil bajara oladi.

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

---

# 10. Qisqa xulosa

Bu darsda:

- `viewsets.ModelViewSet`;
- `routers.DefaultRouter`;
- `Avtomatik URL lar`

ni o‘rgandik.

Keyingi darsda: **Pagination va Filtering**.

---

# Resurslar va fayllar

- 📄 Konspekt: `53_dars_konspekt.pdf`
- 💻 Kodlar: `github.com/dars-reja/53-dars`
- 🎬 Video: `youtube.com/watch?v=dars53`
- 📝 Qo‘shimcha mashqlar: `python.uz/mashq53`
""",

    54: """# 📄 54. Pagination va Filtering — Dars dokumentatsiyasi

`Pagination` va `Filtering` — API dan keladigan **minglab ma'lumotlarni sahifalarga bo'lish hamda qidiruv/saralash amallarini bajarish** uchun ishlatiladi.

Bu mavzu orqali:

- `PageNumberPagination` va `LimitOffsetPagination`;
- `django-filter` kutubxonasi va `DjangoFilterBackend`;
- `SearchFilter` (`search_fields = ['title', 'content']`) va `OrderingFilter`

mumkin.

---

## Dars maqsadi

Bu dars oxirida o‘quvchi:

- API ma'lumotlarini sahifalarga (pages) bo'lib berish;
- Matnlar bo'yicha tezkor search qidiruvlarini qo'shish;
- Narx va sanalar bo'yicha filtrlarni sozlash

ni mustaqil bajara oladi.

---

# 1. Asosiy tushuncha

```python
from rest_framework.pagination import PageNumberPagination

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
```

---

# 10. Qisqa xulosa

Bu darsda:

- `PageNumberPagination`;
- `SearchFilter (?search=query)`;
- `OrderingFilter`

ni o‘rgandik.

Keyingi darsda: **User Authentication (Session vs Token)**.

---

# Resurslar va fayllar

- 📄 Konspekt: `54_dars_konspekt.pdf`
- 💻 Kodlar: `github.com/dars-reja/54-dars`
- 🎬 Video: `youtube.com/watch?v=dars54`
- 📝 Qo‘shimcha mashqlar: `python.uz/mashq54`
""",

    55: """# 🔑 55. User Authentication (Session vs Token) — Dars dokumentatsiyasi

`Authentication` — DRF'da **tizimga kirgan foydalanuvchini aniqlash (Session vs Token) va ularga mos huquqlar berish** uchun ishlatiladi.

Bu mavzu orqali:

- `SessionAuthentication` (Cookie va Session ID);
- `TokenAuthentication` va `authtoken` jadvali;
- Token yaratish: `python manage.py drf_create_token username`

mumkin.

---

## Dars maqsadi

Bu dars oxirida o‘quvchi:

- Session va Token autentifikatsiya farqlarini tushunish;
- DRF foydalanuvchilariga token biriktirish va tekshirish;
- Mobil va SPA ilovalari uchun mos xavfsizlikni o'rnatish

ni mustaqil bajara oladi.

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

---

# 10. Qisqa xulosa

Bu darsda:

- `Session vs Token Authentication`;
- `TokenAuthentication sozlamasi`;
- `authtoken kalitlari`

ni o‘rgandik.

Keyingi darsda: **JWT Auth (SimpleJWT)**.

---

# Resurslar va fayllar

- 📄 Konspekt: `55_dars_konspekt.pdf`
- 💻 Kodlar: `github.com/dars-reja/55-dars`
- 🎬 Video: `youtube.com/watch?v=dars55`
- 📝 Qo‘shimcha mashqlar: `python.uz/mashq55`
""",

    56: """# 🔐 56. JWT Auth (SimpleJWT) — Dars dokumentatsiyasi

`JWT (JSON Web Token)` va `djangorestframework-simplejwt` — **Access Token va Refresh Token lar yordamida eng zamonaviy va xavfsiz autentifikatsiya** o'rnatish uchun ishlatiladi.

Bu mavzu orqali:

- Access Token (qisqa muddatli, masalan 5 min) va Refresh Token (uzun muddatli, masalan 1 kun);
- `TokenObtainPairView` (`/api/token/`) va `TokenRefreshView` (`/api/token/refresh/`);
- HTTP Header: `Authorization: Bearer <access_token>`

mumkin.

---

## Dars maqsadi

Bu dars oxirida o‘quvchi:

- JWT tokenlar (Access va Refresh) ishlash mexanizmini tushunish;
- SimpleJWT kutubxonasini Django loyihasiga ulash;
- Header orqali `Bearer <token>` so'rovlarini yuborish

ni mustaqil bajara oladi.

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

---

# 10. Qisqa xulosa

Bu darsda:

- `JWT (Access va Refresh token)`;
- `SimpleJWT kutubxonasi`;
- `Authorization: Bearer header`

ni o‘rgandik.

Keyingi darsda: **Permissions va Throttling**.

---

# Resurslar va fayllar

- 📄 Konspekt: `56_dars_konspekt.pdf`
- 💻 Kodlar: `github.com/dars-reja/56-dars`
- 🎬 Video: `youtube.com/watch?v=dars56`
- 📝 Qo‘shimcha mashqlar: `python.uz/mashq56`
""",

    57: """# 🛡️ 57. Permissions va Throttling — Dars dokumentatsiyasi

`Permissions` va `Throttling` — **API resurslariga kirish huquqlarini cheklash (IsAuthenticated) hamda so'rovlar sonini me'yorlashtirish (Rate Limit)** uchun ishlatiladi.

Bu mavzu orqali:

- `AllowAny`, `IsAuthenticated`, `IsAdminUser`, `IsAuthenticatedOrReadOnly`;
- Throttling (Rate limiting): `AnonRateThrottle` va `UserRateThrottle`;
- `settings.py` ichida `'DEFAULT_THROTTLE_RATES': {'anon': '100/day', 'user': '1000/day'}`

mumkin.

---

## Dars maqsadi

Bu dars oxirida o‘quvchi:

- API ko'rinishlariga ruxsatnomalar (`permission_classes`) o'rnatish;
- Anonim va ro'yxatdan o'tgan foydalanuvchilar huquqlarini ajratish;
- Throttling orqali spam so'rovlarning oldini olish

ni mustaqil bajara oladi.

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

---

# 10. Qisqa xulosa

Bu darsda:

- `IsAuthenticated va IsAdminUser`;
- `IsAuthenticatedOrReadOnly`;
- `Throttling va Rate Limits`

ni o‘rgandik.

Keyingi darsda: **Custom Permissions**.

---

# Resurslar va fayllar

- 📄 Konspekt: `57_dars_konspekt.pdf`
- 💻 Kodlar: `github.com/dars-reja/57-dars`
- 🎬 Video: `youtube.com/watch?v=dars57`
- 📝 Qo‘shimcha mashqlar: `python.uz/mashq57`
""",

    58: """# 🎭 58. Custom Permissions — Dars dokumentatsiyasi

`Custom Permissions` — DRF'da **xususiy mantiqiy huquqlar yaratish (masalan: Faqat muallif o'z postini tahrirlay olsin)** uchun ishlatiladi.

Bu mavzu orqali:

- `permissions.BasePermission` sinfidan voris olish;
- `has_permission(self, request, view)` (Umumiy kirish);
- `has_object_permission(self, request, view, obj)` (Obyekt darajasida kirish)

mumkin.

---

## Dars maqsadi

Bu dars oxirida o‘quvchi:

- `BasePermission` sinfidan foydalanib o'z ruxsatnoma mantiqlarini yozish;
- `has_object_permission` orqali mualliflik huquqini tekshirish;
- SAFE_METHODS (`GET`, `HEAD`, `OPTIONS`) larni o'qish uchun ochiq qoldirish

ni mustaqil bajara oladi.

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

---

# 10. Qisqa xulosa

Bu darsda:

- `BasePermission sinfi`;
- `has_object_permission()`;
- `permissions.SAFE_METHODS`

ni o‘rgandik.

Keyingi darsda: **DRF Swagger va Redoc (drf-spectacular)**.

---

# Resurslar va fayllar

- 📄 Konspekt: `58_dars_konspekt.pdf`
- 💻 Kodlar: `github.com/dars-reja/58-dars`
- 🎬 Video: `youtube.com/watch?v=dars58`
- 📝 Qo‘shimcha mashqlar: `python.uz/mashq58`
""",

    59: """# 📑 59. DRF Swagger va Redoc (drf-spectacular) — Dars dokumentatsiyasi

`drf-spectacular` — DRF loyihasi uchun **interaktiv va avtomatik API hujjatlarini (Swagger UI va Redoc) yaratish** uchun ishlatiladi.

Bu mavzu orqali:

- `pip install drf-spectacular`;
- `SPECTACULAR_SETTINGS` va `DEFAULT_SCHEMA_CLASS`;
- Swagger UI (`/api/schema/swagger-ui/`) va Redoc (`/api/schema/redoc/`) interfeyslari

mumkin.

---

## Dars maqsadi

Bu dars oxirida o‘quvchi:

- OpenAPI sxemalarini loyihada avtomatik shakllantirish;
- Swagger UI brauzer interfeysini ulash hamda endpoints larni sinab ko'rish;
- Frontend dasturchilar uchun professional API dokumentatsiya taqdim etish

ni mustaqil bajara oladi.

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

---

# 10. Qisqa xulosa

Bu darsda:

- `drf-spectacular paketini o'rnatish`;
- `OpenAPI 3.0 schema`;
- `Swagger UI va Redoc hujjatlari`

ni o‘rgandik.

Keyingi darsda: **5-modul imtihoni**.

---

# Resurslar va fayllar

- 📄 Konspekt: `59_dars_konspekt.pdf`
- 💻 Kodlar: `github.com/dars-reja/59-dars`
- 🎬 Video: `youtube.com/watch?v=dars59`
- 📝 Qo‘shimcha mashqlar: `python.uz/mashq59`
""",

    60: """# 🎓 60. 5-modul imtihoni — Dars dokumentatsiyasi

`5-modul imtihoni` — 49-darsdan 59-darsgacha o'rganilgan **DRF, Serializers, APIView, ViewSets, JWT Auth, Permissions va Swagger ko'nikmalarini sinash** uchun o'tkaziladi.

Bu mavzu orqali:

- 49–59 darslar bo'yicha nazariy va amaliy bilimlarni sinash;
- Real 3 ta murakkab DRF REST API va JWT Auth masalalarini yechish;
- Sertifikatlash uchun 5-modul natijalarini belgilash

mumkin.

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
"""
}

for num, txt in FULL_LONG_50_TO_60.items():
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
    if n in FULL_LONG_50_TO_60:
        item["content"] = FULL_LONG_50_TO_60[n]

with open(LESSONS_JSON, "w", encoding="utf-8") as f:
    json.dump(j_data, f, ensure_ascii=False, indent=2)

print("✨ 50-60 darslar kontenti to'liqligicha 10 bo'limli variantda saqlandi!")
