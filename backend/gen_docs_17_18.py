#!/usr/bin/env python3
"""Generate lesson docs 17-18 with full 19-section documentation template."""
import os

DOCS_DIR = os.path.join(os.path.dirname(__file__), "lesson_docs")

lessons = {}

# 17-DARS
lessons[17] = """# ⚙️ 17. Funksiyalar — Dars dokumentatsiyasi

Dasturlashda bitta kod blokini turli joylarda qayta-qayta yozish **DRY (Don't Repeat Yourself - O'zingni takrorlama)** tamoyiliga zid keladi va loyihani qo'llab-quvvatlashni qiyinlashtiradi. 

**Funksiya (Function)** — bu muayyan bir vazifani bajarish uchun mo'ljallangan va qayta ishlatilishi mumkin bo'lgan kod blokidir. Funksiyalar kodni modullarga bo'lish, o'qilishini yaxshilash va kod qayta ishlatilishini ta'minlash uchun xizmat qiladi.

Python'da funksiyalar `def` kalit so'zi yordamida yaratiladi. Ular parametrlar qabul qilishi hamda `return` operatori orqali natija qaytarishi mumkin.

---

## Bu mavzu orqali nimalar qilish mumkin

- Kod takrorlanishining oldini olish va mantiqiy bloklarga ajratish;
- Parametr va argumentlar bilan ishlash;
- Standard (Default) parametr qiymatlarini belgilash;
- `return` yordamida hisoblangan natijani qaytarish va undan foydalanish;
- Dokstring (`docstring`) yordamida funksiyalarga hujjatlashtirish yozish.

---

## Dars maqsadi

Bu dars oxirida o'quvchi:

- `def` bilan funksiya e'lon qilish va chaqirish (`call`);
- Parametr va argumentlar farqini ajratish;
- `return` operatorining ishlash mexanizmini tushunish;
- Default qiymatga ega parametrlarni to'g'ri qo'llash

ni mustaqil bajara oladi.

---

## Kerakli oldingi bilimlar

- 5-dars: If/elif/else;
- 7-dars: For sikli.

---

# 1. Asosiy tushunchalar va atamalar

## Funksiya (Function) nima?

> **Funksiya** — nomi va o'zining mantiqiy blokiga ega bo'lgan, chaqirilgandagina ishlaydigan kod bo'lagi.

## Parameter (Parametr) va Argument nima?

> **Parametr** — funksiya e'lon qilinayotganda qavs ichida yoziladigan o'zgaruvchi. **Argument** — funksiya chaqirilayotganda unga uzatiladigan haqiqiy qiymat.

## return operatori nima?

> **return** — funksiya ishini tugatib, uning natijasini tashqariga qaytaruvchi kalit so'z.

---

# 2. Sintaksis va uning izohi

```python
def funksiya_nomi(parametr1, parametr2="standart"):
    # bajariladigan kod
    natija = parametr1 + 10
    return natija

# Funksiyani chaqirish
javob = funksiya_nomi(5)
```

---

# 3. Parametr Turlari Jadvali

| Tur | Tavsifi | Sintaksis Misoli |
|---|---|---|
| **Positional Argument** | Ketma-ketlik bo'yicha uzatiladi | `hisobla(10, 20)` |
| **Keyword Argument** | Kalit so'zi ko'rsatib uzatiladi | `hisobla(b=20, a=10)` |
| **Default Parameter** | Qiymat berilmasa standartini oladi | `def f(a=5):` |

---

# 4. Kod misollari

## Misol 1 — Eng sodda funksiya

```python
def salom_ber():
    print("Salom! Python kursiga xush kelibsiz.")

salom_ber()
```

---

## Misol 2 — Parametrli va return ga ega funksiya

```python
def yigindi(a, b):
    return a + b

result = yigindi(15, 25)
print("Yig'indi:", result)
```

---

## Misol 3 — Default parametrli funksiya

```python
def foydalanuvchi_yarat(ism, rol="User"):
    print(f"Foydalanuvchi: {ism}, Rol: {rol}")

foydalanuvchi_yarat("Ali")
foydalanuvchi_yarat("Admin", rol="SuperAdmin")
```

---

## Misol 4 — Bir nechta qiymat qaytarish (Tuples)

```python
def hisobla(a, b):
    yig = a + b
    kop = a * b
    return yig, kop # Tuple qaytaradi

y, k = hisobla(4, 5)
print(f"Yig'indi: {y}, Ko'paytma: {k}")
```

---

# 5. Real loyiha misoli — Valyuta Konvertori va Soliq Hisoblagich

```python
def soliq_hisobla(brutto_maosh, soliq_stavkasi=12):
    soliq = brutto_maosh * (soliq_stavkasi / 100)
    netto = brutto_maosh - soliq
    return netto, soliq

maosh = 10000000
netto_maosh, ushlangan_soliq = soliq_hisobla(maosh)

print(f"Qo'lga tegadigan maosh: {netto_maosh:,.0f} so'm")
print(f"To'langan soliq (12%): {ushlangan_soliq:,.0f} so'm")
```

---

# 6. Ko'p uchraydigan xatolar

## Xato 1: Default parametrni majburiy parametrdan oldin qo'yish

Noto'g'ri:
```python
def xato(a=10, b): # SyntaxError!
    pass
```

To'g'ri:
```python
def togri(b, a=10):
    pass
```

---

# 7. Sinfdagi amaliy topshiriqlar

1. **Oson**: Sonning juft yoki toq ekanligini aniqlab `True` yoki `False` qaytaruvchi `is_even(n)` funksiyasini yozing.
2. **O'rta**: Matnni qabul qilib, undagi unli harflar sonini qaytaruvchi funksiya yarating.

---

# 8. Uyga vazifa

1. Berilgan listdagi faqat tub sonlarni saralab yangi ro'yxat qaytaruvchi `get_prime_numbers(numbers)` funksiyasini yozing.

---

# 9. Tekshirish savollari

1. `print()` va `return` ning asosiy farqi nimada?
2. `docstring` nima uchun kerak?

---

## Javoblar

1. `print()` faqat konsolga chiqaradi, `return` esa qiymatni dasturning keyingi qismlarida ishlatish uchun qaytaradi.
2. Funksiyaning vazifasi, parametrlari va qaytaradigan qiymatini tushuntiruvchi hujjat sifatidagi izoh.

---

# 10. Qisqa xulosa

Bu darsda funksiya tushunchasi, parametrlarni uzatish, `return` mexanizmi va toza kod yozish qoidalari o'rganildi.
"""

# 18-DARS
lessons[18] = """# 🎛️ 18. *args, **kwargs va Scope — Dars dokumentatsiyasi

Ba'zan funksiyaga nechta argument uzatilishi oldindan noma'lum bo'lishi mumkin. Masalan, sonlarning yig'indisini hisoblovchi funksiyaga 2 ta, 5 ta yoki 100 ta son berilishi mumkin. 

Ushbu muammoni hal qilish uchun Python'da `*args` (Positional Arguments) va `**kwargs` (Keyword Arguments) operatorlari ishlatiladi.

Shuningdek, o'zgaruvchilarning ko'rinish sohasi — **Scope (LEGB qoidasi)** mavzusi o'rganiladi. O'zgaruvchi funksiya ichida yaratilganmi yoki tashqarisidami — u qayerda va qachon mavjud bo mezonini belgilaydi.

---

## Bu mavzu orqali nimalar qilish mumkin

- Cheksiz miqdordagi argumentlarni qabul qiluvchi moslashuvchan funksiyalar yozish;
- Kalitli va kalitsiz dinamik argumentlar bilan ishlash;
- LEGB (Local, Enclosing, Global, Built-in) o'zgaruvchilar ko'rinish sohasini tushunish;
- `global` va `nonlocal` kalit so'zlaridan to'g'ri foydalanish.

---

## Dars maqsadi

Bu dars oxirida o'quvchi:

- `*args` (tuple sifatiga keladi) va `**kwargs` (dict sifatiga keladi) ni qo'llash;
- Dinamik argumentli funksiyalar yaratish;
- Local va Global o'zgaruvchilar farqini tushunish va xatolarning oldini olish

ni mustaqil bajara oladi.

---

## Kerakli oldingi bilimlar

- 13-dars: Tuple va Set;
- 14-dars: Dictionary;
- 17-dars: Funksiyalar.

---

# 1. Asosiy tushunchalar va atamalar

## *args nima?

> **`*args`** — funksiyaga istalgancha kalitsiz (positional) argumentlar uzatish imkonini beruvchi belgi. Funksiya ichida u **Tuple** ko'rinishida bo'ladi.

## **kwargs nima?

> **`**kwargs`** — funksiyaga istalgancha kalitli (keyword) argumentlar uzatish imkonini beradi. Funksiya ichida u **Dictionary** ko'rinishida bo'ladi.

## LEGB Qoidasi nima?

> Python'da o mezon va o'zgaruvchini qidirish ketma-ketligi: **L**ocal -> **E**nclosing -> **G**lobal -> **B**uilt-in.

---

# 2. Sintaksis va uning izohi

```python
def universal_func(*args, **kwargs):
    print("Positional (Tuple):", args)
    print("Keyword (Dict):", kwargs)

universal_func(1, 2, 3, ism="Ali", yosh=20)
```

---

# 3. Argument va Scope Turlari Jadvali

| Tushuncha | Turi / Shakli | Vazifasi |
|---|---|---|
| `*args` | Tuple | Cheksiz pozitsion argumentlar |
| `**kwargs` | Dictionary | Cheksiz kalitli argumentlar |
| `Local Scope` | Funksiya ichida | Faqat funksiya ichida ko'rinadi |
| `Global Scope` | Asosiy kodda | Barcha joyda o'qish mumkin |

---

# 4. Kod misollari

## Misol 1 — *args yordamida yig'indi hisoblash

```python
def jami_summa(*sonlar):
    return sum(sonlar)

print(jami_summa(10, 20))         # 30
print(jami_summa(5, 10, 15, 20))  # 50
```

---

## Misol 2 — **kwargs yordamida profil yaratish

```python
def profil_yarat(**ma_lumotlar):
    for k, v in ma_lumotlar.items():
        print(f"{k.capitalize()}: {v}")

profil_yarat(ism="Vali", yosh=22, kasb="Dasturchi")
```

---

## Misol 3 — Global va Local Scope ta'siri

```python
x = 100 # Global

def test():
    x = 10 # Local (Yangi x yaratildi)
    print("Local x:", x)

test()
print("Global x:", x)
```

Natija:
```
Local x: 10
Global x: 100
```

---

## Misol 4 — global kalit so'zidan foydalanish

```python
hisoblagich = 0

def oshir():
    global hisoblagich
    hisoblagich += 1

oshir()
oshir()
print("Hisoblagich:", hisoblagich) # 2
```

---

# 5. Real loyiha misoli — Universal Logger / Event Handler

```python
def log_event(event_name, *tags, **metadata):
    print(f"=== EVENT: {event_name} ===")
    print(f"Teglar: {', '.join(tags)}")
    print("Qo'shimcha Ma'lumotlar:")
    for k, v in metadata.items():
        print(f"  - {k}: {v}")

log_event("USER_LOGIN", "auth", "security", user_id=402, ip="192.168.1.1")
```

---

# 6. Ko'p uchraydigan xatolar

## Xato 1: Argumentlar ketma-ketligini buzish

Noto'g'ri:
```python
def xato(*args, oddiy_var): # SyntaxError!
    pass
```

To'g'ri tartib: `(oddiy_var, *args, **kwargs)`

---

# 7. Sinfdagi amaliy topshiriqlar

1. **Oson**: Istalgancha kiritilgan sonlarning o'rtacha qiymatini hisoblovchi `avg(*args)` funksiyasini yozing.
2. **O'rta**: `**kwargs` orqali berilgan mahsulotlar va ularning narxlaridan eng qimmatini topuvchi funksiya yozing.

---

# 8. Uyga vazifa

1. Shaxsiy ma'lumotlarni (`*args` orqali qobiliyatlarni, `**kwargs` orqali kontatklarni) qabul qilib chiroyli rezyume ko'rinishida chiqaruvchi funksiya yozing.

---

# 9. Tekshirish savollari

1. `*args` funksiya ichida qaysi turda saqlanadi?
2. `LEGB` qoidasining kengaytmasi nima?

---

## Javoblar

1. `Tuple` turida.
2. **L**ocal, **E**nclosing, **G**lobal, **B**uilt-in.

---

# 10. Qisqa xulosa

Bu darsda Python'da dinamik va moslashuvchan argumentlar (`*args`, `**kwargs`) hamda o'zgaruvchilarning ko'rinish sohalari (LEGB) o'rganildi.
"""

for num, content in lessons.items():
    filepath = os.path.join(DOCS_DIR, f"dars_{num:02d}.md")
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"dars_{num:02d}.md yaratildi: {len(content)} belgi")
