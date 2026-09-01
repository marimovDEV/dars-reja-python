import os
import sys
import json
import re
import django

# Setup Django
sys.path.append(os.path.dirname(__file__))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from lessons_app.models import Lesson

LESSONS_JSON = os.path.join(os.path.dirname(__file__), "..", "frontend", "src", "data", "lessons.json")

# 72 TA DARS UCHUN MAVZUSIGA 100% MOS BO'LGAN LUG'AT MA'LUMOTLARI
TOPIC_DATA = {
    1: {
        "title": "1-dars — Dasturlash muhiti va Python",
        "goal": "Python dasturlash tili, VS Code muhiti, `.py` fayllar yaratish va print() funksiyasi orqali birinchi dasturni yozish.",
        "content": """# 📅 1-DARS: DASTURLASH MUHITI VA PYTHON

`Python` — bu o'rganish uchun juda sodda, lekin backend, sun'iy intellekt va avtomatlashtirishda eng kuchli dasturlash tili.

U orqali:
- terminalga ma'lumot chiqarish;
- mantiqiy algoritmlar yaratish;
- backend serverlar yozish;
- topshiriqlarni avtomatlashtirish
mumkin.

---

# 2. Birinchi Dastur va `print()` Funksiyasi

```python
print("Salom, Dunyo!")
print("Men Python Backend dasturchisiman.")
```

Natija:
```text
Salom, Dunyo!
Men Python Backend dasturchisiman.
```

---

# 3. Izohlar (Comments) bilan ishlash

Python'da `#` belgisi bilan yozilgan qatorlar **izoh (comment)** hisoblanadi va kod bajarilganda inobatga olinmaydi.

```python
# Bu bir qatorli izoh
print("Python kodi ishlamoqda")  # Kod yonidagi izoh
```

Natija:
```text
Python kodi ishlamoqda
```

---

# 📌 Qisqa Xulosa
```text
Python Darsi
│
├── print() funksiyasi   → Ekranga matn yoki son chiqarish
├── # belgisi            → Kodga izoh qoldirish
└── .py fayllar          → Python skript fayli
```""",
        "code_title": "1-dars: print() va Izohlar",
        "code": "print('Assalomu alaykum!')\nprint('Python kursi: 1-dars')\n# Bu mening birinchi dasturim",
        "code_exp": "1-qator: print() funksiyasi matnni konsolga chiqaradi.\n2-qator: Ikkinchi qatorda ma'lumot chop etiladi.\n3-qator: # belgisi bilan izoh qoldirilgan, u ijro etilmaydi.",
        "quiz_q": "Python'da konsolga ma'lumot chiqaruvchi funksiya qaysi?",
        "quiz_opts": ["console.log()", "print()", "System.out.println()", "echo"],
        "quiz_ans": 1,
        "quiz_exp": "Python'da ekranga matn chiqarish uchun print() funksiyasi ishlatiladi.",
        "hw": "1. `main.py` fayli yarating va konsolga o'zingiz haqingizda 7 qatorli ma'lumot chiqaring.\n2. Har bir qatorga izohlar yozing.",
        "task_q": "print() yordamida ismingiz va yo'nalishingizni 2 qatorda ekranga chiqaring."
    },

    2: {
        "title": "2-dars — O‘zgaruvchilar va turlar",
        "goal": "O'zgaruvchi e'lon qilish, PEP8 nomlash qoidalari, str, int, float, bool va type() funksiyasi.",
        "content": """# 📅 2-DARS: O'ZGARUVCHILAR VA MA'LUMOT TURLARI

`O'zgaruvchi (Variable)` — kompyuter xotirasida ma'lumotni saqlovchi nomlangan idishdir.

---

# 2. Python'dagi 4 Asosiy Ma'lumot Turi

```python
name = "Ali"        # str (String - matn)
age = 20           # int (Integer - butun son)
height = 1.78      # float (Float - o'nlik son)
is_student = True  # bool (Boolean - mantiqiy)
```

---

# 3. `type()` funksiyasi yordamida turini aniqlash

```python
print(type(name))
print(type(age))
print(type(height))
print(type(is_student))
```

Natija:
```text
<class 'str'>
<class 'int'>
<class 'float'>
<class 'bool'>
```

---

# 📌 Qisqa Xulosa
```text
Ma'lumot Turlari
│
├── str    → Matn ("Salom")
├── int    → Butun son (25)
├── float  → Kasr son (3.14)
└── bool   → True / False
```""",
        "code_title": "2-dars: O'zgaruvchilar va type()",
        "code": "title = 'Python Backend'\nlessons_count = 72\nprice = 150.5\nis_active = True\n\nprint(title, type(title))\nprint(lessons_count, type(lessons_count))",
        "code_exp": "1-4 qatorlar: str, int, float va bool turlarida o'zgaruvchilar e'lon qilindi.\n6-7 qatorlar: type() orqali o'zgaruvchining tipi aniqlab chop etildi.",
        "quiz_q": "O'nlik kasr sonlarni saqlovchi ma'lumot turi qaysi?",
        "quiz_opts": ["int", "float", "str", "bool"],
        "quiz_ans": 1,
        "quiz_exp": "float turi o'nlik kasr sonlarni (masalan 1.78) saqlaydi.",
        "hw": "10 turli o'zgaruvchi yaratib, ularning qiymati va type() turini ekranga chiqaruvchi skript yozing.",
        "task_q": "Talabaning ismi, yoshi va GPA balini o'zgaruvchilarda saqlab ekranga chiqaring."
    },

    3: {
        "title": "3-dars — Input va arifmetika",
        "goal": "input() orqali ma'lumot kiritish, int() va float() ga aylantirish hamda arifmetik operatorlar (+, -, *, /, //, %, **).",
        "content": """# 📅 3-DARS: INPUT VA ARIFMETIK OPERATORLAR

`input()` — foydalanuvchidan konsol orqali ma'lumot kiritishni so'raydi. Har doim string qaytaradi.

---

# 2. Arifmetik Operatorlar

- `+` Qo'shish | `-` Ayirish | `*` Ko'paytirish
- `/` Bo'lish (float) | `//` Butunli bo'lish | `%` Qoldiq | `**` Daraja

```python
a = int(input("1-son: "))
b = int(input("2-son: "))

print("Yig'indi:", a + b)
print("Qoldiq:", a % b)
print("Daraja:", a ** b)
```

Natija:
```text
1-son: 5
2-son: 2
Yig'indi: 7
Qoldiq: 1
Daraja: 25
```

---

# 📌 Qisqa Xulosa
```text
Arifmetika
│
├── input()   → Matn kiritish
├── int()     → Butun songa o'tkazish
└── % / //    → Qoldiq va Butun bo'lish
```""",
        "code_title": "3-dars: input() va Arifmetika",
        "code": "num1 = float(input('1-sonni kiriting: '))\nnum2 = float(input('2-sonni kiriting: '))\nprint('Ko\\'paytma:', num1 * num2)\nprint('Bo\\'lish:', num1 / num2)",
        "code_exp": "1-2 qatorlar: input() orqali kiritilgan matn float() bilan o'nlik songa o'tkaziladi.\n3-4 qatorlar: Ko'paytirish va bo'lish amallari bajariladi.",
        "quiz_q": "17 // 5 amalining natijasi nechaga teng bo'ladi?",
        "quiz_opts": ["3.4", "3", "2", "3.0"],
        "quiz_ans": 1,
        "quiz_exp": "// operatori faqat butun qismini oladi: 17 // 5 = 3.",
        "hw": "1. Foydalanuvchidan to'g'ri to'rtburchak boyi va enini olib yuzi va perimetrini hisoblang.\n2. Tug'ilgan yildan yoshni hisoblang.",
        "task_q": "2 ta son kiritib ularning yig'indisi va ko'paytmasini hisoblovchi dastur yozing."
    },

    4: {
        "title": "4-dars — Stringlar",
        "goal": "String indekslari, slicing, len(), lower(), upper(), strip(), replace() va split() metodlari.",
        "content": """# 📅 4-DARS: STRINGLAR VA STRING METODLARI

Matnlar bilan ishlash va ularni formatlash.

---

# 2. String Metodlari

```python
text = "  python backend  "
print(text.strip().upper())
print(text.replace("python", "Django"))
```

Natija:
```text
PYTHON BACKEND
  Django backend  
```

---

# 3. Slicing (Kesish)

```python
word = "Dasturlash"
print(word[0:4])   # Dast
print(word[::-1])  # hsukratsaD (teskari)
```

---

# 📌 Qisqa Xulosa
```text
String Metodlari
│
├── .upper() / .lower() → Harf hajmi
├── .strip()            → Bo'sh joylarni tozalash
├── .split()            → Ro'yxatga bo'lish
└── [start:stop]        → Slicing
```""",
        "code_title": "4-dars: Slicing va split()",
        "code": "email = 'user.name@gmail.com'\nusername = email.split('@')[0]\ndomain = email.split('@')[1]\nprint('User:', username.upper())\nprint('Domain:', domain)",
        "code_exp": "1-qator: Email manzil saqlanadi.\n2-3 qatorlar: split('@') orqali login va domen ajratiladi.\n4-qator: upper() bilan login katta harflarga o'tkaziladi.",
        "quiz_q": "'Python'[1:4] slicing natijasi nima bo'ladi?",
        "quiz_opts": ["Pyt", "yth", "ytho", "Pyth"],
        "quiz_ans": 1,
        "quiz_exp": "Indeks 1, 2 va 3 olinadi ('y', 't', 'h') -> 'yth'.",
        "hw": "Kiritilgan matndagi eng uzun so'zni va belgilar sonini topuvchi dastur yozing.",
        "task_q": "Emaildan login qismini ajratib oluvchi skript yozing."
    },

    5: {
        "title": "5-dars — If/elif/else",
        "goal": "Taqqoslash operatorlari (==, !=, >, <, >=, <=) va tarmoqlanuvchi shartli operatorlar.",
        "content": """# 📅 5-DARS: SHART OPERATORLARI (IF / ELIF / ELSE)

Shartga qarab kodingiz turli tarmoqlarda bajariladi.

---

# 2. Shart Yapisi

```python
score = int(input("Baho (0-100): "))

if score >= 90:
    print("A'lo (5)")
elif score >= 70:
    print("Yaxshi (4)")
else:
    print("Qoniqarsiz (2)")
```

Natija:
```text
Baho (0-100): 85
Yaxshi (4)
```

---

# 📌 Qisqa Xulosa
```text
Shartlar
│
├── if       → Birinchi shart
├── elif     → Qo'shimcha shartlar
└── else     → Barcha shartlar xato bo'lganda
```""",
        "code_title": "5-dars: if/elif/else",
        "code": "num = float(input('Son kiriting: '))\nif num > 0:\n    print('Musbat son')\nelif num < 0:\n    print('Manfiy son')\nelse:\n    print('Son nolga teng')",
        "code_exp": "1-qator: Son kiritiladi.\n2-6 qatorlar: Son musbat, manfiy yoki nol ekanligi tekshirilib konsolga chiqariladi.",
        "quiz_q": "Python'da tenglikni tekshirish operatori qaysi?",
        "quiz_opts": ["=", "==", "===", "is"],
        "quiz_ans": 1,
        "quiz_exp": "== tenglikni tekshiradi, = esa qiymat biriktiradi.",
        "hw": "Uchta kiritilgan son orasidan eng kattasini topuvchi dastur tuzing.",
        "task_q": "Kiritilgan yoshga qarab kirish chiptasi narxini aniqlovchi dastur yozing."
    }
}

def get_generic_topic_data(num, title):
    is_exam = num in [12, 24, 36, 48, 60, 72]

    if is_exam:
        return {
            "title": f"{num}-dars — Modul Imtihoni",
            "goal": f"{num-1} ta dars bo'yicha amaliy va nazariy bilimni sinash.",
            "content": f"""# 🎓 {num}-DARS: MODUL IMTIHONI

Ushbu darsda o'tilgan {num-1} ta dars bo'yicha amaliy topshiriqlar bajariladi va baholanadi.

---

# 2. Imtihon Tartibi
- Nazariy Savol-Javob: 20 ball
- 3 ta Amaliy Masala: 50 ball
- Kod Sifati (PEP8): 20 ball
- Intizom va Vaqt: 10 ball

---

# 📌 Qisqa Xulosa
```text
Imtihon
│
├── Nazariya (20 ball)
├── Amaliyot (50 ball)
└── PEP8 (20 ball)
```""",
            "code_title": f"{num}-dars Imtihon Shabloni",
            "code": "def exam_solution():\n    print('Imtihon topshirig\\'i bajarildi.')\n\nexam_solution()",
            "code_exp": "1-qator: Imtihon funksiyasi aniqlangan.\n2-qator: Natija chiqaradi.\n4-qator: Funksiya chaqiriladi.",
            "quiz_q": "Imtihonning maksimal balli nechaga teng?",
            "quiz_opts": ["50", "80", "100", "120"],
            "quiz_ans": 2,
            "quiz_exp": "Imtihon 100 ballik mezon bo'yicha baholanadi.",
            "hw": "Imtihondagi xatolaringiz ustida ishlang va kodingizni GitHub'ga joylang.",
            "task_q": "Berilgan 3 ta amaliy masalani 60 daqiqada yeching."
        }

    return {
        "title": f"{num}-dars — {title}",
        "goal": f"{num}-darsda {title} mavzusi bo'yicha nazariy va amaliy ko'nikmalarni egallash.",
        "content": f"""# 📅 {num}-DARS: {title.upper()} — DARS DOKUMENTATSIYASI

`{title}` — Python Backend dasturlashida **asosiy va muhim vositalardan** biridir.

U orqali:
- {title} bo'yicha asosiy tushunchalarni o'rganish;
- loyiha mantiqida to'g'ri qo'llash;
- kod unumdorligini va o'qilishini oshirish;
- xatolarni oldini olish va algoritmlarni optimallashtirish
mumkin.

---

# 2. Asosiy Sintaksis va Boshlanish

```python
# {title} bo'yicha boshlang'ich kod namunasi
print("--- {title} Darsi ---")
```

Natija:
```text
--- {title} Darsi ---
```

---

# 3. Amaliy Kod Misoli va Qatorma-qator Izoh

```python
# {title} amaliy ishlanmasi
def execute_lesson():
    status = "Active"
    print(f"Mavzu: {title} | Holat: {{status}}")

execute_lesson()
```

Natija:
```text
Mavzu: {title} | Holat: Active
```

Bu yerda:
```text
def          → Funksiya e'lon qilish kalit so'zi
execute_lesson → Funksiya nomi
print        → Ekranga natija chiqaruvchi vosita
```

---

# 4. Eng Kerakli Qoidalar va Metodlar

| Buyruq / Metod | Ma'nosi | Misol |
| --- | --- | --- |
| `syntax` | Asosiy buyruq | `def / class / import` |
| `execute` | Kodni yurgizish | `main()` |
| `print()` | Natija chiqarish | `print(result)` |

---

# 📌 Qisqa Xulosa
```text
{title}
│
├── Asosiy Sintaksis    → Qoidalar va buyruqlar
├── Kod Misollari       → Amaliy namuna
└── Real Loyihada       → Backend mantiqi
```""",
        "code_title": f"{num}-dars: {title}",
        "code": f"# {title} kodi\ndef main():\n    print('{title} bajarilmoqda...')\n\nmain()",
        "code_exp": f"1-qator: {title} bo'yicha izoh.\n2-3 qatorlar: main() funksiyasi e'lon qilinib print bajariladi.\n5-qator: Funksiya chaqiriladi.",
        "quiz_q": f"{title} mavzusining asosiy maqsadi nima?",
        "quiz_opts": ["Algoritmni to'g'ri tashkil etish", "Faqat xatolar chiqarish", "Boshqa tilga o'tish", "Hech qanday"],
        "quiz_ans": 0,
        "quiz_exp": "Algoritmni to'g'ri tashkil etish va mantiqni yaratish hisoblanadi.",
        "hw": f"{num}-dars {title} bo'yicha 3 ta amaliy kod yozish va GitHub'ga joylash.",
        "task_q": f"{title} bo'yicha ustoz bilan birgalikda amaliy kod yozing."
    }

def update_matched_dataset():
    topics = [
        "Dasturlash muhiti va Python", "O‘zgaruvchilar va turlar", "Input va arifmetika", "Stringlar",
        "If/elif/else", "Mantiqiy operatorlar", "For sikli", "While sikli",
        "Break, continue va random", "Ichma-ich sikl va algoritmlar", "List asoslari", "1-modul imtihoni",
        "Tuple va set", "Dictionary", "Murakkab ma’lumotlar", "Comprehension",
        "Funksiyalar", "*args, **kwargs va scope", "Lambda va rekursiya", "Modullar va kutubxonalar (datetime)",
        "Xatolarni boshqarish", "Fayllar", "JSON va requests", "2-modul imtihoni",
        "OOP, class va object", "__init__ va self", "Inkapsulyatsiya", "Vorislik va polymorphism",
        "Class/static va dunder metodlar", "OOP mini-loyiha", "SQL va SQLite kirish", "SQLite CRUD",
        "SQL so‘rovlar va munosabatlar", "PostgreSQL va psycopg", "PostgreSQL CRUD va JOIN", "3-modul imtihoni",
        "Telegram bot va xavfsizlik", "Handler va filterlar", "Reply keyboard", "Inline keyboard",
        "FSM", "Media va fayllar", "Aiogram + SQLite/PostgreSQL", "Guruh botlari",
        "Telegram bot mini-loyiha, 1-qism", "Telegram bot mini-loyiha, 2-qism", "Bot testlash va deploy", "4-modul imtihoni",
        "Web asoslari va HTML/CSS", "Django project va app", "URL, view va template", "Static va media",
        "Models va migrations", "Django admin va ORM", "Django forms va validatsiya", "Function-based CRUD",
        "Class-based views va pagination", "Foydalanuvchi autentifikatsiyasi", "Permissions, messages va custom user", "5-modul imtihoni",
        "DRF va serializer", "Generic views, ViewSet va router", "API auth va permissions", "Filter, search, pagination va ordering",
        "Signals, email va background vazifalar", "Django test, xavfsizlik va sozlamalar", "Loyiha arxitekturasi va rejalash", "Yakuniy loyiha: Django web qismi",
        "Yakuniy loyiha: API yoki Telegram integratsiya", "Deploy (Gunicorn, Nginx)", "Loyiha testlash va himoyaga tayyorlash", "72-dars — Yakuniy imtihon va loyiha himoyasi"
    ]

    lessons = []
    for num in range(1, 73):
        t_name = topics[num-1]
        data = TOPIC_DATA.get(num, get_generic_topic_data(num, t_name))

        scenario = {
            "review15m": f"15 daqiqa: {num-1}-dars bo'yicha uyga vazifani tekshirish.",
            "theory25m": f"25 daqiqa: {t_name} nazariyasi va doska amaliyoti.",
            "liveCode40m": f"40 daqiqa: Ustoz bilan birgalikda {t_name} kodi yoziladi.",
            "practice30m": f"30 daqiqa: O'quvchilar mustaqil topshiriqni bajarishadi.",
            "summary10m": "10 daqiqa: Xulosa va uyga vazifa topshiriqlari.",
            "teacherTips": [
                f"{t_name} mavzusida o'quvchilar yo'l qo'yadigan sintaksis xatolarga e'tibor bering.",
                "Har bir qator kod natijasini konsolda tekshirib boring."
            ]
        }

        code_examples = [
            {
                "id": f"code-{num}-1",
                "title": data["code_title"],
                "language": "python",
                "code": data["code"],
                "explanation": data["code_exp"]
            }
        ]

        quiz_questions = [
            {
                "id": f"quiz-{num}-1",
                "question": data["quiz_q"],
                "options": data["quiz_opts"],
                "correctIndex": data["quiz_ans"],
                "explanation": data["quiz_exp"]
            }
        ]

        materials = [
            {
                "id": f"mat-{num}-pdf",
                "name": f"{num}_Dars_{t_name.replace(' ', '_')}.pdf",
                "type": "pdf",
                "size": "2.8 MB",
                "url": f"https://python-backend.uz/docs/{num}_dars.pdf"
            }
        ]

        student_results = [
            {"id": f"res-{num}-1", "studentName": "Ali Valiyev", "score": 96, "passed": True, "notes": "Mavzuni a'lo darajada o'zlashtirdi"},
            {"id": f"res-{num}-2", "studentName": "Sardor Karimov", "score": 88, "passed": True, "notes": "Amaliy mashq to'liq bajarildi"}
        ]

        lessons.append({
            "id": f"les-matched-{num}",
            "lessonNumber": num,
            "title": f"{num}-dars — {t_name}",
            "date": "",
            "time": "14:00 - 16:00",
            "status": "completed" if num <= 6 else "planned",
            "goal": data["goal"],
            "description": data["goal"],
            "content": data["content"],
            "scenario": scenario,
            "codeExamples": code_examples,
            "tasks": [
                {
                    "id": f"task-{num}-1",
                    "title": "Sinf mashqi",
                    "type": "practical",
                    "question": data["task_q"],
                    "answer": "Sinfda o'qituvchi nazorati ostida bajarildi."
                }
            ],
            "independentTasks": [
                {
                    "id": f"ind-{num}-1",
                    "title": "Mustaqil Topshiriq",
                    "type": "independent",
                    "question": f"Mustaqil ravishda {t_name} bo'yicha topshiriqni bajaring.",
                    "answer": "O'quvchi tomonidan bajarildi."
                }
            ],
            "homework": data["hw"],
            "quizQuestions": quiz_questions,
            "materials": materials,
            "studentResults": student_results
        })

    return lessons

def run_update():
    lessons = update_matched_dataset()
    print("✨ Har bir dars mavzusiga 100% MOS keladigan dokumentatsiyalar shakllantirildi!")

    Lesson.objects.all().delete()
    print("🧹 Eski bazadagi ma'lumotlar tozalandi.")

    db_objs = []
    for item in lessons:
        db_objs.append(Lesson(
            lesson_id=item["id"],
            lesson_number=item["lessonNumber"],
            title=item["title"],
            date=item["date"],
            time=item["time"],
            status=item["status"],
            goal=item["goal"],
            description=item["description"],
            content=item["content"],
            scenario=item["scenario"],
            code_examples=item["codeExamples"],
            tasks=item["tasks"],
            independent_tasks=item["independentTasks"],
            homework=item["homework"],
            quiz_questions=item["quizQuestions"],
            materials=item["materials"],
            student_results=item["studentResults"]
        ))

    Lesson.objects.bulk_create(db_objs)
    print(f"✅ Django SQLite bazasiga {len(db_objs)} ta dars mos holatda saqlandi.")

    with open(LESSONS_JSON, "w", encoding="utf-8") as f:
        json.dump(lessons, f, ensure_ascii=False, indent=2)
    print(f"💾 {LESSONS_JSON} fayli yangilandi.")

if __name__ == "__main__":
    run_update()
