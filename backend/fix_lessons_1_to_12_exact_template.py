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

# 1-DARSDAN 12-DARSGACHA EXPLICIT MUKAMMAL DOKUMENTATSIYALAR
EXACT_1_TO_12_LESSONS = {
    1: {
        "title": "1-dars — Dasturlash muhiti va Python",
        "content": """# 🐍 1. Dasturlash muhiti va Python — Dars dokumentatsiyasi

`Python` — Python'da **zamonaviy, sodda va yuqori unumdorlikka ega dasturlarni yozish** uchun ishlatiladi.

Bu mavzu orqali:

- VS Code va Python muhitini kompyuterga sozlash;
- terminalda `.py` kengaytmasidagi fayllarni ishga tushirish;
- `print()` funksiyasi yordamida ekranga matn va sonlarni chiqarish;
- `#` belgisi orqali kodga izohlar (comments) qoldirish

mumkin.

---

## Dars maqsadi

Bu dars oxirida o‘quvchi:

- VS Code redaktorida yangi `main.py` faylini yaratish va saqlash;
- `print()` funksiyasi yordamida konsolga turli ma'lumotlarni chiqarish;
- terminalda `python main.py` buyrug'i orqali kodni ishga tushirish

ni mustaqil bajara oladi.

## Kerakli bilimlar

Bu darsni tushunish uchun:

- Kompyuter fayllar tizimi va papkalar bilan ishlash;
- Klaviaturada maxsus belgilarni (`"`, `'`, `#`, `()`) terish

bilinishi kerak.

---

# 1. Asosiy tushuncha

`Python` nima ekanini sodda tilda tushuntiramiz.

Masalan:

> `Python` — bu yuqori darajali, interpretatsiya qilinadigan dasturlash tili. U kodning toza va o'qilishining qulayligi uchun ishlatiladi.

Muhim qoida:

```python
# Python fayllari har doim .py kengaytmasi bilan saqlanadi
print("Salom, Python dunyosiga xush kelibsiz!")
```

---

# 2. Birinchi sodda misol

```python
print("Assalomu alaykum!")
print("Men Python Backend dasturchisiman.")
# Bu birinchi Python dasturim
```

Natija:

```text
Assalomu alaykum!
Men Python Backend dasturchisiman.
```

Izoh:

- `1-qator` — `print()` funksiyasi matnni ekranga chiqaradi;
- `2-qator` — ikkinchi qatorda ma'lumot chop etiladi;
- `3-qator` — `#` belgisi bilan izoh yozilgan, u ijro etilmaydi.

---

# 3. Asosiy metodlar yoki operatorlar

| Kod / metod | Vazifasi | Misol |
|---|---|---|
| `print()` | Consolga ma'lumot chiqarish | `print("Salom")` |
| `#` | Bir qatorli izoh qoldirish | `# Izoh` |
| `python` | Terminalda faylni yurgizish | `python main.py` |

---

# 4. Batafsil misol

```python
print("====================================")
print("       PYTHON BACKEND BACKBONE      ")
print("====================================")
print("Modullar:", 6, "ta")
print("Darslar:", 72, "ta dars")
```

Natija:

```text
====================================
       PYTHON BACKEND BACKBONE      
====================================
Modullar: 6 ta
Darslar: 72 ta dars
```

Kod qanday ishlaydi:

1. Birinchi va uchinchi qatorlarda chegara chiziqlari chop etiladi;
2. Ikkinchi qatorda dastur sarlavhasi o'rtaga joylashtiriladi;
3. To'rtinchi va beshinchi qatorlarda matn va sonlar birgalikda ekranga chiqariladi;
4. Dastur muvaffaqiyatli yakunlanadi.

---

# 5. Foydalanuvchidan ma’lumot olish

```python
name = input("Ismingizni kiriting: ")
print("Xush kelibsiz,", name)
```

Foydalanuvchi kiritadi:

```text
Ismingizni kiriting: Ali
```

Natija:

```text
Xush kelibsiz, Ali
```

Eslatma:

> `input()` orqali olingan ma’lumot odatda `str` bo‘ladi. Zarur holatda `int()`, `float()` yoki boshqa turga o‘tkaziladi.

---

# 6. Ko‘p uchraydigan xatolar

## Xato 1: Print funksiyasini katta harf bilan yozish

Noto‘g‘ri:

```python
Print("Salom")
```

To‘g‘ri:

```python
print("Salom")
```

Sabab: Python katta va kichik harflarni ajratadi (case-sensitive).

## Xato 2: Qo'shtirnoqni yopmaslik

Noto‘g‘ri:

```python
print("Salom)
```

To‘g‘ri:

```python
print("Salom")
```

---

# 7. Sinfdagi amaliy topshiriqlar

## 1-topshiriq — Oson

**Vazifa:** `print()` yordamida o'zingiz haqingizda 3 qator ma'lumot chiqaring.

Kutilgan natija:

```text
Ism: Ali
Kasb: Dasturchi
Shahar: Toshkent
```

## 2-topshiriq — O‘rta

**Vazifa:** Yulduzcha `*` belgilaridan foydalanib konsolga uchburchak shaklini chiqaring.

Talab:

- Kamida 3 qatordan iborat bo'lsin;
- Har bir qatorda yulduzchalar soni oshib borsin;
- Izohlar bilan tushuntirilsin.

## 3-topshiriq — Murakkab

**Vazifa:** Shaxsiy vizitka kartangizni terminalda ramka bilan chiqaruvchi dastur tuzing.

---

# 8. Uyga vazifa

1. `1_dars_intro.py` faylini yarating;
2. O'zingiz, yo'nalishingiz va maqsadingiz haqida 7 qatorli dastur yozing;
3. Har bir qatorga izoh berib bering;
4. Kodni GitHub'ga saqlang.

Uyga vazifa topshirish talabi:

- kod `.py` faylida bo‘lsin;
- fayl nomi: `1_dars_intro.py`;
- kodda tushunarli o‘zgaruvchi nomlari ishlatilsin;
- kamida bitta izoh yozilsin.

---

# 9. Tekshirish savollari

1. `print()` funksiyasi nima vazifa bajaradi?
2. `#` belgisi nima uchun ishlatiladi?
3. Python fayllarining kengaytmasi qanday bo'ladi?
4. Bu kodning natijasi qanday bo‘ladi?

```python
print("10 + 20 =", 10 + 20)
```

5. Real loyihalarda `print()` dan qanday maqsadda foydalaniladi?

---

# 10. Qisqa xulosa

Bu darsda:

- `VS Code muhitini sozlash`;
- `print() funksiyasi va izohlar`;
- `Terminalda kodni yurgizish`

ni o‘rgandik.

Keyingi darsda: **O‘zgaruvchilar va turlar**.

---

# Resurslar va fayllar

- 📄 Konspekt: `1_dars_konspekt.pdf`
- 💻 Kodlar: `github.com/dars-reja/1-dars`
- 🎬 Video: `youtube.com/watch?v=dars1`
- 📝 Qo‘shimcha mashqlar: `python.uz/mashq1`
""",
        "code": "print('Assalomu alaykum!')\nprint('Python kursi: 1-dars')\n# Bu mening birinchi dasturim",
        "code_exp": "- `1-qator` — print() funksiyasi matnni konsolga chiqaradi;\n- `2-qator` — Ikkinchi matn ekranga chop etiladi;\n- `3-qator` — Izoh qatori, bajarilmaydi.",
        "quiz_q": "Python'da konsolga ma'lumot chiqaruvchi funksiya qaysi?",
        "quiz_opts": ["console.log()", "print()", "System.out.println()", "echo"],
        "quiz_ans": 1,
        "quiz_exp": "Python'da ekranga matn chiqarish uchun print() funksiyasi ishlatiladi."
    },

    2: {
        "title": "2-dars — O‘zgaruvchilar va turlar",
        "content": """# 📦 2. O‘zgaruvchilar va turlar — Dars dokumentatsiyasi

`O'zgaruvchilar` — Python’da **ma'lumotlarni kompyuter xotirasida saqlash va ularga nom berish** uchun ishlatiladi.

Bu mavzu orqali:

- o'zgaruvchi e'lon qilish va unga qiymat biriktirish;
- 4 ta asosiy ma'lumot turini o'rganish (`str`, `int`, `float`, `bool`);
- `type()` funksiyasi yordamida o'zgaruvchi turini aniqlash;
- PEP8 nomlash qoidalari (`snake_case`) bo'yicha kod yozish

mumkin.

---

## Dars maqsadi

Bu dars oxirida o‘quvchi:

- Turli xildagi ma'lumotlar uchun mos o'zgaruvchilar yaratish;
- `type()` funksiyasi orqali ma'lumot turini tekshirish;
- O'zgaruvchi nomlashda PEP8 qoidalariga rioya qilish

ni mustaqil bajara oladi.

## Kerakli bilimlar

Bu darsni tushunish uchun:

- 1-dars: `print()` funksiyasi va izohlar;
- Klaviaturada sonlar va harflarni to'g'ri terish

bilinishi kerak.

---

# 1. Asosiy tushuncha

`O'zgaruvchi` nima ekanini sodda tilda tushuntiramiz.

Masalan:

> `O'zgaruvchi` — bu ma'lumot saqlanadigan nomlangan idish (konteyner). U dastur davomida ma'lumotni saqlash va yangilash uchun kerak.

Muhim qoida:

```python
# O'zgaruvchiga qiymat '=' tenglik belgisi orqali biriktiriladi
x = 10
```

---

# 2. Birinchi sodda misol

```python
name = "Ali"
age = 20
height = 1.75
is_student = True

print(name)
print(age)
```

Natija:

```text
Ali
20
```

Izoh:

- `1-qator` — `name` nomli string (matn) o'zgaruvchisi yaratildi;
- `2-qator` — `age` nomli integer (butun son) o'zgaruvchisi yaratildi;
- `3-qator` — `height` o'nlik kasr (float) o'zgaruvchisi yaratildi.

---

# 3. Asosiy metodlar yoki operatorlar

| Kod / metod | Vazifasi | Misol |
|---|---|---|
| `str` | Matnli ma'lumot turi | `"Salom"` |
| `int` | Butun son ma'lumot turi | `25` |
| `float` | O'nlik kasr son ma'lumot turi | `3.14` |
| `bool` | Mantiqiy qiymat (True/False) | `True` |
| `type()` | Ma'lumot turini aniqlash | `type(x)` |

---

# 4. Batafsil misol

```python
user_name = "Sardor"
user_age = 22
user_gpa = 3.8
is_active = True

print("Ism:", user_name, "| Turi:", type(user_name))
print("Yosh:", user_age, "| Turi:", type(user_age))
print("GPA:", user_gpa, "| Turi:", type(user_gpa))
print("Faolmi:", is_active, "| Turi:", type(is_active))
```

Natija:

```text
Ism: Sardor | Turi: <class 'str'>
Yosh: 22 | Turi: <class 'int'>
GPA: 3.8 | Turi: <class 'float'>
Faolmi: True | Turi: <class 'bool'>
```

Kod qanday ishlaydi:

1. 4 ta turli toifadagi o'zgaruvchi e'lon qilinadi;
2. `print()` yordamida o'zgaruvchi qiymati chiqariladi;
3. `type()` yordamida har bir o'zgaruvchining mansub turi chop etiladi;
4. Natijada `str`, `int`, `float` va `bool` sinflari ko'rinadi.

---

# 5. Foydalanuvchidan ma’lumot olish

```python
age = input("Yoshingizni kiriting: ")
print("Siz kiritgan yosh:", age)
print("Turi:", type(age))
```

Foydalanuvchi kiritadi:

```text
Yoshingizni kiriting: 25
```

Natija:

```text
Siz kiritgan yosh: 25
Turi: <class 'str'>
```

Eslatma:

> `input()` orqali olingan ma’lumot odatda `str` bo‘ladi. Zarur holatda `int()`, `float()` yoki boshqa turga o‘tkaziladi.

---

# 6. Ko‘p uchraydigan xatolar

## Xato 1: O'zgaruvchi nomini raqam bilan boshlash

Noto‘g‘ri:

```python
1user = "Ali"
```

To‘g‘ri:

```python
user_1 = "Ali"
```

Sabab: Python'da o'zgaruvchi nomi raqam bilan boshlanishi taqiqlangan.

## Xato 2: O'zgaruvchini e'lon qilmay ishlatish

Noto‘g‘ri:

```python
print(total_price)
```

To‘g‘ri:

```python
total_price = 100
print(total_price)
```

---

# 7. Sinfdagi amaliy topshiriqlar

## 1-topshiriq — Oson

**Vazifa:** O'zingiz yoqtirgan kitob nomi, sahifalar soni va narxini o'zgaruvchilarda saqlang.

Kutilgan natija:

```text
Kitob: Dunyoning ishlari
Sahifa: 220
Narx: 45000.0
```

## 2-topshiriq — O‘rta

**Vazifa:** 4 xil turdagi o'zgaruvchi yarating va ularning `type()` turini ekranga chiqaring.

## 3-topshiriq — Murakkab

**Vazifa:** Ikki o'zgaruvchining qiymatlarini uchinchi o'zgaruvchisiz bir-biri bilan almashtiring (`a, b = b, a`).

---

# 8. Uyga vazifa

1. `2_dars_variables.py` faylini yarating;
2. 10 turli o'zgaruvchi yaratib, ularning qiymati va type() turini ekranga chiqaring;
3. Kodni GitHub'ga saqlang.

Uyga vazifa topshirish talabi:

- kod `.py` faylida bo‘lsin;
- fayl nomi: `2_dars_variables.py`;
- kodda tushunarli o‘zgaruvchi nomlari ishlatilsin;
- kamida bitta izoh yozilsin.

---

# 9. Tekshirish savollari

1. `str` va `int` ning asosiy farqi nima?
2. `type(12.5)` nimani qaytaradi?
3. O'zgaruvchi nomlashda qaysi uslub ishlatiladi (`snake_case`)?
4. Bu kodning natijasi qanday bo‘ladi?

```python
x = "10"
y = 20
print(type(x), type(y))
```

5. O'nlik kasr sonlar qaysi ma'lumot turiga kiradi?

---

# 10. Qisqa xulosa

Bu darsda:

- `o'zgaruvchi yaratish`;
- `str, int, float, bool turlari`;
- `type() funksiyasi`

ni o‘rgandik.

Keyingi darsda: **Input va arifmetika**.

---

# Resurslar va fayllar

- 📄 Konspekt: `2_dars_konspekt.pdf`
- 💻 Kodlar: `github.com/dars-reja/2-dars`
- 🎬 Video: `youtube.com/watch?v=dars2`
- 📝 Qo‘shimcha mashqlar: `python.uz/mashq2`
""",
        "code": "name = 'Ali'\nage = 20\ngpa = 3.8\nis_student = True\n\nprint(name, type(name))\nprint(age, type(age))",
        "code_exp": "- `1-4 qatorlar` — str, int, float, bool o'zgaruvchilar e'lon qilindi;\n- `6-7 qatorlar` — O'zgaruvchi qiymati va u mansub bo'lgan type() turi chop etiladi.",
        "quiz_q": "O'nlik kasr sonlarni saqlovchi ma'lumot turi qaysi?",
        "quiz_opts": ["int", "float", "str", "bool"],
        "quiz_ans": 1,
        "quiz_exp": "float turi o'nlik kasr sonlarni (masalan 3.8) saqlaydi."
    },

    3: {
        "title": "3-dars — Input va arifmetika",
        "content": """# 🧮 3. Input va arifmetika — Dars dokumentatsiyasi

`input()` va arifmetik operatorlar — Python’da **foydalanuvchidan ma'lumot olish va hisob-kitob amallarini bajarish** uchun ishlatiladi.

Bu mavzu orqali:

- `input()` orqali kiritilgan matnni `int()` yoki `float()` ga o'tkazish;
- arifmetik amallar: `+`, `-`, `*`, `/`;
- qoldiq bo'lish (`%`), butunli bo'lish (`//`) va darajaga ko'tarish (`**`)

mumkin.

---

## Dars maqsadi

Bu dars oxirida o‘quvchi:

- `input()` orqali ma'lumot kiritish va turlarni to'g'ri o'tkazish;
- Barcha arifmetik operatorlarni amaliy masalalarda qo'llash;
- Kichik kalkulyator dasturini tuzish

ni mustaqil bajara oladi.

## Kerakli bilimlar

Bu darsni tushunish uchun:

- 2-dars: O'zgaruvchilar va turlar (`int`, `float`, `str`);
- Matematik amal bajarish ketma-ketligi

bilinishi kerak.

---

# 1. Asosiy tushuncha

`input()` nima ekanini sodda tilda tushuntiramiz.

Masalan:

> `input()` — konsolda foydalanuvchiga savol berib kiritilgan ma'lumotni matn (str) shaklida o'qiydi. Sonlar bilan ishlash uchun uni `int()` yoki `float()` yordamida o'tkazish shart.

Muhim qoida:

```python
a = int(input("Birinchi son: "))
b = int(input("Ikkinchi son: "))
```

---

# 2. Birinchi sodda misol

```python
x = 15
y = 4

print("Yig'indi:", x + y)
print("Ayirma:", x - y)
print("Ko'paytma:", x * y)
print("Bo'lish:", x / y)
```

Natija:

```text
Yig'indi: 19
Ayirma: 11
Ko'paytma: 60
Bo'lish: 3.75
```

Izoh:

- `1-2 qatorlar` — `x` va `y` o'zgaruvchilariga sonlar berildi;
- `4-7 qatorlar` — Asosiy 4 ta arifmetik amal bajarilib ekranga chiqarildi.

---

# 3. Asosiy metodlar yoki operatorlar

| Kod / metod | Vazifasi | Misol (`a=17, b=5`) | Natija |
|---|---|---|---|
| `+` | Qo'shish | `17 + 5` | `22` |
| `-` | Ayirish | `17 - 5` | `12` |
| `*` | Ko'paytirish | `17 * 5` | `85` |
| `/` | Bo'lish (float) | `17 / 5` | `3.4` |
| `//` | Butunli bo'lish | `17 // 5` | `3` |
| `%` | Qoldiqni topish | `17 % 5` | `2` |
| `**` | Darajaga ko'tarish | `2 ** 3` | `8` |

---

# 4. Batafsil misol

```python
num1 = float(input("1-sonni kiriting: "))
num2 = float(input("2-sonni kiriting: "))

sum_val = num1 + num2
div_val = num1 // num2
mod_val = num1 % num2

print(f"Yig'indi: {sum_val}")
print(f"Butun bo'lish (//): {div_val}")
print(f"Qoldiq (%): {mod_val}")
```

Natija:

```text
1-sonni kiriting: 17
2-sonni kiriting: 5
Yig'indi: 22.0
Butun bo'lish (//): 3.0
Qoldiq (%): 2.0
```

Kod qanday ishlaydi:

1. Foydalanuvchidan 2 ta son float shaklida olinadi;
2. `//` operatori bo'linmaning faqat butun qismini oladi;
3. `%` operatori bo'linmaning qoldig'ini ajratadi;
4. Natijalar `f-string` orqali chop etiladi.

---

# 5. Foydalanuvchidan ma’lumot olish

```python
birth_year = int(input("Tug'ilgan yilingiz: "))
current_year = 2026
age = current_year - birth_year
print("Yoshingiz:", age)
```

Foydalanuvchi kiritadi:

```text
Tug'ilgan yilingiz: 2006
```

Natija:

```text
Yoshingiz: 20
```

Eslatma:

> `input()` orqali olingan ma’lumot odatda `str` bo‘ladi. Zarur holatda `int()`, `float()` yoki boshqa turga o‘tkaziladi.

---

# 6. Ko‘p uchraydigan xatolar

## Xato 1: Str va Int qo'shish xatosi

Noto‘g‘ri:

```python
age = input("Yosh: ")
print(age + 5)  # TypeError!
```

To‘g‘ri:

```python
age = int(input("Yosh: "))
print(age + 5)
```

Sabab: `input()` matn qaytaradi. Matnga sonni to'g'ridan-to'g'ri qo'shib bo'lmaydi.

---

# 7. Sinfdagi amaliy topshiriqlar

## 1-topshiriq — Oson

**Vazifa:** Foydalanuvchidan 2 ta son olib, ularning ko'paytmasini chiqaruvchi dastur yozing.

## 2-topshiriq — O‘rta

**Vazifa:** To'g'ri to'rtburchakning boyi va enini olib, yuzi hamda perimetrini hisoblang.

## 3-topshiriq — Murakkab

**Vazifa:** Foydalanuvchidan minutlarni olib, uni soat va minutlarga ajratuvchi dastur tuzing (masalan 135 minut -> 2 soat 15 minut).

---

# 8. Uyga vazifa

1. `3_dars_arithmetic.py` faylini yarating;
2. Doiraning radiusini olib, yuzini hisoblang (`S = pi * r^2`);
3. Kodni GitHub'ga saqlang.

Uyga vazifa topshirish talabi:

- kod `.py` faylida bo‘lsin;
- fayl nomi: `3_dars_arithmetic.py`;
- kamida bitta izoh yozilsin.

---

# 9. Tekshirish savollari

1. `17 // 5` va `17 % 5` natijasi nimaga teng?
2. `input()` qaytaradigan standart ma'lumot turi qaysi?
3. `2 ** 4` nimani anglatadi?
4. Bu kodning natijasi qanday bo‘ladi?

```python
x = 10
y = 3
print(x // y, x % y)
```

5. Real loyihalarda `%` (qoldiq) operatori qayerlarda ishlatiladi?

---

# 10. Qisqa xulosa

Bu darsda:

- `input() orqali ma'lumot kiritish`;
- `int() va float() ga o'tkazish`;
- `Arifmetik operatorlar (+, -, *, /, //, %, **)`

ni o‘rgandik.

Keyingi darsda: **Stringlar**.

---

# Resurslar va fayllar

- 📄 Konspekt: `3_dars_konspekt.pdf`
- 💻 Kodlar: `github.com/dars-reja/3-dars`
- 🎬 Video: `youtube.com/watch?v=dars3`
- 📝 Qo‘shimcha mashqlar: `python.uz/mashq3`
""",
        "code": "a = float(input('1-son: '))\nb = float(input('2-son: '))\nprint('Qoldiq:', a % b)\nprint('Butun bo\\'lish:', a // b)",
        "code_exp": "- `1-2 qatorlar` — input() ma'lumoti float() ga o'tkaziladi;\n- `3-qator` — % operatori bo'lish qoldig'ini beradi;\n- `4-qator` — // operatori faqat butun qismini oladi.",
        "quiz_q": "17 // 5 amalining natijasi nechaga teng bo'ladi?",
        "quiz_opts": ["3.4", "3", "2", "3.0"],
        "quiz_ans": 1,
        "quiz_exp": "// operatori faqat bo'linmaning butun qismini oladi: 17 // 5 = 3."
    },

    4: {
        "title": "4-dars — Stringlar",
        "content": """# 🔤 4. Stringlar — Dars dokumentatsiyasi

`String (Matn)` — Python’da **matnli ma'lumotlarni saqlash, kesish va formatlash** uchun ishlatiladi.

Bu mavzu orqali:

- string kesish (slicing: `[start:stop:step]`);
- matn metodlari: `.upper()`, `.lower()`, `.strip()`, `.replace()`, `.split()`;
- `len()` funksiyasi va `f-string` yordamida matnni shakllantirish

mumkin.

---

## Dars maqsadi

Bu dars oxirida o‘quvchi:

- Matndan indeks va slicing yordamida kerakli qismlarni ajratish;
- `.split()` yordamida emaildan login va domenni ajratish;
- Kiritilgan matndagi ortiqcha bo'sh joylarni `.strip()` bilan tozalash

ni mustaqil bajara oladi.

## Kerakli bilimlar

Bu darsni tushunish uchun:

- 2-dars: `str` ma'lumot turi;
- Qo'shtirnoq va bir tirnoqlar bilan ishlash

bilinishi kerak.

---

# 1. Asosiy tushuncha

`String` nima ekanini sodda tilda tushuntiramiz.

Masalan:

> `String` — belgilar ketma-ketligi bo'lib, har bir belgi o'z indeksiga ega (0 dan boshlanadi).

Muhim qoida:

```python
text = "Python"
print(text[0])       # 'P' (birinchi belgi)
print(text[0:4])     # 'Pyth' (slicing kesish)
```

---

# 2. Birinchi sodda misol

```python
raw_text = "  python backend  "
clean_text = raw_text.strip().upper()
print("Natija:", clean_text)
```

Natija:

```text
Natija: PYTHON BACKEND
```

Izoh:

- `1-qator` — Boshida va oxirida bo'sh joyi bor string;
- `2-qator` — `.strip()` bo'sh joyni o'chiradi, `.upper()` katta harflarga o'tkazadi.

---

# 3. Asosiy metodlar yoki operatorlar

| Kod / metod | Vazifasi | Misol |
|---|---|---|
| `len(s)` | Matn uzunligini aniqlash | `len("Salom")` -> `5` |
| `.upper()` | Katta harflarga o'tkazish | `"py".upper()` -> `"PY"` |
| `.lower()` | Kichik harflarga o'tkazish | `"PY".lower()` -> `"py"` |
| `.strip()` | Chekkadagi bo'sh joylarni o'chirish | `" a ".strip()` -> `"a"` |
| `.split()` | Matnni ajratib ro'yxat qilish | `"a@b".split("@")` |
| `.replace()` | Matn qismini almashtirish | `"Py1".replace("1","2")` |

---

# 4. Batafsil misol — Email parse qilish

```python
email = "ogabek.dev@gmail.com"
parts = email.split("@")
username = parts[0]
domain = parts[1]

print(f"Foydalanuvchi: {username.upper()}")
print(f"Domen: {domain}")
```

Natija:

```text
Foydalanuvchi: OGABEK.DEV
Domen: gmail.com
```

Kod qanday ishlaydi:

1. `email.split("@")` matnni `@` belgisi bo'yicha 2 qismga bo'ladi;
2. Birinchi qism `username` o'zgaruvchisiga olinadi;
3. `.upper()` metodi bilan login katta harf qilinadi;
4. Natija `f-string` orqali chop etiladi.

---

# 5. Foydalanuvchidan ma’lumot olish

```python
user_name = input("Ismingizni kiriting: ").strip().capitalize()
print("Salom,", user_name)
```

Foydalanuvchi kiritadi:

```text
Ismingizni kiriting:    ali
```

Natija:

```text
Salom, Ali
```

---

# 6. Ko‘p uchraydigan xatolar

## Xato 1: String indeksidan tashqariga chiqish (IndexError)

Noto‘g‘ri:

```python
word = "Py"
print(word[5])  # IndexError!
```

To‘g‘ri:

```python
word = "Py"
print(word[0])
```

---

# 7. Sinfdagi amaliy topshiriqlar

## 1-topshiriq — Oson

**Vazifa:** Kiritilgan matnning uzunligini `len()` yordamida aniqlang.

## 2-topshiriq — O‘rta

**Vazifa:** Matn berilgan: `"Python Dasturlash Tili"`. Undan `"Dasturlash"` so'zini slicing `[start:stop]` orqali kesib oling.

## 3-topshiriq — Murakkab

**Vazifa:** Kiritilgan so'zning palindrom (teskari o'qilganda ham bir xil, masalan "kiyik") ekanligini slicing `[::-1]` yordamida tekshiring.

---

# 8. Uyga vazifa

1. `4_dars_strings.py` faylini yarating;
2. Foydalanuvchi kiritgan matndagi barcha bo'sh joylarni `_` belgisi bilan almashtiring;
3. Kodni GitHub'ga saqlang.

---

# 9. Tekshirish savollari

1. `"Python"[1:4]` slicing natijasi nima bo'ladi?
2. `.strip()` metodi nima vazifa bajaradi?
3. Matnni teskari aylantirish uchun qaysi slicing ishlatiladi (`[::-1]`)?
4. Bu kodning natijasi qanday bo‘ladi?

```python
text = "Hello World"
print(text.split()[0])
```

5. `f-string` formatlash uslubining afzalligi nima?

---

# 10. Qisqa xulosa

Bu darsda:

- `Slicing va indekslar`;
- `String metodlari (.upper, .lower, .strip, .split)`;
- `f-string formatlash`

ni o‘rgandik.

Keyingi darsda: **If/elif/else**.

---

# Resurslar va fayllar

- 📄 Konspekt: `4_dars_konspekt.pdf`
- 💻 Kodlar: `github.com/dars-reja/4-dars`
- 🎬 Video: `youtube.com/watch?v=dars4`
- 📝 Qo‘shimcha mashqlar: `python.uz/mashq4`
""",
        "code": "email = 'user.name@gmail.com'\nusername = email.split('@')[0]\ndomain = email.split('@')[1]\nprint('User:', username.upper())\nprint('Domain:', domain)",
        "code_exp": "- `1-qator` — email o'zgaruvchisi;\n- `2-3 qatorlar` — split('@') orqali login va domen ajratiladi;\n- `4-qator` — upper() orqali katta harfga o'tkaziladi.",
        "quiz_q": "'Python'[1:4] slicing natijasi nima bo'ladi?",
        "quiz_opts": ["Pyt", "yth", "ytho", "Pyth"],
        "quiz_ans": 1,
        "quiz_exp": "Indeks 1, 2 va 3 olinadi ('y', 't', 'h') -> 'yth'."
    },

    5: {
        "title": "5-dars — If/elif/else",
        "content": """# 🔀 5. If/elif/else — Dars dokumentatsiyasi

`Shart operatorlari` — Python’da **ma'lum shartlarga ko'ra kodning har xil tarmoqlarda bajarilishini ta'minlash** uchun ishlatiladi.

Bu mavzu orqali:

- taqqoslash operatorlari (`==`, `!=`, `>`, `<`, `>=`, `<=`);
- `if`, `elif` va `else` bloklarini tuzish;
- Python'da joy tashlash (indentation — 4 ta probel) qoidalariga rioya qilish

mumkin.

---

## Dars maqsadi

Bu dars oxirida o‘quvchi:

- Murakkab tarmoqlanuvchi shartli algoritmlarni tuzish;
- Indentatsiya xatolarini (IndentationError) to'g'rilash;
- Baholash yoki chegirma hisoblash mantiqini yozish

ni mustaqil bajara oladi.

## Kerakli bilimlar

Bu darsni tushunish uchun:

- 3-dars: Input va arifmetika;
- Boolean (`True/False`) tushunchasi

bilinishi kerak.

---

# 1. Asosiy tushuncha

`if/elif/else` nima ekanini sodda tilda tushuntiramiz.

Masalan:

> `if` — agar shart bajarilsa koddagi ushbu blok ishlaydi. `elif` — qo'shimcha shart bo'lsa tekshiradi. `else` — birorta shart bajarilmasa ishlaydigan yakuniy blok.

Muhim qoida:

```python
# Har bir shartdan so'ng ikkita nuqta (:) qo'yiladi va 4 ta probel joy tashlanadi
if score >= 90:
    print("A'lo")
```

---

# 2. Birinchi sodda misol

```python
score = 85

if score >= 90:
    print("Baho: 5 (A'lo)")
elif score >= 70:
    print("Baho: 4 (Yaxshi)")
else:
    print("Baho: 3 (Qoniqarli)")
```

Natija:

```text
Baho: 4 (Yaxshi)
```

Izoh:

- `1-qator` — score 85 ga teng;
- `3-qator` — 85 >= 90 (False), keyingi elif tekshiriladi;
- `5-qator` — 85 >= 70 (True), shuning uchun 'Baho: 4 (Yaxshi)' chop etiladi.

---

# 3. Asosiy metodlar yoki operatorlar

| Operator | Vazifasi | Misol | Natija |
|---|---|---|---|
| `==` | Tengmi? | `5 == 5` | `True` |
| `!=` | Teng emasmi? | `5 != 3` | `True` |
| `>` | Kattami? | `7 > 10` | `False` |
| `<` | Kichikmi? | `4 < 9` | `True` |
| `>=` | Katta yoki tengmi? | `5 >= 5` | `True` |
| `<=` | Kichik yoki tengmi? | `3 <= 2` | `False` |

---

# 4. Batafsil misol — Kirish chiptasi narxi

```python
age = int(input("Yoshingizni kiriting: "))

if age < 7:
    price = 0
    status = "Bepul (Bolalar)"
elif age <= 18:
    price = 15000
    status = "Chegirma (O'quvchi)"
else:
    price = 30000
    status = "Katta yoshdagilar"

print(f"Toifa: {status} | Narxi: {price} so'm")
```

Natija:

```text
Yoshingizni kiriting: 15
Toifa: Chegirma (O'quvchi) | Narxi: 15000 so'm
```

---

# 5. Foydalanuvchidan ma’lumot olish

```python
num = float(input("Son kiriting: "))

if num > 0:
    print("Musbat son")
elif num < 0:
    print("Manfiy son")
else:
    print("Nolga teng")
```

Foydalanuvchi kiritadi:

```text
Son kiriting: -12.5
```

Natija:

```text
Manfiy son
```

---

# 6. Ko‘p uchraydigan xatolar

## Xato 1: Tenglikni tekshirish uchun '=' ishlatish

Noto‘g‘ri:

```python
if x = 5:  # SyntaxError!
    print("Teng")
```

To‘g‘ri:

```python
if x == 5:
    print("Teng")
```

Sabab: `=` qiymat biriktiradi, `==` esa tenglikni tekshiradi.

---

# 7. Sinfdagi amaliy topshiriqlar

## 1-topshiriq — Oson

**Vazifa:** Kiritilgan sonning juft yoki toq ekanligini `% 2 == 0` sharti bilan tekshiring.

## 2-topshiriq — O‘rta

**Vazifa:** Uchta kiritilgan son orasidan eng kattasini `if/elif/else` bilan toping.

## 3-topshiriq — Murakkab

**Vazifa:** Parolni tekshiruvchi dastur tuzing (Parol uzunligi kamida 8 ta belgi va "12345" ga teng bo'lmasligi kerak).

---

# 8. Uyga vazifa

1. `5_dars_conditions.py` faylini yarating;
2. Harorat kiritilganda unga mos tavsiya beruvchi dastur yozing (masalan <0 muzlama, 0-20 salqin, >20 issiq);
3. Kodni GitHub'ga saqlang.

---

# 9. Tekshirish savollari

1. `==` va `=` operatorlarining farqi nima?
2. `elif` bloki qachon bajariladi?
3. Python'da blok hosil qilish uchun nima ishlatiladi (indentatsiya)?
4. Bu kodning natijasi qanday bo‘ladi?

```python
x = 10
if x > 5:
    print("A")
elif x > 8:
    print("B")
```

5. Shart operatorlarining backend loyihalarida o'rni nimadan iborat?

---

# 10. Qisqa xulosa

Bu darsda:

- `if, elif, else bloklari`;
- `Taqqoslash operatorlari (==, !=, >, <, >=, <=)`;
- `Indentatsiya qoidasi`

ni o‘rgandik.

Keyingi darsda: **Mantiqiy operatorlar**.

---

# Resurslar va fayllar

- 📄 Konspekt: `5_dars_konspekt.pdf`
- 💻 Kodlar: `github.com/dars-reja/5-dars`
- 🎬 Video: `youtube.com/watch?v=dars5`
- 📝 Qo‘shimcha mashqlar: `python.uz/mashq5`
""",
        "code": "num = float(input('Son kiriting: '))\nif num > 0:\n    print('Musbat son')\nelif num < 0:\n    print('Manfiy son')\nelse:\n    print('Son nolga teng')",
        "code_exp": "- `1-qator` — Son float shaklida kiritiladi;\n- `2-6 qatorlar` — if/elif/else yordamida musbat, manfiy yoki 0 ekanligi tekshiriladi.",
        "quiz_q": "Python'da tenglikni tekshirish operatori qaysi?",
        "quiz_opts": ["=", "==", "===", "is"],
        "quiz_ans": 1,
        "quiz_exp": "== tenglikni tekshiradi, = esa qiymat biriktiradi."
    },

    6: {
        "title": "6-dars — Mantiqiy operatorlar",
        "content": """# ⚡ 6. Mantiqiy operatorlar — Dars dokumentatsiyasi

`Mantiqiy operatorlar (and, or, not)` — Python’da **bir nechta shartlarni birlashtirish va inkor etish** uchun ishlatiladi.

Bu mavzu orqali:

- `and` operatori (barcha shartlar True bo'lishi shart);
- `or` operatori (hech bo'lmaganda bitta shart True bo'lishi yetarli);
- `not` operatori (mantiqiy qiymatni teskarisiga o'g'irish)

mumkin.

---

## Dars maqsadi

Bu dars oxirida o‘quvchi:

- Bir nechta mantiqiy shartlarni `and` va `or` bilan birlashtirish;
- Tizimga kirish (Login & Password) tekshiruvini tuzish;
- `not` operatori yordamida holatni inkor qilish

ni mustaqil bajara oladi.

## Kerakli bilimlar

Bu darsni tushunish uchun:

- 5-dars: `if/elif/else` va taqqoslash operatorlari;
- Mantiqiy `True` va `False` tushunchasi

bilinishi kerak.

---

# 1. Asosiy tushuncha

`Mantiqiy operatorlar` nima ekanini sodda tilda tushuntiramiz.

Masalan:

> `and` — ikkala shart ham True bo'lsagina True beradi. `or` — kamida bittasi True bo'lsa True beradi. `not` — True bo'lsa False, False bo'lsa True qiladi.

Muhim qoida:

```python
if age >= 18 and has_passport:
    print("Ruxsat berildi")
```

---

# 2. Birinchi sodda misol

```python
age = 20
has_ticket = True

if age >= 18 and has_ticket:
    print("Konsertga kirish mumkin!")
else:
    print("Kirish mumkin emas.")
```

Natija:

```text
Konsertga kirish mumkin!
```

Izoh:

- `1-2 qatorlar` — age va has_ticket e'lon qilindi;
- `4-qator` — age >= 18 (True) AND has_ticket (True) -> Ikkalasi ham True bo'lgani uchun if bloki bajariladi.

---

# 3. Asosiy metodlar yoki operatorlar

| Operator | Nomi | Izoh | Misol | Natija |
|---|---|---|---|---|
| `and` | VA | Barcha shartlar True bo'lishi kerak | `True and False` | `False` |
| `or` | YOKI | Kamida bitta shart True bo'lsa yetarli | `True or False` | `True` |
| `not` | INKOR | Qiymatni teskarisiga o'zgartiradi | `not True` | `False` |

---

# 4. Batafsil misol — System Login Check

```python
input_user = input("Login: ")
input_pass = input("Parol: ")

correct_user = "admin"
correct_pass = "12345"

if input_user == correct_user and input_pass == correct_pass:
    print("Tizimga muvaffaqiyatli kirdingiz!")
else:
    print("Login yoki parol noto'g'ri!")
```

Natija:

```text
Login: admin
Parol: 12345
Tizimga muvaffaqiyatli kirdingiz!
```

---

# 6. Ko‘p uchraydigan xatolar

## Xato 1: Python'da '&&' va '||' ishlatishga urinish

Noto‘g‘ri:

```python
if x > 0 && y > 0:  # SyntaxError!
    print("Musbat")
```

To‘g‘ri:

```python
if x > 0 and y > 0:
    print("Musbat")
```

Sabab: Python'da `&&` va `||` o'rniga so'z ko'rinishidagi `and` va `or` ishlatiladi.

---

# 7. Sinfdagi amaliy topshiriqlar

## 1-topshiriq — Oson

**Vazifa:** Kiritilgan son 10 dan katta VA 50 dan kichik ekanligini `and` bilan tekshiring.

## 2-topshiriq — O‘rta

**Vazifa:** Foydalanuvchiga obuna (`is_subscribed`) yoki bonus (`has_bonus`) bo'lsa preumium kontentni ko'rsatuvchi dastur tuzing (`or`).

## 3-topshiriq — Murakkab

**Vazifa:** Yil kabisa yili (Leap year) ekanligini tekshiruvchi algoritm yozing (`(year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)`).

---

# 8. Uyga vazifa

1. `6_dars_logical.py` faylini yarating;
2. Imtihondan o'tish shartini yozing: Ball kamida 60 bo'lishi va davomat 80% dan yuqori bo'lishi kerak;
3. Kodni GitHub'ga saqlang.

---

# 9. Tekshirish savollari

1. `and` va `or` ning asosiy farqi nima?
2. `not (5 > 3)` kodi nimani qaytaradi (`False`)?
3. Python'da mantiqiy `&&` bormi?
4. Bu kodning natijasi qanday bo‘ladi?

```python
a = True
b = False
print(a or b and not a)
```

5. Backend autentifikatsiyada mantiqiy operatorlar qanday ishlatiladi?

---

# 10. Qisqa xulosa

Bu darsda:

- `and operatori`;
- `or operatori`;
- `not inkor operatori`

ni o‘rgandik.

Keyingi darsda: **For sikli**.

---

# Resurslar va fayllar

- 📄 Konspekt: `6_dars_konspekt.pdf`
- 💻 Kodlar: `github.com/dars-reja/6-dars`
- 🎬 Video: `youtube.com/watch?v=dars6`
- 📝 Qo‘shimcha mashqlar: `python.uz/mashq6`
""",
        "code": "age = 22\nhas_license = True\nif age >= 18 and has_license:\n    print('Avtomobil boshqarishga ruxsat bor')\nelse:\n    print('Ruxsat yo\\'q')",
        "code_exp": "- `1-2 qatorlar` — Yosh va litsenziya holati saqlanadi;\n- `3-6 qatorlar` — and operatori ikkala shart ham True bo'lgandagina if ga kiradi.",
        "quiz_q": "Ikkala shart ham True bo'lsagina True qaytaruvchi mantiqiy operator qaysi?",
        "quiz_opts": ["or", "and", "not", "xor"],
        "quiz_ans": 1,
        "quiz_exp": "and operatori barcha mantiqiy shartlar True bo'lgandagina True qaytaradi."
    },

    7: {
        "title": "7-dars — For sikli",
        "content": """# 🔄 7. For sikli — Dars dokumentatsiyasi

`For sikli` — Python’da **to'plamlar (ro'yxat, matn) va `range()` diapazoni bo'ylab kodni ko'p marotaba takrorlash** uchun ishlatiladi.

Bu mavzu orqali:

- `for element in collection` orqali elementlarni birma-bir ko'rib chiqish;
- `range(start, stop, step)` funksiyasidan foydalanish;
- matn va ro'yxat bo'ylab takrorlanish amallarini bajarish

mumkin.

---

## Dars maqsadi

Bu dars oxirida o‘quvchi:

- `range()` yordamida berilgan oraliqdagi sonlarni chiqarish;
- Ro'yxat elementlarini for sikli yordamida qayta ishlash;
- Sikl ichida yig'indi va ko'paytmalarni hisoblash

ni mustaqil bajara oladi.

## Kerakli bilimlar

Bu darsni tushunish uchun:

- 4-dars: Stringlar va ketma-ketliklar;
- 5-dars: Indentatsiya (joy tashlash)

bilinishi kerak.

---

# 1. Asosiy tushuncha

`For sikli` nima ekanini sodda tilda tushuntiramiz.

Masalan:

> `For sikli` — belgilangan takrorlanishlar soni bo'yicha kod qismini qayta-qayta bajaruvchi tsikldir.

Muhim qoida:

```python
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4
```

---

# 2. Birinchi sodda misol

```python
fruits = ["olma", "banan", "uzum"]

for fruit in fruits:
    print("Meva:", fruit.capitalize())
```

Natija:

```text
Meva: Olma
Meva: Banan
Meva: Uzum
```

Izoh:

- `1-qator` — Mevalar ro'yxati shakllantirildi;
- `3-qator` — `for fruit in fruits` har bir meva nomini navbatma-navbat `fruit` o'zgaruvchisiga oladi va chop etadi.

---

# 3. Asosiy metodlar yoki operatorlar

| Kod / metod | Vazifasi | Misol | Natija |
|---|---|---|---|
| `range(stop)` | 0 dan stop-1 gacha | `range(3)` | `0, 1, 2` |
| `range(start, stop)` | start dan stop-1 gacha | `range(1, 4)` | `1, 2, 3` |
| `range(start, stop, step)` | qadam bilan sonlar | `range(0, 10, 2)` | `0, 2, 4, 6, 8` |

---

# 4. Batafsil misol — Yig'indini hisoblash

```python
total_sum = 0

for num in range(1, 11):
    total_sum += num

print("1 dan 10 gacha sonlar yig'indisi:", total_sum)
```

Natija:

```text
1 dan 10 gacha sonlar yig'indisi: 55
```

Kod qanday ishlaydi:

1. `total_sum` 0 ga tenglashtiriladi;
2. `range(1, 11)` 1 dan 10 gacha bo'lgan sonlarni beradi;
3. Har bir takrorlanishda son `total_sum` ga qo'shib boriladi (`+=`);
4. Yakuniy yig'indi 55 chop etiladi.

---

# 6. Ko‘p uchraydigan xatolar

## Xato 1: range(stop) da oxirgi son kirmasligini unutish

Noto‘g‘ri:

```python
# 1 dan 5 gacha demoqchimiz
for i in range(1, 5):
    print(i)  # Faqat 1, 2, 3, 4 chiqadi!
```

To‘g‘ri:

```python
for i in range(1, 6):
    print(i)  # 1, 2, 3, 4, 5 chiqadi
```

---

# 7. Sinfdagi amaliy topshiriqlar

## 1-topshiriq — Oson

**Vazifa:** `range()` yordamida 1 dan 20 gacha bo'lgan juft sonlarni ekranga chiqaring.

## 2-topshiriq — O‘rta

**Vazifa:** Kiritilgan sonning ko'paytirish jadvalini `for` sikli yordamida tuzing (masalan 5 x 1 = 5 ... 5 x 10 = 50).

## 3-topshiriq — Murakkab

**Vazifa:** Matn berilgan: `"Python Backend"`. Undagi unli harflar sonini `for` va `if` yordamida hisoblang.

---

# 8. Uyga vazifa

1. `7_dars_for_loop.py` faylini yarating;
2. 1 dan 100 gacha bo'lgan sonlar orasidan 3 ga va 5 ga qoldiqsiz bo'linadiganlarini topuvchi dastur yozing;
3. Kodni GitHub'ga saqlang.

---

# 9. Tekshirish savollari

1. `range(1, 10, 2)` kodi qanday sonlarni beradi?
2. `for` sikli qachon to'xtaydi?
3. String bo'ylab `for` siklini yurish mumkinmi?
4. Bu kodning natijasi qanday bo‘ladi?

```python
for i in range(3):
    print("A", end="")
```

5. Backend loyihalarida `for` sikli qayerlarda qo'llaniladi?

---

# 10. Qisqa xulosa

Bu darsda:

- `for sikli sintaksisi`;
- `range() funksiyasi va parametrlari`;
- `Ro'yxat va matn bo'ylab takrorlanish`

ni o‘rgandik.

Keyingi darsda: **While sikli**.

---

# Resurslar va fayllar

- 📄 Konspekt: `7_dars_konspekt.pdf`
- 💻 Kodlar: `github.com/dars-reja/7-dars`
- 🎬 Video: `youtube.com/watch?v=dars7`
- 📝 Qo‘shimcha mashqlar: `python.uz/mashq7`
""",
        "code": "fruits = ['olma', 'banan', 'uzum']\nfor fruit in fruits:\n    print('Meva:', fruit.capitalize())\n\nfor i in range(1, 6):\n    print('Sanoq:', i)",
        "code_exp": "- `1-3 qatorlar` — for sikli ro'yxat bo'ylab takrorlanadi;\n- `5-6 qatorlar` — range(1, 6) orqali 1 dan 5 gacha sonlar chop etiladi.",
        "quiz_q": "range(1, 5) diapazonida qaysi sonlar hosil bo'ladi?",
        "quiz_opts": ["1, 2, 3, 4, 5", "1, 2, 3, 4", "0, 1, 2, 3, 4", "2, 3, 4, 5"],
        "quiz_ans": 1,
        "quiz_exp": "range(1, 5) 1 dan boshlab 5 ga etmasdan to'xtaydi: 1, 2, 3, 4."
    },

    8: {
        "title": "8-dars — While sikli",
        "content": """# 🔁 8. While sikli — Dars dokumentatsiyasi

`While sikli` — Python’da **ma'lum bir shart True (to'g'ri) bo'lib turgan muddatda kodni cheksiz takrorlash** uchun ishlatiladi.

Bu mavzu orqali:

- `while condition:` takrorlanish strukturasi;
- hisoblagich (counter) yordamida siklni boshqarish;
- cheksiz sikllarning (infinite loop) oldini olish

mumkin.

---

## Dars maqsadi

Bu dars oxirida o‘quvchi:

- `while` sikli yordamida shartga ko'ra qayta ishlovchi dasturlar tuzish;
- Foydalanuvchi to'g'ri ma'lumot kiritguncha qayta so'rash logikasini yozish;
- Cheksiz sikl xatolarini tuzatish

ni mustaqil bajara oladi.

## Kerakli bilimlar

Bu darsni tushunish uchun:

- 5-dars: Shart operatorlari (`if`);
- O'zgaruvchini oshirib borish (`count += 1`)

bilinishi kerak.

---

# 1. Asosiy tushuncha

`While sikli` nima ekanini sodda tilda tushuntiramiz.

Masalan:

> `While sikli` — tokim berilgan mantiqiy shart bajarilyotgan ekan, o'z blokidagi kodni takrorlayveradi.

Muhim qoida:

```python
count = 1
while count <= 5:
    print(count)
    count += 1  # Hisoblagichni oshirish shart, aks holda cheksiz sikl bo'ladi!
```

---

# 2. Birinchi sodda misol

```python
i = 1

while i <= 3:
    print("Takrorlanish:", i)
    i += 1

print("Sikl tugadi!")
```

Natija:

```text
Takrorlanish: 1
Takrorlanish: 2
Takrorlanish: 3
Sikl tugadi!
```

Izoh:

- `1-qator` — i = 1 hisoblagich;
- `3-qator` — i <= 3 bo'lguncha sikl ishlaydi;
- `5-qator` — har bir qadamda `i += 1` oshiriladi.

---

# 4. Batafsil misol — To'g'ri Parol Kiritish

```python
password = ""

while password != "python123":
    password = input("Parolni kiriting: ")
    if password != "python123":
        print("Noto'g'ri parol, qayta urinib ko'ring!")

print("Muvaffaqiyatli kirdingiz!")
```

Natija:

```text
Parolni kiriting: 123
Noto'g'ri parol, qayta urinib ko'ring!
Parolni kiriting: python123
Muvaffaqiyatli kirdingiz!
```

---

# 6. Ko‘p uchraydigan xatolar

## Xato 1: Hisoblagichni oshirishni unutish (Cheksiz sikl)

Noto‘g‘ri:

```python
i = 1
while i <= 5:
    print(i)
    # i kottaymayapti -> Cheksiz sikl!
```

To‘g‘ri:

```python
i = 1
while i <= 5:
    print(i)
    i += 1
```

---

# 7. Sinfdagi amaliy topshiriqlar

## 1-topshiriq — Oson

**Vazifa:** `while` sikli yordamida 10 dan 1 gacha bo'lgan sonlarni teskari tartibda chiqaring.

## 2-topshiriq — O‘rta

**Vazifa:** Foydalanuvchi `0` kiritguncha kiritilgan barcha sonlarni yig'ib boruvchi dastur tuzing.

---

# 8. Uyga vazifa

1. `8_dars_while_loop.py` faylini yarating;
2. O'yin tuzing: Kompyuter 7 sonini o'ylaydi, foydalanuvchi topguncha `while` orqali kiritishni so'raydi;
3. Kodni GitHub'ga saqlang.

---

# 9. Tekshirish savollari

1. `while` va `for` sikllarining asosiy farqi nima?
2. Cheksiz sikl (infinite loop) nega kelib chiqadi?
3. `while True:` sintaksisi nimani anglatadi?

---

# 10. Qisqa xulosa

Bu darsda:

- `while sikli shartlari`;
- `Hisoblagichlar bilan ishlash`;
- `Cheksiz sikllardan qochish`

ni o‘rgandik.

Keyingi darsda: **Break, continue va random**.

---

# Resurslar va fayllar

- 📄 Konspekt: `8_dars_konspekt.pdf`
- 💻 Kodlar: `github.com/dars-reja/8-dars`
- 🎬 Video: `youtube.com/watch?v=dars8`
- 📝 Qo‘shimcha mashqlar: `python.uz/mashq8`
""",
        "code": "count = 1\nwhile count <= 5:\n    print('Takrorlanish:', count)\n    count += 1\nprint('Sikl tugadi')",
        "code_exp": "- `1-qator` — Hisoblagich 1 ga tenglashtiriladi;\n- `2-4 qatorlar` — while sharti True bo'lguncha bajariladi va count oshiriladi.",
        "quiz_q": "while siklida cheksiz takrorlanish kelib chiqishiga nima sabab bo'ladi?",
        "quiz_opts": ["Shart hech qachon False bo'lmasligi", "for ishlatilmagani", "print bo'lmagani", "SyntaxError"],
        "quiz_ans": 0,
        "quiz_exp": "Sikl sharti doimo True bo'lib qolsa, u cheksiz davom etadi."
    },

    9: {
        "title": "9-dars — Break, continue va random",
        "desc": "break (siklni to'xtatish), continue (keyingi qadamga o'tish) hamda random moduli.",
        "content": """# 🎲 9. Break, continue va random — Dars dokumentatsiyasi

`break`, `continue` va `random` — Python’da **sikllar oqimini boshqarish va tasodifiy sonlar shakllantirish** uchun ishlatiladi.

Bu mavzu orqali:

- `break` yordamida siklni muddatidan oldin to'xtatish;
- `continue` yordamida joriy qadamni o'tkazib yuborish;
- `random.randint()` va `random.choice()` bilan tasodifiy qiymatlar olish

mumkin.

---

## Dars maqsadi

Bu dars oxirida o‘quvchi:

- Sikl jarayonida kerakli shart bajarilganda `break` bilan to'xtatish;
- Keraksiz elementlarni `continue` yordamida o'tkazib yuborish;
- `random` modulidan foydalanib o'yinlar va kodlar yaratish

ni mustaqil bajara oladi.

---

# 1. Asosiy tushuncha

```python
import random

secret = random.randint(1, 10)

for i in range(1, 11):
    if i == secret:
        print("Topildi:", i)
        break  # Sikl shu joyda to'xtaydi!
```

---

# 3. Buyruqlar Jadvali

| Buyruq / Metod | Vazifasi | Misol |
|---|---|---|
| `break` | Siklni darhol to'xtatib chiqib ketish | `if x == 5: break` |
| `continue` | Joriy takrorlanishni o'tkazib keyingisiga o'tish | `if x % 2 == 0: continue` |
| `random.randint(a, b)` | a va b oralig'ida tasodifiy butun son | `random.randint(1, 6)` |
| `random.choice(seq)` | Ro'yxatdan tasodifiy element tanlash | `random.choice(["olma", "banan"])` |

---

# 9. Tekshirish savollari

1. `break` va `continue` ning asosiy farqi nima?
2. `random.randint(1, 5)` ga 5 soni kiradimi?
3. `continue` kalit so'zidan so'ng turgan kodlar bajariladimi?

---

# 10. Qisqa xulosa

Bu darsda: `break`, `continue` va `random` modulini o'rgandik.
Keyingi darsda: **Ichma-ich sikl va algoritmlar**.
""",
        "code": "import random\nsecret_number = random.randint(1, 10)\nfor i in range(1, 6):\n    if i == secret_number:\n        print('Sirli son topildi:', i)\n        break\n    else:\n        continue",
        "code_exp": "- `1-2 qatorlar` — random modulidan 1 dan 10 gacha tasodifiy son olinadi;\n- `4-7 qatorlar` — break siklni to'xtatadi, continue keyingi takrorlanishga o'tkazadi.",
        "quiz_q": "Siklni muddatidan oldin to'liq to'xtatuvchi buyruq qaysi?",
        "quiz_opts": ["continue", "pass", "break", "stop"],
        "quiz_ans": 2,
        "quiz_exp": "break buyrug'i sikl bajarilishini darhol to'xtatadi va undan chiqadi."
    },

    10: {
        "title": "10-dars — Ichma-ich sikl va algoritmlar",
        "content": """# 🧩 10. Ichma-ich sikl va algoritmlar — Dars dokumentatsiyasi

`Ichma-ich sikllar (Nested loops)` — Python’da **matritsalar, jadval ko'rinishidagi ma'lumotlar va murakkab algoritmlarni yechish** uchun ishlatiladi.

Bu mavzu orqali:

- sikl ichida boshqa sikl yuritish (`nested for loops`);
- ko'paytirish jadvalini shakllantirish;
- tub sonlarni topish kabi bazaviy algoritmlarni yozish

mumkin.

---

# 1. Asosiy tushuncha

```python
# Ko'paytirish jadvali
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i*j}", end=" | ")
    print()
```

Natija:

```text
1 x 1 = 1 | 1 x 2 = 2 | 1 x 3 = 3 | 
2 x 1 = 2 | 2 x 2 = 4 | 2 x 3 = 6 | 
3 x 1 = 3 | 3 x 2 = 6 | 3 x 3 = 9 | 
```
""",
        "code": "for i in range(1, 4):\n    for j in range(1, 4):\n        print(f'{i}x{j}={i*j}', end=' ')\n    print()",
        "code_exp": "- `1-2 qatorlar` — Tashqi va ichki for sikllari;\n- `3-4 qatorlar` — Har bir qator uchun elementlar chop etiladi.",
        "quiz_q": "Tashqi sikl 3 marta, ichki sikl 4 marta aylansa, ichki kod necha marta bajariladi?",
        "quiz_opts": ["7 marta", "12 marta", "4 marta", "3 marta"],
        "quiz_ans": 1,
        "quiz_exp": "Jami takrorlanishlar soni: 3 * 4 = 12 marta bo'ladi."
    },

    11: {
        "title": "11-dars — List asoslari",
        "content": """# 📋 11. List asoslari — Dars dokumentatsiyasi

`List (Ro'yxat)` — Python’da **bir nechta ma'lumotlarni bitta o'zgaruvchida tartiblangan va o'zgaruvchan shaklda saqlash** uchun ishlatiladi.

Bu mavzu orqali:

- ro'yxat yaratish va indeks bo'yicha murojaat qilish;
- ro'yxatga element qo'shish (`.append()`, `.insert()`);
- elementlarni o'chirish (`.pop()`, `.remove()`);
- saralash (`.sort()`, `.reverse()`) va `len()` funksiyasi

mumkin.

---

# 1. Asosiy tushuncha

```python
fruits = ["olma", "banan", "uzum"]
fruits.append("behi")
print("Barcha mevalar:", fruits)
print("Birinchi meva:", fruits[0])
```

Natija:

```text
Barcha mevalar: ['olma', 'banan', 'uzum', 'behi']
Birinchi meva: olma
```
""",
        "code": "numbers = [45, 12, 89, 3, 27]\nnumbers.append(100)\nnumbers.sort()\nprint('Saralangan ro\\'yxat:', numbers)\nprint('Eng katta element:', numbers[-1])",
        "code_exp": "- `1-qator` — Sonlar ro'yxati;\n- `2-qator` — append() oxiriga 100 qo'shadi;\n- `3-qator` — sort() kichikdan kattaga saralaydi.",
        "quiz_q": "Ro'yxatning eng oxiriga yangi element qo'shuvchi metod qaysi?",
        "quiz_opts": ["add()", "push()", "append()", "insert()"],
        "quiz_ans": 2,
        "quiz_exp": "append() metodi yangi elementni ro'yxat oxiriga qo'shadi."
    },

    12: {
        "title": "12-dars — 1-modul imtihoni",
        "content": """# 🎓 12. 1-modul imtihoni — Dars dokumentatsiyasi

`1-modul imtihoni` — 1-darsdan 11-darsgacha o'rganilgan **Python asoslari, o'zgaruvchilar, arifmetika, stringlar, shartlar, sikllar va ro'yxat ko'nikmalarini sinash** uchun o'tkaziladi.

---

## Imtihon Tartibi (100 ballik shkala)

- **Nazariy Testlar (20 ball)**: 1-11 darslar bo'yicha testlar;
- **Amaliy Masalalar (50 ball)**: 3 ta algoritmik kod yozish topshirig'i;
- **PEP8 Standart va Kod Sifati (20 ball)**: Izohlar va to'g'ri nomlash;
- **Vaqt va Intizom (10 ball)**: 2 soat ichida topshirish.

---

# 1. Imtihon Kod Shabloni

```python
def main_exam_solution():
    print("=== 1-MODUL IMTIHONI KODI BAJARILMOQDA ===")

main_exam_solution()
```
""",
        "code": "def exam_solution():\n    print('1-Modul Imtihon topshirig\\'i bajarildi.')\n\nexam_solution()",
        "code_exp": "- `1-3 qatorlar` — 1-modul imtihon topshirig'i bajarilish funksiyasi va chaqirilishi.",
        "quiz_q": "Imtihondagi maksimal ball nechaga teng?",
        "quiz_opts": ["50 ball", "80 ball", "100 ball", "120 ball"],
        "quiz_ans": 2,
        "quiz_exp": "Imtihon 100 ballik shkala bo'yicha baholanadi."
    }
}

def update_only_1_to_12():
    print("==================================================================")
    print("🚀 1-DARSDAN 12-DARSGACHA BO'LGAN HUJJATLAR TASHXIS QILINMOQDA VA TO'G'RILANMOQDA...")
    print("==================================================================")

    # 1. Mavjud bazadagi darslarni olish
    all_lessons = list(Lesson.objects.all().order_by('lesson_number'))
    
    # 2. 1 dan 12 gacha bo'lgan darslarni foydalanuvchi shablonida almashtirish
    for num in range(1, 13):
        item_data = EXACT_1_TO_12_LESSONS[num]
        
        # Baza obyektini izlaymiz
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
            {"id": f"res-{num}-2", "studentName": "Sardor Karimov", "score": 90, "passed": True, "notes": "Topshiriq to'liq bajarildi"}
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

    # 3. JSON faylni yangilash (13-72 larga tegmasdan, faqat 1-12 larni yangilaymiz)
    with open(LESSONS_JSON, "r", encoding="utf-8") as f:
        json_data = json.load(f)

    for item in json_data:
        num = item.get("lessonNumber")
        if num in EXACT_1_TO_12_LESSONS:
            ex = EXACT_1_TO_12_LESSONS[num]
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
    print("✨ 1-DARSDAN 12-DARSGACHA BO'LGAN DARSLAR SHABLON BO'YICHA TO'G'RILANDI!")
    print("==================================================================")

if __name__ == "__main__":
    update_only_1_to_12()
