# 📑 54. Pagination va Filtering — Dars dokumentatsiyasi

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
