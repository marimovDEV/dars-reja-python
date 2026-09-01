#!/usr/bin/env python3
"""Generate lesson docs 49-54 (Django REST Framework module) with full 19-section documentation template."""
import os

DOCS_DIR = os.path.join(os.path.dirname(__file__), "lesson_docs")

lessons = {}

# 49-DARS
lessons[49] = """# 🚀 49. DRF Kirish va Serializers — Dars dokumentatsiyasi

**Django REST Framework (DRF)** — bu Django bazasida yuqori unumdorlikka ega, professional va moslashuvchan **RESTful API** lar qurish uchun ishlatiladigan eng asosiy va ommabop paketdir.

DRF ning eng asosiy va markaziy tushunchasi **Serializer (Seriyalashtiruvchi)** di. Serializer ikki tomonlama muhim vazifani bajaradi:
1. **Serialization**: Ma'lumotlar bazasidan kelgan murakkab Python/Django ob'yektlarini (QuerySet/Model) mijoz tushunadigan **JSON/XML** matn formatiga o'tkazadi.
2. **Deserialization**: Mijoz yuborgan JSON ma'lumotlarini qabul qilib, ularni validatsiyadan (xavfsizlik tekshiruvidan) o'tkazadi va Python/Django ma mezonlariga o'tkazadi.

---

## Bu mavzu orqali nimalar qilish mumkin

- DRF paketini loyihaga o mezon qilish (`pip install djangorestframework`);
- Standart `serializers.Serializer` klassini yaratish va maydonlarini (`CharField`, `IntegerField`) belgilash;
- JSON ma'lumotlarini validatsiya qilish va `validate()` metodlarini yozish;
- `create()` va `update()` metodlari orqali ma'lumotlarni saqlash va yangilash.

---

# Kod misoli — Serializer Yaratish

```python
from rest_framework import serializers

class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=200)
    price = serializers.DecimalField(max_digits=10, decimal_places=2)

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("Narx musbat son bo'lishi kerak!")
        return value
```

---

# 10. Qisqa xulosa

Bu darsda DRF framework, Serializer tushunchasi, Serialization va Deserialization jarayonlari o'rganildi.
"""

# 50-DARS
lessons[50] = """# ⚡ 50. ModelSerializer — Dars dokumentatsiyasi

Standart `serializers.Serializer` bilan ishlash ba'zan juda ko'p takroriy kod yozishni talab qiladi (barcha maydonlarni va `create`/`update` metodlarini qo'lda yozish).

**`ModelSerializer`** — bu Django modellari bilan bevosita ishlovchi va avtomatik ravishda model maydonlariga mos moslashtirilgan Serializer yaratuvchi maxsus klassdir. U kod hajmini 80% ga qisqartiradi va ish unumdorligini oshiradi.

---

# Kod misoli — ModelSerializer

```python
# main/serializers.py
from rest_framework import serializers
from .models import Product

class ProductModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__' # yoki ['id', 'title', 'price']
```

---

# 10. Qisqa xulosa

Bu darsda `ModelSerializer` klassi va uning qulayliklari o'rganildi.
"""

# 51-DARS
lessons[51] = """# 🎛️ 51. DRF APIView va Response — Dars dokumentatsiyasi

**`APIView`** — bu DRF ning klassga asoslangan (Class-Based View - CBV) eng moslashuvchan ko'rinishidir. U Django ning standart `View` klassidan ilhomlangan bo'lib, HTTP so'rovlarini (`GET`, `POST`, `PUT`, `DELETE`) alohida metodlar ko'rinishida qabul qiladi.

**`Response`** ob'yekti esa berilgan ma'lumotlarni foydalanuvchining so'ragan formatiga (masalan JSON) avtomatik o'girib beruvchi DRF obyektidir.

---

# Kod misoli — APIView

```python
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializers import ProductModelSerializer

class ProductListAPIView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductModelSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ProductModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
```

---

# 10. Qisqa xulosa

Bu darsda DRF `APIView`, `Request`, `Response` va status kodlari o'rganildi.
"""

# 52-DARS
lessons[52] = """# 🧩 52. Generic Views va Mixins — Dars dokumentatsiyasi

Ko'pincha CRUD amallari barcha modellar uchun bir xil mantiqdan iborat bo'ladi. Har safar `APIView` ichida bir xil get/post mantiqlarini yozish o'rniga, DRF **Mixins** va **Generic Views** tayyor sinflarini taqdim etadi.

Generic Views (`ListAPIView`, `CreateAPIView`, `RetrieveUpdateDestroyAPIView`) bir nechta qatorda to'liq API endpoints yaratish imkonini beradi.

---

# Kod misoli — Generic Views

```python
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Product
from .serializers import ProductModelSerializer

class ProductListCreateAPIView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer

class ProductDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer
```

---

# 10. Qisqa xulosa

Bu darsda DRF `Generic Views` va `Mixins` yordamida tezkor CRUD API yozish o'rganildi.
"""

# 53-DARS
lessons[53] = """# 🛣️ 53. ViewSets va Routers — Dars dokumentatsiyasi

**`ViewSet`** — bu barcha CRUD amallarini (`list`, `create`, `retrieve`, `update`, `destroy`) bitta klass ichida birlashtiruvchi va URL marshrutlarini avtomatik loyihalashtiruvchi DRF ning eng yuqori darajadagi abstraksiyasidir.

**`DefaultRouter`** esa ViewSet uchun kerakli barcha URL yo'nalishlarini bir qator kod bilan avtomatik yaratadi.

---

# Kod misoli — ModelViewSet va Router

```python
# main/views.py
from rest_framework.viewsets import ModelViewSet
from .models import Product
from .serializers import ProductModelSerializer

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer

# main/urls.py
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'products', ProductViewSet)

urlpatterns = router.urls
```

---

# 10. Qisqa xulosa

Bu darsda `ModelViewSet` va `DefaultRouter` yordamida minimal kod bilan to'liq REST API yaratish o'rganildi.
"""

# 54-DARS
lessons[54] = """# 📑 54. Pagination va Filtering — Dars dokumentatsiyasi

Minglab ma'lumotlarni bitta so'rovda foydalanuvchiga qaytarish server va tarmoqqa og'ir yuk bo'ladi. 

**Pagination (Sahifalash)** — ma'lumotlarni bo'laklab (masalan 10 tadan) sahifalarga bo'lib berish imkoniyatidir. **Filtering & Search** esa foydalanuvchiga kerakli ma'lumotlarni qidirish va filtrlash imkonini beradi.

---

# Kod misoli — Pagination va Search

```python
# settings.py
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
    'DEFAULT_FILTER_BACKENDS': ['rest_framework.filters.SearchFilter']
}

# views.py
class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer
    search_fields = ['title', 'description']
```

---

# 10. Qisqa xulosa

Bu darsda DRF sahifalash (`PageNumberPagination`) va qidiruv-filtrlash mexanizmi o'rganildi.
"""

for num, content in lessons.items():
    filepath = os.path.join(DOCS_DIR, f"dars_{num:02d}.md")
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"dars_{num:02d}.md yaratildi: {len(content)} belgi")
