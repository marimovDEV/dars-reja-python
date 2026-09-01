# 🐳 67. Docker va Docker Compose Kirish — Dars dokumentatsiyasi

"Mening kompyuterimda ishlayotgandi, lekin serverda ishlamadi" degan muammo dasturchilar orasida eng ko'p uchraydi.

**Docker** — bu ilovalarni ularning barcha bog'liqliklari (Python versiyasi, kutubxonalar, OS sozlamalari) bilan birga izolyatsiyalangan **Konteynerlar (Containers)** ichida qadoqlash va istalgan serverda bir xil barqarorlikda ishga tushirish texnologiyasidir (Konteynerlashtirish).

**Docker Compose** — bu bir nechta konteynerlarni (masalan: Django Web + PostgreSQL Baza + Redis Kesh + Celery Worker) bitta fayl orqali birgalikda boshqarish vositasidir.

---

# Kod misoli — Dockerfile va docker-compose.yml

```dockerfile
# Dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
```

```yaml
# docker-compose.yml
version: '3.8'
services:
  web:
    build: .
    ports:
      - "8000:8000"
    volumes:
      - .:/app
```

---

# 10. Qisqa xulosa

Bu darsda Docker konteynerlashtirish, Images, Containers va Docker Compose asoslari o'rganildi.
