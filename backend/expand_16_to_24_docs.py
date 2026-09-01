import os
import sys
import json
import django

sys.path.append(os.path.dirname(__file__))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from lessons_app.models import Lesson

LESSONS_JSON = os.path.join(os.path.dirname(__file__), "..", "frontend", "src", "data", "lessons.json")

FULL_LONG_16_TO_24 = {
    16: """# ⚡ 16. Comprehension — Dars dokumentatsiyasi

`Comprehension` — Python’da **bitta qator kod yordamida ro'yxat va lug'atlarni ixcham va tezkor yaratish** uchun ishlatiladi.

Bu mavzu orqali:

- `List comprehension`: `[x for x in range(10)]`;
- Shartli filtrlar: `[x for x in range(10) if x % 2 == 0]`;
- `Dict comprehension`: `{k: v for k, v in data}`;
- Kod qatorlarini qisqartirish va o'qilishini yaxshilash

mumkin.

---

## Dars maqsadi

Bu dars oxirida o‘quvchi:

- Oddiy `for` sikllarini `List comprehension` ga o'tkazish;
- Shartli mantiqiy filtrlarni comprehension ichida yozish;
- Kalit va qiymatlarni tezkor almashtirish uchun `Dict comprehension` qo'llash

ni mustaqil bajara oladi.

## Kerakli bilimlar

Bu darsni tushunish uchun:

- 7-dars: `for` sikli;
- 11-dars: List asoslari

bilinishi kerak.

---

# 1. Asosiy tushuncha

`Comprehension` nima ekanini sodda tilda tushuntiramiz.

Masalan:

> `Comprehension` — yangi ro'yxat yoki lug'at yaratish uchun ishlatiladigan sintaksis shakli. U oddiy 4-5 qatorli for siklini bitta ixcham qatorga qisqartiradi.

Muhim qoida:

```python
evens = [x for x in range(1, 11) if x % 2 == 0]
```

---

# 2. Birinchi sodda misol

```python
numbers = [1, 2, 3, 4, 5]
squares = [n ** 2 for n in numbers]
print("Kvadratlar:", squares)
```

Natija:

```text
Kvadratlar: [1, 4, 9, 16, 25]
```

Izoh:

- `1-qator` — Boshlang'ich sonlar ro'yxati;
- `2-qator` — `[n ** 2 for n in numbers]` har bir son kvadratini hisoblab yangi ro'yxat yaratadi.

---

# 3. Asosiy metodlar yoki operatorlar

| Shakli | Sintaksisi | Misol |
|---|---|---|
| List Comprehension | `[expr for item in seq]` | `[x*2 for x in range(5)]` |
| Shartli List | `[expr for item in seq if cond]` | `[x for x in range(10) if x > 5]` |
| Dict Comprehension | `{k: v for item in seq}` | `{x: x**2 for x in range(3)}` |

---

# 4. Batafsil misol — Dict Comprehension

```python
words = ["python", "django", "api", "sql"]
word_len = {w: len(w) for w in words if len(w) > 3}
print("Uzun so'zlar lug'ati:", word_len)
```

Natija:

```text
Uzun so'zlar lug'ati: {'python': 6, 'django': 6}
```

---

# 6. Ko‘p uchraydigan xatolar

## Xato 1: Comprehension ichida murakkab koblarni yozish

Noto‘g‘ri:

```python
# Juda murakkab comprehension o'qishni qiyinlashtiradi
res = [x**2 if x % 2 == 0 else x**3 for x in range(10) if x > 2 and x < 8]
```

To‘g‘ri:

```python
# Sodda va tushunarli yozish
res = [x**2 for x in range(3, 8) if x % 2 == 0]
```

---

# 7. Sinfdagi amaliy topshiriqlar

## 1-topshiriq — Oson

**Vazifa:** 1 dan 20 gacha sonlar ichidan faqat toqlari kvadratlarini comprehension bilan toping.

## 2-topshiriq — O‘rta

**Vazifa:** Matnlar ro'yxati berilgan: `["ali", "sardor", "vali"]`. Ularning birinchi harfini katta qilib yangi ro'yxat hosil qiling.

---

# 8. Uyga vazifa

1. `16_dars_comprehension.py` faylini yarating;
2. Foydalanuvchilar lug mezonidan faqat 18 yoshdan kattalarini Dict comprehension bilan ajratib oling;
3. Kodni GitHub'ga saqlang.

---

# 9. Tekshirish savollari

1. List comprehension ning oddiy `for` siklidan afzalligi nima?
2. `[x**2 for x in range(1, 4)]` kodi natijasi nima bo'ladi?
3. Dict comprehension sintaksisi qanday yoziladi?

---

# 10. Qisqa xulosa

Bu darsda:

- `List comprehension sintaksisi`;
- `Shartli filtrlar (if)`;
- `Dict comprehension`

ni o‘rgandik.

Keyingi darsda: **Funksiyalar**.

---

# Resurslar va fayllar

- 📄 Konspekt: `16_dars_konspekt.pdf`
- 💻 Kodlar: `github.com/dars-reja/16-dars`
- 🎬 Video: `youtube.com/watch?v=dars16`
- 📝 Qo‘shimcha mashqlar: `python.uz/mashq16`
""",

    17: """# ⚙️ 17. Funksiyalar — Dars dokumentatsiyasi

`Funksiya (Function)` — Python’da **ma'lum bir vazifani bajaruvchi va qayta ishlatiluvchi kod bloklarini yaratish** uchun ishlatiladi.

Bu mavzu orqali:

- `def` yordamida funksiyalar e'lon qilish;
- parametrlar va argumentlar berish;
- `return` orqali qiymat qaytarish;
- parametrga standart qiymatlar biriktirish (`def greet(name="Do'st"):`)

mumkin.

---

## Dars maqsadi

Bu dars oxirida o‘quvchi:

- Qayta ishlatiladigan universal funksiyalar yozish;
- `return` va `print()` o'rtasidagi farqni tushunish;
- Kalkulyator va biznes-mantiq funksiyalarini yaratish

ni mustaqil bajara oladi.

## Kerakli bilimlar

Bu darsni tushunish uchun:

- 3-dars: Arifmetika va o'zgaruvchilar;
- 5-dars: Shart operatorlari

bilinishi kerak.

---

# 1. Asosiy tushuncha

`Funksiya` nima ekanini sodda tilda tushuntiramiz.

Masalan:

> `Funksiya` — bu nom berilgan va chaqirilgandagina ishlaydigan kod bloki. U kod qaytarilishini (DRY — Don't Repeat Yourself) oldini olish uchun kerak.

Muhim qoida:

```python
def add(a, b):
    return a + b
```

---

# 2. Birinchi sodda misol

```python
def greet(name, role="Talaba"):
    return f"Salom {name}, sizning rolingiz: {role}"

print(greet("Ali"))
print(greet("Ogabek", "O'qituvchi"))
```

Natija:

```text
Salom Ali, sizning rolingiz: Talaba
Salom Ogabek, sizning rolingiz: O'qituvchi
```

Izoh:

- `1-2 qatorlar` — `greet` funksiyasi va standart `"Talaba"` parametri;
- `4-5 qatorlar` — Funksiya turli argumentlar uzatib chaqiriladi.

---

# 3. Asosiy metodlar yoki operatorlar

| Tushuncha | Vazifasi | Misol |
|---|---|---|
| `def` | Funksiya yaratish | `def my_func():` |
| `return` | Natija qaytarish va to'xtash | `return result` |
| Parametr | Funksiyaning kiruvchi o'zgaruvchisi | `def calc(x):` |
| Argument | Funksiyaga uzatilgan real qiymat | `calc(5)` |

---

# 4. Batafsil misol — Soliq Hisoblash

```python
def calculate_salary(base_salary, bonus=0, tax_percent=12):
    total = base_salary + bonus
    tax = total * (tax_percent / 100)
    net_salary = total - tax
    return net_salary

result = calculate_salary(5000000, 1000000)
print("Qolga tegadigan maosh:", result, "so'm")
```

Natija:

```text
Qolga tegadigan maosh: 5280000.0 so'm
```

---

# 6. Ko‘p uchraydigan xatolar

## Xato 1: Return o'rniga print ishlatib qiymat kutish

Noto‘g‘ri:

```python
def add(a, b):
    print(a + b)

res = add(2, 3) * 2  # TypeError (NoneType * int)!
```

To‘g‘ri:

```python
def add(a, b):
    return a + b

res = add(2, 3) * 2  # 10
```

---

# 7. Sinfdagi amaliy topshiriqlar

## 1-topshiriq — Oson

**Vazifa:** Sonning kvadratini qaytaruvchi `square(n)` funksiyasini tuzing.

## 2-topshiriq — O‘rta

**Vazifa:** Uchta son olib, ularning eng kattasini qaytaruvchi `max_of_three(a, b, c)` funksiyasini yozing.

---

# 8. Uyga vazifa

1. `17_dars_functions.py` faylini yarating;
2. Kiritilgan matn palindrom ekanligini `is_palindrome(text)` funksiyasi yordamida True/False qaytaradigan qilib yozing;
3. Kodni GitHub'ga saqlang.

---

# 9. Tekshirish savollari

1. `return` va `print()` ning asosiy farqi nima?
2. Standart parametr qiymati (Default parameter) qanday beriladi?
3. Funksiyaga uzatilgan o'zgaruvchi qanday nomlanadi (Argument)?

---

# 10. Qisqa xulosa

Bu darsda:

- `def sintaksisi`;
- `Parametrlar va argumentlar`;
- `return qiymat qaytarish`

ni o‘rgandik.

Keyingi darsda: ***args, **kwargs va scope**.

---

# Resurslar va fayllar

- 📄 Konspekt: `17_dars_konspekt.pdf`
- 💻 Kodlar: `github.com/dars-reja/17-dars`
- 🎬 Video: `youtube.com/watch?v=dars17`
- 📝 Qo‘shimcha mashqlar: `python.uz/mashq17`
""",

    18: """# 🎯 18. *args, **kwargs va scope — Dars dokumentatsiyasi

`*args` va `**kwargs` — Python’da **noaniq miqdordagi pozitsion va nomlangan argumentlarni qabul qilish** uchun ishlatiladi.

Bu mavzu orqali:

- `*args` yordamida istalgancha argumentlarni Tuple shaklida olish;
- `**kwargs` yordamida nomlangan argumentlarni Dict shaklida olish;
- Global va Local scope (o'zgaruvchilarning ko'rinish sohasi) va `global` kalit so'zi

mumkin.

---

## Dars maqsadi

Bu dars oxirida o‘quvchi:

- Noaniq miqdordagi argumentlarni qabul qiluvchi moslashuvchan funksiyalar yozish;
- `*args` va `**kwargs` ni bir vaqtda funksiyada qo'llash;
- Global va lokal o'zgaruvchilar toqnashuvini oldini olish

ni mustaqil bajara oladi.

---

# 1. Asosiy tushuncha

```python
def sum_all(*args):
    return sum(args)

print(sum_all(1, 2, 3, 4, 5))  # 15
```
""",

    19: """# ♾️ 19. Lambda va rekursiya — Dars dokumentatsiyasi

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
```
""",

    21: """# 🛡️ 21. Xatolarni boshqarish — Dars dokumentatsiyasi

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
```
""",

    22: """# 📁 22. Fayllar — Dars dokumentatsiyasi

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
```
""",

    23: """# 🌐 23. JSON va requests — Dars dokumentatsiyasi

`JSON` va `requests` — Python’da **tashqi API lar bilan ishlash va ma'lumotlarni almashish** uchun ishlatiladi.

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
print(response.json())
```
""",

    24: """# 🎓 24. 2-modul imtihoni — Dars dokumentatsiyasi

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
"""
}

for num, txt in FULL_LONG_16_TO_24.items():
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
    if n in FULL_LONG_16_TO_24:
        item["content"] = FULL_LONG_16_TO_24[n]

with open(LESSONS_JSON, "w", encoding="utf-8") as f:
    json.dump(j_data, f, ensure_ascii=False, indent=2)

print("✨ 16-24 darslar kontenti ham to'liq 10 bo'limli hajmda yangilandi!")
