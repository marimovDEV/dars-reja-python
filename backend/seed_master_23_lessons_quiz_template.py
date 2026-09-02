import os
import sys
import django

# Setup Django Environment
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from lessons_app.models import QuizTemplate, Quiz

MASTER_30_QUESTIONS = [
    {
        "id": "q1",
        "question": "Python'da quyidagi o'zgaruvchilardan qaysilari o'zgarmas (immutable) turga kiradi?",
        "options": ["tuple, int, str, bool", "list, dict, set", "tuple, list, dict", "set, dict, str"],
        "correctAnswer": 0,
        "explanation": "tuple, int, str va bool obyektlari yaratilgach xotirada o'zgarmasdir.",
        "duration": 20
    },
    {
        "id": "q2",
        "question": "Quyidagi Python kodining natijasi nima bo'ladi?",
        "codeSnippet": "numbers = [10, 20, 30, 40, 50, 60]\nprint(numbers[-4:-1])",
        "options": ["[30, 40, 50]", "[20, 30, 40]", "[30, 40, 50, 60]", "[40, 50, 60]"],
        "correctAnswer": 0,
        "explanation": "Manfiy indekslashda -4 indeks (30) dan -1 indeksgacha (50) olinadi.",
        "duration": 25
    },
    {
        "id": "q3",
        "question": "Dictionary'dan mavjud bo'lmagan kalitni xatolik yuz bermasdan xavfsiz olish uchun qaysi metod ishlatiladi?",
        "options": ["dict.get(key, default)", "dict.fetch(key)", "dict.find(key)", "dict.search(key)"],
        "correctAnswer": 0,
        "explanation": "get() metodi kalit bo'lmasa KeyError bermaydi, None yoki default qiymat qaytaradi.",
        "duration": 20
    },
    {
        "id": "q4",
        "question": "Quyidagi List Comprehension kodi nimani qaytaradi?",
        "codeSnippet": "res = [x**2 for x in range(10) if x % 2 != 0]\nprint(res)",
        "options": ["[1, 9, 25, 49, 81]", "[0, 4, 16, 36, 64]", "[1, 3, 5, 7, 9]", "[1, 4, 9, 16, 25]"],
        "correctAnswer": 0,
        "explanation": "1, 3, 5, 7, 9 toq sonlarining kvadratlari hosil qilinadi.",
        "duration": 25
    },
    {
        "id": "q5",
        "question": "Quyidagi set amallari bajarilgach, `s1 & s2` ning natijasi nima bo'ladi?",
        "codeSnippet": "s1 = {1, 2, 3, 4, 5}\ns2 = {3, 4, 5, 6, 7}\nprint(s1 & s2)",
        "options": ["{3, 4, 5}", "{1, 2, 3, 4, 5, 6, 7}", "{1, 2}", "{6, 7}"],
        "correctAnswer": 0,
        "explanation": "& operaori to'plamlarning kesishmasini (umumiy elementlarini) qaytaradi.",
        "duration": 20
    },
    {
        "id": "q6",
        "question": "Quyidagi kod ishga tushsa natija nima chiqadi?",
        "codeSnippet": "nums = [1, 2, 3, 4]\nresult = list(map(lambda x: x * 3, nums))\nprint(result)",
        "options": ["[3, 6, 9, 12]", "[1, 2, 3, 4]", "[3, 3, 3, 3]", "[1, 8, 27, 64]"],
        "correctAnswer": 0,
        "explanation": "map va lambda yordamida har bir element 3 ga ko'paytiriladi.",
        "duration": 20
    },
    {
        "id": "q7",
        "question": "Quyidagi filter amali bajarilgach, `res` ro'yxatida nimalar qoladi?",
        "codeSnippet": "items = [0, 1, False, True, '', 'Python', None, [], [5]]\nres = list(filter(None, items))\nprint(res)",
        "options": ["[1, True, 'Python', [5]]", "[0, False, '', None, []]", "[1, 'Python', [5]]", "[0, 1, True, 'Python']"],
        "correctAnswer": 0,
        "explanation": "filter(None, ...) faqat Truthy (mantiqiy rost) qiymatlarni saqlab qoladi.",
        "duration": 25
    },
    {
        "id": "q8",
        "question": "Python funktsiyasida `*args` va `**kwargs` mos ravishda qanday turda qabul qilinadi?",
        "options": ["args - Tuple, kwargs - Dict", "args - List, kwargs - Dict", "args - Tuple, kwargs - List", "args - Dict, kwargs - Tuple"],
        "correctAnswer": 0,
        "explanation": "*args tuple shaklida pozitsion, **kwargs esa dict shaklida kalitli argumentlarni yig'adi.",
        "duration": 20
    },
    {
        "id": "q9",
        "question": "Quyidagi rekursiv funktsiya `fact(5)` chaqirilganda necha qiymat qaytaradi?",
        "codeSnippet": "def fact(n):\n    return 1 if n <= 1 else n * fact(n - 1)\nprint(fact(5))",
        "options": ["120", "24", "60", "720"],
        "correctAnswer": 0,
        "explanation": "5! = 5 * 4 * 3 * 2 * 1 = 120 hisoblanadi.",
        "duration": 20
    },
    {
        "id": "q10",
        "question": "Quyidagi kod ishga tushganda konsolda qanday natija chop etiladi?",
        "codeSnippet": "x = 10\ndef foo():\n    global x\n    x += 5\nfoo()\nprint(x)",
        "options": ["15", "10", "UnboundLocalError", "5"],
        "correctAnswer": 0,
        "explanation": "global x orqali tashqi x o'zgaruvchisi 10 + 5 = 15 ga o'zgaradi.",
        "duration": 20
    },
    {
        "id": "q11",
        "question": "OOP'da `super().__init__()` chaqiruvining asosiy vazifasi nima?",
        "options": ["Ota (Parent) sinfining __init__ konstruktorini chaqirish", "Yangi obyekt nusxasini yaratish", "Sinf metodlarini o'chirish", "Sinf nomini o'zgartirish"],
        "correctAnswer": 0,
        "explanation": "super() otasining init funksiyasini chaqirib otadagi atributlarni initsializatsiya qiladi.",
        "duration": 20
    },
    {
        "id": "q12",
        "question": "Python'da o'zgaruvchi nomidan oldin ikkita pastki chiziq (`__var`) qo'yilganda nima sodir bo'ladi?",
        "options": ["Name Mangling tufayli atribut private bo'lib, sinf tashqarisidan to'g'ridan-to'g'ri ko'rinmaydi", "Atribut global o'zgaruvchiga aylanadi", "Atribut o'zgarmas (const) bo'ladi", "Sintaktik xatolik yuz beradi"],
        "correctAnswer": 0,
        "explanation": "Python Name Mangling mexanizmi orqali _ClassName__var nomiga o'zgartirib private qiladi.",
        "duration": 25
    },
    {
        "id": "q13",
        "question": "Python obyektini print() qilganda tushunarli matn shaklida chiqarish uchun qaysi sehrli (magic) metod yoziladi?",
        "options": ["__str__", "__init__", "__call__", "__main__"],
        "correctAnswer": 0,
        "explanation": "__str__ metodi print() va str() funksiyalari chaqirilganda javob beradi.",
        "duration": 20
    },
    {
        "id": "q14",
        "question": "Try-Except-Else-Finally blokida `else` bo'limi qachon ishga tushadi?",
        "options": ["Faqat try bloki ichida hech qanday xatolik yuz bermaganda", "Faqat xatolik yuz berganda", "Har doim xatolik bo'lsa ham, bo'lmasa ham", "Faqat Exception turi mos kelmaganda"],
        "correctAnswer": 0,
        "explanation": "else bloki try muvaffaqiyatli xatoliksiz o'tgandagina ishlaydi.",
        "duration": 25
    },
    {
        "id": "q15",
        "question": "Python'da o'zingizning maxsus xatolik sinfingizni (Custom Exception) yaratish uchun qaysi bazaviy sinfdan meros olinadi?",
        "options": ["Exception", "BaseObject", "TypeError", "StandardError"],
        "correctAnswer": 0,
        "explanation": "Barcha custom exceptionlar Exception sinfidan meros olib yaratiladi.",
        "duration": 20
    },
    {
        "id": "q16",
        "question": "Fayllar bilan ishlashda `with open(...) as f:` konstruktsiyasining asosiy afzalligi nima?",
        "options": ["Fayl bilan ishlash tugagach, u avtomatik tarzda yopiladi (close qilinadi)", "Fayl hajmini 2 barobar qisqartiradi", "Faylni keshga yuklaydi", "Fayl parolini shifrlaydi"],
        "correctAnswer": 0,
        "explanation": "Context Manager faylni ish yakunida xatolik bo'lsa ham xavfsiz yopilishini kafolatlaydi.",
        "duration": 20
    },
    {
        "id": "q17",
        "question": "Faylni faqat yozish uchun va agar fayl mavjud bo'lmasa uni yangi yaratish uchun qaysi rejim ishlatiladi?",
        "options": ["'w'", "'r'", "'a'", "'x+'"],
        "correctAnswer": 0,
        "explanation": "'w' rejimi yangi yozish uchun fayl ochadi va eskisini ustidan yozadi.",
        "duration": 20
    },
    {
        "id": "q18",
        "question": "Quyidagi dekorator ishga tushirilgach, `greet()` chaqirilganda nima chop etiladi?",
        "codeSnippet": "def my_dec(func):\n    def wrapper():\n        print('Boshlandi')\n        func()\n        print('Tugadi')\n    return wrapper\n\n@my_dec\ndef greet():\n    print('Salom!')\n\ngreet()",
        "options": ["Boshlandi \\n Salom! \\n Tugadi", "Salom!", "Boshlandi \\n Tugadi", "SyntaxError"],
        "correctAnswer": 0,
        "explanation": "Dekorator funksiya bajarilishidan oldin va keyin qo'shimcha kodni ishlatadi.",
        "duration": 25
    },
    {
        "id": "q19",
        "question": "Python Generator funksiyalarida `return` o'rniga qaysi kalit so'z ishlatiladi?",
        "options": ["yield", "generate", "produce", "emit"],
        "correctAnswer": 0,
        "explanation": "yield kalit so'zi qiymatni ketma-ket generatsiya qilish imkonini beradi.",
        "duration": 20
    },
    {
        "id": "q20",
        "question": "Iterator tugaganda (elementlar qolmaganda) `next()` chaqirilsa qaysi istisno (exception) yuzaga keladi?",
        "options": ["StopIteration", "IndexError", "KeyError", "ValueRangeError"],
        "correctAnswer": 0,
        "explanation": "Iterator tugashini bildirish uchun StopIteration exception uzatiladi.",
        "duration": 20
    },
    {
        "id": "q21",
        "question": "Quyidagi kod natijasida `dict(zip(keys, values))` nima beradi?",
        "codeSnippet": "keys = ['a', 'b', 'c']\nvalues = [10, 20, 30]\nprint(dict(zip(keys, values)))",
        "options": ["{'a': 10, 'b': 20, 'c': 30}", "[('a', 10), ('b', 20), ('c', 30)]", "{10: 'a', 20: 'b', 30: 'c'}", "['a10', 'b20', 'c30']"],
        "correctAnswer": 0,
        "explanation": "zip ikkita ro'yxatni juftlab, dict u bilan lug'at yaratadi.",
        "duration": 20
    },
    {
        "id": "q22",
        "question": "Quyidagi enumerate siklidan keyin `res` nima bo'ladi?",
        "codeSnippet": "names = ['Python', 'Django', 'REST']\nres = list(enumerate(names, start=1))\nprint(res)",
        "options": ["[(1, 'Python'), (2, 'Django'), (3, 'REST')]", "[(0, 'Python'), (1, 'Django'), (2, 'REST')]", "['1-Python', '2-Django', '3-REST']", "[(1, 1), (2, 2), (3, 3)]"],
        "correctAnswer": 0,
        "explanation": "enumerate(..., start=1) 1 dan boshlab indeks tayinlaydi.",
        "duration": 20
    },
    {
        "id": "q23",
        "question": "Ichma-ich joylashgan ro'yxatlarni (nested lists) bir-biridan to'liq va mustaqil nusxalash uchun qaysi metod ishlatiladi?",
        "options": ["copy.deepcopy()", "copy.copy()", "list.copy()", "list[:]"],
        "correctAnswer": 0,
        "explanation": "deepcopy ichki barcha chuqur obyeqtlarni ham yangidan nusxalaydi.",
        "duration": 20
    },
    {
        "id": "q24",
        "question": "Quyidagi `all()` va `any()` natijalari nima chiqadi?",
        "codeSnippet": "a = [True, True, False]\nprint(all(a), any(a))",
        "options": ["False True", "True True", "False False", "True False"],
        "correctAnswer": 0,
        "explanation": "all faqat hammasi True bo'lsa True, any bittasi True bo'lsa ham True qaytaradi.",
        "duration": 20
    },
    {
        "id": "q25",
        "question": "Quyidagi string amali bajarilgach, natijada nima hosil bo'ladi?",
        "codeSnippet": "words = ['Python', 'Dars', 'Reja']\nres = '-'.join(words)\nprint(res)",
        "options": ["'Python-Dars-Reja'", "['Python', 'Dars', 'Reja']", "'Python Dars Reja'", "'Python-Dars-Reja-'"],
        "correctAnswer": 0,
        "explanation": "join elementi ro'yxat elementlarini ko'rsatilgan belgi bilan birlashtiradi.",
        "duration": 20
    },
    {
        "id": "q26",
        "question": "Python'da `is` va `==` operatorlari o'rtasidagi asosiy farq nima?",
        "options": ["'==' qiymatlarni tengligini, 'is' esa xotiradagi manzili (id) bir xilligini tekshiradi", "'is' qiymatlarni tengligini tekshiradi", "Ular bir xil ishlaydi", "'==' faqat sonlar uchun ishlatiladi"],
        "correctAnswer": 0,
        "explanation": "== qiymatni, is esa identity (id(x) == id(y)) ni tekshiradi.",
        "duration": 20
    },
    {
        "id": "q27",
        "question": "Quyidagi kod ikki marta chaqirilgach, ikkinchi natija nima chiqadi?",
        "codeSnippet": "def add_item(val, arr=[]):\n    arr.append(val)\n    return arr\nadd_item(1)\nprint(add_item(2))",
        "options": ["[1, 2]", "[2]", "[1]", "[2, 2]"],
        "correctAnswer": 0,
        "explanation": "Python'da mutable default argument (arr=[]) funktsiya e'lon qilinganda bir marta hosil qilinadi va saqlanib qoladi.",
        "duration": 25
    },
    {
        "id": "q28",
        "question": "Fayl to'g'ridan-to'g'ri ishga tushirilganda Python'da `__name__` o'zgaruvchisining qiymati nima bo'ladi?",
        "options": ["'__main__'", "'__file__'", "'main'", "'root'"],
        "correctAnswer": 0,
        "explanation": "Fayl asosiy (main) skript sifatida bajarilganda __name__ qiymati '__main__' bo'ladi.",
        "duration": 20
    },
    {
        "id": "q29",
        "question": "Python sinflarida `@property` dekoratorining asosiy vazifasi nima?",
        "options": ["Metodni atribut kabi qavssiz () chaqiriladigan qilish", "Metodni statik qilish", "Metodni sinf metodiga o'tkazish", "Metodni o'chirish"],
        "correctAnswer": 0,
        "explanation": "@property metodni xossalarga (attribute) o'xshab getter shaklida chaqirish imkonini beradi.",
        "duration": 20
    },
    {
        "id": "q30",
        "question": "Quyidagi kod bajarilgach, `len(data)` nechaga teng bo'ladi?",
        "codeSnippet": "data = {1, True, 1.0, '1', (1,)}\nprint(len(data))",
        "options": ["3", "5", "4", "2"],
        "correctAnswer": 0,
        "explanation": "1, True, 1.0 bitta hash va unikal qiymat (1) deb qaraladi. Shuning uchun set ichida faqat 1, '1' va (1,) qoladi (3 ta element).",
        "duration": 25
    }
]

def seed_master_template():
    print("🚀 Seeding Marimov Game Zone Master 30-Question Template (1-23 lessons)...")

    template_id = "master-tpl-1-to-23"
    title = "🏆 Marimov Game Zone: 1-darsdan 23-darsgacha Kompleks 30 ta Test"
    description = "1-darsdan 23-darsgacha bo'lgan barcha Python mavzulari (Sintaksis, List/Dict/Set, Funktsiyalar, OOP, Exceptions, File I/O, Decorators) bo'yicha mukammal 30 ta qiyin va amaliy savollar."
    category = "Marimov Game Master"
    lesson_ids = list(range(1, 24))

    template_obj, created = QuizTemplate.objects.update_or_create(
        template_id=template_id,
        defaults={
            "title": title,
            "description": description,
            "category": category,
            "question_count": 30,
            "difficulty": "hard",
            "lesson_ids": lesson_ids,
            "custom_questions": MASTER_30_QUESTIONS
        }
    )

    action = "Created" if created else "Updated"
    print(f"✅ [{action}] QuizTemplate '{template_obj.title}' with {len(MASTER_30_QUESTIONS)} questions successfully saved to DB!")

if __name__ == "__main__":
    seed_master_template()
