import os
import re
import json
import random
from .models import Lesson

def validate_and_clean_questions(questions):
    """
    Strictly validates and sanitizes AI generated JSON questions.
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
            continue
            
        valid.append({
            "question": str(question_text),
            "type": "single_choice",
            "options": [str(opt) for opt in options],
            "correctOptionIndex": int(correct_idx),
            "explanation": str(q.get('explanation', '')),
            "lessonId": int(q.get('lessonId', 1)),
            "durationSeconds": int(q.get('durationSeconds', 20))
        })
    return valid

def generate_ai_quiz(lesson_numbers, question_count=10, difficulty="mixed", include_code=True, language="uz"):
    """
    Generates quiz questions based on selected lesson_numbers using Gemini AI API or robust fallback.
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

Quyidagi darslar materialidan foydalanib, JAMI {question_count} TA TEST SAVOLI YARATING:
Darslar ro'yxati: {lesson_numbers}
Qiyinlik darajasi: {difficulty}
Kodli savollar bo'lsinmi: {code_text}
Til: {language}

Darslar materiallari:
{combined_text[:12000]}

TALABLAR:
1. Har bir savol tanlangan darslar materiallaridan kelib chiqishi shart.
2. Har bir savolda aniq 4 ta variant bo'lsin.
3. 'correctOptionIndex' (0, 1, 2, 3) to'g'ri ko'rsatilsin.
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
                if len(validated) > 0:
                    return validated[:question_count]
        except Exception as e:
            print("Gemini API generation error, falling back to local extractor:", e)

    # Fallback extractor: Generate high-quality questions from lesson content & quizQuestions in DB
    fallback_questions = []
    for l in lessons_in_db:
        num = l.lesson_number
        if l.quiz_questions:
            for q in l.quiz_questions:
                if isinstance(q, dict) and "question" in q:
                    fallback_questions.append({
                        "question": q["question"],
                        "type": "single_choice",
                        "options": q.get("options", ["Variant 1", "Variant 2", "Variant 3", "Variant 4"]),
                        "correctOptionIndex": q.get("correctOptionIndex", 0),
                        "explanation": q.get("explanation", f"{l.title} bo'yicha nazariy tushuncha."),
                        "lessonId": num,
                        "durationSeconds": 20
                    })
        fallback_questions.append({
            "question": f"{num}-dars: '{l.title}' mavzusining asosiy maqsadi nima?",
            "type": "single_choice",
            "options": [
                l.goal or f"{l.title} mavzusini mukammal o'zlashtirish",
                "Python tilini o'rnatmasdan ishga tushirish",
                "Ma'lumotlar bazasini o'chirib tashlash",
                "HTML fayllarni saqlash"
            ],
            "correctOptionIndex": 0,
            "explanation": f"{l.title} darsi aynan shu mavzuni o'rgatadi.",
            "lessonId": num,
            "durationSeconds": 20
        })

    random.shuffle(fallback_questions)
    return validate_and_clean_questions(fallback_questions[:question_count])
