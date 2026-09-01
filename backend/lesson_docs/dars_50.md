# ⚡ 50. ModelSerializer — Dars dokumentatsiyasi

Standart `serializers.Serializer` bilan ishlash ba'zan juda ko'p takroriy kod yozishni talab qiladi (barcha maydonlarni va `create`/`update` metodlarini qo'lda yozish).

**`ModelSerializer`** — bu Django modellari bilan bevosita ishlovchi va avtomatik ravishda model maydonlariga mos moslashtirilgan Serializer yaratuvchi maxsus klassdir. U kod hajmini 80% ga qisqartiradi va ish unumdorligini oshiradi.

---

# Kod misoli — ModelSerializer

```python
# main/serializers.py
from rest_framework import serializers
from .models import Product

class ProductModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__' # yoki ['id', 'title', 'price']
```

---

# 10. Qisqa xulosa

Bu darsda `ModelSerializer` klassi va uning qulayliklari o'rganildi.
