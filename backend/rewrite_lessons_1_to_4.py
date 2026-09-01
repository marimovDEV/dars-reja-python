import os
import sys
import json
import django

sys.path.append(os.path.dirname(__file__))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from lessons_app.models import Lesson

LESSONS_JSON = os.path.join(os.path.dirname(__file__), "..", "frontend", "src", "data", "lessons.json")

# ============================================================================
# 1-DARSDAN 12-DARSGACHA TO'LIQ PROFESSIONAL DOKUMENTATSIYA (19 BO'LIMLI SHABLON)
# ============================================================================

FULL_DOCS = {}

# ===== 1-DARS =====
FULL_DOCS[1] = r"""# 💻 1. Dasturlash muhiti va Python — Dars dokumentatsiyasi

Python — bu dunyodagi eng mashhur va o'rganish uchun eng qulay dasturlash tillaridan biri. U 1991-yilda Guido van Rossum tomonidan yaratilgan bo'lib, hozirda veb-dasturlash, sun'iy intellekt, data science, avtomatlashtirish va boshqa ko'plab sohalarda keng qo'llaniladi.

Dasturlash muhiti (Development Environment) — bu kod yozish, ishga tushirish va xatolarni topish uchun ishlatiladigan asboblar to'plami. Python'da kod yozish uchun oddiy matn muharriri (Notepad) ham yetarli, lekin professional ishda maxsus dasturlar — IDE (Integrated Development Environment) va kod muharrirlari ishlatiladi.

Bu darsda siz Python'ni kompyuteringizga o'rnatishni, birinchi dasturingizni yozishni va uni ishga tushirishni o'rganasiz. Bu sizning dasturchilik yo'lingizning birinchi qadami.

---

## Bu mavzu orqali nimalar qilish mumkin

- Python dasturlash tilini kompyuterga o'rnatish;
- VS Code yoki PyCharm muhitini sozlash;
- Terminal (cmd/PowerShell) orqali Python'ni ishga tushirish;
- Birinchi `print()` dasturini yozish va natijani ko'rish;
- Python interaktiv rejimida (`>>>`) tajriba qilish;
- `.py` fayllarni yaratish va ishga tushirish.

---

## Dars maqsadi

Bu dars oxirida o'quvchi:

- Python'ni o'rnatish va versiyasini tekshirish (`python --version`);
- VS Code yoki PyCharm'da Python loyiha yaratish;
- `print()` funksiyasi yordamida matn chiqarish;
- Terminal orqali `.py` faylini ishga tushirish;
- Python interaktiv rejimida ishlash

ni mustaqil bajara oladi.

---

## Kerakli oldingi bilimlar

Bu darsni tushunish uchun:

- Kompyuterda fayl va papkalar bilan ishlash;
- Brauzer orqali dastur yuklab o'rnatish;
- Klaviaturada matn yozish

bilinishi kerak.

---

# 1. Asosiy tushunchalar va atamalar

## Python nima?

> **Python** — bu yuqori darajali, interpretatsiya qilinadigan, ko'p maqsadli dasturlash tili. Uning sintaksisi oddiy va ingliz tiliga yaqin bo'lgani uchun yangi boshlovchilar uchun eng qulay til hisoblanadi.

## IDE nima?

> **IDE (Integrated Development Environment)** — bu kod yozish, ishga tushirish, xatolarni topish (debugging) va loyihani boshqarish imkonini beradigan yagona dastur. Masalan: PyCharm, VS Code.

## Terminal nima?

> **Terminal** — bu kompyuterga matnli buyruqlar orqali ko'rsatma beradigan dastur. Python fayllarini terminal orqali ishga tushirish mumkin: `python fayl.py`.

## Interpreter nima?

> **Interpreter** — bu Python kodini satrma-satr o'qib, har bir satrni darhol bajaradigan dastur. Python kompilyatsiya qilinmaydi, balki interpretatsiya qilinadi.

## `print()` funksiyasi nima?

> **`print()`** — bu Python'dagi eng asosiy funksiya bo'lib, qavs ichidagi ma'lumotni ekranga (terminalga) chiqaradi.

---

# 2. Sintaksis va uning izohi

```python
print("Salom, Dunyo!")
```

- `print` — bu Python'ning ichki (built-in) funksiyasi;
- `(` va `)` — funksiyaga argument berish uchun qavslar;
- `"Salom, Dunyo!"` — ekranga chiqariladigan matn (string). Qo'shtirnoq ichida yoziladi;
- Har bir buyruq alohida qatorda yoziladi;
- Python'da satr oxirida nuqta-vergul (`;`) qo'yish shart emas.

---

# 3. Asosiy buyruqlar jadvali

| Buyruq / Funksiya | Vazifasi | Misol | Natija |
|---|---|---|---|
| `print()` | Ekranga matn/qiymat chiqarish | `print("Salom")` | `Salom` |
| `print(a, b)` | Bir nechta qiymatni chiqarish | `print("Ism:", "Ali")` | `Ism: Ali` |
| `print(a, end="")` | Yangi qatorga o'tmaslik | `print("A", end="-")` | `A-` |
| `print(a, sep=",")` | Ajratuvchi belgi o'zgartirish | `print("a", "b", sep=",")` | `a,b` |
| `# izoh` | Kod izohi (bajarilmaydi) | `# bu izoh` | — |
| `python --version` | Python versiyasini ko'rish | Terminal: `python --version` | `Python 3.12.0` |
| `python fayl.py` | Faylni ishga tushirish | Terminal: `python salom.py` | Faylni bajaradi |
| `python` | Interaktiv rejim | Terminal: `python` | `>>>` paydo bo'ladi |
| `exit()` | Interaktiv rejimdan chiqish | `>>> exit()` | Terminalga qaytadi |

---

# 4. Kod misollari

## Misol 1 — Eng sodda dastur

```python
print("Salom, Dunyo!")
```

Natija:

```
Salom, Dunyo!
```

Qatorma-qator izoh:
- `print("Salom, Dunyo!")` — `print` funksiyasi qavs ichidagi matnni ekranga chiqaradi. Matn qo'shtirnoq (`"..."`) ichida yoziladi.

Qachon ishlatiladi: Har qanday dasturda foydalanuvchiga xabar ko'rsatish uchun.

---

## Misol 2 — Bir nechta print

```python
print("Mening ismim Ali.")
print("Men 20 yoshdaman.")
print("Men Python o'rganmoqdaman.")
```

Natija:

```
Mening ismim Ali.
Men 20 yoshdaman.
Men Python o'rganmoqdaman.
```

Qatorma-qator izoh:
- Har bir `print()` alohida qatorda natija chiqaradi;
- Python kodni yuqoridan pastga, ketma-ket bajaradi.

Qachon ishlatiladi: Bir nechta satr ma'lumotni ko'rsatish kerak bo'lganda.

---

## Misol 3 — Bir nechta argument

```python
print("Ism:", "Sardor", "Yosh:", 22)
```

Natija:

```
Ism: Sardor Yosh: 22
```

Qatorma-qator izoh:
- `print()` ga vergul bilan bir nechta argument berish mumkin;
- Argumentlar orasiga avtomatik bo'sh joy qo'yiladi;
- Son (`22`) ham matn (`"Sardor"`) ham berilishi mumkin.

Qachon ishlatiladi: Bir qatorda har xil turdagi ma'lumotlarni birga chiqarish uchun.

---

## Misol 4 — sep parametri

```python
print("2024", "09", "01", sep="-")
```

Natija:

```
2024-09-01
```

Qatorma-qator izoh:
- `sep="-"` — argumentlar orasidagi ajratuvchini bo'sh joy o'rniga `-` belgisiga o'zgartiradi;
- Bu sana, IP manzil, yo'l kabi formatlarni chiqarishda juda qulay.

Qachon ishlatiladi: Ma'lumotlarni maxsus formatda (sana, vaqt) chiqarish kerak bo'lganda.

---

## Misol 5 — end parametri

```python
print("Yuklanmoqda", end="...")
print("Tayyor!")
```

Natija:

```
Yuklanmoqda...Tayyor!
```

Qatorma-qator izoh:
- Odatda `print()` oxirida yangi qatorga o'tadi (`\n`);
- `end="..."` buni o'zgartiradi — yangi qator o'rniga `...` qo'yiladi;
- Ikkinchi `print()` shu qator davomida chiqadi.

Qachon ishlatiladi: Progressbar, yuklanish holati yoki bir qatorda natija chiqarish uchun.

---

## Misol 6 — Izohlar (comments)

```python
# Bu dastur salom beradi
print("Salom!")  # Bu qator ekranga "Salom!" chiqaradi

# Quyidagi qator bajarilmaydi:
# print("Bu ko'rinmaydi")
```

Natija:

```
Salom!
```

Qatorma-qator izoh:
- `#` belgisidan keyingi hamma narsa izoh hisoblanadi va Python uni o'tkazib yuboradi;
- Izohlar kodni tushuntirish uchun yoziladi;
- Qatorning oxiriga ham izoh qo'shish mumkin.

Qachon ishlatiladi: Kodni boshqa dasturchilar (yoki kelajakdagi o'zingiz) tushunishi uchun.

---

## Misol 7 — Ko'p qatorli matn

```python
print("""Bu birinchi qator.
Bu ikkinchi qator.
Bu uchinchi qator.""")
```

Natija:

```
Bu birinchi qator.
Bu ikkinchi qator.
Bu uchinchi qator.
```

Qatorma-qator izoh:
- Uchta qo'shtirnoq (`"""..."""`) ko'p qatorli matnni yozish imkonini beradi;
- Har bir qator aynan yozilganidek chiqadi.

Qachon ishlatiladi: Uzun matnlar, yo'riqnomalar yoki ASCII art chiqarishda.

---

## Misol 8 — Maxsus belgilar

```python
print("Ism:\tAli")
print("Familiya:\tValiyev")
print("---")
print("Birinchi qator\nIkkinchi qator")
print("---")
print("U shunday dedi: \"Python zo'r!\"")
```

Natija:

```
Ism:	Ali
Familiya:	Valiyev
---
Birinchi qator
Ikkinchi qator
---
U shunday dedi: "Python zo'r!"
```

Qatorma-qator izoh:
- `\t` — tab (katta bo'sh joy) belgisi;
- `\n` — yangi qatorga o'tish belgisi;
- `\"` — qo'shtirnoqni matn ichida ko'rsatish uchun (escape character);
- Bu belgilar `escape sequences` deyiladi.

Qachon ishlatiladi: Jadvallar, formatli chiqishlar va maxsus belgilar kerak bo'lganda.

---

# 5. Real loyiha misoli — Vizitkarta dasturi

```python
print("=" * 40)
print("       VIZITKARTA")
print("=" * 40)
print()
print("Ism:          Ali Valiyev")
print("Kasb:         Python Backend Developer")
print("Telefon:      +998 90 123 45 67")
print("Email:        ali@example.com")
print("GitHub:       github.com/ali-valiyev")
print()
print("=" * 40)
print("  Python | Django | PostgreSQL | Docker")
print("=" * 40)
```

Natija:

```
========================================
       VIZITKARTA
========================================

Ism:          Ali Valiyev
Kasb:         Python Backend Developer
Telefon:      +998 90 123 45 67
Email:        ali@example.com
GitHub:       github.com/ali-valiyev

========================================
  Python | Django | PostgreSQL | Docker
========================================
```

Izoh:
- `"=" * 40` — `=` belgisini 40 marta takrorlaydi (string ko'paytirish);
- `print()` — bo'sh qator chiqaradi;
- Bu dastur faqat `print()` dan foydalanadi, lekin chiroyli natija beradi.

---

# 6. Ko'p uchraydigan xatolar

## Xato 1: Qo'shtirnoq unutilishi

Noto'g'ri:

```python
print(Salom)
```

Nima uchun xato: `Salom` qo'shtirnoqsiz yozilsa, Python uni o'zgaruvchi deb o'ylaydi va `NameError: name 'Salom' is not defined` xatosini beradi.

To'g'ri:

```python
print("Salom")
```

Qanday oldini olish: Matnni doim qo'shtirnoq (`"..."` yoki `'...'`) ichida yozing.

---

## Xato 2: Qavsni yopmaslik

Noto'g'ri:

```python
print("Salom"
```

Nima uchun xato: `SyntaxError: unexpected EOF while parsing` — Python ochilgan qavsning yopilishini kutadi.

To'g'ri:

```python
print("Salom")
```

Qanday oldini olish: Har bir ochilgan qavsni yopishni unutmang. VS Code kabi IDE lar buni avtomatik qiladi.

---

## Xato 3: Print so'zini katta harf bilan yozish

Noto'g'ri:

```python
Print("Salom")
```

Nima uchun xato: Python katta-kichik harfga sezgir (case-sensitive). `Print` va `print` — ikki xil narsa.

To'g'ri:

```python
print("Salom")
```

Qanday oldini olish: Python'dagi barcha built-in funksiyalar kichik harfda yoziladi.

---

## Xato 4: Noto'g'ri qo'shtirnoq juftligi

Noto'g'ri:

```python
print("Salom')
```

Nima uchun xato: Ochilish (`"`) va yopilish (`'`) qo'shtirnoqlari har xil. Python ularni moslashtira olmaydi.

To'g'ri:

```python
print("Salom")
print('Salom')
```

Qanday oldini olish: Har doim bir xil turdagi qo'shtirnoq ishlating: ikkalasi `"` yoki ikkalasi `'`.

---

# 7. Sinfdagi amaliy topshiriqlar

## 1-topshiriq — Oson

**Vazifa:** `print()` yordamida o'z ismingiz, familiyangiz va yoshingizni 3 ta alohida qatorda chiqaring.

Kutilgan natija:

```
Ali
Valiyev
20
```

---

## 2-topshiriq — O'rta

**Vazifa:** `sep` va `end` parametrlarini ishlatib, quyidagi natijani bitta `print()` buyrug'i bilan chiqaring:

```
2024/09/01
```

---

## 3-topshiriq — Murakkab

**Vazifa:** Faqat `print()` va `*` operatori yordamida quyidagi rasmni chiqaring:

```
*
**
***
****
*****
```

---

# 8. Uyga vazifa

1. Python'ni kompyuteringizga o'rnating va `python --version` buyrug'i natijasini screenshotga oling.
2. VS Code'da `salom.py` fayl yarating va undagi `print()` yordamida o'z ismingizni chiqaring.
3. `sep` parametri yordamida telefon raqamini `+998-90-123-45-67` formatida chiqaring.
4. `end` parametri yordamida 5 ta so'zni bitta qatorda, orasida `*` belgisi bilan chiqaring.
5. `"""..."""` yordamida 5 qatorlik she'r chiqaring.

---

# 9. Tekshirish savollari

1. Python qaysi yilda va kim tomonidan yaratilgan?
2. IDE nima va qanday IDElarni bilasiz?
3. `print()` funksiyasining vazifasi nima?
4. `print("a", "b", sep="-")` natijasi nima bo'ladi?
5. `print("Salom", end="!")` dan keyin `print("Dunyo")` natijasi nima?
6. `#` belgisi Python'da nima vazifani bajaradi?
7. `\n` va `\t` maxsus belgilarining farqi nima?
8. `print("=" * 20)` natijasi nima bo'ladi?
9. `Print("Salom")` nima uchun xato beradi?
10. Python interaktiv rejimiga qanday kirish va chiqish mumkin?

---

## Javoblar

**1.** Python 1991-yilda Gollandiyalik dasturchi Guido van Rossum tomonidan yaratilgan. U oddiy va o'qilishi oson sintaksisga ega bo'lgan yuqori darajali dasturlash tilidir.

**2.** IDE (Integrated Development Environment) — kod yozish, ishga tushirish va xatolarni topish uchun yagona muhit. Mashhur IDElar: PyCharm (Python uchun maxsus), VS Code (universal), Jupyter Notebook (data science uchun).

**3.** `print()` — Python'ning ichki funksiyasi bo'lib, qavs ichidagi argument(lar)ni ekranga (terminalga) chiqaradi. U matn, son va boshqa turdagi ma'lumotlarni ko'rsatish uchun ishlatiladi.

**4.** Natija: `a-b`. `sep="-"` parametri argumentlar orasidagi standart bo'sh joyni `-` belgisiga almashtiradi.

**5.** Natija: `Salom!Dunyo`. Birinchi `print` oxirida yangi qator o'rniga `!` qo'yiladi, shuning uchun ikkinchi `print` shu qator davomida chiqadi.

**6.** `#` belgisi izoh (comment) boshlanishini bildiradi. `#` dan keyingi barcha matn Python tomonidan o'tkazib yuboriladi va bajarilmaydi. U kodni tushuntirish uchun ishlatiladi.

**7.** `\n` — yangi qatorga o'tish (newline), `\t` — gorizontal tab (katta bo'sh joy). Ikkalasi ham escape sequence bo'lib, matn ichida maxsus formatlash uchun ishlatiladi.

**8.** Natija: `====================` (20 ta `=` belgisi). Python'da stringni songa ko'paytirish uni takrorlaydi.

**9.** `NameError: name 'Print' is not defined` xatosi beradi. Python case-sensitive til, ya'ni `Print` va `print` har xil nom. Built-in funksiyalar doim kichik harfda yoziladi.

**10.** Interaktiv rejimga kirish: terminalda `python` yoki `python3` buyrug'ini yozing — `>>>` belgisi paydo bo'ladi. Chiqish: `exit()` funksiyasini yozing yoki `Ctrl+D` (Mac/Linux) / `Ctrl+Z + Enter` (Windows) bosing.

---

# 10. Qisqa xulosa

Bu darsda:

- Python dasturlash tili va uning tarixi;
- IDE (VS Code, PyCharm) va terminal tushunchalari;
- `print()` funksiyasi va uning `sep`, `end` parametrlari;
- Izohlar (`#`), maxsus belgilar (`\n`, `\t`, `\"`);
- Python'ni o'rnatish va birinchi dasturni ishga tushirish

o'rganildi.

---

Keyingi **2-dars: O'zgaruvchilar va turlar** da ma'lumotlarni xotirada saqlash, o'zgaruvchi yaratish va Python'dagi asosiy ma'lumot turlari (`int`, `float`, `str`, `bool`) o'rganiladi.

---

# Resurslar va fayllar

- 📄 Python rasmiy sayti: https://www.python.org
- 📄 VS Code yuklab olish: https://code.visualstudio.com
- 📄 Python rasmiy hujjat: https://docs.python.org/3/tutorial/
- 💻 Kodlar: `github.com/dars-reja/01-dars`
- 🎬 Video dars: `youtube.com/watch?v=dars01`
"""

# ===== 2-DARS =====
FULL_DOCS[2] = r"""# 📦 2. O'zgaruvchilar va turlar — Dars dokumentatsiyasi

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
# TO'G'RI nomlar:
ism = "Ali"
yosh_2024 = 20
_maxfiy = "sir"
MAX_SIZE = 100
user_name = "admin"

# NOTO'G'RI nomlar (xato beradi):
# 2ism = "Ali"       # raqam bilan boshlanmaydi
# ism-familiya = ""  # tire ishlatilmaydi
# class = "sinf"     # kalit so'z ishlatilmaydi

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
- Python kalit so'zlari (`if`, `for`, `class`, `return` va boshqalar) nom sifatida ishlatilmaydi;
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
print(f"  HOLAT:     {'Faol' if ishlayaptimi else 'Nofaol'}")
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
if x = 10:  # SyntaxError!
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

**Vazifa:** 4 ta o'zgaruvchi yarating: `ism` (str), `yosh` (int), `bo'y` (float), `talabami` (bool). Har birini `f-string` yordamida bir qatorda chiqaring.

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
...
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
"""

# ===== 3-DARS =====
FULL_DOCS[3] = r"""# ⌨️ 3. Input va arifmetika — Dars dokumentatsiyasi

`input()` funksiyasi — bu foydalanuvchidan klaviatura orqali ma'lumot olish uchun ishlatiladigan Python'ning ichki funksiyasi. Dastur `input()` ga yetganda to'xtaydi va foydalanuvchi matn kiritib Enter bosguncha kutadi. `input()` har doim `str` (matn) qaytaradi — son kiritilgan bo'lsa ham.

Arifmetik operatorlar — bu sonlar ustida matematik amallar bajarish uchun ishlatiladigan belgilar. Python'da 7 ta asosiy arifmetik operator bor: qo'shish (`+`), ayirish (`-`), ko'paytirish (`*`), bo'lish (`/`), butun bo'lish (`//`), qoldiq (`%`) va daraja (`**`).

`input()` va arifmetika birgalikda ishlaganda, foydalanuvchi kiritgan ma'lumotni songa aylantirish (`int()` yoki `float()`) va ustida hisob-kitob bajarish mumkin bo'ladi. Bu real dasturlarning asosi — kalkulyator, savdo tizimi, maosh hisoblash kabi ilovalar shu tamoyilga qurilgan.

---

## Bu mavzu orqali nimalar qilish mumkin

- Foydalanuvchidan matn va son olish;
- Arifmetik amallar bajarish;
- `input()` natijasini songa aylantirish;
- Kalkulyator va hisob-kitob dasturlari yozish;
- Operatorlar ustunligini (prioritetini) tushunish.

---

## Dars maqsadi

Bu dars oxirida o'quvchi:

- `input()` funksiyasidan foydalanish;
- Barcha 7 ta arifmetik operatorni bilish;
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

## Operatorlar ustuniigi (Operator Precedence) nima?

> **Operatorlar ustuniigi** — bu Python bir satrda bir nechta operator bo'lganda qaysi birini avval bajarishini belgilaydigan qoida. Masalan: `2 + 3 * 4 = 14` (avval `*`, keyin `+`).

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

## Operatorlar ustuniigi jadvali (yuqoridan pastga — avval bajariladi)

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

Qatorma-qator izoh:
- `/` — har doim `float` qaytaradi (`3.4`);
- `//` — kasrni tashlaydi (`3`);
- `%` — 17 ni 5 ga bo'lganda 3 ta to'liq, 2 qoldiq;
- `**` — 17 ning 5-darajasi.

Qachon ishlatiladi: Matematik hisob-kitoblar, algoritmlar va formulalar.

---

## Misol 4 — Operatorlar ustuniigi

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
- Ikkinchisida: avval qavs `(2 + 3) = 5`, keyin `5 * 4 = 20`;
- Qavslar har doim birinchi bajariladi.

Qachon ishlatiladi: Murakkab formulalar yozganda tartibni nazorat qilish uchun.

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

Qatorma-qator izoh:
- `float(input(...))` — kasrli sonlarni ham qabul qiladi;
- `son2 != 0` — nolga bo'lishdan himoya qiladi.

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

Qatorma-qator izoh:
- `son % 2` — sonni 2 ga bo'lgandagi qoldiq;
- Qoldiq 0 bo'lsa juft, 1 bo'lsa toq.

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

Qatorma-qator izoh:
- `math.pi` — π ning aniq qiymati (3.14159...);
- `radius ** 2` — radiusning kvadrati;
- `:.2f` — natijani 2 ta kasr bilan chiqaradi.

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

Qatorma-qator izoh:
- `brutto * 0.12` — 12% soliq hisoblash;
- `:,.2f` — sonni minglik ajratuvchi bilan formatlash (`8,000,000.00`).

Qachon ishlatiladi: Buxgalteriya, ish haqi va moliyaviy hisob-kitoblarda.

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
print(f"  💵 {usd:,.2f} AQSh dollari")
print(f"  💶 {eur:,.2f} Yevro")
print(f"\nKurslar: 1 USD = {usd_kurs:,.0f}, 1 EUR = {eur_kurs:,.0f}")
```

---

# 6. Ko'p uchraydigan xatolar

## Xato 1: input() natijasini songa aylantirsiz hisoblash

Noto'g'ri:

```python
son = input("Son: ")
print(son + 5)  # TypeError!
```

Nima uchun xato: `input()` doim `str` qaytaradi. `"10" + 5` matn va sonni qo'sha olmaydi.

To'g'ri:

```python
son = int(input("Son: "))
print(son + 5)
```

---

## Xato 2: Nolga bo'lish

Noto'g'ri:

```python
print(10 / 0)  # ZeroDivisionError!
```

To'g'ri:

```python
if b != 0:
    print(10 / b)
else:
    print("Nolga bo'lish mumkin emas!")
```

---

## Xato 3: Kasrli sonni int() ga o'tkazish

Noto'g'ri:

```python
son = int(input("Son: "))  # Foydalanuvchi "3.5" kiritse ValueError
```

To'g'ri:

```python
son = float(input("Son: "))
```

---

## Xato 4: Qavslarni unutish

Noto'g'ri:

```python
natija = 100 + 20 * 0.12  # 100 + 2.4 = 102.4 (noto'g'ri)
```

To'g'ri:

```python
natija = (100 + 20) * 0.12  # 120 * 0.12 = 14.4
```

Qanday oldini olish: Murakkab formulalarda doim qavslardan foydalaning.

---

# 7. Sinfdagi amaliy topshiriqlar

## 1-topshiriq — Oson

**Vazifa:** Foydalanuvchidan ikkita son oling va ularning yig'indisi, ayirmasi va ko'paytmasini chiqaring.

## 2-topshiriq — O'rta

**Vazifa:** Foydalanuvchidan to'rtburchakning eni va bo'yini oling, yuzasi va perimetrini hisoblang.

## 3-topshiriq — Murakkab

**Vazifa:** Foydalanuvchidan 3 ta fan bahosini oling, o'rtacha bahoni hisoblang va `"A'lo"` (90+), `"Yaxshi"` (70+) yoki `"Qoniqarli"` (boshqa) deb baholang.

---

# 8. Uyga vazifa

1. Sodda kalkulyator yozing: 2 ta son va 1 ta operator (`+`, `-`, `*`, `/`) olib natijani chiqarsin.
2. Foydalanuvchidan Selsiy haroratni oling va Farengeytga aylantiring (`F = C * 9/5 + 32`).
3. Foydalanuvchidan mahsulot narxi va miqdorini oling, jami summani va 15% chegirmali summani chiqaring.
4. Sonning raqamlar yig'indisini toping: masalan `123` → `1 + 2 + 3 = 6` (faqat 3 xonali sonlar uchun).
5. Foydalanuvchidan sekundlar sonini oling va soat:minut:sekund formatida chiqaring.

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

**1.** `input()` har doim `str` (string, matn) turini qaytaradi — foydalanuvchi son kiritgan bo'lsa ham. Masalan, foydalanuvchi `25` kiritse, natija `"25"` (matn).

**2.** `int(input("..."))` — butun songa aylantirish, `float(input("..."))` — kasrli songa aylantirish. `int()` yoki `float()` funksiyasi bilan o'rash kerak.

**3.** `/` — oddiy bo'lish, natija har doim `float`: `7 / 2 = 3.5`. `//` — butun bo'lish, kasrni tashlaydi: `7 // 2 = 3`. Manfiy sonlarda `//` pastga yaxlitlaydi: `-7 // 2 = -4`.

**4.** `%` (modulo) — bo'lishdan keyin qolgan qoldiqni qaytaradi. `17 % 5 = 2` (17 ni 5 ga bo'lganda 3 to'liq, 2 qoldiq). Juft/toq aniqlash uchun keng ishlatiladi.

**5.** Natija: `14`. Sabab: `*` operatori `+` dan ustunroq, shuning uchun avval `3 * 4 = 12` hisoblanadi, keyin `2 + 12 = 14`.

**6.** `**` — daraja (exponentiation) operatori. `2 ** 10 = 1024` (2 ning 10-chi darajasi). Barcha operatorlar ichida eng yuqori ustunlikka ega.

**7.** `ZeroDivisionError: division by zero` xatosi chiqadi. Python nolga bo'lishga ruxsat bermaydi. Oldini olish uchun bo'lishdan oldin `if b != 0:` tekshiruvi qo'yish kerak.

**8.** `int(input())` — faqat butun sonlarni qabul qiladi (`25`), kasrli son kiritilsa `ValueError` beradi. `float(input())` — ham butun (`25` → `25.0`), ham kasrli (`3.14`) sonlarni qabul qiladi.

**9.** `:.2f` — sonni 2 ta kasr bilan formatlaydi. `f"{3.14159:.2f}"` natijasi `"3.14"`. `f` — float format, `2` — kasrdan keyingi raqamlar soni.

**10.** Qavslar `()` har doim eng birinchi bajariladi va standart ustunlikni o'zgartiradi. `(2 + 3) * 4 = 20`, qavsiz `2 + 3 * 4 = 14`. Murakkab formulalarda aniqlik uchun qavslar ishlatish tavsiya etiladi.

---

# 10. Qisqa xulosa

Bu darsda:

- `input()` funksiyasi va foydalanuvchidan ma'lumot olish;
- 7 ta arifmetik operator: `+`, `-`, `*`, `/`, `//`, `%`, `**`;
- Turlar konvertatsiyasi: `int(input())`, `float(input())`;
- Operatorlar ustuniigi va qavslar;
- Real hisob-kitob dasturlari yozish

o'rganildi.

---

Keyingi **4-dars: Stringlar** da matn (string) ma'lumot turi bilan batafsil ishlash — indekslash, kesish (slicing), string metodlari va formatlash usullari o'rganiladi.

---

# Resurslar va fayllar

- 📄 Python input(): https://docs.python.org/3/library/functions.html#input
- 📄 Arifmetik operatorlar: https://docs.python.org/3/reference/expressions.html#binary-arithmetic-operations
- 💻 Kodlar: `github.com/dars-reja/03-dars`
- 🎬 Video dars: `youtube.com/watch?v=dars03`
"""

# ===== 4-DARS =====
FULL_DOCS[4] = r"""# 🔤 4. Stringlar — Dars dokumentatsiyasi

String (matn) — bu belgilar ketma-ketligi bo'lib, Python'da eng ko'p ishlatiladigan ma'lumot turlaridan biri. `str` turi qo'shtirnoq (`"..."` yoki `'...'`) ichida yoziladi. Stringlar o'zgarmas (immutable) — ya'ni yaratilgandan keyin undagi alohida belgini o'zgartirib bo'lmaydi, lekin yangi string yaratish mumkin.

Stringlar bilan ishlash dasturlashning deyarli har bir sohasida uchraydi: foydalanuvchi kiritgan ma'lumotlarni qayta ishlash, fayllar bilan ishlash, ma'lumotlarni formatlash, web sahifalar yaratish, API javoblarini tahlil qilish — bularning barchasi string operatsiyalari.

Python stringlari uchun juda boy metodlar to'plamiga ega — 40 dan ortiq ichki metod mavjud. Bu darsda eng muhim va ko'p ishlatiladigan metodlarni batafsil o'rganamiz.

---

## Bu mavzu orqali nimalar qilish mumkin

- Matnlarni birlashtirish va takrorlash;
- Indekslash va kesish (slicing) orqali kerakli qismni olish;
- String metodlari (`upper()`, `lower()`, `strip()`, `replace()`, `split()`, `find()`, `count()`) bilan ishlash;
- `f-string`, `.format()` va `%` yordamida formatlash;
- Matnni tekshirish: `startswith()`, `endswith()`, `isdigit()`, `isalpha()`.

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

> **Indeks** — bu stringdagi har bir belgining tartib raqami. Python'da indeks 0 dan boshlanadi: `"Python"[0]` → `"P"`. Manfiy indeks oxiridan sanaydi: `"Python"[-1]` → `"n"`.

## Slicing nima?

> **Slicing (kesish)** — bu stringdan ma'lum qismni ajratib olish: `"Python"[0:3]` → `"Pyt"`. Sintaksis: `string[boshlanish:tugash:qadam]`.

## Immutability nima?

> **Immutability (o'zgarmaslik)** — stringdagi alohida belgini o'zgartirib bo'lmaydi. `s[0] = "X"` xato beradi. Buning o'rniga yangi string yaratish kerak.

---

# 2. Sintaksis

```python
matn = "Salom, Dunyo!"
print(matn[0])       # S (birinchi belgi)
print(matn[-1])      # ! (oxirgi belgi)
print(matn[0:5])     # Salom (0 dan 5 gacha, 5 kirmaydi)
print(len(matn))     # 13 (belgilar soni)
```

---

# 3. String metodlari jadvali

| Metod | Vazifasi | Misol | Natija |
|---|---|---|---|
| `upper()` | Barchasini katta harfga | `"salom".upper()` | `"SALOM"` |
| `lower()` | Barchasini kichik harfga | `"SALOM".lower()` | `"salom"` |
| `capitalize()` | Birinchi harfni katta | `"salom".capitalize()` | `"Salom"` |
| `title()` | Har so'z boshini katta | `"salom dunyo".title()` | `"Salom Dunyo"` |
| `strip()` | Bosh/oxirdagi bo'sh joyni olib tashlaydi | `"  salom  ".strip()` | `"salom"` |
| `lstrip()` | Faqat chapdagi bo'sh joy | `"  salom".lstrip()` | `"salom"` |
| `rstrip()` | Faqat o'ngdagi bo'sh joy | `"salom  ".rstrip()` | `"salom"` |
| `replace(a, b)` | `a` ni `b` ga almashtiradi | `"salom".replace("s","S")` | `"Salom"` |
| `split(sep)` | Matnni bo'laklarga ajratadi | `"a,b,c".split(",")` | `["a","b","c"]` |
| `join(list)` | Listni matnga birlashtiradi | `"-".join(["a","b"])` | `"a-b"` |
| `find(sub)` | Qism matnning indeksini topadi | `"salom".find("lo")` | `2` |
| `count(sub)` | Qism matn necha marta uchrashini sanaydi | `"salom".count("a")` | `1` |
| `startswith(s)` | Boshlanishini tekshiradi | `"salom".startswith("sa")` | `True` |
| `endswith(s)` | Tugashini tekshiradi | `"salom".endswith("om")` | `True` |
| `isdigit()` | Faqat raqamlardan iboratmi | `"123".isdigit()` | `True` |
| `isalpha()` | Faqat harflardan iboratmi | `"abc".isalpha()` | `True` |
| `center(n, ch)` | Matnni markazga joylashtiradi | `"hi".center(10, "-")` | `"----hi----"` |
| `zfill(n)` | Chapga nol qo'shadi | `"42".zfill(5)` | `"00042"` |

---

# 4. Kod misollari

## Misol 1 — String yaratish

```python
s1 = "Salom"
s2 = 'Dunyo'
s3 = """Ko'p qatorli
matn"""

print(s1, s2)
print(s3)
```

Natija:

```
Salom Dunyo
Ko'p qatorli
matn
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
- `til[0]` → `"P"` (birinchi belgi, indeks 0 dan boshlanadi);
- `til[-1]` → `"n"` (oxirgi belgi);
- `til[-2]` → `"o"` (oxiridan ikkinchi).

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
print(f"Asl:    [{matn}]")
print(f"Strip:  [{matn.strip()}]")

yangi = matn.strip().replace("Dunyo", "Python")
print(f"Yangi:  [{yangi}]")
```

Natija:

```
Asl:    [   Salom, Dunyo!   ]
Strip:  [Salom, Dunyo!]
Yangi:  [Salom, Python!]
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
matn = "Python dasturlash tili. Python zo'r!"

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

Qatorma-qator izoh:
- `find()` topilmasa `-1` qaytaradi;
- `count()` necha marta uchrashini sanaydi;
- `in` — mavjudligini tekshiradi (`True`/`False`).

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

# 5. Real loyiha misoli — Email validatori

```python
email = input("Email manzilingizni kiriting: ").strip().lower()

xatolar = []

if "@" not in email:
    xatolar.append("'@' belgisi yo'q")
elif email.count("@") > 1:
    xatolar.append("Bir nechta '@' belgisi bor")

if "." not in email:
    xatolar.append("'.' belgisi yo'q")

if email.startswith("@") or email.endswith("@"):
    xatolar.append("'@' bosh yoki oxirda bo'lmasligi kerak")

if " " in email:
    xatolar.append("Bo'sh joy bo'lmasligi kerak")

if xatolar:
    print("Xatolar topildi:")
    for x in xatolar:
        print(f"  - {x}")
else:
    print(f"'{email}' to'g'ri email manzil!")
```

---

# 6. Ko'p uchraydigan xatolar

## Xato 1: Stringda belgini o'zgartirish

Noto'g'ri:

```python
s = "Salom"
s[0] = "X"  # TypeError!
```

To'g'ri:

```python
s = "Salom"
s = "X" + s[1:]  # "Xalom"
```

## Xato 2: find() o'rniga index() ishlatish

Noto'g'ri:

```python
"salom".index("xyz")  # ValueError!
```

To'g'ri:

```python
if "salom".find("xyz") != -1:
    print("Topildi")
```

## Xato 3: split() ga noto'g'ri ajratuvchi berish

Noto'g'ri:

```python
"a,b,c".split(" ")  # ["a,b,c"] — ajratmadi!
```

To'g'ri:

```python
"a,b,c".split(",")  # ["a", "b", "c"]
```

## Xato 4: Matn va sonni + bilan birlashtirish

Noto'g'ri:

```python
"Yosh: " + 20  # TypeError!
```

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
**Vazifa:** Palindromni tekshiruvchi dastur yozing: foydalanuvchi so'z kiritadi, dastur uning teskari yozilishi bilan bir xil ekanligini aniqlaydi (`"madam"` → `True`).

---

# 8. Uyga vazifa

1. Foydalanuvchidan to'liq ism (ism familiya) oling va bosh harflarini (initials) chiqaring: `"Ali Valiyev"` → `"A.V."`.
2. Berilgan matnda eng ko'p uchraydigan harfni toping.
3. Foydalanuvchidan jumla oling va undagi so'zlarni teskari tartibda chiqaring: `"Salom Dunyo"` → `"Dunyo Salom"`.
4. Telefon raqamini formatlang: `"998901234567"` → `"+998 (90) 123-45-67"`.
5. Foydalanuvchidan matn oling va undagi unli harflar sonini hisoblang.

---

# 9. Tekshirish savollari

1. String nima va Python'da qanday yaratiladi?
2. Indeks nima va nima uchun 0 dan boshlanadi?
3. Manfiy indeks nima va qachon ishlatiladi?
4. Slicing sintaksisi qanday: `[start:stop:step]`?
5. `upper()` va `capitalize()` o'rtasidagi farq nima?
6. `split()` va `join()` o'rtasidagi farq nima?
7. `find()` va `index()` o'rtasidagi farq nima?
8. String immutability nima va nima uchun muhim?
9. `in` operatori stringlarda qanday ishlaydi?
10. `f-string` va `.format()` o'rtasidagi farq nima?

---

## Javoblar

**1.** String — belgilar ketma-ketligi. Qo'shtirnoq ichida yaratiladi: `"Salom"`, `'Salom'` yoki `"""ko'p qatorli"""`. Python'da `str` turi bilan ifodalanadi.

**2.** Indeks — stringdagi belgining tartib raqami. 0 dan boshlanadi chunki kompyuter xotirasida birinchi element ofset 0 da joylashadi. `"ABC"[0]` → `"A"`.

**3.** Manfiy indeks oxiridan sanaydi: `[-1]` — oxirgi belgi, `[-2]` — oxiridan ikkinchi. String uzunligini bilmasdan oxirgi elementga murojaat qilish uchun qulay.

**4.** `string[start:stop:step]` — `start` dan `stop` gacha (stop kirmaydi), `step` qadam bilan. `"Python"[0:4:2]` → `"Pt"`. Har birini tushirish mumkin: `[:3]`, `[2:]`, `[::-1]`.

**5.** `upper()` — barcha harflarni katta qiladi: `"salom"` → `"SALOM"`. `capitalize()` — faqat birinchi harfni katta, qolganini kichik: `"salom DUNYO"` → `"Salom dunyo"`.

**6.** `split(",")` — matnni ajratuvchi bo'yicha listga bo'ladi: `"a,b"` → `["a","b"]`. `join()` — list elementlarini bitta matnga birlashtiradi: `",".join(["a","b"])` → `"a,b"`. Ular bir-birining teskari amali.

**7.** `find()` — topilmasa `-1` qaytaradi. `index()` — topilmasa `ValueError` xatosi beradi. Xavfsiz kod uchun `find()` ishlatish tavsiya etiladi.

**8.** Immutability — stringdagi alohida belgini o'zgartirib bo'lmaydi: `s[0] = "X"` xato beradi. Buning o'rniga yangi string yaratish kerak. Bu Python'ning xotira xavfsizligi va optimizatsiyasi uchun muhim.

**9.** `"Python" in "Men Python o'rganaman"` → `True`. `in` operatori bitta stringning boshqa string ichida mavjudligini tekshiradi va `True`/`False` qaytaradi.

**10.** Ikkalasi ham string formatlash usullari. `f-string` (`f"Ism: {ism}"`) Python 3.6+ da qo'shilgan va eng tez, eng qulay usul. `.format()` (`"Ism: {}".format(ism)`) eski usul, lekin hali ham ishlaydi.

---

# 10. Qisqa xulosa

Bu darsda:

- String yaratish va xususiyatlari;
- Indekslash va slicing;
- 18 ta string metodi;
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
"""

print("1-4 darslar tayyor!")
print(f"1-dars: {len(FULL_DOCS[1])} belgi")
print(f"2-dars: {len(FULL_DOCS[2])} belgi")
print(f"3-dars: {len(FULL_DOCS[3])} belgi")
print(f"4-dars: {len(FULL_DOCS[4])} belgi")
