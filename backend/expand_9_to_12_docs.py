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

def get_lesson_9_content():
    return """# 🎲 9. Break, continue va random — Dars dokumentatsiyasi

`break`, `continue` va `random` — Python’da **sikllar oqimini muddatidan oldin boshqarish hamda tasodifiy son va qiymatlarni shakllantirish** uchun ishlatiladi.

Bu mavzu orqali:

- `break` yordamida siklni darhol to'xtatib chiqib ketish;
- `continue` yordamida joriy takrorlanishni o'tkazib yuborib keyingi qadamga o'tish;
- `random.randint()` yordamida ma'lum oraliqda tasodifiy sonlar olish;
- `random.choice()` yordamida ro'yxatdan tasodifiy element tanlash

mumkin.

---

## Dars maqsadi

Bu dars oxirida o‘quvchi:

- Sikllar jarayonida kutilgan shart bajarilganda `break` bilan sikldan chiqish;
- Keraksiz elementlarni `continue` bilan o'tkazib yuborib vaqtni tejash;
- `random` modulidan foydalanib o'yinlar va algoritmlar tuzish

ni mustaqil bajara oladi.

## Kerakli bilimlar

Bu darsni tushunish uchun:

- 7-dars: `for` sikli;
- 8-dars: `while` sikli

bilinishi kerak.

---

# 1. Asosiy tushuncha

`break` va `continue` nima ekanini sodda tilda tushuntiramiz.

Masalan:

> `break` — sikl sharti hali tugamagan bo'lsa ham siklni darhol to'xtatadi. `continue` — joriy qadamni to'xtatib, siklning keyingi takrorlanishiga o'tkazib yuboradi.

Muhim qoida:

```python
import random
secret = random.randint(1, 10)
```

---

# 2. Birinchi sodda misol

```python
for i in range(1, 10):
    if i == 5:
        break
    print(i)
```

Natija:

```text
1
2
3
4
```

Izoh:

- `1-qator` — 1 dan 9 gacha sonlar bo'ylab for sikli;
- `2-3 qatorlar` — `i == 5` bo'lganda `break` ishlaydi va sikl to'xtaydi.

---

# 3. Asosiy metodlar yoki operatorlar

| Kod / metod | Vazifasi | Misol |
|---|---|---|
| `break` | Siklni darhol to'xtatib chiqish | `if x == 5: break` |
| `continue` | Joriy qadamni o'tkazib yuborish | `if x % 2 == 0: continue` |
| `random.randint(a, b)` | a va b oralig'ida tasodifiy son | `random.randint(1, 10)` |
| `random.choice(list)` | Ro'yxatdan tasodifiy element | `random.choice(["olma", "banan"])` |

---

# 4. Batafsil misol — Random O'yin

```python
import random

secret = random.randint(1, 10)

for attempt in range(1, 4):
    guess = int(input(f"{attempt}-urinish (1-10 son kiriting): "))
    if guess == secret:
        print("Tabriklaymiz, topdingiz!")
        break
    else:
        print("Noto'g'ri!")
```

Natija:

```text
1-urinish (1-10 son kiriting): 5
Noto'g'ri!
2-urinish (1-10 son kiriting): 7
Tabriklaymiz, topdingiz!
```

---

# 5. Foydalanuvchidan ma’lumot olish

```python
while True:
    text = input("Matn kiriting (to'xtatish uchun 'stop'): ")
    if text.lower() == "stop":
        print("Dastur to'xtatildi!")
        break
    print("Siz kiritdingiz:", text)
```

Foydalanuvchi kiritadi:

```text
Matn kiriting (to'xtatish uchun 'stop'): Salom
Siz kiritdingiz: Salom
Matn kiriting (to'xtatish uchun 'stop'): stop
```

Natija:

```text
Dastur to'xtatildi!
```

---

# 6. Ko‘p uchraydigan xatolar

## Xato 1: Continue dan so'ng koddagi buyruqlar bajarilmay qolishi

Noto‘g‘ri:

```python
for i in range(5):
    if i == 2:
        continue
        print("Bu chop etilmaydi!")
```

To‘g‘ri:

```python
for i in range(5):
    if i == 2:
        continue
    print(i)
```

---

# 7. Sinfdagi amaliy topshiriqlar

## 1-topshiriq — Oson

**Vazifa:** 1 dan 20 gacha bo'lgan toq sonlarni `continue` yordamida konsolga chiqaring.

## 2-topshiriq — O‘rta

**Vazifa:** `random.choice()` yordamida "Tosh", "Qog'oz", "Qaychi" o'yinini tuzing.

## 3-topshiriq — Murakkab

**Vazifa:** `while True` va `break` yordamida foydalanuvchidan son kiritishni so'rang, manfiy son kiritilganda dasturni to'xtatib yig'indini ko'rsating.

---

# 8. Uyga vazifa

1. `9_dars_break_continue.py` faylini yarating;
2. Kompyuter o'ylagan sonni topish o'yinini 5 ta urinishda ishlaydigan qilib yozing;
3. Kodni GitHub'ga saqlang.

---

# 9. Tekshirish savollari

1. `break` va `continue` ning asosiy farqi nima?
2. `random.randint(1, 6)` qaysi sonlarni chiqarishi mumkin?
3. `while True:` va `break` qanday holatlarda birga ishlatiladi?
4. Bu kodning natijasi qanday bo‘ladi?

```python
for i in range(5):
    if i == 3:
        continue
    print(i, end="")
```

5. O'yinlar dasturlashda random modulinig o'rni nima?

---

# 10. Qisqa xulosa

Bu darsda:

- `break buyrug'i`;
- `continue buyrug'i`;
- `random moduli va metodlari`

ni o‘rgandik.

Keyingi darsda: **Ichma-ich sikl va algoritmlar**.

---

# Resurslar va fayllar

- 📄 Konspekt: `9_dars_konspekt.pdf`
- 💻 Kodlar: `github.com/dars-reja/9-dars`
- 🎬 Video: `youtube.com/watch?v=dars9`
- 📝 Qo‘shimcha mashqlar: `python.uz/mashq9`
"""

def get_lesson_10_content():
    return """# 🧩 10. Ichma-ich sikl va algoritmlar — Dars dokumentatsiyasi

`Ichma-ich sikllar (Nested Loops)` — Python’da **matritsalar, jadvallar va murakkab algoritmik masalalarni yechish** uchun ishlatiladi.

Bu mavzu orqali:

- tashqi va ichki `for` va `while` sikllarini tuzish;
- ko'paytirish jadvalini konsolga chiqarish;
- shakllar (piramida, to'rtburchak) va tub sonlarni topish algoritmlari

mumkin.

---

## Dars maqsadi

Bu dars oxirida o‘quvchi:

- Ichma-ich sikllarning ishlash ketma-ketligini tushunish;
- Ko'paytirish jadvalini chiroyli formatda chiqaruvchi dastur tuzish;
- Berilgan sonning tub yoki murakkab ekanligini aniqlovchi algoritm yozish

ni mustaqil bajara oladi.

## Kerakli bilimlar

Bu darsni tushunish uchun:

- 7-dars: `for` sikli;
- 8-dars: `while` sikli

bilinishi kerak.

---

# 1. Asosiy tushuncha

`Ichma-ich sikl` nima ekanini sodda tilda tushuntiramiz.

Masalan:

> `Ichma-ich sikl` — bu bir sikl bloki ichida ikkinchi bir siklning joylashtirilishi. Tashqi siklning har bir qadami uchun ichki sikl to'liq aylanib chiqadi.

Muhim qoida:

```python
for i in range(3):
    for j in range(3):
        print(i, j)
```

---

# 2. Birinchi sodda misol

```python
for i in range(1, 4):
    for j in range(1, 4):
        print(f"({i},{j})", end=" ")
    print()
```

Natija:

```text
(1,1) (1,2) (1,3) 
(2,1) (2,2) (2,3) 
(3,1) (3,2) (3,3) 
```

Izoh:

- `1-qator` — Tashqi sikl `i` (1, 2, 3);
- `2-qator` — Ichki sikl `j` (1, 2, 3);
- `3-qator` — Har bir katak uchun indekslar chiqariladi va `print()` yangi qatordan boshlaydi.

---

# 4. Batafsil misol — Ko'paytirish Jadvali

```python
print("====================================")
print("       KO'PAYTIRISH JADVALI         ")
print("====================================")

for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i} x {j} = {i*j:2d}", end=" | ")
    print()
```

Natija:

```text
1 x 1 =  1 | 1 x 2 =  2 | 1 x 3 =  3 | 1 x 4 =  4 | 1 x 5 =  5 | 
2 x 1 =  2 | 2 x 2 =  4 | 2 x 3 =  6 | 2 x 4 =  8 | 2 x 5 = 10 | 
3 x 1 =  3 | 3 x 2 =  6 | 3 x 3 =  9 | 3 x 4 = 12 | 3 x 5 = 15 | 
```

---

# 6. Ko‘p uchraydigan xatolar

## Xato 1: Indentatsiyani (joy tashlashni) adashtirib yuborish

Noto‘g‘ri:

```python
for i in range(3):
for j in range(3):  # IndentationError!
    print(i, j)
```

To‘g‘ri:

```python
for i in range(3):
    for j in range(3):
        print(i, j)
```

---

# 7. Sinfdagi amaliy topshiriqlar

## 1-topshiriq — Oson

**Vazifa:** Yulduzchalardan foydalanib 4x4 kvadrat shaklini ekranga chiqaring.

## 2-topshiriq — O‘rta

**Vazifa:** 1 dan 50 gacha bo'lgan tub sonlarni (faqat 1 ga va o'ziga bo'linadigan) ichma-ich sikl bilan toping.

---

# 8. Uyga vazifa

1. `10_dars_nested_loops.py` faylini yarating;
2. 1 dan 10 gacha bo'lgan sonlar uchun to'liq 10x10 ko'paytirish jadvalini yozing;
3. Kodni GitHub'ga saqlang.

---

# 9. Tekshirish savollari

1. Tashqi sikl 5 marta, ichki sikl 4 marta aylansa, ichki kod necha marta bajariladi (20 marta)?
2. `print(end=" ")` parametri nima uchun ishlatiladi?
3. Tub sonni aniqlash algoritmi qanday ishlaydi?

---

# 10. Qisqa xulosa

Bu darsda:

- `Ichma-ich sikllar strukturasi`;
- `Ko'paytirish jadvali algoritmi`;
- `Tub sonlarni saralash`

ni o‘rgandik.

Keyingi darsda: **List asoslari**.

---

# Resurslar va fayllar

- 📄 Konspekt: `10_dars_konspekt.pdf`
- 💻 Kodlar: `github.com/dars-reja/10-dars`
- 🎬 Video: `youtube.com/watch?v=dars10`
- 📝 Qo‘shimcha mashqlar: `python.uz/mashq10`
"""

def get_lesson_11_content():
    return """# 📋 11. List asoslari — Dars dokumentatsiyasi

`List (Ro'yxat)` — Python’da **bir nechta ma'lumotlarni bitta o'zgaruvchida tartiblangan va o'zgaruvchan (mutable) shaklda saqlash** uchun ishlatiladi.

Bu mavzu orqali:

- ro'yxat yaratish va indekslar orqali murojaat qilish;
- ro'yxatga element qo'shish (`.append()`, `.insert()`);
- elementlarni o'chirish (`.pop()`, `.remove()`);
- saralash (`.sort()`, `.reverse()`) hamda `len()` funksiyasi

mumkin.

---

## Dars maqsadi

Bu dars oxirida o‘quvchi:

- Turli toifadagi ma'lumotlardan iborat ro'yxatlar tuzish;
- `.append()` va `.pop()` yordamida ro'yxatni dinamik o'zgartirish;
- `.sort()` yordamida sonlar va matnlarni saralash

ni mustaqil bajara oladi.

## Kerakli bilimlar

Bu darsni tushunish uchun:

- 2-dars: O'zgaruvchilar;
- 4-dars: Indekslar (0 dan boshlanishi)

bilinishi kerak.

---

# 1. Asosiy tushuncha

`List` nima ekanini sodda tilda tushuntiramiz.

Masalan:

> `List` — elementlar ketma-ketligi bo'lib, kvadrat qavslar `[]` ichida vergul bilan ajratib yoziladi. U o'zgartirilishi mumkin.

Muhim qoida:

```python
fruits = ["olma", "banan", "uzum"]
print(fruits[0])  # 'olma'
```

---

# 2. Birinchi sodda misol

```python
numbers = [10, 20, 30]
numbers.append(40)
print("Ro'yxat:", numbers)
print("Uzunligi:", len(numbers))
```

Natija:

```text
Ro'yxat: [10, 20, 30, 40]
Uzunligi: 4
```

Izoh:

- `1-qator` — 3 ta elementdan iborat ro'yxat;
- `2-qator` — `.append(40)` ro'yxat oxiriga 40 ni qo'shadi;
- `4-qator` — `len()` ro'yxat elementlari sonini 4 deb beradi.

---

# 3. Asosiy metodlar yoki operatorlar

| Metod / Funksiya | Vazifasi | Misol |
|---|---|---|
| `.append(val)` | Oxiriga element qo'shish | `fruits.append("behi")` |
| `.insert(idx, val)` | Belgilangan indeksga qo'shish | `fruits.insert(0, "anor")` |
| `.pop(idx)` | Indeks bo'yicha sudrab o'chirish | `fruits.pop(0)` |
| `.remove(val)` | Qiymat bo'yicha o'chirish | `fruits.remove("banan")` |
| `.sort()` | Kichikdan kattaga saralash | `nums.sort()` |
| `.reverse()` | Ro'yxatni teskari aylantirish | `nums.reverse()` |

---

# 4. Batafsil misol — Talabalar Ro'yxati

```python
students = ["Ali", "Vali", "Sardor"]
students.append("Jasur")
students.sort()

for idx, name in enumerate(students, 1):
    print(f"{idx}. {name}")
```

Natija:

```text
1. Ali
2. Jasur
3. Sardor
4. Vali
```

---

# 6. Ko‘p uchraydigan xatolar

## Xato 1: Mavjud bo'lmagan indeksga murojaat qilish (IndexError)

Noto‘g‘ri:

```python
nums = [1, 2]
print(nums[5])  # IndexError!
```

To‘g‘ri:

```python
nums = [1, 2]
print(nums[0])
```

---

# 7. Sinfdagi amaliy topshiriqlar

## 1-topshiriq — Oson

**Vazifa:** 5 ta sevgan taomingiz ro'yxatini tuzing va o'rtadagi taomni chop eting.

## 2-topshiriq — O‘rta

**Vazifa:** Sonlar ro'yxati berilgan. Undagi eng katta va eng kichik sonni `.sort()` yoki `max()` / `min()` yordamida toping.

---

# 8. Uyga vazifa

1. `11_dars_lists.py` faylini yarating;
2. Bo'sh ro'yxat yaratib `input()` yordamida 5 ta do'stingiz ismini qo'shing va alifbo tartibida saralang;
3. Kodni GitHub'ga saqlang.

---

# 9. Tekshirish savollari

1. `.append()` va `.insert()` farqi nima?
2. Ro'yxatning oxirgi elementiga qanday murojaat qilinadi (`list[-1]`)?
3. `.pop()` va `.remove()` ning farqi nimada?

---

# 10. Qisqa xulosa

Bu darsda:

- `List strukturasi va indekslar`;
- `.append(), .pop(), .sort() metodlari`;
- `len() va enumerate()`

ni o‘rgandik.

Keyingi darsda: **1-modul imtihoni**.

---

# Resurslar va fayllar

- 📄 Konspekt: `11_dars_konspekt.pdf`
- 💻 Kodlar: `github.com/dars-reja/11-dars`
- 🎬 Video: `youtube.com/watch?v=dars11`
- 📝 Qo‘shimcha mashqlar: `python.uz/mashq11`
"""

def get_lesson_12_content():
    return """# 🎓 12. 1-modul imtihoni — Dars dokumentatsiyasi

`1-modul imtihoni` — 1-darsdan 11-darsgacha o'rganilgan **Python asoslari, o'zgaruvchilar, arifmetika, stringlar, shartlar, sikllar va ro'yxat ko'nikmalarini sinash va sertifikatlash** uchun o'tkaziladi.

Bu dars orqali:

- 1–11 darslar bo'yicha nazariy va amaliy bilimlarni mustahkamlash;
- real vaqt rejimida 3 ta murakkab algoritmik masalani yechish;
- PEP8 standarti va kod sifatini amalda ko'rsatish

mumkin.

---

## Imtihon Tartibi (100 ballik shkala)

- **Nazariy Testlar (20 ball)**: 1-11 darslar bo'yicha 10 ta test;
- **Amaliy Masalalar (50 ball)**: 3 ta algoritmik kod yozish topshirig'i;
- **PEP8 Standart va Kod Sifati (20 ball)**: Izohlar va to'g'ri nomlash;
- **Vaqt va Intizom (10 ball)**: 2 soat (120 min) ichida topshirish.

---

# 1. Imtihon Kod Shabloni

```python
def main_exam_solution():
    print("====================================")
    print("   1-MODUL IMTIHONI KODI BAJARILDI  ")
    print("====================================")

main_exam_solution()
```

Natija:

```text
====================================
   1-MODUL IMTIHONI KODI BAJARILDI  
====================================
```

---

# 7. Imtihon Topshiriqlari Namunasi

## 1-topshiriq — Oson (15 ball)

**Vazifa:** Foydalanuvchidan 3 ta son olib, ularning o'rtacha arifmetigini hisoblang.

## 2-topshiriq — O‘rta (15 ball)

**Vazifa:** Berilgan matndagi unli va undosh harflar sonini `for` va `if` yordamida hisoblang.

## 3-topshiriq — Murakkab (20 ball)

**Vazifa:** Sonlar ro'yxatidan faqat tub sonlarni ajratib oluvchi va saralab beruvchi dastur tuzing.

---

# 8. Imtihon topshirish talabi

- kod `.py` faylida bo‘lsin;
- fayl nomi: `12_dars_exam_solution.py`;
- kodda tushunarli o‘zgaruvchi nomlari ishlatilsin;
- kamida ikkita izoh yozilsin.

---

# 10. Qisqa xulosa

Bu darsda:

- `1-modul imtihoni topshirildi`;
- `Python asoslari moduli muvaffaqiyatli yakunlandi`

Keyingi darsda: **Tuple va set**.

---

# Resurslar va fayllar

- 📄 Konspekt: `12_dars_exam_guide.pdf`
- 💻 Kodlar: `github.com/dars-reja/12-dars`
- 🎬 Video: `youtube.com/watch?v=dars12`
- 📝 Qo‘shimcha mashqlar: `python.uz/exam1`
"""

def apply_full_long_contents():
    content_map = {
        9: get_lesson_9_content(),
        10: get_lesson_10_content(),
        11: get_lesson_11_content(),
        12: get_lesson_12_content(),
    }

    for num, text in content_map.items():
        try:
            lesson_obj = Lesson.objects.get(lesson_number=num)
            lesson_obj.content = text
            lesson_obj.save()
            print(f"✅ {num}-dars kontenti to'liq 10 bo'limli matn bilan yangilandi.")
        except Lesson.DoesNotExist:
            pass

    with open(LESSONS_JSON, "r", encoding="utf-8") as f:
        json_data = json.load(f)

    for item in json_data:
        num = item.get("lessonNumber")
        if num in content_map:
            item["content"] = content_map[num]

    with open(LESSONS_JSON, "w", encoding="utf-8") as f:
        json.dump(json_data, f, ensure_ascii=False, indent=2)

    print("✨ 9, 10, 11 va 12 darslarning kontenti to'liq yangilandi!")

if __name__ == "__main__":
    apply_full_long_contents()
