# 🛡️ 21. Xatolarni boshqarish (Exceptions) — Dars dokumentatsiyasi

Dastur runs jarayonida kutilmagan xatolar (masalan, nolga bo'lish, mavjud bo'lmagan faylni ochish, noto'g'ri turdagi ma'lumot kiritish) yuz berishi mumkin. Agar bu xatolar ushlanmasa, Python dasturni **avariya holatida (crash)** to'xtatadi.

**Try-Except (Exception Handling)** — bu dasturning kutilmagan xatolar sababli to'xtab qolishining oldini olish va xatolarni nazorat ostida ushlab, foydalanuvchiga tushunarli xabar berish mexanizmidir.

Professional dastur har qanday noto'g'ri kiritilgan ma'lumotda ham qulab tushmasdan, barqaror (robust) ishlashi shart.

---

## Bu mavzu orqali nimalar qilish mumkin

- Dasturdagi xatolarni `try-except` bloklari orqali tutib olish;
- Xato turiga qarab alohida ishlov berish (`ValueError`, `ZeroDivisionError`, `KeyError`);
- `else` va `finally` bloklaridan to'g'ri foydalanish;
- Sun'iy ravishda xato chaqirish (`raise`).

---

## Dars maqsadi

Bu dars oxirida o'quvchi:

- `try`, `except`, `else`, `finally` strukturasini tushunish;
- Dastur barqarorligini ta'minlash va crash bo'lishining oldini olish;
- Maxsus xatolarni `raise` orqali hosil qilish

ni mustaqil bajara oladi.

---

## Kerakli oldingi bilimlar

- 3-dars: Input va arifmetika;
- 5-dars: If/elif/else.

---

# 1. Asosiy tushunchalar va atamalar

## Exception (Istisno/Xato) nima?

> **Exception** — dastur bajarilayotgan vaqtda yuzaga keladigan va uning normal oqimini buzadigan xatolik ob'yekti.

## try-except nima?

> **try** bloki ichiga xato chiqishi mumkin bo'lgan kod yoziladi. **except** bloki esa xato yuz berganda bajariladigan muqobil kodni saqlaydi.

## raise nima?

> Dasturchi tomonidan sun'iy ravishda ma'lum bir xatolikni yuzaga keltirish buyrug'i.

---

# 2. Sintaksis va uning izohi

```python
try:
    # Xato berishi mumkin bo'lgan kod
    son = int(input("Son kiriting: "))
    natija = 10 / son
except ZeroDivisionError:
    print("Nolga bo'lish mumkin emas!")
except ValueError:
    print("Faqat son kiritishingiz kerak!")
else:
    print("Xatosiz bajarildi. Natija:", natija)
finally:
    print("Bu blok har doim ishlaydi (tozalash vaqti).")
```

---

# 3. Eng Ko'p Uchraydigan Xatolar Jadvali

| Xatolik Nomi | Sababi | Misol |
|---|---|---|
| **`ZeroDivisionError`** | Sonni nolga bo'lganda | `10 / 0` |
| **`ValueError`** | Noto'g mezon turdagi qiymat berilganda | `int("salom")` |
| **`TypeError`** | Mos kelmaydigan turlar amali | `"a" + 5` |
| **`IndexError`** | Ro'yxatda yo'q indeksga murojaat | `[1][5]` |
| **`KeyError`** | Lug'atda yo'q kalitga murojaat | `{}[ "key"]` |

---

# 4. Kod misollari

## Misol 1 — Sodda xatoni ushlash

```python
try:
    yosh = int(input("Yoshingizni kiriting: "))
    print(f"Siz {yosh} yoshdasiz.")
except ValueError:
    print("Xato! Iltimos, raqam kiriting.")
```

---

## Misol 2 — Bir nechta except bloklari

```python
try:
    a = int(input("a = "))
    b = int(input("b = "))
    res = a / b
    print("Natija:", res)
except ValueError:
    print("Iltimos, faqat butun son kiriting!")
except ZeroDivisionError:
    print("Nolga bo'lish amali taqiqlangan!")
```

---

## Misol 3 — raise yordamida shaxsiy xato chiqarish

```python
def yoshni_tekshir(yosh):
    if yosh < 0:
        raise ValueError("Yosh manfiy bo'lishi mumkin emas!")
    return f"Yoshingiz: {yosh}"

try:
    print(yoshni_tekshir(-5))
except ValueError as e:
    print("Ushlangan xato:", e)
```

---

# 5. Real loyiha misoli — Xavfsiz Kalkulyator va Input Tekshiruvi

```python
def xavfsiz_bo_lish():
    while True:
        try:
            n1 = float(input("1-son: "))
            n2 = float(input("2-son: "))
            natija = n1 / n2
            return natija
        except ValueError:
            print("Xato: Iltimos, faqat son kiriting!
")
        except ZeroDivisionError:
            print("Xato: Ikkinchi son nol bo'lmasligi kerak!
")

res = xavfsiz_bo_lish()
print("Bo'linma natijasi:", res)
```

---

# 6. Ko'p uchraydigan xatolar

## Xato 1: Quruq `except:` ishlatish (Bare Except)

Noto'g'ri:
```python
try:
    kod()
except: # Barcha xatolar (xatto Ctrl+C ni ham) yutib yuboradi!
    print("Xato bo'ldi")
```

To mezon: Har doim aniq xatolik turini ko'rsating: `except ValueError:`.

---

# 7. Sinfdagi amaliy topshiriqlar

1. **Oson**: List va indeks qabul qilib, `IndexError` ni ushlovchi funksiya yozing.
2. **O'rta**: Lug'atdan kalit bo'yicha qiymat oluvchi, `KeyError` yuz berganda mos xabar chiqaruvchi kod tuzing.

---

# 8. Uyga vazifa

1. Foydalanuvchidan parol kiritishni so'rang. Agar parol 8 ta belgidan kam bo'lsa `raise Exception("Parol juda qisqa")` orqali xato chiqaring va uni `try-except` da ushlang.

---

# 9. Tekshirish savollari

1. `finally` bloki qachon ishlaydi?
2. `else` bloki `try-except` da nima uchun kerak?

---

## Javoblar

1. `finally` bloki xato yuz berishidan yoki berib-bermasligidan qat'iy nazar har doim ishlaydi.
2. `else` bloki faqat `try` bloki ichida HECH QANDAY xato yuz bermaganda bajariladi.

---

# 10. Qisqa xulosa

Bu darsda Python'da xatolarni boshqarish (`try-except-else-finally`), maxsus xatolarni chiqarish va dastur barqarorligini oshirish o'rganildi.
