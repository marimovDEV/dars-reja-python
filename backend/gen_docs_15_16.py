#!/usr/bin/env python3
"""Generate lesson docs 15-24 with full 19-section documentation template."""
import os

DOCS_DIR = os.path.join(os.path.dirname(__file__), "lesson_docs")

lessons = {}

# 15-DARS
lessons[15] = """# 🏗️ 15. Murakkab ma'lumotlar — Dars dokumentatsiyasi

Dasturlashda real dunyo obyektlari va murakkab tizim ma'lumotlari kamdan-kam hollarda bir dona oddiy o'zgaruvchida saqlanadi. Masalan, internet magazin loyihasida foydalanuvchilar, ularning savatlari, buyurtmalar tarixi va har bir mahsulotning xususiyatlari murakkab tarzda bir-biriga bog'langan bo'ladi.

**Murakkab ma'lumotlar strukturalari** — bu ma'lumot turlarini (List, Dictionary, Set, Tuple) bir-birining ichiga joylashtirish (nesting) orqali hosil qilinadigan ko'p bosqichli tuzilmalardir. Masalan: Lug'atlar ro'yxati (`List of Dicts`), Ro'yxatlar lug'ati (`Dict of Lists`) yoki Lug'at ichida lug'atlar ro'yxati.

Ushbu darsda siz JSON formatiga juda o'xshash bo'lgan va professional backend dasturchilar har kuni ishlatadigan murakkab strukturalarni yaratish, ulardan ma'lumotlarni to'g'ri o'qib olish va o'zgartirishni mayda detallarigacha o'rganasiz.

---

## Bu mavzu orqali nimalar qilish mumkin

- Real loyihalardagi (masalan, REST API dan keladigan) murakkab ma'lumotlar tuzilmasi bilan ishlash;
- Lug'atlar ro'yxatini (`List of Dicts`) filtrlash va tartiblash;
- Ko'p bosqichli ichma-ich tuzilmalardan ma'lumotni kalit va indeks bo mezonlari bo'yicha olish;
- Murakkab ma'lumotlarni sikllar yordamida qayta ishlash;
- Ma'lumotlar yaxlitligini buzmasdan ularga o'zgartirish kiritish.

---

## Dars maqsadi

Bu dars oxirida o'quvchi:

- Ko'p bosqichli murakkab ma'lumot tuzilmalarini loyihalashtirish;
- `List[Dict]` va `Dict[List]` ko'rinishidagi ma'lumotlar bilan muammosiz ishlash;
- Murakkab strukturani filtrlash, qidirish va statistik ma'lumotlar chiqarish;
- REST API va JSON ma'lumot tuzilishiga tayyor bo'lish

ni mustaqil bajara oladi.

---

## Kerakli oldingi bilimlar

- 11-dars: List asoslari;
- 13-dars: Tuple va Set;
- 14-dars: Dictionary.

---

# 1. Asosiy tushunchalar va atamalar

## Nesting (Ichma-ichlik) nima?

> **Nesting** — bir ma'lumot strukturasi ichida boshqa ma'lumot strukturasini saqlash usuli. Masalan, List ichida Dictionary, yoki Dict ichida List.

## List of Dictionaries (Lug'atlar ro'yxati) nima?

> Bir xil turdagi ko'plab obyektlarni (masalan, foydalanuvchilar ro'yxati, mahsulotlar ro'yxati) saqlash uchun eng keng tarqalgan tuzilma: `[{'id': 1, 'name': 'Ali'}, {'id': 2, 'name': 'Vali'}]`.

## Dict of Lists (Ro'yxatlar lug'ati) nima?

> Biror kalitga tegishli ko'plab qiymatlarni guruhlash uchun ishlatiladigan tuzilma: `{'fruits': ['olma', 'banan'], 'veggies': ['sabzi']}`.

---

# 2. Sintaksis va uning izohi

```python
# Murakkab tuzilma misoli
kompaniya = {
    "nomi": "TechCorp",
    "xodimlar": [
        {"ism": "Ali", "ko_nikmalar": ["Python", "Django"]},
        {"ism": "Vali", "ko_nikmalar": ["React", "CSS"]}
    ]
}

# Murojaat qilish (Zanjirsimon indeksatsiyalash)
print(kompaniya["xodimlar"][0]["ko_nikmalar"][0]) # Python
```

---

# 3. Murakkab Ma'lumot Turlari Solishtirma Jadvali

| Tuzilma Turi | Sintaksis Misoli | Ishlatilish Holati | Murojaat Usuli |
|---|---|---|---|
| **List of Dicts** | `[{"id": 1}, {"id": 2}]` | Obyektlar ro'yxati (Baza jadvallari kabi) | `list[0]["id"]` |
| **Dict of Lists** | `{"juft": [2,4], "toq": [1,3]}` | GURUH-LASH va KATEGORIYALAR | `dict["juft"][0]` |
| **Dict of Dicts** | `{"user1": {"age": 20}}` | Kalitli Unikal Obyektlar | `dict["user1"]["age"]` |

---

# 4. Kod misollari

## Misol 1 — List of Dicts bilan ishlash

```python
talabalar = [
    {"ism": "Ali", "baho": 85},
    {"ism": "Vali", "baho": 92},
    {"ism": "Sardor", "baho": 78}
]

for t in talabalar:
    print(f"Talaba: {t['ism']}, Baho: {t['baho']}")
```

---

## Misol 2 — Murakkab strukturadan ma'lumot filtrlash

```python
xodimlar = [
    {"ism": "Anvar", "maosh": 5000, "bo_lim": "IT"},
    {"ism": "Dilnoza", "maosh": 3000, "bo_lim": "HR"},
    {"ism": "Jasur", "maosh": 6000, "bo_lim": "IT"}
]

it_xodimlari = [x for x in xodimlar if x["bo_lim"] == "IT"]

print("IT bo'limi xodimlari:")
for x in it_xodimlari:
    print(f"- {x['ism']}: ${x['maosh']}")
```

---

## Misol 3 — Dict of Lists (Guruhlash)

```python
shaharlar = {
    "Uzbekistan": ["Toshkent", "Samarqand", "Buxoro"],
    "USA": ["New York", "Chicago", "Los Angeles"]
}

for davlat, shahar_list in shaharlar.items():
    print(f"{davlat} shaharlari: {', '.join(shahar_list)}")
```

---

## Misol 4 — Chuqur (Deep) o'zgaruvchi o'zgartirish

```python
loyihalar = {
    "p1": {"nom": "E-Commerce", "jamoa": ["Ali", "Vali"]},
    "p2": {"nom": "CRM", "jamoa": ["Sardor"]}
}

# CRM loyihasiga yangi a'zo qo'shamiz
loyihalar["p2"]["jamoa"].append("Malika")

print(loyihalar["p2"]["jamoa"])
```

---

## Misol 5 — Maxsus agregatsiya (Yig'indi hisoblash)

```python
do_kon = [
    {"nom": "Olma", "narx": 10000, "soni": 50},
    {"nom": "Banan", "narx": 20000, "soni": 30},
    {"nom": "Uzum", "narx": 15000, "soni": 20}
]

jami_qiymat = sum(item["narx"] * item["soni"] for item in do_kon)
print(f"Ombordagi barcha mahsulotlar umumi qiymati: {jami_qiymat:,} so'm")
```

---

# 5. Real loyiha misoli — E-Commerce Savat Boshqaruvi

```python
foydalanuvchi_profil = {
    "id": 101,
    "ism": "Bobur",
    "savat": [
        {"p_id": 1, "nomi": "Noutbuk", "narx": 9000000, "dona": 1},
        {"p_id": 2, "nomi": "Sichqoncha", "narx": 120000, "dona": 2}
    ]
}

print(f"Foydalanuvchi: {foydalanuvchi_profil['ism']}")
print("--- SAVAT MA'LUMOTLARI ---")

jami_to_lov = 0
for item in foydalanuvchi_profil["savat"]:
    summa = item["narx"] * item["dona"]
    jami_to_lov += summa
    print(f"- {item['nomi']} ({item['dona']} dona): {summa:,} so'm")

print(f"JAMI CHECK: {jami_to_lov:,} so'm")
```

---

# 6. Ko'p uchraydigan xatolar

## Xato 1: Noto'g'ri turdagi indeksatsiyani ishlatish

Noto'g'ri:
```python
data = [{"ism": "Ali"}]
print(data["ism"]) # TypeError: list indices must be integers, not str
```

To'g'ri:
```python
print(data[0]["ism"]) # Birinchi ro'yxat indekslanadi, so'ngra lug'at kaliti!
```

---

# 7. Sinfdagi amaliy topshiriqlar

1. **Oson**: 3 ta avtomobil (nomi, narxi, rangi) berilgan lug'atlar ro'yxatini yarating va har birining nomini ekranga chiqaring.
2. **O'rta**: Yuqoridagi avtomobillar ro'yxatidan narxi 15,000$ dan yuqori bo'lganlarini filtrlb oling.

---

# 8. Uyga vazifa

1. Kutubxona tizimi uchun ma'lumot tuzilmasini yarating (Kitoblar ro'yxati, har bir kitobda muallif, janr, chop etilgan yili va olinganligi haqida bool qiymat bo'lsin). Ulardan faqat olinmagan (bo'sh) kitoblarni ko'rsating.

---

# 9. Tekshirish savollari

1. `List of Dicts` va `Dict of Lists` o'rtasidagi asosiy farq nimada?
2. Chuqur joylashgan elementga murojaat qilishda qanday tartibda harakat qilinadi?

---

## Javoblar

1. `List of Dicts` ro'yxat elementlari lug'atlardan iborat tuzilma, `Dict of Lists` esa lug'at qiymatlari ro'yxatdan iborat tuzilma.
2. Tashqi strukturadan ichki strukturaga qarab ketma-ket har bir daraja turi (List bo'lsa indeks `[0]`, Dict bo'lsa kalit `["key"]`) bo'yicha zanjirsimon bog'lanadi.

---

# 10. Qisqa xulosa

Bu darsda murakkab va ko'p bosqichli ma'lumotlar tuzilmasi, real backend tizimlardagi ma'lumotlar arxitekturasi va u bilan ishlash ko'nikmalari o'rganildi.
"""

# 16-DARS
lessons[16] = """# ⚡ 16. Comprehension — Dars dokumentatsiyasi

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
"""

for num, content in lessons.items():
    filepath = os.path.join(DOCS_DIR, f"dars_{num:02d}.md")
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"dars_{num:02d}.md yaratildi: {len(content)} belgi")
