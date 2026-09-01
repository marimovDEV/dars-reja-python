# 🧩 52. Generic Views va Mixins — Dars dokumentatsiyasi

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
