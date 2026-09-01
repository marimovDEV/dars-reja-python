# 🛡️ 57. Permissions va Throttling — Dars dokumentatsiyasi

**Authorization (Authorization / Permissions)** — shaxsi aniqlangan foydalanuvchiga muayyan harakatni (masalan o'chirish yoki tahrirlash) bajarishga ruxsat bor-yo'qligini tekshiradi.

**Throttling (Rate Limiting)** — bir daqiqada yoki kunda foydalanuvchi nechtagacha so'rov yuborishi mumkinligini cheklash (DDOS va Spamdan himoya).

---

# Permissions va Throttling Misoli

```python
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.throttling import UserRateThrottle

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    throttle_classes = [UserRateThrottle]
```

---

# 10. Qisqa xulosa

Bu darsda DRF Permissions (`IsAuthenticatedOrReadOnly`) va Throttling cheklovlari o'rganildi.
