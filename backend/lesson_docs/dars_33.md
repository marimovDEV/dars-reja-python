# 🔗 33. SQL So'rovlar va Munosabatlar (Relationships) — Dars dokumentatsiyasi

Relatsion ma'lumotlar bazasining asosiy kuchi — jadvallar o'rtasidagi **Munosabatlar (Relationships)** va murakkab **So'rovlar (Queries)** yozish imkoniyatidadir.

Jadvallarni bir-biriga bog'lash uchun **Foreign Key (Tashqi Kalit)** va jadvallarni birlashtirib o'qish uchun **`JOIN`** operatorlari ishlatiladi.

---

## Bu mavzu orqali nimalar qilish mumkin

- Jadvallar o'rtasidagi bog'liqlik turlarini (`One-to-Many`, `Many-to-Many`) tushunish;
- `FOREIGN KEY` yordamida jadvallarni bog'lash;
- `INNER JOIN`, `LEFT JOIN` yordamida birlashgan so'rovlar yozish;
- `ORDER BY`, `GROUP BY`, `LIMIT` bilan saralash va guruhlash.

---

# 1. SQL Munosabatlar Turlari

1. **One-to-Many (Birga Ko'p)**: Masalan, Bitta Avtor -> Ko'plab Kitoblar.
2. **Many-to-Many (Ko'pga Ko'p)**: Masalan, Talabalar va Kurslar (O'rtada ulovchi jadval kerak).

---

# 2. Kod misoli — Foreign Key va JOIN

```python
import sqlite3

conn = sqlite3.connect("school.db")
cursor = conn.cursor()

# Otalar va Bolalar jadvallari
cursor.execute("CREATE TABLE IF NOT EXISTS authors (id INTEGER PRIMARY KEY, name TEXT)")
cursor.execute("CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, title TEXT, author_id INTEGER)")

# JOIN So'rovi
query = "SELECT books.title, authors.name FROM books JOIN authors ON books.author_id = authors.id"

cursor.execute(query)
print(cursor.fetchall())
conn.close()
```

---

# 10. Qisqa xulosa

Bu darsda SQL jadvallarini bog'lash (Foreign Key) va `JOIN` operatsiyalari o'rganildi.
