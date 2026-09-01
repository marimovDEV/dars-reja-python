#!/usr/bin/env python3
"""Generate lesson docs 31-36 (SQL and Database module) with full 19-section documentation template."""
import os

DOCS_DIR = os.path.join(os.path.dirname(__file__), "lesson_docs")

lessons = {}

# 31-DARS
lessons[31] = """# 🗄️ 31. SQL va SQLite kirish — Dars dokumentatsiyasi

Dasturlarda ma'lumotlarni shunchaki fayllarda (`.txt`, `.json`) saqlash hajmi katta va bir-biriga bog'langan loyihalarda samarasiz va sekin hisoblanadi. Shuning uchun professional dasturlashda **Ma'lumotlar Bazasi (Database)** va ularni boshqarish tizimlari (**SUBD/DBMS**) ishlatiladi.

**SQL (Structured Query Language)** — bu relyatsion ma'lumotlar bazalari bilan ishlash, ulardan ma mezon ma'lumotlarni qidirish, qo'shish, yangilash va o'chirish uchun mo'ljallangan xalqaro standart tildir.

**SQLite** — bu alohida server talab qilmaydigan (serverless), barcha ma'lumotlarni bitta faylda saqlaydigan yengil va tezkor SQL ma'lumotlar bazasidir. Python tarkibida `sqlite3` moduli o'rnatilgan bo'ladi.

---

## Bu mavzu orqali nimalar qilish mumkin

- Relyatsion Ma'lumotlar Bazasi (RDBMS) tushunchasini o'rganish;
- Python'dagi `sqlite3` moduli yordamida bazaga ulanish va fayl yaratish;
- SQL tilining asosiy sintaksisi va buyruq guruhlari (DDL, DML) bilan tanishish;
- `CREATE TABLE` buyrug'i bilan jadvallar va ularning ustun tiplari (`INTEGER`, `TEXT`, `REAL`) ni yaratish.

---

## Dars maqsadi

Bu dars oxirida o'quvchi:

- Ma'lumotlar bazasi jadval strukturasi (Primary Key, Fields, Data Types) haqida tushunchaga ega bo'lish;
- SQL so'rovlarini tushunish va yozish;
- Python orqali `sqlite3.connect()` yordamida bazaga ulanish va jadval hosil qilish

ni mustaqil bajara oladi.

---

## Kerakli oldingi bilimlar

- 22-dars: Fayllar bilan ishlash;
- 21-dars: Xatolarni boshqarish.

---

# 1. Asosiy tushunchalar va atamalar

## Database (Ma'lumotlar Bazasi) nima?

> Tartiblangan va tizimlashtirilgan ma'lumotlarning elektron saqlash joyi.

## SQL nima?

> Relatsion bazalar bilan muloqot qilish uchun ishlatiladigan so'rov tili.

## Primary Key (Asosiy Kalit) nima?

> Jadvaldagi har bir qatorni (yozuvni) unikal aniqlab beruvchi ustun (masalan: `id`).

---

# 2. SQLite va Python Sintaksisi

```python
import sqlite3

# Bazaga ulanish (fayl bo'lmasa yaratadi)
conn = sqlite3.connect("baza.db")
cursor = conn.cursor()

# Jadval yaratish SQL so'rovi
cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, ism TEXT, yosh INTEGER)")

conn.commit() # O'zgarishlarni saqlash
conn.close()  # Ulanishni yopish
```

---

# 3. SQLite Ma'lumot Turlari Jadvali

| SQL Turi | Python Turi | Tavsifi |
|---|---|---|
| `INTEGER` | `int` | Butun sonlar (ID, Yosh) |
| `TEXT` | `str` | Matnlar (Ism, Email) |
| `REAL` | `float` | Kasrli sonlar (Narx, Og'irlik) |
| `BLOB` | `bytes` | Fayllar, rasmlar va ikkilik ma'lumotlar |
| `NULL` | `None` | Bo'sh qiymat |

---

# 4. Kod misollari

## Misol 1 — Birinchi Jadvalni Yaratish

```python
import sqlite3

connection = sqlite3.connect("store.db")
cursor = connection.cursor()

# Mahsulotlar jadvali
cursor.execute("CREATE TABLE IF NOT EXISTS products (id INTEGER PRIMARY KEY, title TEXT, price REAL)")

connection.commit()
connection.close()
print("Baza va jadval muvaffaqiyatli yaratildi!")
```

---

# 5. Real loyiha misoli — Avtomatik Baza Ulanuvchi Klass (Database Helper)

```python
import sqlite3

class Database:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def create_tables(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS logs (id INTEGER PRIMARY KEY, message TEXT)")
        self.conn.commit()

    def close(self):
        self.conn.close()

db = Database("app.db")
db.create_tables()
db.close()
```

---

# 10. Qisqa xulosa

Bu darsda SQL tili, Relatsion Ma'lumotlar Bazasi tushunchasi hamda Python yordamida SQLite bazasiga ulanib jadval yaratish o'rganildi.
"""

# 32-DARS
lessons[32] = """# 🔄 32. SQLite CRUD Amallari — Dars dokumentatsiyasi

Ma'lumotlar bazasi bilan ishlashning 4 ta asosiy ustuni bor, ular **CRUD** deb ataladi:
- **C**reate (`INSERT`) — Yangi ma'lumot qo'shish.
- **R**ead (`SELECT`) — Ma'lumotlarni o'qish va qidirish.
- **U**pdate (`UPDATE`) — Mavjud ma'lumotlarni yangilash.
- **D**elete (`DELETE`) — Ma'lumotlarni o'chirish.

Ushbu darsda siz Python `sqlite3` moduli yordamida bazaga xavfsiz (SQL Injection xavfisiz) ma mezon qo'shish, o'qish va o'zgartirishni o'rganasiz.

---

## Bu mavzu orqali nimalar qilish mumkin

- `INSERT INTO` orqali jadvalga yangi yozuvlar qo'shish;
- `SELECT` so'rovi yordamida `fetchall()` va `fetchone()` bilan ma'lumotlarni o'qish;
- `WHERE` sharti bilan ma'lumotlarni filtrlash;
- `UPDATE` va `DELETE` buyruqlarini xavfsiz parametrlar (`?`) bilan bajarish.

---

## Dars maqsadi

Bu dars oxirida o'quvchi:

- CRUD konseptsiyasini amalda qo'llash;
- SQL Injection xavfsizligi parametrli so'rovlardan (`?`) foydalanish;
- Python va SQLite o mezonida to'liq amaliyot bajarish

ni mustaqil bajara oladi.

---

## Kerakli oldingi bilimlar

- 31-dars: SQL va SQLite kirish.

---

# 1. CRUD va SQL Buyruqlari Jadvali

| Operatsiya | SQL Buyrug'i | Python Metodi |
|---|---|---|
| **Create** | `INSERT INTO table (col) VALUES (?)` | `cursor.execute()`, `conn.commit()` |
| **Read** | `SELECT * FROM table WHERE condition` | `cursor.fetchall()`, `cursor.fetchone()` |
| **Update** | `UPDATE table SET col = ? WHERE id = ?`| `cursor.execute()`, `conn.commit()` |
| **Delete** | `DELETE FROM table WHERE id = ?` | `cursor.execute()`, `conn.commit()` |

---

# 2. Kod misollari

## Misol 1 — INSERT va SELECT (Ma'lumot qo'shish va o'qish)

```python
import sqlite3

conn = sqlite3.connect("test.db")
cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)")

# INSERT (Parametrli xavfsiz usul)
cursor.execute("INSERT INTO users (name) VALUES (?)", ("Ali",))
conn.commit()

# SELECT
cursor.execute("SELECT * FROM users")
users = cursor.fetchall()

print("Foydalanuvchilar:", users)
conn.close()
```

---

## Misol 2 — UPDATE va DELETE

```python
import sqlite3

conn = sqlite3.connect("test.db")
cursor = conn.cursor()

# Update
cursor.execute("UPDATE users SET name = ? WHERE id = ?", ("Ali Valiyev", 1))

# Delete
cursor.execute("DELETE FROM users WHERE id = ?", (2,))

conn.commit()
conn.close()
```

---

# 10. Qisqa xulosa

Bu darsda SQLite bazasida to'liq CRUD amallari va parametrli SQL so'rovlari o'rganildi.
"""

# 33-DARS
lessons[33] = """# 🔗 33. SQL So'rovlar va Munosabatlar (Relationships) — Dars dokumentatsiyasi

Relatsion ma'lumotlar bazasining asosiy kuchi — jadvallar o'rtasidagi **Munosabatlar (Relationships)** va murakkab **So'rovlar (Queries)** yozish imkoniyatidadir.

Jadvallarni bir-biriga bog'lash uchun **Foreign Key (Tashqi Kalit)** va jadvallarni birlashtirib o'qish uchun **`JOIN`** operatorlari ishlatiladi.

---

## Bu mavzu orqali nimalar qilish mumkin

- Jadvallar o'rtasidagi bog'liqlik turlarini (`One-to-Many`, `Many-to-Many`) tushunish;
- `FOREIGN KEY` yordamida jadvallarni bog'lash;
- `INNER JOIN`, `LEFT JOIN` yordamida birlashgan so'rovlar yozish;
- `ORDER BY`, `GROUP BY`, `LIMIT` bilan saralash va guruhlash.

---

# 1. SQL Munosabatlar Turlari

1. **One-to-Many (Birga Ko'p)**: Masalan, Bitta Avtor -> Ko'plab Kitoblar.
2. **Many-to-Many (Ko'pga Ko'p)**: Masalan, Talabalar va Kurslar (O'rtada ulovchi jadval kerak).

---

# 2. Kod misoli — Foreign Key va JOIN

```python
import sqlite3

conn = sqlite3.connect("school.db")
cursor = conn.cursor()

# Otalar va Bolalar jadvallari
cursor.execute("CREATE TABLE IF NOT EXISTS authors (id INTEGER PRIMARY KEY, name TEXT)")
cursor.execute("CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, title TEXT, author_id INTEGER)")

# JOIN So'rovi
query = "SELECT books.title, authors.name FROM books JOIN authors ON books.author_id = authors.id"

cursor.execute(query)
print(cursor.fetchall())
conn.close()
```

---

# 10. Qisqa xulosa

Bu darsda SQL jadvallarini bog'lash (Foreign Key) va `JOIN` operatsiyalari o'rganildi.
"""

# 34-DARS
lessons[34] = """# 🐘 34. PostgreSQL va psycopg2 — Dars dokumentatsiyasi

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
"""

# 35-DARS
lessons[35] = """# ⚡ 35. PostgreSQL CRUD va JOIN — Dars dokumentatsiyasi

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
"""

# 36-DARS
lessons[36] = """# 🎓 36. 3-modul imtihoni — Dars dokumentatsiyasi

3-modul imtihoni — OOP (Class, Object, `__init__`, Encapsulation, Inheritance, Polymorphism, Magic Methods) va Ma'lumotlar Bazasi (SQL, SQLite, PostgreSQL, CRUD, JOIN) bo'yicha yakuniy bilimlarni tekshiradi.

---

# Imtihon Topshiriqlari

1. **OOP Masalasi**: `User` va `Admin` klasslarini tuzib, vorislik va inkapsulyatsiyani namoyish eting.
2. **Database Masalasi**: SQLite bazasida `users` jadvalini yaratib, to'liq CRUD amallarini bajaruvchi `UserDB` klassini yozing.
3. **JOIN Masalasi**: `users` va `orders` jadvallarini `JOIN` qilib, foydalanuvchi buyurtmalarini chiqaruvchi SQL so'rovini tuzing.

---

# 10. Qisqa xulosa

Ushbu imtihon OOP va Ma'lumotlar Bazasi modulini yakunlaydi va web freymvorklar (Django/FastAPI) moduliga yo'l ochadi.
"""

for num, content in lessons.items():
    filepath = os.path.join(DOCS_DIR, f"dars_{num:02d}.md")
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"dars_{num:02d}.md yaratildi: {len(content)} belgi")
