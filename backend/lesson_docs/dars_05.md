# 🔀 5. If/elif/else — Dars dokumentatsiyasi

Shartli operatorlar (`if`, `elif`, `else`) — bu dasturning turli sharoitlarga qarab turli yo'llardan borishi uchun ishlatiladigan boshqaruv strukturalari. Dastur doim yuqoridan pastga ketma-ket bajariladi, lekin shartli operatorlar yordamida muayyan shartlar bajarilganda faqat kerakli kod bloki ishlaydi.

Real hayotda ham shartlar har qadamda: agar yosh 18 dan katta bo'lsa — ovoz berish mumkin, aks holda — mumkin emas. Python'da bu mantiq `if/elif/else` bilan ifodalanadi.

Shartli operatorlar solishtirish (`==`, `!=`, `<`, `>`, `<=`, `>=`) va mantiqiy (`and`, `or`, `not`) operatorlar bilan birgalikda ishlaydi.

---

## Bu mavzu orqali nimalar qilish mumkin

- Shartga qarab turli kodlarni bajarish;
- Bir nechta shartni `elif` bilan tekshirish;
- Ichma-ich (nested) shartlar yozish;
- Solishtirish operatorlarini qo'llash;
- Ternary operator (qisqa if-else) ishlatish.

---

## Dars maqsadi

Bu dars oxirida o'quvchi:

- `if`, `elif`, `else` strukturasini to'g'ri yozish;
- Solishtirish operatorlarini (`==`, `!=`, `<`, `>`, `<=`, `>=`) qo'llash;
- Bir nechta shartni ketma-ket tekshirish;
- Ichma-ich shartlar yozish;
- Ternary operatorni bilish

ni mustaqil bajara oladi.

---

## Kerakli oldingi bilimlar

- 2-dars: O'zgaruvchilar va turlar;
- 3-dars: input() va arifmetika.

---

# 1. Asosiy tushunchalar

## if nima?

> **`if`** — bu shartni tekshiradi. Shart `True` bo'lsa, ichidagi kod bajariladi, `False` bo'lsa o'tkazib yuboriladi.

## elif nima?

> **`elif`** (else if) — oldingi `if` yoki `elif` `False` bo'lganda qo'shimcha shartni tekshiradi.

## else nima?

> **`else`** — barcha oldingi shartlar `False` bo'lganda bajariladigan "qoldiq" blok. Hech qanday shart yozilmaydi.

## Solishtirish operatorlari nima?

> **Solishtirish operatorlari** — ikki qiymatni solishtirib `True` yoki `False` qaytaradi: `==` (teng), `!=` (teng emas), `<` (kichik), `>` (katta), `<=` (kichik yoki teng), `>=` (katta yoki teng).

---

# 2. Sintaksis

```python
if shart:
    # shart True bo'lsa bajariladi
elif boshqa_shart:
    # birinchi shart False, bu shart True bo'lsa
else:
    # hech bir shart True bo'lmasa
```

---

# 3. Solishtirish operatorlari jadvali

| Operator | Nomi | Misol | Natija |
|---|---|---|---|
| `==` | Teng | `5 == 5` | `True` |
| `!=` | Teng emas | `5 != 3` | `True` |
| `<` | Kichik | `3 < 5` | `True` |
| `>` | Katta | `5 > 3` | `True` |
| `<=` | Kichik yoki teng | `5 <= 5` | `True` |
| `>=` | Katta yoki teng | `5 >= 3` | `True` |

---

# 4. Kod misollari

## Misol 1 — Sodda if

```python
yosh = 20

if yosh >= 18:
    print("Siz voyaga yetgansiz.")
```

Natija:

```
Siz voyaga yetgansiz.
```

Qatorma-qator izoh:
- `yosh >= 18` sharti `True` (20 >= 18), shuning uchun `print()` bajariladi.

---

## Misol 2 — if/else

```python
yosh = 15

if yosh >= 18:
    print("Ovoz berish mumkin.")
else:
    print("Ovoz berish mumkin emas.")
```

Natija:

```
Ovoz berish mumkin emas.
```

---

## Misol 3 — if/elif/else

```python
baho = int(input("Bahoni kiriting: "))

if baho >= 90:
    print("A'lo")
elif baho >= 70:
    print("Yaxshi")
elif baho >= 50:
    print("Qoniqarli")
else:
    print("Qoniqarsiz")
```

Natija:

```
Bahoni kiriting: 85
Yaxshi
```

---

## Misol 4 — Ichma-ich if

```python
yosh = int(input("Yoshingiz: "))
haydovchilik = input("Haydovchilik guvohnomasi bormi? (ha/yo'q): ")

if yosh >= 18:
    if haydovchilik == "ha":
        print("Mashina haydashingiz mumkin.")
    else:
        print("Avval guvohnoma oling.")
else:
    print("Siz hali voyaga yetmagansiz.")
```

---

## Misol 5 — Ternary operator

```python
yosh = 20
holat = "voyaga yetgan" if yosh >= 18 else "voyaga yetmagan"
print(f"Siz {holat}siz.")
```

Natija:

```
Siz voyaga yetgansiz.
```

---

## Misol 6 — Bir nechta shart

```python
harorat = float(input("Harorat: "))

if harorat > 40:
    print("Juda issiq! Ehtiyot bo'ling.")
elif harorat > 25:
    print("Iliq ob-havo.")
elif harorat > 10:
    print("Salqin ob-havo.")
elif harorat > 0:
    print("Sovuq.")
else:
    print("Muzlash xavfi bor!")
```

---

## Misol 7 — Kalkulyator

```python
son1 = float(input("1-son: "))
operator = input("Operator (+, -, *, /): ")
son2 = float(input("2-son: "))

if operator == "+":
    print(f"Natija: {son1 + son2}")
elif operator == "-":
    print(f"Natija: {son1 - son2}")
elif operator == "*":
    print(f"Natija: {son1 * son2}")
elif operator == "/":
    if son2 != 0:
        print(f"Natija: {son1 / son2}")
    else:
        print("Nolga bo'lish mumkin emas!")
else:
    print("Noto'g'ri operator!")
```

---

## Misol 8 — Yil fasli aniqlash

```python
oy = int(input("Oy raqamini kiriting (1-12): "))

if oy in [3, 4, 5]:
    print("Bahor")
elif oy in [6, 7, 8]:
    print("Yoz")
elif oy in [9, 10, 11]:
    print("Kuz")
elif oy in [12, 1, 2]:
    print("Qish")
else:
    print("Noto'g'ri oy raqami!")
```

---

# 5. Real loyiha misoli — Kirish tizimi

```python
print("=== KIRISH TIZIMI ===")
foydalanuvchi = input("Login: ")
parol = input("Parol: ")

if foydalanuvchi == "admin" and parol == "12345":
    print("Xush kelibsiz, Admin!")
elif foydalanuvchi == "user" and parol == "password":
    print("Xush kelibsiz, Foydalanuvchi!")
elif foydalanuvchi == "admin" or foydalanuvchi == "user":
    print("Parol noto'g'ri!")
else:
    print("Bunday foydalanuvchi topilmadi!")
```

---

# 6. Ko'p uchraydigan xatolar

## Xato 1: = va == ni aralashtirish

Noto'g'ri:

```python
if x = 5:
    print("Besh")
```

To'g'ri:

```python
if x == 5:
    print("Besh")
```

## Xato 2: Ikki nuqtani (:) unutish

Noto'g'ri:

```python
if x > 5
    print("Katta")
```

To'g'ri:

```python
if x > 5:
    print("Katta")
```

## Xato 3: Indentatsiya xatosi

Noto'g'ri:

```python
if x > 5:
print("Katta")
```

To'g'ri:

```python
if x > 5:
    print("Katta")
```

## Xato 4: elif o'rniga alohida if ishlatish

Noto'g'ri:

```python
if baho >= 90:
    print("A'lo")
if baho >= 70:
    print("Yaxshi")
```

Nima uchun xato: 95 baho uchun ikkala shart ham bajariladi.

To'g'ri:

```python
if baho >= 90:
    print("A'lo")
elif baho >= 70:
    print("Yaxshi")
```

---

# 7. Sinfdagi amaliy topshiriqlar

## 1-topshiriq — Oson

**Vazifa:** Foydalanuvchidan son oling va juft yoki toq ekanligini aniqlang.

## 2-topshiriq — O'rta

**Vazifa:** Foydalanuvchidan 3 ta son oling va eng kattasini toping (faqat if/elif/else bilan, max() ishlatmang).

## 3-topshiriq — Murakkab

**Vazifa:** Sodda kalkulyator: 2 ta son va operator olib natijani chiqaring. Nolga bo'lish va noto'g'ri operatorni tekshiring.

---

# 8. Uyga vazifa

1. Foydalanuvchidan yosh oling va yoshga qarab bola/o'smir/katta/keksa deb ajrating.
2. Sonning musbat, manfiy yoki nol ekanligini aniqlang.
3. Foydalanuvchidan 5 ballik baho oling va harfiy bahoga aylantiring (5=A, 4=B, ...).
4. Uchburchakning 3 tomonini oling va uchburchak tuzish mumkinligini tekshiring.
5. Login/parol tizimi yozing: 3 ta urinish, har safar xato bo'lsa qoldiq urinishlarni ko'rsating.

---

# 9. Tekshirish savollari

1. `if` operatorining vazifasi nima?
2. `elif` va `else` o'rtasidagi farq nima?
3. `==` va `=` o'rtasidagi farq nima?
4. Ternary operator qanday yoziladi?
5. `if x > 5:` dan keyin nima uchun indentatsiya (4 bo'sh joy) kerak?
6. Ichma-ich if qachon ishlatiladi?
7. `in` operatori shartlarda qanday ishlaydi?
8. elif ni if bilan almashtirsangiz nima bo'ladi?
9. `if True:` va `if False:` natijasi nima?
10. Bir nechta shartni bitta if ichida qanday tekshirish mumkin?

---

## Javoblar

**1.** `if` — shartni tekshiradi. Shart `True` bo'lsa, ichidagi kod bajariladi, `False` bo'lsa o'tkazib yuboriladi.

**2.** `elif` — oldingi shartlar `False` bo'lganda qo'shimcha shartni tekshiradi. `else` — hech bir shart `True` bo'lmaganda bajariladi, shart yozilmaydi.

**3.** `=` — tayinlash (qiymat berish): `x = 5`. `==` — solishtirish (tengmi?): `x == 5`. `if` ichida doim `==` ishlatiladi.

**4.** `natija = "ha" if shart else "yo'q"`. Bitta qatorda if/else yozish usuli.

**5.** Python blok strukturasini indentatsiya (bo'sh joy) bilan aniqlaydi. 4 bo'sh joy — bu if blokiga tegishli kod ekanini bildiradi. Indentatsiyasiz `IndentationError` xatosi chiqadi.

**6.** Ichma-ich if bitta shart ichida yana shart tekshirish kerak bo'lganda ishlatiladi. Masalan: yosh tekshirilgandan keyin guvohnoma borligini tekshirish.

**7.** `if x in [1, 2, 3]:` — `x` qiymati ro'yxatda bormi tekshiradi. `True` yoki `False` qaytaradi.

**8.** `elif` o'rniga alohida `if` qo'yilsa, barcha shartlar mustaqil tekshiriladi. Masalan, 95 baho uchun "A'lo" ham "Yaxshi" ham chiqishi mumkin.

**9.** `if True:` — ichidagi kod doim bajariladi. `if False:` — ichidagi kod hech qachon bajarilmaydi.

**10.** `and`, `or` mantiqiy operatorlari bilan: `if yosh >= 18 and fuqaro == True:`.

---

# 10. Qisqa xulosa

Bu darsda:

- `if`, `elif`, `else` shartli operatorlar;
- Solishtirish operatorlari: `==`, `!=`, `<`, `>`, `<=`, `>=`;
- Ichma-ich shartlar;
- Ternary operator;
- Real kalkulyator va kirish tizimi

o'rganildi.

---

Keyingi **6-dars: Mantiqiy operatorlar** da `and`, `or`, `not` operatorlari va murakkab shartlarni tuzish o'rganiladi.

---

# Resurslar va fayllar

- 📄 Python if: https://docs.python.org/3/tutorial/controlflow.html
- 💻 Kodlar: `github.com/dars-reja/05-dars`
- 🎬 Video dars: `youtube.com/watch?v=dars05`
