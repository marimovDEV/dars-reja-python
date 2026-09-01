import os
import re
import json
import random
from .models import Lesson

def shuffle_question_options(q):
    """
    Randomly shuffles the 4 options of a question and updates correctOptionIndex accordingly
    so that correct answers are evenly distributed among A (0), B (1), C (2), D (3).
    """
    options = list(q.get('options', []))
    if len(options) != 4:
        return q
    
    orig_idx = q.get('correctOptionIndex', 0)
    if not isinstance(orig_idx, int) or orig_idx < 0 or orig_idx >= 4:
        orig_idx = 0
        
    correct_value = options[orig_idx]
    
    # Shuffle options randomly
    random.shuffle(options)
    new_correct_idx = options.index(correct_value)
    
    q['options'] = options
    q['correctOptionIndex'] = new_correct_idx
    return q

def validate_and_clean_questions(questions):
    """
    Strictly validates, sanitizes, and randomly shuffles option positions.
    """
    valid = []
    if not isinstance(questions, list):
        return []
    for q in questions:
        if not isinstance(q, dict):
            continue
        question_text = q.get('question')
        options = q.get('options')
        correct_idx = q.get('correctOptionIndex')
        
        if not question_text or not isinstance(options, list) or len(options) != 4:
            continue
        if not isinstance(correct_idx, int) or correct_idx < 0 or correct_idx > 3:
            correct_idx = 0

        # Clean any "X-dars:" prefix from question text
        clean_text = str(question_text)
        clean_text = re.sub(r'^\d+[\s\-_]*dars[:\s\-_]*', '', clean_text, flags=re.IGNORECASE)
        clean_text = re.sub(r'^\d+[\s\-_]*darsniki[:\s\-_]*', '', clean_text, flags=re.IGNORECASE)
            
        shuffled_q = shuffle_question_options({
            "question": clean_text.strip(),
            "type": "single_choice",
            "options": [str(opt) for opt in options],
            "correctOptionIndex": int(correct_idx),
            "explanation": str(q.get('explanation', '')),
            "lessonId": int(q.get('lessonId', 1)),
            "durationSeconds": int(q.get('durationSeconds', 20)),
            "codeSnippet": q.get('codeSnippet') or q.get('code') or None,
            "imageUrl": q.get('imageUrl') or None
        })
        valid.append(shuffled_q)
    return valid

def generate_local_fallback_questions(lessons_in_db, docs_dir, target_count):
    """
    Generates authentic, high-challenge Python & Django technical questions with plausible distractors.
    """
    pool = [
        {
            "question": "Python'da ro'yxatning (list) oxiriga yangi element qo'shish uchun qaysi metod ishlatiladi?",
            "options": ["append()", "extend()", "insert()", "add()"],
            "correctOptionIndex": 0,
            "explanation": "append() metodi ro'yxat oxiriga bitta element qo'shadi. extend() esa boshqa ketma-ketlikni ulash uchun ishlatiladi.",
            "durationSeconds": 20
        },
        {
            "question": "Python'da matnli (string) ma'lumot turini e'lon qilishda qaysi tur belgilanadi?",
            "options": ["str", "string", "text", "varchar"],
            "correctOptionIndex": 0,
            "explanation": "Python'da matnlar uchun o'rnatilgan tur 'str' hisoblanadi.",
            "durationSeconds": 20
        },
        {
            "question": "Dictionary (lug'at) ning barcha kalitlarini ro'yxat ko'rinishida olish uchun qaysi metod ishlatiladi?",
            "options": ["keys()", "values()", "items()", "all_keys()"],
            "correctOptionIndex": 0,
            "explanation": "keys() metodi lug'atdagi barcha kalitlarni (keys) qaytaradi. values() qiymatlarni, items() esa kalit-qiymat juftliklarini beradi.",
            "durationSeconds": 20
        },
        {
            "question": "Python'da o'zgartirib bo'lmaydigan (immutable) ketma-ketlik ma'lumot turi qaysi?",
            "options": ["tuple", "list", "dict", "set"],
            "correctOptionIndex": 0,
            "explanation": "tuple (kortej) yaratilgach, uning elementlarini o'zgartirib yoki o'chirib bo'lmaydi.",
            "durationSeconds": 20
        },
        {
            "question": "Ro'yxat (list) elementini berilgan indeks bo'yicha sug'urib olish va o'chirish uchun qaysi metod ishlatiladi?",
            "options": ["pop()", "remove()", "del", "clear()"],
            "correctOptionIndex": 0,
            "explanation": "pop(index) ko'rsatilgan indeksdagi elementni qaytaradi va ro'yxatdan o'chiradi.",
            "durationSeconds": 20
        },
        {
            "question": "Django proyektida yangi ilova (app) yaratish uchun qaysi buyruq ishlatiladi?",
            "options": ["python manage.py startapp app_name", "django-admin createapp app_name", "python manage.py newapp app_name", "django init app_name"],
            "correctOptionIndex": 0,
            "explanation": "startapp buyrug'i Django proyektida yangi ilova papkasi va strukturani tuzadi.",
            "durationSeconds": 20
        },
        {
            "question": "Python'da funksiya (function) ta'riflash uchun qaysi kalit so'z ishlatiladi?",
            "options": ["def", "func", "function", "define"],
            "correctOptionIndex": 0,
            "explanation": "Python'da funksiyalar 'def' (define) kalit so'zi orqali e'lon qilinadi.",
            "durationSeconds": 20
        },
        {
            "question": "Django ORM yordamida ma'lumotlar bazasidagi barcha obyektlarni olish uchun qanday so'rov yoziladi?",
            "options": ["Model.objects.all()", "Model.objects.get_all()", "Model.select_all()", "Model.fetch_all()"],
            "correctOptionIndex": 0,
            "explanation": "Django ORM'da barcha qatorlarni olish uchun Model.objects.all() QuerySet ishlatiladi.",
            "durationSeconds": 20
        },
        {
            "question": "Python'da shartli tarmoqlanishda aks holda (aks shart) bloki qaysi kalit so'z bilan beriladi?",
            "options": ["else", "elseif", "then", "otherwise"],
            "correctOptionIndex": 0,
            "explanation": "if / elif shartlari bajarilmaganda aks holda bloki 'else:' deb yoziladi.",
            "durationSeconds": 20
        },
        {
            "question": "REST API so'rovida mavjud resursni to'liq yangilash uchun qaysi HTTP metodi qo'llaniladi?",
            "options": ["PUT", "POST", "GET", "DELETE"],
            "correctOptionIndex": 0,
            "explanation": "PUT metodi resursni to'liq almashtirish/yangilash uchun, PATCH esa qisman yangilash uchun ishlatiladi.",
            "durationSeconds": 20
        },
        {
            "question": "Python'da kod xatolarini ushlash va qayta ishlash uchun qaysi blok ishlatiladi?",
            "options": ["try ... except", "try ... catch", "do ... catch", "begin ... rescue"],
            "correctOptionIndex": 0,
            "explanation": "Python'da istisnolarni ushlash try va except kalit so'zlari orqali bajariladi.",
            "durationSeconds": 20
        },
        {
            "question": "Python'da ikkita to'plamning (set) umumiy kesishgan elementlarini topish uchun qaysi operator yoki metod ishlatiladi?",
            "options": ["intersection() yoki &", "union() yoki |", "difference() yoki -", "symmetric_difference()"],
            "correctOptionIndex": 0,
            "explanation": "intersection() metodi yoki & binar operatori ikkita to'plamning faqat umumiy elementlarini qaytaradi.",
            "durationSeconds": 20
        }
    ]

    # Include any custom quizQuestions stored in DB lessons
    for l in lessons_in_db:
        if l.quiz_questions:
            for q in l.quiz_questions:
                if isinstance(q, dict) and "question" in q and "options" in q:
                    pool.append({
                        "question": q["question"],
                        "type": "single_choice",
                        "options": q["options"],
                        "correctOptionIndex": q.get("correctOptionIndex", 0),
                        "explanation": q.get("explanation", "Texnik savol javobi."),
                        "lessonId": l.lesson_number,
                        "durationSeconds": 20
                    })

    random.shuffle(pool)

    # Duplicate and vary questions if needed to reach exact target_count
    result = list(pool)
    index = 0
    while len(result) < target_count and len(pool) > 0:
        base_q = pool[index % len(pool)]
        cloned = dict(base_q)
        result.append(cloned)
        index += 1

    return validate_and_clean_questions(result[:target_count])

def generate_ai_quiz(lesson_numbers, question_count=10, difficulty="mixed", include_code=True, language="uz"):
    """
    Generates professional Python/Django quiz questions with Gemini AI API or robust fallback.
    Guarantees returning EXACTLY question_count questions with direct, clear phrasing & realistic distractors.
    """
    lesson_texts = []
    lessons_in_db = Lesson.objects.filter(lesson_number__in=lesson_numbers).order_by('lesson_number')
    
    docs_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "lesson_docs")
    
    for l in lessons_in_db:
        num = l.lesson_number
        file_path = os.path.join(docs_dir, f"dars_{num:02d}.md")
        content = ""
        if os.path.exists(file_path):
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()
            except Exception:
                pass
        if not content:
            content = f"{l.title}\n{l.description}\n{l.content}"
        
        content_snippet = content[:3000] if len(content) > 3000 else content
        lesson_texts.append(f"--- MAVZU: {l.title} ---\n{content_snippet}")

    combined_text = "\n\n".join(lesson_texts)
    
    api_key = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
    code_text = "Ha" if include_code else "Yo'q"
    
    if api_key and combined_text:
        try:
            from google import genai
            from google.genai import types
            
            client = genai.Client(api_key=api_key)
            prompt = f"""Siz Python va Django Backend dasturlash bo'yicha professional test tuzuvchi mutaxassissiz.

Quyidagi dars materiallaridan foydalanib, ANIQ {question_count} TA PROFESSIONAL TEST SAVOLI YARATING:
Darslar ro'yxati: {lesson_numbers}
Qiyinlik darajasi: {difficulty} (oson bo'lsa mantiqiy va tushunarli, murakkab bo'lsa real kod xatolar va sintaksisni sinaydigan bo'lsin)
Kodli savollar bo'lsinmi: {code_text}
Til: {language}

Darslar materiallari:
{combined_text[:12000]}

QAT'IY QOIDALAR (MUST FOLLOW):
1. SAVOL MATNIDA HECH QACHON "5-darsniki", "1-dars:", "Dars maqsadi nima" kabi so'zlarni ishlatmang! Savol to'g'ridan-to'g mezon aniq va professional texnik savol bo'lsin. (Masalan: "Python'da lug'atning barcha qiymatlarini olish uchun qaysi metod ishlatiladi?")
2. HAR BIR SAVOLDA ANIQ 4 TA VARIANT BO'LSIN.
3. NOTO'G'RI 3 TA VARIANT HAM O'QUVCHINI O'YLANISHGA MAJBUR QILADIGAN REAL PYTHON SINTAKSIS / METODLARI BO'LSIN. (Chalg'ituvchi bo'lsin, kulgili/aloqasiz javob yozmang!).
4. 'correctOptionIndex' (0, 1, 2, 3) to'g'ri ko'rsatilsin va variantlar tasodifiy aralashtirilsin.
5. Javobning o'zbek tilidagi qisqa va tushunarli texnik tushuntirishi ('explanation') bo'lsin.
6. 'durationSeconds': 20 soniya.

JAVOBNI FAQAT QUYIDAGI SOF JSON ARRAY FORMATIDA QAYTARING (boshqa hech qanday izoh yozmang):
[
  {{
    "question": "Python'da ro'yxat oxiriga element qo'shish uchun qaysi metod ishlatiladi?",
    "type": "single_choice",
    "options": ["append()", "extend()", "insert()", "add()"],
    "correctOptionIndex": 0,
    "explanation": "append() metodi ro'yxat oxiriga bitta element qo'shadi.",
    "lessonId": 1,
    "durationSeconds": 20
  }}
]
"""

            response = client.models.generate_content(
                model='gemini-1.5-flash',
                contents=prompt,
                config=types.GenerateContentConfig(
                    response_mime_type="application/json",
                    temperature=0.7
                )
            )

            if response and response.text:
                clean_json_str = response.text.strip()
                clean_json_str = re.sub(r'^```json\s*', '', clean_json_str)
                clean_json_str = re.sub(r'\s*```$', '', clean_json_str)
                raw_questions = json.loads(clean_json_str)
                validated = validate_and_clean_questions(raw_questions)
                if len(validated) >= question_count:
                    return validated[:question_count]
                elif len(validated) > 0:
                    extra = generate_local_fallback_questions(lessons_in_db, docs_dir, question_count - len(validated))
                    combined = validated + extra
                    return combined[:question_count]
        except Exception as e:
            print("Gemini API generation error, falling back to local extractor:", e)

    # Fallback extractor
    return generate_local_fallback_questions(lessons_in_db, docs_dir, question_count)
