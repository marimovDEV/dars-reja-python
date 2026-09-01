#!/usr/bin/env python3
"""Generate lesson docs 13-18 with full 19-section documentation template."""
import os

DOCS_DIR = os.path.join(os.path.dirname(__file__), "lesson_docs")

lessons = {}

# 13-DARS
lessons[13] = """# 📦 13. Tuple va Set — Dars dokumentatsiyasi

Tuple (kortej) va Set (to'plam) — Python'dagi ikkita muhim va ko'p ishlatiladigan ma'lumot strukturasidir. Ular list (ro'yxat) ga o'xshash ko'rinsada, xotirada saqlanishi, o'zgartirilishi va bajaradigan vazifalari bo'yicha tubdan farq qiladi.

Tuple — tartiblangan va **o'zgarmas (immutable)** ketma-ketlikdir. Yaratilgandan so'ng unga element qo'shib, o'chirib yoki o'zgartirib bo'lmaydi. Bu xususiyat ma'lumotlar yaxlitligini va xavfsizligini ta'minlash hamda xotiradan samarali foydalanish uchun xizmat qiladi.

Set — tartiblanmagan va **noyob (unique)** elementlar to mezonidir. Set ichida bir xil qiymat takrorlanmaydi. Matematikadagi to'plamlar nazariyasi kabi, Set yordamida kesishma (`intersection`), birlashma (`union`), farq (`difference`) kabi amallarni juda tez bajarish mumkin.

---

## Bu mavzu orqali nimalar qilish mumkin

- Tuple yaratish va undan ma'lumotlarni xavfsiz o'qish;
- Unpacking (qiymatlarni ajratib olish) mexanizmini qo'llash;
- Set yaratish va takroriy elementlarni bir zumda tozalash;
- To'plamlar ustida matematik amallar (`union`, `intersection`, `difference`) bajarish;
- List, Tuple va Set o'rtasidagi farqlardan to'g'ri foydalanish.

---

## Dars maqsadi

Bu dars oxirida o'quvchi:

- Tuple va Set strukturalarini to'g'ri e'lon qilish;
- Tuple immutability tamoyilini tushunish va qo'llash;
- Set yordamida duplikatsiyalarni olib tashlash;
- Matematik to'plam operatsiyalarini kodda yozish;
- Har bir holat uchun mos ma'lumot strukturasini tanlay olish

ni mustaqil bajara oladi.

---

## Kerakli oldingi bilimlar

- 11-dars: List asoslari;
- 4-dars: Stringlar va immutability;
- 2-dars: O'zgaruvchilar va turlar.

---

# 1. Asosiy tushunchalar va atamalar

## Tuple nima?

> **Tuple** — o'zgarmas (immutable), tartiblangan elementlar to'plami. Oddiy qavslar `()` ichida yoziladi: `koordinata = (41.2995, 69.2401)`.

## Set nima?

> **Set** — tartibsiz (unordered), takrorlanmas (unique) va o'zgaruvchan elementlar to mezonidir. Jingalak qavslar `{}` ichida yoziladi: `to'plam = {1, 2, 3}`.

## Unpacking nima?

> **Unpacking** — Tuple yoki List ichidagi qiymatlarni alohida o'zgaruvchilarga bir vaqtning o'zida biriktirish jarayoni: `x, y = (10, 20)`.

## Immutability nima?

> **Immutability** — obyekt yaratilgandan so'ng uning ichki holati va qiymatlarini o'zgartirib bo'lmasligi.

---

# 2. Sintaksis va uning izohi

```python
# Tuple e'lon qilish
nuqta = (10, 20)
bitta_element = (5,)  # Vergul shart!

# Set e'lon qilish
mevalar = {"olma", "banan", "uzum"}
bo_sh_set = set()  # {} yozilsa dict bo'lib qoladi!
```

---

# 3. Tuple va Set taqqoslash jadvali

| Xususiyat | List `[]` | Tuple `()` | Set `{}` |
|---|---|---|---|
| Tartiblangan (Ordered) | Ha | Ha | Yo'q |
| O'zgaruvchan (Mutable) | Ha | Yo'q | Ha |
| Takrorlanish (Duplicates) | Ruxsat berilgan | Ruxsat berilgan | **Ruxsat berilmagan** |
| Indekslash (Indexing) | `list[0]` | `tuple[0]` | Qo'llab-quvvatlanmaydi |
| Tezlik & Xotira | O'rtacha | **Juda tez & Kam xotira** | **Qidiruv juda tez O(1)** |

---

# 4. Kod misollari

## Misol 1 — Tuple yaratish va indekslash

```python
ranglar = ("qizil", "yashil", "ko'k")
print(ranglar[0])
print(ranglar[-1])
print(len(ranglar))
```

Natija:
```
qizil
ko'k
3
```

Qatorma-qator izoh:
- `ranglar[0]` — Tuple'ning birinchi elementini oladi;
- Tuple indeksatsiyasi List bilan bir xil ishlaydi.

---

## Misol 2 — Tuple Unpacking (Qiymatlarni ajratish)

```python
talaba = ("Ali", 21, "Dasturlash")
ism, yosh, yo_nalish = talaba

print(f"Ism: {ism}, Yosh: {yosh}, Yo'nalish: {yo_nalish}")
```

Natija:
```
Ism: Ali, Yosh: 21, Yo'nalish: Dasturlash
```

---

## Misol 3 — Set va takrorlanmaslik xususiyati

```python
sonlar = [1, 2, 2, 3, 4, 4, 4, 5]
noyob_sonlar = set(sonlar)

print("Asl list:", sonlar)
print("Noyob set:", noyob_sonlar)
```

Natija:
```
Asl list: [1, 2, 2, 3, 4, 4, 4, 5]
Noyob set: {1, 2, 3, 4, 5}
```

---

## Misol 4 — Set metodlari (add, remove, discard)

```python
tillar = {"Python", "Java"}
tillar.add("C++")
tillar.discard("Java") # Topilmasa ham xato bermaydi

print(tillar)
```

Natija:
```
{'Python', 'C++'}
```

---

## Misol 5 — Set amallari (Birlashma va Kesishma)

```python
frontend = {"HTML", "CSS", "JavaScript", "React"}
backend = {"Python", "Django", "JavaScript", "PostgreSQL"}

birgalikda = frontend.union(backend) # yoki frontend | backend
ortaq = frontend.intersection(backend) # yoki frontend & backend

print("Barcha texnologiyalar:", birgalikda)
print("Umumiy texnologiya:", ortaq)
```

Natija:
```
Barcha texnologiyalar: {'HTML', 'CSS', 'JavaScript', 'React', 'Python', 'Django', 'PostgreSQL'}
Umumiy texnologiya: {'JavaScript'}
```

---

## Misol 6 — Set amallari (Farq - Difference)

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

faqat_a = a.difference(b) # a - b
print("Faqat A da bor:", faqat_a)
```

Natija:
```
Faqat A da bor: {1, 2}
```

---

## Misol 7 — Tuple immutable ekanligini isbotlash

```python
koordinata = (41.2995, 69.2401)
try:
    koordinata[0] = 40.0
except TypeError as e:
    print("Xatolik ushlandi:", e)
```

Natija:
```
Xatolik ushlandi: 'tuple' object does not support item assignment
```

---

## Misol 8 — Frozenset (O'zgarmas Set)

```python
turgun_to_plam = frozenset([1, 2, 3, 3])
print(turgun_to_plam)
# turgun_to_plam.add(4) -> AttributeError beradi!
```

Natija:
```
frozenset({1, 2, 3})
```

---

# 5. Real loyiha misoli — Tizim foydalanuvchilari huquqini tekshirish

```python
# Tizimdagi rollar va ularning huquqlari (Set yordamida)
admin_huquqlari = {"read", "write", "delete", "execute"}
user_huquqlari = {"read", "write"}

# Foydalanuvchi sinovi
joriy_huquqlar = user_huquqlari.copy()

# Tekshirish
talab_qilingan = "delete"

if talab_qilingan in joriy_huquqlar:
    print("Amal bajarildi: O'chirildi.")
else:
    print(f"Ruxsat yo'q! '{talab_qilingan}' huquqi yetishmaydi.")
```

---

# 6. Ko'p uchraydigan xatolar

## Xato 1: Bitta elementli Tuple yaratishda vergulni unutish

Noto'g'ri:
```python
x = (5) # Bu int turi bo'lib qoladi!
print(type(x)) # <class 'int'>
```

To'g'ri:
```python
x = (5,)
print(type(x)) # <class 'tuple'>
```

## Xato 2: Bo'sh Set yaratishda {} ishlatish

Noto'g'ri:
```python
s = {} # Bu dict yaratadi!
print(type(s)) # <class 'dict'>
```

To'g'ri:
```python
s = set()
print(type(s)) # <class 'set'>
```

---

# 7. Sinfdagi amaliy topshiriqlar

1. **Oson**: 5 ta mevadan iborat Tuple yarating va 2-elementni ekranga chiqaring.
2. **O'rta**: Berilgan listdagi takrorlangan elementlarni Set yordamida tozalab, yana qayta List holatiga keltiring.
3. **Murakkab**: Ikki guruh talabalari ro'yxatidan faqat ikkala guruhda ham qatnashadigan talabalarni toping.

---

# 8. Uyga vazifa

1. Foydalanuvchi kiritgan matndagi barcha noyob harflarni aniqlovchi dastur yozing.
2. 3 ta Tuple elementini qabul qilib ularni bitta Tuple ga birlashtiring.
3. Set amallari yordamida ikki ro'yxat orasidagi faqat birida uchraydigan elementlarni (Symmetric Difference) toping.

---

# 9. Tekshirish savollari

1. Tuple va List orasidagi 2 ta asosiy farq nima?
2. Set ichida nima uchun bir xil element saqlanmaydi?
3. Bitta elementli Tuple qanday e'lon qilinadi?
4. `set.discard()` va `set.remove()` farqi nimada?
5. `frozenset` nima?

---

## Javoblar

1. List o'zgaruvchan (mutable) va sekinroq, Tuple o'zgarmas (immutable) va xotiradan samarali foydalanadi.
2. Set matematik to'plam bo'lib, uning barcha elementlari unikal bo'lishi shart.
3. Elementdan so'ng vergul qo'yish orqali: `(1,)`.
4. `remove()` element topilmasa `KeyError` beradi, `discard()` esa indamay o'tib ketadi.
5. `frozenset` — bu Set'ning o'zgarmas (immutable) variantidir.

---

# 10. Qisqa xulosa

Bu darsda Tuple va Set ma'lumot turlari, ularning o'ziga xos xususiyatlari, o'zgarmaslik (immutability), duplikatsiyalardan xalos bo'lish hamda to'plamlar ustida matematik amallar bajarish o'rganildi.
"""

# 14-DARS
lessons[14] = """# 📖 14. Dictionary — Dars dokumentatsiyasi

Dictionary (Lug'at) — Python'da ma'lumotlarni **Key-Value (Kalit-Qiymat)** juftligi ko'rinishida saqlaydigan eng qudratli ma'lumot strukturalaridan biridir. Har bir kalit (`key`) takrorlanmas bo'lib, u tegishli qiymatga (`value`) ishora qiladi.

Real hayotdagi ko'plab ma'lumotlar lug'at tuzilishiga ega: foydalanuvchi profili (ism, familiya, yosh), mahsulot xususiyatlari (narxi, nomi, ombordagi soni) yoki sozlamalar.

Dictionary Python 3.7+ versiyalaridan boshlab tartiblangan (ordered) hisoblanadi va xotiradan juda tez ma'lumot qidirish (Hash Table mexanizmi sababli) imkoniyatini beradi.

---

## Bu mavzu orqali nimalar qilish mumkin

- Key-Value ko'rinishida murakkab strukturaga ega ma'lumotlarni saqlash;
- Kalit bo'yicha qiymatni bir zumda olish va yangilash;
- Lug'at metodlari (`keys()`, `values()`, `items()`, `get()`) bilan ishlash;
- Lug'at elementlarini sikl yordamida aylanib chiqish;
- Ichma-ich (Nested) lug'atlar yaratish.

---

## Dars maqsadi

Bu dars oxirida o'quvchi:

- Dictionary yaratish va undan to'g'ri foydalanish;
- `get()` metodi orqali xavfsiz qiymat olish;
- Lug'atni o'zgartirish, qo'shish va o'chirish;
- `.items()` yordamida kalit va qiymatni birga iteratsiya qilish

ni mustaqil bajara oladi.

---

## Kerakli oldingi bilimlar

- 11-dars: List asoslari;
- 13-dars: Tuple va Set.

---

# 1. Asosiy tushunchalar va atamalar

## Dictionary (dict) nima?

> **Dictionary** — jingalak qavslar `{}` ichida `key: value` juftliklari ko'rinishida saqlanuvchi, o'zgaruvchan ma'lumot strukturasi.

## Key (Kalit) nima?

> **Key** — lug'atdagi har bir qiymatga murojaat qilish uchun ishlatiladigan unikal nom. Kalit har doim o'zgarmas (immutable) turda bo'lishi shart (str, int, tuple).

## Value (Qiymat) nima?

> **Value** — kalitga biriktirilgan ma'lumot. Har qanday turda (int, list, dict, bool va h.k.) bo'lishi mumkin.

---

# 2. Sintaksis va uning izohi

```python
# Lug'at yaratish
user = {
    "username": "ali123",
    "email": "ali@mail.com",
    "age": 25
}

# Murojaat qilish
print(user["username"]) # Ali123
print(user.get("age")) # 25
```

---

# 3. Dictionary metodlari jadvali

| Metod | Vazifasi | Misol |
|---|---|---|
| `.get(key, default)` | Kalit bo'yicha qiymat oladi (xavfsiz) | `d.get("age", 0)` |
| `.keys()` | Barcha kalitlar ro'yxatini beradi | `d.keys()` |
| `.values()` | Barcha qiymatlar ro'yxatini beradi | `d.values()` |
| `.items()` | Kalit-qiymat juftliklarini Tuple ko'rinishida beradi | `d.items()` |
| `.update(dict2)` | Boshqa lug'at bilan yangilaydi | `d.update({"a": 1})` |
| `.pop(key)` | Kalitli elementni o'chirib qiymatini qaytaradi | `d.pop("age")` |
| `.clear()` | Lug'atni to'liq tozalaydi | `d.clear()` |

---

# 4. Kod misollari

## Misol 1 — Lug'at yaratish va o'qish

```python
talaba = {
    "ism": "Vali",
    "yosh": 20,
    "kurs": 3
}

print(talaba["ism"])
print(talaba.get("guruh", "Guruh ko'rsatilmadi"))
```

Natija:
```
Vali
Guruh ko'rsatilmadi
```

---

## Misol 2 — Qiymatlarni o'zgartirish va qo'shish

```python
avto = {"model": "Cobalt", "rang": "Oq"}
avto["rang"] = "Qora" # O'zgartirish
avto["yil"] = 2023   # Yangi kalit qo'shish

print(avto)
```

Natija:
```
{'model': 'Cobalt', 'rang': 'Qora', 'yil': 2023}
```

---

## Misol 3 — Lug'at bo'ylab sikl (for loop)

```python
narxlar = {"olma": 12000, "banan": 25000, "uzum": 18000}

for mahsulot, narx in narxlar.items():
    print(f"{mahsulot.capitalize()}: {narx} so'm")
```

Natija:
```
Olma: 12000 so'm
Banan: 25000 so'm
Uzum: 18000 so'm
```

---

## Misol 4 — Elementni o'chirish (pop va del)

```python
baza = {"a": 1, "b": 2, "c": 3}
ochirilgan = baza.pop("b")

print("O'chirildi:", ochirilgan)
print("Qoldi:", baza)
```

Natija:
```
O'chirildi: 2
Qoldi: {'a': 1, 'c': 3}
```

---

## Misol 5 — Ichma-ich (Nested) lug'atlar

```python
xodimlar = {
    "emp1": {"ism": "Ali", "lavozim": "Dev"},
    "emp2": {"ism": "Sardor", "lavozim": "QA"}
}

print(xodimlar["emp1"]["ism"])
```

Natija:
```
Ali
```

---

# 5. Real loyiha misoli — Savat va Mahsulotlar hisobi

```python
mahsulotlar = {
    "1": {"nomi": "Noutbuk", "narx": 8000000},
    "2": {"nomi": "Sichqoncha", "narx": 150000}
}

savat = ["1", "2", "2"] # ID lardan iborat savat
jami = 0

print("--- SHAXSIY CHEK ---")
for item_id in set(savat):
    sanoq = savat.count(item_id)
    nom = mahsulotlar[item_id]["nomi"]
    narx = mahsulotlar[item_id]["narx"]
    summa = sanoq * narx
    jami += summa
    print(f"{nom} x {sanoq} ta = {summa} so'm")

print(f"JAMI TO'LOV: {jami} so'm")
```

---

# 6. Ko'p uchraydigan xatolar

## Xato 1: Mavjud bo'lmagan kalitga `[]` orqali murojaat qilish

Noto'g'ri:
```python
d = {"a": 1}
print(d["b"]) # KeyError beradi!
```

To'g'ri:
```python
print(d.get("b", "Topilmadi")) # Xavfsiz!
```

---

# 7. Sinfdagi amaliy topshiriqlar

1. **Oson**: 3 ta kalitli lug'at yarating va `.keys()` hamda `.values()` metodlarini chiqaring.
2. **O'rta**: Lug'at ichidagi barcha sonli qiymatlarning yig'indisini hisoblovchi kod yozing.

---

# 8. Uyga vazifa

1. Foydalanuvchi kiritgan matndagi har bir so'z necha marta uchrashini lug'atda hisoblang.
2. Lug'at kalitlari va qiymatlari o'rnini almashtiruvchi dastur tuzing.

---

# 9. Tekshirish savollari

1. Dictionary kaliti sifatida qaysi ma'lumot turlari ishlatilishi mumkin?
2. `get()` metodining afzalligi nimada?
3. `.items()` metodi nima qaytaradi?

---

## Javoblar

1. Faqat o'zgarmas (immutable) turlar: `str`, `int`, `float`, `tuple`.
2. Kalit topilmasa dastur qulab tushmaydi (`KeyError` bermaydi), balki `None` yoki default qiymat qaytaradi.
3. Kalit va qiymatlardan iborat `(key, value)` ko'rinishidagi tuple'lar ro'yxatini.

---

# 10. Qisqa xulosa

Bu darsda Dictionary ma'lumot strukturasi, Key-Value konseptsiyasi, lug'atlar ustida amallar bajarish va xavfsiz murojaat metodlari o'rganildi.
"""

for num, content in lessons.items():
    filepath = os.path.join(DOCS_DIR, f"dars_{num:02d}.md")
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"dars_{num:02d}.md yaratildi: {len(content)} belgi")
