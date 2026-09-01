# ⏹️ 9. Break, continue va random — Dars dokumentatsiyasi

`break` va `continue` — bu sikl ichidagi oqimni boshqarish buyruqlari. `break` siklni to'liq to'xtatadi, `continue` esa joriy iteratsiyani o'tkazib yuborib keyingi iteratsiyaga o'tadi.

`random` moduli — Python'ning tasodifiy sonlar va tanlovlar bilan ishlash uchun ishlatiladigan standart kutubxonasi. U o'yinlar, simulyatsiyalar, test ma'lumotlari yaratish va xavfsizlikda keng qo'llaniladi.

Bu uchta tushuncha birgalikda kuchli algoritmlar yaratish imkonini beradi: masalan, tasodifiy son o'yini, yoki ma'lum shartlar asosida siklni boshqarish.

---

## Bu mavzu orqali nimalar qilish mumkin

- Siklni muayyan shartda to'xtatish (`break`);
- Muayyan elementlarni o'tkazib yuborish (`continue`);
- Tasodifiy butun sonlar yaratish (`randint`);
- Ro'yxatdan tasodifiy element tanlash (`choice`);
- O'yin va simulyatsiya dasturlari yozish.

---

## Dars maqsadi

Bu dars oxirida o'quvchi:

- `break` va `continue` ni to'g'ri qo'llash;
- `random` modulining asosiy funksiyalarini bilish;
- O'yinlar va amaliy dasturlarda qo'llash

ni mustaqil bajara oladi.

---

## Kerakli oldingi bilimlar

- 7-dars: For sikli;
- 8-dars: While sikli.

---

# 1. Asosiy tushunchalar

## break nima?

> **`break`** — siklni darhol to'xtatadi va sikldan keyingi kodga o'tadi. `for` va `while` ikkisida ham ishlaydi.

## continue nima?

> **`continue`** — joriy iteratsiyaning qolgan qismini o'tkazib yuborib, keyingi iteratsiyani boshlaydi.

## random nima?

> **`random`** — Python'ning standart kutubxonasi bo'lib, tasodifiy sonlar va tanlovlar bilan ishlash uchun ishlatiladi. `import random` bilan yuklanadi.

---

# 2. random funksiyalari jadvali

| Funksiya | Vazifasi | Misol | Natija |
|---|---|---|---|
| `randint(a, b)` | a dan b gacha tasodifiy butun son | `random.randint(1, 10)` | `7` (masalan) |
| `random()` | 0.0 dan 1.0 gacha tasodifiy float | `random.random()` | `0.583...` |
| `choice(list)` | Listdan tasodifiy element | `random.choice(["a","b"])` | `"b"` |
| `shuffle(list)` | Listni aralashtiradi | `random.shuffle(sonlar)` | list o'zgaradi |
| `sample(list, n)` | n ta noyob tasodifiy element | `random.sample(range(100), 5)` | `[23, 7, ...]` |
| `uniform(a, b)` | a dan b gacha tasodifiy float | `random.uniform(1.0, 5.0)` | `3.14...` |

---

# 3. Kod misollari

## Misol 1 — break

```python
for i in range(1, 11):
    if i == 6:
        print("6 topildi, sikl to'xtadi!")
        break
    print(i)
```

Natija: `1 2 3 4 5 6 topildi, sikl to'xtadi!`

---

## Misol 2 — continue

```python
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)
```

Natija: `1 3 5 7 9` (juft sonlar o'tkazib yuborildi)

---

## Misol 3 — break bilan qidiruv

```python
sonlar = [4, 7, 2, 9, 1, 5, 8]
qidirilayotgan = 9

for son in sonlar:
    if son == qidirilayotgan:
        print(f"{qidirilayotgan} topildi!")
        break
else:
    print(f"{qidirilayotgan} topilmadi.")
```

---

## Misol 4 — random.randint()

```python
import random

for i in range(5):
    son = random.randint(1, 100)
    print(f"Tasodifiy son: {son}")
```

---

## Misol 5 — random.choice()

```python
import random

ranglar = ["qizil", "ko'k", "yashil", "sariq", "oq"]
tanlangan = random.choice(ranglar)
print(f"Tasodifiy rang: {tanlangan}")
```

---

## Misol 6 — Son topish o'yini

```python
import random

son = random.randint(1, 50)
urinish = 0

while True:
    taxmin = int(input("Taxminingiz (1-50): "))
    urinish += 1
    
    if taxmin < son:
        print("Kattaroq!")
    elif taxmin > son:
        print("Kichikroq!")
    else:
        print(f"To'g'ri! {urinish} ta urinishda topdingiz!")
        break
```

---

## Misol 7 — Parol generatori

```python
import random
import string

uzunlik = 12
belgilar = string.ascii_letters + string.digits + "!@#$%"
parol = ""

for i in range(uzunlik):
    parol += random.choice(belgilar)

print(f"Yangi parol: {parol}")
```

---

## Misol 8 — Tosh-qaychi-qog'oz

```python
import random

tanlovlar = ["tosh", "qaychi", "qog'oz"]

while True:
    player = input("Tanlang (tosh/qaychi/qog'oz/chiqish): ").lower()
    if player == "chiqish":
        break
    
    computer = random.choice(tanlovlar)
    print(f"Kompyuter: {computer}")
    
    if player == computer:
        print("Durrang!")
    elif (player == "tosh" and computer == "qaychi") or          (player == "qaychi" and computer == "qog'oz") or          (player == "qog'oz" and computer == "tosh"):
        print("Siz yutdingiz!")
    else:
        print("Kompyuter yutdi!")
```

---

# 5. Real loyiha misoli — Viktorina o'yini

```python
import random

savollar = [
    {"savol": "Python qaysi yilda yaratilgan?", "javob": "1991"},
    {"savol": "Python yaratuvchisi kim?", "javob": "Guido van Rossum"},
    {"savol": "print() nima qiladi?", "javob": "ekranga chiqaradi"},
]

random.shuffle(savollar)
ball = 0

for s in savollar:
    javob = input(f"{s['savol']} ")
    if javob.lower() == s["javob"].lower():
        print("To'g'ri!")
        ball += 1
    else:
        print(f"Noto'g'ri! Javob: {s['javob']}")

print(f"
Natija: {ball}/{len(savollar)}")
```

---

# 6. Ko'p uchraydigan xatolar

## Xato 1: break ichma-ich siklda faqat ichki siklni to'xtatadi

```python
for i in range(3):
    for j in range(3):
        if j == 1:
            break  # faqat ichki sikl to'xtaydi
    print(f"i = {i}")
```

## Xato 2: continue dan keyin muhim kod

```python
for i in range(5):
    if i == 2:
        continue
    print(i)
    # i==2 da bu print BAJARILMAYDI
```

## Xato 3: random import qilmaslik

```python
son = random.randint(1, 10)  # NameError!
```

To'g'ri: `import random` birinchi qator.

## Xato 4: randint chegaralari

```python
random.randint(1, 10)  # 1 HAM 10 HAM kiradi (range dan farqli!)
```

---

# 7. Sinfdagi amaliy topshiriqlar

## 1-topshiriq — Oson

**Vazifa:** 1 dan 20 gacha, 13 ni o'tkazib yuboruvchi dastur yozing (continue).

## 2-topshiriq — O'rta

**Vazifa:** 10 ta tasodifiy son yarating (1-100), ular orasidan 50 dan kattalarini chiqaring.

## 3-topshiriq — Murakkab

**Vazifa:** Tosh-qaychi-qog'oz o'yini: 3 ta g'alaba kerak, natijani hisoblab boring.

---

# 8. Uyga vazifa

1. Listdan birinchi manfiy sonni topib, siklni to'xtating.
2. 1-100 orasida faqat 3 ga va 5 ga bo'linadigan sonlarni chiqaring.
3. Tasodifiy 20 ta son yaratib, juft va toqlarini alohida sanang.
4. Loto o'yini: 6 ta noyob tasodifiy son (1-49) yarating.
5. "Harfni top" o'yini: kompyuter harf o'ylaydi, foydalanuvchi topadi.

---

# 9. Tekshirish savollari

1. `break` nima qiladi?
2. `continue` nima qiladi?
3. `break` va `continue` orasidagi farq nima?
4. `random.randint(1, 10)` qanday sonlar qaytaradi?
5. `random.choice()` nima qiladi?
6. `random.shuffle()` nima qiladi?
7. Ichma-ich siklda `break` qaysi siklni to'xtatadi?
8. `for/else` da `else` qachon bajariladi?
9. `import random` ni qayerga yozish kerak?
10. `random.random()` va `random.randint()` farqi nima?

---

## Javoblar

**1.** `break` — siklni darhol to'xtatadi va sikldan keyingi kodga o'tadi.

**2.** `continue` — joriy iteratsiyaning qolgan qismini o'tkazib, keyingi iteratsiyani boshlaydi.

**3.** `break` siklni butunlay to'xtatadi. `continue` faqat joriy iteratsiyani o'tkazib yuboradi, sikl davom etadi.

**4.** 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 — 1 ham 10 ham kiradi (`range` dan farqli).

**5.** `random.choice(list)` — listdan tasodifiy bitta element tanlaydi va qaytaradi.

**6.** `random.shuffle(list)` — listning o'zini (in-place) tasodifiy tartibda aralashtiradi.

**7.** Faqat eng ichki siklni to'xtatadi. Tashqi siklga ta'sir qilmaydi.

**8.** `else` bloki sikl `break` siz, tabiiy tugatilganda bajariladi. Agar `break` ishlasa, `else` bajarilmaydi.

**9.** Faylning boshida, koddan oldin. `import random` standart Python kutubxonasini yuklaydi.

**10.** `random.random()` — 0.0 dan 1.0 gacha float. `random.randint(a, b)` — a dan b gacha butun son (ikkalasi ham kiradi).

---

# 10. Qisqa xulosa

Bu darsda:

- `break` — siklni to'xtatish;
- `continue` — iteratsiyani o'tkazish;
- `random` moduli: `randint`, `choice`, `shuffle`, `sample`;
- O'yinlar va amaliy dasturlar

o'rganildi.

---

Keyingi **10-dars: Ichma-ich sikl va algoritmlar** da naqshlar, matritsa va murakkab algoritmlar o'rganiladi.

---

# Resurslar va fayllar

- 📄 break/continue: https://docs.python.org/3/tutorial/controlflow.html#break-and-continue-statements
- 📄 random: https://docs.python.org/3/library/random.html
- 💻 Kodlar: `github.com/dars-reja/09-dars`
- 🎬 Video dars: `youtube.com/watch?v=dars09`
