# 🔒 58. Custom Permissions — Dars dokumentatsiyasi

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
