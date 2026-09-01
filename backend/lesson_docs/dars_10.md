# 🔲 10. Ichma-ich sikl va algoritmlar — Dars dokumentatsiyasi

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
print(f"{'O\'rtacha':<10}")
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
