#!/usr/bin/env python3
"""Generate lesson docs 19-24 with full 19-section documentation template."""
import os

DOCS_DIR = os.path.join(os.path.dirname(__file__), "lesson_docs")

lessons = {}

# 19-DARS
lessons[19] = """# ⚡ 19. Lambda va Rekursiya — Dars dokumentatsiyasi

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
"""

# 20-DARS
lessons[20] = """# 📅 20. Modullar va Datetime — Dars dokumentatsiyasi

Standard Python kutubxonasi o'z ichiga yuzlab tayyor **Modul (Module)** va kutubxonalarni oladi. Kodni noldan yozmasdan, tayyor modullardan foydalanish ("Gildirakni qayta kashf qilmaslik") professional dasturchining asosiy odatidir.

Bu darsda siz o'zingizning shaxsiy modulingizni yaratish va import qilish, standart `math`, `random` modullari hamda backend dasturlashda eng ko'p ishlatiladigan **`datetime` (Sana va Vaqt)** moduli bilan ishlashni o'rganasiz.

Dasturda foydalanuvchilarning ro'yxatdan o'tgan vaqtini saqlash, vaqt zonalarini to'g'irlash, muddatlarni (deadline) hisoblash kabi amallar aynan `datetime` yordamida bajariladi.

---

## Bu mavzu orqali nimalar qilish mumkin

- Shaxsiy `.py` fayllarni modul sifatida import qilish (`import my_module`);
- Standard `datetime` moduli orqali hozirgi vaqt va sanani olish;
- `strftime` va `strptime` yordamida sanalarni formatlash va matndan sanaga o'tkazish;
- `timedelta` yordamida sanalar o'rtasidagi farqni va kelajakdagi/o'tmishdagi sanalarni hisoblash.

---

## Dars maqsadi

Bu dars oxirida o'quvchi:

- `import` va `from ... import ...` konstruksiyasidan to'g'ri foydalanish;
- Hozirgi sana/vaqtni olish va formatlash (`YYYY-MM-DD`);
- Sanalar bilan matematik amallar bajarish (`timedelta`)

ni mustaqil bajara oladi.

---

## Kerakli oldingi bilimlar

- 17-dars: Funksiyalar;
- 4-dars: Stringlar.

---

# 1. Asosiy tushunchalar va atamalar

## Modul (Module) nima?

> **Modul** — Python kodlari (funksiyalar, o'zgaruvchilar, klasslar) saqlangan alohida `.py` fayli.

## datetime nima?

> **datetime** — sana va vaqt bilan ishlash uchun Python'ning o'rnatilgan standart moduli.

## timedelta nima?

> **timedelta** — ikki sana yoki vaqt oralig'idagi farqni (davomiylikni) ifodalovchi ob'yekt.

---

# 2. Sintaksis va uning izohi

```python
import datetime

# Hozirgi vaqt
hozir = datetime.datetime.now()

# Formatlash (Sana -> String)
matn_sana = hozir.strftime("%Y-%m-%d %H:%M:%S")

# Parsing (String -> Sana)
sana_obj = datetime.datetime.strptime("2024-09-01", "%Y-%m-%d")
```

---

# 3. strftime Format Kodlari Jadvali

| Kod | Vazifasi | Misol Natijasi |
|---|---|---|
| `%Y` | 4 xonali Yil | `2024` |
| `%m` | 2 xonali Oy | `09` |
| `%d` | 2 xonali Kun | `01` |
| `%H` | 24-soatlik Soat | `15` |
| `%M` | Daqiqa | `45` |
| `%S` | Sekund | `30` |

---

# 4. Kod misollari

## Misol 1 — Hozirgi sana va alohida qismlari

```python
import datetime

now = datetime.datetime.now()

print("Yil:", now.year)
print("Oy:", now.month)
print("Kun:", now.day)
```

---

## Misol 2 — Sana yaratish va formatlash

```python
from datetime import datetime

toshkent_vaqti = datetime.now()
chiroyli_sana = toshkent_vaqti.strftime("%d/%m/%Y, %H:%M")

print("Formatlangan vaqt:", chiroyli_sana)
```

---

## Misol 3 — timedelta (Kelajak sanasini hisoblash)

```python
from datetime import datetime, timedelta

bugun = datetime.now()
kelajak_30_kun = bugun + timedelta(days=30)

print("Bugun:", bugun.strftime("%Y-%m-%d"))
print("30 kundan keyin:", kelajak_30_kun.strftime("%Y-%m-%d"))
```

---

## Misol 4 — Sanalar farqini hisoblash

```python
from datetime import datetime

yangi_yil = datetime(2025, 1, 1)
bugun = datetime.now()

farq = yangi_yil - bugun
print(f"Yangi yilgacha {farq.days} kun va {farq.seconds // 3600} soat qoldi!")
```

---

# 5. Real loyiha misoli — Obuna Tugash Muddatini Tekshirish

```python
from datetime import datetime, timedelta

def obuna_holatini_tekshir(boshlangan_sana_str, davomiylik_kun=30):
    boshlangan = datetime.strptime(boshlangan_sana_str, "%Y-%m-%d")
    tugash_sanası = boshlangan + timedelta(days=davomiylik_kun)
    bugun = datetime.now()
    
    if bugun > tugash_sanası:
        return False, "Obuna muddati tugagan!"
    else:
        qolgan_kun = (tugash_sanası - bugun).days
        return True, f"Obuna faol. {qolgan_kun} kun qoldi."

faolmi, xabar = obuna_holatini_tekshir("2024-08-10", davomiylik_kun=30)
print("Natija:", xabar)
```

---

# 6. Ko'p uchraydigan xatolar

## Xato 1: strftime va strptime ni aralashtirib yuborish

- **`strftime`** (String **Format** Time): Sana Ob'yektini -> Stringga aylantiradi.
- **`strptime`** (String **Parse** Time): String Matnini -> Sana Ob'yektiga aylantiradi.

---

# 7. Sinfdagi amaliy topshiriqlar

1. **Oson**: Tug'ilgan kuningiz sanasini yarating va uning haftaning qaysi kuniga to'g'ri kelishini chiqaring.
2. **O'rta**: Foydalanuvchi kiritgan sanadan shu kungacha necha kun o'tganini hisoblang.

---

# 8. Uyga vazifa

1. Mahsulotning ishlab chiqarilgan sanasi va yaroqlilik muddatini (kun) qabul qilib, bugungi kunda yaroqli yoki o'tib ketganini aniqlovchi funksiya yozing.

---

# 9. Tekshirish savollari

1. `timedelta` ob'yekti nima uchun ishlatiladi?
2. `%m` va `%d` kodlarining farqi nimada?

---

## Javoblar

1. Sanalarga kun, soat, sekund qo'shish yoki ayirish orqali vaqt oralig'ini hisoblash uchun.
2. `%m` bu 2 xonali oy, `%d` esa 2 xonali kunni bildiradi.

---

# 10. Qisqa xulosa

Bu darsda Python modullari, ularni import qilish hamda `datetime` moduli yordamida sana va vaqt bilan professional ishlash o'rganildi.
"""

# 21-DARS
lessons[21] = """# 🛡️ 21. Xatolarni boshqarish (Exceptions) — Dars dokumentatsiyasi

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
            print("Xato: Iltimos, faqat son kiriting!\n")
        except ZeroDivisionError:
            print("Xato: Ikkinchi son nol bo'lmasligi kerak!\n")

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
"""

# 22-DARS
lessons[22] = """# 📁 22. Fayllar bilan ishlash — Dars dokumentatsiyasi

Dastur o'chirilganda uning xotirasidagi (RAM) barcha o'zgaruvchilar yo'qoladi. Ma'lumotlarni doimiy (persistent) saqlashning eng sodda usuli ularni **Fayllar (Files)** ko mezonida kompyuter xotirasiga (HDD/SSD) yozishdir.

Python fayllarni ochish, o'qish, yozish va yopish uchun juda qulay imkoniyatlarni taqdim etadi. Ushbu darsda siz `.txt` fayllar yaratish, ularga ma'lumot qo'shish va fayllar bilan ishlashda eng xavfsiz hisoblangan **`with` kontekst menejeri (Context Manager)** bilan ishlashni o'rganasiz.

---

## Bu mavzu orqali nimalar qilish mumkin

- Fayllarni ochish va yopish (`open`, `close`);
- Fayldan ma'lumotlarni o'qish (`read`, `readline`, `readlines`);
- Faylga yangi ma'lumot yozish (`w` rejimi) va ma'lumot qo'shish (`a` rejimi);
- Context Manager (`with open(...) as f:`) yordamida resurslarni xavfsiz boshqarish.

---

## Dars maqsadi

Bu dars oxirida o'quvchi:

- Fayllarni ochish rejimlarini (`r`, `w`, `a`) farqlash;
- `with` operatoridan foydalanish;
- Fayl tarkibini qatorma-qator o mezonida o mezon qilish va tahlil qilish

ni mustaqil bajara oladi.

---

## Kerakli oldingi bilimlar

- 4-dars: Stringlar;
- 21-dars: Xatolarni boshqarish.

---

# 1. Asosiy tushunchalar va atamalar

## File Mode (Fayl Rejimi) nima?

> Fayl ochilayotganda u bilan nima amaliyot bajarilishini belgilovchi belgi: `r` (read - o'qish), `w` (write - qayta yozish), `a` (append - oxiriga qo'shish).

## Context Manager (`with` bayonoti) nima?

> Fayl bilan amallar bajarilib bo'lingach, uni avtomatik va xavfsiz yopilishini kafolatlovchi konstruksiya.

---

# 2. Sintaksis va uning izohi

```python
# Xavfsiz usul (with bilan)
with open("fayl.txt", "w", encoding="utf-8") as f:
    f.write("Salom, Dunyo!\n")
```

---

# 3. Fayl Ochish Rejimlari Jadvali

| Rejim | Nomi | Vazifasi | Fayl Bo'lmasa? |
|---|---|---|---|
| `"r"` | Read | Faqat o'qish uchun | `FileNotFoundError` beradi |
| `"w"` | Write | Yozish (Eskisini o'chirib yuboradi!) | Yangi fayl yaratadi |
| `"a"` | Append | Oxiriga qo'shish | Yangi fayl yaratadi |
| `"r+"` | Read/Write | Ham o'qish, ham yozish | `FileNotFoundError` beradi |

---

# 4. Kod misollari

## Misol 1 — Faylga yozish va o'qish

```python
# Faylga yozish
with open("test.txt", "w", encoding="utf-8") as f:
    f.write("Python dasturlash tili\nFayllar bilan ishlash")

# Faylni o'qish
with open("test.txt", "r", encoding="utf-8") as f:
    matn = f.read()
    print(matn)
```

---

## Misol 2 — Qatorma-qator o'qish (readlines)

```python
with open("test.txt", "r", encoding="utf-8") as f:
    for qator in f:
        print("Qator:", qator.strip())
```

---

## Misol 3 — Fayl oxiriga ma'lumot qo'shish (Append mode)

```python
with open("log.txt", "a", encoding="utf-8") as f:
    f.write("\nYangi log yozuvi qo'shildi.")
```

---

# 5. Real loyiha misoli — Oddiy Log Tizimi

```python
from datetime import datetime

def log_yaz(xabar):
    vaqt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_qatori = f"[{vaqt}] {xabar}\n"
    
    with open("system.log", "a", encoding="utf-8") as f:
        f.write(log_qatori)

log_yaz("Foydalanuvchi tizimga kirdi.")
log_yaz("Ma'lumotlar bazasi yangilandi.")

print("Loglar yozildi!")
```

---

# 6. Ko'p uchraydigan xatolar

## Xato 1: Faylni yopishni unutish (with ishlatmaslik)

Noto'g'ri:
```python
f = open("data.txt", "w")
f.write("test")
# f.close() unutildi -> Ma'lumot xotirada qolib ketishi mumkin!
```

---

# 7. Sinfdagi amaliy topshiriqlar

1. **Oson**: `names.txt` faylini yarating va unga 3 ta ism yozing.
2. **O'rta**: `names.txt` faylini o'qib, undagi ismlarni bosh harfini katta qilib ekranga chiqaring.

---

# 8. Uyga vazifa

1. Foydalanuvchidan matn olib, fayldagi so'zlar va qatorlar sonini hisoblovchi dastur yozing.

---

# 9. Tekshirish savollari

1. `"w"` va `"a"` rejimlari o'rtasidagi asosiy farq nimada?
2. `encoding="utf-8"` nima uchun kerak?

---

## Javoblar

1. `"w"` fayl ichidagi barcha eski ma'lumotni o'chirib yuboradi, `"a"` esa mavjud ma'lumot oxiriga yangisini qo'shadi.
2. Kirill va boshqa maxsus alifbo harflari to'g'ri o mezon qilinishi va saqlanishi uchun.

---

# 10. Qisqa xulosa

Bu darsda Python'da fayllar yaratish, ularni xavfsiz o'qish hamda yozish tamoyillari o'rganildi.
"""

# 23-DARS
lessons[23] = """# 🌐 23. JSON va Requests — Dars dokumentatsiyasi

Zamonaviy dasturlar (Backend, Mobile App, Frontend) bir-biri bilan ma'lumot almashish uchun **API (Application Programming Interface)** lardan foydalanadi. Ma'lumot almashishning eng mashhur formati esa **JSON (JavaScript Object Notation)** di.

**`json` moduli** Python ma'lumot turlarini (Dict, List) JSON matniga va aksincha aylantirish uchun ishlatiladi.

**`requests` kutubxonasi** esa internet orqali serverlarga HTTP so'rovlar (`GET`, `POST`) yuborish va tashqi API lardan (masalan, ob-havo, valyuta kurslari, yangiliklar) ma'lumot olish imkonini beradi.

---

## Bu mavzu orqali nimalar qilish mumkin

- Python ob'yektlarini JSON formatiga o'tkazish (`json.dumps`, `json.dump`);
- JSON formatidagi matnlarni Python ob'yektlariga o'tkazish (`json.loads`, `json.load`);
- `requests` kutubxonasi yordamida websaytlarga HTTP GET va POST so'rovlarini yuborish;
- Tashqi API lar bilan ishlash va real ma'lumotlarni yuklab olish.

---

## Dars maqsadi

Bu dars oxirida o'quvchi:

- JSON va Python Dictionary o'rtasidagi bog'liqlikni tushunish;
- `requests.get()` yordamida API dan ma'lumot olish;
- HTTP Status Kodlarini (`200 OK`, `404 Not Found`) tekshirish

ni mustaqil bajara oladi.

---

## Kerakli oldingi bilimlar

- 14-dars: Dictionary;
- 22-dars: Fayllar.

---

# 1. Asosiy tushunchalar va atamalar

## JSON nima?

> **JSON** — kalit-qiymat ko'rinishidagi, inson uchun ham, kompyuter uchun ham o'qilishi oson bo'lgan matnli ma'lumot formati.

## HTTP Request (HTTP So'rov) nima?

> Mijoz (Client/Python) tomonidan Serverga ma'lumot so'rab yoki yuborib qilinadigan murojaat.

---

# 2. Sintaksis va uning izohi

```python
import json
import requests

# JSON Parsing
py_dict = json.loads('{"ism": "Ali"}')

# API So'rov
response = requests.get("https://api.example.com/data")
data = response.json()
```

---

# 3. JSON Metodlari Jadvali

| Metod | Vazifasi |
|---|---|
| `json.dumps(obj)` | Python Dict -> JSON String ga o'tkazadi |
| `json.loads(json_str)` | JSON String -> Python Dict ga o'tkazadi |
| `json.dump(obj, f)` | Python Dict ni JSON faylga yozadi |
| `json.load(f)` | JSON fayldan Python Dict ga o'qiydi |

---

# 4. Kod misollari

## Misol 1 — JSON Serialization (dumps)

```python
import json

data = {"ism": "Ali", "yosh": 25, "dasturchi": True}
json_text = json.dumps(data, indent=4)

print(json_text)
```

---

## Misol 2 — Real API dan Ma'lumot Olish (Requests)

```python
import requests

url = "https://jsonplaceholder.typicode.com/todos/1"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print("Sarlavha:", data["title"])
    print("Bajarildimi:", data["completed"])
```

---

# 5. Real loyiha misoli — Valyuta Kurslari Dasturi

```python
import requests

def valyuta_kursini_ol():
    url = "https://cbu.uz/uz/arkhiv-kursov-valyut/json/"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        for item in data:
            if item["Ccy"] == "USD":
                print(f"1 USD = {item['Rate']} so'm ({item['Date']})")
                break

valyuta_kursini_ol()
```

---

# 6. Ko'p uchraydigan xatolar

## Xato 1: `requests` o'rnatilmagan bo'lsa

```
ModuleNotFoundError: No module named 'requests'
```
Yechim: Terminalda `pip install requests` buyrug'ini runs qiling.

---

# 7. Sinfdagi amaliy topshiriqlar

1. **Oson**: Python lug'atini `data.json` fayliga saqlang.
2. **O'rta**: `https://jsonplaceholder.typicode.com/users` API sidan foydalanuvchilar ismini oling.

---

# 8. Uyga vazifa

1. Istalgan ochiq Ob-havo yoki Valyuta API sidan foydalanib, konsol uchun foydali kichik loyiha tuzing.

---

# 9. Tekshirish savollari

1. JSON va Python Dictionary farqi nimada?
2. HTTP Status `200` va `404` nimani bildiradi?

---

## Javoblar

1. Dict bu Python ma'lumot strukturasi, JSON esa matnli (string) ma'lumot shaklidir.
2. `200` — Muvaffaqiyatli so'rov, `404` — Sahifa yoki resurs topilmadi.

---

# 10. Qisqa xulosa

Bu darsda JSON formati bilan ishlash hamda `requests` yordamida API so'rovlarini amalga oshirish o'rganildi.
"""

# 24-DARS
lessons[24] = """# 🎓 24. 2-modul imtihoni — Dars dokumentatsiyasi

2-modul imtihoni — bu 13-darsdan 23-darsgacha o'rganilgan barcha mavzular (Tuple, Set, Dictionary, Murakkab ma'lumotlar, Comprehension, Funksiyalar, *args, **kwargs, Scope, Lambda, Rekursiya, Modullar, Datetime, Exceptions, Fayllar va JSON/Requests) bo'yicha bilimlarni sinovdan o'tkazuvchi yakuniy nazoratdir.

Imtihon nazariy va amaliy bo mezonlardan iborat bo'lib, o'quvchining professional Backend dasturchi sifatidagi tayyorgarlik darajasini ko'rsatadi.

---

## Imtihon strukturasi (100 Ball)

1. **Nazariy Savollar va Testlar (30 Ball)**
2. **Amaliy Kodlash Topshiriqlari (50 Ball)**
3. **Real Loyiha Masalasi (20 Ball)**

---

# 1. Nazariy Tekshiruv Savollari

1. Tuple va List farqini 2 ta misolda tushuntiring.
2. Set nima uchun unikal elementlar saqlaydi?
3. Dictionary da `.get()` metodi va `[]` murojaat farqi nimada?
4. `List Comprehension` qanday sintaksisga ega?
5. `*args` va `**kwargs` birgalikda ishlatilganda tartibi qanday bo'ladi?
6. `LEGB` qoidasini tushuntiring.
7. Lambda funksiyaning oddiy funksiyadan farqi nimada?
8. Rekursiv funksiyada `Base Case` bo'lmasa nima yuz beradi?
9. `strftime` va `strptime` farqini ayting.
10. `try-except-finally` blokida `finally` qachon ishlaydi?

---

# 2. Amaliy Topshiriqlar

## Topshiriq 1: Data Cleaning (Comprehension & Dict)
Berilgan aralash ro'yxatdan faqat musbat sonlarning kvadratini olib, unikal Set ko'rinishida qaytaruvchi funksiya yozing.

## Topshiriq 2: Multi-Calculator (*args & Exception)
Istalgancha sonlarni qabul qilib ularning o'rtacha qiymatini hisoblovchi, agar argument berilmasa yoki nolga bo'lish yuzaga kelsa `ZeroDivisionError` ni ushlab 0 qaytaruvchi funksiya yozing.

## Topshiriq 3: File & JSON Handling
`users.json` faylidan foydalanuvchilar ma'lumotlarini o'qib, faqat faol foydalanuvchilarni `active_users.txt` fayliga yozuvchi skript tuzing.

---

# 3. Yakuniy Real Loyiha Masalasi (20 Ball)

**Valyuta & Log Tizimi:**
1. CBU API sidan bugungi dollar kursini `requests` orqali yuklab oling.
2. Foydalanuvchidan so'm madorini so'rang va dollarga o'giring.
3. Barcha amaliyot va natijani vaqti bilan `transactions.log` fayliga `with open` yordamida yozib boring.
4. Barcha mumkin bo'lgan xatoliklarni (`requests.exceptions.RequestException`, `ValueError`) `try-except` bilan nazorat qiling.

---

# 10. Qisqa xulosa

Ushbu imtihon 2-modul bo'yicha bilimlaringizni mustahkamlaydi va keyingi murakkab OOP (Ob'yektga Yo'naltirilgan Dasturlash) moduliga o'tish eshigini ochadi.
"""

for num, content in lessons.items():
    filepath = os.path.join(DOCS_DIR, f"dars_{num:02d}.md")
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"dars_{num:02d}.md yaratildi: {len(content)} belgi")
