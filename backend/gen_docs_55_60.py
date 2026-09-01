#!/usr/bin/env python3
"""Generate lesson docs 55-60 (DRF Auth, Permissions and Module 5 Exam)."""
import os

DOCS_DIR = os.path.join(os.path.dirname(__file__), "lesson_docs")

lessons = {}

# 55-DARS
lessons[55] = """# 🔑 55. User Authentication (Session vs Token) — Dars dokumentatsiyasi

**Authentication (Autentifikatsiya)** — bu so'rov yuborgan foydalanuvchining shaxsini (kimligini) aniqlash jarayoni.

Veb-ishda ikkita asosiy autentifikatsiya usuli ishlatiladi:
1. **Session-Based Auth**: Odatda monolit veb-saytlar (HTML/Cookies) uchun.
2. **Token-Based Auth**: REST API va Mobil ilovalar uchun. Har bir so'rov bilan birga maxsus **Token** uzatiladi.

---

# Token Authentication Misoli

```python
# settings.py
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ]
}

# Terminalda token generator app qo'shish:
# INSTALLED_APPS = [..., 'rest_framework.authtoken']
```

---

# 10. Qisqa xulosa

Bu darsda Autentifikatsiya turlari (Session va Token Auth) o'rganildi.
"""

# 56-DARS
lessons[56] = """# 🔐 56. JWT Authentication (SimpleJWT) — Dars dokumentatsiyasi

**JWT (JSON Web Token)** — bu zamonaviy Web va Mobile API larda eng ko'p ishlatiladigan xavfsiz va holatsiz (stateless) autentifikatsiya standartidir.

JWT 2 ta tokendan iborat bo'ladi:
1. **`Access Token`**: Qisqa muddatli (masalan 5-15 daqiqa) so'rovlar uchun.
2. **`Refresh Token`**: Uzun muddatli (masalan 1-7 kun) yangi Access Token olish uchun.

Python'da `djangorestframework-simplejwt` kutubxonasi ishlatiladi.

---

# SimpleJWT Sozlash va Qo'llash

```python
# urls.py
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_python_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_python_view(), name='token_refresh'),
]
```

---

# 10. Qisqa xulosa

Bu darsda JWT (JSON Web Token) standartining ishlash tamoyili va SimpleJWT o'rganildi.
"""

# 57-DARS
lessons[57] = """# 🛡️ 57. Permissions va Throttling — Dars dokumentatsiyasi

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
"""

# 58-DARS
lessons[58] = """# 🔒 58. Custom Permissions — Dars dokumentatsiyasi

Ba'zan standart ruxsatlar yetarli bo'lmaydi (masalan: "Postni faqat uning muallifi tahrirlashi mumkin"). Shunday hollar uchun **Custom Permission (Shaxsiy Ruxsatnoma)** sinfi yoziladi.

---

# Custom Permission Misoli

```python
# permissions.py
from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # O'qish so'rovlariga (GET) barchaga ruxsat
        if request.method in permissions.SAFE_METHODS:
            return True
        # Yozish so'rovlariga faqat obyekt egasiga ruxsat
        return obj.author == request.user
```

---

# 10. Qisqa xulosa

Bu darsda Shaxsiy ruxsatnomalar (`BasePermission`, `has_object_permission`) o'rganildi.
"""

# 59-DARS
lessons[59] = """# 📚 59. DRF Swagger va Redoc — Dars dokumentatsiyasi

Backend dasturchi tomonidan yaratilgan API lar hujjatlashtirilishi (Documentation) va Frontend/Mobile dasturchilarga taqdim etilishi shart.

**`drf-spectacular`** — bu DRF loyihasi uchun avtomatik ravishda chiroyli, interaktiv **Swagger UI** va **ReDoc** dokumentatsiyalarini yaratuvchi vositadir.

---

# Swagger Sozlanishi

```python
# settings.py
REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}

# urls.py
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]
```

---

# 10. Qisqa xulosa

Bu darsda Avtomatik OpenAPI, Swagger UI va ReDoc dokumentatsiya yaratish o'rganildi.
"""

# 60-DARS
lessons[60] = """# 🎓 60. 5-modul imtihoni — Dars dokumentatsiyasi

5-modul imtihoni — **Django REST Framework (DRF)** (Serializers, ModelSerializer, APIView, Generic Views, ViewSets, Routers, Pagination, Filtering, JWT Auth, Custom Permissions va Swagger Documentation) bo'yicha to'liq bilimlarni sinaydi.

---

# Imtihon Topshiriqlari

1. **DRF Serializers & ViewSets**: `Book` modeli uchun `ModelSerializer` va `ModelViewSet` yaratib, router ga ulayotgan kodni yozing.
2. **JWT Auth & Permissions**: SimpleJWT autentifikatsiyani ulalang va faqat autorizatsiyadan o'tgan foydalanuvchilar kitob yaratishi mumkin bo'lgan ruxsatnoma o'rnating.
3. **Swagger & Custom Permission**: Kitobni faqat uni yaratgan muallifi tahrirlashi mumkin bo'lgan `IsOwnerOrReadOnly` custom permission yaratib, Swagger UI ni sozlang.

---

# 10. Qisqa xulosa

Ushbu imtihon Django REST Framework modulini muvaffaqiyatli yakunlaydi.
"""

for num, content in lessons.items():
    filepath = os.path.join(DOCS_DIR, f"dars_{num:02d}.md")
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"dars_{num:02d}.md yaratildi: {len(content)} belgi")
