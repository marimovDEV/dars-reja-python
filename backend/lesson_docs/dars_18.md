# 🎛️ 18. *args, **kwargs va Scope — Dars dokumentatsiyasi

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
