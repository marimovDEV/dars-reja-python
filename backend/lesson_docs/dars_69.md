# 🔄 69. CI/CD Asoslari (GitHub Actions) — Dars dokumentatsiyasi

**CI/CD (Continuous Integration / Continuous Deployment)** — bu koddagi har bir yangi o'zgarish va commit bajarilganda, avtomatik ravishda testlarni o'tkazish (CI) hamda kodni production serverga muvaffaqiyatli joylashtirish (CD) jarayonidir.

**GitHub Actions** — bu GitHub repozitoriysi ichida avtomatik pipeline va workflow larni (test, build, deploy) ishga tushiruvchi ommabop vositadir.

---

# Kod misoli — `.github/workflows/main.yml`

```yaml
name: Django CI/CD Pipeline

on:
  push:
    branches: [ "main" ]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      - name: Install Dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt
      - name: Run Tests
        run: |
          pytest
```

---

# 10. Qisqa xulosa

Bu darsda CI/CD tamoyili va GitHub Actions bilan avtomatik testlash o'rganildi.
