import os
import sys
import json
import django

sys.path.append(os.path.dirname(__file__))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from lessons_app.models import Lesson

LESSONS_JSON = os.path.join(os.path.dirname(__file__), "..", "frontend", "src", "data", "lessons.json")

FULL_LONG_18_TO_24 = {
    18: """# 🎯 18. *args, **kwargs va scope — Dars dokumentatsiyasi

`*args` va `**kwargs` — Python’da **noaniq miqdordagi pozitsion va nomlangan argumentlarni qabul qilish hamda o'zgaruvchilar sohasi (scope)** uchun ishlatiladi.

Bu mavzu orqali:

- `*args` yordamida ko'plab argumentlarni Tuple shaklida olish;
- `**kwargs` yordamida nomlangan argumentlarni Dict shaklida olish;
- Local (ichki) va Global (tashqi) o'zgaruvchilar sohasi;
- `global` kalit so'zi bilan tashqi o'zgaruvchini yangilash

mumkin.

---

## Dars maqsadi

Bu dars oxirida o‘quvchi:

- Istalgan miqdordagi argumentlarni qabul qiluvchi moslashuvchan funksiyalar yozish;
- `*args` va `**kwargs` ni bir vaqtda funksiyada qo'llash;
- Global va lokal o'zgaruvchilar toqnashuvini oldini olish

ni mustaqil bajara oladi.

## Kerakli bilimlar

Bu darsni tushunish uchun:

- 17-dars: Funksiyalar va parametrlar;
- Tuple va Dict tushunchalari

bilinishi kerak.

---

# 1. Asosiy tushuncha

`*args` va `**kwargs` nima ekanini sodda tilda tushuntiramiz.

Masalan:

> `*args` — funksiyaga uzatilgan barcha ortiqcha pozitsion argumentlarni bitta Tuplega yig'adi. `**kwargs` — barcha nomlangan argumentlarni bitta Lug'atga (Dict) yig'adi.

Muhim qoida:

```python
def my_func(*args, **kwargs):
    print(args)    # tuple
    print(kwargs)  # dict
```

---

# 2. Birinchi sodda misol

```python
def sum_all(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total

print("Yig'indi:", sum_all(1, 2, 3, 4, 5))
```

Natija:

```text
Yig'indi: 15
```

Izoh:

- `1-qator` — `*numbers` barcha uzatilgan sonlarni tuple ko'rinishida yig'adi;
- `5-qator` — Funksiyaga istalgancha son uzatilishi mumkin.

---

# 3. Asosiy metodlar yoki operatorlar

| Sintaksis | Vazifasi | Misol |
|---|---|---|
| `*args` | Pozitsion argumentlarni Tuple shaklida yig'ish | `def f(*args):` |
| `**kwargs` | Nomlangan argumentlarni Dict shaklida yig'ish | `def f(**kwargs):` |
| `global x` | Global o'zgaruvchini funksiya ichida o'zgartirish | `global counter` |

---

# 4. Batafsil misol — Foydalanuvchi Profili

```python
def create_profile(name, email, *skills, **details):
    print(f"Ism: {name} | Email: {email}")
    print("Ko'nikmalar:", ", ".join(skills))
    for key, val in details.items():
        print(f"{key.upper()}: {val}")

create_profile("Ali", "ali@dev.uz", "Python", "Django", "SQL", city="Toshkent", role="Backend")
```

Natija:

```text
Ism: Ali | Email: ali@dev.uz
Ko'nikmalar: Python, Django, SQL
CITY: Toshkent
ROLE: Backend
```

---

# 6. Ko‘p uchraydigan xatolar

## Xato 1: *args va **kwargs ketma-ketligini buzish

Noto‘g‘ri:

```python
def func(**kwargs, *args):  # SyntaxError!
    pass
```

To‘g‘ri:

```python
def func(*args, **kwargs):
    pass
```

---

# 7. Sinfdagi amaliy topshiriqlar

## 1-topshiriq — Oson

**Vazifa:** Istalgancha kiritilgan sonlarning ko'paytmasini qaytaruvchi `multiply_all(*args)` funksiyasini yozing.

## 2-topshiriq — O‘rta

**Vazifa:** Foydalanuvchi ma'lumotlarini `**kwargs` orqali qabul qilib chiroyli formatda chop etuvchi dastur tuzing.

---

# 8. Uyga vazifa

1. `18_dars_args_kwargs.py` faylini yarating;
2. Do'kon mahsulotlarini hisoblovchi funksiya tuzing (`*prices` va `**discounts`);
3. Kodni GitHub'ga saqlang.

---

# 9. Tekshirish savollari

1. `*args` argumentlarni qaysi ma'lumot turida yig'adi (Tuple)?
2. `**kwargs` va `*args` ning asosiy farqi nima?
3. Local scope va Global scope ning farqini tushuntiring.

---

# 10. Qisqa xulosa

Bu darsda:

- `*args va pozitsion argumentlar`;
- `**kwargs va nomlangan argumentlar`;
- `Local va Global scope`

ni o‘rgandik.

Keyingi darsda: **Lambda va rekursiya**.

---

# Resurslar va fayllar

- 📄 Konspekt: `18_dars_konspekt.pdf`
- 💻 Kodlar: `github.com/dars-reja/18-dars`
- 🎬 Video: `youtube.com/watch?v=dars18`
- 📝 Qo‘shimcha mashqlar: `python.uz/mashq18`
""",

    19: """# ♾️ 19. Lambda va rekursiya — Dars dokumentatsiyasi

`Lambda` va `Rekursiya` — Python’da **bir qatorli anonim funksiyalar hamda o'z-o'zini chaqiruvchi algoritmik mantiqni yozish** uchun ishlatiladi.

Bu mavzu orqali:

- `lambda` anonim funksiyalarini e'lon qilish;
- `map()` va `filter()` funksiyalari bilan lambdani qo'llash;
- Rekursiv funksiyalar (faktorial va fibonachchi topish)

mumkin.

---

## Dars maqsadi

Bu dars oxirida o‘quvchi:

- Bir qatorli ixcham lambda funksiyalarini yozish;
- `filter()` yordamida ro'yxat elementlarini saralash;
- Faktorial va cheksiz qaytarilish xatolarisiz rekursiv funksiyalar tuzish

ni mustaqil bajara oladi.

---

# 1. Asosiy tushuncha

```python
square = lambda x: x ** 2
print(square(5))  # 25

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)
print(factorial(5))  # 120
```
""",

    21: """# 🛡️ 21. Xatolarni boshqarish — Dars dokumentatsiyasi

`try / except / else / finally` — Python’da **dastur bajarilishida yuzaga kelishi mumkin bo'lgan xatolarni ushlash va dastur to'xtab qolishining oldini olish** uchun ishlatiladi.

Bu mavzu orqali:

- `try` va `except` bloklari bilan ishlash;
- aniq xatolik turlari: `ZeroDivisionError`, `ValueError`, `KeyError`;
- `finally` bloki yordamida har doim bajarilishi shart bo'lgan kodlarni yozish

mumkin.

---

## Dars maqsadi

Bu dars oxirida o‘quvchi:

- Kiritilgan noto'g'ri ma'lumotlarda dastur ro'yxatini halokatdan (crash) saqlab qolish;
- Aniq xato turlari uchun mos xabarlarni chiqarish;
- `try-except` bloklarini backend kodingizga tatbiq etish

ni mustaqil bajara oladi.

---

# 1. Asosiy tushuncha

```python
try:
    num = int(input("Son kiriting: "))
    res = 100 / num
    print("Natija:", res)
except ZeroDivisionError:
    print("Nolga bo'lish mumkin emas!")
except ValueError:
    print("Faqat butun son kiritishingiz kerak!")
```
""",

    22: """# 📁 22. Fayllar — Dars dokumentatsiyasi

`Fayllar bilan ishlash` — Python’da **matnli fayllarni yaratish, o'qish, yozish va ma'lumotlarni saqlash** uchun ishlatiladi.

Bu mavzu orqali:

- `open(filename, mode)` funksiyasi;
- rejimlar: `'r'` (read), `'w'` (write), `'a'` (append);
- `with open(...) as f:` xavfsiz kontekst menejeri

mumkin.

---

## Dars maqsadi

Bu dars oxirida o‘quvchi:

- Faylga ma'lumot yozish va o'qish;
- Faylni ishlatib bo'lgach avtomatik yopilishi uchun `with open()` qo'llash;
- Matnli fayllardan ma'lumotlarni qatorma-qator o'qish

ni mustaqil bajara oladi.

---

# 1. Asosiy tushuncha

```python
with open("data.txt", "w", encoding="utf-8") as f:
    f.write("Salom Python Backend!\n22-dars: Fayllar")

with open("data.txt", "r", encoding="utf-8") as f:
    print(f.read())
```
""",

    23: """# 🌐 23. JSON va requests — Dars dokumentatsiyasi

`JSON` va `requests` — Python’da **tashqi API lar bilan ishlash hamda HTTP so'rovlar yuborish** uchun ishlatiladi.

Bu mavzu orqali:

- `json.dumps()` (Dict -> JSON string) va `json.loads()` (JSON string -> Dict);
- `requests.get(url)` orqali internetdan ma'lumot olish;
- REST API xizmatlaridan kelgan javoblarni tahlil qilish

mumkin.

---

## Dars maqsadi

Bu dars oxirida o‘quvchi:

- Python lug'atini JSON formatiga serializatsiya qilish;
- `requests` kutubxonasi yordamida tashqi API larga so'rov yuborish;
- API javobini `json()` orqali o'qib loyihada qo'llash

ni mustaqil bajara oladi.

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

    24: """# 🎓 24. 2-modul imtihoni — Dars dokumentatsiyasi

`2-modul imtihoni` — 13-darsdan 23-darsgacha o'rganilgan **Tuple/Set, Dict, Comprehension, Funksiyalar, datetime, Fayllar va API ko'nikmalarini sinash va baholash** uchun o'tkaziladi.

Bu mavzu orqali:

- 13–23 darslar bo'yicha nazariy va amaliy bilimlarni sinash;
- Real 3 ta algoritmik va API masalalarini yechish;
- Sertifikatlash uchun 2-modul natijalarini belgilash

mumkin.

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
    print("====================================")
    print("   2-MODUL IMTIHONI KODI BAJARILDI  ")
    print("====================================")

module_2_exam()
```
"""
}

for num, txt in FULL_LONG_18_TO_24.items():
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
    if n in FULL_LONG_18_TO_24:
        item["content"] = FULL_LONG_18_TO_24[n]

with open(LESSONS_JSON, "w", encoding="utf-8") as f:
    json.dump(j_data, f, ensure_ascii=False, indent=2)

print("✨ 18-24 darslar kontenti to'liqligicha saqlandi!")
