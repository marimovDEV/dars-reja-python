# 🚀 49. DRF Kirish va Serializers — Dars dokumentatsiyasi

**Django REST Framework (DRF)** — bu Django bazasida yuqori unumdorlikka ega, professional va moslashuvchan **RESTful API** lar qurish uchun ishlatiladigan eng asosiy va ommabop paketdir.

DRF ning eng asosiy va markaziy tushunchasi **Serializer (Seriyalashtiruvchi)** di. Serializer ikki tomonlama muhim vazifani bajaradi:
1. **Serialization**: Ma'lumotlar bazasidan kelgan murakkab Python/Django ob'yektlarini (QuerySet/Model) mijoz tushunadigan **JSON/XML** matn formatiga o'tkazadi.
2. **Deserialization**: Mijoz yuborgan JSON ma'lumotlarini qabul qilib, ularni validatsiyadan (xavfsizlik tekshiruvidan) o'tkazadi va Python/Django ma mezonlariga o'tkazadi.

---

## Bu mavzu orqali nimalar qilish mumkin

- DRF paketini loyihaga o mezon qilish (`pip install djangorestframework`);
- Standart `serializers.Serializer` klassini yaratish va maydonlarini (`CharField`, `IntegerField`) belgilash;
- JSON ma'lumotlarini validatsiya qilish va `validate()` metodlarini yozish;
- `create()` va `update()` metodlari orqali ma'lumotlarni saqlash va yangilash.

---

# Kod misoli — Serializer Yaratish

```python
from rest_framework import serializers

class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=200)
    price = serializers.DecimalField(max_digits=10, decimal_places=2)

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("Narx musbat son bo'lishi kerak!")
        return value
```

---

# 10. Qisqa xulosa

Bu darsda DRF framework, Serializer tushunchasi, Serialization va Deserialization jarayonlari o'rganildi.
