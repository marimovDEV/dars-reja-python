# 🔄 8. While sikli — Dars dokumentatsiyasi

`while` sikli — shart `True` bo'lguncha kodni qayta-qayta bajaradigan boshqaruv strukturasi. `for` siklidan farqli o'laroq, `while` siklida takrorlash soni oldindan ma'lum bo'lishi shart emas — shart bajarilguncha davom etadi.

`while` sikli login tizimlarida (parol to'g'ri kiritilguncha so'rash), o'yinlarda (o'yin tugaguncha davom ettirish), real-time dasturlarda (server doim ishlashi kerak) va menyu tizimlarida (foydalanuvchi chiqishni tanlaguncha) keng qo'llaniladi.

Eng muhim qoida: `while` sikli ichida shart o'zgarishi kerak, aks holda cheksiz sikl (infinite loop) hosil bo'ladi va dastur to'xtamaydi.

---

## Bu mavzu orqali nimalar qilish mumkin

- Shartga asoslangan takrorlash;
- Hisoblagich (counter) bilan ishlash;
- Foydalanuvchi kiritishini kutuvchi sikllar;
- Menyu tizimi yaratish;
- while/else strukturasi.

---

## Dars maqsadi

Bu dars oxirida o'quvchi:

- `while` siklini to'g'ri yozish;
- Cheksiz sikllarni aniqlash va oldini olish;
- Hisoblagich bilan boshqariladigan sikllar;
- while/else strukturasini tushunish;
- Menyu tizimi yozish

ni mustaqil bajara oladi.

---

## Kerakli oldingi bilimlar

- 5-dars: If/elif/else;
- 7-dars: For sikli.

---

# 1. Asosiy tushunchalar

## while sikli nima?

> **`while`** — shart `True` bo'lguncha kod blokini qayta-qayta bajaradi. Shart `False` bo'lganda sikl to'xtaydi.

## Cheksiz sikl (Infinite Loop) nima?

> **Cheksiz sikl** — shart hech qachon `False` bo'lmaydigan sikl. Dastur to'xtamaydi va `Ctrl+C` bilan to'xtatish kerak.

## Hisoblagich nima?

> **Hisoblagich (counter)** — siklda iteratsiyalar sonini kuzatuvchi o'zgaruvchi. Har iteratsiyada qiymati o'zgaradi.

---

# 2. Sintaksis

```python
while shart:
    # shart True bo'lguncha bajariladi
    # shart o'zgarishi kerak!
```

---

# 3. while vs for jadvali

| Xususiyat | for | while |
|---|---|---|
| Takrorlash soni | Oldindan ma'lum | Noma'lum bo'lishi mumkin |
| Asoslangan | Ketma-ketlik | Shart |
| Cheksiz sikl xavfi | Yo'q | Bor |
| Qachon ishlatiladi | List, range, string takrorlash | Shart tekshiruvi, menyu, o'yin |

---

# 4. Kod misollari

## Misol 1 — Sodda while

```python
hisoblagich = 1

while hisoblagich <= 5:
    print(hisoblagich)
    hisoblagich += 1
```

Natija: `1 2 3 4 5`

---

## Misol 2 — Foydalanuvchi kiritishini kutish

```python
parol = ""

while parol != "secret123":
    parol = input("Parol kiriting: ")

print("Tizimga kirdingiz!")
```

---

## Misol 3 — Yig'indi hisoblash

```python
yigindi = 0
son = int(input("Son kiriting (0 — tugatish): "))

while son != 0:
    yigindi += son
    son = int(input("Son kiriting (0 — tugatish): "))

print(f"Yig'indi: {yigindi}")
```

---

## Misol 4 — Teskari hisoblash

```python
sekund = 10

while sekund > 0:
    print(sekund, end=" ")
    sekund -= 1

print("Start!")
```

Natija: `10 9 8 7 6 5 4 3 2 1 Start!`

---

## Misol 5 — while/else

```python
n = 7
i = 2
tub = True

while i < n:
    if n % i == 0:
        tub = False
        break
    i += 1
else:
    print(f"{n} — tub son")

if not tub:
    print(f"{n} — tub emas")
```

---

## Misol 6 — Cheksiz sikl bilan menyu

```python
while True:
    print("
=== MENYU ===")
    print("1. Salom")
    print("2. Vaqt")
    print("3. Chiqish")
    
    tanlov = input("Tanlang: ")
    
    if tanlov == "1":
        print("Salom, foydalanuvchi!")
    elif tanlov == "2":
        import datetime
        print(datetime.datetime.now())
    elif tanlov == "3":
        print("Xayr!")
        break
    else:
        print("Noto'g'ri tanlov!")
```

---

## Misol 7 — Son topish o'yini

```python
import random

maxfiy_son = random.randint(1, 100)
urinishlar = 0

print("1 dan 100 gacha son o'yladim. Toping!")

while True:
    taxmin = int(input("Taxminingiz: "))
    urinishlar += 1
    
    if taxmin < maxfiy_son:
        print("Kattaroq!")
    elif taxmin > maxfiy_son:
        print("Kichikroq!")
    else:
        print(f"To'g'ri! {urinishlar} ta urinishda topdingiz!")
        break
```

---

## Misol 8 — Raqamlar yig'indisi

```python
son = int(input("Son kiriting: "))
asl_son = son
yigindi = 0

while son > 0:
    raqam = son % 10
    yigindi += raqam
    son //= 10

print(f"{asl_son} ning raqamlari yig'indisi: {yigindi}")
```

---

# 5. Real loyiha misoli — ATM simulyatsiyasi

```python
balans = 1000000

while True:
    print(f"
Balans: {balans:,} so'm")
    print("1. Pul yechish")
    print("2. Pul qo'yish")
    print("3. Chiqish")
    
    tanlov = input("Tanlang: ")
    
    if tanlov == "1":
        summa = int(input("Miqdor: "))
        if summa <= balans:
            balans -= summa
            print(f"{summa:,} so'm yechildi.")
        else:
            print("Mablag' yetarli emas!")
    elif tanlov == "2":
        summa = int(input("Miqdor: "))
        balans += summa
        print(f"{summa:,} so'm qo'yildi.")
    elif tanlov == "3":
        print("Xayr!")
        break
```

---

# 6. Ko'p uchraydigan xatolar

## Xato 1: Cheksiz sikl

```python
x = 1
while x <= 5:
    print(x)
    # x += 1 UNUTILDI — cheksiz sikl!
```

## Xato 2: Shartni noto'g'ri yozish

```python
while x = 5:  # SyntaxError! == bo'lishi kerak
    pass
```

## Xato 3: while True dan chiqishni unutish

```python
while True:
    print("Cheksiz!")
    # break yo'q — dastur to'xtamaydi
```

## Xato 4: Hisoblagichni sikl ichida noto'g'ri joyda o'zgartirish

```python
i = 0
while i < 5:
    i += 1  # i o'zgarishi sikl boshida
    print(i)
# 1, 2, 3, 4, 5 chiqadi (0 chiqmaydi)
```

---

# 7. Sinfdagi amaliy topshiriqlar

## 1-topshiriq — Oson

**Vazifa:** 1 dan 20 gacha bo'lgan toq sonlarni while bilan chiqaring.

## 2-topshiriq — O'rta

**Vazifa:** Parol kiritish tizimi: 3 ta urinish, har safar xato bo'lsa qoldiq urinishlarni ko'rsating.

## 3-topshiriq — Murakkab

**Vazifa:** ATM simulyatsiyasi: balansni ko'rish, pul yechish, pul qo'yish va chiqish imkoniyatlari.

---

# 8. Uyga vazifa

1. while bilan 1 dan 100 gacha bo'lgan juft sonlarning yig'indisini hisoblang.
2. Foydalanuvchidan sonlar oling (0 kiritilguncha), eng kattasini toping.
3. Sonning tub ekanligini while bilan tekshiring.
4. Son topish o'yini yozing (1-100 orasida, kompyuter o'ylaydi).
5. Sonni ikkilik sanoq tizimiga while bilan aylantiring.

---

# 9. Tekshirish savollari

1. `while` siklining `for` siklidan asosiy farqi nima?
2. Cheksiz sikl qanday hosil bo'ladi?
3. `while True:` qachon ishlatiladi?
4. `while/else` strukturasi qanday ishlaydi?
5. Hisoblagich nima va nima uchun kerak?
6. `Ctrl+C` nima qiladi?
7. `break` while siklida qanday ishlaydi?
8. while siklida shart qachon tekshiriladi?
9. `do-while` sikli Python'da bormi?
10. while siklida `continue` nima qiladi?

---

## Javoblar

**1.** `for` — takrorlash soni oldindan ma'lum (ketma-ketlik bo'ylab). `while` — shart `True` bo'lguncha davom etadi, takrorlash soni oldindan ma'lum bo'lishi shart emas.

**2.** Shart hech qachon `False` bo'lmasa: `while True:` yoki shart o'zgaruvchisi yangilanmasa.

**3.** `while True:` menyu tizimlarida, o'yinlarda, server dasturlarida ishlatiladi — `break` bilan boshqariladi.

**4.** `else` bloki sikl `break` siz tugatilganda bajariladi. `break` bilan tugatilsa, `else` bajarilmaydi.

**5.** Hisoblagich — siklda iteratsiyalar sonini kuzatuvchi o'zgaruvchi. Siklni tugatish sharti sifatida ishlatiladi.

**6.** `Ctrl+C` — cheksiz siklni tashqaridan to'xtatadi (`KeyboardInterrupt` xatosi).

**7.** `break` siklni darhol to'xtatadi va sikldan keyingi kodga o'tadi.

**8.** Shart har bir iteratsiya boshida tekshiriladi. Shart `False` bo'lsa, sikl tanasi bajarilmaydi.

**9.** Python'da `do-while` yo'q. Uning o'rniga `while True:` + `break` ishlatiladi.

**10.** `continue` — joriy iteratsiyaning qolgan qismini o'tkazib yuborib, keyingi iteratsiyani boshlaydi.

---

# 10. Qisqa xulosa

Bu darsda:

- `while` sikli va shartga asoslangan takrorlash;
- Cheksiz sikllar va ularni boshqarish;
- Hisoblagich bilan ishlash;
- while/else strukturasi;
- Menyu tizimi va ATM simulyatsiyasi

o'rganildi.

---

Keyingi **9-dars: Break, continue va random** da sikl oqimini boshqarish va tasodifiy sonlar bilan ishlash o'rganiladi.

---

# Resurslar va fayllar

- 📄 Python while: https://docs.python.org/3/reference/compound_stmts.html#the-while-statement
- 💻 Kodlar: `github.com/dars-reja/08-dars`
- 🎬 Video dars: `youtube.com/watch?v=dars08`
