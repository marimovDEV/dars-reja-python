# 🚀 62. Redis va Kesh (Caching) — Dars dokumentatsiyasi

Har bir so'rov kelganda ma'lumotlar bazasiga (PostgreSQL) murojaat qilish va murakkab hisob-kitoblarni qayta bajarish loyihaning sekinlashishiga olib keladi.

**Kesh (Caching)** — bu tez-tez so'raladigan va kam o'zgaradigan ma mezonlarni juda tezkor xotiraga (RAM) saqlab qo'yish mexanizmidir.

**Redis (Remote Dictionary Server)** — bu xotirada (In-Memory) Key-Value formatida ishlovchi ultra-tezkor ma mezonlar bazasidir. U kesh saqlash, seanslar boshqaruvi va xabarlar navbati (Message Broker) uchun ishlatiladi.

---

# Kod misoli — Django va Redis Caching

```python
# settings.py
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.redis.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/1',
    }
}

# views.py
from django.core.cache import cache
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Product

class ProductListCachedView(APIView):
    def get(self, request):
        data = cache.get("all_products")
        if not data:
            print("DB dan o'qilmoqda...")
            products = Product.objects.all()
            data = list(products.values())
            cache.set("all_products", data, timeout=60*15) # 15 minut keshda turadi
        else:
            print("Keshdan (Redis) o'qildi!")
        return Response(data)
```

---

# 10. Qisqa xulosa

Bu darsda Kesh (Caching) konseptsiyasi, Redis In-Memory DB va Django Caching o'rganildi.
