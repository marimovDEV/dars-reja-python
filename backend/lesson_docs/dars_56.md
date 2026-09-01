# 🔐 56. JWT Authentication (SimpleJWT) — Dars dokumentatsiyasi

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
