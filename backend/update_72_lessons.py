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

# 72 TA DARS MANBASI (Foydalanuvchi tomonidan kiritilgan to'liq o'quv dasturi)
RAW_TEXT = """
### 1-dars — Dasturlash muhiti va Python
**Mavzu:** algoritm, Python, VS Code, `.py` fayl, `print()`, izohlar.  
**Amaliyot:** shaxsiy ma’lumotlarni ekranga chiqaruvchi dastur.  
**Uyga vazifa:** 7 qatorli “Men haqimda” dasturi.

### 2-dars — O‘zgaruvchilar va turlar
**Mavzu:** `str`, `int`, `float`, `bool`, `type()`, nomlash qoidalari.  
**Amaliyot:** talaba profilini o‘zgaruvchilarda saqlash.  
**Uyga vazifa:** 10 turli o‘zgaruvchi va ularning turlarini chiqarish.

### 3-dars — Input va arifmetika
**Mavzu:** `input()`, turga o‘tkazish, `+ - * / // % **`.  
**Amaliyot:** ikki sonli kalkulyator; yosh hisoblash.  
**Uyga vazifa:** to‘g‘ri to‘rtburchak yuzi va perimetri.

### 4-dars — Stringlar
**Mavzu:** indeks, slicing, `len`, `lower`, `upper`, `strip`, `replace`, `split`.  
**Amaliyot:** so‘zlar soni va emaildan loginni ajratish.  
**Uyga vazifa:** matndagi eng uzun so‘zni topish.

### 5-dars — If/elif/else
**Mavzu:** taqqoslash operatorlari, shartlar, indentatsiya.  
**Amaliyot:** son musbat/manfiy/nol; baholash tizimi.  
**Uyga vazifa:** uchta sonning kattasini topish.

### 6-dars — Mantiqiy operatorlar
**Mavzu:** `and`, `or`, `not`, ichma-ich shartlar.  
**Amaliyot:** login-parol va bankomat mantiqi.  
**Uyga vazifa:** kursga qabul qiluvchi dastur.

### 7-dars — For sikli
**Mavzu:** `for`, `range()`, `enumerate()`.  
**Amaliyot:** 1–100 sonlari, juft/toq sonlar, yig‘indi.  
**Uyga vazifa:** ko‘paytirish jadvali.

### 8-dars — While sikli
**Mavzu:** hisoblagich, sikl sharti, cheksiz sikl.  
**Amaliyot:** `0` kiritilguncha sonlar yig‘indisi.  
**Uyga vazifa:** 3 urinishli parol tekshiruvi.

### 9-dars — Break, continue va random
**Mavzu:** `break`, `continue`, `while True`, `random`.  
**Amaliyot:** son topish o‘yini.  
**Uyga vazifa:** tasodifiy sonli viktorina.

### 10-dars — Ichma-ich sikl va algoritmlar
**Mavzu:** ichma-ich sikl, tub son, palindrom.  
**Amaliyot:** yulduzchali shakllar, son raqamlari yig‘indisi.  
**Uyga vazifa:** 1 dan `n` gacha tub sonlarni chiqarish.

### 11-dars — List asoslari
**Mavzu:** list, indeks, slicing, `append`, `insert`, `remove`, `pop`, `sort`.  
**Amaliyot:** xaridlar ro‘yxati va baholar tahlili.  
**Uyga vazifa:** sonlarni juft/toq listlarga ajratish.

### 12-dars — 1-modul imtihoni
**Mavzu:** 1–11-dars bo'yicha 1-modul nazorati.  
**Amaliyot:** kalkulyator, shartli baholash, sikl bilan masala, string va list vazifasi.  
**Uyga vazifa:** Baholash: nazariya 20, amaliy kod 50, kod sifati 20, faollik 10 ball.

### 13-dars — Tuple va set
**Mavzu:** tuple/list farqi, set, `add`, `discard`, `union`, `intersection`.  
**Amaliyot:** takrorlanadigan elementlarni tozalash.  
**Uyga vazifa:** ikki listning umumiy va farqli elementlari.

### 14-dars — Dictionary
**Mavzu:** kalit-qiymat, `get`, `keys`, `values`, `items`.  
**Amaliyot:** telefon daftari, mahsulotlar narxi.  
**Uyga vazifa:** 5 mahsulotli lug‘atdan umumiy narxni hisoblash.

### 15-dars — Murakkab ma’lumotlar
**Mavzu:** list ichidagi dictionary, dictionary ichidagi list.  
**Amaliyot:** talabalar-fanlar-baholar ma’lumoti.  
**Uyga vazifa:** uch o‘quvchilik ma’lumotlar bazasi (list/dict ko‘rinishida).

### 16-dars — Comprehension
**Mavzu:** list, set, dictionary comprehension.  
**Amaliyot:** juft sonlar, sonlar kvadrati, so‘z uzunliklari.  
**Uyga vazifa:** matndagi har bir so‘zning takrorlanish soni.

### 17-dars — Funksiyalar
**Mavzu:** `def`, parametr, `return`, default parametr.  
**Amaliyot:** funksiyali kalkulyator va chegirma hisoblash.  
**Uyga vazifa:** uchta sonning kattasini qaytaruvchi funksiya.

### 18-dars — *args, **kwargs va scope
**Mavzu:** istalgan argumentlar, local/global o‘zgaruvchi.  
**Amaliyot:** istalgan sonlarning yig‘indisi; talaba pasporti.  
**Uyga vazifa:** istalgan sonlardan maksimalini topish.

### 19-dars — Lambda va rekursiya
**Mavzu:** lambda, `map`, `filter`, rekursiv funksiya.  
**Amaliyot:** sonlar kvadrati, juftlarni filtrlash, faktorial.  
**Uyga vazifa:** rekursiya bilan raqamlar yig‘indisi.

### 20-dars — Modullar va kutubxonalar
**Mavzu:** `math`, `random`, `datetime`, o‘z moduli.  
**Amaliyot:** parol generatsiyasi va yosh hisoblash.  
**Uyga vazifa:** 10 savolli konsol testi.

### 21-dars — Xatolarni boshqarish
**Mavzu:** `try`, `except`, `else`, `finally`, `ValueError`.  
**Amaliyot:** xavfsiz kalkulyator va tekshirilgan input.  
**Uyga vazifa:** xatodan himoyalangan login dasturi.

### 22-dars — Fayllar
**Mavzu:** `open`, `read`, `write`, `append`, `with open`, UTF-8.  
**Amaliyot:** kontaktlarni faylga yozish va o‘qish.  
**Uyga vazifa:** fayldagi qator, so‘z va belgi sonini topish.

### 23-dars — JSON va requests
**Mavzu:** `json.load`, `json.dump`, HTTP so‘rovi, `requests.get()`, API javobi.  
**Amaliyot:** JSON test; ochiq API dan mahsulotlarni chiqarish.  
**Uyga vazifa:** JSON fayldagi testni ishlatadigan dastur.

### 24-dars — 2-modul imtihoni
**Mavzu:** 13–23-darslar bo'yicha 2-modul imtihoni.  
**Amaliyot:** dictionary savati, funksiya, faylga saqlash, JSON dan test chiqarish.  
**Uyga vazifa:** O‘quvchi terminaldagi Python dasturini mustaqil yoza olishi kerak.

### 25-dars — OOP, class va object
**Mavzu:** class, object, atribut, metod.  
**Amaliyot:** `Talaba`, `Mashina`, `Telefon` klasslari.  
**Uyga vazifa:** `Kitob` klassi.

### 26-dars — __init__ va self
**Mavzu:** konstruktor, instance atributlar.  
**Amaliyot:** talaba va mahsulot obyektlari.  
**Uyga vazifa:** `Xodim` klassida ish haqi hisoblash.

### 27-dars — Inkapsulyatsiya
**Mavzu:** private atribut, getter/setter, property.  
**Amaliyot:** `BankHisobi`: balans, pul qo‘shish, pul yechish.  
**Uyga vazifa:** private parolli foydalanuvchi klassi.

### 28-dars — Vorislik va polymorphism
**Mavzu:** inheritance, `super()`, method override.  
**Amaliyot:** `Hayvon` → `Mushuk`, `It`; `Shaxs` → `Talaba`, `Oqituvchi`.  
**Uyga vazifa:** transport klasslari.

### 29-dars — Class/static va dunder metodlar
**Mavzu:** classmethod, staticmethod, `__str__`, `__repr__`, `__eq__`, `__lt__`.  
**Amaliyot:** talabalarni bahosi bo‘yicha solishtirish.  
**Uyga vazifa:** kitoblarni sahifasi bo‘yicha solishtirish.

### 30-dars — OOP mini-loyiha
**Mavzu:** loyihani klasslarga va fayllarga bo‘lish.  
**Amaliyot:** kutubxona/bank tizimi: qo‘shish, qidirish, berish, qaytarish.  
**Uyga vazifa:** ma’lumotlarni JSON ga saqlash.

### 31-dars — SQL va SQLite kirish
**Mavzu:** database, table, row, column, SQLite, `CREATE TABLE`.  
**Amaliyot:** talabalar jadvali.  
**Uyga vazifa:** mahsulotlar jadvali.

### 32-dars — SQLite CRUD
**Mavzu:** `INSERT`, `SELECT`, `UPDATE`, `DELETE`, parametrli so‘rov.  
**Amaliyot:** talaba qo‘shish, qidirish, tahrirlash, o‘chirish.  
**Uyga vazifa:** SQLite telefon daftari.

### 33-dars — SQL so‘rovlar va munosabatlar
**Mavzu:** `WHERE`, `ORDER BY`, `LIMIT`, `LIKE`, primary/foreign key, `JOIN`.  
**Amaliyot:** guruhlar va talabalar jadvallari.  
**Uyga vazifa:** mijoz-buyurtma-mahsulot sxemasi.

### 34-dars — PostgreSQL va psycopg
**Mavzu:** PostgreSQL o‘rnatish, database, user, `psycopg` ulanishi.  
**Amaliyot:** Python dan PostgreSQL jadvali yaratish.  
**Uyga vazifa:** PostgreSQL da talabalar bazasi.

### 35-dars — PostgreSQL CRUD va JOIN
**Mavzu:** Python orqali CRUD, transaction, `commit`, `rollback`, JOIN.  
**Amaliyot:** mahsulotlar CRUD dasturi.  
**Uyga vazifa:** buyurtmalar tizimi.

### 36-dars — 3-modul imtihoni
**Mavzu:** 25–35-dars: OOP, SQLite va PostgreSQL.  
**Amaliyot:** class yozish; SQLite CRUD; SQL JOIN; PostgreSQL bilan Python dasturi.  
**Uyga vazifa:** Nazariy va amaliy bilimlarni takrorlash.

### 37-dars — Telegram bot va xavfsizlik
**Mavzu:** BotFather, token, `.env`, virtual environment, Aiogram loyiha tuzilishi.  
**Amaliyot:** `/start`, `/help`, `/about` buyruqli bot.  
**Uyga vazifa:** foydalanuvchi ismiga mos salomlashish.

### 38-dars — Handler va filterlar
**Mavzu:** `Message`, router, filter, command, xabar turlari.  
**Amaliyot:** echo bot va matnli kalkulyator.  
**Uyga vazifa:** foydalanuvchi ma’lumotini so‘rovchi bot.

### 39-dars — Reply keyboard
**Mavzu:** `ReplyKeyboardMarkup`, keyboard builder, contact/location.  
**Amaliyot:** kurslar, aloqa va manzil menyuli bot.  
**Uyga vazifa:** taom buyurtma menyusi.

### 40-dars — Inline keyboard
**Mavzu:** inline tugmalar, callback query, callback data.  
**Amaliyot:** mahsulot katalogi va mahsulot detail sahifasi.  
**Uyga vazifa:** 3 mahsulotli katalog.

### 41-dars — FSM
**Mavzu:** `State`, `StatesGroup`, `FSMContext`, cancel holati.  
**Amaliyot:** ism, telefon, manzil so‘raydigan anketa.  
**Uyga vazifa:** kursga yozilish jarayoni.

### 42-dars — Media va fayllar
**Mavzu:** photo, document, video, voice bilan ishlash.  
**Amaliyot:** fayl qabul qiladigan va rasm yuboradigan bot.  
**Uyga vazifa:** yuborilgan fayl ma’lumotini chiqarish.

### 43-dars — Aiogram + SQLite/PostgreSQL
**Mavzu:** foydalanuvchi va buyurtmalarni database ga saqlash.  
**Amaliyot:** `/start` qilgan foydalanuvchini database ga yozish.  
**Uyga vazifa:** admin uchun foydalanuvchilar ro‘yxati.

### 44-dars — Guruh botlari
**Mavzu:** guruh xabarlari, admin tekshirish, yangi a’zolar, qoidalar.  
**Amaliyot:** yangi a’zoni kutib oluvchi va qoidalarni yuboruvchi bot.  
**Uyga vazifa:** taqiqlangan so‘zlar uchun ogohlantirish mantiqi.

### 45-dars — Telegram bot mini-loyiha, 1-qism
**Mavzu:** loyiha arxitekturasi va routerlar.  
**Amaliyot:** kursga yozilish yoki buyurtma botining menyusi, FSM va database qismi.  
**Uyga vazifa:** asosiy oqimni yakunlash.

### 46-dars — Telegram bot mini-loyiha, 2-qism
**Mavzu:** admin ga xabar yuborish, buyurtma holati, xatolar.  
**Amaliyot:** buyurtmani qabul qilish va database ga saqlash.  
**Uyga vazifa:** admin komandalarini qo‘shish.

### 47-dars — Bot testlash va deploy tayyorgarligi
**Mavzu:** logging, xato holatlari, `requirements.txt`, README.  
**Amaliyot:** 10 ta test holati va GitHub ga joylash.  
**Uyga vazifa:** imtihon uchun botni tayyorlash.

### 48-dars — 4-modul imtihoni
**Mavzu:** 37–47-dars: Aiogram, tugmalar, FSM, media, database va guruh botlari.  
**Amaliyot:** `/start`; inline katalog; FSM anketa; database ga saqlash.  
**Uyga vazifa:** Barcha bot loyihalarini GitHub'ga topshirish.

### 49-dars — Web asoslari va HTML/CSS takrorlash
**Mavzu:** browser-server, HTTP, URL, request/response, HTML semantic teglar, CSS/flexbox.  
**Amaliyot:** Django loyihasi uchun statik portfolio maketi.  
**Uyga vazifa:** 3 sahifali HTML/CSS maket.

### 50-dars — Django project va app
**Mavzu:** venv, pip, project/app, `manage.py`, development server, settings.  
**Amaliyot:** `core` app yaratish va bosh sahifani ochish.  
**Uyga vazifa:** `about` va `contact` sahifalari.

### 51-dars — URL, view va template
**Mavzu:** URL routing, function-based views, context, template inheritance.  
**Amaliyot:** `base.html`, navbar, home/about/contact.  
**Uyga vazifa:** sahifalarga dinamik sarlavha chiqarish.

### 52-dars — Static va media
**Mavzu:** static files, CSS/JS, media files, image upload sozlamalari.  
**Amaliyot:** dizayn va rasm yuklash.  
**Uyga vazifa:** sahifani responsive qilish.

### 53-dars — Models va migrations
**Mavzu:** Django model fieldlari, `makemigrations`, `migrate`, relationshiplar.  
**Amaliyot:** kurs va dars modeli; foreign key.  
**Uyga vazifa:** category va product modellari.

### 54-dars — Django admin va ORM
**Mavzu:** admin sozlash, list display, search, filter, ORM so‘rovlari.  
**Amaliyot:** admin panelda mahsulotlarni boshqarish.  
**Uyga vazifa:** 10 ta ma’lumot qo‘shib, qidiruv/filter sozlash.

### 55-dars — Django forms va validatsiya
**Mavzu:** `forms.Form`, `ModelForm`, `clean_*`, xato xabarlari, CSRF.  
**Amaliyot:** mahsulot yoki post qo‘shish formasi.  
**Uyga vazifa:** forma validatsiyasini qo‘shish.

### 56-dars — Function-based CRUD
**Mavzu:** list, detail, create, update, delete; GET/POST.  
**Amaliyot:** to‘liq mahsulot/post CRUD.  
**Uyga vazifa:** o‘chirish oldidan tasdiqlash sahifasi.

### 57-dars — Class-based views va pagination
**Mavzu:** `ListView`, `DetailView`, `CreateView`, `UpdateView`, `DeleteView`, pagination.  
**Amaliyot:** CRUD ni class-based view ga o‘tkazish.  
**Uyga vazifa:** qidiruv va pagination qo‘shish.

### 58-dars — Foydalanuvchi autentifikatsiyasi
**Mavzu:** register, login, logout, password hash, session, `login_required`.  
**Amaliyot:** ro‘yxatdan o‘tish va kirish tizimi.  
**Uyga vazifa:** faqat login qilgan foydalanuvchi post yaratishi.

### 59-dars — Permissions, messages va custom user
**Mavzu:** `UserPassesTestMixin`, group, permission, messages framework, custom user modeli tushunchasi.  
**Amaliyot:** faqat muallif postini tahrirlay/ochira oladigan sayt.  
**Uyga vazifa:** admin va oddiy user rollarini sozlash.

### 60-dars — 5-modul imtihoni
**Mavzu:** 49–59-dars: HTML/CSS, Django project, template, static/media, model, admin, ORM, form, CRUD, auth.  
**Amaliyot:** model; CRUD; login; faqat muallifga tahrirlash ruxsati.  
**Uyga vazifa:** Loyihani to'liq tekshirish.

### 61-dars — DRF va serializer
**Mavzu:** REST API, JSON, serializer, `ModelSerializer`, APIView.  
**Amaliyot:** mahsulotlar uchun GET API.  
**Uyga vazifa:** talaba yoki kurs modeli uchun serializer.

### 62-dars — Generic views, ViewSet va router
**Mavzu:** `ListCreateAPIView`, `RetrieveUpdateDestroyAPIView`, ModelViewSet, router.  
**Amaliyot:** to‘liq CRUD API.  
**Uyga vazifa:** API endpointlarini Postman da tekshirish.

### 63-dars — API auth va permissions
**Mavzu:** Token authentication, JWT tushunchasi, `IsAuthenticated`, custom permission.  
**Amaliyot:** register/login API va himoyalangan endpoint.  
**Uyga vazifa:** faqat egasi o‘zgartira oladigan API.

### 64-dars — Filter, search, pagination va ordering
**Mavzu:** `django-filter`, search filter, ordering filter, API pagination.  
**Amaliyot:** mahsulot API qidiruvi va sahifalash.  
**Uyga vazifa:** 3 ta filter bilan API endpoint.

### 65-dars — Signals, email va background vazifalar
**Mavzu:** Django signals, email jo‘natish, Celery/Redis tushunchasi.  
**Amaliyot:** yangi user ro‘yxatdan o‘tganda profil yaratish; email xabari.  
**Uyga vazifa:** signal yordamida user profil yaratish.

### 66-dars — Django test, xavfsizlik va sozlamalar
**Mavzu:** unit test, test client, DEBUG, ALLOWED_HOSTS, CSRF, secret key, `.env`, logging.  
**Amaliyot:** model/view uchun test yozish va production settings tayyorlash.  
**Uyga vazifa:** loyiha uchun `.env.example` va test yozish.

### 67-dars — Loyiha arxitekturasi va rejalash
**Mavzu:** loyiha mavzusi, ER diagramma, user flow, app bo‘linishi.  
**Amaliyot:** yakuniy loyiha (dars reja, blog, do‘kon yoki o‘quv markaz) sxemasini yaratish.  
**Uyga vazifa:** model va endpointlar ro‘yxati.

### 68-dars — Yakuniy loyiha: Django web qismi
**Mavzu:** model, admin, template, CRUD, auth ni birlashtirish.  
**Amaliyot:** loyihaning web qismini yozish.  
**Uyga vazifa:** web qismi 70% tayyor bo‘lishi.

### 69-dars — Yakuniy loyiha: API yoki Telegram integratsiya
**Mavzu:** DRF endpointlarini ulash yoki Aiogram botni Django backend bilan bog‘lash.  
**Amaliyot:** API/bot orqali ma’lumot olish va yuborish.  
**Uyga vazifa:** barcha asosiy funksiyalarni tugatish.

### 70-dars — Deploy
**Mavzu:** Git/GitHub, `requirements.txt`, Gunicorn, Nginx tushunchasi, server/deploy, static/media.  
**Amaliyot:** loyihani deploy uchun tayyorlash.  
**Uyga vazifa:** README, demo video yoki screenshots.

### 71-dars — Loyiha testlash va himoyaga tayyorlash
**Mavzu:** xatolar, refaktor, kod sifati, taqdimot.  
**Amaliyot:** 10 ta test holati; kod ko‘rigi; GitHub profilini tartibga keltirish.  
**Uyga vazifa:** 3–5 daqiqali loyiha taqdimoti.

### 72-dars — Yakuniy imtihon va loyiha himoyasi
**Mavzu:** 6 oylik to'liq kurs bo'yicha yakuniy himoya.  
**Amaliyot:** o‘quvchi ishlaydigan Django loyihasi va uning API/bot qismini ko‘rsatadi.  
**Uyga vazifa:** Loyihani foydalanishga topshirish va Sertifikat olish.
"""

def parse_lessons():
    pattern = r"### (\d+)-dars — (.*?)\n\*\*Mavzu:\*\* (.*?)\n\*\*Amaliyot:\*\* (.*?)\n\*\*Uyga vazifa:\*\* (.*?)(?=\n### |\Z)"
    matches = re.findall(pattern, RAW_TEXT, re.DOTALL)
    
    parsed_lessons = []
    
    for match in matches:
        num = int(match[0])
        title = match[1].strip()
        mavzu = match[2].strip()
        amaliyot = match[3].strip()
        vazifa = match[4].strip()
        
        is_exam = num in [12, 24, 36, 48, 60, 72]
        
        content = f"""### Dars Konspekti

**Mavzu:** {mavzu}

---

### 💻 Amaliy Mashg'ulot
{amaliyot}

---

### 📋 Dars Formati va Rejasi
- **15 daqiqa:** Avvalgi uyga vazifani tekshirish
- **25 daqiqa:** Nazariya ({mavzu})
- **40 daqiqa:** Ustoz bilan birga kod yozish
- **30 daqiqa:** Mustaqil amaliyot
- **10 daqiqa:** Xulosa va uyga vazifa
"""
        tasks = []
        if amaliyot:
          tasks.append({
              "id": f"task-{num}-1",
              "title": "Sinfdagi amaliy topshiriq",
              "type": "practical",
              "question": amaliyot,
              "answer": "O'qituvchi ko'rsatmasi bo'yicha bajarildi."
          })

        parsed_lessons.append({
            "id": f"les-72curriculum-{num}",
            "lessonNumber": num,
            "title": f"{num}-dars — {title}",
            "date": "",
            "time": "14:00 - 16:00",
            "status": "completed" if num <= 6 else "planned",
            "description": mavzu,
            "content": content,
            "homework": vazifa,
            "materials": [
                {
                    "id": f"mat-{num}-1",
                    "name": f"{num}_dars_qo_llanma.pdf",
                    "type": "pdf",
                    "url": "#"
                }
            ],
            "tasks": tasks
        })
        
    return parsed_lessons

def update_database():
    lessons = parse_lessons()
    print(f"📋 Parsed {len(lessons)} lessons from the official 72-lesson curriculum.")
    
    # 1. Clear existing database in Django ORM
    Lesson.objects.all().delete()
    print("🧹 Purged old database records.")
    
    # 2. Re-create all 72 lessons
    db_objects = []
    for item in lessons:
        db_objects.append(Lesson(
            lesson_id=item["id"],
            lesson_number=item["lessonNumber"],
            title=item["title"],
            date=item["date"],
            time=item["time"],
            status=item["status"],
            description=item["description"],
            content=item["content"],
            homework=item["homework"],
            materials=item["materials"],
            tasks=item["tasks"]
        ))
    Lesson.objects.bulk_create(db_objects)
    print(f"✅ Created {len(db_objects)} lessons in Django SQLite database.")
    
    # 3. Update lessons.json for frontend backup/cache
    with open(LESSONS_JSON, "w", encoding="utf-8") as f:
        json.dump(lessons, f, ensure_ascii=False, indent=2)
    print(f"💾 Updated {LESSONS_JSON} with 72 curated lessons.")

if __name__ == "__main__":
    update_database()
