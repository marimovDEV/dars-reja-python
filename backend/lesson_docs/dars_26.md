# ⚙️ 26. __init__ va self — Dars dokumentatsiyasi

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
