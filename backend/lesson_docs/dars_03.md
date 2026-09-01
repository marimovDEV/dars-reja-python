# ⌨️ 3. Input va arifmetika — Dars dokumentatsiyasi

`input()` funksiyasi — bu foydalanuvchidan klaviatura orqali ma'lumot olish uchun ishlatiladigan Python'ning ichki funksiyasi. Dastur `input()` ga yetganda to'xtaydi va foydalanuvchi matn kiritib Enter bosguncha kutadi. `input()` har doim `str` (matn) qaytaradi — son kiritilgan bo'lsa ham.

Arifmetik operatorlar — bu sonlar ustida matematik amallar bajarish uchun ishlatiladigan belgilar. Python'da 7 ta asosiy arifmetik operator bor: qo'shish (`+`), ayirish (`-`), ko'paytirish (`*`), bo'lish (`/`), butun bo'lish (`//`), qoldiq (`%`) va daraja (`**`).

`input()` va arifmetika birgalikda ishlaganda, foydalanuvchi kiritgan ma'lumotni songa aylantirish (`int()` yoki `float()`) va ustida hisob-kitob bajarish mumkin bo'ladi. Bu real dasturlarning asosi — kalkulyator, savdo tizimi, maosh hisoblash kabi ilovalar shu tamoyilga qurilgan.

---

## Bu mavzu orqali nimalar qilish mumkin

- Foydalanuvchidan matn va son olish;
- Arifmetik amallar bajarish (7 ta operator);
- `input()` natijasini songa aylantirish;
- Kalkulyator va hisob-kitob dasturlari yozish;
- Operatorlar ustunligini (prioritetini) tushunish.

---

## Dars maqsadi

Bu dars oxirida o'quvchi:

- `input()` funksiyasidan foydalanish;
- Barcha 7 ta arifmetik operatorni bilish va qo'llash;
- `input()` natijasini `int()` yoki `float()` ga aylantirish;
- Operatorlar ustunligini tushunish;
- Amaliy hisob-kitob dasturlari yozish

ni mustaqil bajara oladi.

---

## Kerakli oldingi bilimlar

Bu darsni tushunish uchun:

- 1-dars: print() funksiyasi;
- 2-dars: O'zgaruvchilar va turlar (int, float, str)

bilinishi kerak.

---

# 1. Asosiy tushunchalar va atamalar

## `input()` nima?

> **`input()`** — bu foydalanuvchidan klaviatura orqali ma'lumot olish funksiyasi. U doim `str` (matn) qaytaradi. Qavs ichiga so'rov matni yoziladi: `input("Ismingiz: ")`.

## Arifmetik operator nima?

> **Arifmetik operator** — bu sonlar ustida matematik amallar bajarish uchun ishlatiladigan belgi. Masalan: `+` (qo'shish), `*` (ko'paytirish), `**` (daraja).

## Operatorlar ustunligi (Operator Precedence) nima?

> **Operatorlar ustunligi** — bu Python bir satrda bir nechta operator bo'lganda qaysi birini avval bajarishini belgilaydigan qoida. Masalan: `2 + 3 * 4 = 14` (avval `*`, keyin `+`).

## Butun bo'lish nima?

> **Butun bo'lish (`//`)** — bo'lish natijasining faqat butun qismini qaytaradi, kasrni tashlaydi. `7 // 2 = 3`.

## Qoldiq nima?

> **Qoldiq (`%`)** — bo'lishdan keyin qolgan qismni qaytaradi. `7 % 2 = 1` (7 ni 2 ga bo'lganda 1 qoldiq qoladi).

---

# 2. Sintaksis va uning izohi

```python
ozgaruvchi = input("So'rov matni: ")
```

- `input("So'rov matni: ")` — ekranga `So'rov matni: ` yozadi va foydalanuvchi kiritishini kutadi;
- Foydalanuvchi yozgan matn `ozgaruvchi` ga saqlanadi;
- Natija **har doim** `str` turida bo'ladi.

---

# 3. Arifmetik operatorlar jadvali

| Operator | Nomi | Vazifasi | Misol | Natija |
|---|---|---|---|---|
| `+` | Qo'shish | Ikki sonni qo'shadi | `5 + 3` | `8` |
| `-` | Ayirish | Ikki sonning farqi | `10 - 4` | `6` |
| `*` | Ko'paytirish | Ikki sonni ko'paytiradi | `6 * 7` | `42` |
| `/` | Bo'lish | Natija doim float | `7 / 2` | `3.5` |
| `//` | Butun bo'lish | Kasrni tashlaydi | `7 // 2` | `3` |
| `%` | Qoldiq (modulo) | Bo'lishdan qoldiq | `7 % 2` | `1` |
| `**` | Daraja | Sonni darajaga ko'taradi | `2 ** 10` | `1024` |

## Operatorlar ustunligi jadvali (yuqoridan pastga — avval bajariladi)

| Ustunlik | Operator | Misol |
|---|---|---|
| 1 (eng yuqori) | `**` | `2 ** 3 = 8` |
| 2 | `*`, `/`, `//`, `%` | `10 / 2 = 5.0` |
| 3 (eng past) | `+`, `-` | `5 + 3 = 8` |

Qavslar `()` har doim birinchi bajariladi.

---

# 4. Kod misollari

## Misol 1 — input() dan matn olish

```python
ism = input("Ismingizni kiriting: ")
print(f"Salom, {ism}!")
```

Natija:

```
Ismingizni kiriting: Ali
Salom, Ali!
```

Qatorma-qator izoh:
- `input("Ismingizni kiriting: ")` — ekranga so'rov yozadi va kutadi;
- Foydalanuvchi `Ali` yozdi va Enter bosdi;
- `ism` o'zgaruvchisiga `"Ali"` (str) saqlandi.

Qachon ishlatiladi: Foydalanuvchidan ism, email, parol kabi matnli ma'lumot olishda.

---

## Misol 2 — input() dan son olish

```python
yosh = int(input("Yoshingizni kiriting: "))
print(f"Siz {yosh} yoshdasiz.")
print(f"5 yildan keyin siz {yosh + 5} yoshda bo'lasiz.")
```

Natija:

```
Yoshingizni kiriting: 20
Siz 20 yoshdasiz.
5 yildan keyin siz 25 yoshda bo'lasiz.
```

Qatorma-qator izoh:
- `input()` matn qaytaradi, shuning uchun `int()` bilan songa aylantiramiz;
- `yosh + 5` — endi arifmetik amal bajarish mumkin.

Qachon ishlatiladi: Son talab qilingan har qanday kiritishda (yosh, miqdor, narx).

---

## Misol 3 — Barcha arifmetik operatorlar

```python
a = 17
b = 5

print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b}")
print(f"{a} // {b} = {a // b}")
print(f"{a} % {b} = {a % b}")
print(f"{a} ** {b} = {a ** b}")
```

Natija:

```
17 + 5 = 22
17 - 5 = 12
17 * 5 = 85
17 / 5 = 3.4
17 // 5 = 3
17 % 5 = 2
17 ** 5 = 1419857
```

Qachon ishlatiladi: Matematik hisob-kitoblar, algoritmlar va formulalar.

---

## Misol 4 — Operatorlar ustunligi

```python
natija1 = 2 + 3 * 4
natija2 = (2 + 3) * 4

print(f"2 + 3 * 4 = {natija1}")
print(f"(2 + 3) * 4 = {natija2}")
```

Natija:

```
2 + 3 * 4 = 14
(2 + 3) * 4 = 20
```

Qatorma-qator izoh:
- Birinchisida: avval `3 * 4 = 12`, keyin `2 + 12 = 14`;
- Ikkinchisida: avval qavs `(2 + 3) = 5`, keyin `5 * 4 = 20`.

---

## Misol 5 — Sodda kalkulyator

```python
son1 = float(input("Birinchi sonni kiriting: "))
son2 = float(input("Ikkinchi sonni kiriting: "))

print(f"Yig'indi:    {son1} + {son2} = {son1 + son2}")
print(f"Ayirma:      {son1} - {son2} = {son1 - son2}")
print(f"Ko'paytma:   {son1} * {son2} = {son1 * son2}")
if son2 != 0:
    print(f"Bo'linma:    {son1} / {son2} = {son1 / son2}")
else:
    print("Bo'linma:    Nolga bo'lish mumkin emas!")
```

Natija:

```
Birinchi sonni kiriting: 10
Ikkinchi sonni kiriting: 3
Yig'indi:    10.0 + 3.0 = 13.0
Ayirma:      10.0 - 3.0 = 7.0
Ko'paytma:   10.0 * 3.0 = 30.0
Bo'linma:    10.0 / 3.0 = 3.3333333333333335
```

Qachon ishlatiladi: Hisob-kitob dasturlari va amaliy loyihalarda.

---

## Misol 6 — Juft/toq aniqlash

```python
son = int(input("Son kiriting: "))
qoldiq = son % 2

if qoldiq == 0:
    print(f"{son} — juft son")
else:
    print(f"{son} — toq son")
```

Natija:

```
Son kiriting: 7
7 — toq son
```

Qachon ishlatiladi: Algoritmik masalalarda va ma'lumotlarni filtrlashda.

---

## Misol 7 — Doira yuzasi hisoblash

```python
import math

radius = float(input("Doira radiusini kiriting: "))
yuza = math.pi * radius ** 2
perimetr = 2 * math.pi * radius

print(f"Doira yuzasi: {yuza:.2f}")
print(f"Doira perimetri: {perimetr:.2f}")
```

Natija:

```
Doira radiusini kiriting: 5
Doira yuzasi: 78.54
Doira perimetri: 31.42
```

Qachon ishlatiladi: Geometrik hisob-kitoblar va ilmiy dasturlarda.

---

## Misol 8 — Maosh hisoblash

```python
soatlik_stavka = float(input("Soatlik stavka (so'm): "))
ishlangan_soat = float(input("Ishlangan soat: "))

brutto = soatlik_stavka * ishlangan_soat
soliq = brutto * 0.12
netto = brutto - soliq

print(f"\nMaosh hisoboti:")
print(f"  Brutto maosh:  {brutto:,.2f} so'm")
print(f"  Soliq (12%):   {soliq:,.2f} so'm")
print(f"  Netto maosh:   {netto:,.2f} so'm")
```

Natija:

```
Soatlik stavka (so'm): 50000
Ishlangan soat: 160

Maosh hisoboti:
  Brutto maosh:  8,000,000.00 so'm
  Soliq (12%):   960,000.00 so'm
  Netto maosh:   7,040,000.00 so'm
```

---

# 5. Real loyiha misoli — Valyuta konvertori

```python
print("=" * 40)
print("   VALYUTA KONVERTORI")
print("=" * 40)

usd_kurs = 12650.0
eur_kurs = 13800.0

som = float(input("\nMiqdorni so'mda kiriting: "))

usd = som / usd_kurs
eur = som / eur_kurs

print(f"\n{som:,.2f} so'm =")
print(f"  {usd:,.2f} AQSh dollari")
print(f"  {eur:,.2f} Yevro")
print(f"\nKurslar: 1 USD = {usd_kurs:,.0f}, 1 EUR = {eur_kurs:,.0f}")
```

---

# 6. Ko'p uchraydigan xatolar

## Xato 1: input() natijasini songa aylantirsiz hisoblash

Noto'g'ri:

```python
son = input("Son: ")
print(son + 5)
```

Nima uchun xato: `TypeError`. `input()` doim `str` qaytaradi.

To'g'ri:

```python
son = int(input("Son: "))
print(son + 5)
```

## Xato 2: Nolga bo'lish

Noto'g'ri:

```python
print(10 / 0)
```

Nima uchun xato: `ZeroDivisionError`. Nolga bo'lish matematik jihatdan noaniq.

To'g'ri:

```python
if b != 0:
    print(10 / b)
else:
    print("Nolga bo'lish mumkin emas!")
```

## Xato 3: Kasrli sonni int() ga berish

Noto'g'ri:

```python
son = int(input("Son: "))  # "3.5" kiritilsa ValueError
```

To'g'ri:

```python
son = float(input("Son: "))
```

## Xato 4: Qavslarni unutish

Noto'g'ri:

```python
natija = 100 + 20 * 0.12  # 102.4 (noto'g'ri hisob)
```

To'g'ri:

```python
natija = (100 + 20) * 0.12  # 14.4
```

---

# 7. Sinfdagi amaliy topshiriqlar

## 1-topshiriq — Oson

**Vazifa:** Foydalanuvchidan ikkita son oling va ularning yig'indisi, ayirmasi va ko'paytmasini chiqaring.

## 2-topshiriq — O'rta

**Vazifa:** Foydalanuvchidan to'rtburchakning eni va bo'yini oling, yuzasi va perimetrini hisoblang.

## 3-topshiriq — Murakkab

**Vazifa:** Foydalanuvchidan 3 ta fan bahosini oling, o'rtacha bahoni hisoblang va darajasini aniqlang (90+ "A'lo", 70+ "Yaxshi", qolgani "Qoniqarli").

---

# 8. Uyga vazifa

1. Sodda kalkulyator yozing: 2 ta son va 1 ta operator olib natijani chiqarsin.
2. Selsiy haroratni Farengeytga aylantiring (`F = C * 9/5 + 32`).
3. Mahsulot narxi va miqdorini oling, jami va 15% chegirmali summani chiqaring.
4. 3 xonali sonning raqamlar yig'indisini toping: `123` → `1 + 2 + 3 = 6`.
5. Sekundlar sonini soat:minut:sekund formatida chiqaring.

---

# 9. Tekshirish savollari

1. `input()` funksiyasi qanday tur qaytaradi?
2. `input()` natijasini songa aylantirish uchun nima qilish kerak?
3. `/` va `//` operatorlari o'rtasidagi farq nima?
4. `%` operatori nima qaytaradi?
5. `2 + 3 * 4` natijasi nima va nima uchun?
6. `**` operatorining vazifasi nima?
7. `10 / 0` yozilganda nima sodir bo'ladi?
8. `float(input())` va `int(input())` o'rtasidagi farq nima?
9. `:.2f` formatlash nima qiladi?
10. Qavslar `()` operatorlar ustunligiga qanday ta'sir qiladi?

---

## Javoblar

**1.** `input()` har doim `str` (string, matn) turini qaytaradi — foydalanuvchi son kiritgan bo'lsa ham.

**2.** `int(input("..."))` — butun songa aylantirish, `float(input("..."))` — kasrli songa aylantirish.

**3.** `/` — oddiy bo'lish, natija har doim `float`: `7 / 2 = 3.5`. `//` — butun bo'lish, kasrni tashlaydi: `7 // 2 = 3`.

**4.** `%` (modulo) — bo'lishdan keyin qolgan qoldiqni qaytaradi. `17 % 5 = 2`.

**5.** Natija: `14`. `*` operatori `+` dan ustunroq, avval `3 * 4 = 12`, keyin `2 + 12 = 14`.

**6.** `**` — daraja operatori. `2 ** 10 = 1024`. Eng yuqori ustunlikka ega.

**7.** `ZeroDivisionError: division by zero` xatosi chiqadi. Oldini olish uchun `if b != 0:` tekshiruvi kerak.

**8.** `int(input())` faqat butun sonlarni qabul qiladi, kasrli son kiritilsa `ValueError`. `float(input())` ham butun ham kasrli sonlarni qabul qiladi.

**9.** `:.2f` — sonni 2 ta kasr bilan formatlaydi. `f"{3.14159:.2f}"` → `"3.14"`.

**10.** Qavslar har doim birinchi bajariladi va standart ustunlikni o'zgartiradi. `(2 + 3) * 4 = 20`, qavsiz `2 + 3 * 4 = 14`.

---

# 10. Qisqa xulosa

Bu darsda:

- `input()` funksiyasi va foydalanuvchidan ma'lumot olish;
- 7 ta arifmetik operator: `+`, `-`, `*`, `/`, `//`, `%`, `**`;
- Turlar konvertatsiyasi: `int(input())`, `float(input())`;
- Operatorlar ustunligi va qavslar;
- Real hisob-kitob dasturlari

o'rganildi.

---

Keyingi **4-dars: Stringlar** da matn bilan ishlash — indekslash, slicing, string metodlari va formatlash usullari o'rganiladi.

---

# Resurslar va fayllar

- 📄 Python input(): https://docs.python.org/3/library/functions.html#input
- 📄 Arifmetik operatorlar: https://docs.python.org/3/reference/expressions.html
- 💻 Kodlar: `github.com/dars-reja/03-dars`
- 🎬 Video dars: `youtube.com/watch?v=dars03`
