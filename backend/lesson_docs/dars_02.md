# 📦 2. O'zgaruvchilar va turlar — Dars dokumentatsiyasi

O'zgaruvchi (variable) — bu kompyuter xotirasida ma'lumotni saqlash uchun ajratilgan joy. Har bir o'zgaruvchining nomi bor va unga qiymat beriladi. Python'da o'zgaruvchi yaratish uchun maxsus kalit so'z yoki tur ko'rsatish shart emas — qiymat berganda o'zgaruvchi avtomatik yaratiladi.

Python'da har bir qiymatning turi (type) bor. Asosiy turlar: `int` (butun son), `float` (kasrli son), `str` (matn), `bool` (mantiqiy qiymat). Python dinamik tipli til — ya'ni o'zgaruvchining turini oldindan e'lon qilish kerak emas, Python uni qiymatdan avtomatik aniqlaydi.

Ma'lumot turlarini tushunish juda muhim, chunki turga qarab qanday amallar bajarish mumkinligi o'zgaradi. Masalan, ikkita sonni qo'shish (`5 + 3 = 8`) va ikkita matnni qo'shish (`"5" + "3" = "53"`) butunlay boshqa natija beradi.

---

## Bu mavzu orqali nimalar qilish mumkin

- O'zgaruvchi yaratish va unga qiymat berish;
- Ma'lumot turlarini aniqlash (`type()` funksiyasi);
- Turlar orasida konvertatsiya qilish (`int()`, `float()`, `str()`, `bool()`);
- O'zgaruvchi nomlash qoidalariga rioya qilish;
- Bir nechta o'zgaruvchiga bir vaqtda qiymat berish;
- `f-string` yordamida o'zgaruvchilarni matn ichida ishlatish.

---

## Dars maqsadi

Bu dars oxirida o'quvchi:

- O'zgaruvchi yaratish va qayta qiymat berish;
- `int`, `float`, `str`, `bool` turlarini farqlash;
- `type()` funksiyasi bilan turni aniqlash;
- Turlar orasida konvertatsiya qilish;
- `f-string` yordamida formatlangan chiqish yaratish;
- O'zgaruvchi nomlash qoidalarini bilish

ni mustaqil bajara oladi.

---

## Kerakli oldingi bilimlar

Bu darsni tushunish uchun:

- 1-dars: Dasturlash muhiti va Python;
- `print()` funksiyasi

bilinishi kerak.

---

# 1. Asosiy tushunchalar va atamalar

## O'zgaruvchi nima?

> **O'zgaruvchi** — bu xotiradagi nomlangan joy. Siz unga qiymat berasiz va keyin shu nom orqali qiymatga murojaat qilasiz. Masalan: `ism = "Ali"` — bu `ism` nomli o'zgaruvchiga `"Ali"` qiymatini beradi.

## Ma'lumot turi (Data type) nima?

> **Ma'lumot turi** — bu qiymatning qanday ma'lumot ekanligini bildiradi. Python'da 4 ta asosiy tur: `int` (butun son), `float` (kasr), `str` (matn), `bool` (True/False).

## Dinamik tipizatsiya nima?

> **Dinamik tipizatsiya** — Python'da o'zgaruvchining turini oldindan e'lon qilish shart emas. `x = 5` yozganingizda Python o'zi `x` ni `int` deb aniqlaydi. Keyinroq `x = "salom"` yozsangiz, `x` endi `str` turiga o'tadi.

## f-string nima?

> **f-string** — bu `f"..."` formatidagi matn bo'lib, jingalak qavslar `{}` ichida Python ifodalarini yozish imkonini beradi: `f"Mening ismim {ism}"`.

## Konvertatsiya nima?

> **Konvertatsiya (type casting)** — bu qiymatni bir turdan boshqa turga o'zgartirish. Masalan: `int("25")` matnni songa, `str(100)` sonni matnga aylantiradi.

---

# 2. Sintaksis va uning izohi

```python
ozgaruvchi_nomi = qiymat
```

- `ozgaruvchi_nomi` — siz tanlagan nom (harflar, raqamlar, pastki chiziq);
- `=` — tayinlash (assignment) operatori. Bu "teng" emas, "qiymat berish" demak;
- `qiymat` — saqlash kerak bo'lgan ma'lumot.

---

# 3. Ma'lumot turlari jadvali

| Tur | Nomi | Tavsifi | Misol | `type()` natijasi |
|---|---|---|---|---|
| `int` | Integer | Butun son | `42`, `-7`, `0` | `<class 'int'>` |
| `float` | Float | Kasrli son | `3.14`, `-0.5`, `2.0` | `<class 'float'>` |
| `str` | String | Matn (qo'shtirnoq ichida) | `"Salom"`, `'Python'` | `<class 'str'>` |
| `bool` | Boolean | Mantiqiy qiymat | `True`, `False` | `<class 'bool'>` |
| `NoneType` | None | Qiymat yo'qligi | `None` | `<class 'NoneType'>` |

## Konvertatsiya funksiyalari jadvali

| Funksiya | Vazifasi | Misol | Natija |
|---|---|---|---|
| `int(x)` | `x` ni butun songa aylantiradi | `int("25")` | `25` |
| `float(x)` | `x` ni kasrli songa aylantiradi | `float("3.14")` | `3.14` |
| `str(x)` | `x` ni matnga aylantiradi | `str(100)` | `"100"` |
| `bool(x)` | `x` ni mantiqiy qiymatga aylantiradi | `bool(0)` | `False` |
| `type(x)` | `x` ning turini qaytaradi | `type(42)` | `<class 'int'>` |

---

# 4. Kod misollari

## Misol 1 — O'zgaruvchi yaratish

```python
ism = "Ali"
yosh = 20
print(ism)
print(yosh)
```

Natija:

```
Ali
20
```

Qatorma-qator izoh:
- `ism = "Ali"` — `ism` nomli o'zgaruvchiga `"Ali"` matni berildi;
- `yosh = 20` — `yosh` o'zgaruvchisiga `20` butun soni berildi;
- Python turni avtomatik aniqlaydi: `ism` → `str`, `yosh` → `int`.

Qachon ishlatiladi: Ma'lumotlarni keyinchalik ishlatish uchun xotirada saqlashda.

---

## Misol 2 — type() funksiyasi

```python
a = 42
b = 3.14
c = "Salom"
d = True

print(type(a))
print(type(b))
print(type(c))
print(type(d))
```

Natija:

```
<class 'int'>
<class 'float'>
<class 'str'>
<class 'bool'>
```

Qatorma-qator izoh:
- `type()` — o'zgaruvchining qaysi turga tegishli ekanini ko'rsatadi;
- Bu xatolarni topishda juda foydali: kutilgan tur bilan haqiqiy turni solishtirish mumkin.

Qachon ishlatiladi: Debugging vaqtida va tur xatolarini aniqlashda.

---

## Misol 3 — Qayta qiymat berish

```python
x = 10
print(x)

x = "o'n"
print(x)

x = True
print(x)
```

Natija:

```
10
o'n
True
```

Qatorma-qator izoh:
- O'zgaruvchiga yangi qiymat berilganda eski qiymat yo'qoladi;
- Python dinamik tipli: `x` avval `int`, keyin `str`, keyin `bool` bo'ldi;
- Bu qulay, lekin ehtiyot bo'lish kerak — tur kutilmaganda o'zgarishi xatolarga olib keladi.

Qachon ishlatiladi: O'zgaruvchini yangilash, hisoblagichlar, davlat o'zgarishi (state).

---

## Misol 4 — f-string formatlash

```python
ism = "Sardor"
yosh = 22
kasb = "dasturchi"

print(f"Salom! Mening ismim {ism}.")
print(f"Men {yosh} yoshdaman va {kasb}man.")
print(f"Kelasi yil men {yosh + 1} yoshda bo'laman.")
```

Natija:

```
Salom! Mening ismim Sardor.
Men 22 yoshdaman va dasturchiman.
Kelasi yil men 23 yoshda bo'laman.
```

Qatorma-qator izoh:
- `f"..."` — matn oldiga `f` harfi qo'yilganda `{}` ichidagi ifodalar hisoblanadi;
- `{ism}` — o'zgaruvchining qiymati matn ichiga qo'yiladi;
- `{yosh + 1}` — `{}` ichida hisoblash ham mumkin.

Qachon ishlatiladi: Matn ichida o'zgaruvchilarni ko'rsatish kerak bo'lganda (eng zamonaviy usul).

---

## Misol 5 — Turlar konvertatsiyasi

```python
yosh_text = "25"
yosh_son = int(yosh_text)

print(type(yosh_text))
print(type(yosh_son))
print(yosh_son + 5)
```

Natija:

```
<class 'str'>
<class 'int'>
30
```

Qatorma-qator izoh:
- `"25"` — bu matn (string), arifmetik amal bajarib bo'lmaydi;
- `int("25")` — matnni butun songa aylantiradi;
- Endi `yosh_son + 5` ishlaydi, chunki ikkalasi ham son.

Qachon ishlatiladi: Foydalanuvchidan `input()` orqali olingan ma'lumotlarni (doim `str`) songa o'zgartirishda.

---

## Misol 6 — Bir nechta o'zgaruvchiga qiymat berish

```python
x, y, z = 10, 20, 30
print(x, y, z)

a = b = c = 0
print(a, b, c)
```

Natija:

```
10 20 30
0 0 0
```

Qatorma-qator izoh:
- `x, y, z = 10, 20, 30` — uchta o'zgaruvchiga bir qatorda alohida qiymatlar berildi;
- `a = b = c = 0` — uchta o'zgaruvchiga bir xil qiymat berildi;
- Bu kodni qisqartirish usuli.

Qachon ishlatiladi: Bir nechta bog'liq o'zgaruvchini bir vaqtda e'lon qilishda.

---

## Misol 7 — Bool turining xususiyatlari

```python
print(bool(1))
print(bool(0))
print(bool("salom"))
print(bool(""))
print(bool(None))
print(bool([1, 2]))
print(bool([]))
```

Natija:

```
True
False
True
False
False
True
False
```

Qatorma-qator izoh:
- `0`, `""` (bo'sh string), `None`, `[]` (bo'sh list) — bularning barchasi `False`;
- Qolgan barcha qiymatlar `True`;
- Bu qoida `if` shartlarida juda muhim.

Qachon ishlatiladi: Shartli tekshirishlarda va bool konvertatsiyasida.

---

## Misol 8 — O'zgaruvchi nomlash qoidalari

```python
ism = "Ali"
yosh_2024 = 20
_maxfiy = "sir"
MAX_SIZE = 100
user_name = "admin"

print(ism, yosh_2024, _maxfiy, MAX_SIZE, user_name)
```

Natija:

```
Ali 20 sir 100 admin
```

Qatorma-qator izoh:
- O'zgaruvchi nomi harf yoki `_` bilan boshlanishi kerak;
- Raqam bilan boshlanmaydi;
- Bo'sh joy va tire (`-`) ishlatilmaydi, `_` (pastki chiziq) ishlatiladi;
- Python kalit so'zlari (`if`, `for`, `class`, `return`) nom sifatida ishlatilmaydi;
- `KATTA_HARFLAR` — konstantalar uchun, `kichik_harflar` — oddiy o'zgaruvchilar uchun.

Qachon ishlatiladi: Har doim — to'g'ri nomlash o'qilishi oson va professional kod yozish uchun muhim.

---

# 5. Real loyiha misoli — Shaxsiy ma'lumotlar kartasi

```python
ism = "Sardor"
familiya = "Karimov"
yosh = 22
kasb = "Backend Developer"
maosh = 8500000.50
ishlayaptimi = True

print("=" * 40)
print(f"  ISM:       {ism} {familiya}")
print(f"  YOSH:      {yosh}")
print(f"  KASB:      {kasb}")
print(f"  MAOSH:     {maosh:,.2f} so'm")
if ishlayaptimi:
    print(f"  HOLAT:     Faol")
else:
    print(f"  HOLAT:     Nofaol")
print("=" * 40)
print()
print(f"  Turlar: ism={type(ism).__name__}, yosh={type(yosh).__name__}")
print(f"          maosh={type(maosh).__name__}, holat={type(ishlayaptimi).__name__}")
```

Natija:

```
========================================
  ISM:       Sardor Karimov
  YOSH:      22
  KASB:      Backend Developer
  MAOSH:     8,500,000.50 so'm
  HOLAT:     Faol
========================================

  Turlar: ism=str, yosh=int
          maosh=float, holat=bool
```

---

# 6. Ko'p uchraydigan xatolar

## Xato 1: Matn va sonni `+` bilan birlashtirish

Noto'g'ri:

```python
yosh = 20
print("Yosh: " + yosh)
```

Nima uchun xato: `TypeError: can only concatenate str to str`. `+` operatori matn va sonni birlashtira olmaydi.

To'g'ri:

```python
yosh = 20
print("Yosh: " + str(yosh))
print(f"Yosh: {yosh}")
```

Qanday oldini olish: `f-string` ishlating yoki `str()` bilan konvertatsiya qiling.

---

## Xato 2: Raqam bilan boshlanadigan o'zgaruvchi nomi

Noto'g'ri:

```python
2son = 10
```

Nima uchun xato: `SyntaxError`. Python'da o'zgaruvchi nomi raqam bilan boshlanmaydi.

To'g'ri:

```python
son_2 = 10
ikkinchi_son = 10
```

Qanday oldini olish: Nomni doim harf yoki `_` bilan boshlang.

---

## Xato 3: Matnni songa konvertatsiya qilishda xato

Noto'g'ri:

```python
qiymat = int("salom")
```

Nima uchun xato: `ValueError: invalid literal for int()`. `"salom"` matni songa aylantirib bo'lmaydi.

To'g'ri:

```python
qiymat = int("25")
```

Qanday oldini olish: Konvertatsiya qilishdan oldin qiymatning son ekanligini tekshiring (`str.isdigit()`).

---

## Xato 4: Tayinlash va solishtirish operatorlarini aralashtirish

Noto'g'ri:

```python
x = 10
if x = 10:
    print("Teng")
```

Nima uchun xato: `=` tayinlash operatori, `==` solishtirish operatori. `if` ichida `==` ishlatilishi kerak.

To'g'ri:

```python
x = 10
if x == 10:
    print("Teng")
```

Qanday oldini olish: `=` ni "qiymat ber", `==` ni "tengmi?" deb yodlang.

---

# 7. Sinfdagi amaliy topshiriqlar

## 1-topshiriq — Oson

**Vazifa:** 4 ta o'zgaruvchi yarating: `ism` (str), `yosh` (int), `boy` (float), `talabami` (bool). Har birini `f-string` yordamida bir qatorda chiqaring.

---

## 2-topshiriq — O'rta

**Vazifa:** Foydalanuvchi `"150"` matnini berdi. Uni songa aylantiring, 10 qo'shing va natijani `f-string` bilan chiqaring: `"Natija: 160"`.

---

## 3-topshiriq — Murakkab

**Vazifa:** 5 ta o'zgaruvchi yarating. Har birining nomi, qiymati va turini jadval ko'rinishida chiqaring:

```
Nom          | Qiymat     | Tur
-------------|------------|--------
ism          | Ali        | str
yosh         | 20         | int
```

---

# 8. Uyga vazifa

1. 5 ta turli xil turdagi o'zgaruvchi yarating va har birining `type()` natijasini chiqaring.
2. `f-string` yordamida o'zingiz haqingizda 5 qatorlik ma'lumot chiqaring.
3. `int()`, `float()`, `str()` funksiyalarini har birini kamida 2 xil misolda sinab ko'ring.
4. O'zgaruvchi nomlash qoidalarini buzadigan 5 ta noto'g'ri nom yozing va har birida qanday xato chiqishini izohlang.
5. `bool()` funksiyasiga 10 xil qiymat bering va natijalarini jadval ko'rinishida chiqaring.

---

# 9. Tekshirish savollari

1. O'zgaruvchi nima va u nima uchun kerak?
2. Python'da qanday asosiy ma'lumot turlari bor?
3. `int` va `float` o'rtasidagi farq nima?
4. `type()` funksiyasi nima qaytaradi?
5. `x = "10"` bo'lsa, `x + 5` nima uchun xato beradi?
6. f-string nima va qanday ishlatiladi?
7. `bool(0)`, `bool("")`, `bool(None)` nima qaytaradi va nima uchun?
8. O'zgaruvchi nomida qanday belgilar ishlatish mumkin va qaysilari mumkin emas?
9. `a, b, c = 1, 2, 3` qatorida nima sodir bo'ladi?
10. Dinamik tipizatsiya nima va Python'da qanday ishlaydi?

---

## Javoblar

**1.** O'zgaruvchi — bu xotiradagi nomlangan joy bo'lib, unga qiymat beriladi va keyinchalik shu nom orqali qiymatga murojaat qilinadi. U ma'lumotlarni saqlash va qayta ishlatish uchun kerak.

**2.** Python'dagi asosiy ma'lumot turlari: `int` (butun son), `float` (kasrli son), `str` (matn), `bool` (mantiqiy True/False), `NoneType` (qiymat yo'qligi — `None`).

**3.** `int` — butun son (kasrsiz): `42`, `-7`. `float` — kasrli son: `3.14`, `2.0`. `int` aniq, `float` taxminiy bo'lishi mumkin (floating-point precision muammosi).

**4.** `type()` funksiyasi argument sifatida berilgan qiymat yoki o'zgaruvchining ma'lumot turini qaytaradi. Masalan: `type(42)` natijasi `<class 'int'>`.

**5.** `TypeError` xatosi beradi, chunki `x` turi `str`, `5` turi `int`. Python `+` operatori bilan har xil turlarni birlashtira olmaydi. Yechim: `int(x) + 5` yoki `x + str(5)`.

**6.** f-string — bu `f"..."` formatidagi matn bo'lib, `{}` ichida Python ifodalarini yozish imkonini beradi. Masalan: `f"Salom, {ism}!"` — `ism` o'zgaruvchisining qiymati matn ichiga qo'yiladi.

**7.** `bool(0)` → `False`, `bool("")` → `False`, `bool(None)` → `False`. Python'da "bo'sh" yoki "nol" qiymatlar `False` hisoblanadi. Bu qoida: 0, bo'sh string, None, bo'sh list/dict — barchasi `False`.

**8.** Ruxsat etilgan: harflar (a-z, A-Z), raqamlar (0-9, lekin boshida emas), pastki chiziq (`_`). Mumkin emas: bo'sh joy, tire (`-`), nuqta, boshqa maxsus belgilar. Python kalit so'zlari (`if`, `for`, `class`) nom sifatida ishlatilmaydi.

**9.** Bir qatorda uchta o'zgaruvchiga alohida qiymatlar beriladi: `a = 1`, `b = 2`, `c = 3`. Bu Python'ning tuple unpacking xususiyati.

**10.** Dinamik tipizatsiya — Python'da o'zgaruvchining turini oldindan e'lon qilish shart emas. Python turni qiymatdan avtomatik aniqlaydi. Bir o'zgaruvchiga avval son, keyin matn berish mumkin — tur o'zgaradi.

---

# 10. Qisqa xulosa

Bu darsda:

- O'zgaruvchi yaratish va qiymat berish;
- Ma'lumot turlari: `int`, `float`, `str`, `bool`;
- `type()` funksiyasi;
- Turlar konvertatsiyasi: `int()`, `float()`, `str()`, `bool()`;
- `f-string` formatlash;
- O'zgaruvchi nomlash qoidalari

o'rganildi.

---

Keyingi **3-dars: Input va arifmetika** da foydalanuvchidan ma'lumot olish (`input()`) va arifmetik amallar (`+`, `-`, `*`, `/`, `//`, `%`, `**`) o'rganiladi.

---

# Resurslar va fayllar

- 📄 Python Data Types: https://docs.python.org/3/library/stdtypes.html
- 📄 f-string: https://docs.python.org/3/reference/lexical_analysis.html#f-strings
- 💻 Kodlar: `github.com/dars-reja/02-dars`
- 🎬 Video dars: `youtube.com/watch?v=dars02`
