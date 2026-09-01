# 🏗️ 15. Murakkab ma'lumotlar — Dars dokumentatsiyasi

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
