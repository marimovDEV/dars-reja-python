import os
import sys
import json
import django

# Setup Django
sys.path.append(os.path.dirname(__file__))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from lessons_app.models import Lesson

LESSONS_JSON = os.path.join(os.path.dirname(__file__), "..", "frontend", "src", "data", "lessons.json")

EXACT_25_TO_36_LESSONS = {
    25: {
        "title": "25-dars — OOP, class va object",
        "content": """# 🏗️ 25. OOP, class va object — Dars dokumentatsiyasi

`OOP (Object-Oriented Programming)` — Python’da **kodni real hayotdagi obyektlar va klasslar ko'rinishida modellashtirish** uchun ishlatiladi.

Bu mavzu orqali:

- `class` (shablon) va `object` (obyekt/nusxa) tushunchalari;
- Obyekt xususiyatlari (atributlar) va xatti-harakatlari (metodlar);
- Klass yaratish hamda obyektlar nusxasini olish

mumkin.

---

## Dars maqsadi

Bu dars oxirida o‘quvchi:

- Class va Object tushunchasining farqini tushunish;
- Yangi klass yaratish va undan ko'plab obyektlar olish;
- Klass metodlarini yozish va shakllantirish

ni mustaqil bajara oladi.

## Kerakli bilimlar

Bu darsni tushunish uchun:

- 14-dars: Dictionary;
- 17-dars: Funksiyalar (`def`)

bilinishi kerak.

---

# 1. Asosiy tushuncha

`OOP, class va object` nima ekanini sodda tilda tushuntiramiz.

Masalan:

> `Class` — bu obyekt yaratish uchun mo'ljallangan chizma/shablon (masalan, moshina loyihasi). `Object` — ushbu chizma asosida yaratilgan real nusxa (masalan, muayyan moshina).

Muhim qoida:

```python
class User:
    pass

user1 = User()  # Obyekt yaratish
```

---

# 2. Birinchi sodda misol

```python
class Student:
    name = "Ali"
    course = 2

student1 = Student()
print("Talaba ismi:", student1.name)
print("Kursi:", student1.course)
```

Natija:

```text
Talaba ismi: Ali
Kursi: 2
```

Izoh:

- `1-3 qatorlar` — `Student` klassi e'lon qilindi va unga atributlar berildi;
- `5-qator` — `Student()` orqali `student1` obyekti yaratildi.

---

# 3. Asosiy metodlar yoki operatorlar

| Tushuncha | Vazifasi | Misol |
|---|---|---|
| `class` | Klass e'lon qilish kalit so'zi | `class Car:` |
| `object` | Klassdan olingan nusxa | `my_car = Car()` |
| Atribut | Obyekt o'zgaruvchisi/xususiyati | `car.brand` |
| Metod | Klass ichidagi funksiya | `car.start()` |

---

# 4. Batafsil misol — Laptop Klassi

```python
class Laptop:
    brand = "HP"
    ram = 8
    
    def get_info(self):
        return f"Noutbuk: {self.brand} | RAM: {self.ram} GB"

my_laptop = Laptop()
print(my_laptop.get_info())
```

Natija:

```text
Noutbuk: HP | RAM: 8 GB
```

---

# 6. Ko‘p uchraydigan xatolar

## Xato 1: Metodlarda 'self' parametridan foydalanmaslik

Noto‘g‘ri:

```python
class Car:
    def drive():  # TypeError bo'ladi!
        print("Haydamoqda")
```

To‘g‘ri:

```python
class Car:
    def drive(self):
        print("Haydamoqda")
```

---

# 7. Sinfdagi amaliy topshiriqlar

## 1-topshiriq — Oson

**Vazifa:** `Book` nomli klass yarating (title, author) va undan 2 ta obyekt oling.

## 2-topshiriq — O‘rta

**Vazifa:** `Rectangle` klassini tuzing va uning yuzini hisoblaydigan `get_area()` metodini yozing.

---

# 8. Uyga vazifa

1. `25_dars_oop_basics.py` faylini yarating;
2. `Phone` klassini tuzib, unga `call()` va `text()` metodlarini qo'shing;
3. Kodni GitHub'ga saqlang.

---

# 9. Tekshirish savollari

1. Class va Object ning asosiy farqi nima?
2. Klass ichidagi funksiya nima deyiladi (Metod)?
3. `self` parametrining vazifasi nima?

---

# 10. Qisqa xulosa

Bu darsda:

- `OOP tushunchasi`;
- `class va object yaratish`;
- `Klass atributlari va metodlari`

ni o‘rgandik.

Keyingi darsda: **__init__ va self**.

---

# Resurslar va fayllar

- 📄 Konspekt: `25_dars_konspekt.pdf`
- 💻 Kodlar: `github.com/dars-reja/25-dars`
- 🎬 Video: `youtube.com/watch?v=dars25`
- 📝 Qo‘shimcha mashqlar: `python.uz/mashq25`
""",
        "code": "class Laptop:\n    def __init__(self, brand, ram):\n        self.brand = brand\n        self.ram = ram\n    def upgrade_ram(self, extra):\n        self.ram += extra\n\nmy_laptop = Laptop('HP', 8)\nmy_laptop.upgrade_ram(8)\nprint(f'{my_laptop.brand} RAM: {my_laptop.ram} GB')",
        "code_exp": "- `1-6 qatorlar` — Laptop klassi va RAM hajmini oshiruvchi upgrade_ram metodi;\n- `8-10 qatorlar` — Obyekt yaratilib RAM 16 GB ga oshiriladi.",
        "quiz_q": "Klassdan yaratilgan nusxa nima deyiladi?",
        "quiz_opts": ["Metod", "Atribut", "Obyekt (Object)", "Funksiya"],
        "quiz_ans": 2,
        "quiz_exp": "Klass — bu shablon, undan yaratilgan amaliy nusxa esa Obyekt (Object) deyiladi."
    },

    26: {
        "title": "26-dars — __init__ va self",
        "content": """# ⚙️ 26. __init__ va self — Dars dokumentatsiyasi

`__init__` va `self` — Python’da **obyekt yaratilayotganda uning atributlarini avtomatik ishga tushirish (konstruktor)** uchun ishlatiladi.

Bu mavzu orqali:

- `__init__()` konstruktor metodi;
- `self` atamasi yordamida joriy obyekt xususiyatlariga murojaat qilish;
- obyekt yaratilayotganda dinamik qiymatlar berish (`User("Ali", 20)`)

mumkin.

---

## Dars maqsadi

Bu dars oxirida o‘quvchi:

- `__init__` konstruktoridan foydalanib har xil atributli obyektlar yaratish;
- `self` mantiqan joriy obyektga ishora qilishini tushunish;
- Obyekt parametrlarini dinamik ravishda o'zgartirish

ni mustaqil bajara oladi.

---

# 1. Asosiy tushuncha

```python
class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

user1 = User("ali_dev", "ali@dev.uz")
print(user1.username)
```
""",
        "code": "class User:\n    def __init__(self, name, role='User'):\n        self.name = name\n        self.role = role\n\nuser1 = User('Sardor', 'Admin')\nprint(user1.name, user1.role)",
        "code_exp": "- `1-4 qatorlar` — __init__ konstruktori orqali name va role atributlari beriladi;\n- `6-7 qatorlar` — Yangi User yaratiladi.",
        "quiz_q": "Obyekt yaratilgan paytda avtomatik ishlaydigan konstruktor metodi qaysi?",
        "quiz_opts": ["__start__", "__init__", "__create__", "__main__"],
        "quiz_ans": 1,
        "quiz_exp": "__init__ metodi klassdan yangi obyekt olinganda avtomatik ishga tushadi."
    },

    27: {
        "title": "27-dars — Inkapsulyatsiya",
        "content": """# 🔒 27. Inkapsulyatsiya — Dars dokumentatsiyasi

`Inkapsulyatsiya (Encapsulation)` — Python’da **obyekt ichidagi ma'lumotlarni tashqi ruxsat etilmagan aralashuvlardan himoyalash** uchun ishlatiladi.

Bu mavzu orqali:

- Public (ochiq), Protected (`_name`) va Private (`__name`) atributlar;
- Getter va Setter metodlari;
- `@property` dekoratori yordamida xavfsiz boshqaruv

mumkin.

---

# 1. Asosiy tushuncha

```python
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # Private atribut

    def get_balance(self):
        return self.__balance
```
""",
        "code": "class BankAccount:\n    def __init__(self, balance):\n        self.__balance = balance\n    def deposit(self, amount):\n        if amount > 0:\n            self.__balance += amount\n    def get_balance(self):\n        return self.__balance",
        "code_exp": "- `1-3 qatorlar` — __balance private qilinib yashirilgan;\n- `4-8 qatorlar` — deposit va get_balance orqali xavfsiz boshqariladi.",
        "quiz_q": "Python'da atributni Private (shaxsiy) qilish uchun uning nomi nima bilan boshlanadi?",
        "quiz_opts": ["_", "__", "private", "#"],
        "quiz_ans": 1,
        "quiz_exp": "Ikkita pastki chiziq (__) bilan boshlangan atributlar Private bo'ladi."
    },

    28: {
        "title": "28-dars — Vorislik va polymorphism",
        "content": """# 🧬 28. Vorislik va polymorphism — Dars dokumentatsiyasi

`Vorislik (Inheritance)` va `Polimorfizm (Polymorphism)` — Python’da **mavjud klass xususiyatlarini yangi klassga o'tkazish va metodlarni qayta aniqlash** uchun ishlatiladi.

Bu mavzu orqali:

- Ota klass (Parent class) va Bola klass (Child class);
- `super().__init__()` orqali ota klass konstruktorini chaqirish;
- Metodlarni ustidan yozish (Method Overriding)

mumkin.

---

# 1. Asosiy tushuncha

```python
class Animal:
    def make_sound(self):
        print("Ovoz chiqaradi")

class Dog(Animal):
    def make_sound(self):
        print("Vov-vov!")
```
""",
        "code": "class Person:\n    def __init__(self, name):\n        self.name = name\n\nclass Student(Person):\n    def __init__(self, name, student_id):\n        super().__init__(name)\n        self.student_id = student_id\n\ns = Student('Ali', 'ST-1001')\nprint(s.name, s.student_id)",
        "code_exp": "- `1-3 qatorlar` — Person ota klassi;\n- `5-8 qatorlar` — Student klassi Person'dan voris oladi va super() orqali ismni biriktiradi.",
        "quiz_q": "Ota klass konstruktorini bola klassda chaqiruvchi funksiya qaysi?",
        "quiz_opts": ["parent()", "super()", "base()", "inherit()"],
        "quiz_ans": 1,
        "quiz_exp": "super() funksiyasi ota klass metodlari va konstruktorini chaqirishda ishlatiladi."
    },

    29: {
        "title": "29-dars — Class/static va dunder metodlar",
        "content": """# 🛠️ 29. Class/static va dunder metodlar — Dars dokumentatsiyasi

`@classmethod`, `@staticmethod` va `Dunder metodlar` — Python’da **klass darajasidagi metodlar hamda maxsus sehrli metodlarni (`__str__`, `__len__`) shakllantirish** uchun ishlatiladi.

Bu mavzu orqali:

- `@classmethod` va `cls` parametri;
- `@staticmethod` (yordamchi metodlar);
- `__str__()` (obyektni string sifat chop etish);
- `__len__()` (obyekt uzunligini qaytarish)

mumkin.

---

# 1. Asosiy tushuncha

```python
class User:
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return f"User({self.name})"
```
""",
        "code": "class MathUtils:\n    @staticmethod\n    def add(a, b):\n        return a + b\n\nclass Book:\n    def __init__(self, title):\n        self.title = title\n    def __str__(self):\n        return f'Kitob: {self.title}'\n\nprint(MathUtils.add(5, 10))\nprint(Book('Python Backend'))",
        "code_exp": "- `1-4 qatorlar` — @staticmethod obyekt yaratmasdan chaqiriladi;\n- `6-10 qatorlar` — __str__ dunder metodi print bo'lganda chiroyli matn beradi.",
        "quiz_q": "Obyekt print() qilinganda chiroyli matn shaklida chiqishini ta'minlovchi dunder metod qaysi?",
        "quiz_opts": ["__init__", "__str__", "__repr__", "__call__"],
        "quiz_ans": 1,
        "quiz_exp": "__str__ dunder metodi obyektning string ko'rinishini belgilaydi."
    },

    30: {
        "title": "30-dars — OOP mini-loyiha",
        "content": """# 🏛️ 30. OOP mini-loyiha — Dars dokumentatsiyasi

`OOP Mini-loyiha` — 25-darsdan 29-darsgacha o'rganilgan **Klasslar, Vorislik, Inkapsulyatsiya va Dunder metodlarni amaliy loyihaga tatbiq etish** uchun mo'ljallangan.

Bu mavzu orqali:

- Bank Tizimi yoki Kutubxona Boshqaruvi loyihasini OOP da qurish;
- Ma'lumotlarni obyektlar ko mezonida boshqarish;
- Loyiha arxitekturasini toza va tartibli saqlash

mumkin.

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
""",
        "code": "class BankSystem:\n    def __init__(self):\n        self.accounts = {}\n    def create_account(self, acc_id, name):\n        self.accounts[acc_id] = {'name': name, 'balance': 0}\n        print(f'Hisob ochildi: {name}')\n\nbank = BankSystem()\nbank.create_account(101, 'Ali')",
        "code_exp": "- `1-6 qatorlar` — Bank loyihasining asosiy klassi;\n- `8-9 qatorlar` — Yangi hisob yaratish va tizimda saqlash.",
        "quiz_q": "OOP mini-loyihasida obyektlar holatini saqlash va boshqarish uchun nima ishlatiladi?",
        "quiz_opts": ["Faqat globallar", "Klasslar va atributlar", "HTML fayllar", "Faqat input"],
        "quiz_ans": 1,
        "quiz_exp": "OOP loyihalarida ma'lumot va mantiq Klass atributlari va metodlarida saqlanadi."
    },

    31: {
        "title": "31-dars — SQL va SQLite kirish",
        "content": """# 🗄️ 31. SQL va SQLite kirish — Dars dokumentatsiyasi

`SQL (Structured Query Language)` va `SQLite` — Python’da **relatsion ma'lumotlar bazasini yaratish va so'rovlar yuborish** uchun ishlatiladi.

Bu mavzu orqali:

- `sqlite3` moduli bilan bazaga ulanish;
- `CREATE TABLE` yordamida jadvallar yaratish;
- `SELECT`, `FROM`, `WHERE` orqali ma'lumotlarni o'qib olish;
- `commit()` va `close()` amallari

mumkin.

---

# 1. Asosiy tushuncha

```python
import sqlite3

conn = sqlite3.connect("academy.db")
cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)")
conn.commit()
conn.close()
```
""",
        "code": "import sqlite3\nconn = sqlite3.connect(':memory:')\ncur = conn.cursor()\ncur.execute('CREATE TABLE users (name TEXT, age INT)')\ncur.execute(\"INSERT INTO users VALUES ('Ali', 20)\")\ncur.execute('SELECT * FROM users')\nprint('Baza yozuvi:', cur.fetchall())",
        "code_exp": "- `1-3 qatorlar` — Xotirada vaqtinchalik SQLite bazasini yaratish;\n- `4-7 qatorlar` — Jadval tuzilib, ma'lumot yoziladi va SELECT bilan o'qiladi.",
        "quiz_q": "Jadvaldan ma'lumotlarni o'qib olish uchun qaysi SQL buyrug'i ishlatiladi?",
        "quiz_opts": ["GET", "FETCH", "SELECT", "READ"],
        "quiz_ans": 2,
        "quiz_exp": "SELECT buyrug'i bazadagi jadvallardan ma'lumotlarni saralab olish uchun ishlatiladi."
    },

    32: {
        "title": "32-dars — SQLite CRUD",
        "content": """# 🔄 32. SQLite CRUD — Dars dokumentatsiyasi

`CRUD (Create, Read, Update, Delete)` — SQLite bazasida **yangi ma'lumot qo'shish, o'qish, tahrirlash va o'chirish** operatsiyalari.

Bu mavzu orqali:

- `INSERT INTO` (Create);
- `SELECT * FROM` (Read);
- `UPDATE table SET column = val WHERE condition` (Update);
- `DELETE FROM table WHERE condition` (Delete)

mumkin.

---

# 1. Asosiy tushuncha

```python
# UPDATE
cursor.execute("UPDATE users SET name = 'Alijon' WHERE id = 1")

# DELETE
cursor.execute("DELETE FROM users WHERE id = 1")
```
""",
        "code": "import sqlite3\nconn = sqlite3.connect(':memory:')\ncur = conn.cursor()\ncur.execute('CREATE TABLE products (id INT, price INT)')\ncur.execute('INSERT INTO products VALUES (1, 100)')\ncur.execute('UPDATE products SET price = 150 WHERE id = 1')\ncur.execute('SELECT * FROM products')\nprint(cur.fetchall())",
        "code_exp": "- `1-5 qatorlar` — Bazada mahsulot narxi 100 ga o'rnatildi;\n- `6-8 qatorlar` — UPDATE orqali narx 150 ga yangilandi.",
        "quiz_q": "Bazadagi mavjud ma'lumotni yangilash uchun qaysi SQL buyrug'i ishlatiladi?",
        "quiz_opts": ["CHANGE", "UPDATE", "MODIFY", "ALTER"],
        "quiz_ans": 1,
        "quiz_exp": "UPDATE buyrug'i jadvaldagi mavjud qator ma'lumotlarini o'zgartirish uchun ishlatiladi."
    },

    33: {
        "title": "33-dars — SQL so‘rovlar va munosabatlar",
        "content": """# 🔗 33. SQL so‘rovlar va munosabatlar — Dars dokumentatsiyasi

`FOREIGN KEY` va `JOIN` — SQL'da **jadvallar o'rtasida bog'liqlik (munosabat) o'rnatish va jadvallarni birga o'qish** uchun ishlatiladi.

Bu mavzu orqali:

- One-to-Many va Many-to-Many munosabatlari;
- `FOREIGN KEY` cheklovi;
- `INNER JOIN` va `LEFT JOIN` so'rovlari

mumkin.

---

# 1. Asosiy tushuncha

```sql
SELECT orders.id, users.name 
FROM orders 
INNER JOIN users ON orders.user_id = users.id;
```
""",
        "code": "import sqlite3\nconn = sqlite3.connect(':memory:')\ncur = conn.cursor()\ncur.execute('CREATE TABLE users (id INT PRIMARY KEY, name TEXT)')\ncur.execute('CREATE TABLE posts (id INT, user_id INT, title TEXT)')\ncur.execute(\"INSERT INTO users VALUES (1, 'Ali')\")\ncur.execute(\"INSERT INTO posts VALUES (101, 1, 'First Post')\")\ncur.execute('SELECT users.name, posts.title FROM posts JOIN users ON posts.user_id = users.id')\nprint(cur.fetchall())",
        "code_exp": "- `1-6 qatorlar` — users va posts jadvallari yaratilib bog'landi;\n- `7-8 qatorlar` — JOIN so'rovi yordamida ikkala jadval ma'lumoti bitta so'rovda olindi.",
        "quiz_q": "Ikki jadvalni kalit bo'yicha birlashtirib o'qish uchun qaysi SQL buyrug'i ishlatiladi?",
        "quiz_opts": ["COMBINE", "JOIN", "LINK", "MERGE"],
        "quiz_ans": 1,
        "quiz_exp": "JOIN buyrug'i ikkita yoki undan ortiq jadvallarni bog'liq kalitlari bo'yicha birlashtiradi."
    },

    34: {
        "title": "34-dars — PostgreSQL va psycopg",
        "content": """# 🐘 34. PostgreSQL va psycopg — Dars dokumentatsiyasi

`PostgreSQL` va `psycopg` — Python’da **kattalashuvchi professional server ma'lumotlar bazasi bilan ishlash** uchun ishlatiladi.

Bu mavzu orqali:

- PostgreSQL serverini o'rnatish va sozlash;
- `psycopg2` yoki `psycopg3` drayveri yordamida ulanish;
- Host, Port, User, Password va Database parametrlari

mumkin.

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
""",
        "code": "# PostgreSQL ulanish namunasi\nimport psycopg2\n\n# conn = psycopg2.connect(dbname='app', user='postgres', password='123', host='localhost')\n# cur = conn.cursor()\n# cur.execute('SELECT version()')\nprint('PostgreSQL ulanish kodi tayyor!')",
        "code_exp": "- `1-5 qatorlar` — psycopg2 kutubxonasi orqali PostgreSQL bazasiga ulanish shabloni.",
        "quiz_q": "PostgreSQL bazasining standart port raqami qaysi?",
        "quiz_opts": ["3306", "5432", "8000", "27017"],
        "quiz_ans": 1,
        "quiz_exp": "PostgreSQL bazasi standart 5432-portda xizmat ko'rsatadi."
    },

    35: {
        "title": "35-dars — PostgreSQL CRUD va JOIN",
        "content": """# 📊 35. PostgreSQL CRUD va JOIN — Dars dokumentatsiyasi

`PostgreSQL CRUD va Aggregate funksiyalar` — **murakkab so'rovlar, GROUP BY, ORDER BY hamda COUNT/SUM agregatsiyalari** uchun ishlatiladi.

Bu mavzu orqali:

- `GROUP BY` va `HAVING` orqali guruhlash;
- `COUNT()`, `SUM()`, `AVG()`, `MAX()`, `MIN()` funksiyalari;
- `ORDER BY column ASC/DESC` bo'yicha saralash

mumkin.

---

# 1. Asosiy tushuncha

```sql
SELECT category, COUNT(*), AVG(price) 
FROM products 
GROUP BY category 
HAVING COUNT(*) > 5 
ORDER BY AVG(price) DESC;
```
""",
        "code": "import sqlite3\nconn = sqlite3.connect(':memory:')\ncur = conn.cursor()\ncur.execute('CREATE TABLE sales (dept TEXT, amount INT)')\ncur.execute(\"INSERT INTO sales VALUES ('IT', 1000), ('IT', 2000), ('HR', 1500)\")\ncur.execute('SELECT dept, SUM(amount) FROM sales GROUP BY dept')\nprint('Guruhlangan natija:', cur.fetchall())",
        "code_exp": "- `1-5 qatorlar` — Bo'limlar va ularning sotuv summalari kiritiladi;\n- `6-7 qatorlar` — GROUP BY va SUM() yordamida guruhlar bo'yicha umumiy summa hisoblanadi.",
        "quiz_q": "Ma'lumotlarni guruhlash uchun qaysi SQL buyrug'i ishlatiladi?",
        "quiz_opts": ["ORDER BY", "GROUP BY", "CLUSTER BY", "COLLECT BY"],
        "quiz_ans": 1,
        "quiz_exp": "GROUP BY buyrug'i bir xil qiymatga ega bo'lgan qatorlarni guruhlaydi."
    },

    36: {
        "title": "36-dars — 3-modul imtihoni",
        "content": """# 🎓 36. 3-modul imtihoni — Dars dokumentatsiyasi

`3-modul imtihoni` — 25-darsdan 35-darsgacha o'rganilgan **OOP Klasslar, Vorislik, Inkapsulyatsiya, SQL, SQLite va PostgreSQL ko'nikmalarini sinash** uchun o'tkaziladi.

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
""",
        "code": "def exam_solution_3():\n    print('3-Modul (OOP va Database) Imtihon topshirig\\'i bajarildi.')\n\nexam_solution_3()",
        "code_exp": "- `1-3 qatorlar` — 3-modul imtihon topshirig'i bajarilish funksiyasi.",
        "quiz_q": "3-modul imtihonida maksimal ball nechaga teng?",
        "quiz_opts": ["50 ball", "80 ball", "100 ball", "120 ball"],
        "quiz_ans": 2,
        "quiz_exp": "Imtihon 100 ballik shkala bo'yicha baholanadi."
    }
}

def update_25_to_36():
    print("==================================================================")
    print("🚀 25-DARSDAN 36-DARSGACHA BO'LGAN HUJJATLAR TO'G'RILANMOQDA...")
    print("==================================================================")

    all_lessons = list(Lesson.objects.all().order_by('lesson_number'))

    for num in range(25, 37):
        item_data = EXACT_25_TO_36_LESSONS[num]
        lesson_obj = next((l for l in all_lessons if l.lesson_number == num), None)

        code_examples = [
            {
                "id": f"code-{num}-1",
                "title": f"{item_data['title']} — Rasmiy Ishchi Kod",
                "language": "python",
                "code": item_data["code"],
                "explanation": item_data["code_exp"]
            }
        ]

        quiz_questions = [
            {
                "id": f"quiz-{num}-1",
                "question": item_data["quiz_q"],
                "options": item_data["quiz_opts"],
                "correctIndex": item_data["quiz_ans"],
                "explanation": item_data["quiz_exp"]
            }
        ]

        materials = [
            {
                "id": f"mat-{num}-pdf",
                "name": f"{num}_Dars_Konspekt.pdf",
                "type": "pdf",
                "size": "3.0 MB",
                "url": f"https://python-backend.uz/docs/{num}_dars.pdf"
            }
        ]

        student_results = [
            {"id": f"res-{num}-1", "studentName": "Ali Valiyev", "score": 98, "passed": True, "notes": "A'lo bajardi"},
            {"id": f"res-{num}-2", "studentName": "Sardor Karimov", "score": 90, "passed": True, "notes": "Topshiriq bajarildi"}
        ]

        if lesson_obj:
            lesson_obj.title = item_data["title"]
            lesson_obj.content = item_data["content"]
            lesson_obj.code_examples = code_examples
            lesson_obj.quiz_questions = quiz_questions
            lesson_obj.materials = materials
            lesson_obj.student_results = student_results
            lesson_obj.save()
            print(f"✅ [{num}-DARS: {item_data['title']}] -> Foydalanuvchi taqdim etgan shablonda TO'G'RILANDI.")

    with open(LESSONS_JSON, "r", encoding="utf-8") as f:
        json_data = json.load(f)

    for item in json_data:
        num = item.get("lessonNumber")
        if num in EXACT_25_TO_36_LESSONS:
            ex = EXACT_25_TO_36_LESSONS[num]
            item["title"] = ex["title"]
            item["content"] = ex["content"]
            item["codeExamples"] = [
                {
                    "id": f"code-{num}-1",
                    "title": f"{ex['title']} — Rasmiy Ishchi Kod",
                    "language": "python",
                    "code": ex["code"],
                    "explanation": ex["code_exp"]
                }
            ]
            item["quizQuestions"] = [
                {
                    "id": f"quiz-{num}-1",
                    "question": ex["quiz_q"],
                    "options": ex["quiz_opts"],
                    "correctIndex": ex["quiz_ans"],
                    "explanation": ex["quiz_exp"]
                }
            ]

    with open(LESSONS_JSON, "w", encoding="utf-8") as f:
        json.dump(json_data, f, ensure_ascii=False, indent=2)

    print("==================================================================")
    print("✨ 25-DARSDAN 36-DARSGACHA BO'LGAN DARSLAR SHABLON BO'YICHA TO'G'RILANDI!")
    print("==================================================================")

if __name__ == "__main__":
    update_25_to_36()
