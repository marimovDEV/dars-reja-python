# 🎛️ 51. DRF APIView va Response — Dars dokumentatsiyasi

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
