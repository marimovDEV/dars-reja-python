# 🔄 32. SQLite CRUD Amallari — Dars dokumentatsiyasi

Ma'lumotlar bazasi bilan ishlashning 4 ta asosiy ustuni bor, ular **CRUD** deb ataladi:
- **C**reate (`INSERT`) — Yangi ma'lumot qo'shish.
- **R**ead (`SELECT`) — Ma'lumotlarni o'qish va qidirish.
- **U**pdate (`UPDATE`) — Mavjud ma'lumotlarni yangilash.
- **D**elete (`DELETE`) — Ma'lumotlarni o'chirish.

Ushbu darsda siz Python `sqlite3` moduli yordamida bazaga xavfsiz (SQL Injection xavfisiz) ma mezon qo'shish, o'qish va o'zgartirishni o'rganasiz.

---

## Bu mavzu orqali nimalar qilish mumkin

- `INSERT INTO` orqali jadvalga yangi yozuvlar qo'shish;
- `SELECT` so'rovi yordamida `fetchall()` va `fetchone()` bilan ma'lumotlarni o'qish;
- `WHERE` sharti bilan ma'lumotlarni filtrlash;
- `UPDATE` va `DELETE` buyruqlarini xavfsiz parametrlar (`?`) bilan bajarish.

---

## Dars maqsadi

Bu dars oxirida o'quvchi:

- CRUD konseptsiyasini amalda qo'llash;
- SQL Injection xavfsizligi parametrli so'rovlardan (`?`) foydalanish;
- Python va SQLite o mezonida to'liq amaliyot bajarish

ni mustaqil bajara oladi.

---

## Kerakli oldingi bilimlar

- 31-dars: SQL va SQLite kirish.

---

# 1. CRUD va SQL Buyruqlari Jadvali

| Operatsiya | SQL Buyrug'i | Python Metodi |
|---|---|---|
| **Create** | `INSERT INTO table (col) VALUES (?)` | `cursor.execute()`, `conn.commit()` |
| **Read** | `SELECT * FROM table WHERE condition` | `cursor.fetchall()`, `cursor.fetchone()` |
| **Update** | `UPDATE table SET col = ? WHERE id = ?`| `cursor.execute()`, `conn.commit()` |
| **Delete** | `DELETE FROM table WHERE id = ?` | `cursor.execute()`, `conn.commit()` |

---

# 2. Kod misollari

## Misol 1 — INSERT va SELECT (Ma'lumot qo'shish va o'qish)

```python
import sqlite3

conn = sqlite3.connect("test.db")
cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)")

# INSERT (Parametrli xavfsiz usul)
cursor.execute("INSERT INTO users (name) VALUES (?)", ("Ali",))
conn.commit()

# SELECT
cursor.execute("SELECT * FROM users")
users = cursor.fetchall()

print("Foydalanuvchilar:", users)
conn.close()
```

---

## Misol 2 — UPDATE va DELETE

```python
import sqlite3

conn = sqlite3.connect("test.db")
cursor = conn.cursor()

# Update
cursor.execute("UPDATE users SET name = ? WHERE id = ?", ("Ali Valiyev", 1))

# Delete
cursor.execute("DELETE FROM users WHERE id = ?", (2,))

conn.commit()
conn.close()
```

---

# 10. Qisqa xulosa

Bu darsda SQLite bazasida to'liq CRUD amallari va parametrli SQL so'rovlari o'rganildi.
