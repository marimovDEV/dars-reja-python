# 🛣️ 53. ViewSets va Routers — Dars dokumentatsiyasi

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
