# 📚 59. DRF Swagger va Redoc — Dars dokumentatsiyasi

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
