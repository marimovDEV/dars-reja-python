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

EXACT_13_TO_24_LESSONS = {
    13: {
        "title": "13-dars — Tuple va set",
        "content": """# 🧊 13. Tuple va set — Dars dokumentatsiyasi

`Tuple` va `Set` — Python’da **o'zgarmas ma'lumotlar to'plami hamda unikal (takrorlanmas) elementlarni saqlash** uchun ishlatiladi.

Bu mavzu orqali:

- `Tuple` (o'zgarmas ro'yxat) yaratish va uning xavfsizligidan foydalanish;
- `Set` yordamida ro'yxatdagi takrorlangan elementlarni avtomatik o'chirish;
- `.add()`, `.remove()`, `.union()`, `.intersection()` kabi to'plam metodlarini qo'llash

mumkin.

---

## Dars maqsadi

Bu dars oxirida o‘quvchi:

- Tuple va List orasidagi farqni tushunish va o'zgarmas ma'lumotlarni saqlash;
- Set yordamida takrorlangan ma'lumotlarni bir qatorda tozalash;
- To'plamlar ustida kesishma (intersection) va birlashma (union) amallarini bajarish

ni mustaqil bajara oladi.

## Kerakli bilimlar

Bu darsni tushunish uchun:

- 11-dars: List asoslari;
- Indekslar bilan ishlash

bilinishi kerak.

---

# 1. Asosiy tushuncha

`Tuple` va `Set` nima ekanini sodda tilda tushuntiramiz.

Masalan:

> `Tuple` — o'zgartirib bo'lmaydigan (immutable) elementlar ketma-ketligi, qavs `()` bilan yoziladi. `Set` — takrorlanmas elementlar to'plami, figurali qavs `{}` bilan yoziladi.

Muhim qoida:

```python
point = (41.2995, 69.2401)  # Tuple
numbers = {1, 2, 2, 3, 3}   # Set -> {1, 2, 3}
```

---

# 2. Birinchi sodda misol

```python
# Tuple
colors = ("qizil", "yashil", "ko'k")
print("Birinchi rang:", colors[0])

# Set
unique_numbers = {10, 20, 20, 30, 10}
print("Unikal sonlar:", unique_numbers)
```

Natija:

```text
Birinchi rang: qizil
Unikal sonlar: {10, 20, 30}
```

Izoh:

- `2-qator` — `colors` tuple bo'lgani uchun elementini o'zgartirib bo'lmaydi;
- `6-qator` — Set takrorlangan `10` va `20` larni avtomatik o'chirib tashlaydi.

---

# 3. Asosiy metodlar yoki operatorlar

| Kod / metod | Vazifasi | Misol |
|---|---|---|
| `set.add(x)` | Setga yangi element qo'shish | `s.add(5)` |
| `set.remove(x)` | Elementni o'chirish | `s.remove(2)` |
| `a.union(b)` | Ikki to'plamni birlashtirish | `a | b` |
| `a.intersection(b)` | Ikki to'plam kesishmasi | `a & b` |
| `tuple.count(x)` | Element sonini hisoblash | `t.count(1)` |

---

# 4. Batafsil misol — Unikal Foydalanuvchilar

```python
raw_users = ["ali", "valisher", "ali", "sardor", "valisher"]
unique_users = set(raw_users)
unique_users.add("jasur")

print("Dastlabki soni:", len(raw_users))
print("Tozalangan unikal nomlar:", unique_users)
```

Natija:

```text
Dastlabki soni: 5
Tozalangan unikal nomlar: {'ali', 'valisher', 'sardor', 'jasur'}
```

---

# 6. Ko‘p uchraydigan xatolar

## Xato 1: Tuple elementini o'zgartirishga urinish (TypeError)

Noto‘g‘ri:

```python
t = (1, 2, 3)
t[0] = 10  # TypeError!
```

To‘g‘ri:

```python
t = (1, 2, 3)
print(t[0])
```

---

# 7. Sinfdagi amaliy topshiriqlar

## 1-topshiriq — Oson

**Vazifa:** Haftaning 7 kuni nomidan iborat Tuple yarating va 3-kunni ekranga chiqaring.

## 2-topshiriq — O‘rta

**Vazifa:** Ikkita ro'yxat berilgan: `a = [1, 2, 3, 4]` va `b = [3, 4, 5, 6]`. Ularning umumiy elementlarini `set.intersection()` yordamida toping.

---

# 8. Uyga vazifa

1. `13_dars_tuple_set.py` faylini yarating;
2. Foydalanuvchi kiritgan matndagi unikal harflar sonini `set()` yordamida topuvchi dastur yozing;
3. Kodni GitHub'ga saqlang.

---

# 9. Tekshirish savollari

1. Tuple va List ning asosiy farqi nima?
2. Set ichida takroriy elementlar saqlanadimi?
3. Set elementlariga indeks orqali (`set[0]`) murojaat qilsa bo'ladimi (Yo'q)?
4. Bu kodning natijasi qanday bo‘ladi?

```python
s = {1, 2, 3}
s.add(2)
print(len(s))
```

5. O'zgarmas ma'lumotlarni saqlashda Tuple ning afzalligi nimada?

---

# 10. Qisqa xulosa

Bu darsda:

- `Tuple va uning immutable xususiyati`;
- `Set to'plami va unikal elementlar`;
- `Set metodlari (.add, .union, .intersection)`

ni o‘rgandik.

Keyingi darsda: **Dictionary**.

---

# Resurslar va fayllar

- 📄 Konspekt: `13_dars_konspekt.pdf`
- 💻 Kodlar: `github.com/dars-reja/13-dars`
- 🎬 Video: `youtube.com/watch?v=dars13`
- 📝 Qo‘shimcha mashqlar: `python.uz/mashq13`
""",
        "code": "unique_users = {'ali', 'sardor', 'ali'}\nunique_users.add('valijon')\nprint('Foydalanuvchilar:', unique_users)",
        "code_exp": "- `1-qator` — 'ali' takrorlangan, Set avtomatik bittasini qoldiradi;\n- `2-qator` — add() yangi element qo'shadi.",
        "quiz_q": "Qaysi ma'lumot tuzilmasi elementlari o'zgarmas (immutable) hisoblanadi?",
        "quiz_opts": ["List", "Tuple", "Set", "Dictionary"],
        "quiz_ans": 1,
        "quiz_exp": "Tuple yaratilgandan so'ng uning elementlarini o'zgartirib bo'lmaydi."
    },

    14: {
        "title": "14-dars — Dictionary",
        "content": """# 📖 14. Dictionary — Dars dokumentatsiyasi

`Dictionary (Lug'at)` — Python’da **kalit va qiymat (key: value) juftligi ko'rinishida ma'lumot saqlash** uchun ishlatiladi.

Bu mavzu orqali:

- lug'at yaratish va kalitlar orqali qiymatlarni o'qish;
- `.get()` metodi yordamida xatolarsiz ma'lumot olish;
- `.keys()`, `.values()`, `.items()` metodlari orqali lug'atni aylanib chiqish;
- yangi kalit qo'shish va qiymatni yangilash

mumkin.

---

## Dars maqsadi

Bu dars oxirida o‘quvchi:

- Kalit-qiymat ko'rinishidagi ma'lumotlarni saqlash;
- `.get()` metodi yordamida kalit topilmaganda default qiymat qaytarish;
- `for key, val in dict.items():` orqali lug'at elementlarini o'qish

ni mustaqil bajara oladi.

## Kerakli bilimlar

Bu darsni tushunish uchun:

- 11-dars: List asoslari;
- Kalit tushunchasi (String va Integer)

bilinishi kerak.

---

# 1. Asosiy tushuncha

`Dictionary` nima ekanini sodda tilda tushuntiramiz.

Masalan:

> `Dictionary` — obyekt xususiyatlarini saqlash uchun ishlatiladigan lug'at bo'lib, har bir element `key: value` ko'rinishida bo'ladi va `{}` qavsga olinadi.

Muhim qoida:

```python
user = {
    "name": "Ali",
    "age": 20
}
print(user["name"])
```

---

# 2. Birinchi sodda misol

```python
car = {
    "brand": "Chevrolet",
    "model": "Gentra",
    "year": 2024
}

print("Moshina brendi:", car["brand"])
print("Yili:", car.get("year"))
```

Natija:

```text
Moshina brendi: Chevrolet
Yili: 2024
```

Izoh:

- `1-5 qatorlar` — `car` lug'ati e'lon qilindi;
- `7-8 qatorlar` — `[]` va `.get()` yordamida qiymatlar olindi.

---

# 3. Asosiy metodlar yoki operatorlar

| Metod | Vazifasi | Misol |
|---|---|---|
| `.get(key, default)` | Kalit orqali qiymat olish (xatosiz) | `d.get("age", 0)` |
| `.keys()` | Barcha kalitlar ro'yxati | `d.keys()` |
| `.values()` | Barcha qiymatlar ro'yxati | `d.values()` |
| `.items()` | Kalit va qiymat juftliklari | `for k, v in d.items():` |
| `.pop(key)` | Kalit bo'yicha o'chirish | `d.pop("age")` |

---

# 4. Batafsil misol — Mahsulot Ombori

```python
product = {
    "name": "Laptop HP",
    "price": 1200,
    "stock": 15
}

product["price"] = 1100  # Narxni yangilash
product["color"] = "Black"  # Yangi kalit qo'shish

for key, val in product.items():
    print(f"{key.upper()}: {val}")
```

Natija:

```text
NAME: Laptop HP
PRICE: 1100
STOCK: 15
COLOR: Black
```

---

# 6. Ko‘p uchraydigan xatolar

## Xato 1: Mavjud bo'lmagan kalitga murojaat qilish (KeyError)

Noto‘g‘ri:

```python
user = {"name": "Ali"}
print(user["age"])  # KeyError!
```

To‘g‘ri:

```python
user = {"name": "Ali"}
print(user.get("age", "Noma'lum"))  # 'Noma'lum' qaytadi
```

---

# 7. Sinfdagi amaliy topshiriqlar

## 1-topshiriq — Oson

**Vazifa:** Telefon haqida lug'at yarating (nomi, xotirasi, narxi) va ularni chop eting.

## 2-topshiriq — O‘rta

**Vazifa:** Lug'atdagi barcha sonli qiymatlarning yig'indisini hisoblang.

---

# 8. Uyga vazifa

1. `14_dars_dictionary.py` faylini yarating;
2. Talabalar va ularning ballaridan iborat lug'at tuzib, eng yuqori ball olgan talabani toping;
3. Kodni GitHub'ga saqlang.

---

# 9. Tekshirish savollari

1. `dict["key"]` va `dict.get("key")` ning farqi nima?
2. `.items()` metodi nima qaytaradi?
3. Lug'atga yangi qiymat qanday qo'shiladi?

---

# 10. Qisqa xulosa

Bu darsda:

- `Dictionary strukturasi va key-value`;
- `.get(), .keys(), .values(), .items() metodlari`;
- `KeyError dan qochish`

ni o‘rgandik.

Keyingi darsda: **Murakkab ma’lumotlar**.

---

# Resurslar va fayllar

- 📄 Konspekt: `14_dars_konspekt.pdf`
- 💻 Kodlar: `github.com/dars-reja/14-dars`
- 🎬 Video: `youtube.com/watch?v=dars14`
- 📝 Qo‘shimcha mashqlar: `python.uz/mashq14`
""",
        "code": "product = {'name': 'Laptop', 'price': 1200, 'stock': 15}\nproduct['price'] = 1100\nfor k, v in product.items():\n    print(f'{k}: {v}')",
        "code_exp": "- `1-qator` — Lug'at e'lon qilindi;\n- `2-qator` — 'price' qiymati yangilandi;\n- `3-4 qatorlar` — items() orqali barcha kalit va qiymatlar bosib chiqariladi.",
        "quiz_q": "Mavjud bo'lmagan kalit murojaat qilinganda xato bermaydigan metod qaysi?",
        "quiz_opts": ["dict[key]", "dict.get(key)", "dict.pop(key)", "dict.find(key)"],
        "quiz_ans": 1,
        "quiz_exp": "dict.get(key) kalit topilmasa None qaytaradi va xato bermaydi."
    },

    15: {
        "title": "15-dars — Murakkab ma’lumotlar",
        "content": """# 🌳 15. Murakkab ma’lumotlar — Dars dokumentatsiyasi

`Murakkab ma'lumotlar tuzilmalari` — Python’da **ichma-ich lug'at va ro'yxat shaklidagi ma'lumotlar bilan ishlash** uchun ishlatiladi.

Bu mavzu orqali:

- Ro'yxat ichida Lug'atlar saqlash (`[{...}, {...}]`);
- Lug'at ichida Ro'yxatlar saqlash (`{"skills": ["Py", "SQL"]}`);
- Real REST API va JSON ma'lumotlarini qayta ishlash

mumkin.

---

## Dars maqsadi

Bu dars oxirida o‘quvchi:

- Ichma-ich joylashgan ma'lumotlarga to'g'ri indeks va kalitlar bilan murojaat qilish;
- Murakkab ma'lumotlar to'plamini `for` sikllari yordamida filtrlash;
- Real loyihalar uchun JSON sifat ma'lumotlar modelini tuzish

ni mustaqil bajara oladi.

---

# 1. Asosiy tushuncha

```python
data = {
    "course": "Python Backend",
    "students": [
        {"name": "Ali", "score": 90},
        {"name": "Vali", "score": 85}
    ]
}

print(data["students"][0]["name"])  # 'Ali'
```
""",
        "code": "data = {\n  'course': 'Python Backend',\n  'modules': ['Basics', 'OOP', 'SQL', 'Django'],\n  'author': {'name': 'Ogabek', 'exp': 5}\n}\nprint('Muallif:', data['author']['name'])\nprint('1-modul:', data['modules'][0])",
        "code_exp": "- `1-5 qatorlar` — Ichma-ich ro'yxat va lug'atlardan iborat murakkab obyekt;\n- `6-7 qatorlar` — Indeks va kalitlar bo'yicha murojaat.",
        "quiz_q": "Dict ichidagi ro'yxatning birinchi elementini olish uchun qanday murojaat qilinadi?",
        "quiz_opts": ["dict['key'][0]", "dict['key'][1]", "dict[0]['key']", "dict.get(0)"],
        "quiz_ans": 0,
        "quiz_exp": "Avval dict['key'] orqali ro'yxat olinadi, so'ng [0] orqali birinchi element."
    },

    16: {
        "title": "16-dars — Comprehension",
        "content": """# ⚡ 16. Comprehension — Dars dokumentatsiyasi

`Comprehension` — Python’da **bitta qator kod yordamida ro'yxat va lug'atlarni ixcham yaratish** uchun ishlatiladi.

Bu mavzu orqali:

- `List comprehension`: `[x for x in range(10)]`;
- Shartli filtrlar: `[x for x in range(10) if x % 2 == 0]`;
- `Dict comprehension`: `{k: v for k, v in data}`

mumkin.

---

# 1. Asosiy tushuncha

```python
# List comprehension bilan juft sonlar:
evens = [x for x in range(1, 11) if x % 2 == 0]
print(evens)  # [2, 4, 6, 8, 10]
```
""",
        "code": "words = ['python', 'django', 'api', 'sql']\nlengths = {w: len(w) for w in words if len(w) > 3}\nprint('Uzun so\\'zlar:', lengths)",
        "code_exp": "- `1-qator` — So'zlar ro'yxati;\n- `2-qator` — Dict comprehension yordamida uzunligi 3 dan katta bo'lgan so'z va ularning uzunligi lug'atga yig'iladi.",
        "quiz_q": "[x**2 for x in range(1, 4)] kodi natijasi nima bo'ladi?",
        "quiz_opts": ["[1, 4, 9]", "[1, 2, 3]", "[2, 4, 6]", "[1, 8, 27]"],
        "quiz_ans": 0,
        "quiz_exp": "range(1, 4) sonlari (1, 2, 3) kvadratga oshiriladi: 1^2=1, 2^2=4, 3^2=9."
    },

    17: {
        "title": "17-dars — Funksiyalar",
        "content": """# ⚙️ 17. Funksiyalar — Dars dokumentatsiyasi

`Funksiya (Function)` — Python’da **ma'lum bir vazifani bajaruvchi va qayta ishlatiluvchi kod bloklarini yaratish** uchun ishlatiladi.

Bu mavzu orqali:

- `def` yordamida funksiyalar e'lon qilish;
- parametrlar va argumentlar berish;
- `return` orqali qiymat qaytarish

mumkin.

---

# 1. Asosiy tushuncha

```python
def greet(name):
    return f"Salom, {name}!"

msg = greet("Ali")
print(msg)
```
""",
        "code": "def greet(name, role='Talaba'):\n    return f'Salom {name}, sizning rolingiz: {role}'\n\nprint(greet('Ali'))\nprint(greet('Ogabek', 'O\\'qituvchi'))",
        "code_exp": "- `1-2 qatorlar` — greet funksiyasi va standart 'Talaba' parametri;\n- `4-5 qatorlar` — Funksiyani turli argumentlar bilan chaqirish.",
        "quiz_q": "Funksiyadan natija qaytaruvchi kalit so'z qaysi?",
        "quiz_opts": ["yield", "return", "output", "send"],
        "quiz_ans": 1,
        "quiz_exp": "return funksiya bajarilishini to'xtatadi va qiymatni qaytaradi."
    },

    18: {
        "title": "18-dars — *args, **kwargs va scope",
        "content": """# 🎯 18. *args, **kwargs va scope — Dars dokumentatsiyasi

`*args` va `**kwargs` — Python’da **noaniq miqdordagi pozitsion va nomlangan argumentlarni qabul qilish** uchun ishlatiladi.

Bu mavzu orqali:

- `*args` yordamida ko'plab argumentlarni Tuple shaklida olish;
- `**kwargs` yordamida nomlangan argumentlarni Dict shaklida olish;
- Global va Local scope (o'zgaruvchilarning ko'rinish sohasi)

mumkin.

---

# 1. Asosiy tushuncha

```python
def sum_all(*args):
    return sum(args)

print(sum_all(1, 2, 3, 4, 5))  # 15
```
""",
        "code": "def user_info(*args, **kwargs):\n    print('Pozitsion:', args)\n    print('Nomlangan:', kwargs)\n\nuser_info('Ali', 20, role='Admin', status='Active')",
        "code_exp": "- `1-3 qatorlar` — *args tuple variantida, **kwargs dict variantida olinadi;\n- `5-qator` — Turli parametrlar uzatiladi.",
        "quiz_q": "Noaniq miqdordagi nomlangan argumentlarni qabul qiluvchi sintaksis qaysi?",
        "quiz_opts": ["*args", "**kwargs", "&kwargs", "params"],
        "quiz_ans": 1,
        "quiz_exp": "**kwargs nomlangan argumentlarni lug'at (dict) shaklida qabul qiladi."
    },

    19: {
        "title": "19-dars — Lambda va rekursiya",
        "content": """# ♾️ 19. Lambda va rekursiya — Dars dokumentatsiyasi

`Lambda` va `Rekursiya` — Python’da **bir qatorli anonim funksiyalar va o'z-o'zini chaqiruvchi algoritmlarni yozish** uchun ishlatiladi.

Bu mavzu orqali:

- `lambda x, y: x + y` anonim funksiyalari;
- `map()` va `filter()` bilan lambda qo'llash;
- Rekursiv funksiyalar (faktorial va fibonachchi topish)

mumkin.

---

# 1. Asosiy tushuncha

```python
square = lambda x: x ** 2
print(square(5))  # 25

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)
```
""",
        "code": "square = lambda x: x ** 2\nnums = [1, 2, 3, 4]\nsquares = list(map(lambda x: x**2, nums))\nprint('Kvadratlar:', squares)",
        "code_exp": "- `1-qator` — Lambda bir qatorli funksiyasi;\n- `3-qator` — map() yordamida ro'yxatning har bir elementiga lambda qo'llaniladi.",
        "quiz_q": "Bir qatorli anonim funksiya yaratish kalit so'zi qaysi?",
        "quiz_opts": ["def", "lambda", "inline", "func"],
        "quiz_ans": 1,
        "quiz_exp": "lambda kalit so'zi anonim bir qatorli funksiyalarni e'lon qilishda ishlatiladi."
    },

    20: {
        "title": "20-dars — Modullar va kutubxonalar (datetime)",
        "content": """# 📅 20. Python datetime — Dars dokumentatsiyasi

`datetime` — Python'da **sana va vaqt bilan ishlash** uchun ishlatiladigan rasmiy modul.

Bu dars orqali:

- bugungi sanani va hozirgi vaqtni olish;
- yil, oy, kun, soat, minutlarni ajratish;
- `strftime()` orqali sanani matnga o'tkazish;
- `strptime()` orqali matnni sanaga o'tkazish;
- `timedelta` yordamida sanaga kun va vaqt qo'shish/ayirish

mumkin.

---

## Dars maqsadi

Bu dars oxirida o‘quvchi:

- Foydalanuvchi kiritgan tug'ilgan sanadan yoshini va kunlarini hisoblash;
- Loyihalar uchun deadline muddatlarini aniqlash;
- Sanalarni to'g'ri formatlab ko'rsatish

ni mustaqil bajara oladi.

---

# 1. Asosiy tushuncha

```python
from datetime import datetime, date, timedelta

now = datetime.now()
print("Hozirgi vaqt:", now)
```

Natija:

```text
Hozirgi vaqt: 2026-09-01 12:55:00.123456
```

---

# 3. Formatlash koda jadvallari (strftime)

| Kod | Ma'nosi | Misol |
|---|---|---|
| `%Y` | 4 xonali yil | `2026` |
| `%m` | 2 xonali oy | `09` |
| `%d` | 2 xonali kun | `01` |
| `%H` | 24 soatlik soat | `14` |
| `%M` | Minut | `30` |
| `%S` | Sekund | `45` |

---

# 4. strftime vs strptime

### `strptime()`: String -> Datetime
```python
dt = datetime.strptime("2026-08-22", "%Y-%m-%d")
```

### `strftime()`: Datetime -> String
```python
text = dt.strftime("%d.%m.%Y")  # '22.08.2026'
```

---

# 5. Timedelta bilan ishlash

```python
today = date.today()
next_week = today + timedelta(days=7)
print("7 kundan keyin:", next_week)
```

---

# 9. Tekshirish savollari

1. `strptime()` va `strftime()` farqi nima?
2. `%Y` va `%y` farqi nima?
3. Sanaga 10 kun qo'shish uchun qaysi klass ishlatiladi?

---

# 10. Qisqa xulosa

Bu darsda:

- `datetime va date sinflari`;
- `strftime va strptime metodlari`;
- `timedelta bilan kun qo'shish`

ni o‘rgandik.

Keyingi darsda: **Xatolarni boshqarish**.

---

# Resurslar va fayllar

- 📄 Konspekt: `20_dars_konspekt.pdf`
- 💻 Kodlar: `github.com/dars-reja/20-dars`
- 🎬 Video: `youtube.com/watch?v=dars20`
- 📝 Qo‘shimcha mashqlar: `python.uz/mashq20`
""",
        "code": "from datetime import datetime, timedelta\n\nnow = datetime.now()\nprint('Bugun:', now.strftime('%d.%m.%Y'))\nfuture = now + timedelta(days=10)\nprint('10 kundan keyin:', future.strftime('%d.%m.%Y'))",
        "code_exp": "- `1-qator` — datetime va timedelta import qilinadi;\n- `3-qator` — now.strftime('%d.%m.%Y') sanani matnga o'tkazadi;\n- `4-qator` — timedelta(days=10) orqali 10 kun qo'shiladi.",
        "quiz_q": "Stringni datetime obyektiga aylantiruvchi metod qaysi?",
        "quiz_opts": ["strftime()", "strptime()", "todatetime()", "parse()"],
        "quiz_ans": 1,
        "quiz_exp": "strptime() stringni datetime obyektiga o'tkazadi (string -> datetime)."
    },

    21: {
        "title": "21-dars — Xatolarni boshqarish",
        "content": """# 🛡️ 21. Xatolarni boshqarish — Dars dokumentatsiyasi

`try / except / else / finally` — Python’da **dastur bajarilishida yuzaga kelishi mumkin bo'lgan xatolarni ushlash va to'xtab qolishining oldini olish** uchun ishlatiladi.

Bu mavzu orqali:

- `try` va `except` bloklari;
- aniq xatolik turlari: `ZeroDivisionError`, `ValueError`, `KeyError`;
- `finally` bloki (har doim bajariladigan qism)

mumkin.

---

# 1. Asosiy tushuncha

```python
try:
    num = int(input("Son kiriting: "))
    print(100 / num)
except ZeroDivisionError:
    print("Nolga bo'lib bo'lmaydi!")
except ValueError:
    print("Faqat son kiritishingiz kerak!")
```
""",
        "code": "try:\n    num = int(input('Son kiriting: '))\n    res = 100 / num\n    print('Natija:', res)\nexcept ZeroDivisionError:\n    print('Xatolik: Nolga bo\\'lish mumkin emas!')\nexcept ValueError:\n    print('Xatolik: Faqat butun son kiriting!')",
        "code_exp": "- `1-4 qatorlar` — try bloki ichida xato kelib chiqishi mumkin bo'lgan kod bajariladi;\n- `5-8 qatorlar` — except mos xatolik turini ushlab xabarni ko'rsatadi.",
        "quiz_q": "Python'da xatolarni ushlash bloki qaysi?",
        "quiz_opts": ["catch", "except", "error", "handle"],
        "quiz_ans": 1,
        "quiz_exp": "Python'da try-except strukturasi ishlatiladi, except xatoni ushlaydi."
    },

    22: {
        "title": "22-dars — Fayllar",
        "content": """# 📁 22. Fayllar — Dars dokumentatsiyasi

`Fayllar bilan ishlash` — Python’da **matnli fayllarni yaratish, o'qish, yozish va ma'lumotlarni saqlash** uchun ishlatiladi.

Bu mavzu orqali:

- `open(filename, mode)` funksiyasi;
- rejimlar: `'r'` (read), `'w'` (write), `'a'` (append);
- `with open(...) as f:` xavfsiz konteyneri

mumkin.

---

# 1. Asosiy tushuncha

```python
with open("notes.txt", "w", encoding="utf-8") as f:
    f.write("Salom Python Backend!")

with open("notes.txt", "r", encoding="utf-8") as f:
    print(f.read())
```
""",
        "code": "with open('data.txt', 'w', encoding='utf-8') as f:\n    f.write('Python Backend Kursi\\n22-dars: Fayllar')\n\nwith open('data.txt', 'r', encoding='utf-8') as f:\n    content = f.read()\n    print('Fayl mazmuni:\\n', content)",
        "code_exp": "- `1-2 qatorlar` — with open('...', 'w') faylga matn yozadi;\n- `4-6 qatorlar` — with open('...', 'r') fayldan matnni o'qiydi.",
        "quiz_q": "Faylni avtomatik yopishni ta'minlaydigan konstruktsiya qaysi?",
        "quiz_opts": ["using", "with open()", "file.close()", "try-file"],
        "quiz_ans": 1,
        "quiz_exp": "with open(...) kontekst menejeri faylni foydalanib bo'lingach avtomatik yopadi."
    },

    23: {
        "title": "23-dars — JSON va requests",
        "content": """# 🌐 23. JSON va requests — Dars dokumentatsiyasi

`JSON` va `requests` — Python’da **tashqi API bolar bilan ishlash va ma'lumotlarni almashish** uchun ishlatiladi.

Bu mavzu orqali:

- `json.dumps()` (Dict -> String) va `json.loads()` (String -> Dict);
- `requests.get(url)` orqali internetdan HTTP so'rovlar yuborish;
- API dan qaytgan JSON ma'lumotni o'qish

mumkin.

---

# 1. Asosiy tushuncha

```python
import json
import requests

response = requests.get("https://api.github.com")
data = response.json()
print("GitHub API javobi:", data.get("current_user_url"))
```
""",
        "code": "import json\ndata = {'name': 'Ali', 'age': 20}\njson_str = json.dumps(data)\nprint('JSON string:', json_str)\nparsed = json.loads(json_str)\nprint('Python dict:', parsed['name'])",
        "code_exp": "- `1-3 qatorlar` — json.dumps() dictni JSON stringga o'tkazadi;\n- `5-6 qatorlar` — json.loads() JSON stringni qayta Python dictiga o'tkazadi.",
        "quiz_q": "Python lug'atini JSON matniga aylantiruvchi metod qaysi?",
        "quiz_opts": ["json.loads()", "json.dumps()", "json.parse()", "json.stringify()"],
        "quiz_ans": 1,
        "quiz_exp": "json.dumps() Python ob'ektini JSON matn formatiga serializatsiya qiladi."
    },

    24: {
        "title": "24-dars — 2-modul imtihoni",
        "content": """# 🎓 24. 2-modul imtihoni — Dars dokumentatsiyasi

`2-modul imtihoni` — 13-darsdan 23-darsgacha o'rganilgan **Tuple/Set, Dict, Comprehension, Funksiyalar, datetime, Fayllar va API ko'nikmalarini sinash** uchun o'tkaziladi.

---

## Imtihon Tartibi (100 ballik shkala)

- **Nazariy Testlar (20 ball)**: 13-23 darslar bo'yicha 10 ta test;
- **Amaliy Masalalar (50 ball)**: 3 ta murakkab algoritmik va API topshiriq;
- **PEP8 Standart va Kod Sifati (20 ball)**: Izohlar va to'g'ri nomlash;
- **Vaqt va Intizom (10 ball)**: 2 soat ichida topshirish.

---

# 1. Imtihon Kod Shabloni

```python
def module_2_exam():
    print("=== 2-MODUL IMTIHONI KODI BAJARILDI ===")

module_2_exam()
```
""",
        "code": "def exam_solution_2():\n    print('2-Modul Imtihon topshirig\\'i bajarildi.')\n\nexam_solution_2()",
        "code_exp": "- `1-3 qatorlar` — 2-modul imtihon topshirig'i bajarilish funksiyasi.",
        "quiz_q": "2-modul imtihonida maksimal ball nechaga teng?",
        "quiz_opts": ["50 ball", "80 ball", "100 ball", "120 ball"],
        "quiz_ans": 2,
        "quiz_exp": "Imtihon 100 ballik shkala bo'yicha baholanadi."
    }
}

def update_13_to_24():
    print("==================================================================")
    print("🚀 13-DARSDAN 24-DARSGACHA BO'LGAN HUJJATLAR TO'G'RILANMOQDA...")
    print("==================================================================")

    all_lessons = list(Lesson.objects.all().order_by('lesson_number'))

    for num in range(13, 25):
        item_data = EXACT_13_TO_24_LESSONS[num]
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
        if num in EXACT_13_TO_24_LESSONS:
            ex = EXACT_13_TO_24_LESSONS[num]
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
    print("✨ 13-DARSDAN 24-DARSGACHA BO'LGAN DARSLAR SHABLON BO'YICHA TO'G'RILANDI!")
    print("==================================================================")

if __name__ == "__main__":
    update_13_to_24()
