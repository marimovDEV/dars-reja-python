# 🌐 23. JSON va Requests — Dars dokumentatsiyasi

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
