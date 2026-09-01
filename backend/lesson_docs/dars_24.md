# 🎓 24. 2-modul imtihoni — Dars dokumentatsiyasi

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
