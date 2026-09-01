# 📁 22. Fayllar bilan ishlash — Dars dokumentatsiyasi

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
    f.write("Salom, Dunyo!
")
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
    f.write("Python dasturlash tili
Fayllar bilan ishlash")

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
    f.write("
Yangi log yozuvi qo'shildi.")
```

---

# 5. Real loyiha misoli — Oddiy Log Tizimi

```python
from datetime import datetime

def log_yaz(xabar):
    vaqt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_qatori = f"[{vaqt}] {xabar}
"
    
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
