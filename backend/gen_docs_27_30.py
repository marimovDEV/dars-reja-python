#!/usr/bin/env python3
"""Generate lesson docs 27-30 (OOP module continuation)."""
import os

DOCS_DIR = os.path.join(os.path.dirname(__file__), "lesson_docs")

lessons = {}

# 27-DARS
lessons[27] = """# 🔒 27. Inkapsulyatsiya (Encapsulation) — Dars dokumentatsiyasi

**Inkapsulyatsiya (Encapsulation)** — OOP ning 4 ta asosiy ustunidan biri bo'lib, u obyektning ichki ma'lumotlarini (atributlarini) va metodlarini tashqi noqonuniy yoki kutilmagan o'zgarishlardan **himoya qilish** (yashirish) konseptsiyasidir.

Real hayotda bank kartangizning PIN kodi yoki balansi barcha uchun ochiq bo'lmaganidek, dasturdagi muhim obyekt ma'lumotlari ham to'g'ridan-to'g'ri tashqaridan o'zgartirilmasligi kerak.

Python'da Inkapsulyatsiya kirish huquqlari bo'yicha 3 darajaga bo'linadi: **Public (Ochiq)**, **Protected (Himoyalangan)** va **Private (Maxfiy)**. Maxfiy atributlarga xavfsiz murojaat qilish uchun esa **Getter va Setter** metodlaridan foydalaniladi.

---

## Bu mavzu orqali nimalar qilish mumkin

- Obyekt ma'lumotlarini tashqi tasodifiy o'zgarishlardan himoya qilish;
- Public, Protected (`_`) va Private (`__`) atributlar yaratish;
- Getter va Setter metodlari orqali atributlarni tekshirib (validation) yangilash;
- `@property` dekoratori yordamida atribut sifatiga ishlov berish.

---

## Dars maqsadi

Bu dars oxirida o'quvchi:

- Inkapsulyatsiya ma'nosi va zaruratini tushunish;
- `_protected` va `__private` sintaksisini qo'llash;
- Accessor (Getter) va Mutator (Setter) metodlarini yozish;
- `@property` dekoratorini amalda qo'llash

ni mustaqil bajara oladi.

---

## Kerakli oldingi bilimlar

- 25-dars: OOP, Class va Object;
- 26-dars: __init__ va self.

---

# 1. Asosiy tushunchalar va atamalar

## Encapsulation (Inkapsulyatsiya) nima?

> **Inkapsulyatsiya** — ma'lumotlar va metodlarni bir kapsulaga (klassga) biriktirish va ichki holatni tashqaridan yashirish.

## Public, Protected va Private nima?

> **Public**: Barcha joydan murojaat qilsa bo'ladi (`self.name`).
> **Protected**: Faqat shu klass va uning vorislarida ishlatilishi tavsiya etiladi (`self._age`).
> **Private**: Faqat shu klass ichida ko'rinadi, tashqaridan to'g'ridan-to'g'ri murojaat qilib bo'lmaydi (`self.__salary`).

## Getter va Setter nima?

> **Getter** — private atribut qiymatini o'qish uchun metod. **Setter** — private atribut qiymatini tekshirib (validatsiya qilib) o'zgartirish uchun metod.

---

# 2. Sintaksis va uning izohi

```python
class Shaxs:
    def __init__(self, ism, maosh):
        self.ism = ism          # Public
        self._yosh = 25         # Protected
        self.__maosh = maosh    # Private

# Getter va Setter
    def get_maosh(self):
        return self.__maosh
    
    def set_maosh(self, yangi_maosh):
        if yangi_maosh > 0:
            self.__maosh = yangi_maosh
```

---

# 3. Kirish Huquqlari Darajasi Jadvali

| Daraja | Sintaksis | Klass Ichida | Voris Klassda | Tashqarida |
|---|---|---|---|---|
| **Public** | `self.x` | Ha | Ha | Ha |
| **Protected** | `self._x` | Ha | Ha | Ha (Lekin tavsiya etilmaydi) |
| **Private** | `self.__x` | Ha | **Yo'q** | **Yo'q (Name Mangling o'tadi)** |

---

# 4. Kod misollari

## Misol 1 — Private atribut va Name Mangling

```python
class Bank:
    def __init__(self, balans):
        self.__balans = balans

b = Bank(1000)
# print(b.__balans) -> AttributeError!
# Lekin Python ichida _Bank__balans nomi bilan saqlanadi (Name Mangling)
print(b._Bank__balans) # 1000
```

---

## Misol 2 — Getter va Setter bilan ishlash

```python
class Inson:
    def __init__(self, yosh):
        self.__yosh = yosh

    def get_yosh(self):
        return self.__yosh

    def set_yosh(self, yangi_yosh):
        if yangi_yosh > 0 and yangi_yosh < 150:
            self.__yosh = yangi_yosh
        else:
            print("Xato yosh kiritildi!")

i = Inson(20)
i.set_yosh(-5) # Xato yosh kiritildi!
print("Yosh:", i.get_yosh()) # 20
```

---

## Misol 3 — `@property` Dekoratori bilan ishlash (Pythonic Usul)

```python
class Mahsulot:
    def __init__(self, narx):
        self.__narx = narx

    @property
    def narx(self):
        return self.__narx

    @narx.setter
    def narx(self, qiymat):
        if qiymat >= 0:
            self.__narx = qiymat
        else:
            print("Narx manfiy bo'lolmaydi!")

m = Mahsulot(500)
m.narx = 600 # Setter ishlaydi
print(m.narx) # Getter ishlaydi
```

---

# 5. Real loyiha misoli — Foydalanuvchi Paroli va Xavfsizlik

```python
class User:
    def __init__(self, username, password):
        self.username = username
        self.__password_hash = self.__hash_password(password)

    def __hash_password(self, password):
        return f"hash_{password}_123" # Simulyatsiya

    def check_password(self, password):
        return self.__password_hash == self.__hash_password(password)

u = User("ali", "secret123")
print("Parol to'g'rimi?:", u.check_password("secret123")) # True
print("Parol to'g'rimi?:", u.check_password("123"))       # False
```

---

# 6. Ko'p uchraydigan xatolar

## Xato 1: Private atributga tashqaridan to'g'ridan-to mezon murojaat qilish

Noto'g'ri:
```python
obj.__private_var # AttributeError!
```

---

# 7. Sinfdagi amaliy topshiriqlar

1. **Oson**: `__pin` degan private atributi bor `Karta` klassini yarating va uni ko'rish hamda o'zgartirish uchun getter/setter yozing.

---

# 8. Uyga vazifa

1. `Avtomobil` klassida `__probeg` atributini saqlang. Probegni faqat oshirish mumkin bo'lsin, kamaytirishga urinilganda xabar chiqarsin.

---

# 9. Tekshirish savollari

1. Single underscore (`_`) va double underscore (`__`) farqi nimada?
2. `@property` dekoratorining afzalligi nimada?

---

## Javoblar

1. `_` bu shunchaki ishlab chiquvchilar kelishuvi (protected), `__` esa Name Mangling mexanizmini yoqib atribut nomini o'zgartiradi (private).
2. Metodlarni atribut sifatiga chaqirish imkonini beradi (`obj.narx` ko'rinishida getter va setter ishlaydi).

---

# 10. Qisqa xulosa

Bu darsda Inkapsulyatsiya konseptsiyasi, Public/Protected/Private darajalari va Getter-Setter mexanizmi o'rganildi.
"""

# 28-DARS
lessons[28] = """# 🧬 28. Vorislik (Inheritance) va Polimorfizm — Dars dokumentatsiyasi

**Vorislik (Inheritance)** va **Polimorfizm (Polymorphism)** — OOP ning eng muhim va qudratli tamoyillaridandir.

Vorislik — bu mavjud klass (Ota/Parent Class) asosida yangi klass (Bola/Child Class) yaratish va ota klassning barcha atribut hamda metodlarini qayta yozmasdan meros qilib olish imkoniyatidir. Bu kod takrorlanishini keskin kamaytiradi.

Polimorfizm — bir xil nomdagi metodlarning har xil klasslarda turlicha harakat qilishi va har bir klass o'ziga mos ravishda metodni qayta belgilashi (**Method Overriding**) imkoniyatidir.

---

## Bu mavzu orqali nimalar qilish mumkin

- Ota klass (Base/Parent) va Bola klass (Derived/Child) lar iyerarxiyasini tuzish;
- `super()` yordamida ota klass konstruktori va metodlarini chaqirish;
- Metodlarni qayta ta'riflash (Method Overriding);
- Ko'p shakllilik (Polimorfizm) yordamida universal interfeyslar yaratish.

---

## Dars maqsadi

Bu dars oxirida o'quvchi:

- Vorislik iyerarxiyasini to'g'ri loyihalashtirish;
- `super().__init__()` dan foydalana olish;
- Method Overriding mexanizmini tushunish va Polimorfizm tamoyilini qo'llash

ni mustaqil bajara oladi.

---

## Kerakli oldingi bilimlar

- 25-dars: OOP asoslari;
- 26-dars: __init__ va self.

---

# 1. Asosiy tushunchalar va atamalar

## Inheritance (Vorislik) nima?

> **Vorislik** — bola klassning ota klass xususiyat va metodlarini meros qilib olishi.

## Polimorfizm nima?

> **Polimorfizm** (yunoncha "ko'p shakllilik") — bir xil nomli metodning turli ob'yektlarda har xil natija berishi.

## Method Overriding (Metod qayta belgilash) nima?

> Bola klassda ota klassdan kelgan metodni o'z ehtiyojiga moslab qayta yozib chiqish jarayoni.

---

# 2. Sintaksis va uning izohi

```python
# Ota Klass
class Hayvon:
    def ovoz(self):
        print("Boshqacha ovoz")

# Bola Klass
class Kuchuk(Hayvon):
    def ovoz(self): # Method Overriding
        print("Vov-vov!")
```

---

# 3. Vorislik Turlari Jadvali

| Tur | Tavsifi | Sintaksis Misoli |
|---|---|---|
| **Single Inheritance** | Bitta otadan bitta bola | `class B(A):` |
| **Multiple Inheritance** | Bir nechta otadan bitta bola | `class C(A, B):` |
| **Multilevel Inheritance** | Zanjirsimon vorislik | `class C(B):` (B esa A dan) |

---

# 4. Kod misollari

## Misol 1 — Oddiy Vorislik va super()

```python
class Shaxs:
    def __init__(self, ism, yosh):
        self.ism = ism
        self.yosh = yosh

class Talaba(Shaxs):
    def __init__(self, ism, yosh, guruh):
        super().__init__(ism, yosh) # Ota konstruktorini chaqirish
        self.guruh = guruh

t = Talaba("Ali", 20, "IT-01")
print(t.ism, t.guruh)
```

---

## Misol 2 — Polimorfizm (Metod Overriding)

```python
class Shakl:
    def yuza(self):
        return 0

class Doira(Shakl):
    def __init__(self, r):
        self.r = r
    def yuza(self):
        return 3.14 * self.r ** 2

class Kvadrat(Shakl):
    def __init__(self, a):
        self.a = a
    def yuza(self):
        return self.a ** 2

shakllar = [Doira(5), Kvadrat(4)]
for s in shakllar:
    print("Yuza:", s.yuza()) # Polimorfizm!
```

---

# 5. Real loyiha misoli — Xodimlar Tizimi (HR System)

```python
class Employee:
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary
    
    def calculate_salary(self):
        return self.base_salary

class Developer(Employee):
    def __init__(self, name, base_salary, bonus):
        super().__init__(name, base_salary)
        self.bonus = bonus
        
    def calculate_salary(self):
        return self.base_salary + self.bonus

dev = Developer("Ali", 1000, 500)
print(f"{dev.name} Maoshi:", dev.calculate_salary()) # 1500
```

---

# 6. Ko'p uchraydigan xatolar

## Xato 1: `super().__init__()` ni chaqirishni unutish

Bola klassda `__init__` override qilinganda `super()` chaqirilmasa, ota klass atributlari yo'qolib qoladi!

---

# 7. Sinfdagi amaliy topshiriqlar

1. **Oson**: `Transport` ota klassi va undan voris oluvchi `Avtobus` hamda `YengilMashina` klasslarini tuzing.

---

# 8. Uyga vazifa

1. `Tolov` ota klassi va `KartaTolov`, `NaqdTolov` bola klasslarini yarating. Har birida `tolang(summa)` metodini polimorfik tarzda qayta belgilang.

---

# 9. Tekshirish savollari

1. `super()` kalit so'zi nima uchun kerak?
2. Polimorfizm dasturchiga qanday qulaylik beradi?

---

## Javoblar

1. Ota klassning atribut va metodlariga bola klass ichidan murojaat qilish va chaqirish uchun.
2. Har xil turdagi obyektlar bilan bir xil interfeys (metod nomi) orqali ishlash imkonini beradi.

---

# 10. Qisqa xulosa

Bu darsda Vorislik (Inheritance), `super()` va Polimorfizm (Method Overriding) tamoyillari o'rganildi.
"""

# 29-DARS
lessons[29] = """# 🛠️ 29. Class/Static Metodlar va Dunder Metodlar — Dars dokumentatsiyasi

Python klasslarida oddiy metodlardan (Instance Methods) tashqari, klassning o'ziga bog'liq bo'lgan **Class Method (`@classmethod`)** hamda umumiy yordamchi vazifalarni bajaruvchi **Static Method (`@staticmethod`)** lar ham mavjud.

Shuningdek, Python'da **Dunder (Double Underscore - Magic Methods)** deb ataluvchi maxsus metodlar bor. Ular ko'rinishidan `__name__` shaklida bo'lib, klass obyektlariga operatorlar (`+`, `-`, `==`) va ichki funksiyalar (`len()`, `print()`, `str()`) qo'llanilganda qanday harakat qilishini belgilaydi.

---

## Bu mavzu orqali nimalar qilish mumkin

- `@classmethod` yordamida klass holatini o'zgartiruvchi yoki muqobil konstruktorlar yaratish;
- `@staticmethod` yordamida mantiqan klassga tegishli, lekin obyekt va klass holatiga bog'liq bo'lmagan funksiyalar yozish;
- Magic Methods (`__str__`, `__repr__`, `__len__`, `__add__`, `__eq__`) yordamida obyektlarni formatlash va ularga operatorlarni tatbiq etish.

---

## Dars maqsadi

Bu dars oxirida o'quvchi:

- Instance, Class va Static metodlar farqini tushunish;
- `@classmethod` va `@staticmethod` dekoratorlarini to'g'ri qo'llash;
- Dunder metodlar yordamida obyektlarni Python built-in funksiyalari bilan moslashtirish

ni mustaqil bajara oladi.

---

## Kerakli oldingi bilimlar

- 25-dars: OOP asoslari;
- 26-dars: __init__ va self.

---

# 1. Asosiy tushunchalar va atamalar

## Class Method (`@classmethod`) nima?

> Birinchi parametri sifatida obyektni emas (`self`), klassning o'zini (`cls`) qabul qiluvchi va klass darajasidagi ma'lumotlar bilan ishlovchi metod.

## Static Method (`@staticmethod`) nima?

> Nima `self`, nima `cls` ni qabul qilmaydigan, oddiy mustaqil funksiya kabi ishlaydigan, lekin mantiqan klass ichiga joylashtirilgan metod.

## Dunder (Magic) Methods nima?

> Ikki pastki chiziq bilan boshlanuvchi va tugovchi maxsus metodlar (`__str__`, `__len__`, `__add__` h.k.).

---

# 2. Metod Turlari Solishtirma Jadvali

| Metod Turi | Dekorator | Birinchi Parametr | Qo'llanilishi |
|---|---|---|---|
| **Instance Method** | Yo'q | `self` | Obyekt holati va atributlari bilan ishlash |
| **Class Method** | `@classmethod` | `cls` | Klass atributlari va Muqobil Konstruktorlar |
| **Static Method** | `@staticmethod` | Yo'q | Mustaqil utility/yordamchi funksiyalar |

---

# 3. Kod misollari

## Misol 1 — Classmethod va Staticmethod

```python
class Sana:
    def __init__(self, yil, oy, kun):
        self.yil = yil
        self.oy = oy
        self.kun = kun

    @classmethod
    def stringdan_yarat(cls, sana_str): # Muqobil konstruktor
        yil, oy, kun = map(int, sana_str.split("-"))
        return cls(yil, oy, kun)

    @staticmethod
    def kabisa_yili(yil):
        return yil % 4 == 0 and (yil % 100 != 0 or yil % 400 == 0)

s = Sana.stringdan_yarat("2024-09-01")
print(s.yil, s.oy, s.kun)
print("2024 kabisami?:", Sana.kabisa_yili(2024))
```

---

## Misol 2 — Magic Methods (`__str__` va `__len__`)

```python
class Kitob:
    def __init__(self, nom, sahifa):
        self.nom = nom
        self.sahifa = sahifa

    def __str__(self): # print(obj) qilinganda chiqadi
        return f"Kitob: '{self.nom}' ({self.sahifa} sahifa)"

    def __len__(self): # len(obj) qilinganda chiqadi
        return self.sahifa

k = Kitob("Python Asoslari", 350)
print(k)      # Kitob: 'Python Asoslari' (350 sahifa)
print(len(k)) # 350
```

---

## Misol 3 — Operator Overloading (`__add__` va `__eq__`)

```python
class Puli:
    def __init__(self, qiymat):
        self.qiymat = qiymat

    def __add__(self, boshqa): # + operatori
        return Puli(self.qiymat + boshqa.qiymat)

    def __eq__(self, boshqa): # == operatori
        return self.qiymat == boshqa.qiymat

p1 = Puli(5000)
p2 = Puli(3000)
p3 = p1 + p2

print("Jami puli:", p3.qiymat) # 8000
print("Tengmi?:", p1 == p2)   # False
```

---

# 7. Sinfdagi amaliy topshiriqlar

1. **Oson**: `__str__` va `__len__` metodlariga ega `Savat` klassini yarating.

---

# 10. Qisqa xulosa

Bu darsda Class/Static metodlar va Magic Methods (Dunder methods) imkoniyatlari o'rganildi.
"""

# 30-DARS
lessons[30] = """# 🏆 30. OOP Mini-Loyiha — Dars dokumentatsiyasi

Ushbu dars OOP modulidagi barcha bilimlarni (Class, Object, `__init__`, Inkapsulyatsiya, Vorislik, Polimorfizm, Magic Methods) amaliyotda birlashtiruvchi **Mini-Loyiha: Bank Boshqaruvi va Foydalanuvchilar Tizimi**ga bag'ishlanadi.

Loyiha arxitekturasi bir-biri bilan bog'langan klasslardan tashkil topadi.

---

## Loyiha Arxitekturasi

1. **`User` (Ota Klass)**: Barcha foydalanuvchilar uchun umumiy (ism, email).
2. **`Customer` (Bola Klass)**: Bank mijozlari, shaxsiy bank hisobiga (`BankAccount`) ega.
3. **`BankAccount`**: Balansni inkapsulyatsiya qiladi (Private `__balance`), depozit va pul yechish amallari.
4. **`BankSystem`**: Barcha mijozlar va hisoblarni boshqaruvchi asosiy tizim.

---

# Kod Implementatsiyasi

```python
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.__balance = balance # Private

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return True
        return False

    def __str__(self):
        return f"Hisob [{self.account_number}]: Balans = ${self.__balance}"

class Customer(User):
    def __init__(self, name, email, account_number, initial_balance=0):
        super().__init__(name, email)
        self.account = BankAccount(account_number, initial_balance)

    def __str__(self):
        return f"Mijoz: {self.name} | {self.account}"

# Test qilish
c1 = Customer("Ali Valiyev", "ali@mail.com", "ACC1001", 500)
c1.account.deposit(200)
c1.account.withdraw(100)

print(c1)
print("Haqiqiy balans:", c1.account.get_balance())
```

---

# 10. Qisqa xulosa

Ushbu mini-loyiha orqali OOP ning barcha 4 ustuni va amaliy qo'llanilishi to'liq mustahkamlandi.
"""

for num, content in lessons.items():
    filepath = os.path.join(DOCS_DIR, f"dars_{num:02d}.md")
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"dars_{num:02d}.md yaratildi: {len(content)} belgi")
