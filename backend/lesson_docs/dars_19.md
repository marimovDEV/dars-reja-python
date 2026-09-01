# ⚡ 19. Lambda va Rekursiya — Dars dokumentatsiyasi

Python'da funksiyalar nafaqat standart `def` yordamida, balki bir qatorli nomlanmagan **Lambda (Anonim funksiyalar)** ko'rinishida ham e'lon qilinishi mumkin. Lambda funksiyalar asosan qisqa va bir marotabalik mantiqlarni boshqa funksiyalarga (masalan, `map()`, `filter()`, `sort()`) argument sifatida uzatish uchun ishlatiladi.

**Rekursiya (Recursion)** esa funksiyaning o'z-o'zini chaqirish texnikasidir. U murakkab muammolarni (masalan, daraxtsimon strukturalarni aylanib chiqish, faktorial, Fibonachchi ketma-ketligi, fayllar tizimini skanerlash) o'ziga o'xshash kichikroq sub-muammolarga bo'lish uchun xizmat qiladi.

Bu darsda siz anonsiz funksiyalar va rekursiv algoritmlar yaratish hamda ularning to'xtash sharti (`Base Case`) muhimligini o'rganasiz.

---

## Bu mavzu orqali nimalar qilish mumkin

- Bir qatorli anonim `lambda` funksiyalarini yozish;
- `map()`, `filter()`, `sorted()` funksiyalari bilan `lambda` ni birga ishlatish;
- Rekursiv funksiyalar yaratish va Base Case (to'xtash shartini) to'g'ri qo'yish;
- Faktorial, Fibonachchi va ichma-ich ro'yxatlarni rekursiya orqali qayta ishlash.

---

## Dars maqsadi

Bu dars oxirida o'quvchi:

- Lambda funksiyalari sintaksisini bilish va o'z o'rnida ishlatish;
- `map()` va `filter()` mexanizmini tushunish;
- Rekursiya tamoyilini va to'xtash shartini to'g'ri loyihalashtirish

ni mustaqil bajara oladi.

---

## Kerakli oldingi bilimlar

- 17-dars: Funksiyalar;
- 11-dars: List asoslari.

---

# 1. Asosiy tushunchalar va atamalar

## Lambda Funksiya nima?

> **Lambda** — nomi yo'q, bitta ifodadan (expression) iborat va avtomatik qiymat qaytaruvchi anonim funksiya.

## Rekursiya nima?

> **Rekursiya** — funksiyaning o'z tanasi ichida o'zini chaqirishi.

## Base Case (To'xtash Sharti) nima?

> Rekursiv funksiyada cheksiz chaqiruvning oldini oluvchi va rekursiyani to'xtatuvchi eng sodda holat (shart).

---

# 2. Sintaksis va uning izohi

```python
# Lambda Sintaksisi
# lambda parametr1, parametr2: ifoda

kvadrat = lambda x: x ** 2
print(kvadrat(5)) # 25

# Rekursiya Sintaksisi
def rekursiv_func(n):
    if n <= 1: # Base Case
        return 1
    return n * rekursiv_func(n - 1) # Rekursiv qadam
```

---

# 3. Lambda vs Standart Funksiya Jadvali

| Xususiyat | Standart Funksiya (`def`) | Lambda Funksiya (`lambda`) |
|---|---|---|
| Nomlanishi | Har doim nomli | Anonim (nomsiz) |
| Qatorlar soni | Ko'p qatorli | **Faqat 1 qator** |
| `return` so'zi | Aniq yoziladi | **Avtomatik qaytaradi** |
| Ishlatilishi | Murakkab mantiq uchun | Qisqa callback'lar uchun |

---

# 4. Kod misollari

## Misol 1 — Lambda bilan listni saralash (sorted)

```python
talabalar = [("Ali", 85), ("Vali", 92), ("Sardor", 78)]
# Bahosi bo'yicha saralash
saralangan = sorted(talabalar, key=lambda x: x[1], reverse=True)

print(saralangan)
```

Natija:
```
[('Vali', 92), ('Ali', 85), ('Sardor', 78)]
```

---

## Misol 2 — map() va filter() bilan Lambda

```python
sonlar = [1, 2, 3, 4, 5, 6]

# Juft sonlarni filtrlash
juftlar = list(filter(lambda x: x % 2 == 0, sonlar))

# Har birini kvadratga oshirish
kvadratlar = list(map(lambda x: x ** 2, sonlar))

print("Juftlar:", juftlar)
print("Kvadratlar:", kvadratlar)
```

---

## Misol 3 — Rekursiv Faktorial

```python
def faktorial(n):
    if n == 1 or n == 0: # Base case
        return 1
    return n * faktorial(n - 1)

print("5! =", faktorial(5)) # 120
```

---

## Misol 4 — Rekursiv Fibonachchi

```python
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

print("6-Fibonachchi soni:", fibonacci(6)) # 8
```

---

# 5. Real loyiha misoli — Katalog/Papka hajmini rekursiv hisoblash

```python
fayllar_tizimi = {
    "nom": "root",
    "fayllar": [{"nom": "a.txt", "hajm": 100}, {"nom": "b.txt", "hajm": 200}],
    "papkalar": [
        {
            "nom": "docs",
            "fayllar": [{"nom": "c.pdf", "hajm": 500}],
            "papkalar": []
        }
    ]
}

def jami_hajm(tizim):
    h = sum(f["hajm"] for f in tizim["fayllar"])
    for p in tizim["papkalar"]:
        h += jami_hajm(p) # Rekursiv chaqiruv
    return h

print("Jami fayllar hajmi:", jami_hajm(fayllar_tizimi), "KB")
```

---

# 6. Ko'p uchraydigan xatolar

## Xato 1: Rekursiyada Base Case yozishni unutish

Noto'g'ri:
```python
def cheksiz(n):
    return cheksiz(n - 1) # RecursionError: maximum recursion depth exceeded
```

---

# 7. Sinfdagi amaliy topshiriqlar

1. **Oson**: Berilgan sonning musbat yoki manfiyligini aniqlovchi `lambda` yozing.
2. **O'rta**: Rekursiv ravishda 1 dan N gacha bo'lgan sonlar yig'indisini hisoblovchi funksiya tuzing.

---

# 8. Uyga vazifa

1. Berilgan murakkab ichma-ich ro'yxatni (masalan `[1, [2, [3, 4]], 5]`) bitta tekis ro'yxatga (`[1, 2, 3, 4, 5]`) aylantiruvchi rekursiv funksiya yozing.

---

# 9. Tekshirish savollari

1. `map()` funksiyasining vazifasi nima?
2. `RecursionError` qachon yuzaga keladi?

---

## Javoblar

1. Ketma-ketlikdagi har bir elementga berilgan funksiyani qo'llab yangi iterator qaytaradi.
2. Rekursiv funksiya to'xtash shartisiz o'zini juda ko'p marta (standart bo'yicha 1000 marta) chaqirganda.

---

# 10. Qisqa xulosa

Bu darsda bir qatorli anonim lambda funksiyalari hamda o'z-o'zini chaqiruvchi rekursiv algoritmlar o'rganildi.
