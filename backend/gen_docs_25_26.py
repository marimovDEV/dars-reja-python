#!/usr/bin/env python3
"""Generate lesson docs 25-30 (OOP module) with full 19-section documentation template."""
import os

DOCS_DIR = os.path.join(os.path.dirname(__file__), "lesson_docs")

lessons = {}

# 25-DARS
lessons[25] = """# 🏛️ 25. OOP, Class va Object — Dars dokumentatsiyasi

**Ob'yektga Yo'naltirilgan Dasturlash (OOP - Object-Oriented Programming)** — bu dastur mantiqini real dunyo obyektlari va ularning o mezonidagi munosabatlari ko'rinishida modellashtiruvchi dasturlash paradiqmasidir.

Shu vaqtgacha o mezon qilingan funksional dasturlashda ma'lumotlar va funksiyalar alohida saqlangan bo'lsa, OOP da ma'lumotlar (atributlar) va ular ustida bajariladigan amallar (metodlar) bitta **Obyekt** ichiga biriktiriladi.

Python'da har bir narsa (sonlar, matnlar, ro'yxatlar) obyekt hisoblanadi. Ushbu darsda siz obyektlar yaratish uchun shablon vazifasini o'tovchi **Klass (Class)** va undan nusxa olib yaratiluvchi **Obyekt (Object/Instance)** tushunchalarini o'rganasiz.

---

## Bu mavzu orqali nimalar qilish mumkin

- Dasturni modulli, tushunarli va qayta ishlatiladigan (reusable) tuzilishga keltirish;
- Shaxsiy Klasslar (`Class`) yaratish va uning obyektlarini e'lon qilish;
- Obyekt atributlari (xususiyatlari) va metodlarini (funksiyalarini) belgilash;
- Real dunyodagi (masalan: Avtomobil, Bank Hisobi, Foydalanuvchi) tushunchalarni kodda modellashtirish.

---

## Dars maqsadi

Bu dars oxirida o'quvchi:

- OOP paradiqmasining afzalliklarini va asosiy 4 ustunini bilish;
- Klass va Obyekt o'rtasidagi farqni tushunish (Chizma va Bino o'xshatishi);
- `class` kalit so'zi bilan yangi tur e'lon qilish;
- Obyekt xususiyatlari hamda metodlariga murojaat qilish

ni mustaqil bajara oladi.

---

## Kerakli oldingi bilimlar

- 14-dars: Dictionary;
- 17-dars: Funksiyalar.

---

# 1. Asosiy tushunchalar va atamalar

## OOP (Object-Oriented Programming) nima?

> **OOP** — dasturni obyektlar to'plami sifatida ko'radigan yondashuv.

## Class (Klass) nima?

> **Class** — obyektlarni yaratish uchun mo mezon mo'ljallangan qolip, shablon yoki chizma. U obyektning qanday xususiyatlari va metodlari bo'lishini belgilaydi.

## Object / Instance (Obyekt) nima?

> **Object** — klass shabloni asosida xotiradan joy olgan haqiqiy obyekt nusxasi.

## Attribute va Method nima?

> **Attribute (Atribut)** — obyekt saqlaydigan ma'lumotlar (o'zgaruvchilar). **Method (Metod)** — obyekt bajarishi mumkin bo'lgan harakatlar (funksiyalar).

---

# 2. Sintaksis va uning izohi

```python
# Klass yaratish
class Avtomobil:
    pass

# Obyekt yaratish (Instance)
spark = Avtomobil()
cobalt = Avtomobil()
```

---

# 3. Klass va Obyekt Farqlari Jadvali

| Xususiyat | Class (Klass) | Object (Obyekt) |
|---|---|---|
| Tavsifi | Shablon, loyiha, chizma | Xotiradagi haqiqiy obyekt |
| Xotiradagi o'rni | Faqat klass kodi saqlanadi | Har bir obyekt alohida xotira egallaydi |
| Misol | `Avtomobil` chizmasi | `Cobalt` (Rang: Oq, Yil: 2023) |

---

# 4. Kod misollari

## Misol 1 — Birinchi sodda Klass va Obyekt

```python
class Talaba:
    pass

# 2 ta obyekt yaratamiz
t1 = Talaba()
t2 = Talaba()

# Atribut biriktiramiz
t1.ism = "Ali"
t1.yosh = 20

t2.ism = "Vali"

print(f"1-Talaba: {t1.ism}, {t1.yosh} yosh")
print(f"2-Talaba: {t2.ism}")
```

---

## Misol 2 — Klass ichida Metod yaratish

```python
class Telefon:
    model = "iPhone 15" # Klass atributi
    
    def zang_qil(self):
        print(f"{self.model} dan qo'ng'iroq qilinmoqda...")

p1 = Telefon()
p1.zang_qil()
```

---

## Misol 3 — Obyekt atributlarini dinamik o'zgartirish

```python
class Kuchuk:
    laqab = "Tobi"

k1 = Kuchuk()
k2 = Kuchuk()

k2.laqab = "Reks"

print("k1 laqabi:", k1.laqab) # Tobi
print("k2 laqabi:", k2.laqab) # Reks
```

---

# 5. Real loyiha misoli — Avtosalon va Mashinalar Boshqaruvi

```python
class Car:
    marka = "Chevrolet"
    
    def info(self, nom, narx):
        print(f"Marka: {self.marka} | Model: {nom} | Narx: ${narx:,}")

car1 = Car()
car1.info("Onix", 15000)

car2 = Car()
car2.info("Tracker", 21000)
```

---

# 6. Ko'p uchraydigan xatolar

## Xato 1: Metodda `self` argumentini unutish

Noto'g'ri:
```python
class Xato:
    def hi(): # self yozilmadi!
        print("Hi")

x = Xato()
x.hi() # TypeError: hi() takes 0 positional arguments but 1 was given
```

To mezon: Klass metodlarida har doim birinchi parametr `self` bo'lishi shart!

---

# 7. Sinfdagi amaliy topshiriqlar

1. **Oson**: `Kitob` nomli klass yarating va undan 2 ta obyekt olib nom va muallif biriktiring.
2. **O'rta**: `Kalkulyator` klassini yarating, uning ichida `qo_shish(a, b)` va `ayirish(a, b)` metodlari bo'lsin.

---

# 8. Uyga vazifa

1. `Magazin` klassini yarating. Unda mahsulot nomlari ro'yxati va yangi mahsulot qo'shuvchi `add_item()` metodi bo'lsin.

---

# 9. Tekshirish savollari

1. Klass va Obyekt o'rtasidagi asosiy farq nimada?
2. Klass ichidagi metodda `self` nimani anglatadi?

---

## Javoblar

1. Klass bu ma'lumot va metodlar loyihasi/shablonidir, Obyekt esa shu shablon asosida yaratilgan haqiqiy obyekt nusxasidir.
2. `self` joriy chaqirilayotgan obyektning o'ziga ishora qiluvchi havola.

---

# 10. Qisqa xulosa

Bu darsda OOP tamoyillari, Klass va Obyekt tushunchasi hamda birinchi metod va atributlar bilan ishlash o'rganildi.
"""

# 26-DARS
lessons[26] = """# ⚙️ 26. __init__ va self — Dars dokumentatsiyasi

OOP da obyekt yaratilayotgan soniyaning o'zidayoq unga dastlabki xususiyatlarni (atributlarni) yuklash talab etiladi. Buning uchun Python'da maxsus **Konstruktor (Constructor)** metodi — **`__init__`** ishlatiladi.

`__init__` dunder (double underscore) metodi obyekt yaratilishi bilan avtomatik tarzda chaqiriladi.

Ushbu darsda siz `__init__` konstruktori, joriy obyektga ishora qiluvchi **`self`** kalit so'zining ishlash mexanizmi va obyekt hamda klass atributlari o mezonidagi farqni o'rganasiz.

---

## Bu mavzu orqali nimalar qilish mumkin

- Obyekt yaratilishi vaqtidanoq unga dastlabki ma'lumotlarni uzatish;
- `self` yordamida obyektning ichki holatini va atributlarini boshqarish;
- Instance Attributes (Obyekt atributlari) va Class Attributes (Klass atributlari) ni ajratish;
- Obyektlar yaratuvchi qulay va toza konstruktorlar loyihalashtirish.

---

## Dars maqsadi

Bu dars oxirida o'quvchi:

- `__init__` metodi qachon va qanday ishlashini bilish;
- `self` nima uchun har bir metodda birinchi bo'lib yozilishini tushunish;
- Dinamik atributli obyektlar yaratish

ni mustaqil bajara oladi.

---

## Kerakli oldingi bilimlar

- 25-dars: OOP, Class va Object.

---

# 1. Asosiy tushunchalar va atamalar

## __init__ (Konstruktor) nima?

> **`__init__`** — yangi obyekt yaratilganda avtomatik chaqiriluvchi va obyekt atributlariga dastlabki qiymatlarni biriktiruvchi maxsus metod.

## self nima?

> **`self`** — yaratilayotgan yoki chaqirilayotgan joriy obyekt nusxasiga (instance) ishora qiluvchi havola.

## Instance Attribute nima?

> Faqat bitta muayyan obyektga tegishli bo'lgan va `self.attribute_name` orqali e'lon qilinadigan o'zgaruvchi.

---

# 2. Sintaksis va uning izohi

```python
class Foydalanuvchi:
    def __init__(self, ism, email):
        self.ism = ism      # Instance attribute
        self.email = email  # Instance attribute

# Obyekt yaratish
u1 = Foydalanuvchi("Ali", "ali@mail.com")
```

---

# 3. Instance vs Class Attribute Jadvali

| Attribute Turi | Qayerda E'lon Qilinadi? | Xotiradagi Holati | Misol |
|---|---|---|---|
| **Instance Attribute** | `__init__` ichida (`self.x`) | Har bir obyektda alohida | `self.ism = "Ali"` |
| **Class Attribute** | Klass tanasida (metodlardan tashqarida) | Barcha obyektlar uchun bitta va umumiy | `turi = "Inson"` |

---

# 4. Kod misollari

## Misol 1 — __init__ bilan obyekt yaratish

```python
class Talaba:
    def __init__(self, ism, yosh, guruh):
        self.ism = ism
        self.yosh = yosh
        self.guruh = guruh

t1 = Talaba("Ali", 20, "FN-101")
print(f"Talaba: {t1.ism}, Guruh: {t1.guruh}")
```

---

## Misol 2 — Metodlarda self dan foydalanish

```python
class Avto:
    def __init__(self, model, tezlik):
        self.model = model
        self.tezlik = tezlik
    
    def tezlash(self, qiymat):
        self.tezlik += qiymat
        print(f"{self.model} tezligi: {self.tezlik} km/h")

a1 = Avto("Nexia", 80)
a1.tezlash(20) # 100 km/h
```

---

## Misol 3 — Class va Instance Atributlari farqi

```python
class Ishchi:
    kompaniya = "Google" # Class attribute
    
    def __init__(self, ism):
        self.ism = ism # Instance attribute

i1 = Ishchi("Ali")
i2 = Ishchi("Vali")

print(i1.ism, i1.kompaniya) # Ali Google
print(i2.ism, i2.kompaniya) # Vali Google
```

---

# 5. Real loyiha misoli — Bank Hisobi Tizimi (Bank Account)

```python
class BankAccount:
    def __init__(self, egalari_ismi, dastlabki_balans=0):
        self.egasi = egalari_ismi
        self.balans = dastlabki_balans
    
    def depozit(self, summa):
        self.balans += summa
        print(f"+{summa} so'm tushdi. Jami balans: {self.balans} so'm")
    
    def yechish(self, summa):
        if summa <= self.balans:
            self.balans -= summa
            print(f"-{summa} so'm yechildi. Qoldiq: {self.balans} so'm")
        else:
            print("Xato: Mablag' yetarli emas!")

acc = BankAccount("Sardor", 100000)
acc.depozit(50000)
acc.yechish(30000)
```

---

# 6. Ko'p uchraydigan xatolar

## Xato 1: __init__ dan qiymat qaytarishga urinish (`return value`)

Noto'g'ri:
```python
class Xato:
    def __init__(self):
        return "Natija" # TypeError: __init__() should return None!
```

---

# 7. Sinfdagi amaliy topshiriqlar

1. **Oson**: `Shaxs` klassini yarating (`ism`, `yosh`, `manzil` atributlari `__init__` da berilsin).
2. **O'rta**: `To'rtburchak` klassida `eni` va `bo'yi` berilsin. `yuza()` va `perimetr()` metodlari natija qaytarsin.

---

# 8. Uyga vazifa

1. `Mahsulot` klassida nom, narx va chegirma foizi bo'lsin. `get_discounted_price()` metodi chegirmali narxni hisoblasin.

---

# 9. Tekshirish savollari

1. `__init__` metodi qachon ishga tushadi?
2. `self` so'zi o'rniga boshqa so'z ishlatish mumkinmi?

---

## Javoblar

1. Klassdan yangi obyekt yaratilgan (`Obyekt()`) zahoti avtomatik chaqiriladi.
2. Texnik jihatdan mumkin (chunki u sintaktik o'zgaruvchi), lekin Python konvensiyasiga ko'ra har doim `self` deb yozilishi shart.

---

# 10. Qisqa xulosa

Bu darsda obyektlarni initsializatsiya qilish (`__init__`), joriy obyekt murojaati (`self`) va atribut turlari o'rganildi.
"""

for num, content in lessons.items():
    filepath = os.path.join(DOCS_DIR, f"dars_{num:02d}.md")
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"dars_{num:02d}.md yaratildi: {len(content)} belgi")
