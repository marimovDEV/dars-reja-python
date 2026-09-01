# 🔒 27. Inkapsulyatsiya (Encapsulation) — Dars dokumentatsiyasi

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
