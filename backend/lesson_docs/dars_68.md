# 🐳 68. Django Loyihasini Dockerlashtirish — Dars dokumentatsiyasi

Ushbu darsda haqiqiy Django loyihasini Docker va Docker Compose yordamida to'liq konteynerlashtiramiz. Loyiha tarkibida Django Web ilovasi, PostgreSQL bazasi, Redis kesh serveri hamda Celery asinxron ishchisi bo'ladi.

---

# Kod misoli — Multi-container Docker Compose

```yaml
version: '3.8'

services:
  db:
    image: postgres:15
    environment:
      POSTGRES_DB: mydb
      POSTGRES_USER: myuser
      POSTGRES_PASSWORD: mypassword

  redis:
    image: redis:7-alpine

  web:
    build: .
    command: python manage.py runserver 0.0.0.0:8000
    volumes:
      - .:/app
    ports:
      - "8000:8000"
    depends_on:
      - db
      - redis
```

---

# 10. Qisqa xulosa

Bu darsda Django + Postgres + Redis ilovalarini Docker Compose bilan konteynerlashtirish o'rganildi.
