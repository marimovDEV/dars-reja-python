# ⚙️ 17. Funksiyalar — Dars dokumentatsiyasi

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
