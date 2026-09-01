# 🗄️ 31. SQL va SQLite kirish — Dars dokumentatsiyasi

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
