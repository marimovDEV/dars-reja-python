import os
import sys
import json
import django

# Setup Django environment
sys.path.append(os.path.dirname(__file__))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from lessons_app.models import Lesson

LESSONS_JSON = os.path.join(os.path.dirname(__file__), "..", "frontend", "src", "data", "lessons.json")

def seed():
    if not os.path.exists(LESSONS_JSON):
        print(f"Xato: {LESSONS_JSON} topilmadi!")
        return

    with open(LESSONS_JSON, "r", encoding="utf-8") as f:
        lessons_data = json.load(f)

    print(f"📦 JSON faylda {len(lessons_data)} ta dars topildi.")
    
    count = 0
    for item in lessons_data:
        lesson_id = item.get("id") or f"les-{item.get('lessonNumber', count+1)}"
        lesson, created = Lesson.objects.update_or_create(
            lesson_id=lesson_id,
            defaults={
                "lesson_number": item.get("lessonNumber", count + 1),
                "title": item.get("title", f"{count+1}-dars"),
                "date": item.get("date", ""),
                "time": item.get("time", "14:00 - 16:00"),
                "status": item.get("status", "planned"),
                "description": item.get("description", ""),
                "content": item.get("content", ""),
                "homework": item.get("homework", ""),
                "materials": item.get("materials", []),
                "tasks": item.get("tasks", [])
            }
        )
        count += 1

    print(f"✅ Django SQLite ma'lumotlar bazasiga {count} ta dars muvaffaqiyatli saqlandi!")

if __name__ == "__main__":
    seed()
