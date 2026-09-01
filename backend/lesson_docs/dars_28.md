# 🧬 28. Vorislik (Inheritance) va Polimorfizm — Dars dokumentatsiyasi

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
