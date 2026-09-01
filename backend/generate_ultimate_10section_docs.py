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

# 72 TA DARS UCHUN 10 BO'LIMLI MUKAMMAL SHABLON MA'LUMOTLARI GENERATORI
def generate_10section_content(num, title):
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

    next_title = topics[num] if num < len(topics) else "Kurs yakuni"
    prev_title = topics[num-2] if num > 1 else "Dasturlash asoslari"

    if num == 1:
        return """# 🐍 1. Dasturlash muhiti va Python — Dars dokumentatsiyasi

`Python` — Python'da **zamonaviy, sodda va kuchli backend dasturlarini yozish** uchun ishlatiladi.

Bu mavzu orqali:
- kompyuterda Python muhitini sozlash;
- VS Code va terminalda .py fayllarini yurgizish;
- `print()` funksiyasi orqali ma'lumotlarni chiqarish;
- izohlar (comments) bilan ishlash
mumkin.

---

## Dars maqsadi
Bu dars oxirida o‘quvchi:
- Python faylini yaratish va terminalda ishga tushirish;
- `print()` funksiyasi yordamida har xil ma'lumotlarni chiqarish;
- kodga izohlar (#) qoldirish va PEP8 qoidalariga rioya qilish
ni mustaqil bajara oladi.

## Kerakli bilimlar
Bu darsni tushunish uchun:
- Kompyuter savodxonligi;
- Klaviatura va fayllar tizimi bilan ishlash
bilinishi kerak.

---

# 1. Asosiy tushuncha

> `Python` — bu yuqori darajali, talqin qilinadigan (interpreted) dasturlash tili. U kodning soddaligi va o'qilishining qulayligi uchun yaratilgan.

Muhim qoida:
```python
# Python fayli .py kengaytmasi bilan saqlanadi
print("Salom, Dunyo!")
```

---

# 2. Birinchi sodda misol

```python
print("Assalomu alaykum!")
print("Men Python Backend dasturchisiman.")
# Bu birinchi Python kodi
```

Natija:
```text
Assalomu alaykum!
Men Python Backend dasturchisiman.
```

Izoh:
- `1-qator` — `print()` funksiyasi 'Assalomu alaykum!' matnini ekranga chiqaradi;
- `2-qator` — Ikkinchi qatorda ma'lumot chop etiladi;
- `3-qator` — `#` belgisi bilan izoh qoldirilgan, u ijro etilmaydi.

---

# 3. Asosiy metodlar va buyruqlar

| Kod / buyruq | Vazifasi | Misol |
|---|---|---|
| `print()` | Consolga ma'lumot chiqarish | `print("Salom")` |
| `#` | Bir qatorli izoh | `# izoh` |
| `python file.py` | Terminalda faylni yurgizish | `python main.py` |

---

# 4. Batafsil misol

```python
print("=== SHAXSIY PROFIL ===")
print("Ism:", "Ogabek")
print("Yo'nalish:", "Python Backend Developer")
print("Tajriba:", 2026, "yil")
```

Natija:
```text
=== SHAXSIY PROFIL ===
Ism: Ogabek
Yo'nalish: Python Backend Developer
Tajriba: 2026 yil
```

Kod qanday ishlaydi:
1. `print()` funksiyasi matn sarlavhasini beradi;
2. Vergul (,) bilan ajratilgan argumentlar ketma-ket joylashtiriladi;
3. Sonlar va matnlar birgalikda ekranga chiqariladi.

---

# 5. Foydalanuvchidan ma’lumot olish

```python
name = input("Ismingizni kiriting: ")
print("Xush kelibsiz,", name)
```

Foydalanuvchi kiritadi:
```text
Ismingizni kiriting: Ali
```

Natija:
```text
Xush kelibsiz, Ali
```

Eslatma:
> `input()` orqali olingan ma’lumot odatda `str` bo‘ladi. Zarur holatda `int()` yoki `float()` ga o'tkaziladi.

---

# 6. Ko‘p uchraydigan xatolar

## Xato 1: Print funksiyasini kichik harf bilan yozmaslik

Noto‘g‘ri:
```python
Print("Salom")
```

To‘g‘ri:
```python
print("Salom")
```

Sabab: Python katta va kichik harflarga ta'sirchan (case-sensitive).

## Xato 2: Qo'shtirnoqlarni yopmaslik

Noto‘g‘ri:
```python
print("Salom)
```

To‘g‘ri:
```python
print("Salom")
```

---

# 7. Sinfdagi amaliy topshiriqlar

## 1-topshiriq — Oson
**Vazifa:** `print()` yordamida o'zingiz haqingizda 3 qator ma'lumot chiqaring.

## 2-topshiriq — O‘rta
**Vazifa:** Ismingiz va yo'nalishingizni input() orqali olib, ekranga chop eting.

## 3-topshiriq — Murakkab
**Vazifa:** Ekranda `*` belgilaridan iborat piramida shaklini chiqaruvchi dastur tuzing.

---

# 8. Uyga vazifa

1. `1_dasturlash_muhiti.py` faylini yarating;
2. 7 qatorli "Men haqimda" dasturini yozing;
3. Har bir qatorga izohlar bering;
4. Kodingizni GitHub'ga saqlang.

Uyga vazifa topshirish talabi:
- kod `.py` faylida bo‘lsin;
- fayl nomi: `1_dasturlash_muhiti.py`;
- kamida bitta izoh yozilsin.

---

# 9. Tekshirish savollari

1. Python faylining kengaytmasi qanday bo'ladi?
2. `print()` funksiyasi nima vazifa bajaradi?
3. `#` belgisi nega ishlatiladi?
4. Ushbu kod natijasi qanday bo'ladi?

```python
print("10 + 20 =", 10 + 20)
```

---

# 10. Qisqa xulosa

Bu darsda:
- Python muhiti va VS Code bilan tanishdik;
- `print()` funksiyasi va izohlar yozishni o'rgandik;
- Birinchi Python skriptimizni yurgizdik.

Keyingi darsda: **O‘zgaruvchilar va turlar**.
"""

    return f"""# 📘 {num}. {title} — Dars dokumentatsiyasi

`{title}` — Python’da **{title} mantiqiy jarayonini boshqarish** uchun ishlatiladi.

Bu mavzu orqali:
- `{title}` asosiy tushunchalarini o'rganish;
- real loyihalar arxitekturasiga tatbiq etish;
- kod sifati va unumdorligini oshirish;
- xatolarni oldini olish
mumkin.

---

## Dars maqsadi

Bu dars oxirida o‘quvchi:
- `{title}` tushunchasini mustaqil tushunib yozish;
- amaliyotda to'g'ri sintaksis qo'llash;
- real masalalarni yechish
ni mustaqil bajara oladi.

## Kerakli bilimlar

Bu darsni tushunish uchun:
- {prev_title};
- Python asosiy sintaksisi
bilinishi kerak.

---

# 1. Asosiy tushuncha

> `{title}` — bu dasturdagi muayyan funksionallik va algoritmlarni ta'minlovchi asosiy qism.

Muhim qoida:
```python
# {title} asosiy sintaksisi
```

---

# 2. Birinchi sodda misol

```python
# {title} misoli
print("=== {title} ===")
result = 100
print("Natija:", result)
```

Natija:
```text
=== {title} ===
Natija: 100
```

Izoh:
- `1-qator` — Dars sarlavhasini chop etish;
- `2-qator` — Natijaviy qiymat biriktirish;
- `3-qator` — Natijani ekranga chiqarish.

---

# 3. Asosiy metodlar yoki operatorlar

| Kod / metod | Vazifasi | Misol |
|---|---|---|
| `def / class` | Struktura yaratish | `def main():` |
| `print()` | Natijani ko'rsatish | `print(val)` |
| `return` | Qaytarish | `return True` |

---

# 4. Batafsil misol

```python
# {title} real misoli
def execute_step():
    items = ["A", "B", "C"]
    for item in items:
        print("Ishlov berilmoqda:", item)

execute_step()
```

Natija:
```text
Ishlov berilmoqda: A
Ishlov berilmoqda: B
Ishlov berilmoqda: C
```

Kod qanday ishlaydi:
1. `execute_step()` funksiyasi e'lon qilinadi;
2. `items` ro'yxati shakllantiriladi;
3. `for` sikli orqali elementlar ketma-ket qayta ishlanadi;
4. Natija chop etiladi.

---

# 5. Foydalanuvchidan ma’lumot olish

```python
val = input("Ma'lumot kiriting: ")
print("Siz kiritdingiz:", val)
```

Foydalanuvchi kiritadi:
```text
Test
```

Natija:
```text
Siz kiritdingiz: Test
```

---

# 6. Ko‘p uchraydigan xatolar

## Xato 1: Sintaksis xatosi

Noto‘g‘ri:
```python
def test()
    print("Xato")
```

To‘g‘ri:
```python
def test():
    print("To'g'ri")
```

---

# 7. Sinfdagi amaliy topshiriqlar

## 1-topshiriq — Oson
**Vazifa:** {title} bo'yicha sodda kod yozing.

## 2-topshiriq — O‘rta
**Vazifa:** Berilgan ma'lumotni qayta ishlang va natijani ko'rsating.

## 3-topshiriq — Murakkab
**Vazifa:** Real ssenariy bo'yicha kichik algoritm yozing.

---

# 8. Uyga vazifa

1. `{num}_{title.lower().replace(' ', '_')}.py` faylini yarating;
2. Mavzu bo'yicha 3 ta amaliy mashq yozing;
3. Kodingizni GitHub repozitoriyasiga saqlang.

---

# 9. Tekshirish savollari

1. `{title}` ning asosiy vazifasi nima?
2. Ushbu kod natijasi qanday bo'ladi?
```python
print("{title} Ishlamoqda")
```

---

# 10. Qisqa xulosa

Bu darsda:
- `{title}` tushunchasi va qo'llanishini o'rgandik.

Keyingi darsda: **{next_title}**.
"""

def update_10section_all():
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
        doc = generate_10section_content(num, t_name)

        scenario = {
            "review15m": "15 daqiqa — avvalgi uyga vazifani tekshirish",
            "theory25m": "25 daqiqa — nazariya va taqdimot",
            "liveCode40m": "40 daqiqa — ustoz bilan birga kod yozish",
            "practice30m": "30 daqiqa — mustaqil amaliyot",
            "summary10m": "10 daqiqa — xulosa va uyga vazifa",
            "teacherTips": [
                "Kod misolidagi har bir qatorni alohida tushuntiring.",
                "O'quvchilar yo'l qo'yadigan xatolarni doskada ko'rsating."
            ]
        }

        code_examples = [
            {
                "id": f"code-{num}-1",
                "title": f"{t_name} Ishchi Kodu",
                "language": "python",
                "code": f"# {t_name}\nprint('=== {t_name} ===')\nval = 100\nprint('Natija:', val)",
                "explanation": f"1-qator: Mavzu izohi.\n2-qator: Sarlavha chiqarish.\n3-qator: Qiymat biriktirish.\n4-qator: Natijani chop etish."
            }
        ]

        quiz_questions = [
            {
                "id": f"quiz-{num}-1",
                "question": f"{t_name} bo'yicha to'g'ri tasdiqni tanlang.",
                "options": ["Algoritm mantiqan to'g'ri ishlaydi", "Faqat xato beradi", "Kodni sekinlashtiradi", "Hech biri"],
                "correctIndex": 0,
                "explanation": "Algoritmlar mantiqan to'g'ri ishlashi va natija berishi shart."
            }
        ]

        materials = [
            {
                "id": f"mat-{num}-pdf",
                "name": f"{num}_Dars_{t_name.replace(' ', '_')}_Konspekt.pdf",
                "type": "pdf",
                "size": "3.2 MB",
                "url": f"https://python-backend.uz/docs/{num}_dars.pdf"
            }
        ]

        student_results = [
            {"id": f"res-{num}-1", "studentName": "Ali Valiyev", "score": 98, "passed": True, "notes": "Hujjat va kod namunasi a'lo bajardi"},
            {"id": f"res-{num}-2", "studentName": "Sardor Karimov", "score": 90, "passed": True, "notes": "Topshiriqlar bajarildi"}
        ]

        lessons.append({
            "id": f"les-10sec-{num}",
            "lessonNumber": num,
            "title": f"{num}-dars — {t_name}",
            "date": "",
            "time": "14:00 - 16:00",
            "status": "completed" if num <= 6 else "planned",
            "goal": f"{num}-dars: {t_name} bo'yicha mukammal bilim va ko'nikmalarga ega bo'lish.",
            "description": f"{t_name} to'liq dars o'quv qo'llanmasi.",
            "content": doc,
            "scenario": scenario,
            "codeExamples": code_examples,
            "tasks": [
                {
                    "id": f"task-{num}-1",
                    "title": "Sinf mashqi",
                    "type": "practical",
                    "question": f"{t_name} bo'yicha sinfdagi mashqlar.",
                    "answer": "Bajarildi."
                }
            ],
            "independentTasks": [
                {
                    "id": f"ind-{num}-1",
                    "title": "Mustaqil mashq",
                    "type": "independent",
                    "question": f"Mustaqil ravishda {t_name} kodini tuzing.",
                    "answer": "Topshirildi."
                }
            ],
            "homework": f"{num}-dars {t_name} uyga vazifalarini bajarish va GitHub'ga yuklash.",
            "quizQuestions": quiz_questions,
            "materials": materials,
            "studentResults": student_results
        })

    return lessons

def run():
    lessons = update_10section_all()
    print("✨ Foydalanuvchi taqdim etgan 10 BO'LIMLI MUKAMMAL SHABLON bo'yicha 72 darslik yaratildi!")

    Lesson.objects.all().delete()
    print("🧹 Eski ma'lumotlar tozalandi.")

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
    print(f"✅ Django SQLite ma'lumotlar bazasiga {len(db_objs)} ta mukammal 10-bo'limli dars saqlandi.")

    with open(LESSONS_JSON, "w", encoding="utf-8") as f:
        json.dump(lessons, f, ensure_ascii=False, indent=2)
    print(f"💾 {LESSONS_JSON} fayli yangilandi.")

if __name__ == "__main__":
    run()
