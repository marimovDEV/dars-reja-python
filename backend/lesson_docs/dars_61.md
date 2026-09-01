# ⚡ 61. Asinxron Python (asyncio) — Dars dokumentatsiyasi

Standart Python kodi **sinxron (synchronous)** ishlaydi, ya'ni bitta operatsiya (masalan, tarmoq so'rovi yoki fayldan o'qish) tugamaguncha keyingi kod kutib turadi (blocking I/O).

**Asinxron Dasturlash (`asyncio`)** — bu vaqt oluvchi I/O operatsiyalari (Network, Database, File) bajarilayotganda protsessor vaqtini zoye ketkazmasdan, boshqa vazifalarni parallel ravishda bajarish imkonini beruvchi texnologiyadir.

Python 3.5+ versiyalarida asinxronlik **`async`** va **`await`** kalit so'zlari hamda **Event Loop (Hodisalar Sikli)** orqali amalga oshiriladi.

---

## Bu mavzu orqali nimalar qilish mumkin

- Sinxron (blocking) va Asinxron (non-blocking) kod o'rtasidagi farqni tushunish;
- `async def` yordamida korutinalar (coroutines) yaratish;
- `await` yordamida asinxron operatsiyalarni kutish;
- `asyncio.gather()` orqali yuzlab tarmoq so'rovlarini bir vaqtda parallel bajarish.

---

# Kod misoli — asyncio bilan Parallel So'rovlar

```python
import asyncio
import time

async def fetch_data(id, delay):
    print(f"Task {id} boshlandi...")
    await asyncio.sleep(delay) # Non-blocking sleep
    print(f"Task {id} tugadi!")
    return f"Natija {id}"

async def main():
    # Parallel bajarish
    results = await asyncio.gather(
        fetch_data(1, 2),
        fetch_data(2, 3),
        fetch_data(3, 1)
    )
    print("Barcha natijalar:", results)

start = time.time()
asyncio.run(main())
print(f"Jami ketgan vaqt: {time.time() - start:.2f} soniya") # 3 soniya (sinxron bo'lsa 6 sec bo'lardi)
```

---

# 10. Qisqa xulosa

Bu darsda Asinxron dasturlash, Event Loop, `async/await` va `asyncio` moduli o'rganildi.
