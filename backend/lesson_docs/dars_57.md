# 🔐 57. Django Forms va Validatsiya — Dars dokumentatsiyasi

Django formalari ma'lumotlarni qabul qilish, tozalash (sanitize) va bazaga saqlashdan oldin xatoliklarni tekshirishni (validation) avtomatlashtiradi.

---

## Django ModelForm Misoli

```python
# main/forms.py
from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['full_name', 'email', 'phone']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }
```

Keyingi **58-dars: Django Models, Migrations va ORM So'rovlari** da bazalar bilan ishlashni o'rganamiz.
