# 📦 13. Tuple va Set — Dars dokumentatsiyasi

Tuple (kortej) va Set (to'plam) — Python'dagi ikkita muhim va ko'p ishlatiladigan ma'lumot strukturasidir. Ular list (ro'yxat) ga o'xshash ko'rinsada, xotirada saqlanishi, o'zgartirilishi va bajaradigan vazifalari bo'yicha tubdan farq qiladi.

Tuple — tartiblangan va **o'zgarmas (immutable)** ketma-ketlikdir. Yaratilgandan so'ng unga element qo'shib, o'chirib yoki o'zgartirib bo'lmaydi. Bu xususiyat ma'lumotlar yaxlitligini va xavfsizligini ta'minlash hamda xotiradan samarali foydalanish uchun xizmat qiladi.

Set — tartiblanmagan va **noyob (unique)** elementlar to mezonidir. Set ichida bir xil qiymat takrorlanmaydi. Matematikadagi to'plamlar nazariyasi kabi, Set yordamida kesishma (`intersection`), birlashma (`union`), farq (`difference`) kabi amallarni juda tez bajarish mumkin.

---

## Bu mavzu orqali nimalar qilish mumkin

- Tuple yaratish va undan ma'lumotlarni xavfsiz o'qish;
- Unpacking (qiymatlarni ajratib olish) mexanizmini qo'llash;
- Set yaratish va takroriy elementlarni bir zumda tozalash;
- To'plamlar ustida matematik amallar (`union`, `intersection`, `difference`) bajarish;
- List, Tuple va Set o'rtasidagi farqlardan to'g'ri foydalanish.

---

## Dars maqsadi

Bu dars oxirida o'quvchi:

- Tuple va Set strukturalarini to'g'ri e'lon qilish;
- Tuple immutability tamoyilini tushunish va qo'llash;
- Set yordamida duplikatsiyalarni olib tashlash;
- Matematik to'plam operatsiyalarini kodda yozish;
- Har bir holat uchun mos ma'lumot strukturasini tanlay olish

ni mustaqil bajara oladi.

---

## Kerakli oldingi bilimlar

- 11-dars: List asoslari;
- 4-dars: Stringlar va immutability;
- 2-dars: O'zgaruvchilar va turlar.

---

# 1. Asosiy tushunchalar va atamalar

## Tuple nima?

> **Tuple** — o'zgarmas (immutable), tartiblangan elementlar to'plami. Oddiy qavslar `()` ichida yoziladi: `koordinata = (41.2995, 69.2401)`.

## Set nima?

> **Set** — tartibsiz (unordered), takrorlanmas (unique) va o'zgaruvchan elementlar to mezonidir. Jingalak qavslar `{}` ichida yoziladi: `to'plam = {1, 2, 3}`.

## Unpacking nima?

> **Unpacking** — Tuple yoki List ichidagi qiymatlarni alohida o'zgaruvchilarga bir vaqtning o'zida biriktirish jarayoni: `x, y = (10, 20)`.

## Immutability nima?

> **Immutability** — obyekt yaratilgandan so'ng uning ichki holati va qiymatlarini o'zgartirib bo'lmasligi.

---

# 2. Sintaksis va uning izohi

```python
# Tuple e'lon qilish
nuqta = (10, 20)
bitta_element = (5,)  # Vergul shart!

# Set e'lon qilish
mevalar = {"olma", "banan", "uzum"}
bo_sh_set = set()  # {} yozilsa dict bo'lib qoladi!
```

---

# 3. Tuple va Set taqqoslash jadvali

| Xususiyat | List `[]` | Tuple `()` | Set `{}` |
|---|---|---|---|
| Tartiblangan (Ordered) | Ha | Ha | Yo'q |
| O'zgaruvchan (Mutable) | Ha | Yo'q | Ha |
| Takrorlanish (Duplicates) | Ruxsat berilgan | Ruxsat berilgan | **Ruxsat berilmagan** |
| Indekslash (Indexing) | `list[0]` | `tuple[0]` | Qo'llab-quvvatlanmaydi |
| Tezlik & Xotira | O'rtacha | **Juda tez & Kam xotira** | **Qidiruv juda tez O(1)** |

---

# 4. Kod misollari

## Misol 1 — Tuple yaratish va indekslash

```python
ranglar = ("qizil", "yashil", "ko'k")
print(ranglar[0])
print(ranglar[-1])
print(len(ranglar))
```

Natija:
```
qizil
ko'k
3
```

Qatorma-qator izoh:
- `ranglar[0]` — Tuple'ning birinchi elementini oladi;
- Tuple indeksatsiyasi List bilan bir xil ishlaydi.

---

## Misol 2 — Tuple Unpacking (Qiymatlarni ajratish)

```python
talaba = ("Ali", 21, "Dasturlash")
ism, yosh, yo_nalish = talaba

print(f"Ism: {ism}, Yosh: {yosh}, Yo'nalish: {yo_nalish}")
```

Natija:
```
Ism: Ali, Yosh: 21, Yo'nalish: Dasturlash
```

---

## Misol 3 — Set va takrorlanmaslik xususiyati

```python
sonlar = [1, 2, 2, 3, 4, 4, 4, 5]
noyob_sonlar = set(sonlar)

print("Asl list:", sonlar)
print("Noyob set:", noyob_sonlar)
```

Natija:
```
Asl list: [1, 2, 2, 3, 4, 4, 4, 5]
Noyob set: {1, 2, 3, 4, 5}
```

---

## Misol 4 — Set metodlari (add, remove, discard)

```python
tillar = {"Python", "Java"}
tillar.add("C++")
tillar.discard("Java") # Topilmasa ham xato bermaydi

print(tillar)
```

Natija:
```
{'Python', 'C++'}
```

---

## Misol 5 — Set amallari (Birlashma va Kesishma)

```python
frontend = {"HTML", "CSS", "JavaScript", "React"}
backend = {"Python", "Django", "JavaScript", "PostgreSQL"}

birgalikda = frontend.union(backend) # yoki frontend | backend
ortaq = frontend.intersection(backend) # yoki frontend & backend

print("Barcha texnologiyalar:", birgalikda)
print("Umumiy texnologiya:", ortaq)
```

Natija:
```
Barcha texnologiyalar: {'HTML', 'CSS', 'JavaScript', 'React', 'Python', 'Django', 'PostgreSQL'}
Umumiy texnologiya: {'JavaScript'}
```

---

## Misol 6 — Set amallari (Farq - Difference)

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

faqat_a = a.difference(b) # a - b
print("Faqat A da bor:", faqat_a)
```

Natija:
```
Faqat A da bor: {1, 2}
```

---

## Misol 7 — Tuple immutable ekanligini isbotlash

```python
koordinata = (41.2995, 69.2401)
try:
    koordinata[0] = 40.0
except TypeError as e:
    print("Xatolik ushlandi:", e)
```

Natija:
```
Xatolik ushlandi: 'tuple' object does not support item assignment
```

---

## Misol 8 — Frozenset (O'zgarmas Set)

```python
turgun_to_plam = frozenset([1, 2, 3, 3])
print(turgun_to_plam)
# turgun_to_plam.add(4) -> AttributeError beradi!
```

Natija:
```
frozenset({1, 2, 3})
```

---

# 5. Real loyiha misoli — Tizim foydalanuvchilari huquqini tekshirish

```python
# Tizimdagi rollar va ularning huquqlari (Set yordamida)
admin_huquqlari = {"read", "write", "delete", "execute"}
user_huquqlari = {"read", "write"}

# Foydalanuvchi sinovi
joriy_huquqlar = user_huquqlari.copy()

# Tekshirish
talab_qilingan = "delete"

if talab_qilingan in joriy_huquqlar:
    print("Amal bajarildi: O'chirildi.")
else:
    print(f"Ruxsat yo'q! '{talab_qilingan}' huquqi yetishmaydi.")
```

---

# 6. Ko'p uchraydigan xatolar

## Xato 1: Bitta elementli Tuple yaratishda vergulni unutish

Noto'g'ri:
```python
x = (5) # Bu int turi bo'lib qoladi!
print(type(x)) # <class 'int'>
```

To'g'ri:
```python
x = (5,)
print(type(x)) # <class 'tuple'>
```

## Xato 2: Bo'sh Set yaratishda {} ishlatish

Noto'g'ri:
```python
s = {} # Bu dict yaratadi!
print(type(s)) # <class 'dict'>
```

To'g'ri:
```python
s = set()
print(type(s)) # <class 'set'>
```

---

# 7. Sinfdagi amaliy topshiriqlar

1. **Oson**: 5 ta mevadan iborat Tuple yarating va 2-elementni ekranga chiqaring.
2. **O'rta**: Berilgan listdagi takrorlangan elementlarni Set yordamida tozalab, yana qayta List holatiga keltiring.
3. **Murakkab**: Ikki guruh talabalari ro'yxatidan faqat ikkala guruhda ham qatnashadigan talabalarni toping.

---

# 8. Uyga vazifa

1. Foydalanuvchi kiritgan matndagi barcha noyob harflarni aniqlovchi dastur yozing.
2. 3 ta Tuple elementini qabul qilib ularni bitta Tuple ga birlashtiring.
3. Set amallari yordamida ikki ro'yxat orasidagi faqat birida uchraydigan elementlarni (Symmetric Difference) toping.

---

# 9. Tekshirish savollari

1. Tuple va List orasidagi 2 ta asosiy farq nima?
2. Set ichida nima uchun bir xil element saqlanmaydi?
3. Bitta elementli Tuple qanday e'lon qilinadi?
4. `set.discard()` va `set.remove()` farqi nimada?
5. `frozenset` nima?

---

## Javoblar

1. List o'zgaruvchan (mutable) va sekinroq, Tuple o'zgarmas (immutable) va xotiradan samarali foydalanadi.
2. Set matematik to'plam bo'lib, uning barcha elementlari unikal bo'lishi shart.
3. Elementdan so'ng vergul qo'yish orqali: `(1,)`.
4. `remove()` element topilmasa `KeyError` beradi, `discard()` esa indamay o'tib ketadi.
5. `frozenset` — bu Set'ning o'zgarmas (immutable) variantidir.

---

# 10. Qisqa xulosa

Bu darsda Tuple va Set ma'lumot turlari, ularning o'ziga xos xususiyatlari, o'zgarmaslik (immutability), duplikatsiyalardan xalos bo'lish hamda to'plamlar ustida matematik amallar bajarish o'rganildi.
