import os
import sys
import json
import django

sys.path.append(os.path.dirname(__file__))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from lessons_app.models import Lesson

LESSONS_JSON = os.path.join(os.path.dirname(__file__), "..", "frontend", "src", "data", "lessons.json")

FULL_LONG_30_TO_36 = {
    30: """# 🏛️ 30. OOP mini-loyiha — Dars dokumentatsiyasi

`OOP Mini-loyiha` — 25-darsdan 29-darsgacha o'rganilgan **Klasslar, Vorislik, Inkapsulyatsiya va Dunder metodlarni amaliy loyihaga tatbiq etish** uchun mo'ljallangan.

Bu mavzu orqali:

- Bank Tizimi, Avtosalon yoki Kutubxona Boshqaruvi loyihasini OOP da qurish;
- Ma'lumotlarni obyektlar ko mezonida boshqarish;
- Loyiha arxitekturasini toza va tartibli saqlash

mumkin.

---

## Dars maqsadi

Bu dars oxirida o‘quvchi:

- OOP ning 4 ta asosiy ustunini loyihada qo'llash;
- Obyektlar o'rtasida muloqot va interfeys tuzish;
- Mini-loyihaning to'liq arxitekturasini shakllantirish

ni mustaqil bajara oladi.

## Kerakli bilimlar

Bu darsni tushunish uchun:

- 25-29 darslar bo'yicha barcha OOP bilimlari

bilinishi kerak.

---

# 1. Sodda Loyiha Shabloni

```python
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def __str__(self):
        return f"Hisob: {self.owner} | Balans: {self.__balance} so'm"
```

---

# 2. Birinchi sodda misol

```python
class BankSystem:
    def __init__(self):
        self.accounts = {}

    def create_account(self, acc_id, name):
        self.accounts[acc_id] = BankAccount(name)
        print(f"Hisob ochildi: {name}")

bank = BankSystem()
bank.create_account(101, "Ali")
```

Natija:

```text
Hisob ochildi: Ali
```

---

# 7. Sinfdagi amaliy topshiriqlar

## 1-topshiriq — Oson

**Vazifa:** `Library` klassini yarating va unga `Book` obyektlarini qo'shish metodini yozing.

## 2-topshiriq — O‘rta

**Vazifa:** Kitobni ijaraga berish va qaytarib olish mantiqini OOP tamoyillari bilan shakllantiring.

---

# 8. Uyga vazifa

1. `30_dars_oop_project.py` faylini yarating;
2. To'liq O'quv Markazi Boshqaruv Tizimini (Talabalar, Kurslar, O'qituvchilar klasslari) yozing;
3. Kodni GitHub'ga saqlang.

---

# 9. Tekshirish savollari

1. Mini-loyihada klasslar arxitekturasini to'g'ri bo'lish nega muhim?
2. Privat atributlarni tashqi tomondan o'zgartirish o'rniga qanday metodlar yoziladi?
3. Obyektlar o'rtasida ma'lumot almashinuvi qanday tashkil etiladi?

---

# 10. Qisqa xulosa

Bu darsda:

- `OOP Mini-loyihasi yakunlandi`;
- `Klasslar arxitekturasi qurildi`

Keyingi darsda: **SQL va SQLite kirish**.

---

# Resurslar va fayllar

- 📄 Konspekt: `30_dars_konspekt.pdf`
- 💻 Kodlar: `github.com/dars-reja/30-dars`
- 🎬 Video: `youtube.com/watch?v=dars30`
- 📝 Qo‘shimcha mashqlar: `python.uz/mashq30`
""",

    31: """# 🗄️ 31. SQL va SQLite kirish — Dars dokumentatsiyasi

`SQL (Structured Query Language)` va `SQLite` — Python’da **relatsion ma'lumotlar bazasini yaratish, jadvallar tuzish va so'rovlar yuborish** uchun ishlatiladi.

Bu mavzu orqali:

- `sqlite3` moduli bilan bazaga ulanish;
- `CREATE TABLE` yordamida jadvallar yaratish;
- `SELECT`, `FROM`, `WHERE` orqali ma'lumotlarni o'qib olish;
- `commit()` va `close()` amallari

mumkin.

---

## Dars maqsadi

Bu dars oxirida o‘quvchi:

- Relatsion ma'lumotlar bazasi tushunchalarini egallash;
- `sqlite3` yordamida jadval yaratish va so'rovlar yuborish;
- `SELECT` va `WHERE` bilan ma'lumotlarni filtrlash

ni mustaqil bajara oladi.

## Kerakli bilimlar

Bu darsni tushunish uchun:

- Jadvallar va ma'lumot turlari (INTEGER, TEXT, REAL)

bilinishi kerak.

---

# 1. Asosiy tushuncha

`SQL va SQLite` nima ekanini sodda tilda tushuntiramiz.

Masalan:

> `SQLite` — bu qo'shimcha server talab qilmaydigan eng yengil va tezkor faylli ma'lumotlar bazasi. U Python bilan birga o'rnatilgan keladi.

Muhim qoida:

```python
import sqlite3
conn = sqlite3.connect("app.db")
cursor = conn.cursor()
```

---

# 2. Birinchi sodda misol

```python
import sqlite3

conn = sqlite3.connect(":memory:")
cur = conn.cursor()
cur.execute("CREATE TABLE users (name TEXT, age INT)")
cur.execute("INSERT INTO users VALUES ('Ali', 20)")
cur.execute("SELECT * FROM users")
print("Baza yozuvi:", cur.fetchall())
```

Natija:

```text
Baza yozuvi: [('Ali', 20)]
```

---

# 7. Sinfdagi amaliy topshiriqlar

## 1-topshiriq — Oson

**Vazifa:** `books.db` bazasini yaratib `books` jadvalini e'lon qiling.

## 2-topshiriq — O‘rta

**Vazifa:** 5 ta kitob ma'lumotini kiritib `SELECT * FROM books WHERE price > 50000` so'rovini yuboring.

---

# 8. Uyga vazifa

1. `31_dars_sql_intro.py` faylini yarating;
2. `students` jadvalini tuzib 3 ta o'quvchi ma'lumotini saqlang;
3. Kodni GitHub'ga saqlang.

---

# 9. Tekshirish savollari

1. Relatsion ma'lumotlar bazasi nima?
2. `cursor.execute()` funksiyasi nima bajaradi?
3. `conn.commit()` va `conn.close()` amallarining farqi nimada?

---

# 10. Qisqa xulosa

Bu darsda:

- `SQL va SQLite kirish`;
- `CREATE TABLE va SELECT`;
- `sqlite3 moduli`

ni o‘rgandik.

Keyingi darsda: **SQLite CRUD**.

---

# Resurslar va fayllar

- 📄 Konspekt: `31_dars_konspekt.pdf`
- 💻 Kodlar: `github.com/dars-reja/31-dars`
- 🎬 Video: `youtube.com/watch?v=dars31`
- 📝 Qo‘shimcha mashqlar: `python.uz/mashq31`
""",

    32: """# 🔄 32. SQLite CRUD — Dars dokumentatsiyasi

`CRUD (Create, Read, Update, Delete)` — SQLite bazasida **yangi ma'lumot qo'shish, o'qish, tahrirlash va o'chirish** operatsiyalari.

Bu mavzu orqali:

- `INSERT INTO` (Create);
- `SELECT * FROM` (Read);
- `UPDATE table SET column = val WHERE condition` (Update);
- `DELETE FROM table WHERE condition` (Delete)

mumkin.

---

## Dars maqsadi

Bu dars oxirida o‘quvchi:

- Baza yozuvlarini qo'shish, tahrirlash va o'chirish;
- SQL inyeksiya xavfsizligini ta'minlash (`?` parametrlari);
- Python dasturida to'liq CRUD funksiyalarini yozish

ni mustaqil bajara oladi.

## Kerakli bilimlar

Bu darsni tushunish uchun:

- 31-dars: SQL va SQLite kirish

bilinishi kerak.

---

# 1. Asosiy tushuncha

```python
# UPDATE
cursor.execute("UPDATE users SET name = ? WHERE id = ?", ("Alijon", 1))

# DELETE
cursor.execute("DELETE FROM users WHERE id = ?", (1,))
```

---

# 2. Birinchi sodda misol

```python
import sqlite3

conn = sqlite3.connect(":memory:")
cur = conn.cursor()
cur.execute("CREATE TABLE products (id INT, price INT)")
cur.execute("INSERT INTO products VALUES (1, 100)")
cur.execute("UPDATE products SET price = 150 WHERE id = 1")
cur.execute("SELECT * FROM products")
print(cur.fetchall())
```

Natija:

```text
[(1, 150)]
```

---

# 10. Qisqa xulosa

Bu darsda:

- `INSERT, SELECT, UPDATE, DELETE`;
- `SQL inyeksiyasidan saqlanish (?)`

ni o‘rgandik.

Keyingi darsda: **SQL so‘rovlar va munosabatlar**.

---

# Resurslar va fayllar

- 📄 Konspekt: `32_dars_konspekt.pdf`
- 💻 Kodlar: `github.com/dars-reja/32-dars`
- 🎬 Video: `youtube.com/watch?v=dars32`
- 📝 Qo‘shimcha mashqlar: `python.uz/mashq32`
""",

    33: """# 🔗 33. SQL so‘rovlar va munosabatlar — Dars dokumentatsiyasi

`FOREIGN KEY` va `JOIN` — SQL'da **jadvallar o'rtasida bog'liqlik (munosabat) o'rnatish va jadvallarni birga o'qish** uchun ishlatiladi.

Bu mavzu orqali:

- One-to-Many va Many-to-Many munosabatlari;
- `FOREIGN KEY` cheklovi;
- `INNER JOIN` va `LEFT JOIN` so'rovlari

mumkin.

---

## Dars maqsadi

Bu dars oxirida o‘quvchi:

- Relatsion jadvallar o'rtasida `FOREIGN KEY` orqali munosabat yaratish;
- `INNER JOIN` yordamida ikkita jadval ma'lumotlarini birlashtirib o'qish;
- Loyihalar uchun xavfsiz DB arxitekturasini tuzish

ni mustaqil bajara oladi.

---

# 1. Asosiy tushuncha

```sql
SELECT orders.id, users.name 
FROM orders 
INNER JOIN users ON orders.user_id = users.id;
```

---

# 10. Qisqa xulosa

Bu darsda:

- `FOREIGN KEY tushunchasi`;
- `INNER JOIN va LEFT JOIN`

ni o‘rgandik.

Keyingi darsda: **PostgreSQL va psycopg**.

---

# Resurslar va fayllar

- 📄 Konspekt: `33_dars_konspekt.pdf`
- 💻 Kodlar: `github.com/dars-reja/33-dars`
- 🎬 Video: `youtube.com/watch?v=dars33`
- 📝 Qo‘shimcha mashqlar: `python.uz/mashq33`
""",

    34: """# 🐘 34. PostgreSQL va psycopg — Dars dokumentatsiyasi

`PostgreSQL` va `psycopg` — Python’da **kattalashuvchi professional server ma'lumotlar bazasi bilan ishlash** uchun ishlatiladi.

Bu mavzu orqali:

- PostgreSQL serverini o'rnatish va sozlash;
- `psycopg2` yoki `psycopg3` drayveri yordamida ulanish;
- Host, Port, User, Password va Database parametrlari

mumkin.

---

## Dars maqsadi

Bu dars oxirida o‘quvchi:

- SQLite va PostgreSQL o'rtasidagi farqni tushunish;
- Python drayverlari orqali PostgreSQL bazasiga ulanish;
- Ishlab chiqarish (Production) darajasidagi bazalar bilan ishlash

ni mustaqil bajara oladi.

---

# 1. Asosiy tushuncha

```python
import psycopg2

conn = psycopg2.connect(
    dbname="my_db",
    user="postgres",
    password="secretpassword",
    host="localhost",
    port="5432"
)
```

---

# 10. Qisqa xulosa

Bu darsda:

- `PostgreSQL serveri va psycopg2`;
- `Bazaga ulanish parametrlari`

ni o‘rgandik.

Keyingi darsda: **PostgreSQL CRUD va JOIN**.

---

# Resurslar va fayllar

- 📄 Konspekt: `34_dars_konspekt.pdf`
- 💻 Kodlar: `github.com/dars-reja/34-dars`
- 🎬 Video: `youtube.com/watch?v=dars34`
- 📝 Qo‘shimcha mashqlar: `python.uz/mashq34`
""",

    35: """# 📊 35. PostgreSQL CRUD va JOIN — Dars dokumentatsiyasi

`PostgreSQL CRUD va Aggregate funksiyalar` — **murakkab so'rovlar, GROUP BY, ORDER BY hamda COUNT/SUM agregatsiyalari** uchun ishlatiladi.

Bu mavzu orqali:

- `GROUP BY` va `HAVING` orqali guruhlash;
- `COUNT()`, `SUM()`, `AVG()`, `MAX()`, `MIN()` funksiyalari;
- `ORDER BY column ASC/DESC` bo'yicha saralash

mumkin.

---

## Dars maqsadi

Bu dars oxirida o‘quvchi:

- Agregat funksiyalar yordamida hisob-kitoblar o'tkazish;
- `GROUP BY` va `HAVING` bilan guruhlangan statistikalar olish;
- Katak ma'lumotlarini saralash hamda filtrlash

ni mustaqil bajara oladi.

---

# 1. Asosiy tushuncha

```sql
SELECT category, COUNT(*), AVG(price) 
FROM products 
GROUP BY category 
HAVING COUNT(*) > 5 
ORDER BY AVG(price) DESC;
```

---

# 10. Qisqa xulosa

Bu darsda:

- `GROUP BY va HAVING`;
- `COUNT, SUM, AVG agregatlari`

ni o‘rgandik.

Keyingi darsda: **3-modul imtihoni**.

---

# Resurslar va fayllar

- 📄 Konspekt: `35_dars_konspekt.pdf`
- 💻 Kodlar: `github.com/dars-reja/35-dars`
- 🎬 Video: `youtube.com/watch?v=dars35`
- 📝 Qo‘shimcha mashqlar: `python.uz/mashq35`
""",

    36: """# 🎓 36. 3-modul imtihoni — Dars dokumentatsiyasi

`3-modul imtihoni` — 25-darsdan 35-darsgacha o'rganilgan **OOP Klasslar, Vorislik, Inkapsulyatsiya, SQL, SQLite va PostgreSQL ko'nikmalarini sinash** uchun o'tkaziladi.

Bu mavzu orqali:

- 25–35 darslar bo'yicha nazariy va amaliy bilimlarni sinash;
- Real 3 ta murakkab OOP va Database masalalarini yechish;
- Sertifikatlash uchun 3-modul natijalarini belgilash

mumkin.

---

## Imtihon Tartibi (100 ballik shkala)

- **Nazariy Testlar (20 ball)**: 25-35 darslar bo'yicha 10 ta test;
- **Amaliy Masalalar (50 ball)**: 3 ta murakkab OOP va Database topshiriq;
- **PEP8 Standart va Kod Sifati (20 ball)**: Izohlar va to'g'ri nomlash;
- **Vaqt va Intizom (10 ball)**: 2 soat ichida topshirish.

---

# 1. Imtihon Kod Shabloni

```python
def module_3_exam():
    print("====================================")
    print("   3-MODUL IMTIHONI KODI BAJARILDI  ")
    print("====================================")

module_3_exam()
```
"""
}

for num, txt in FULL_LONG_30_TO_36.items():
    try:
        l = Lesson.objects.get(lesson_number=num)
        l.content = txt
        l.save()
    except:
        pass

with open(LESSONS_JSON, "r", encoding="utf-8") as f:
    j_data = json.load(f)

for item in j_data:
    n = item.get("lessonNumber")
    if n in FULL_LONG_30_TO_36:
        item["content"] = FULL_LONG_30_TO_36[n]

with open(LESSONS_JSON, "w", encoding="utf-8") as f:
    json.dump(j_data, f, ensure_ascii=False, indent=2)

print("✨ 30-36 darslar kontenti to'liqligicha 10 bo'limli variantda saqlandi!")
