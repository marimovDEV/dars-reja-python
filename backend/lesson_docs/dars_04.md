# 🔤 4. Stringlar — Dars dokumentatsiyasi

String (matn) — bu belgilar ketma-ketligi bo'lib, Python'da eng ko'p ishlatiladigan ma'lumot turlaridan biri. `str` turi qo'shtirnoq ichida yoziladi. Stringlar o'zgarmas (immutable) — yaratilgandan keyin undagi alohida belgini o'zgartirib bo'lmaydi, lekin yangi string yaratish mumkin.

Stringlar bilan ishlash dasturlashning deyarli har bir sohasida uchraydi: foydalanuvchi kiritgan ma'lumotlarni qayta ishlash, fayllar bilan ishlash, ma'lumotlarni formatlash, web sahifalar yaratish — bularning barchasi string operatsiyalari.

Python stringlari uchun juda boy metodlar to'plamiga ega — 40 dan ortiq ichki metod mavjud. Bu darsda eng muhim va ko'p ishlatiladigan metodlarni batafsil o'rganamiz.

---

## Bu mavzu orqali nimalar qilish mumkin

- Matnlarni birlashtirish va takrorlash;
- Indekslash va kesish (slicing) orqali kerakli qismni olish;
- String metodlari bilan ishlash;
- f-string, .format() yordamida formatlash;
- Matnni tekshirish: startswith(), endswith(), isdigit(), isalpha().

---

## Dars maqsadi

Bu dars oxirida o'quvchi:

- String yaratish va asosiy xususiyatlarini bilish;
- Indeks va slicing bilan ishlash;
- Kamida 15 ta string metodini bilish va qo'llash;
- f-string yordamida murakkab formatlash;
- String o'zgarmasligi (immutability) tushunchasini tushunish

ni mustaqil bajara oladi.

---

## Kerakli oldingi bilimlar

- 1-dars: print() funksiyasi;
- 2-dars: O'zgaruvchilar va turlar;
- 3-dars: input() funksiyasi.

---

# 1. Asosiy tushunchalar

## String (str) nima?

> **String** — bu belgilar (harflar, raqamlar, bo'sh joy, maxsus belgilar) ketma-ketligi. Python'da qo'shtirnoq ichida yoziladi: `"Salom"` yoki `'Salom'`.

## Indeks nima?

> **Indeks** — bu stringdagi har bir belgining tartib raqami. Python'da indeks 0 dan boshlanadi: `"Python"[0]` = `"P"`. Manfiy indeks oxiridan sanaydi: `"Python"[-1]` = `"n"`.

## Slicing nima?

> **Slicing (kesish)** — bu stringdan ma'lum qismni ajratib olish: `"Python"[0:3]` = `"Pyt"`. Sintaksis: `string[boshlanish:tugash:qadam]`.

## Immutability nima?

> **Immutability (o'zgarmaslik)** — stringdagi alohida belgini o'zgartirib bo'lmaydi. `s[0] = "X"` xato beradi. Buning o'rniga yangi string yaratish kerak.

---

# 2. Sintaksis

```python
matn = "Salom, Dunyo!"
print(matn[0])
print(matn[-1])
print(matn[0:5])
print(len(matn))
```

---

# 3. String metodlari jadvali

| Metod | Vazifasi | Misol | Natija |
|---|---|---|---|
| `upper()` | Barchasini katta harfga | `"salom".upper()` | `"SALOM"` |
| `lower()` | Barchasini kichik harfga | `"SALOM".lower()` | `"salom"` |
| `capitalize()` | Birinchi harfni katta | `"salom".capitalize()` | `"Salom"` |
| `title()` | Har so'z boshini katta | `"salom dunyo".title()` | `"Salom Dunyo"` |
| `strip()` | Bosh/oxirdagi bo'sh joy olib tashlash | `"  salom  ".strip()` | `"salom"` |
| `replace(a, b)` | a ni b ga almashtirish | `"salom".replace("s","S")` | `"Salom"` |
| `split(sep)` | Matnni bo'laklarga ajratish | `"a,b,c".split(",")` | `["a","b","c"]` |
| `join(list)` | Listni matnga birlashtirish | `"-".join(["a","b"])` | `"a-b"` |
| `find(sub)` | Qism matn indeksini topish | `"salom".find("lo")` | `2` |
| `count(sub)` | Necha marta uchrashini sanash | `"salom".count("a")` | `1` |
| `startswith(s)` | Boshlanishini tekshirish | `"salom".startswith("sa")` | `True` |
| `endswith(s)` | Tugashini tekshirish | `"salom".endswith("om")` | `True` |
| `isdigit()` | Faqat raqamlardan iboratmi | `"123".isdigit()` | `True` |
| `isalpha()` | Faqat harflardan iboratmi | `"abc".isalpha()` | `True` |
| `center(n, ch)` | Matnni markazga joylashtirish | `"hi".center(10, "-")` | `"----hi----"` |
| `zfill(n)` | Chapga nol qo'shish | `"42".zfill(5)` | `"00042"` |

---

# 4. Kod misollari

## Misol 1 — String yaratish

```python
s1 = "Salom"
s2 = 'Dunyo'
print(s1, s2)
print(s1 + " " + s2)
```

Natija:

```
Salom Dunyo
Salom Dunyo
```

Qachon ishlatiladi: Har qanday dasturda matnli ma'lumotlarni saqlashda.

---

## Misol 2 — Indekslash

```python
til = "Python"
print(til[0])
print(til[3])
print(til[-1])
print(til[-2])
```

Natija:

```
P
h
n
o
```

Qatorma-qator izoh:
- `til[0]` = `"P"` (birinchi belgi, indeks 0 dan boshlanadi);
- `til[-1]` = `"n"` (oxirgi belgi);
- `til[-2]` = `"o"` (oxiridan ikkinchi).

---

## Misol 3 — Slicing

```python
matn = "Dasturlash"
print(matn[0:5])
print(matn[5:])
print(matn[:5])
print(matn[::2])
print(matn[::-1])
```

Natija:

```
Dastu
rlash
Dastu
Dsuls
hsalrutsaD
```

Qatorma-qator izoh:
- `[0:5]` — 0 dan 5 gacha (5 kirmaydi);
- `[5:]` — 5 dan oxirigacha;
- `[:5]` — boshidan 5 gacha;
- `[::2]` — har ikkinchi belgi;
- `[::-1]` — teskari tartibda (stringni aylantirish).

---

## Misol 4 — upper(), lower(), capitalize(), title()

```python
matn = "salom, dunyo!"
print(matn.upper())
print(matn.lower())
print(matn.capitalize())
print(matn.title())
```

Natija:

```
SALOM, DUNYO!
salom, dunyo!
Salom, dunyo!
Salom, Dunyo!
```

---

## Misol 5 — strip(), replace()

```python
matn = "   Salom, Dunyo!   "
print(matn.strip())
yangi = matn.strip().replace("Dunyo", "Python")
print(yangi)
```

Natija:

```
Salom, Dunyo!
Salom, Python!
```

---

## Misol 6 — split() va join()

```python
jumla = "Python,Java,C++,JavaScript"
tillar = jumla.split(",")
print(tillar)

birlashtirish = " | ".join(tillar)
print(birlashtirish)
```

Natija:

```
['Python', 'Java', 'C++', 'JavaScript']
Python | Java | C++ | JavaScript
```

---

## Misol 7 — find(), count(), in operatori

```python
matn = "Python dasturlash tili. Python yaxshi!"

print(matn.find("Python"))
print(matn.find("Java"))
print(matn.count("Python"))
print("Python" in matn)
print("Java" in matn)
```

Natija:

```
0
-1
2
True
False
```

---

## Misol 8 — Tekshirish metodlari

```python
print("12345".isdigit())
print("salom".isalpha())
print("salom123".isalnum())
print("   ".isspace())
print("salom".islower())
print("SALOM".isupper())
```

Natija:

```
True
True
True
True
True
True
```

---

# 5. Real loyiha misoli — Email tekshiruvchi

```python
email = input("Email kiriting: ").strip().lower()

xatolar = []

if "@" not in email:
    xatolar.append("@ belgisi yo'q")
elif email.count("@") > 1:
    xatolar.append("Bir nechta @ belgisi bor")

if "." not in email:
    xatolar.append(". belgisi yo'q")

if " " in email:
    xatolar.append("Bo'sh joy bo'lmasligi kerak")

if xatolar:
    print("Xatolar topildi:")
    for x in xatolar:
        print(f"  - {x}")
else:
    print(f"'{email}' to'g'ri email!")
```

---

# 6. Ko'p uchraydigan xatolar

## Xato 1: Stringda belgini o'zgartirish

Noto'g'ri:

```python
s = "Salom"
s[0] = "X"
```

Nima uchun xato: Stringlar immutable — alohida belgini o'zgartirib bo'lmaydi.

To'g'ri:

```python
s = "Salom"
s = "X" + s[1:]
```

## Xato 2: find() o'rniga index() ishlatish

Noto'g'ri:

```python
"salom".index("xyz")
```

Nima uchun xato: `index()` topilmasa `ValueError` beradi.

To'g'ri:

```python
pos = "salom".find("xyz")
if pos != -1:
    print("Topildi")
```

## Xato 3: split() ga noto'g'ri ajratuvchi

Noto'g'ri:

```python
"a,b,c".split(" ")
```

Nima uchun xato: Bo'sh joy bo'yicha ajratadi, lekin vergul bor.

To'g'ri:

```python
"a,b,c".split(",")
```

## Xato 4: Matn va sonni + bilan birlashtirish

Noto'g'ri:

```python
"Yosh: " + 20
```

Nima uchun xato: `TypeError`. `+` matn va sonni birlashtira olmaydi.

To'g'ri:

```python
"Yosh: " + str(20)
f"Yosh: {20}"
```

---

# 7. Sinfdagi amaliy topshiriqlar

## 1-topshiriq — Oson

**Vazifa:** Foydalanuvchidan jumla oling va harflar sonini, so'zlar sonini va birinchi harfni chiqaring.

## 2-topshiriq — O'rta

**Vazifa:** Foydalanuvchidan gap oling, undagi barcha bo'sh joylarni `_` ga, kichik harflarni katta harfga almashtiring.

## 3-topshiriq — Murakkab

**Vazifa:** Palindromni tekshiruvchi dastur yozing: foydalanuvchi so'z kiritadi, dastur uning teskari yozilishi bilan bir xil ekanligini aniqlaydi.

---

# 8. Uyga vazifa

1. To'liq ism oling va bosh harflarini chiqaring: "Ali Valiyev" = "A.V.".
2. Berilgan matnda eng ko'p uchraydigan harfni toping.
3. So'zlarni teskari tartibda chiqaring: "Salom Dunyo" = "Dunyo Salom".
4. Telefon raqamini formatlang: "998901234567" = "+998 (90) 123-45-67".
5. Matnda unli harflar sonini hisoblang.

---

# 9. Tekshirish savollari

1. String nima va Python'da qanday yaratiladi?
2. Indeks nima va nima uchun 0 dan boshlanadi?
3. Manfiy indeks nima va qachon ishlatiladi?
4. Slicing sintaksisi qanday?
5. upper() va capitalize() o'rtasidagi farq nima?
6. split() va join() o'rtasidagi farq nima?
7. find() va index() o'rtasidagi farq nima?
8. String immutability nima?
9. `in` operatori stringlarda qanday ishlaydi?
10. f-string va .format() o'rtasidagi farq nima?

---

## Javoblar

**1.** String — belgilar ketma-ketligi. Qo'shtirnoq ichida yaratiladi: `"Salom"`, `'Salom'`. Python'da `str` turi bilan ifodalanadi.

**2.** Indeks — stringdagi belgining tartib raqami. 0 dan boshlanadi chunki kompyuter xotirasida birinchi element ofset 0 da joylashadi.

**3.** Manfiy indeks oxiridan sanaydi: `[-1]` — oxirgi belgi, `[-2]` — oxiridan ikkinchi. String uzunligini bilmasdan oxirgi elementga murojaat qilish uchun qulay.

**4.** `string[start:stop:step]` — `start` dan `stop` gacha (stop kirmaydi), `step` qadam bilan. Har birini tushirish mumkin.

**5.** `upper()` — barcha harflarni katta qiladi. `capitalize()` — faqat birinchi harfni katta, qolganini kichik qiladi.

**6.** `split()` — matnni listga ajratadi. `join()` — list elementlarini matnga birlashtiradi. Ular bir-birining teskari amali.

**7.** `find()` — topilmasa `-1` qaytaradi. `index()` — topilmasa `ValueError` xatosi beradi. Xavfsiz kod uchun `find()` ishlatish tavsiya etiladi.

**8.** Immutability — stringdagi alohida belgini o'zgartirib bo'lmaydi. Buning o'rniga yangi string yaratish kerak.

**9.** `"Python" in "Men Python o'rganaman"` = `True`. `in` operatori bitta stringning boshqa string ichida mavjudligini tekshiradi.

**10.** `f-string` (`f"Ism: {ism}"`) Python 3.6+ da qo'shilgan va eng tez usul. `.format()` eski usul, lekin hali ham ishlaydi.

---

# 10. Qisqa xulosa

Bu darsda:

- String yaratish va xususiyatlari;
- Indekslash va slicing;
- 16 ta string metodi;
- f-string formatlash;
- String immutability

o'rganildi.

---

Keyingi **5-dars: If/elif/else** da shartli operatorlar — dasturning turli sharoitlarga qarab turli yo'llardan borishini boshqarish o'rganiladi.

---

# Resurslar va fayllar

- 📄 String Methods: https://docs.python.org/3/library/stdtypes.html#string-methods
- 💻 Kodlar: `github.com/dars-reja/04-dars`
- 🎬 Video dars: `youtube.com/watch?v=dars04`
