import os
import sys
import json
import django

sys.path.append(os.path.dirname(__file__))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from lessons_app.models import Lesson

LESSONS_JSON = os.path.join(os.path.dirname(__file__), "..", "frontend", "src", "data", "lessons.json")

EXPANDED_15_TO_24 = {
    15: """# 🌳 15. Murakkab ma’lumotlar — Dars dokumentatsiyasi

`Murakkab ma'lumotlar tuzilmalari` — Python’da **ichma-ich lug'at va ro'yxat shaklidagi murakkab backend va API ma'lumotlari bilan ishlash** uchun ishlatiladi.

Bu mavzu orqali:

- Ro'yxat ichida Lug'atlar saqlash (`[{...}, {...}]`);
- Lug'at ichida Ro'yxatlar saqlash (`{"skills": ["Py", "SQL"]}`);
- Real REST API va JSON ma'lumotlarini `for` sikllari orqali qayta ishlash;
- Ko'p darajali obyektlardan kerakli qiymatni ajratish

mumkin.

---

## Dars maqsadi

Bu dars oxirida o‘quvchi:

- Ichma-ich joylashgan ma'lumotlarga to'g'ri indeks va kalitlar bilan murojaat qilish;
- Murakkab ma'lumotlar to'plamini `for` sikllari yordamida filtrlash;
- Real loyihalar uchun JSON ma'lumotlar modelini tuzish

ni mustaqil bajara oladi.

## Kerakli bilimlar

Bu darsni tushunish uchun:

- 11-dars: List asoslari;
- 14-dars: Dictionary

bilinishi kerak.

---

# 1. Asosiy tushuncha

`Murakkab ma'lumotlar` nima ekanini sodda tilda tushuntiramiz.

Masalan:

> `Murakkab ma'lumotlar` — bu bir necha darajali to'plamlar majmuasi. Masalan, bir necha talabalar ro'yxati va har bir talabaning baholar ro'yxati.

Muhim qoida:

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

---

# 2. Birinchi sodda misol

```python
users = [
    {"id": 1, "name": "Ali", "skills": ["Python", "Django"]},
    {"id": 2, "name": "Sardor", "skills": ["SQL", "FastAPI"]}
]

for user in users:
    print(f"Dasturchi: {user['name']} | Ko'nikmalar: {', '.join(user['skills'])}")
```

Natija:

```text
Dasturchi: Ali | Ko'nikmalar: Python, Django
Dasturchi: Sardor | Ko'nikmalar: SQL, FastAPI
```

Izoh:

- `1-4 qatorlar` — Ro'yxat ichida lug'atlar va ularning ichida ko'nikmalar ro'yxati;
- `6-7 qatorlar` — Har bir foydalanuvchi ma'lumoti chop etiladi.

---

# 3. Asosiy metodlar yoki operatorlar

| Struktur a | Murojaat usuli | Misol |
|---|---|---|
| List ichidagi Dict | `list[idx]['key']` | `users[0]['name']` |
| Dict ichidagi List | `dict['key'][idx]` | `user['skills'][0]` |
| Dict ichidagi Dict | `dict['k1']['k2']` | `data['author']['name']` |

---

# 4. Batafsil misol — O'rtacha Bal Hisoblash

```python
students_data = [
    {"name": "Ali", "scores": [90, 85, 95]},
    {"name": "Vali", "scores": [70, 80, 75]}
]

for student in students_data:
    avg = sum(student["scores"]) / len(student["scores"])
    print(f"{student['name']} o'rtacha bali: {avg:.1f}")
```

Natija:

```text
Ali o'rtacha bali: 90.0
Vali o'rtacha bali: 75.0
```

---

# 6. Ko‘p uchraydigan xatolar

## Xato 1: Indeks va kalit ketma-ketligini adashtirish

Noto‘g‘ri:

```python
data = [{"name": "Ali"}]
print(data["name"][0])  # TypeError!
```

To‘g‘ri:

```python
data = [{"name": "Ali"}]
print(data[0]["name"])  # 'Ali'
```

---

# 7. Sinfdagi amaliy topshiriqlar

## 1-topshiriq — Oson

**Vazifa:** 3 ta mahsulot lug'atidan iborat ro'yxat yarating va barcha narxlarni chop eting.

## 2-topshiriq — O‘rta

**Vazifa:** Foydalanuvchilar ro'yxatidan faqat "Admin" rolidagi foydalanuvchilarni ajratib oling.

---

# 8. Uyga vazifa

1. `15_dars_complex_data.py` faylini yarating;
2. Maktab sinfidagi o'quvchilar va ularning fanlardan olgan baholarini saqlaydigan murakkab lug'at tuzing;
3. Kodni GitHub'ga saqlang.

---

# 9. Tekshirish savollari

1. `list[0]["key"]` va `dict["key"][0]` farqi nima?
2. JSON formati Python'da qaysi strukturaga o'xshaydi?
3. Murakkab strukturalarni aylanib chiqishda necha darajali `for` sikllari ishlatiladi?

---

# 10. Qisqa xulosa

Bu darsda:

- `List ichida Dict`;
- `Dict ichida List`;
- `Ko'p darajali ma'lumotlarni o'qish`

ni o‘rgandik.

Keyingi darsda: **Comprehension**.

---

# Resurslar va fayllar

- 📄 Konspekt: `15_dars_konspekt.pdf`
- 💻 Kodlar: `github.com/dars-reja/15-dars`
- 🎬 Video: `youtube.com/watch?v=dars15`
- 📝 Qo‘shimcha mashqlar: `python.uz/mashq15`
""",

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

---

# 1. Asosiy tushuncha

```python
# List comprehension bilan juft sonlar:
evens = [x for x in range(1, 11) if x % 2 == 0]
print(evens)  # [2, 4, 6, 8, 10]
```
""",

    17: """# ⚙️ 17. Funksiyalar — Dars dokumentatsiyasi

`Funksiya (Function)` — Python’da **ma'lum bir vazifani bajaruvchi va qayta ishlatiluvchi kod bloklarini yaratish** uchun ishlatiladi.

Bu mavzu orqali:

- `def` yordamida funksiyalar e'lon qilish;
- parametrlar va argumentlar berish;
- `return` orqali qiymat qaytarish;
- parametrga standart qiymatlar biriktirish

mumkin.

---

## Dars maqsadi

Bu dars oxirida o‘quvchi:

- Qayta ishlatiladigan universal funksiyalar yozish;
- `return` va `print()` o'rtasidagi farqni tushunish;
- Kalkulyator va biznes-mantiq funksiyalarini yaratish

ni mustaqil bajara oladi.

---

# 1. Asosiy tushuncha

```python
def greet(name, role="Talaba"):
    return f"Salom {name}, sizning rolingiz: {role}"

print(greet("Ali"))
```
""",

    18: """# 🎯 18. *args, **kwargs va scope — Dars dokumentatsiyasi

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

for num, txt in EXPANDED_15_TO_24.items():
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
    if n in EXPANDED_15_TO_24:
        item["content"] = EXPANDED_15_TO_24[n]

with open(LESSONS_JSON, "w", encoding="utf-8") as f:
    json.dump(j_data, f, ensure_ascii=False, indent=2)

print("✨ 13-24 darslar kontenti to'liqligicha saqlandi!")
