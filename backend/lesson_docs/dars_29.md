# 🛠️ 29. Class/Static Metodlar va Dunder Metodlar — Dars dokumentatsiyasi

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
