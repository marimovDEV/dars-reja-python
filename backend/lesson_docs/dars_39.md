# 📦 39. Virtual Environment va pip — Dars dokumentatsiyasi

Har bir Python loyihasi har xil tashqi kutubxonalarga va hatto u kutubxonalarning har xil versiyalariga bog'liq bo'lishi mumkin. Masalan, 1-loyiha `Django 4.2` ishlatishi, 2-loyiha esa `Django 5.0` ishlatishi mumkin. 

Kutubxonalarni kompyuterga global o'rnatish loyihalar o'rtasida **versiyalar toqnashuviga (dependency conflict)** olib keladi.

**Virtual Environment (`venv`)** — bu har bir loyiha uchun alohida, izolyatsiyalangan (ajratilgan) Python muhitini yaratish vositasidir. **`pip`** esa Python uchun paket va kutubxonalarni o'rnatuvchi menejerdir.

---

## Bu mavzu orqali nimalar qilish mumkin

- Har bir loyiha uchun alohida `venv` yaratish va uni faollashtirish (activate);
- `pip` yordamida tashqi kutubxonalarni o mezon qilish, yangilash va o'chirish;
- `requirements.txt` fayli orqali loyiha bog'liqliklarini eksport va import qilish.

---

# Asosiy Buyruqlar

```bash
# 1. Virtual Muhit yaratish
python -m venv venv

# 2. Muhitni faollashtirish (Activate)
# Mac/Linux:
source venv/bin/activate
# Windows:
# venv\Scriptsctivate

# 3. Paket o'rnatish
pip install django

# 4. Bog'liqliklar ro'yxatini faylga saqlash
pip freeze > requirements.txt

# 5. Boshqa kompyuterda fayldan o'rnatish
pip install -r requirements.txt
```

---

# 10. Qisqa xulosa

Bu darsda izolyatsiyalangan virtual muhit (`venv`), paketlar menejeri (`pip`) va `requirements.txt` bilan ishlash o'rganildi.
