# 📖 14. Dictionary — Dars dokumentatsiyasi

Dictionary (Lug'at) — Python'da ma'lumotlarni **Key-Value (Kalit-Qiymat)** juftligi ko'rinishida saqlaydigan eng qudratli ma'lumot strukturalaridan biridir. Har bir kalit (`key`) takrorlanmas bo'lib, u tegishli qiymatga (`value`) ishora qiladi.

Real hayotdagi ko'plab ma'lumotlar lug'at tuzilishiga ega: foydalanuvchi profili (ism, familiya, yosh), mahsulot xususiyatlari (narxi, nomi, ombordagi soni) yoki sozlamalar.

Dictionary Python 3.7+ versiyalaridan boshlab tartiblangan (ordered) hisoblanadi va xotiradan juda tez ma'lumot qidirish (Hash Table mexanizmi sababli) imkoniyatini beradi.

---

## Bu mavzu orqali nimalar qilish mumkin

- Key-Value ko'rinishida murakkab strukturaga ega ma'lumotlarni saqlash;
- Kalit bo'yicha qiymatni bir zumda olish va yangilash;
- Lug'at metodlari (`keys()`, `values()`, `items()`, `get()`) bilan ishlash;
- Lug'at elementlarini sikl yordamida aylanib chiqish;
- Ichma-ich (Nested) lug'atlar yaratish.

---

## Dars maqsadi

Bu dars oxirida o'quvchi:

- Dictionary yaratish va undan to'g'ri foydalanish;
- `get()` metodi orqali xavfsiz qiymat olish;
- Lug'atni o'zgartirish, qo'shish va o'chirish;
- `.items()` yordamida kalit va qiymatni birga iteratsiya qilish

ni mustaqil bajara oladi.

---

## Kerakli oldingi bilimlar

- 11-dars: List asoslari;
- 13-dars: Tuple va Set.

---

# 1. Asosiy tushunchalar va atamalar

## Dictionary (dict) nima?

> **Dictionary** — jingalak qavslar `{}` ichida `key: value` juftliklari ko'rinishida saqlanuvchi, o'zgaruvchan ma'lumot strukturasi.

## Key (Kalit) nima?

> **Key** — lug'atdagi har bir qiymatga murojaat qilish uchun ishlatiladigan unikal nom. Kalit har doim o'zgarmas (immutable) turda bo'lishi shart (str, int, tuple).

## Value (Qiymat) nima?

> **Value** — kalitga biriktirilgan ma'lumot. Har qanday turda (int, list, dict, bool va h.k.) bo'lishi mumkin.

---

# 2. Sintaksis va uning izohi

```python
# Lug'at yaratish
user = {
    "username": "ali123",
    "email": "ali@mail.com",
    "age": 25
}

# Murojaat qilish
print(user["username"]) # Ali123
print(user.get("age")) # 25
```

---

# 3. Dictionary metodlari jadvali

| Metod | Vazifasi | Misol |
|---|---|---|
| `.get(key, default)` | Kalit bo'yicha qiymat oladi (xavfsiz) | `d.get("age", 0)` |
| `.keys()` | Barcha kalitlar ro'yxatini beradi | `d.keys()` |
| `.values()` | Barcha qiymatlar ro'yxatini beradi | `d.values()` |
| `.items()` | Kalit-qiymat juftliklarini Tuple ko'rinishida beradi | `d.items()` |
| `.update(dict2)` | Boshqa lug'at bilan yangilaydi | `d.update({"a": 1})` |
| `.pop(key)` | Kalitli elementni o'chirib qiymatini qaytaradi | `d.pop("age")` |
| `.clear()` | Lug'atni to'liq tozalaydi | `d.clear()` |

---

# 4. Kod misollari

## Misol 1 — Lug'at yaratish va o'qish

```python
talaba = {
    "ism": "Vali",
    "yosh": 20,
    "kurs": 3
}

print(talaba["ism"])
print(talaba.get("guruh", "Guruh ko'rsatilmadi"))
```

Natija:
```
Vali
Guruh ko'rsatilmadi
```

---

## Misol 2 — Qiymatlarni o'zgartirish va qo'shish

```python
avto = {"model": "Cobalt", "rang": "Oq"}
avto["rang"] = "Qora" # O'zgartirish
avto["yil"] = 2023   # Yangi kalit qo'shish

print(avto)
```

Natija:
```
{'model': 'Cobalt', 'rang': 'Qora', 'yil': 2023}
```

---

## Misol 3 — Lug'at bo'ylab sikl (for loop)

```python
narxlar = {"olma": 12000, "banan": 25000, "uzum": 18000}

for mahsulot, narx in narxlar.items():
    print(f"{mahsulot.capitalize()}: {narx} so'm")
```

Natija:
```
Olma: 12000 so'm
Banan: 25000 so'm
Uzum: 18000 so'm
```

---

## Misol 4 — Elementni o'chirish (pop va del)

```python
baza = {"a": 1, "b": 2, "c": 3}
ochirilgan = baza.pop("b")

print("O'chirildi:", ochirilgan)
print("Qoldi:", baza)
```

Natija:
```
O'chirildi: 2
Qoldi: {'a': 1, 'c': 3}
```

---

## Misol 5 — Ichma-ich (Nested) lug'atlar

```python
xodimlar = {
    "emp1": {"ism": "Ali", "lavozim": "Dev"},
    "emp2": {"ism": "Sardor", "lavozim": "QA"}
}

print(xodimlar["emp1"]["ism"])
```

Natija:
```
Ali
```

---

# 5. Real loyiha misoli — Savat va Mahsulotlar hisobi

```python
mahsulotlar = {
    "1": {"nomi": "Noutbuk", "narx": 8000000},
    "2": {"nomi": "Sichqoncha", "narx": 150000}
}

savat = ["1", "2", "2"] # ID lardan iborat savat
jami = 0

print("--- SHAXSIY CHEK ---")
for item_id in set(savat):
    sanoq = savat.count(item_id)
    nom = mahsulotlar[item_id]["nomi"]
    narx = mahsulotlar[item_id]["narx"]
    summa = sanoq * narx
    jami += summa
    print(f"{nom} x {sanoq} ta = {summa} so'm")

print(f"JAMI TO'LOV: {jami} so'm")
```

---

# 6. Ko'p uchraydigan xatolar

## Xato 1: Mavjud bo'lmagan kalitga `[]` orqali murojaat qilish

Noto'g'ri:
```python
d = {"a": 1}
print(d["b"]) # KeyError beradi!
```

To'g'ri:
```python
print(d.get("b", "Topilmadi")) # Xavfsiz!
```

---

# 7. Sinfdagi amaliy topshiriqlar

1. **Oson**: 3 ta kalitli lug'at yarating va `.keys()` hamda `.values()` metodlarini chiqaring.
2. **O'rta**: Lug'at ichidagi barcha sonli qiymatlarning yig'indisini hisoblovchi kod yozing.

---

# 8. Uyga vazifa

1. Foydalanuvchi kiritgan matndagi har bir so'z necha marta uchrashini lug'atda hisoblang.
2. Lug'at kalitlari va qiymatlari o'rnini almashtiruvchi dastur tuzing.

---

# 9. Tekshirish savollari

1. Dictionary kaliti sifatida qaysi ma'lumot turlari ishlatilishi mumkin?
2. `get()` metodining afzalligi nimada?
3. `.items()` metodi nima qaytaradi?

---

## Javoblar

1. Faqat o'zgarmas (immutable) turlar: `str`, `int`, `float`, `tuple`.
2. Kalit topilmasa dastur qulab tushmaydi (`KeyError` bermaydi), balki `None` yoki default qiymat qaytaradi.
3. Kalit va qiymatlardan iborat `(key, value)` ko'rinishidagi tuple'lar ro'yxatini.

---

# 10. Qisqa xulosa

Bu darsda Dictionary ma'lumot strukturasi, Key-Value konseptsiyasi, lug'atlar ustida amallar bajarish va xavfsiz murojaat metodlari o'rganildi.
