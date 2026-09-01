#!/usr/bin/env python3
"""Generate lesson docs 7-12."""
import os

DOCS_DIR = os.path.join(os.path.dirname(__file__), "lesson_docs")

lessons = {}

lessons[7] = """# 🔁 7. For sikli — Dars dokumentatsiyasi

`for` sikli — Python'da ketma-ketlik (string, list, tuple, range) elementlarini birma-bir takrorlash uchun ishlatiladigan boshqaruv strukturasi. U ma'lum bir amalni har bir element uchun bajaradi.

`for` sikli eng ko'p ishlatiladigan sikl turi bo'lib, u `range()` funksiyasi bilan birgalikda muayyan sondagi takrorlashlarni ham bajarishi mumkin. Masalan, 1 dan 100 gacha bo'lgan sonlarni chiqarish, list elementlarini birma-bir qayta ishlash yoki matn harflarini sanash.

`for` sikli ichida `if` shartlari, boshqa sikllar va funksiyalar ham ishlatilishi mumkin — bu murakkab algoritmlarning asosini tashkil etadi.

---

## Bu mavzu orqali nimalar qilish mumkin

- Ketma-ketlik elementlarini birma-bir takrorlash;
- `range()` funksiyasi bilan muayyan son marta takrorlash;
- String, list, tuple elementlari ustida ishlash;
- Yig'indi, ko'paytma, sanash kabi hisob-kitoblar;
- `enumerate()` bilan indeks olish.

---

## Dars maqsadi

Bu dars oxirida o'quvchi:

- `for` siklini to'g'ri yozish;
- `range()` funksiyasining 3 ta shaklini bilish;
- String va list elementlarini sikl bilan qayta ishlash;
- `enumerate()` dan foydalanish;
- Yig'indi va sanash algoritmlarini yozish

ni mustaqil bajara oladi.

---

## Kerakli oldingi bilimlar

- 2-dars: O'zgaruvchilar;
- 4-dars: Stringlar;
- 5-dars: If/elif/else.

---

# 1. Asosiy tushunchalar

## for sikli nima?

> **`for`** — ketma-ketlikdagi har bir element uchun kod blokini bajaradigan sikl. `for x in ketmaketlik:` sintaksisida yoziladi.

## range() nima?

> **`range()`** — muayyan oraliqda sonlar ketma-ketligini yaratadi. 3 ta ko'rinishi bor: `range(n)`, `range(start, stop)`, `range(start, stop, step)`.

## enumerate() nima?

> **`enumerate()`** — siklda har bir elementning indeksini ham olish imkonini beradi: `for i, x in enumerate(list):`.

## Iteratsiya nima?

> **Iteratsiya** — siklning bitta takrorlanishi. 5 ta element bo'lsa, 5 ta iteratsiya bo'ladi.

---

# 2. Sintaksis

```python
for ozgaruvchi in ketmaketlik:
    # har bir element uchun bajariladigan kod
```

---

# 3. range() funksiyasi jadvali

| Shakli | Vazifasi | Misol | Natija |
|---|---|---|---|
| `range(n)` | 0 dan n gacha (n kirmaydi) | `range(5)` | `0, 1, 2, 3, 4` |
| `range(start, stop)` | start dan stop gacha | `range(2, 6)` | `2, 3, 4, 5` |
| `range(start, stop, step)` | qadam bilan | `range(0, 10, 2)` | `0, 2, 4, 6, 8` |
| `range(10, 0, -1)` | teskari tartibda | `range(5, 0, -1)` | `5, 4, 3, 2, 1` |

---

# 4. Kod misollari

## Misol 1 — Sodda for

```python
for i in range(5):
    print(i)
```

Natija:

```
0
1
2
3
4
```

---

## Misol 2 — range(start, stop)

```python
for i in range(1, 6):
    print(f"{i} x {i} = {i * i}")
```

Natija:

```
1 x 1 = 1
2 x 2 = 4
3 x 3 = 9
4 x 4 = 16
5 x 5 = 25
```

---

## Misol 3 — String harflarini takrorlash

```python
matn = "Python"
for harf in matn:
    print(harf, end=" ")
```

Natija: `P y t h o n`

---

## Misol 4 — List elementlarini takrorlash

```python
mevalar = ["olma", "banan", "uzum", "anor"]
for meva in mevalar:
    print(f"Men {meva} yaxshi ko'raman.")
```

---

## Misol 5 — Yig'indi hisoblash

```python
sonlar = [10, 20, 30, 40, 50]
yigindi = 0

for son in sonlar:
    yigindi += son

print(f"Yig'indi: {yigindi}")
```

Natija: `Yig'indi: 150`

---

## Misol 6 — enumerate()

```python
talabalar = ["Ali", "Vali", "Sardor"]

for i, talaba in enumerate(talabalar, start=1):
    print(f"{i}. {talaba}")
```

Natija:

```
1. Ali
2. Vali
3. Sardor
```

---

## Misol 7 — range(start, stop, step)

```python
print("Juft sonlar (0-20):")
for i in range(0, 21, 2):
    print(i, end=" ")
```

Natija: `0 2 4 6 8 10 12 14 16 18 20`

---

## Misol 8 — Teskari hisoblash

```python
print("Teskari hisoblash:")
for i in range(10, 0, -1):
    print(i, end=" ")
print("Start!")
```

Natija: `10 9 8 7 6 5 4 3 2 1 Start!`

---

# 5. Real loyiha misoli — Baholar tahlili

```python
baholar = [85, 92, 78, 95, 67, 88, 73, 91]

eng_yuqori = baholar[0]
eng_past = baholar[0]
yigindi = 0

for baho in baholar:
    yigindi += baho
    if baho > eng_yuqori:
        eng_yuqori = baho
    if baho < eng_past:
        eng_past = baho

ortacha = yigindi / len(baholar)

print(f"Talabalar soni: {len(baholar)}")
print(f"Eng yuqori:     {eng_yuqori}")
print(f"Eng past:       {eng_past}")
print(f"O'rtacha:       {ortacha:.1f}")
```

---

# 6. Ko'p uchraydigan xatolar

## Xato 1: range() oxirgi sonni kiritmaydi

```python
for i in range(1, 5):
    print(i)
```

Natija: `1, 2, 3, 4` (5 chiqmaydi!). `range(1, 6)` kerak.

## Xato 2: Sikl o'zgaruvchisini o'zgartirish

```python
for i in range(5):
    i = i * 2
    print(i)
```

Izoh: `i` ni o'zgartirish keyingi iteratsiyaga ta'sir qilmaydi. `range` o'z ketma-ketligini davom ettiradi.

## Xato 3: Bo'sh sikl tanasi

```python
for i in range(5):
# hech narsa yozilmagan — IndentationError
```

To'g'ri: `pass` ishlatish:

```python
for i in range(5):
    pass
```

## Xato 4: Siklda listni o'zgartirish

```python
sonlar = [1, 2, 3, 4, 5]
for son in sonlar:
    if son % 2 == 0:
        sonlar.remove(son)
```

Nima uchun xato: Sikl davomida listni o'zgartirish elementlarni o'tkazib yuboradi. Buning o'rniga yangi list yarating.

---

# 7. Sinfdagi amaliy topshiriqlar

## 1-topshiriq — Oson

**Vazifa:** 1 dan 20 gacha bo'lgan sonlarni chiqaring.

## 2-topshiriq — O'rta

**Vazifa:** Foydalanuvchidan son oling va uning ko'paytirish jadvalini chiqaring (1 dan 10 gacha).

## 3-topshiriq — Murakkab

**Vazifa:** Foydalanuvchidan n ta son oling (n ni ham foydalanuvchi kiritadi), eng katta, eng kichik va o'rtacha qiymatni toping.

---

# 8. Uyga vazifa

1. 1 dan 100 gacha bo'lgan juft sonlarning yig'indisini hisoblang.
2. Foydalanuvchidan so'z oling va teskari tartibda chiqaring (sikldan foydalaning, [::-1] ishlatmang).
3. Foydalanuvchidan 5 ta talaba ismini oling, har birini raqamlang.
4. Factorial hisoblang: n! = 1 * 2 * 3 * ... * n.
5. Fibonachchi sonlarining birinchi 20 tasini chiqaring.

---

# 9. Tekshirish savollari

1. `for` siklining vazifasi nima?
2. `range(5)` qanday sonlarni hosil qiladi?
3. `range(2, 8, 2)` natijasi nima?
4. `enumerate()` nima uchun ishlatiladi?
5. `for` sikli stringda qanday ishlaydi?
6. `for` va `while` sikllarining farqi nima?
7. `range()` ning 3 ta shakli qanday?
8. Sikl ichida listni o'zgartirish nima uchun xavfli?
9. `pass` kalit so'zi siklda nima uchun ishlatiladi?
10. Teskari tartibda hisoblash uchun range() ga qanday argument berish kerak?

---

## Javoblar

**1.** `for` sikli ketma-ketlik elementlarini birma-bir takrorlash uchun ishlatiladi. Har bir element uchun kod bloki bajariladi.

**2.** `range(5)` = `0, 1, 2, 3, 4`. 0 dan boshlanadi, 5 kirmaydi.

**3.** `range(2, 8, 2)` = `2, 4, 6`. 2 dan 8 gacha, 2 qadam bilan.

**4.** `enumerate()` siklda har bir elementning indeksini ham olish imkonini beradi: `for i, x in enumerate(list):`.

**5.** String har bir belgini alohida iteratsiya qiladi: `for harf in "Python":` — `P`, `y`, `t`, `h`, `o`, `n`.

**6.** `for` — takrorlash soni oldindan ma'lum. `while` — shart bajarilguncha davom etadi, soni oldindan noma'lum bo'lishi mumkin.

**7.** `range(n)` — 0 dan n gacha; `range(start, stop)` — start dan stop gacha; `range(start, stop, step)` — qadam bilan.

**8.** Sikl davomida list o'zgarsa, indekslar siljiydi va ba'zi elementlar o'tkazib yuboriladi. Buning o'rniga yangi list yaratish kerak.

**9.** `pass` — bo'sh blok uchun ishlatiladi. Python bo'sh blokka ruxsat bermaydi, `pass` esa hech narsa qilmaydi.

**10.** `range(10, 0, -1)` = `10, 9, 8, ..., 1`. Uchinchi argument manfiy qadam.

---

# 10. Qisqa xulosa

Bu darsda:

- `for` sikli va iteratsiya;
- `range()` funksiyasining 3 ta shakli;
- String va list elementlarini takrorlash;
- `enumerate()` bilan indeksli takrorlash;
- Yig'indi va sanash algoritmlari

o'rganildi.

---

Keyingi **8-dars: While sikli** da shartga asoslangan takrorlash, cheksiz sikllar va menyu tizimi o'rganiladi.

---

# Resurslar va fayllar

- 📄 Python for: https://docs.python.org/3/tutorial/controlflow.html#for-statements
- 📄 range(): https://docs.python.org/3/library/functions.html#func-range
- 💻 Kodlar: `github.com/dars-reja/07-dars`
- 🎬 Video dars: `youtube.com/watch?v=dars07`
"""

lessons[8] = """# 🔄 8. While sikli — Dars dokumentatsiyasi

`while` sikli — shart `True` bo'lguncha kodni qayta-qayta bajaradigan boshqaruv strukturasi. `for` siklidan farqli o'laroq, `while` siklida takrorlash soni oldindan ma'lum bo'lishi shart emas — shart bajarilguncha davom etadi.

`while` sikli login tizimlarida (parol to'g'ri kiritilguncha so'rash), o'yinlarda (o'yin tugaguncha davom ettirish), real-time dasturlarda (server doim ishlashi kerak) va menyu tizimlarida (foydalanuvchi chiqishni tanlaguncha) keng qo'llaniladi.

Eng muhim qoida: `while` sikli ichida shart o'zgarishi kerak, aks holda cheksiz sikl (infinite loop) hosil bo'ladi va dastur to'xtamaydi.

---

## Bu mavzu orqali nimalar qilish mumkin

- Shartga asoslangan takrorlash;
- Hisoblagich (counter) bilan ishlash;
- Foydalanuvchi kiritishini kutuvchi sikllar;
- Menyu tizimi yaratish;
- while/else strukturasi.

---

## Dars maqsadi

Bu dars oxirida o'quvchi:

- `while` siklini to'g'ri yozish;
- Cheksiz sikllarni aniqlash va oldini olish;
- Hisoblagich bilan boshqariladigan sikllar;
- while/else strukturasini tushunish;
- Menyu tizimi yozish

ni mustaqil bajara oladi.

---

## Kerakli oldingi bilimlar

- 5-dars: If/elif/else;
- 7-dars: For sikli.

---

# 1. Asosiy tushunchalar

## while sikli nima?

> **`while`** — shart `True` bo'lguncha kod blokini qayta-qayta bajaradi. Shart `False` bo'lganda sikl to'xtaydi.

## Cheksiz sikl (Infinite Loop) nima?

> **Cheksiz sikl** — shart hech qachon `False` bo'lmaydigan sikl. Dastur to'xtamaydi va `Ctrl+C` bilan to'xtatish kerak.

## Hisoblagich nima?

> **Hisoblagich (counter)** — siklda iteratsiyalar sonini kuzatuvchi o'zgaruvchi. Har iteratsiyada qiymati o'zgaradi.

---

# 2. Sintaksis

```python
while shart:
    # shart True bo'lguncha bajariladi
    # shart o'zgarishi kerak!
```

---

# 3. while vs for jadvali

| Xususiyat | for | while |
|---|---|---|
| Takrorlash soni | Oldindan ma'lum | Noma'lum bo'lishi mumkin |
| Asoslangan | Ketma-ketlik | Shart |
| Cheksiz sikl xavfi | Yo'q | Bor |
| Qachon ishlatiladi | List, range, string takrorlash | Shart tekshiruvi, menyu, o'yin |

---

# 4. Kod misollari

## Misol 1 — Sodda while

```python
hisoblagich = 1

while hisoblagich <= 5:
    print(hisoblagich)
    hisoblagich += 1
```

Natija: `1 2 3 4 5`

---

## Misol 2 — Foydalanuvchi kiritishini kutish

```python
parol = ""

while parol != "secret123":
    parol = input("Parol kiriting: ")

print("Tizimga kirdingiz!")
```

---

## Misol 3 — Yig'indi hisoblash

```python
yigindi = 0
son = int(input("Son kiriting (0 — tugatish): "))

while son != 0:
    yigindi += son
    son = int(input("Son kiriting (0 — tugatish): "))

print(f"Yig'indi: {yigindi}")
```

---

## Misol 4 — Teskari hisoblash

```python
sekund = 10

while sekund > 0:
    print(sekund, end=" ")
    sekund -= 1

print("Start!")
```

Natija: `10 9 8 7 6 5 4 3 2 1 Start!`

---

## Misol 5 — while/else

```python
n = 7
i = 2
tub = True

while i < n:
    if n % i == 0:
        tub = False
        break
    i += 1
else:
    print(f"{n} — tub son")

if not tub:
    print(f"{n} — tub emas")
```

---

## Misol 6 — Cheksiz sikl bilan menyu

```python
while True:
    print("\n=== MENYU ===")
    print("1. Salom")
    print("2. Vaqt")
    print("3. Chiqish")
    
    tanlov = input("Tanlang: ")
    
    if tanlov == "1":
        print("Salom, foydalanuvchi!")
    elif tanlov == "2":
        import datetime
        print(datetime.datetime.now())
    elif tanlov == "3":
        print("Xayr!")
        break
    else:
        print("Noto'g'ri tanlov!")
```

---

## Misol 7 — Son topish o'yini

```python
import random

maxfiy_son = random.randint(1, 100)
urinishlar = 0

print("1 dan 100 gacha son o'yladim. Toping!")

while True:
    taxmin = int(input("Taxminingiz: "))
    urinishlar += 1
    
    if taxmin < maxfiy_son:
        print("Kattaroq!")
    elif taxmin > maxfiy_son:
        print("Kichikroq!")
    else:
        print(f"To'g'ri! {urinishlar} ta urinishda topdingiz!")
        break
```

---

## Misol 8 — Raqamlar yig'indisi

```python
son = int(input("Son kiriting: "))
asl_son = son
yigindi = 0

while son > 0:
    raqam = son % 10
    yigindi += raqam
    son //= 10

print(f"{asl_son} ning raqamlari yig'indisi: {yigindi}")
```

---

# 5. Real loyiha misoli — ATM simulyatsiyasi

```python
balans = 1000000

while True:
    print(f"\nBalans: {balans:,} so'm")
    print("1. Pul yechish")
    print("2. Pul qo'yish")
    print("3. Chiqish")
    
    tanlov = input("Tanlang: ")
    
    if tanlov == "1":
        summa = int(input("Miqdor: "))
        if summa <= balans:
            balans -= summa
            print(f"{summa:,} so'm yechildi.")
        else:
            print("Mablag' yetarli emas!")
    elif tanlov == "2":
        summa = int(input("Miqdor: "))
        balans += summa
        print(f"{summa:,} so'm qo'yildi.")
    elif tanlov == "3":
        print("Xayr!")
        break
```

---

# 6. Ko'p uchraydigan xatolar

## Xato 1: Cheksiz sikl

```python
x = 1
while x <= 5:
    print(x)
    # x += 1 UNUTILDI — cheksiz sikl!
```

## Xato 2: Shartni noto'g'ri yozish

```python
while x = 5:  # SyntaxError! == bo'lishi kerak
    pass
```

## Xato 3: while True dan chiqishni unutish

```python
while True:
    print("Cheksiz!")
    # break yo'q — dastur to'xtamaydi
```

## Xato 4: Hisoblagichni sikl ichida noto'g'ri joyda o'zgartirish

```python
i = 0
while i < 5:
    i += 1  # i o'zgarishi sikl boshida
    print(i)
# 1, 2, 3, 4, 5 chiqadi (0 chiqmaydi)
```

---

# 7. Sinfdagi amaliy topshiriqlar

## 1-topshiriq — Oson

**Vazifa:** 1 dan 20 gacha bo'lgan toq sonlarni while bilan chiqaring.

## 2-topshiriq — O'rta

**Vazifa:** Parol kiritish tizimi: 3 ta urinish, har safar xato bo'lsa qoldiq urinishlarni ko'rsating.

## 3-topshiriq — Murakkab

**Vazifa:** ATM simulyatsiyasi: balansni ko'rish, pul yechish, pul qo'yish va chiqish imkoniyatlari.

---

# 8. Uyga vazifa

1. while bilan 1 dan 100 gacha bo'lgan juft sonlarning yig'indisini hisoblang.
2. Foydalanuvchidan sonlar oling (0 kiritilguncha), eng kattasini toping.
3. Sonning tub ekanligini while bilan tekshiring.
4. Son topish o'yini yozing (1-100 orasida, kompyuter o'ylaydi).
5. Sonni ikkilik sanoq tizimiga while bilan aylantiring.

---

# 9. Tekshirish savollari

1. `while` siklining `for` siklidan asosiy farqi nima?
2. Cheksiz sikl qanday hosil bo'ladi?
3. `while True:` qachon ishlatiladi?
4. `while/else` strukturasi qanday ishlaydi?
5. Hisoblagich nima va nima uchun kerak?
6. `Ctrl+C` nima qiladi?
7. `break` while siklida qanday ishlaydi?
8. while siklida shart qachon tekshiriladi?
9. `do-while` sikli Python'da bormi?
10. while siklida `continue` nima qiladi?

---

## Javoblar

**1.** `for` — takrorlash soni oldindan ma'lum (ketma-ketlik bo'ylab). `while` — shart `True` bo'lguncha davom etadi, takrorlash soni oldindan ma'lum bo'lishi shart emas.

**2.** Shart hech qachon `False` bo'lmasa: `while True:` yoki shart o'zgaruvchisi yangilanmasa.

**3.** `while True:` menyu tizimlarida, o'yinlarda, server dasturlarida ishlatiladi — `break` bilan boshqariladi.

**4.** `else` bloki sikl `break` siz tugatilganda bajariladi. `break` bilan tugatilsa, `else` bajarilmaydi.

**5.** Hisoblagich — siklda iteratsiyalar sonini kuzatuvchi o'zgaruvchi. Siklni tugatish sharti sifatida ishlatiladi.

**6.** `Ctrl+C` — cheksiz siklni tashqaridan to'xtatadi (`KeyboardInterrupt` xatosi).

**7.** `break` siklni darhol to'xtatadi va sikldan keyingi kodga o'tadi.

**8.** Shart har bir iteratsiya boshida tekshiriladi. Shart `False` bo'lsa, sikl tanasi bajarilmaydi.

**9.** Python'da `do-while` yo'q. Uning o'rniga `while True:` + `break` ishlatiladi.

**10.** `continue` — joriy iteratsiyaning qolgan qismini o'tkazib yuborib, keyingi iteratsiyani boshlaydi.

---

# 10. Qisqa xulosa

Bu darsda:

- `while` sikli va shartga asoslangan takrorlash;
- Cheksiz sikllar va ularni boshqarish;
- Hisoblagich bilan ishlash;
- while/else strukturasi;
- Menyu tizimi va ATM simulyatsiyasi

o'rganildi.

---

Keyingi **9-dars: Break, continue va random** da sikl oqimini boshqarish va tasodifiy sonlar bilan ishlash o'rganiladi.

---

# Resurslar va fayllar

- 📄 Python while: https://docs.python.org/3/reference/compound_stmts.html#the-while-statement
- 💻 Kodlar: `github.com/dars-reja/08-dars`
- 🎬 Video dars: `youtube.com/watch?v=dars08`
"""

lessons[9] = """# ⏹️ 9. Break, continue va random — Dars dokumentatsiyasi

`break` va `continue` — bu sikl ichidagi oqimni boshqarish buyruqlari. `break` siklni to'liq to'xtatadi, `continue` esa joriy iteratsiyani o'tkazib yuborib keyingi iteratsiyaga o'tadi.

`random` moduli — Python'ning tasodifiy sonlar va tanlovlar bilan ishlash uchun ishlatiladigan standart kutubxonasi. U o'yinlar, simulyatsiyalar, test ma'lumotlari yaratish va xavfsizlikda keng qo'llaniladi.

Bu uchta tushuncha birgalikda kuchli algoritmlar yaratish imkonini beradi: masalan, tasodifiy son o'yini, yoki ma'lum shartlar asosida siklni boshqarish.

---

## Bu mavzu orqali nimalar qilish mumkin

- Siklni muayyan shartda to'xtatish (`break`);
- Muayyan elementlarni o'tkazib yuborish (`continue`);
- Tasodifiy butun sonlar yaratish (`randint`);
- Ro'yxatdan tasodifiy element tanlash (`choice`);
- O'yin va simulyatsiya dasturlari yozish.

---

## Dars maqsadi

Bu dars oxirida o'quvchi:

- `break` va `continue` ni to'g'ri qo'llash;
- `random` modulining asosiy funksiyalarini bilish;
- O'yinlar va amaliy dasturlarda qo'llash

ni mustaqil bajara oladi.

---

## Kerakli oldingi bilimlar

- 7-dars: For sikli;
- 8-dars: While sikli.

---

# 1. Asosiy tushunchalar

## break nima?

> **`break`** — siklni darhol to'xtatadi va sikldan keyingi kodga o'tadi. `for` va `while` ikkisida ham ishlaydi.

## continue nima?

> **`continue`** — joriy iteratsiyaning qolgan qismini o'tkazib yuborib, keyingi iteratsiyani boshlaydi.

## random nima?

> **`random`** — Python'ning standart kutubxonasi bo'lib, tasodifiy sonlar va tanlovlar bilan ishlash uchun ishlatiladi. `import random` bilan yuklanadi.

---

# 2. random funksiyalari jadvali

| Funksiya | Vazifasi | Misol | Natija |
|---|---|---|---|
| `randint(a, b)` | a dan b gacha tasodifiy butun son | `random.randint(1, 10)` | `7` (masalan) |
| `random()` | 0.0 dan 1.0 gacha tasodifiy float | `random.random()` | `0.583...` |
| `choice(list)` | Listdan tasodifiy element | `random.choice(["a","b"])` | `"b"` |
| `shuffle(list)` | Listni aralashtiradi | `random.shuffle(sonlar)` | list o'zgaradi |
| `sample(list, n)` | n ta noyob tasodifiy element | `random.sample(range(100), 5)` | `[23, 7, ...]` |
| `uniform(a, b)` | a dan b gacha tasodifiy float | `random.uniform(1.0, 5.0)` | `3.14...` |

---

# 3. Kod misollari

## Misol 1 — break

```python
for i in range(1, 11):
    if i == 6:
        print("6 topildi, sikl to'xtadi!")
        break
    print(i)
```

Natija: `1 2 3 4 5 6 topildi, sikl to'xtadi!`

---

## Misol 2 — continue

```python
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)
```

Natija: `1 3 5 7 9` (juft sonlar o'tkazib yuborildi)

---

## Misol 3 — break bilan qidiruv

```python
sonlar = [4, 7, 2, 9, 1, 5, 8]
qidirilayotgan = 9

for son in sonlar:
    if son == qidirilayotgan:
        print(f"{qidirilayotgan} topildi!")
        break
else:
    print(f"{qidirilayotgan} topilmadi.")
```

---

## Misol 4 — random.randint()

```python
import random

for i in range(5):
    son = random.randint(1, 100)
    print(f"Tasodifiy son: {son}")
```

---

## Misol 5 — random.choice()

```python
import random

ranglar = ["qizil", "ko'k", "yashil", "sariq", "oq"]
tanlangan = random.choice(ranglar)
print(f"Tasodifiy rang: {tanlangan}")
```

---

## Misol 6 — Son topish o'yini

```python
import random

son = random.randint(1, 50)
urinish = 0

while True:
    taxmin = int(input("Taxminingiz (1-50): "))
    urinish += 1
    
    if taxmin < son:
        print("Kattaroq!")
    elif taxmin > son:
        print("Kichikroq!")
    else:
        print(f"To'g'ri! {urinish} ta urinishda topdingiz!")
        break
```

---

## Misol 7 — Parol generatori

```python
import random
import string

uzunlik = 12
belgilar = string.ascii_letters + string.digits + "!@#$%"
parol = ""

for i in range(uzunlik):
    parol += random.choice(belgilar)

print(f"Yangi parol: {parol}")
```

---

## Misol 8 — Tosh-qaychi-qog'oz

```python
import random

tanlovlar = ["tosh", "qaychi", "qog'oz"]

while True:
    player = input("Tanlang (tosh/qaychi/qog'oz/chiqish): ").lower()
    if player == "chiqish":
        break
    
    computer = random.choice(tanlovlar)
    print(f"Kompyuter: {computer}")
    
    if player == computer:
        print("Durrang!")
    elif (player == "tosh" and computer == "qaychi") or \
         (player == "qaychi" and computer == "qog'oz") or \
         (player == "qog'oz" and computer == "tosh"):
        print("Siz yutdingiz!")
    else:
        print("Kompyuter yutdi!")
```

---

# 5. Real loyiha misoli — Viktorina o'yini

```python
import random

savollar = [
    {"savol": "Python qaysi yilda yaratilgan?", "javob": "1991"},
    {"savol": "Python yaratuvchisi kim?", "javob": "Guido van Rossum"},
    {"savol": "print() nima qiladi?", "javob": "ekranga chiqaradi"},
]

random.shuffle(savollar)
ball = 0

for s in savollar:
    javob = input(f"{s['savol']} ")
    if javob.lower() == s["javob"].lower():
        print("To'g'ri!")
        ball += 1
    else:
        print(f"Noto'g'ri! Javob: {s['javob']}")

print(f"\nNatija: {ball}/{len(savollar)}")
```

---

# 6. Ko'p uchraydigan xatolar

## Xato 1: break ichma-ich siklda faqat ichki siklni to'xtatadi

```python
for i in range(3):
    for j in range(3):
        if j == 1:
            break  # faqat ichki sikl to'xtaydi
    print(f"i = {i}")
```

## Xato 2: continue dan keyin muhim kod

```python
for i in range(5):
    if i == 2:
        continue
    print(i)
    # i==2 da bu print BAJARILMAYDI
```

## Xato 3: random import qilmaslik

```python
son = random.randint(1, 10)  # NameError!
```

To'g'ri: `import random` birinchi qator.

## Xato 4: randint chegaralari

```python
random.randint(1, 10)  # 1 HAM 10 HAM kiradi (range dan farqli!)
```

---

# 7. Sinfdagi amaliy topshiriqlar

## 1-topshiriq — Oson

**Vazifa:** 1 dan 20 gacha, 13 ni o'tkazib yuboruvchi dastur yozing (continue).

## 2-topshiriq — O'rta

**Vazifa:** 10 ta tasodifiy son yarating (1-100), ular orasidan 50 dan kattalarini chiqaring.

## 3-topshiriq — Murakkab

**Vazifa:** Tosh-qaychi-qog'oz o'yini: 3 ta g'alaba kerak, natijani hisoblab boring.

---

# 8. Uyga vazifa

1. Listdan birinchi manfiy sonni topib, siklni to'xtating.
2. 1-100 orasida faqat 3 ga va 5 ga bo'linadigan sonlarni chiqaring.
3. Tasodifiy 20 ta son yaratib, juft va toqlarini alohida sanang.
4. Loto o'yini: 6 ta noyob tasodifiy son (1-49) yarating.
5. "Harfni top" o'yini: kompyuter harf o'ylaydi, foydalanuvchi topadi.

---

# 9. Tekshirish savollari

1. `break` nima qiladi?
2. `continue` nima qiladi?
3. `break` va `continue` orasidagi farq nima?
4. `random.randint(1, 10)` qanday sonlar qaytaradi?
5. `random.choice()` nima qiladi?
6. `random.shuffle()` nima qiladi?
7. Ichma-ich siklda `break` qaysi siklni to'xtatadi?
8. `for/else` da `else` qachon bajariladi?
9. `import random` ni qayerga yozish kerak?
10. `random.random()` va `random.randint()` farqi nima?

---

## Javoblar

**1.** `break` — siklni darhol to'xtatadi va sikldan keyingi kodga o'tadi.

**2.** `continue` — joriy iteratsiyaning qolgan qismini o'tkazib, keyingi iteratsiyani boshlaydi.

**3.** `break` siklni butunlay to'xtatadi. `continue` faqat joriy iteratsiyani o'tkazib yuboradi, sikl davom etadi.

**4.** 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 — 1 ham 10 ham kiradi (`range` dan farqli).

**5.** `random.choice(list)` — listdan tasodifiy bitta element tanlaydi va qaytaradi.

**6.** `random.shuffle(list)` — listning o'zini (in-place) tasodifiy tartibda aralashtiradi.

**7.** Faqat eng ichki siklni to'xtatadi. Tashqi siklga ta'sir qilmaydi.

**8.** `else` bloki sikl `break` siz, tabiiy tugatilganda bajariladi. Agar `break` ishlasa, `else` bajarilmaydi.

**9.** Faylning boshida, koddan oldin. `import random` standart Python kutubxonasini yuklaydi.

**10.** `random.random()` — 0.0 dan 1.0 gacha float. `random.randint(a, b)` — a dan b gacha butun son (ikkalasi ham kiradi).

---

# 10. Qisqa xulosa

Bu darsda:

- `break` — siklni to'xtatish;
- `continue` — iteratsiyani o'tkazish;
- `random` moduli: `randint`, `choice`, `shuffle`, `sample`;
- O'yinlar va amaliy dasturlar

o'rganildi.

---

Keyingi **10-dars: Ichma-ich sikl va algoritmlar** da naqshlar, matritsa va murakkab algoritmlar o'rganiladi.

---

# Resurslar va fayllar

- 📄 break/continue: https://docs.python.org/3/tutorial/controlflow.html#break-and-continue-statements
- 📄 random: https://docs.python.org/3/library/random.html
- 💻 Kodlar: `github.com/dars-reja/09-dars`
- 🎬 Video dars: `youtube.com/watch?v=dars09`
"""

lessons[10] = """# 🔲 10. Ichma-ich sikl va algoritmlar — Dars dokumentatsiyasi

Ichma-ich sikl (nested loop) — bu bitta sikl ichiga boshqa sikl joylashtirilgan struktura. Tashqi sikl har bir iteratsiyasida ichki sikl to'liq bajariladi. Bu matritsa (2D array), jadval, naqsh chiqarish va murakkab algoritmlar uchun ishlatiladi.

Algoritmlar — bu muammoni bosqichma-bosqich hal qilish yo'riqnomasi. Bu darsda klassik naqsh masalalari, ko'paytirish jadvali va oddiy saralash algoritmlarini o'rganamiz.

---

## Bu mavzu orqali nimalar qilish mumkin

- Jadval va matritsa chiqarish;
- Yulduzcha naqshlar (patterns) yaratish;
- Ko'paytirish jadvali;
- Bubble sort algoritmi;
- Tub sonlar topish.

---

## Dars maqsadi

Bu dars oxirida o'quvchi:

- Ichma-ich sikllar yozish va tushunish;
- Naqsh (pattern) masalalarini yechish;
- Ko'paytirish jadvalini yaratish;
- Oddiy saralash algoritmini tushunish

ni mustaqil bajara oladi.

---

## Kerakli oldingi bilimlar

- 7-dars: For sikli;
- 8-dars: While sikli;
- 9-dars: Break va continue.

---

# 1. Asosiy tushunchalar

## Ichma-ich sikl nima?

> **Ichma-ich sikl** — bitta sikl ichiga boshqa sikl joylashtirilgan struktura. Tashqi sikl har bir iteratsiyasida ichki sikl boshidan oxirigacha bajariladi.

## Naqsh (Pattern) nima?

> **Naqsh** — yulduzcha, raqam yoki harflardan tuzilgan geometrik shakl. Ichma-ich sikllar bilan yaratiladi va algoritmik fikrlashni rivojlantiradi.

## Algoritm nima?

> **Algoritm** — muammoni bosqichma-bosqich, aniq ko'rsatmalar asosida hal qilish usuli.

---

# 2. Kod misollari

## Misol 1 — To'g'ri burchakli uchburchak

```python
for i in range(1, 6):
    print("*" * i)
```

Natija:

```
*
**
***
****
*****
```

---

## Misol 2 — Teskari uchburchak

```python
for i in range(5, 0, -1):
    print("*" * i)
```

---

## Misol 3 — Ko'paytirish jadvali

```python
son = int(input("Son kiriting: "))

for i in range(1, 11):
    print(f"{son} x {i} = {son * i}")
```

---

## Misol 4 — To'liq ko'paytirish jadvali

```python
for i in range(1, 10):
    for j in range(1, 10):
        print(f"{i*j:4}", end="")
    print()
```

---

## Misol 5 — Raqamli uchburchak

```python
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
```

Natija:

```
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 
```

---

## Misol 6 — Markazlashgan piramida

```python
n = 5
for i in range(1, n + 1):
    bo_sh_joy = " " * (n - i)
    yulduzlar = "*" * (2 * i - 1)
    print(bo_sh_joy + yulduzlar)
```

Natija:

```
    *
   ***
  *****
 *******
*********
```

---

## Misol 7 — Tub sonlarni topish

```python
for son in range(2, 51):
    tub = True
    for i in range(2, int(son ** 0.5) + 1):
        if son % i == 0:
            tub = False
            break
    if tub:
        print(son, end=" ")
```

Natija: `2 3 5 7 11 13 17 19 23 29 31 37 41 43 47`

---

## Misol 8 — Bubble Sort (Pufakchali saralash)

```python
sonlar = [64, 34, 25, 12, 22, 11, 90]

for i in range(len(sonlar)):
    for j in range(0, len(sonlar) - i - 1):
        if sonlar[j] > sonlar[j + 1]:
            sonlar[j], sonlar[j + 1] = sonlar[j + 1], sonlar[j]

print(f"Saralangan: {sonlar}")
```

Natija: `Saralangan: [11, 12, 22, 25, 34, 64, 90]`

---

# 5. Real loyiha misoli — O'quvchilar baholar jadvali

```python
talabalar = ["Ali", "Vali", "Sardor"]
fanlar = ["Matematika", "Fizika", "Informatika"]
import random

print(f"{'Talaba':<12}", end="")
for fan in fanlar:
    print(f"{fan:<14}", end="")
print(f"{'O\\'rtacha':<10}")
print("-" * 50)

for talaba in talabalar:
    baholar = [random.randint(60, 100) for _ in fanlar]
    print(f"{talaba:<12}", end="")
    for baho in baholar:
        print(f"{baho:<14}", end="")
    print(f"{sum(baholar)/len(baholar):<10.1f}")
```

---

# 6. Ko'p uchraydigan xatolar

## Xato 1: Ichki va tashqi sikl o'zgaruvchilari bir xil

```python
for i in range(3):
    for i in range(3):  # tashqi i yo'qoldi!
        print(i)
```

## Xato 2: Naqshlarda bo'sh joy xatosi

Noto'g'ri: Bo'sh joylar soni noto'g'ri hisoblanganda piramida noto'g'ri chiqadi.

## Xato 3: Ichma-ich sikl murakkabligi

```python
# O(n^2) — 1000 element uchun 1,000,000 ta amal
# Katta ma'lumotlarda sekin ishlaydi
```

## Xato 4: break faqat ichki siklni to'xtatadi

```python
for i in range(5):
    for j in range(5):
        if j == 2:
            break  # faqat ichki sikl to'xtaydi
```

---

# 7. Sinfdagi amaliy topshiriqlar

## 1-topshiriq — Oson

**Vazifa:** 5x5 yulduzcha to'rtburchak chiqaring.

## 2-topshiriq — O'rta

**Vazifa:** Markazlashgan olmoscha (diamond) shakli chiqaring.

## 3-topshiriq — Murakkab

**Vazifa:** Listni bubble sort bilan saralang va har bir qadamni ko'rsating.

---

# 8. Uyga vazifa

1. 1-10 gacha to'liq ko'paytirish jadvalini chiqaring.
2. Teskari piramida chiqaring.
3. 1 dan 100 gacha tub sonlarni toping.
4. Selection Sort algoritmini yozing.
5. Raqamlar piramidasi chiqaring (1, 12, 123, 1234...).

---

# 9. Tekshirish savollari

1. Ichma-ich sikl nima?
2. Tashqi va ichki sikl o'zgaruvchilari bir xil bo'lsa nima bo'ladi?
3. 3x3 matritsa chiqarish uchun nechta sikl kerak?
4. Bubble Sort qanday ishlaydi?
5. Ichma-ich siklning vaqt murakkabligi (time complexity) qanday?
6. Naqsh masalalarida bo'sh joy qanday hisoblanadi?
7. break ichma-ich siklda qaysi siklni to'xtatadi?
8. Tub son nima va qanday aniqlanadi?
9. `range(1, n+1)` nima uchun `n+1` yoziladi?
10. `"*" * 5` natijasi nima?

---

## Javoblar

**1.** Bitta sikl ichiga boshqa sikl joylashtirilgan struktura. Tashqi siklning har bir iteratsiyasida ichki sikl to'liq ishlaydi.

**2.** Tashqi sikl o'zgaruvchisi ichki siklda qayta yoziladi va qiymati yo'qoladi. Har doim turli nomlar ishlating.

**3.** 2 ta ichma-ich sikl kerak: tashqi sikllar qatorlar, ichki sikllar ustunlar uchun.

**4.** Bubble Sort qo'shni elementlarni solishtirib, kattasini o'ngga suradi. Bu jarayon hamma element to'g'ri joyga kelguncha takrorlanadi.

**5.** O(n^2) — elementlar soni n bo'lsa, amallar soni n*n ga yaqin. Katta ma'lumotlarda sekin ishlaydi.

**6.** Markazlashgan naqshlarda: bo'sh joylar soni = `n - i` (n — qatorlar soni, i — joriy qator).

**7.** Faqat eng ichki siklni to'xtatadi. Tashqi siklga ta'sir qilmaydi.

**8.** Tub son — faqat 1 ga va o'ziga bo'linadigan 1 dan katta son. 2, 3, 5, 7, 11... `range(2, sqrt(n)+1)` da bo'luvchi qidiriladi.

**9.** `range()` da oxirgi son kirmaydi. `range(1, 6)` = 1,2,3,4,5. Shuning uchun `n+1` yoziladi.

**10.** `"*****"` — yulduzchani 5 marta takrorlash. Python'da stringni songa ko'paytirish.

---

# 10. Qisqa xulosa

Bu darsda:

- Ichma-ich sikllar;
- Naqsh (pattern) masalalari;
- Ko'paytirish jadvali;
- Tub sonlar algoritmi;
- Bubble Sort

o'rganildi.

---

Keyingi **11-dars: List asoslari** da ro'yxatlar bilan ishlash — yaratish, o'zgartirish, metodlar va slicing o'rganiladi.

---

# Resurslar va fayllar

- 📄 Python loops: https://docs.python.org/3/tutorial/controlflow.html
- 💻 Kodlar: `github.com/dars-reja/10-dars`
- 🎬 Video dars: `youtube.com/watch?v=dars10`
"""

lessons[11] = """# 📋 11. List asoslari — Dars dokumentatsiyasi

List (ro'yxat) — Python'dagi eng ko'p ishlatiladigan ma'lumot strukturasi bo'lib, bir nechta elementni bitta o'zgaruvchida tartibli saqlash imkonini beradi. List o'zgaruvchan (mutable) — elementlarni qo'shish, o'chirish va o'zgartirish mumkin.

List bilan ishlash Python dasturlashning asosiy qismi: talabalar ro'yxati, mahsulotlar katalogi, ballar jadvali — bularning barchasi list orqali saqlanadi va qayta ishlanadi.

Python listlari har xil turdagi elementlarni saqlashi mumkin (sonlar, matnlar, boshqa listlar), ularga indeks orqali murojaat qilish, slicing bilan kesish va 10 dan ortiq ichki metod bilan ishlash mumkin.

---

## Bu mavzu orqali nimalar qilish mumkin

- Listlar yaratish va elementlarga murojaat qilish;
- Element qo'shish, o'chirish va o'zgartirish;
- List metodlari bilan ishlash;
- Listni saralash va qidirish;
- List comprehension (qisqa yaratish).

---

## Dars maqsadi

Bu dars oxirida o'quvchi:

- List yaratish va indekslash;
- Kamida 10 ta list metodini bilish;
- Slicing bilan ishlash;
- List comprehension yozish;
- Listlarda qidirish va saralash

ni mustaqil bajara oladi.

---

## Kerakli oldingi bilimlar

- 2-dars: O'zgaruvchilar;
- 4-dars: Stringlar (indekslash, slicing);
- 7-dars: For sikli.

---

# 1. Asosiy tushunchalar

## List nima?

> **List** — tartibli, o'zgaruvchan elementlar to'plami. Kvadrat qavslar ichida yaratiladi: `[1, 2, 3]`.

## Mutable nima?

> **Mutable** — o'zgaruvchan. Listdagi elementlarni qo'shish, o'chirish va o'zgartirish mumkin (stringdan farqli).

## List comprehension nima?

> **List comprehension** — listni qisqa yozish usuli: `[x**2 for x in range(5)]` = `[0, 1, 4, 9, 16]`.

---

# 2. List metodlari jadvali

| Metod | Vazifasi | Misol | Natija |
|---|---|---|---|
| `append(x)` | Oxirga element qo'shish | `[1,2].append(3)` | `[1,2,3]` |
| `insert(i, x)` | i indeksga qo'shish | `[1,3].insert(1, 2)` | `[1,2,3]` |
| `extend(list)` | Boshqa listni qo'shish | `[1].extend([2,3])` | `[1,2,3]` |
| `remove(x)` | Birinchi x ni o'chirish | `[1,2,3].remove(2)` | `[1,3]` |
| `pop(i)` | i indeksdagi elementni olish | `[1,2,3].pop(1)` | `2`, list: `[1,3]` |
| `pop()` | Oxirgi elementni olish | `[1,2,3].pop()` | `3`, list: `[1,2]` |
| `clear()` | Barcha elementlarni tozalash | `[1,2,3].clear()` | `[]` |
| `sort()` | Tartibga solish | `[3,1,2].sort()` | `[1,2,3]` |
| `reverse()` | Teskari tartibga | `[1,2,3].reverse()` | `[3,2,1]` |
| `count(x)` | x necha marta uchrashini sanash | `[1,2,2,3].count(2)` | `2` |
| `index(x)` | x ning indeksini topish | `[1,2,3].index(2)` | `1` |
| `copy()` | Nusxa olish | `[1,2,3].copy()` | `[1,2,3]` |

---

# 3. Kod misollari

## Misol 1 — List yaratish va indekslash

```python
mevalar = ["olma", "banan", "uzum", "anor"]
print(mevalar[0])
print(mevalar[-1])
print(mevalar[1:3])
```

Natija:

```
olma
anor
['banan', 'uzum']
```

---

## Misol 2 — Element qo'shish

```python
sonlar = [10, 20, 30]
sonlar.append(40)
sonlar.insert(0, 5)
print(sonlar)
```

Natija: `[5, 10, 20, 30, 40]`

---

## Misol 3 — Element o'chirish

```python
mevalar = ["olma", "banan", "uzum", "anor"]
mevalar.remove("banan")
oxirgi = mevalar.pop()
print(mevalar)
print(f"Olib tashlangan: {oxirgi}")
```

Natija: `['olma', 'uzum']`, `Olib tashlangan: anor`

---

## Misol 4 — sort() va reverse()

```python
sonlar = [64, 25, 12, 22, 11]
sonlar.sort()
print(f"Tartibda: {sonlar}")

sonlar.sort(reverse=True)
print(f"Teskari: {sonlar}")
```

---

## Misol 5 — List bilan for sikli

```python
baholar = [85, 92, 78, 95, 67]

for i, baho in enumerate(baholar, 1):
    if baho >= 90:
        daraja = "A'lo"
    elif baho >= 70:
        daraja = "Yaxshi"
    else:
        daraja = "Qoniqarli"
    print(f"{i}. {baho} — {daraja}")
```

---

## Misol 6 — List comprehension

```python
kvadratlar = [x ** 2 for x in range(1, 11)]
print(kvadratlar)

juft = [x for x in range(1, 21) if x % 2 == 0]
print(juft)
```

Natija:

```
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
```

---

## Misol 7 — Ichma-ich list (2D list)

```python
matritsa = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for qator in matritsa:
    for element in qator:
        print(f"{element:3}", end="")
    print()
```

---

## Misol 8 — in operatori va index()

```python
tillar = ["Python", "Java", "C++", "JavaScript"]

til = input("Dasturlash tili: ")
if til in tillar:
    joy = tillar.index(til)
    print(f"{til} ro'yxatda bor, indeksi: {joy}")
else:
    print(f"{til} ro'yxatda yo'q")
```

---

# 5. Real loyiha misoli — Savdo tizimi

```python
savat = []

while True:
    print(f"\nSavat: {savat}")
    print("1. Mahsulot qo'shish")
    print("2. Mahsulot o'chirish")
    print("3. Savatni tozalash")
    print("4. Chiqish")
    
    tanlov = input("Tanlang: ")
    
    if tanlov == "1":
        mahsulot = input("Mahsulot nomi: ")
        savat.append(mahsulot)
    elif tanlov == "2":
        mahsulot = input("O'chirish: ")
        if mahsulot in savat:
            savat.remove(mahsulot)
        else:
            print("Topilmadi!")
    elif tanlov == "3":
        savat.clear()
    elif tanlov == "4":
        break
```

---

# 6. Ko'p uchraydigan xatolar

## Xato 1: Mavjud bo'lmagan indeksga murojaat

```python
a = [1, 2, 3]
print(a[5])  # IndexError!
```

## Xato 2: remove() ga mavjud bo'lmagan element berish

```python
a = [1, 2, 3]
a.remove(5)  # ValueError!
```

## Xato 3: List nusxalash xatosi

```python
a = [1, 2, 3]
b = a  # nusxa EMAS, havola!
b.append(4)
print(a)  # [1, 2, 3, 4] — a ham o'zgardi!
```

To'g'ri: `b = a.copy()` yoki `b = a[:]`.

## Xato 4: sort() natija qaytarmaydi

```python
a = [3, 1, 2]
b = a.sort()  # b = None!
```

To'g'ri: `b = sorted(a)`.

---

# 7. Sinfdagi amaliy topshiriqlar

## 1-topshiriq — Oson

**Vazifa:** 5 ta son kiritib, eng katta va kichigini toping.

## 2-topshiriq — O'rta

**Vazifa:** List comprehension bilan 1-50 orasidagi 3 ga bo'linadigan sonlarni toping.

## 3-topshiriq — Murakkab

**Vazifa:** Savdo tizimi: mahsulot qo'shish, o'chirish, jami narxni hisoblash.

---

# 8. Uyga vazifa

1. 10 ta son kiritib, o'rtacha, eng katta va eng kichigini toping.
2. Ikki listdagi umumiy elementlarni toping.
3. Listdagi dublikat elementlarni olib tashlang.
4. Listni teskari tartibda chiqaring (reverse() ishlatmang).
5. List comprehension bilan 1-100 orasidagi tub sonlar listini yarating.

---

# 9. Tekshirish savollari

1. List nima va qanday yaratiladi?
2. List va string o'rtasidagi asosiy farq nima?
3. `append()` va `extend()` farqi nima?
4. `remove()` va `pop()` farqi nima?
5. List slicing qanday ishlaydi?
6. `sort()` va `sorted()` farqi nima?
7. List comprehension nima?
8. `a = b` va `a = b.copy()` farqi nima?
9. `in` operatori listlarda qanday ishlaydi?
10. 2D list nima?

---

## Javoblar

**1.** List — tartibli, o'zgaruvchan elementlar to'plami. `sonlar = [1, 2, 3]` yoki `bo_sh = []`.

**2.** List mutable (o'zgaruvchan): `a[0] = "x"` ishlaydi. String immutable: `s[0] = "x"` xato beradi.

**3.** `append(x)` — bitta elementni oxirga qo'shadi. `extend([1,2])` — boshqa listning barcha elementlarini qo'shadi.

**4.** `remove(x)` — qiymat bo'yicha birinchi x ni o'chiradi. `pop(i)` — indeks bo'yicha o'chirib, qiymatni qaytaradi.

**5.** `list[start:stop:step]` — stringdagi kabi ishlaydi. `a[1:3]` — 1 dan 3 gacha (3 kirmaydi).

**6.** `sort()` — listning o'zini saralaydi, `None` qaytaradi. `sorted(list)` — yangi saralangan list qaytaradi, asl list o'zgarmaydi.

**7.** Listni bitta qatorda yaratish usuli: `[ifoda for x in ketmaketlik if shart]`.

**8.** `a = b` — ikkalasi bitta listga havola. `a = b.copy()` — mustaqil nusxa yaratadi.

**9.** `x in list` — x element listda bormi tekshiradi. `True` yoki `False` qaytaradi.

**10.** List ichidagi list: `matritsa = [[1,2],[3,4]]`. Jadval yoki matritsa ifodalash uchun.

---

# 10. Qisqa xulosa

Bu darsda:

- List yaratish va indekslash;
- 12 ta list metodi;
- List comprehension;
- 2D listlar (matritsa);
- Slicing va nusxalash

o'rganildi.

---

Keyingi **12-dars: 1-modul imtihoni** da 1-11 darslar bo'yicha yakuniy tekshiruv o'tkaziladi.

---

# Resurslar va fayllar

- 📄 Python Lists: https://docs.python.org/3/tutorial/datastructures.html#more-on-lists
- 💻 Kodlar: `github.com/dars-reja/11-dars`
- 🎬 Video dars: `youtube.com/watch?v=dars11`
"""

lessons[12] = """# 🎓 12. 1-modul imtihoni — Dars dokumentatsiyasi

1-modul imtihoni — bu 1-darsdan 11-darsgacha o'rganilgan barcha mavzular bo'yicha to'liq bilimlarni tekshiruvchi yakuniy imtihon. Python asoslari, o'zgaruvchilar, turlar, input, arifmetika, stringlar, shartli operatorlar, mantiqiy operatorlar, for/while sikllari, break/continue, random, ichma-ich sikllar va list asoslari qamrab olinadi.

Imtihon nazariy test savollari va amaliy kod yozish topshiriqlaridan iborat. Har bir o'quvchi 100 ballik shkala asosida baholanadi.

---

## Imtihon tartibi (100 ballik shkala)

- **Nazariy test (30 ball)**: 15 ta test savoli, har biri 2 ball.
- **Amaliy topshiriqlar (50 ball)**: 5 ta kod yozish masalasi.
- **Bonus topshiriq (20 ball)**: 1 ta murakkab masala.

---

## Qamrab olingan mavzular

| Dars | Mavzu | Ball ulushi |
|---|---|---|
| 1 | print(), terminal, IDE | 5 |
| 2 | O'zgaruvchilar, turlar, f-string | 10 |
| 3 | input(), arifmetik operatorlar | 10 |
| 4 | Stringlar, metodlar, slicing | 10 |
| 5 | if/elif/else | 10 |
| 6 | and, or, not | 10 |
| 7 | for sikli, range() | 10 |
| 8 | while sikli | 10 |
| 9 | break, continue, random | 10 |
| 10 | Ichma-ich sikllar, algoritmlar | 5 |
| 11 | List asoslari | 10 |

---

# 1. Nazariy test savollari (15 ta)

1. `print("Salom", end="!")` natijasi nima?
2. `type(3.14)` natijasi nima?
3. `input()` qanday tur qaytaradi?
4. `17 % 5` natijasi nima?
5. `"Python"[1:4]` natijasi nima?
6. `"salom".upper()` natijasi nima?
7. `==` va `=` o'rtasidagi farq nima?
8. `True and False` natijasi nima?
9. `range(1, 10, 3)` qanday sonlar hosil qiladi?
10. `break` nima qiladi?
11. `continue` nima qiladi?
12. `random.randint(1, 10)` da 10 kiradimi?
13. `[1, 2, 3].append(4)` dan keyin list qanday bo'ladi?
14. `a = [1, 2, 3]; b = a; b.append(4)` dan keyin `a` nima?
15. List comprehension nima?

---

## Javoblar

**1.** `Salom!` (yangi qatorga o'tmaydi).

**2.** `<class 'float'>`.

**3.** Har doim `str` (string).

**4.** `2` (17 ni 5 ga bo'lganda qoldiq).

**5.** `"yth"` (1 dan 4 gacha, 4 kirmaydi).

**6.** `"SALOM"`.

**7.** `=` — qiymat berish (tayinlash). `==` — solishtirish (tengmi?).

**8.** `False`. `and` da ikkisi ham `True` bo'lishi kerak.

**9.** `1, 4, 7` (1 dan boshlab, 3 qadam bilan).

**10.** Siklni darhol to'xtatadi.

**11.** Joriy iteratsiyani o'tkazib, keyingisiga o'tadi.

**12.** Ha, `randint` da ikkala chegara ham kiradi.

**13.** `[1, 2, 3, 4]`.

**14.** `[1, 2, 3, 4]` — `a` va `b` bitta listga havola.

**15.** Listni bitta qatorda yaratish usuli: `[x**2 for x in range(5)]`.

---

# 2. Amaliy topshiriqlar

## Topshiriq 1 (10 ball)

**Vazifa:** Foydalanuvchidan to'liq ism va yoshni oling. f-string bilan quyidagi formatda chiqaring:

```
Salom, Ali Valiyev! Siz 20 yoshdasiz. 10 yildan keyin siz 30 yoshda bo'lasiz.
```

---

## Topshiriq 2 (10 ball)

**Vazifa:** Foydalanuvchidan son oling va quyidagilarni aniqlang:
- Musbat, manfiy yoki nol;
- Juft yoki toq;
- 3 ga bo'linadimi.

---

## Topshiriq 3 (10 ball)

**Vazifa:** 1 dan 50 gacha bo'lgan tub sonlarni for sikli bilan toping va chiqaring.

---

## Topshiriq 4 (10 ball)

**Vazifa:** Foydalanuvchidan 5 ta son oling, listga saqlang. Eng katta, eng kichik, yig'indi va o'rtacha qiymatni chiqaring (max/min/sum ishlatmang, o'zingiz hisoblang).

---

## Topshiriq 5 (10 ball)

**Vazifa:** So'z teskari yozilgan holini chiqaring (slicing ishlatmang, faqat sikl bilan):

```
Kiritish: Python
Natija: nohtyP
```

---

## Bonus topshiriq (20 ball)

**Vazifa:** Son topish o'yini: kompyuter 1-100 orasida son o'ylaydi, foydalanuvchi topadi. Har bir urinishda "Kattaroq" yoki "Kichikroq" deb yordam bering. Urinishlar soni va vaqtni hisoblang.

---

# 3. Baholash mezonlari

| Mezon | Ball |
|---|---|
| Kod to'g'ri ishlaydi | 40% |
| Kod toza va o'qilishi oson | 20% |
| Xatolar uchun himoya (edge cases) | 20% |
| f-string va to'g'ri formatlash | 10% |
| Izohlar va nomlash | 10% |

---

# 10. Qisqa xulosa

Bu imtihon 1-modulni yakunlaydi. Unda:

- Python asoslari (print, input, o'zgaruvchilar);
- Ma'lumot turlari va konvertatsiya;
- Stringlar va ularning metodlari;
- Shartli va mantiqiy operatorlar;
- for va while sikllari;
- break, continue, random;
- Ichma-ich sikllar va algoritmlar;
- List asoslari

tekshirildi.

---

Keyingi **13-dars: Tuple va Set** da o'zgarmas ketma-ketliklar (tuple) va noyob elementlar to'plami (set) o'rganiladi.

---

# Resurslar va fayllar

- 📄 Konspekt: `12_modul_1_imtihon.pdf`
- 💻 Kodlar: `github.com/dars-reja/12-dars`
- 🎬 Video dars: `youtube.com/watch?v=dars12`
"""

for num, content in lessons.items():
    filepath = os.path.join(DOCS_DIR, f"dars_{num:02d}.md")
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"dars_{num:02d}.md yaratildi: {len(content)} belgi")

print("\n7-12 darslar tayyor!")
