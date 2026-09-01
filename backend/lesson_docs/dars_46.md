# 📝 46. Django Forms va ModelForms — Dars dokumentatsiyasi

Foydalanuvchilar tomonidan kiritilgan ma'lumotlarni HTML formalari orqali qabul qilish, ularni xavfsizlik (XSS, CSRF) bo'yicha tekshirish va bazaga saqlash uchun Django **Forms va ModelForms** mexanizmlaridan foydalanadi.

---

# ModelForm Misoli

```python
# main/forms.py
from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'price']
```

**View ichida ishlatilishi:**
```python
def add_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save() # Bazaga saqlaydi
```

---

# 10. Qisqa xulosa

Bu darsda Django Forms, ModelForms va ma'lumotlar validatsiyasi o'rganildi.
