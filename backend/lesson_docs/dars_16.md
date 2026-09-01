# ⚡ 16. Comprehension — Dars dokumentatsiyasi

Comprehension (Ro'yxat va Lug'at tuzgichlari) — Python tilining eng mashhur, go'zal va o'ziga xos ("Pythonic") xususiyatlaridan biridir. U ketma-ketliklarni (List, Dict, Set) yaratish va ularni bir vaqtning o'zida filtrlash jarayonini 4-5 qatorli oddiy `for` sikli o'rniga **bitta qisqa va tushunarli qatorda** yozish imkonini beradi.

Comprehension nafaqat kod hajmini qisqartiradi va uni o'qilishini yaxshilaydi, balki ko'p hollarda an'anaviy sikllarga qaraganda tezroq ishlaydi (chunki u C darajasida optimallashtirilgan).

Bu darsda siz `List Comprehension`, `Dictionary Comprehension` va `Set Comprehension` sintaksisini professional darajada qo'llashni o'rganasiz.

---

## Bu mavzu orqali nimalar qilish mumkin

- Sikl yozmasdan 1 qatorda yangi ro'yxat, lug'at yoki to'plam yaratish;
- Ma'lumotlarni yaratish vaqtidayoq `if` shartlari bilan filtrlash;
- String va sonlar ro'yxatini tezkor o'zgartirish (transformatsiya);
- Murakkab `for` sikllarini ixchamlashtirish.

---

## Dars maqsadi

Bu dars oxirida o'quvchi:

- List, Dict va Set Comprehension sintaksisini tushunish;
- Filter (shart) va Ternary Operator (if-else) bilan comprehension yozish;
- Kod o'qilishini yaxshilash va optimal Pythonic kod yozish

ni mustaqil bajara oladi.

---

## Kerakli oldingi bilimlar

- 7-dars: For sikli;
- 11-dars: List asoslari;
- 14-dars: Dictionary.

---

# 1. Asosiy tushunchalar va atamalar

## Comprehension nima?

> **Comprehension** — iterator (sikl) asosida yangi ketma-ketlik yaratishning ixcham va sintaktik qulay shaklidir.

## Pythonic Code nima?

> **Pythonic Code** — Python tilining imkoniyatlaridan unumli foydalangan holda yozilgan, qisqa, tushunarli va toza kod.

---

# 2. Sintaksis va uning izohi

```python
# List Comprehension Standart Shakli
# [IFODA for ELEMENT in KETMA_KETLIK if SHART]

juft_kvadratlar = [x**2 for x in range(10) if x % 2 == 0]
# Natija: [0, 4, 16, 36, 64]
```

---

# 3. Comprehension Turlari Jadvali

| Tur | Sintaksis Formulasi | Misol | Natija Turi |
|---|---|---|---|
| **List Comprehension** | `[x for x in data]` | `[i*2 for i in range(3)]` | List `[0, 2, 4]` |
| **Set Comprehension** | `{x for x in data}` | `{i%2 for i in range(5)}` | Set `{0, 1}` |
| **Dict Comprehension**| `{k: v for k, v in data}` | `{x: x**2 for x in range(3)}` | Dict `{0:0, 1:1, 2:4}` |

---

# 4. Kod misollari

## Misol 1 — Oddiy va Comprehension taqqoslashi

```python
# An'anaviy Usul
sonlar = [1, 2, 3, 4, 5]
kvadratlar = []
for s in sonlar:
    kvadratlar.append(s ** 2)

# Comprehension Usuli
kvadratlar_py = [s ** 2 for s in sonlar]

print(kvadratlar_py)
```

---

## Misol 2 — Shartli filtrlash (if bilan)

```python
ismlar = ["Ali", "Vali", "Anvar", "Sardor", "Aziz"]
a_bilan = [ism for ism in ismlar if ism.startswith("A")]

print(a_bilan) # ['Ali', 'Anvar', 'Aziz']
```

---

## Misol 3 — If-Else (Ternary) bilan ishlash

```python
ballar = [60, 85, 45, 90, 70]
natijalar = ["O'tdi" if b >= 60 else "Yiqildi" for b in ballar]

print(natijalar)
```

---

## Misol 4 — Dict Comprehension

```python
tovarlar = ["olma", "banan", "uzum"]
narxlar = [10000, 20000, 15000]

do_kon = {tovarlar[i]: narxlar[i] for i in range(len(tovarlar))}
print(do_kon)
```

Natija: `{'olma': 10000, 'banan': 20000, 'uzum': 15000}`

---

## Misol 5 — Set Comprehension (Noyob qiymatlar)

```python
matn = "abracadabra"
unikal_harflar = {h.upper() for h in matn if h not in "aeiou"}

print(unikal_harflar)
```

---

# 5. Real loyiha misoli — Foydalanuvchi ma'lumotlarini tozalash va tayyorlash

```python
raw_users = [
    {"name": "  ali ", "email": "ALI@MAIL.COM", "active": True},
    {"name": "VALI", "email": "vali@mail.com", "active": False},
    {"name": "sardor", "email": "Sardor@Mail.Com ", "active": True}
]

# Faqat aktiv foydalanuvchilarning email va ismini standartlashtiramiz
clean_users = [
    {
        "name": u["name"].strip().capitalize(),
        "email": u["email"].strip().lower()
    }
    for u in raw_users if u["active"]
]

print(clean_users)
```

---

# 6. Ko'p uchraydigan xatolar

## Xato 1: Juda murakkab va o'qish qiyin bo'lgan Comprehension yozish

Noto'g'ri (Kodni tushunib bo'lmaydi):
```python
res = [x**2 for x in range(10) if x % 2 == 0 for y in range(5) if x + y > 3]
```

To'g'ri: Juda murakkab mantiq bo'lsa, oddiy `for` sikli va funksiyalardan foydalangan ma'qul!

---

# 7. Sinfdagi amaliy topshiriqlar

1. **Oson**: 1 dan 20 gacha bo'lgan sonlar ichidan faqat 3 ga bo'linadiganlarining kubini List Comprehension orqali yarating.
2. **O mezon**: Berilgan matndagi so'zlarning uzunligini kalit, so'zning o'zini qiymat qilib lug'at yarating.

---

# 8. Uyga vazifa

1. Narxlari so'mda berilgan ro'yxatni dollar kursiga bo'lib, yangi `USD` narxlar ro'yxatini comprehension orqali shakllantiring.

---

# 9. Tekshirish savollari

1. Comprehension qachon ishlatilmasligi kerak?
2. `if` va `if-else` comprehension yozilishida o'rni qanday farqlanadi?

---

## Javoblar

1. Kod juda uzun, ichma-ich va o'qilishi qiyin holatga kelib qolganda.
2. Faqat filtrlash `if` sikldan keyin keladi (`[x for x in data if shart]`), lekin `if-else` bo'lsa `for` dan oldin yoziladi (`[x if shart else y for x in data]`).

---

# 10. Qisqa xulosa

Bu darsda Pythonic va toza kod yozishning muhim usuli bo'lgan List, Dict va Set Comprehension imkoniyatlari o'rganildi.
