# 🏛️ 25. OOP, Class va Object — Dars dokumentatsiyasi

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
