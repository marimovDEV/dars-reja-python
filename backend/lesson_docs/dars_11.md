# 📋 11. List asoslari — Dars dokumentatsiyasi

List (ro'yxat) — Python'dagi eng ko'p ishlatiladigan ma'lumot strukturasi bo'lib, bir nechta elementni bitta o'zgaruvchida tartibli saqlash imkonini beradi. List o'zgaruvchan (mutable) — elementlarni qo'shish, o'chirish va o'zgartirish mumkin.

List bilan ishlash Python dasturlashning asosiy qismi: talabalar ro'yxati, mahsulotlar katalogi, ballar jadvali — bularning barchasi list orqali saqlanadi va qayta ishlanadi.

Python listlari har xil turdagi elementlarni saqlashi mumkin (sonlar, matnlar, boshqa listlar), ularga indeks orqali murojaat qilish, slicing bilan kesish va 10 dan ortiq ichki metod bilan ishlash mumkin.

---

## Bu mavzu orqali nimalar qilish mumkin

- Listlar yaratish va elementlarga murojaat qilish;
- Element qo'shish, o'chirish va o'zgartirish;
- List metodlari bilan ishlash;
- Listni saralash va qidirish;
- List comprehension (qisqa yaratish).

---

## Dars maqsadi

Bu dars oxirida o'quvchi:

- List yaratish va indekslash;
- Kamida 10 ta list metodini bilish;
- Slicing bilan ishlash;
- List comprehension yozish;
- Listlarda qidirish va saralash

ni mustaqil bajara oladi.

---

## Kerakli oldingi bilimlar

- 2-dars: O'zgaruvchilar;
- 4-dars: Stringlar (indekslash, slicing);
- 7-dars: For sikli.

---

# 1. Asosiy tushunchalar

## List nima?

> **List** — tartibli, o'zgaruvchan elementlar to'plami. Kvadrat qavslar ichida yaratiladi: `[1, 2, 3]`.

## Mutable nima?

> **Mutable** — o'zgaruvchan. Listdagi elementlarni qo'shish, o'chirish va o'zgartirish mumkin (stringdan farqli).

## List comprehension nima?

> **List comprehension** — listni qisqa yozish usuli: `[x**2 for x in range(5)]` = `[0, 1, 4, 9, 16]`.

---

# 2. List metodlari jadvali

| Metod | Vazifasi | Misol | Natija |
|---|---|---|---|
| `append(x)` | Oxirga element qo'shish | `[1,2].append(3)` | `[1,2,3]` |
| `insert(i, x)` | i indeksga qo'shish | `[1,3].insert(1, 2)` | `[1,2,3]` |
| `extend(list)` | Boshqa listni qo'shish | `[1].extend([2,3])` | `[1,2,3]` |
| `remove(x)` | Birinchi x ni o'chirish | `[1,2,3].remove(2)` | `[1,3]` |
| `pop(i)` | i indeksdagi elementni olish | `[1,2,3].pop(1)` | `2`, list: `[1,3]` |
| `pop()` | Oxirgi elementni olish | `[1,2,3].pop()` | `3`, list: `[1,2]` |
| `clear()` | Barcha elementlarni tozalash | `[1,2,3].clear()` | `[]` |
| `sort()` | Tartibga solish | `[3,1,2].sort()` | `[1,2,3]` |
| `reverse()` | Teskari tartibga | `[1,2,3].reverse()` | `[3,2,1]` |
| `count(x)` | x necha marta uchrashini sanash | `[1,2,2,3].count(2)` | `2` |
| `index(x)` | x ning indeksini topish | `[1,2,3].index(2)` | `1` |
| `copy()` | Nusxa olish | `[1,2,3].copy()` | `[1,2,3]` |

---

# 3. Kod misollari

## Misol 1 — List yaratish va indekslash

```python
mevalar = ["olma", "banan", "uzum", "anor"]
print(mevalar[0])
print(mevalar[-1])
print(mevalar[1:3])
```

Natija:

```
olma
anor
['banan', 'uzum']
```

---

## Misol 2 — Element qo'shish

```python
sonlar = [10, 20, 30]
sonlar.append(40)
sonlar.insert(0, 5)
print(sonlar)
```

Natija: `[5, 10, 20, 30, 40]`

---

## Misol 3 — Element o'chirish

```python
mevalar = ["olma", "banan", "uzum", "anor"]
mevalar.remove("banan")
oxirgi = mevalar.pop()
print(mevalar)
print(f"Olib tashlangan: {oxirgi}")
```

Natija: `['olma', 'uzum']`, `Olib tashlangan: anor`

---

## Misol 4 — sort() va reverse()

```python
sonlar = [64, 25, 12, 22, 11]
sonlar.sort()
print(f"Tartibda: {sonlar}")

sonlar.sort(reverse=True)
print(f"Teskari: {sonlar}")
```

---

## Misol 5 — List bilan for sikli

```python
baholar = [85, 92, 78, 95, 67]

for i, baho in enumerate(baholar, 1):
    if baho >= 90:
        daraja = "A'lo"
    elif baho >= 70:
        daraja = "Yaxshi"
    else:
        daraja = "Qoniqarli"
    print(f"{i}. {baho} — {daraja}")
```

---

## Misol 6 — List comprehension

```python
kvadratlar = [x ** 2 for x in range(1, 11)]
print(kvadratlar)

juft = [x for x in range(1, 21) if x % 2 == 0]
print(juft)
```

Natija:

```
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
```

---

## Misol 7 — Ichma-ich list (2D list)

```python
matritsa = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for qator in matritsa:
    for element in qator:
        print(f"{element:3}", end="")
    print()
```

---

## Misol 8 — in operatori va index()

```python
tillar = ["Python", "Java", "C++", "JavaScript"]

til = input("Dasturlash tili: ")
if til in tillar:
    joy = tillar.index(til)
    print(f"{til} ro'yxatda bor, indeksi: {joy}")
else:
    print(f"{til} ro'yxatda yo'q")
```

---

# 5. Real loyiha misoli — Savdo tizimi

```python
savat = []

while True:
    print(f"
Savat: {savat}")
    print("1. Mahsulot qo'shish")
    print("2. Mahsulot o'chirish")
    print("3. Savatni tozalash")
    print("4. Chiqish")
    
    tanlov = input("Tanlang: ")
    
    if tanlov == "1":
        mahsulot = input("Mahsulot nomi: ")
        savat.append(mahsulot)
    elif tanlov == "2":
        mahsulot = input("O'chirish: ")
        if mahsulot in savat:
            savat.remove(mahsulot)
        else:
            print("Topilmadi!")
    elif tanlov == "3":
        savat.clear()
    elif tanlov == "4":
        break
```

---

# 6. Ko'p uchraydigan xatolar

## Xato 1: Mavjud bo'lmagan indeksga murojaat

```python
a = [1, 2, 3]
print(a[5])  # IndexError!
```

## Xato 2: remove() ga mavjud bo'lmagan element berish

```python
a = [1, 2, 3]
a.remove(5)  # ValueError!
```

## Xato 3: List nusxalash xatosi

```python
a = [1, 2, 3]
b = a  # nusxa EMAS, havola!
b.append(4)
print(a)  # [1, 2, 3, 4] — a ham o'zgardi!
```

To'g'ri: `b = a.copy()` yoki `b = a[:]`.

## Xato 4: sort() natija qaytarmaydi

```python
a = [3, 1, 2]
b = a.sort()  # b = None!
```

To'g'ri: `b = sorted(a)`.

---

# 7. Sinfdagi amaliy topshiriqlar

## 1-topshiriq — Oson

**Vazifa:** 5 ta son kiritib, eng katta va kichigini toping.

## 2-topshiriq — O'rta

**Vazifa:** List comprehension bilan 1-50 orasidagi 3 ga bo'linadigan sonlarni toping.

## 3-topshiriq — Murakkab

**Vazifa:** Savdo tizimi: mahsulot qo'shish, o'chirish, jami narxni hisoblash.

---

# 8. Uyga vazifa

1. 10 ta son kiritib, o'rtacha, eng katta va eng kichigini toping.
2. Ikki listdagi umumiy elementlarni toping.
3. Listdagi dublikat elementlarni olib tashlang.
4. Listni teskari tartibda chiqaring (reverse() ishlatmang).
5. List comprehension bilan 1-100 orasidagi tub sonlar listini yarating.

---

# 9. Tekshirish savollari

1. List nima va qanday yaratiladi?
2. List va string o'rtasidagi asosiy farq nima?
3. `append()` va `extend()` farqi nima?
4. `remove()` va `pop()` farqi nima?
5. List slicing qanday ishlaydi?
6. `sort()` va `sorted()` farqi nima?
7. List comprehension nima?
8. `a = b` va `a = b.copy()` farqi nima?
9. `in` operatori listlarda qanday ishlaydi?
10. 2D list nima?

---

## Javoblar

**1.** List — tartibli, o'zgaruvchan elementlar to'plami. `sonlar = [1, 2, 3]` yoki `bo_sh = []`.

**2.** List mutable (o'zgaruvchan): `a[0] = "x"` ishlaydi. String immutable: `s[0] = "x"` xato beradi.

**3.** `append(x)` — bitta elementni oxirga qo'shadi. `extend([1,2])` — boshqa listning barcha elementlarini qo'shadi.

**4.** `remove(x)` — qiymat bo'yicha birinchi x ni o'chiradi. `pop(i)` — indeks bo'yicha o'chirib, qiymatni qaytaradi.

**5.** `list[start:stop:step]` — stringdagi kabi ishlaydi. `a[1:3]` — 1 dan 3 gacha (3 kirmaydi).

**6.** `sort()` — listning o'zini saralaydi, `None` qaytaradi. `sorted(list)` — yangi saralangan list qaytaradi, asl list o'zgarmaydi.

**7.** Listni bitta qatorda yaratish usuli: `[ifoda for x in ketmaketlik if shart]`.

**8.** `a = b` — ikkalasi bitta listga havola. `a = b.copy()` — mustaqil nusxa yaratadi.

**9.** `x in list` — x element listda bormi tekshiradi. `True` yoki `False` qaytaradi.

**10.** List ichidagi list: `matritsa = [[1,2],[3,4]]`. Jadval yoki matritsa ifodalash uchun.

---

# 10. Qisqa xulosa

Bu darsda:

- List yaratish va indekslash;
- 12 ta list metodi;
- List comprehension;
- 2D listlar (matritsa);
- Slicing va nusxalash

o'rganildi.

---

Keyingi **12-dars: 1-modul imtihoni** da 1-11 darslar bo'yicha yakuniy tekshiruv o'tkaziladi.

---

# Resurslar va fayllar

- 📄 Python Lists: https://docs.python.org/3/tutorial/datastructures.html#more-on-lists
- 💻 Kodlar: `github.com/dars-reja/11-dars`
- 🎬 Video dars: `youtube.com/watch?v=dars11`
