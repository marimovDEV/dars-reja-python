# 📝 55. Django Templates (DTL) — Dars dokumentatsiyasi

**Django Template Language (DTL)** — Python ma'lumotlarini HTML sahifalar ichida dinamik render qilish va sikllar hamda shartlarni ishlatish imkonini beradi.

---

## DTL Shablon Merosxo'rligi (base.html va index.html)

```html
<!-- templates/base.html -->
<!DOCTYPE html>
<html lang="uz">
<head>
    <title>{% block title %}Mening Saytim{% endblock %}</title>
</head>
<body>
    <header><h1>MarimovDev Portal</h1></header>
    <main>
        {% block content %}{% endblock %}
    </main>
</body>
</html>

<!-- templates/index.html -->
{% extends 'base.html' %}

{% block content %}
<h2>Darslar Ro'yxati</h2>
<ul>
    {% for course in courses %}
        <li>{{ course.name }} - <b>{{ course.price }} so'm</b></li>
    {% endfor %}
</ul>
{% endblock %}
```

Keyingi **56-dars: Django Static Files & Media** da CSS va rasmlarni ulanishini o'rganamiz.
