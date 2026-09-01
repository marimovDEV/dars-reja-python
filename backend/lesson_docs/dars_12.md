# 🎓 12. 1-modul imtihoni — Dars dokumentatsiyasi

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
