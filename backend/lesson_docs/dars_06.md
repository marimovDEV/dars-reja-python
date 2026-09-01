# 🧠 6. Mantiqiy operatorlar — Dars dokumentatsiyasi

Mantiqiy operatorlar (`and`, `or`, `not`) — bu bir nechta shartlarni birlashtirib tekshirish uchun ishlatiladigan operatorlar. Ular `if` shartlari ichida eng ko'p qo'llaniladi va murakkab qarorlar qabul qilish imkonini beradi.

`and` — ikkala shart ham `True` bo'lsagina `True` qaytaradi. `or` — kamida bittasi `True` bo'lsa `True` qaytaradi. `not` — shartni teskarisiga o'zgartiradi. Bu operatorlarni to'g'ri tushunish murakkab dasturlar yozishning kalitidir.

Solishtirish operatorlari (`==`, `!=`, `<`, `>`, `<=`, `>=`) ham shartli mantiqning asosiy qismi bo'lib, ular har doim `True` yoki `False` qaytaradi.

---

## Bu mavzu orqali nimalar qilish mumkin

- Bir nechta shartni birlashtirib tekshirish;
- `and`, `or`, `not` operatorlarini qo'llash;
- Murakkab shartli ifodalar tuzish;
- Bool algebra asoslarini tushunish;
- Amaliy tekshiruvlar yozish (login, yosh, chegirma).

---

## Dars maqsadi

Bu dars oxirida o'quvchi:

- `and`, `or`, `not` operatorlarini bilish;
- Truth table (haqiqat jadvali) ni tushunish;
- Murakkab shartlarni to'g'ri yozish;
- Short-circuit evaluation tushunchasini bilish

ni mustaqil bajara oladi.

---

## Kerakli oldingi bilimlar

- 2-dars: O'zgaruvchilar va turlar (bool);
- 5-dars: If/elif/else.

---

# 1. Asosiy tushunchalar

## and nima?

> **`and`** — ikkala shart ham `True` bo'lsagina `True` qaytaradi. Bittasi `False` bo'lsa, natija `False`.

## or nima?

> **`or`** — kamida bitta shart `True` bo'lsa `True` qaytaradi. Ikkisi ham `False` bo'lsagina `False`.

## not nima?

> **`not`** — shartni teskarisiga o'zgartiradi: `not True` = `False`, `not False` = `True`.

## Short-circuit evaluation nima?

> **Short-circuit** — Python shartni chapdan o'ngga tekshiradi va natija aniq bo'lishi bilanoq to'xtaydi. `and` da birinchi `False` topilsa, ikkinchi shartni tekshirmaydi. `or` da birinchi `True` topilsa, davom etmaydi.

---

# 2. Haqiqat jadvali

| A | B | A and B | A or B | not A |
|---|---|---|---|---|
| True | True | True | True | False |
| True | False | False | True | False |
| False | True | False | True | True |
| False | False | False | False | True |

---

# 3. Kod misollari

## Misol 1 — and operatori

```python
yosh = 25
fuqaro = True

if yosh >= 18 and fuqaro:
    print("Ovoz berish mumkin.")
else:
    print("Ovoz berish mumkin emas.")
```

Natija: `Ovoz berish mumkin.`

---

## Misol 2 — or operatori

```python
kun = "shanba"

if kun == "shanba" or kun == "yakshanba":
    print("Dam olish kuni!")
else:
    print("Ish kuni.")
```

Natija: `Dam olish kuni!`

---

## Misol 3 — not operatori

```python
login_qilingan = False

if not login_qilingan:
    print("Iltimos, tizimga kiring.")
```

Natija: `Iltimos, tizimga kiring.`

---

## Misol 4 — Murakkab shart

```python
yosh = 22
talaba = True
ish_tajribasi = 1

if (yosh >= 18 and yosh <= 30) and (talaba or ish_tajribasi >= 1):
    print("Stajyorlikka ariza topshirishingiz mumkin.")
```

---

## Misol 5 — Chegirma tizimi

```python
summa = float(input("Xarid summasi: "))
karta_bor = input("Chegirma kartangiz bormi? (ha/yo'q): ") == "ha"

if summa >= 500000 and karta_bor:
    chegirma = 0.20
elif summa >= 500000 or karta_bor:
    chegirma = 0.10
else:
    chegirma = 0.0

print(f"Chegirma: {chegirma * 100:.0f}%")
print(f"To'lov: {summa * (1 - chegirma):,.0f} so'm")
```

---

## Misol 6 — Parol tekshirish

```python
parol = input("Parol kiriting: ")

uzun = len(parol) >= 8
raqam_bor = any(c.isdigit() for c in parol)
katta_harf = any(c.isupper() for c in parol)

if uzun and raqam_bor and katta_harf:
    print("Kuchli parol!")
elif uzun and (raqam_bor or katta_harf):
    print("O'rtacha parol.")
else:
    print("Zaif parol! Kamida 8 belgi, 1 raqam va 1 katta harf kerak.")
```

---

## Misol 7 — in va not in

```python
ruxsat_tillar = ["Python", "Java", "C++"]
til = input("Dasturlash tilini kiriting: ")

if til in ruxsat_tillar:
    print(f"{til} qo'llab-quvvatlanadi!")
elif til not in ruxsat_tillar:
    print(f"{til} hozircha qo'llab-quvvatlanmaydi.")
```

---

## Misol 8 — Short-circuit

```python
x = 0

if x != 0 and 10 / x > 2:
    print("Shart bajarildi")
else:
    print("Shart bajarilmadi yoki x = 0")
```

Natija: `Shart bajarilmadi yoki x = 0`

Izoh: `x != 0` `False` bo'lgani uchun `and` ikkinchi qismni tekshirmaydi — `ZeroDivisionError` bo'lmaydi!

---

# 5. Real loyiha misoli — Dasturga kirish tekshiruvi

```python
print("=== TIZIMGA KIRISH ===")
login = input("Login: ")
parol = input("Parol: ")
yosh = int(input("Yosh: "))

admin = login == "admin" and parol == "admin123"
user = login == "user" and parol == "user123"
voyaga_yetgan = yosh >= 18

if admin and voyaga_yetgan:
    print("Admin sifatida kirdingiz!")
elif user and voyaga_yetgan:
    print("Foydalanuvchi sifatida kirdingiz!")
elif not voyaga_yetgan:
    print("18 yoshdan kichiklarga ruxsat berilmaydi!")
else:
    print("Login yoki parol noto'g'ri!")
```

---

# 6. Ko'p uchraydigan xatolar

## Xato 1: `and` o'rniga `or` ishlatish

Noto'g'ri:

```python
if yosh > 18 or yosh < 30:
    print("18-30 orasida")
```

To'g'ri:

```python
if yosh > 18 and yosh < 30:
    print("18-30 orasida")
```

## Xato 2: not ni noto'g'ri joyga qo'yish

Noto'g'ri:

```python
if x == not True:
    pass
```

To'g'ri:

```python
if not x == True:
    pass
if x != True:
    pass
```

## Xato 3: and/or ustunligini bilmaslik

Noto'g'ri:

```python
if a or b and c:
    pass
```

Nima uchun xato: `and` birinchi bajariladi: `a or (b and c)`.

To'g'ri:

```python
if (a or b) and c:
    pass
```

## Xato 4: bool qiymatni == True bilan solishtirish

Noto'g'ri:

```python
if x == True:
    pass
```

To'g'ri:

```python
if x:
    pass
```

---

# 7. Sinfdagi amaliy topshiriqlar

## 1-topshiriq — Oson

**Vazifa:** Foydalanuvchidan son oling, u 10 dan 100 gacha oralig'ida ekanligini tekshiring (`and` bilan).

## 2-topshiriq — O'rta

**Vazifa:** Chegirma tizimi: summa 200000+ va VIP karta = 25%, summa 200000+ yoki VIP karta = 15%, qolgani 0%.

## 3-topshiriq — Murakkab

**Vazifa:** Parol validatori: kamida 8 belgi, 1 katta harf, 1 raqam, 1 maxsus belgi tekshirilsin.

---

# 8. Uyga vazifa

1. `and`, `or`, `not` operatorlarining haqiqat jadvalini Python kodi bilan tasdiqlang.
2. Yil kabisami tekshiruvi: `(yil % 4 == 0 and yil % 100 != 0) or (yil % 400 == 0)`.
3. BMI kalkulyator: og'irlik/bo'y**2, natijaga qarab holat chiqaring.
4. Uchburchak turini aniqlang: teng tomonli, teng yonli, har xil tomonli.
5. Transport tanlash: masofa < 1km piyoda, < 5km velosiped, boshqasi avtobus.

---

# 9. Tekshirish savollari

1. `and` operatori qachon `True` qaytaradi?
2. `or` operatori qachon `False` qaytaradi?
3. `not True` natijasi nima?
4. Short-circuit evaluation nima?
5. `and` va `or` ustunligi qanday?
6. `in` operatori shartlarda qanday ishlaydi?
7. `not in` nima uchun ishlatiladi?
8. `if x:` va `if x == True:` o'rtasidagi farq nima?
9. `bool(0)`, `bool("")`, `bool([])` natijasi nima?
10. Nima uchun `if yosh > 18 or yosh < 30:` har doim `True`?

---

## Javoblar

**1.** `and` faqat ikkala operand ham `True` bo'lgandagina `True` qaytaradi. Bittasi `False` bo'lsa, natija `False`.

**2.** `or` faqat ikkala operand ham `False` bo'lgandagina `False` qaytaradi. Kamida bittasi `True` bo'lsa — `True`.

**3.** `not True` = `False`. `not` operatori qiymatni teskarisiga o'zgartiradi.

**4.** Short-circuit — Python shartni chapdan o'ngga tekshiradi va natija aniq bo'lishi bilanoq to'xtaydi. `False and ...` da ikkinchi qism tekshirilmaydi. `True or ...` da ham.

**5.** `not` birinchi, `and` ikkinchi, `or` uchinchi bajariladi. `a or b and c` = `a or (b and c)`.

**6.** `if x in [1, 2, 3]:` — `x` ro'yxatda bormi tekshiradi. `True` yoki `False` qaytaradi.

**7.** `not in` — elementning ro'yxatda yo'qligini tekshiradi: `if "d" not in ["a", "b", "c"]:`.

**8.** `if x:` — `x` truthy ekanini tekshiradi (qisqa, Pythonic). `if x == True:` — aniq `True` ga teng ekanini tekshiradi. Birinchisi tavsiya etiladi.

**9.** `bool(0)` = `False`, `bool("")` = `False`, `bool([])` = `False`. Bo'sh va nol qiymatlar `False`.

**10.** Chunki har qanday son 18 dan katta yoki 30 dan kichik bo'ladi. To'g'ri: `if yosh > 18 and yosh < 30:`.

---

# 10. Qisqa xulosa

Bu darsda:

- `and`, `or`, `not` mantiqiy operatorlar;
- Haqiqat jadvali (Truth Table);
- Short-circuit evaluation;
- Murakkab shartlar va real misollar

o'rganildi.

---

Keyingi **7-dars: For sikli** da ketma-ketlik elementlarini takrorlash, `range()` funksiyasi va sikllarning amaliy qo'llanilishi o'rganiladi.

---

# Resurslar va fayllar

- 📄 Boolean Operations: https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not
- 💻 Kodlar: `github.com/dars-reja/06-dars`
- 🎬 Video dars: `youtube.com/watch?v=dars06`
