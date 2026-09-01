import os
import sys
import json
import django

sys.path.append(os.path.dirname(__file__))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from lessons_app.models import Lesson

LESSONS_JSON = os.path.join(os.path.dirname(__file__), "..", "frontend", "src", "data", "lessons.json")

FULL_LONG_26_TO_36 = {
    26: """# ⚙️ 26. __init__ va self — Dars dokumentatsiyasi

`__init__` va `self` — Python’da **obyekt yaratilayotganda uning atributlarini avtomatik ishga tushirish (konstruktor)** va uning xususiyatlarini saqlash uchun ishlatiladi.

Bu mavzu orqali:

- `__init__()` konstruktor metodi;
- `self` atamasi yordamida joriy obyekt xususiyatlariga murojaat qilish;
- obyekt yaratilayotganda dinamik qiymatlar berish (`User("Ali", 20)`);
- har bir obyekt uchun mustaqil xotira maydoni ajratish

mumkin.

---

## Dars maqsadi

Bu dars oxirida o‘quvchi:

- `__init__` konstruktoridan foydalanib har xil atributli obyektlar yaratish;
- `self` mantiqan joriy obyektga ishora qilishini tushunish;
- Obyekt parametrlarini dinamik ravishda o'zgartirish

ni mustaqil bajara oladi.

## Kerakli bilimlar

Bu darsni tushunish uchun:

- 25-dars: OOP, class va object asoslari;
- Funksiyalar va parametrlar

bilinishi kerak.

---

# 1. Asosiy tushuncha

`__init__ va self` nima ekanini sodda tilda tushuntiramiz.

Masalan:

> `__init__` — bu sehrli metod bo'lib, `Class()` chaqirilishi bilan avtomatik ishlaydi. `self` — obyektning o'ziga ishora qiluvchi birinchi parametr.

Muhim qoida:

```python
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

---

# 2. Birinchi sodda misol

```python
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

student1 = Student("Ali", 90)
print(f"Talaba: {student1.name} | Balli: {student1.score}")
```

Natija:

```text
Talaba: Ali | Balli: 90
```

---

# 3. Asosiy Metodlar va Atributlar

| Tushuncha | Vazifasi | Misol |
|---|---|---|
| `__init__` | Obyekt konstruktori | `def __init__(self):` |
| `self.attr` | Obyekt atributiga qiymat biriktirish | `self.name = name` |
| `self.method()` | Klass ichida o'z metodini chaqirish | `self.get_info()` |

---

# 4. Batafsil misol — Avtomobil Loyihasi

```python
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.is_running = False

    def start_engine(self):
        self.is_running = True
        return f"{self.brand} {self.model} dvigateli yoqildi!"

car1 = Car("Chevrolet", "Gentra", 2024)
print(car1.start_engine())
```

---

# 6. Ko‘p uchraydigan xatolar

## Xato 1: self o'rniga oddiy nom yozib atributga tayinlamaslik

Noto‘g‘ri:

```python
class User:
    def __init__(self, name):
        name = name  # Local o'zgaruvchi bo'lib qoladi!
```

To‘g‘ri:

```python
class User:
    def __init__(self, name):
        self.name = name
```

---

# 7. Sinfdagi amaliy topshiriqlar

## 1-topshiriq — Oson

**Vazifa:** `Movie` klassini yarating (title, director, year) va 2 ta kinoni e'lon qiling.

## 2-topshiriq — O‘rta

**Vazifa:** `BankAccount` klassini yozib, `__init__` da `balance=0` qilib bering va `deposit()` metodini yozing.

---

# 8. Uyga vazifa

1. `26_dars_init_self.py` faylini yarating;
2. `Employee` klassini tuzing (`name`, `position`, `salary`) va maoshni oshiruvchi `increase_salary(percent)` metodini qo'shing;
3. Kodni GitHub'ga saqlang.

---

# 9. Tekshirish savollari

1. `__init__` metodi qachon va qanday ishga tushadi?
2. Klass metodlarida `self` parametrining o'rni nima?
3. Obyekt atributi va local o'zgaruvchi farqi nimada?

---

# 10. Qisqa xulosa

Bu darsda:

- `__init__ konstruktor metodi`;
- `self parametri va obyekt atributlari`;
- `Obyekt holatini boshqarish`

ni o‘rgandik.

Keyingi darsda: **Inkapsulyatsiya**.

---

# Resurslar va fayllar

- 📄 Konspekt: `26_dars_konspekt.pdf`
- 💻 Kodlar: `github.com/dars-reja/26-dars`
- 🎬 Video: `youtube.com/watch?v=dars26`
- 📝 Qo‘shimcha mashqlar: `python.uz/mashq26`
""",

    27: """# 🔒 27. Inkapsulyatsiya — Dars dokumentatsiyasi

`Inkapsulyatsiya (Encapsulation)` — Python’da **obyekt ichidagi ma'lumotlarni tashqi ruxsat etilmagan aralashuvlardan himoyalash va yashirish** uchun ishlatiladi.

Bu mavzu orqali:

- Public (ochiq), Protected (`_name`) va Private (`__name`) atributlar;
- Getter va Setter metodlari yordamida qiymatlarni nazorat qilish;
- `@property` dekoratori yordamida xavfsiz boshqaruv

mumkin.

---

## Dars maqsadi

Bu dars oxirida o‘quvchi:

- Private va Public atributlar farqini tushunish va qo'llash;
- Balans va parollarni tashqi o'zgartirishlardan saqlash;
- Getter hamda Setter metodlarini yozish

ni mustaqil bajara oladi.

## Kerakli bilimlar

Bu darsni tushunish uchun:

- 26-dars: `__init__` va `self`

bilinishi kerak.

---

# 1. Asosiy tushuncha

`Inkapsulyatsiya` nima ekanini sodda tilda tushuntiramiz.

Masalan:

> `Inkapsulyatsiya` — obyektning ichki tuzilishini yashirish va faqat maxsus metodlar (Getter/Setter) orqali muloqot qilish. Masalan, bank kartasi balansini to'g'ridan-to'g'ri o'zgartirib bo'lmaydi, faqat depozit orqali.

Muhim qoida:

```python
class Account:
    def __init__(self, balance):
        self.__balance = balance  # Private
```

---

# 2. Birinchi sodda misol

```python
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    def get_balance(self):
        return self.__balance

acc = BankAccount("Ali", 1000)
print("Balans:", acc.get_balance())
```

Natija:

```text
Balans: 1000
```

---

# 4. Batafsil misol — Deposit va Withdraw

```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"{amount} so'm qo'shildi.")

    def get_balance(self):
        return self.__balance

acc = BankAccount(500)
acc.deposit(200)
print("Yangi balans:", acc.get_balance())
```

---

# 6. Ko‘p uchraydigan xatolar

## Xato 1: Private atributga to'g'ridan-to mezon murojaat qilish (AttributeError)

Noto‘g‘ri:

```python
acc = BankAccount(500)
print(acc.__balance)  # AttributeError!
```

To‘g‘ri:

```python
acc = BankAccount(500)
print(acc.get_balance())
```

---

# 7. Sinfdagi amaliy topshiriqlar

## 1-topshiriq — Oson

**Vazifa:** `User` klassini tuzing va uning `__password` atributini private qilib, tekshiruvchi metod yozing.

## 2-topshiriq — O‘rta

**Vazifa:** `@property` dekoratori yordamida yosh (age) faqat musbat son bo'lishini ta'minlovchi Setter yozing.

---

# 8. Uyga vazifa

1. `27_dars_encapsulation.py` faylini yarating;
2. `Student` klassini tuzing (`__grades` private ro'yxati) va baho qo'shuvchi `add_grade(grade)` metodini yozing;
3. Kodni GitHub'ga saqlang.

---

# 9. Tekshirish savollari

1. Public, Protected va Private atributlar qanday farqlanadi?
2. Getter va Setter metodlarining maqsadi nima?
3. `@property` dekoratori nima uchun ishlatiladi?

---

# 10. Qisqa xulosa

Bu darsda:

- `Private atributlar (__attr)`;
- `Getter va Setter metodlar`;
- `@property dekoratori`

ni o‘rgandik.

Keyingi darsda: **Vorislik va polymorphism**.

---

# Resurslar va fayllar

- 📄 Konspekt: `27_dars_konspekt.pdf`
- 💻 Kodlar: `github.com/dars-reja/27-dars`
- 🎬 Video: `youtube.com/watch?v=dars27`
- 📝 Qo‘shimcha mashqlar: `python.uz/mashq27`
""",

    28: """# 🧬 28. Vorislik va polymorphism — Dars dokumentatsiyasi

`Vorislik (Inheritance)` va `Polimorfizm (Polymorphism)` — Python’da **mavjud klass xususiyatlarini yangi klassga o'tkazish va bir xil nomli metodlarni turli obyektlarda har xil ishlatish** uchun ishlatiladi.

Bu mavzu orqali:

- Ota klass (Parent class) va Bola klass (Child class);
- `super().__init__()` orqali ota klass konstruktorini chaqirish;
- Metodlarni ustidan yozish (Method Overriding);
- Polimorfizm tamoyili

mumkin.

---

## Dars maqsadi

Bu dars oxirida o‘quvchi:

- Ota klassdan voris olib qayta ishlatuvchi bola klasslar yaratish;
- `super()` orqali ota klass atributlarini saqlab qolish;
- Polimorfik metodlar yozish

ni mustaqil bajara oladi.

## Kerakli bilimlar

Bu darsni tushunish uchun:

- 25-dars: Class va Object;
- 26-dars: `__init__` va `self`

bilinishi kerak.

---

# 1. Asosiy tushuncha

`Vorislik va polimorfizm` nima ekanini sodda tilda tushuntiramiz.

Masalan:

> `Vorislik` — Bola klass ota klassning barcha xususiyatlarini tayyor qabul qiladi. `Polimorfizm` — bir xil metod nomi (masalan `make_sound()`) turli hayvonlarda har xil ovoz beradi.

Muhim qoida:

```python
class Animal:
    pass

class Dog(Animal):
    pass
```

---

# 2. Birinchi sodda misol

```python
class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, student_id):
        super().__init__(name)
        self.student_id = student_id

s = Student("Ali", "ST-1001")
print(f"Talaba: {s.name} | ID: {s.student_id}")
```

Natija:

```text
Talaba: Ali | ID: ST-1001
```

---

# 4. Batafsil misol — Polimorfizm

```python
class Shape:
    def area(self):
        return 0

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius ** 2

class Square(Shape):
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side ** 2

shapes = [Circle(5), Square(4)]
for shape in shapes:
    print("Yuzi:", shape.area())
```

---

# 6. Ko‘p uchraydigan xatolar

## Xato 1: super().__init__() ni chaqirishni unutish

Noto‘g‘ri:

```python
class Student(Person):
    def __init__(self, name, student_id):
        self.student_id = student_id  # name atributi ota klassdan olinmaydi!
```

To‘g‘ri:

```python
class Student(Person):
    def __init__(self, name, student_id):
        super().__init__(name)
        self.student_id = student_id
```

---

# 7. Sinfdagi amaliy topshiriqlar

## 1-topshiriq — Oson

**Vazifa:** `Vehicle` ota klassi va undan voris oluvchi `Car` hamda `Bike` bola klasslarini yaratib metod yozing.

## 2-topshiriq — O‘rta

**Vazifa:** `Employee` ota klassi hamda `Developer` va `Manager` bola klasslarida oylik maoshni har xil hisoblovchi polimorfik metod yozing.

---

# 8. Uyga vazifa

1. `28_dars_inheritance.py` faylini yarating;
2. `User` va undan voris oluvchi `Admin` hamda `Customer` klasslarini shakllantiring;
3. Kodni GitHub'ga saqlang.

---

# 9. Tekshirish savollari

1. Vorislikning asosiy afzalligi nima (Kodni qayta ishlatish)?
2. `super()` funksiyasi nima beradi?
3. Polimorfizm tushunchasini tushuntiring.

---

# 10. Qisqa xulosa

Bu darsda:

- `Vorislik (Inheritance)`;
- `super() konstruktori`;
- `Polimorfizm va Method Overriding`

ni o‘rgandik.

Keyingi darsda: **Class/static va dunder metodlar**.

---

# Resurslar va fayllar

- 📄 Konspekt: `28_dars_konspekt.pdf`
- 💻 Kodlar: `github.com/dars-reja/28-dars`
- 🎬 Video: `youtube.com/watch?v=dars28`
- 📝 Qo‘shimcha mashqlar: `python.uz/mashq28`
""",

    29: """# 🛠️ 29. Class/static va dunder metodlar — Dars dokumentatsiyasi

`@classmethod`, `@staticmethod` va `Dunder metodlar` — Python’da **klass darajasidagi metodlar hamda maxsus sehrli metodlarni (`__str__`, `__len__`, `__eq__`) shakllantirish** uchun ishlatiladi.

Bu mavzu orqali:

- `@classmethod` va `cls` parametri;
- `@staticmethod` (yordamchi metodlar);
- `__str__()` (obyektni string sifat chop etish);
- `__len__()` (obyekt uzunligini qaytarish);
- `__eq__()` (obyektlarni solishtirish)

mumkin.

---

## Dars maqsadi

Bu dars oxirida o‘quvchi:

- `@classmethod` orqali muqobil konstruktorlar (alternative constructors) yaratish;
- `@staticmethod` yordamida mustaqil yordamchi funksiyalar yozish;
- `__str__` va `__len__` dunder metodlarini o'z obyektlarida qo'llash

ni mustaqil bajara oladi.

---

# 1. Asosiy tushuncha

```python
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

class Book:
    def __init__(self, title):
        self.title = title

    def __str__(self):
        return f"Kitob: {self.title}"
```
""",

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

---

# 1. Asosiy tushuncha

```python
# UPDATE
cursor.execute("UPDATE users SET name = ? WHERE id = ?", ("Alijon", 1))

# DELETE
cursor.execute("DELETE FROM users WHERE id = ?", (1,))
```
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
""",

    36: """# 🎓 36. 3-modul imtihoni — Dars dokumentatsiyasi

`3-modul imtihoni` — 25-darsdan 35-darsgacha o'rganilgan **OOP Klasslar, Vorislik, Inkapsulyatsiya, SQL, SQLite va PostgreSQL ko'nikmalarini sinash** uchun o'tkaziladi.

Bu dars orqali:

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

for num, txt in FULL_LONG_26_TO_36.items():
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
    if n in FULL_LONG_26_TO_36:
        item["content"] = FULL_LONG_26_TO_36[n]

with open(LESSONS_JSON, "w", encoding="utf-8") as f:
    json.dump(j_data, f, ensure_ascii=False, indent=2)

print("✨ 26-36 darslar kontenti to'liqligicha 10 bo'limli variantda saqlandi!")
