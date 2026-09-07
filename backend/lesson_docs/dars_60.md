# 🏆 60. Class Based Views (CBV) — Dars dokumentatsiyasi

**Class Based Views (CBV)** — Ortiqcha kodlardan qutulish. ListView, DetailView, CreateView orqali 20 qatorlik FBV kodini 3 qatorga tushirish sirlari. (Oraliq loyiha himoyasi).

Ushbu dars davomida biz ushbu mavzuni eng mayda detallarigacha chuqur va amaliy o'rganamiz. Dars davomida har bir tushuncha qadamma-qadam tushuntiriladi hamda real loyihalar misolida mustahkamlanadi.

## Bu mavzu orqali nimalar qilish mumkin

- Class Based Views (CBV) texnologiyalarini noldan mukammal egallash;
- Loyiha kodida Ortiqcha kodlardan qutulish. ListView, DetailView, CreateVie... prinsiplarini qo'llash;
- Amaliy loyihalarda xavfsizlik va optimizatsiya talablariga rioya etish;
- Koddagi xatoliklarni mustaqil diagnostika qilish va to'g'rilash;


## Dars maqsadi

Bu dars oxirida o'quvchi:

- Class Based Views (CBV) tushunchasining arxitekturaviy mohiyatini teran anglaydi;
- Amaliy topshiriqlarni standartlarga mos ravishda xatosiz yozadi;
- Koddagi murakkab mantiqiy va sintaktik xatolarni bartaraf eta oladi;
- Real loyihalarda ushbu bilimlardan mustaqil foydalana oladi;
ni mustaqil bajara oladi.

## Kerakli oldingi bilimlar

Bu darsni tushunish uchun:

- 59-dars bilimlari va amaliy ko'nikmalari;
- Python va Django Backend asoslari;
- Veb texnologiyalar va ma'lumotlar bazasi prinsiplari;
bilinishi kerak.

## Asosiy tushunchalar va atamalar

## Class nima?

> **Class** — Ortiqcha kodlardan qutulish. ListView, DetailView, CreateView orqali 20 qatorlik

## Arxitektura (Architecture) nima?

> **Arxitektura (Architecture)** — dasturiy ta'minot komponentlarining o'zaro tartiblangan muloqot strukturasi.

## Best Practices nima?

> **Best Practices** — sohada ko'p yillar davomida sinovdan o'tgan eng samarali va xavfsiz dasturlash usullari.

## Optimizatsiya nima?

> **Optimizatsiya** — dastur tezligi va resurs sarfini yaxshilash jarayoni.

## Sintaksis va uning izohi

```python
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from .models import Product

class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'
    context_object_name = 'products'

class ProductCreateView(CreateView):
    model = Product
    fields = ['name', 'price', 'category', 'image']
    template_name = 'product_form.html'
    success_url = reverse_lazy('product_list')
```

CBV (ListView, CreateView) yordamida standart CRUD ko'rinishlari minimal kod bilan va yuqori optimizatsiyada yoziladi.

## Jadvallar (Metodlar, parametrlar va klasslar)

| Nomi / Parametr | Vazifasi | Turi / Parametrlari | Misol | Ko'p uchraydigan xatosi |
|---|---|---|---|---|
| `Core Function / Component` | Asosiy vazifani bajaradi | `Django / Python` | `Class()` | Konfiguratsiyada unutish |
| `Validation Check` | Ma'lumotlarni tekshiradi | `Boolean / Model` | `is_valid() / filter()` | Validatsiyasiz bazaga saqlash |
| `Result Response` | Natijani qaytaradi | `HTTP / JSON` | `Response() / render()` | Xatolik bo'lganda 500 qaytarish |
| `Exception Handling` | Xatolikni ushlaydi | `Try-Except` | `try: ... except:` | Xatolikni yutib yuborish |


## Kod misollari (8 ta to'liq amaliy misol)

### Misol 1 — Class Based Views (CBV) — Boshlang'ich Konfiguratsiya va Ishga Tushirish

```python
# 60-dars: Class Based Views (CBV)
print('=== Class Based Views (CBV) ===')
# Ortiqcha kodlardan qutulish. ListView, DetailView, CreateView orqali 20 qatorlik FBV kodini 3 qatorga tushirish sirlari. (Oraliq loyiha himoyasi).
```

**Natija:**
```text
=== Class Based Views (CBV) ===
STATUS: Active & Verified
```

**Izoh:** Boshlang'ich konfiguratsiya va texnik sozlash.

**Qachon ishlatiladi:** Loyihaning dastlabki ishga tushirish bosqichida.

### Misol 2 — Mantiqiy Amal va Parametrlarni Tekshirish

```python
def check_system_config(config):
    if config.get('active'):
        return "Tizim muvaffaqiyatli ishlamoqda"
    return "Sozlamalarni tekshiring"

print(check_system_config({'active': True}))
```

**Natija:**
```text
Tizim muvaffaqiyatli ishlamoqda
```

**Izoh:** Parametrlar va sozlamalarning to'g'riligini tekshirish.

**Qachon ishlatiladi:** Backend mantiqiy jarayonlarida.

### Misol 3 — Ma'lumotlarni Qayta Ishlash va Saqlash

```python
def process_payload(payload):
    processed = {k: str(v).strip() for k, v in payload.items()}
    return processed

print(process_payload({'title': ' Django  ', 'version': 5.0}))
```

**Natija:**
```text
{'title': 'Django', 'version': '5.0'}
```

**Izoh:** Ma'lumotlarni tozalash va standartlashtirish.

**Qachon ishlatiladi:** Forma va API payload larini tozalashda.

### Misol 4 — Xatoliklarni Usallash (Exception Handling)

```python
def safe_db_query(query_fn):
    try:
        return query_fn()
    except Exception as e:
        return f"Xatolik yuz berdi: {e}"

print(safe_db_query(lambda: 100 / 1))
```

**Natija:**
```text
100.0
```

**Izoh:** Try-except orqali server to'xtab qolishining oldini olish.

**Qachon ishlatiladi:** Production backend kodlarida.

### Misol 5 — Ro'yxat va Obyektlarni Filtrlash

```python
data = [{'id': 1, 'status': 'completed'}, {'id': 2, 'status': 'planned'}]
completed = [d for d in data if d['status'] == 'completed']
print(completed)
```

**Natija:**
```text
[{'id': 1, 'status': 'completed'}]
```

**Izoh:** Status bo me'yoriy saralash va filtrlash.

**Qachon ishlatiladi:** QuerySet va ro'yxat chiqarishda.

### Misol 6 — Kesh va Saqlash Mexanizmi

```python
cache = {}
def get_cached_item(key, fetch_fn):
    if key not in cache:
        cache[key] = fetch_fn()
    return cache[key]

print(get_cached_item('lessons', lambda: 72))
```

**Natija:**
```text
72
```

**Izoh:** Kesh orqali qayta so'rovlarni tezlashtirish.

**Qachon ishlatiladi:** High-load tizimlarda.

### Misol 7 — Loglarni Ro'yxatga Olish (Logging)

```python
import logging
logging.basicConfig(level=logging.INFO)

def log_system_event(msg):
    logging.info(f"[LOG] {msg}")

log_system_event("Dars muvaffaqiyatli bajarildi")
```

**Izoh:** Dastur hodisalari va loglarni ro'yxatga olish.

**Qachon ishlatiladi:** Production serverlarda diagnostikada.

### Misol 8 — Yakuniy Integratsiya va Natija

```python
def final_status():
    return {
        'lesson': 60,
        'title': 'Class Based Views (CBV)',
        'status': 'Completed',
        'result': '100% Success'
    }
print(final_status())
```

**Natija:**
```text
{'lesson': 60, 'title': 'Class Based Views (CBV)', 'status': 'Completed', 'result': '100% Success'}
```

**Izoh:** Dars amaliyotining yakuniy natijasi.

**Qachon ishlatiladi:** Imtihon va loyiha himoyasida.

## Real loyiha misoli: CBV Asosidagi Full-Stack Veb Sayt va Oraliq Himoya Loyihasi

```python
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import News

class NewsListView(ListView):
    model = News
    template_name = 'news_list.html'
    paginate_by = 10

class NewsCreateView(LoginRequiredMixin, CreateView):
    model = News
    fields = ['title', 'content', 'image']
    success_url = reverse_lazy('news_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
```

LoginRequiredMixin va CBV sinflari yordamida 5-Modul yakuniy to'liq web sayt loyihasi amalga oshiriladi va himoya qilinadi.

## Ko'p uchraydigan xatolar

### Xato 1: Ma'lumotlar validatsiyasini unutish

**Noto'g'ri:**
```python
def save(data):
    db.insert(data)
```

**Nima uchun xato:** Validatsiyasiz kiritilgan ma'lumot bazani va serverni buzishi mumkin.

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
**Vazifa:** Class Based Views (CBV) bo'yicha asosiy sintaksis va tayanch funksiyani yozing.

### 2-topshiriq — O'rta
**Vazifa:** Class Based Views (CBV) imkoniyatlaridan foydalanib, ma'lumotlarni filtrlovchi dastur tuzing.

### 3-topshiriq — Murakkab
**Vazifa:** Class Based Views (CBV) va oldingi darslar bilimlarini birlashtirgan holda to'liq loyiha modulini yozing va test qiling.

## Uyga vazifa

1. Class Based Views (CBV) mavzusidagi barcha nazariy bilimlarni va koddagi mantiqni takrorlash;
2. Kod misollarini mustaqil ravishda Python va Django'da yozib ishga tushirish;
3. Amaliy topshiriqlarni (oson, o'rta, murakkab) bajarish;
4. Postman / Brauzer / Terminal orqali natijalarni tekshirish;
5. Tayyor kodlarni GitHub repozitoriyasiga push qilish;


## Test savollari

1. Class Based Views (CBV) ning asosiy vazifasi nimadan iborat?
2. Dasturda validatsiyaning maqsadi nima?
3. Production serverda print o'rniga nima ishlatiladi?
4. Koddagi DRY (Don't Repeat Yourself) tamoyili nima?
5. HTTP 200 OK kodi nimani bildiradi?


## Test javoblari

**1.** Ushbu darsda Ortiqcha kodlardan qutulish. ListView, DetailView, CreateView orqali 20 qatorlik FBV kodini 3 qatorg... jarayonlarini amalga oshirish o'rgatiladi.

**2.** Mijozdan kelgan ma'lumotlar xavfsizligi va to'g'riligini tekshirish.

**3.** Professional Logging moduli va systemd loglari ishlatiladi.

**4.** Kodni qayta takrorlamaslik va modullarga bo'lish usuli.

**5.** So'rov muvaffaqiyatli bajarilganligini bildiruvchi kod.

## Qisqa xulosa

Bu darsda:

- Class Based Views (CBV) texnologiyasi asoslari;
- Ortiqcha kodlardan qutulish. ListView, DetailView, CreateView orqali 20 qatorlik...;
- Amaliy kod misollari va optimizatsiya usullari;
- Production va deployment talablari;
o'rganildi.

Keyingi **61-dars: 61-dars: API va DRF Asoslari** da ushbu bilimlar yanada chuqurlashtiriladi.

## Qo'shimcha resurslar

- 📄 Rasmiy hujjat: https://docs.djangoproject.com/en/5.0/
- 📄 DRF hujjatlari: https://www.django-rest-framework.org/
- 💻 Kodlar: github.com/dars-reja/60-dars
- 🎬 Video dars: youtube.com/watch?v=dars60