# 💻 1. Dasturlash muhiti va Python — Dars dokumentatsiyasi

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
matn = """Bu birinchi qator.
Bu ikkinchi qator.
Bu uchinchi qator."""
print(matn)
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

Izoh: `"=" * 40` — `=` belgisini 40 marta takrorlaydi (string ko'paytirish). `print()` — bo'sh qator chiqaradi. Bu dastur faqat `print()` dan foydalanadi, lekin chiroyli natija beradi.

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
```

Qanday oldini olish: Har doim bir xil turdagi qo'shtirnoq ishlating.

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
5. Ko'p qatorli matn yordamida 5 qatorlik she'r chiqaring.

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
