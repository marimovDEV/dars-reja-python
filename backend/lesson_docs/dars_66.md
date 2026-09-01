# 🧪 66. DRF API Testing — Dars dokumentatsiyasi

Backend REST API larni testlash — bu so'rov yuborilganda kutilgan Status kodi (`200`, `201`, `400`) va JSON javob tuzilishi qaytayotganini avtomatik tekshirish demakdir.

Django REST Framework o'zining **`APITestCase`** va **`APIClient`** maxsus vositalarini taqdim etadi.

---

# Kod misoli — DRF APITestCase

```python
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Product

class ProductAPITest(APITestCase):
    def setUp(self):
        self.product = Product.objects.create(title="Test Product", price=100)

    def test_get_product_list(self):
        url = reverse('product-list') # API endpoint URL
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_product(self):
        url = reverse('product-list')
        data = {"title": "New Product", "price": 150}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
```

---

# 10. Qisqa xulosa

Bu darsda DRF API larni avtomatik testlash (`APITestCase`, `APIClient`) o'rganildi.
