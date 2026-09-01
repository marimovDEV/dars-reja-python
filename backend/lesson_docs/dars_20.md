# 📅 20. Modullar va Datetime — Dars dokumentatsiyasi

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
