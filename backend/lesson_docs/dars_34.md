# 🐘 34. PostgreSQL va psycopg2 — Dars dokumentatsiyasi

**PostgreSQL** — bu dunyodagi eng ilg'or, ishonchli va kuchli Ochiq Manbali Relatsion Ma'lumotlar Bazasi Tizimi (ORDBMS). SQLite dan farqli o'laroq, PostgreSQL alohida **Server** sifatida ishlaydi va bir vaqtning o'zida millionlab so'rovlar va ulanishlarni bajara oladi.

Python dasturini PostgreSQL bazasiga ulash uchun **`psycopg2`** yoki `psycopg2-binary` kutubxonasi ishlatiladi.

---

## Bu mavzu orqali nimalar qilish mumkin

- PostgreSQL serveri haqida tushunchaga ega bo'lish;
- `pip install psycopg2-binary` orqali drayverni o mezon qilish;
- `psycopg2.connect()` orqali host, port, user, password bilan ulanish;
- PostgreSQL da tranzaksiyalar va cursors bilan ishlash.

---

# Kod misoli — PostgreSQL ga Ulanish

```python
import psycopg2

try:
    connection = psycopg2.connect(
        user="postgres",
        password="mysecretpassword",
        host="127.0.0.1",
        port="5432",
        database="test_db"
    )
    cursor = connection.cursor()
    cursor.execute("SELECT version();")
    db_version = cursor.fetchone()
    print("PostgreSQL versiyasi:", db_version)

except Exception as error:
    print("Xato yuz berdi:", error)
finally:
    if connection:
        cursor.close()
        connection.close()
```

---

# 10. Qisqa xulosa

Bu darsda PostgreSQL serveri va Python `psycopg2` moduli orqali unga ulanish o'rganildi.
