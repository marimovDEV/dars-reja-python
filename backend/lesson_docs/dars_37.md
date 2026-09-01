# 🌐 37. HTTP, REST API va Web asoslari — Dars dokumentatsiyasi

Zamonaviy veb va mobil dasturlar (Frontend, Mobile App, Backend) o'zaro **HTTP (Hypertext Transfer Protocol)** protokoli orqali muloqot qiladi. Backend dasturchining asosiy vazifasi — mijoz (client/brauzer) yuborgan so'rovlarga to'g'ri javob beruvchi server va **REST API** interfeyslarini qurishdir.

**REST (Representational State Transfer)** — bu veb-xizmatlarni (Web Services) loyihalashtirish uchun ishlatiladigan eng mashhur me'moriy uslub (architectural style) hisoblanadi.

Ushbu darsda siz HTTP so'rov turlari (`GET`, `POST`, `PUT`, `DELETE`), so'rov sarlavhalari (`Headers`), javob kodlari (`Status Codes: 200, 201, 400, 404, 500`) va REST API tamoyillarini o'rganasiz.

---

## Bu mavzu orqali nimalar qilish mumkin

- Client-Server (Mijoz-Server) arxitekturasini tushunish;
- HTTP So'rov metodlaridan (`GET`, `POST`, `PUT`, `PATCH`, `DELETE`) to'g'ri foydalanish;
- HTTP Status Kodlarining guruhlanishini va ma'nolarini bilish;
- RESTful API resurs yo'nalishlarini (Endpoints) to'g'ri loyihalashtirish (`/api/v1/users/`);
- API javoblarini JSON formatida shakllantirish.

---

## Dars maqsadi

Bu dars oxirida o'quvchi:

- HTTP so'rov-javob siklini (Request-Response Cycle) tushunish;
- REST API mezonlari va prinsiplarini bilish;
- Status kodlarini to mezon holatda ishlatish;
- Postman yoki cURL orqali API so'rovlarini sinash

ni mustaqil bajara oladi.

---

## Kerakli oldingi bilimlar

- 23-dars: JSON va requests;
- 31-dars: SQL va ma'lumotlar bazasi.

---

# 1. Asosiy tushunchalar va atamalar

## Client-Server Arxitekturasi nima?

> **Client** (brauzer, mobil ilova) so'rov yuboradi, **Server** (Django/FastAPI) so'rovni qayta ishlab javob (Response) qaytaradi.

## REST API nima?

> HTTP protokoli ustiga qurilgan, resurslarga URL orqali murojaat qiluvchi va ma'lumotlarni asosan JSON ko'rinishida uzatuvchi backend interfeysi.

## Endpoint nima?

> Serverdagi muayyan resursga olib boruvchi URL manzil. Masalan: `https://api.site.com/products/`.

---

# 2. HTTP So'rov Metodlari va Status Kodlari

## HTTP Metodlari (Verbs)

| Metod | Vazifasi | Misol |
|---|---|---|
| **`GET`** | Resursni (ma'lumotni) o'qish/olish | `/api/users/` |
| **`POST`** | Yangi resurs yaratish | `/api/users/` (Body bilan) |
| **`PUT`** | Mavjud resursni to'liq yangilash | `/api/users/1/` |
| **`PATCH`** | Resursning ma'lum qismini yangilash | `/api/users/1/` |
| **`DELETE`**| Resursni o'chirish | `/api/users/1/` |

## HTTP Status Kodlari

- **`2xx` (Success)**: `200 OK`, `201 Created` (Yangi resurs yaratildi).
- **`3xx` (Redirection)**: `301 Moved Permanently`, `302 Found`.
- **`4xx` (Client Error)**: `400 Bad Request`, `401 Unauthorized`, `403 Forbidden`, `404 Not Found`.
- **`5xx` (Server Error)**: `500 Internal Server Error`, `502 Bad Gateway`.

---

# 3. Kod misollari (REST API Struct Simulyatsiyasi)

```python
# REST API Endpoint Strukturasi Namunasining Standarti
# GET /api/v1/books/       -> Barcha kitoblarni olish
# POST /api/v1/books/      -> Yangi kitob qo'shish
# GET /api/v1/books/5/     -> ID=5 bo'lgan kitobni olish
# PUT /api/v1/books/5/     -> ID=5 kitobni to'liq o'zgartirish
# DELETE /api/v1/books/5/  -> ID=5 kitobni o'chirish
```

---

# 10. Qisqa xulosa

Bu darsda Web arxitekturasi, HTTP protokoli, Status kodlar va REST API tamoyillari o'rganildi.
