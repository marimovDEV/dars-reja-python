# 🔁 7. For sikli — Dars dokumentatsiyasi

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
