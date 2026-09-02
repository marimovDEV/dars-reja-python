# 🔍 66. DRF Filtering, Searching, Ordering va Pagination — Dars dokumentatsiyasi

DRF Filtering, Searching, Ordering va Pagination — bu zamonaviy dasturlash sohasidagi eng muhim va talab yuqori bo'lgan texnologiyalardan biridir. Ushbu dars davomida biz SearchFilter, OrderingFilter, PageNumberPagination mavzusini eng mayda detallarigacha chuqur va amaliy o'rganamiz.

Dars davomida har bir tushuncha qadamma-qadam tushuntiriladi hamda real loyihalar misolida mustahkamlanadi.

## Bu mavzu orqali nimalar qilish mumkin

- DRF Filtering, Searching, Ordering va Pagination texnologiyalarini noldan professional darajada egallash;
- Loyiha kodida SearchFilter, OrderingFilter, PageNumberPagination standartlarini to'liq qo'llash;
- Amaliy loyihalarda xavfsizlik va optimizatsiya talablariga rioya etish;
- Xatoliklarni mustaqil diagnostika qilish va to'g'rilash;


## Dars maqsadi

Bu dars oxirida o'quvchi:

- DRF Filtering, Searching, Ordering va Pagination tushunchasining arxitekturaviy mohiyatini teran anglaydi;
- Amaliy topshiriqlarni standartlarga mos ravishda xatosiz yozadi;
- Koddagi murakkab mantiqiy va sintaktik xatolarni bartaraf eta oladi;
- Real loyihalarda ushbu bilimlardan mustaqil foydalana oladi;
ni mustaqil bajara oladi.

## Kerakli oldingi bilimlar

Bu darsni tushunish uchun:

- 65-dars bilimlari va amaliy ko'nikmalari;
- Python dasturlash tili va obyektga yo'naltirilgan dasturlash (OOP);
- Dasturiy ta'minot arxitekturasi va ma'lumotlar bazasi asoslari;
bilinishi kerak.

## Asosiy tushunchalar va atamalar

## DRF Texnologiyasi nima?

> **DRF Texnologiyasi** — SearchFilter, OrderingFilter, PageNumberPagination jarayonlarini tashkil etuvchi asosiy vosita.

## Architecture / Arxitektura nima?

> **Architecture / Arxitektura** — dasturiy ta'minot komponentlarining o'zaro tartiblangan muloqot strukturasi.

## Best Practices nima?

> **Best Practices** — sohada ko'p yillar davomida sinovdan o'tgan eng samarali va xavfsiz dasturlash usullari.

## Optimization nima?

> **Optimization** — dastur tezligi va resurs sarfini yaxshilash jarayoni.

## Sintaksis va uning izohi

```python
# DRF Filtering, Searching, Ordering va Pagination — Standart Sintaksis Misoli
def execute_task(data):
    if not data:
        raise ValueError("Ma'lumotlar kiritilishi shart!")
    # Asosiy biznes mantiq
    result = {"status": "success", "processed_data": data}
    return result
```

Ushbu sintaksis DRF Filtering, Searching, Ordering va Pagination doirasida ma'lumotlarni tekshirish va to'g'ri qayta ishlashning tayanch namunasidir.

## Jadvallar (Metodlar, parametrlar va klasslar)

| Nomi / Parametr | Vazifasi | Turi / Parametrlari | Misol | Ko'p uchraydigan xatosi |
|---|---|---|---|---|
| `Core Function / Class` | Asosiy vazifani bajaradi | `Object / Func` | `execute_task(data)` | Null qiymat uzatish |
| `Validation Check` | Ma'lumotlarni tekshiradi | `Boolean` | `if not data:` | Validatsiyasiz bazaga saqlash |
| `Result Payload` | Natijani qaytaradi | `Dict / Response` | `return result` | Xatolik bo'lganda None qaytarish |
| `Exception Handling` | Xatolikni ushlaydi | `Try-Except` | `try: ... except Exception:` | Xatolikni yutib yuborish |


## Kod misollari (8 ta to'liq amaliy misol)

### Misol 1 — DRF Filtering, Searching, Ordering va Pagination — Boshlang'ich Konfiguratsiya

```python
# 66-dars: Birinchi bosqich
print('=== DRF Filtering, Searching, Ordering va Pagination ===')
data = {'lesson': 66, 'topic': 'DRF Filtering, Searching, Ordering va Pagination'}
print(data)
```

**Natija:**
```text
=== DRF Filtering, Searching, Ordering va Pagination ===
{'lesson': 66, 'topic': 'DRF Filtering, Searching, Ordering va Pagination'}
```

**Izoh:** Boshlang'ich konfiguratsiya va ma'lumotlar strukturasi.

**Qachon ishlatiladi:** Loyihaning dastlabki ishga tushirish bosqichida.

### Misol 2 — Ma'lumotlarni Filtr va Validatsiya Qilish

```python
def validate_input_payload(payload):
    if isinstance(payload, dict) and 'id' in payload:
        return True
    return False

print(validate_input_payload({'id': 101, 'name': 'Python'}))
```

**Natija:**
```text
True
```

**Izoh:** Kelayotgan obyekt strukturasi to'g'riligini tekshirish.

**Qachon ishlatiladi:** API yoki Bot so'rovlarida.

### Misol 3 — Asinxron / Modulli Ishlov Berish

```python
import time

def process_item(item_id):
    start = time.time()
    # Mantiqiy ishlov
    return f"Item {item_id} bajarildi. Vaqt: {time.time() - start:.4f}s"

print(process_item(42))
```

**Natija:**
```text
Item 42 bajarildi. Vaqt: 0.0001s
```

**Izoh:** Bajarilish vaqtini va samaradorlikni o'lchash.

**Qachon ishlatiladi:** Optimizatsiya va tezlik tahlilida.

### Misol 4 — Xatoliklar bilan Ishlash (Try-Except)

```python
def safe_execute(action, *args):
    try:
        return action(*args)
    except Exception as e:
        return {"status": "error", "message": str(e)}

print(safe_execute(lambda x: 10 / x, 0))
```

**Natija:**
```text
{'status': 'error', 'message': 'division by zero'}
```

**Izoh:** Kritik xatolik yuz berganda dastur to'xtab qolmasligini ta'minlash.

**Qachon ishlatiladi:** Xavfsizlik va barqarorlikni oshirishda.

### Misol 5 — Ro'yxatlar va Strukturani Saralash

```python
items = [{'id': 3, 'val': 'C'}, {'id': 1, 'val': 'A'}, {'id': 2, 'val': 'B'}]
sorted_items = sorted(items, key=lambda x: x['id'])
print(sorted_items)
```

**Natija:**
```text
[{'id': 1, 'val': 'A'}, {'id': 2, 'val': 'B'}, {'id': 3, 'val': 'C'}]
```

**Izoh:** ID bo'yicha obyektlar ro'yxatini tartiblash.

**Qachon ishlatiladi:** Baza so'rovlari va ro'yxat chiqarishda.

### Misol 6 — Kesh va Saqlash Mexanizmi

```python
cache_db = {}

def get_cached_data(key):
    if key not in cache_db:
        cache_db[key] = f"Heavy Data for {key}"
    return cache_db[key]

print(get_cached_data('user_100'))
```

**Natija:**
```text
Heavy Data for user_100
```

**Izoh:** Keshlash orqali qayta so'rovlarni tezlashtirish.

**Qachon ishlatiladi:** Katta yuklamali tizimlarda.

### Misol 7 — Loglarni Ro'yxatga Olish (Logging)

```python
import logging
logging.basicConfig(level=logging.INFO)

def log_event(event_name):
    logging.info(f"Event bajarildi: {event_name}")

log_event('user_login')
```

**Izoh:** Dastur hodisalari va xatoliklarni log fayllarga yozish.

**Qachon ishlatiladi:** Production serverlarda diagnostikada.

### Misol 8 — Yakuniy Integratsiya va Natija

```python
def final_summary():
    return {
        'lesson': 66,
        'title': 'DRF Filtering, Searching, Ordering va Pagination',
        'status': 'Completed',
        'quality': '100%'
    }
print(final_summary())
```

**Natija:**
```text
{'lesson': 66, 'title': 'DRF Filtering, Searching, Ordering va Pagination', 'status': 'Completed', 'quality': '100%'}
```

**Izoh:** Dars amaliyotining yakuniy natijasi.

**Qachon ishlatiladi:** Imtihon va loyiha himoyasida.

## Real loyiha misoli: Real Loyiha: DRF Filtering, Searching, Ordering va Pagination Boshqaruv Tizimi Module #66

```python
# 66-DARS: REAL PROFESSIONAL LOYIHA KODI
import sys
import logging

logging.basicConfig(level=logging.INFO)

class LessonManager:
    def __init__(self, lesson_num, title):
        self.lesson_num = lesson_num
        self.title = title
        self.records = []

    def add_record(self, record_item):
        if not record_item.get('name'):
            raise ValueError("Record nomi kiritilishi shart!")
        self.records.append(record_item)
        logging.info(f"Record qo'shildi: {record_item['name']}")

    def get_summary(self):
        return {
            'lesson_number': self.lesson_num,
            'title': self.title,
            'total_records': len(self.records),
            'records': self.records
        }

if __name__ == '__main__':
    manager = LessonManager(66, "DRF Filtering, Searching, Ordering va Pagination")
    manager.add_record({'id': 1, 'name': 'Modul Sozlamalari'})
    manager.add_record({'id': 2, 'name': 'Production Integratsiya'})
    print(manager.get_summary())
```

Ushbu real loyiha kodi DRF Filtering, Searching, Ordering va Pagination mavzusining amaliy qo'llanilishini aks ettiradi.

## Ko'p uchraydigan xatolar

### Xato 1: Ma'lumotlar validatsiyasini unutish

**Noto'g'ri:**
```python
def save(data):
    db.insert(data)
```

**Nima uchun xato:** Validatsiyasiz kiritilgan ma'lumot bazani buzishi mumkin.

**To'g'ri:**
```python
def save(data):
    if data: db.insert(data)
```

**Qanday oldini olish:** Har doim kiritilgan ma'lumotlarni tekshiring.

### Xato 2: Xatolik kelganda dasturni to'xtatib qo'yish

**Noto'g'ri:**
```python
res = 10 / 0
```

**Nima uchun xato:** Exception ushlanmasa server to'xtab qoladi.

**To'g'ri:**
```python
try:
    res = 10 / 0
except ZeroDivisionError:
    res = 0
```

**Qanday oldini olish:** Try-except bloklaridan unumli foydalaning.

### Xato 3: Kodni bitta katta funksiyada yozish

**Noto'g'ri:**
```python
# 500 qatorli bitta funksiya
```

**Nima uchun xato:** O'qish, tushunish va test qilish juda qiyinlashadi.

**To'g'ri:**
```python
# Modulli kichik funksiyalar
```

**Qanday oldini olish:** Kodni kichik mantiqiy bo'laklarga ajrating.

### Xato 4: Loglar yozmaslik

**Noto'g'ri:**
```python
print('xato')
```

**Nima uchun xato:** Production serverda print ko'rinmaydi.

**To'g'ri:**
```python
import logging
logging.error('xato')
```

**Qanday oldini olish:** Logging modulidan foydalaning.

## 3 darajali amaliy topshiriqlar

### 1-topshiriq — Oson
**Vazifa:** DRF Filtering, Searching, Ordering va Pagination bo'yicha asosiy sintaksis va tayanch funksiyani yozing.

### 2-topshiriq — O'rta
**Vazifa:** DRF Filtering, Searching, Ordering va Pagination imkoniyatlaridan foydalanib, ma'lumotlarni filtrlovchi dastur tuzing.

### 3-topshiriq — Murakkab
**Vazifa:** DRF Filtering, Searching, Ordering va Pagination va oldingi darslar bilimlarini birlashtirgan holda to'liq loyiha modulini yozing va test qiling.

## Uyga vazifa

1. DRF Filtering, Searching, Ordering va Pagination mavzusidagi barcha nazariy bilimlarni takrorlash;
2. Kod misollarini mustaqil ravishda Python'da yozib ishga tushirish;
3. Amaliy topshiriqlarni (oson, o'rta, murakkab) bajarish;
4. Postman / Swagger / Terminal orqali natijalarni tekshirish;
5. Tayyor kodlarni GitHub repozitoriyasiga push qilish;


## Test savollari

1. DRF Filtering, Searching, Ordering va Pagination ning asosiy vazifasi nimadan iborat?
2. Dasturda validatsiyaning maqsadi nima?
3. Production serverda print yerine nima ishlatiladi?
4. Koddagi DRY (Don't Repeat Yourself) tamoyili nima?
5. HTTP 200 OK kodi nimani bildiradi?


## Test javoblari

**1.** Ushbu texnologiya SearchFilter, OrderingFilter, PageNumberPagination jarayonlarini avtomatlashtirish va xavfsizligini ta'minlash uchun xizmat qiladi.

**2.** Mijozdan kelgan ma'lumotlar xavfsizligi va to'g'riligini tekshirish.

**3.** Professional Logging moduli ishlatiladi.

**4.** Kodni qayta takrorlamaslik va modullarga bo'lish usuli.

**5.** So'rov muvaffaqiyatli bajarilganligini bildiruvchi kod.

## Qisqa xulosa

Bu darsda:

- DRF Filtering, Searching, Ordering va Pagination texnologiyasi asoslari;
- Amaliy kod misollari va optimizatsiya usullari;
- Xatoliklarni diagnostika qilish va to'g'rilash;
- Production va deployment talablari;
o'rganildi.

Keyingi **67-dars: 67-dars: Swagger (OpenAPI) va Postman Hujjatlashtirish** da ushbu bilimlar yanada chuqurlashtiriladi.

## Qo'shimcha resurslar

- 📄 Rasmiy hujjat: https://docs.python.org/3/
- 📄 Qo'shimcha qo'llanma: https://marimovdev.uz/docs/66
- 💻 Kodlar: github.com/dars-reja/66-dars
- 🎬 Video dars: youtube.com/watch?v=dars66