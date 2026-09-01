import os
import sys
import json
import django

sys.path.append(os.path.dirname(__file__))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from lessons_app.models import Lesson

LESSONS_JSON = os.path.join(os.path.dirname(__file__), "..", "frontend", "src", "data", "lessons.json")

FULL_LONG_19_TO_24 = {
    19: """# ♾️ 19. Lambda va rekursiya — Dars dokumentatsiyasi

`Lambda` va `Rekursiya` — Python’da **bir qatorli anonim funksiyalar va o'z-o'zini chaqiruvchi algoritmlarni yozish** uchun ishlatiladi.

Bu mavzu orqali:

- `lambda` anonim funksiyalarini e'lon qilish;
- `map()` va `filter()` funksiyalari bilan lambdani qo'llash;
- Rekursiv funksiyalar (faktorial va fibonachchi topish);
- Bazaviy holat (base case) bilan cheksiz rekursiyadan qochish

mumkin.

---

## Dars maqsadi

Bu dars oxirida o‘quvchi:

- Bir qatorli ixcham lambda funksiyalarini yozish;
- `filter()` yordamida ro'yxat elementlarini saralash;
- Faktorial va cheksiz qaytarilish xatolarisiz rekursiv funksiyalar tuzish

ni mustaqil bajara oladi.

## Kerakli bilimlar

Bu darsni tushunish uchun:

- 17-dars: Funksiyalar va `return`;
- 16-dars: Comprehension

bilinishi kerak.

---

# 1. Asosiy tushuncha

`Lambda` va `Rekursiya` nima ekanini sodda tilda tushuntiramiz.

Masalan:

> `Lambda` — nom berilmagan va bitta ifodadan iborat tezkor funksiya. `Rekursiya` — funksiyaning o'z-o'zini chaqirishi bo'lib, muammoni kichikroq bo'laklarga bo'lish uchun ishlatiladi.

Muhim qoida:

```python
square = lambda x: x ** 2
```

---

# 2. Birinchi sodda misol

```python
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x ** 2, numbers))
print("Kvadratlar:", squares)
```

Natija:

```text
Kvadratlar: [1, 4, 9, 16, 25]
```

---

# 4. Batafsil misol — Rekursiya bilan Faktorial

```python
def factorial(n):
    if n == 1 or n == 0:
        return 1
    return n * factorial(n - 1)

print("5! =", factorial(5))
```

Natija:

```text
5! = 120
```

---

# 6. Ko‘p uchraydigan xatolar

## Xato 1: Rekursiyada to'xtash shartini (Base case) esdan chiqarish

Noto‘g‘ri:

```python
def count_down(n):
    print(n)
    count_down(n - 1)  # RecursionError!
```

To‘g‘ri:

```python
def count_down(n):
    if n <= 0:
        return
    print(n)
    count_down(n - 1)
```

---

# 7. Sinfdagi amaliy topshiriqlar

## 1-topshiriq — Oson

**Vazifa:** Ikki sonning yig'indisini qaytaruvchi `add = lambda a, b: a + b` yozing.

## 2-topshiriq — O‘rta

**Vazifa:** `filter()` va lambda yordamida ro'yxatdan faqat juft sonlarni ajratib oling.

---

# 8. Uyga vazifa

1. `19_dars_lambda_recursion.py` faylini yarating;
2. Fibonachchi ketma-ketligining n-elementini topuvchi rekursiv funksiya yozing;
3. Kodni GitHub'ga saqlang.

---

# 9. Tekshirish savollari

1. Lambda funksiyaning oddiy funksiyadan farqi nima?
2. Rekursiyada `Base case` (to'xtash sharti) nega shart?
3. `map()` funksiyasi nima vazifa bajaradi?

---

# 10. Qisqa xulosa

Bu darsda:

- `lambda anonim funksiyasi`;
- `map va filter funksiyalari`;
- `Rekursiya va base case`

ni o‘rgandik.

Keyingi darsda: **Modullar va kutubxonalar (datetime)**.

---

# Resurslar va fayllar

- 📄 Konspekt: `19_dars_konspekt.pdf`
- 💻 Kodlar: `github.com/dars-reja/19-dars`
- 🎬 Video: `youtube.com/watch?v=dars19`
- 📝 Qo‘shimcha mashqlar: `python.uz/mashq19`
""",

    21: """# 🛡️ 21. Xatolarni boshqarish — Dars dokumentatsiyasi

`try / except / else / finally` — Python’da **dastur bajarilishida yuzaga kelishi mumkin bo'lgan xatolarni ushlash va dastur to'xtab qolishining oldini olish** uchun ishlatiladi.

Bu mavzu orqali:

- `try` va `except` bloklari bilan ishlash;
- aniq xatolik turlari: `ZeroDivisionError`, `ValueError`, `KeyError`;
- `finally` bloki yordamida har doim bajarilishi shart bo'lgan kodlarni yozish;
- custom xatoliklar ko'tarish (`raise Exception`)

mumkin.

---

## Dars maqsadi

Bu dars oxirida o‘quvchi:

- Kiritilgan noto'g'ri ma'lumotlarda dastur ro'yxatini halokatdan (crash) saqlab qolish;
- Aniq xato turlari uchun mos xabarlarni chiqarish;
- `try-except` bloklarini backend kodingizga tatbiq etish

ni mustaqil bajara oladi.

## Kerakli bilimlar

Bu darsni tushunish uchun:

- 3-dars: Input va arifmetika;
- 17-dars: Funksiyalar

bilinishi kerak.

---

# 1. Asosiy tushuncha

`Xatolarni boshqarish` nima ekanini sodda tilda tushuntiramiz.

Masalan:

> `try-except` — kodda kutilmagan xatolik yuz berganda (masalan sonni 0 ga bo'lish yoki noto'g'ri tur kiritilganda) dasturni to'xtatib qo'ymay xatoni muloyim ushlab qoladi.

Muhim qoida:

```python
try:
    res = 10 / 0
except ZeroDivisionError:
    print("Bo'lishda xatolik!")
```

---

# 2. Birinchi sodda misol

```python
try:
    age = int(input("Yoshingizni kiriting: "))
    print("Keyingi yil yoshingiz:", age + 1)
except ValueError:
    print("Xato: Faqat butun son kiriting!")
```

Natija:

```text
Yoshingizni kiriting: yigirma
Xato: Faqat butun son kiriting!
```

---

# 3. Asosiy Xatolik Turlari

| Xatolik Nomi | Qachon Kelib Chiqadi | Misol |
|---|---|---|
| `ValueError` | Noto'g'ri qiymat/tur | `int("salom")` |
| `ZeroDivisionError` | Nolga bo'lish | `10 / 0` |
| `KeyError` | Lug'atda kalit topilmasa | `dict["no_key"]` |
| `IndexError` | Ro'yxat indeksidan chiqilsa | `list[100]` |
| `TypeError` | Noto'g'ri toifadagi amal | `"a" + 5` |

---

# 4. Batafsil misol — try/except/else/finally

```python
try:
    file = open("data.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("Fayl topilmadi!")
else:
    print("Fayl muvaffaqiyatli o'qildi.")
finally:
    print("Tizim tekshiruvi yakunlandi.")
```

---

# 6. Ko‘p uchraydigan xatolar

## Xato 1: Barcha xatolarni umumiy Exception bilan berish

Noto‘g‘ri:

```python
try:
    # murakkab kod
except:
    print("Xato bo'ldi") # Qaysi xato ekanligi bilmay qolasiz!
```

To‘g‘ri:

```python
try:
    # kod
except ValueError:
    print("Qiymat xatosi")
except ZeroDivisionError:
    print("Nolga bo'lish xatosi")
```

---

# 7. Sinfdagi amaliy topshiriqlar

## 1-topshiriq — Oson

**Vazifa:** `try-except` yordamida ikkita sonni bo'luvchi dastur tuzing (Nolga bo'lish xatosini ushlang).

## 2-topshiriq — O‘rta

**Vazifa:** Foydalanuvchidan narx va miqdorni olib jami summani hisoblang, harflar kiritilsa xabardor qiling.

---

# 8. Uyga vazifa

1. `21_dars_exception_handling.py` faylini yarating;
2. Lug'atdan kalit oluvchi funksiya tuzing va `KeyError` ni ushlang;
3. Kodni GitHub'ga saqlang.

---

# 9. Tekshirish savollari

1. `finally` bloki qachon ishlaydi (Har doim)?
2. `else` bloki try/except da nima vazifa bajaradi?
3. Custom xatolar qay darajada foydali?

---

# 10. Qisqa xulosa

Bu darsda:

- `try va except bloklari`;
- `ValueError, ZeroDivisionError ushlash`;
- `finally va else`

ni o‘rgandik.

Keyingi darsda: **Fayllar**.

---

# Resurslar va fayllar

- 📄 Konspekt: `21_dars_konspekt.pdf`
- 💻 Kodlar: `github.com/dars-reja/21-dars`
- 🎬 Video: `youtube.com/watch?v=dars21`
- 📝 Qo‘shimcha mashqlar: `python.uz/mashq21`
""",

    22: """# 📁 22. Fayllar — Dars dokumentatsiyasi

`Fayllar bilan ishlash` — Python’da **matnli fayllarni yaratish, o'qish, yozish va ma'lumotlarni doimiy saqlash** uchun ishlatiladi.

Bu mavzu orqali:

- `open(filename, mode)` funksiyasi;
- rejimlar: `'r'` (read), `'w'` (write), `'a'` (append);
- `with open(...) as f:` xavfsiz kontekst menejeri;
- `.read()`, `.readline()`, `.readlines()` metodlari

mumkin.

---

## Dars maqsadi

Bu dars oxirida o‘quvchi:

- Faylga ma'lumot yozish va ularni o'qib olish;
- Faylni ishlatib bo'lgach avtomatik yopilishi uchun `with open()` qo'llash;
- Matnli fayllardan ma'lumotlarni qatorma-qator qayta ishlash

ni mustaqil bajara oladi.

## Kerakli bilimlar

Bu darsni tushunish uchun:

- Stringlar va matn formatlash;
- 21-dars: Xatolarni boshqarish (`FileNotFoundError`)

bilinishi kerak.

---

# 1. Asosiy tushuncha

`Fayllar bilan ishlash` nima ekanini sodda tilda tushuntiramiz.

Masalan:

> `with open()` — faylni ochadi va u bilan ishlash imkonini beradi. Operatsiyalar tugagach, fayl avtomatik tarzda yopiladi (close).

Muhim qoida:

```python
with open("notes.txt", "w", encoding="utf-8") as f:
    f.write("Salom Python!")
```

---

# 2. Birinchi sodda misol

```python
# Yozish
with open("data.txt", "w", encoding="utf-8") as f:
    f.write("Python Backend Kursi\n22-dars: Fayllar")

# O'qish
with open("data.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print("Fayl mazmuni:\n", content)
```

Natija:

```text
Fayl mazmuni:
 Python Backend Kursi
22-dars: Fayllar
```

---

# 3. Asosiy Rejimlar Jadvali

| Rejim | Nomi | Izoh |
|---|---|---|
| `'r'` | Read | Faylni o'qish uchun ochadi (Fayl bo'lishi shart) |
| `'w'` | Write | Faylga yozadi (Eski ma'lumotni o'chirib tashlaydi) |
| `'a'` | Append | Fayl oxiriga yangi ma'lumot qo'shadi |
| `'x'` | Create | Yangi fayl yaratadi (Mavjud bo'lsa xato beradi) |

---

# 4. Batafsil misol — Qo'shish Rejimi ('a')

```python
new_log = "2026-09-01: Yangi foydalanuvchi kirdi\n"

with open("logs.txt", "a", encoding="utf-8") as f:
    f.write(new_log)

print("Log muvaffaqiyatli saqlandi!")
```

---

# 6. Ko‘p uchraydigan xatolar

## Xato 1: Faylni open() bilan ochib close() qilishni unutish

Noto‘g‘ri:

```python
f = open("data.txt", "w")
f.write("test")
# f.close() yo'q -> Fayl ochiq qolib ketadi!
```

To‘g‘ri:

```python
with open("data.txt", "w") as f:
    f.write("test")
```

---

# 7. Sinfdagi amaliy topshiriqlar

## 1-topshiriq — Oson

**Vazifa:** `users.txt` faylini yaratib, unga 3 ta do'stingiz ismini yozing.

## 2-topshiriq — O‘rta

**Vazifa:** `users.txt` faylini o'qib, barcha ismlarni katta harflarga o'tkazib konsolga chiqaring.

---

# 8. Uyga vazifa

1. `22_dars_files.py` faylini yarating;
2. Kundalik daftar dasturini tuzing: Foydalanuvchi kiritgan eslatmalarni `diary.txt` ga `a` rejimi bilan yozing;
3. Kodni GitHub'ga saqlang.

---

# 9. Tekshirish savollari

1. `'w'` va `'a'` rejimlarining asosiy farqi nima?
2. `with open()` kontekst menejerining afzalligi nimada?
3. `.read()` va `.readline()` farqi nimada?

---

# 10. Qisqa xulosa

Bu darsda:

- `open() va rejimlar (r, w, a)`;
- `with open() xavfsiz sintaksisi`;
- `fayllarni o'qish va yozish`

ni o‘rgandik.

Keyingi darsda: **JSON va requests**.

---

# Resurslar va fayllar

- 📄 Konspekt: `22_dars_konspekt.pdf`
- 💻 Kodlar: `github.com/dars-reja/22-dars`
- 🎬 Video: `youtube.com/watch?v=dars22`
- 📝 Qo‘shimcha mashqlar: `python.uz/mashq22`
""",

    23: """# 🌐 23. JSON va requests — Dars dokumentatsiyasi

`JSON` va `requests` — Python’da **tashqi API lar bilan ishlash va ma'lumotlarni internet orqali uzatish/qabul qilish** uchun ishlatiladi.

Bu mavzu orqali:

- `json.dumps()` (Dict -> JSON string) va `json.loads()` (JSON string -> Dict);
- `requests.get(url)` orqali internetdan HTTP so'rovlar yuborish;
- REST API xizmatlaridan kelgan javoblarni tahlil qilish

mumkin.

---

## Dars maqsadi

Bu dars oxirida o‘quvchi:

- Python lug'atini JSON formatiga serializatsiya qilish;
- `requests` kutubxonasi yordamida tashqi API larga so'rov yuborish;
- API javobini `.json()` orqali o'qib loyihada qo'llash

ni mustaqil bajara oladi.

## Kerakli bilimlar

Bu darsni tushunish uchun:

- 14-dars: Dictionary;
- 22-dars: Fayllar

bilinishi kerak.

---

# 1. Asosiy tushuncha

`JSON` va `requests` nima ekanini sodda tilda tushuntiramiz.

Masalan:

> `JSON` — dasturlar o'rtasida ma'lumot almashish uchun eng ommabop matnli format. `requests` — Python'dan turli web-saytlar va API-larga HTTP so'rov yuborish kutubxonasi.

Muhim qoida:

```python
import json
import requests
```

---

# 2. Birinchi sodda misol

```python
import json

data = {"name": "Ali", "age": 20, "is_student": True}
json_string = json.dumps(data)

print("JSON matni:", json_string)
print("Turi:", type(json_string))
```

Natija:

```text
JSON matni: {"name": "Ali", "age": 20, "is_student": true}
Turi: <class 'str'>
```

---

# 3. Asosiy Metodlar Jadvali

| Metod | Vazifasi | Misol |
|---|---|---|
| `json.dumps(obj)` | Python dict -> JSON string | `json.dumps(d)` |
| `json.loads(str)` | JSON string -> Python dict | `json.loads(s)` |
| `requests.get(url)` | HTTP GET so'rovi yuborish | `requests.get(url)` |
| `response.json()` | API javobini Dict ga o'tkazish | `res.json()` |

---

# 4. Batafsil misol — Tashqi API ga so'rov

```python
import requests

url = "https://api.github.com/users/octocat"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print("Foydalanuvchi:", data["name"])
    print("Public Repo:", data["public_repos"])
```

Natija:

```text
Foydalanuvchi: The Octocat
Public Repo: 8
```

---

# 6. Ko‘p uchraydigan xatolar

## Xato 1: JSON string va Dict ni adashtirish

Noto‘g‘ri:

```python
s = '{"name": "Ali"}'
print(s["name"])  # TypeError (string indeksida xato)!
```

To‘g‘ri:

```python
import json
s = '{"name": "Ali"}'
d = json.loads(s)
print(d["name"])  # 'Ali'
```

---

# 7. Sinfdagi amaliy topshiriqlar

## 1-topshiriq — Oson

**Vazifa:** O'zingiz haqingizdagi lug'atni `json.dumps()` bilan JSON formatiga o'tkazib chop eting.

## 2-topshiriq — O‘rta

**Vazifa:** `requests.get("https://jsonplaceholder.typicode.com/todos/1")` API rasmiy manzilidan ma'lumot olib sarlavhasini ko'rsating.

---

# 8. Uyga vazifa

1. `23_dars_json_requests.py` faylini yarating;
2. Valyuta kursi API manzilidan bugungi AQSh dollari kursini oluvchi va so'mga o'giruvchi dastur tuzing;
3. Kodni GitHub'ga saqlang.

---

# 9. Tekshirish savollari

1. `json.dumps()` va `json.loads()` farqi nima?
2. `requests.get()` yuborilganda `200` status kodi nimani anglatadi?
3. API lar bilan ishlashda JSON ning o'rni nima?

---

# 10. Qisqa xulosa

Bu darsda:

- `JSON formatlash (dumps, loads)`;
- `requests kutubxonasi va HTTP GET`;
- `REST API ma'lumotlarini o'qish`

ni o‘rgandik.

Keyingi darsda: **2-modul imtihoni**.

---

# Resurslar va fayllar

- 📄 Konspekt: `23_dars_konspekt.pdf`
- 💻 Kodlar: `github.com/dars-reja/23-dars`
- 🎬 Video: `youtube.com/watch?v=dars23`
- 📝 Qo‘shimcha mashqlar: `python.uz/mashq23`
""",

    24: """# 🎓 24. 2-modul imtihoni — Dars dokumentatsiyasi

`2-modul imtihoni` — 13-darsdan 23-darsgacha o'rganilgan **Tuple/Set, Dict, Comprehension, Funksiyalar, datetime, Fayllar va API ko'nikmalarini sinash va sertifikatlash** uchun o'tkaziladi.

Bu dars orqali:

- 13–23 darslar bo'yicha nazariy va amaliy bilimlarni sinash;
- Real 3 ta algoritmik va API masalalarini yechish;
- Sertifikatlash uchun 2-modul natijalarini belgilash

mumkin.

---

## Imtihon Tartibi (100 ballik shkala)

- **Nazariy Testlar (20 ball)**: 13-23 darslar bo'yicha 10 ta test;
- **Amaliy Masalalar (50 ball)**: 3 ta murakkab algoritmik va API topshiriq;
- **PEP8 Standart va Kod Sifati (20 ball)**: Izohlar va to'g'ri nomlash;
- **Vaqt va Intizom (10 ball)**: 2 soat (120 min) ichida topshirish.

---

# 1. Imtihon Kod Shabloni

```python
def module_2_exam():
    print("====================================")
    print("   2-MODUL IMTIHONI KODI BAJARILDI  ")
    print("====================================")

module_2_exam()
```

Natija:

```text
====================================
   2-MODUL IMTIHONI KODI BAJARILDI  
====================================
```

---

# 7. Imtihon Topshiriqlari Namunasi

## 1-topshiriq — Oson (15 ball)

**Vazifa:** Berilgan ro'yxatdagi takrorlangan elementlarni `set()` yordamida tozalab, saralangan holda qaytaring.

## 2-topshiriq — O‘rta (15 ball)

**Vazifa:** Matnli fayldan ma'lumotlarni o'qib, undagi har bir so'zning necha marta qatnashganini lug'atda (Dict) hisoblang.

## 3-topshiriq — Murakkab (20 ball)

**Vazifa:** Tashqi API ga `requests` orqali so'rov yuborib, olingan ma'lumotlarni `JSON` faylga yozing hamda xatolarni `try-except` bilan ushlang.

---

# 8. Imtihon topshirish talabi

- kod `.py` faylida bo‘lsin;
- fayl nomi: `24_dars_exam_solution.py`;
- kodda tushunarli o‘zgaruvchi nomlari ishlatilsin;
- kamida ikkita izoh yozilsin.

---

# 10. Qisqa xulosa

Bu darsda:

- `2-modul imtihoni topshirildi`;
- `Pythonda ma'lumotlar tuzilmalari moduli muvaffaqiyatli yakunlandi`

Keyingi darsda: **OOP, class va object**.

---

# Resurslar va fayllar

- 📄 Konspekt: `24_dars_exam_guide.pdf`
- 💻 Kodlar: `github.com/dars-reja/24-dars`
- 🎬 Video: `youtube.com/watch?v=dars24`
- 📝 Qo‘shimcha mashqlar: `python.uz/exam2`
"""
}

for num, txt in FULL_LONG_19_TO_24.items():
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
    if n in FULL_LONG_19_TO_24:
        item["content"] = FULL_LONG_19_TO_24[n]

with open(LESSONS_JSON, "w", encoding="utf-8") as f:
    json.dump(j_data, f, ensure_ascii=False, indent=2)

print("✨ 19-24 darslar kontenti to'liqligicha 10 bo'limli variantda saqlandi!")
