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
            
        shuffled_q = shuffle_question_options({
            "question": str(question_text),
            "type": "single_choice",
            "options": [str(opt) for opt in options],
            "correctOptionIndex": int(correct_idx),
            "explanation": str(q.get('explanation', '')),
            "lessonId": int(q.get('lessonId', 1)),
            "durationSeconds": int(q.get('durationSeconds', 20))
        })
        valid.append(shuffled_q)
    return valid

def generate_local_fallback_questions(lessons_in_db, docs_dir, target_count):
    """
    Generates rich local questions using lesson topics, goals, content & quizQuestions
    to guarantee target_count (e.g., 10, 15, 20) questions.
    """
    pool = []
    
    for l in lessons_in_db:
        num = l.lesson_number
        title = l.title
        goal = l.goal or f"{title} bo'yicha amaliy va nazariy ko'nikmalar"

        # 1. Standard quizQuestions from DB if present
        if l.quiz_questions:
            for q in l.quiz_questions:
                if isinstance(q, dict) and "question" in q and "options" in q:
                    pool.append({
                        "question": q["question"],
                        "type": "single_choice",
                        "options": q["options"],
                        "correctOptionIndex": q.get("correctOptionIndex", 0),
                        "explanation": q.get("explanation", f"{title} mavzusi bo'yicha nazariy javob."),
                        "lessonId": num,
                        "durationSeconds": 20
                    })

        # 2. Main Goal Question
        pool.append({
            "question": f"{num}-dars ('{title}') o'rganilishining asosiy maqsadi nima?",
            "type": "single_choice",
            "options": [
                goal,
                "Ma'lumotlar bazasini tozalash va o'chirish",
                "Operatsion tizimni qayta o'rnatish",
                "Frontend dizayn ranglarini o'zgartirish"
            ],
            "correctOptionIndex": 0,
            "explanation": f"{title} darsining asosiy maqsadi — {goal}.",
            "lessonId": num,
            "durationSeconds": 20
        })

        # 3. Best Practice / Convention Question
        pool.append({
            "question": f"'{title}' mavzusida kod yozishda qaysi tamoyilga amal qilish tavsiya etiladi?",
            "type": "single_choice",
            "options": [
                f"PEP 8 standartlariga va clean code qoidalariga rioya qilish",
                "Barcha o'zgaruvchilarni bitta harf bilan nomlash",
                "Izohlardan umuman foydalanmaslik",
                "Koddagi barcha xatoliklarni pass bilan yashirish"
            ],
            "correctOptionIndex": 0,
            "explanation": "Python va backend dasturlashda clean code va PEP 8 tamoyillariga amal qilish shart.",
            "lessonId": num,
            "durationSeconds": 20
        })

        # 4. Debugging & Error Handling Question
        pool.append({
            "question": f"'{title}' bo'yicha kodingizda xatolik yuz bersa, birinchi navbatda nima qilish kerak?",
            "type": "single_choice",
            "options": [
                "Terminaldagi xatolik xabarini (Traceback) diqqat bilan o'qish",
                "Kodni butunlay o'chirib tashlash",
                "Kompyuterni o'chirib yoqish",
                "Barcha fayllarni qayta nomlash"
            ],
            "correctOptionIndex": 0,
            "explanation": "Dasturlashda Traceback xabari xatolik yuz bergan fayl va qatorni ko'rsatadi.",
            "lessonId": num,
            "durationSeconds": 20
        })

        # 5. Concept Verification Question
        pool.append({
            "question": f"'{title}' moduli loyihaga qanday integratsiya qilinadi?",
            "type": "single_choice",
            "options": [
                f"{title} uchun to'g'ri mantiqiy struktura va sintaksisdan foydalanib",
                "Faqat CSS fayllarini o'zgartirish orqali",
                "Notion sahifasini o'chirish orqali",
                "Internet tarmoqni uzib qo'yish orqali"
            ],
            "correctOptionIndex": 0,
            "explanation": f"{title} moduli backend mantiqining uzviy qismi hisoblanadi.",
            "lessonId": num,
            "durationSeconds": 20
        })

    # Shuffle initial pool
    random.shuffle(pool)

    # If pool is smaller than target_count, duplicate and vary questions to reach exact count
    result = list(pool)
    index = 0
    while len(result) < target_count and len(pool) > 0:
        base_q = pool[index % len(pool)]
        cloned = dict(base_q)
        cloned["question"] = f"[Amaliyot] {cloned['question']}"
        result.append(cloned)
        index += 1

    return validate_and_clean_questions(result[:target_count])

def generate_ai_quiz(lesson_numbers, question_count=10, difficulty="mixed", include_code=True, language="uz"):
    """
    Generates quiz questions based on selected lesson_numbers using Gemini AI API or robust fallback.
    Guarantees returning EXACTLY question_count (e.g., 5, 10, 15, 20) questions.
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
        lesson_texts.append(f"--- DARS {num}: {l.title} ---\n{content_snippet}")

    combined_text = "\n\n".join(lesson_texts)
    
    api_key = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
    code_text = "Ha" if include_code else "Yo'q"
    
    if api_key and combined_text:
        try:
            from google import genai
            from google.genai import types
            
            client = genai.Client(api_key=api_key)
            prompt = f"""Siz Python Backend o'quv kursi bo'yicha jonli test (quiz) yaratuvchi AI ekspertisiz.

Quyidagi darslar materialidan foydalanib, ANIQ {question_count} TA TEST SAVOLI YARATING (kam ham, ko'p ham bo'lmasin):
Darslar ro'yxati: {lesson_numbers}
Qiyinlik darajasi: {difficulty}
Kodli savollar bo'lsinmi: {code_text}
Til: {language}

Darslar materiallari:
{combined_text[:12000]}

TALABLAR:
1. Aniq {question_count} ta bir-birini takrorlamaydigan savol yarating.
2. Har bir savolda aniq 4 ta variant bo'lsin.
3. 'correctOptionIndex' (0, 1, 2, 3) to'g'ri ko'rsatilsin va variantlar orasida tasodifiy aralashtirilsin (hammasi A javob bo'lmasin).
4. Javobning o'zbek tilidagi qisqa tushuntirishi ('explanation') bo'lsin.
5. Har bir savol uchun tegishli 'lessonId' (dars raqami) ko'rsatilsin.
6. 'durationSeconds': 20 soniya.

JAVOBNI FAQAT QUYIDAGI SOF JSON ARRAY FORMATIDA QAYTARING (boshqa hech qanday izoh va markdown yozmang):
[
  {{
    "question": "Savol matni",
    "type": "single_choice",
    "options": ["A variant", "B variant", "C variant", "D variant"],
    "correctOptionIndex": 0,
    "explanation": "Nima uchun to'g'ri ekanligi tushuntirish",
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
                    # Supplement with local fallback if Gemini generated fewer than question_count
                    extra = generate_local_fallback_questions(lessons_in_db, docs_dir, question_count - len(validated))
                    combined = validated + extra
                    return combined[:question_count]
        except Exception as e:
            print("Gemini API generation error, falling back to local extractor:", e)

    # Fallback extractor: Guarantee returning EXACTLY question_count questions
    return generate_local_fallback_questions(lessons_in_db, docs_dir, question_count)
