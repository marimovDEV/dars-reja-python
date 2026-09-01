# ⚡ 35. PostgreSQL CRUD va JOIN — Dars dokumentatsiyasi

Ushbu darsda PostgreSQL serverida amaliy ravishda to'liq CRUD hamda `JOIN` amallari bajariladi. PostgreSQL da placeholder belgisi sifatida `?` emas, balki **`%s`** ishlatiladi.

---

# Kod misoli — PostgreSQL CRUD va %s

```python
import psycopg2

conn = psycopg2.connect(database="test_db", user="postgres", password="secret", host="localhost")
cursor = conn.cursor()

# INSERT (%s ishlatiladi)
cursor.execute("INSERT INTO users (name, age) VALUES (%s, %s)", ("Sardor", 24))
conn.commit()

# SELECT
cursor.execute("SELECT * FROM users WHERE age > %s", (20,))
rows = cursor.fetchall()
print(rows)

conn.close()
```

---

# 10. Qisqa xulosa

Bu darsda PostgreSQL da `%s` sintaksisi va CRUD amallari ko'rib chiqildi.
