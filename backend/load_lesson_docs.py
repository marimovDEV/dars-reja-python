import os
import sys
import json
import django

sys.path.append(os.path.dirname(__file__))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from lessons_app.models import Lesson

LESSONS_JSON = os.path.join(os.path.dirname(__file__), "..", "frontend", "src", "data", "lessons.json")
DOCS_DIR = os.path.join(os.path.dirname(__file__), "lesson_docs")

def load_and_save(start, end):
    """Loads markdown files from lesson_docs/ and saves to DB + JSON."""
    print(f"{'='*60}")
    print(f"  {start}-DARSDAN {end}-DARSGACHA YUKLASH BOSHLANDI")
    print(f"{'='*60}")

    all_lessons = list(Lesson.objects.all().order_by('lesson_number'))

    for num in range(start, end + 1):
        filepath = os.path.join(DOCS_DIR, f"dars_{num:02d}.md")
        if not os.path.exists(filepath):
            print(f"⚠️  {filepath} topilmadi, o'tkazib yuborildi.")
            continue

        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        lesson_obj = next((l for l in all_lessons if l.lesson_number == num), None)
        if lesson_obj:
            lesson_obj.content = content
            lesson_obj.save()
            print(f"✅ [{num}-DARS] DB ga saqlandi ({len(content)} belgi)")
        else:
            print(f"⚠️  {num}-dars bazada topilmadi!")

    # Update JSON
    with open(LESSONS_JSON, "r", encoding="utf-8") as f:
        json_data = json.load(f)

    for item in json_data:
        n = item.get("lessonNumber")
        if start <= n <= end:
            filepath = os.path.join(DOCS_DIR, f"dars_{n:02d}.md")
            if os.path.exists(filepath):
                with open(filepath, "r", encoding="utf-8") as f:
                    item["content"] = f.read()

    with open(LESSONS_JSON, "w", encoding="utf-8") as f:
        json.dump(json_data, f, ensure_ascii=False, indent=2)

    print(f"{'='*60}")
    print(f"  ✨ {start}-{end} DARSLAR BAZAGA VA JSON GA SAQLANDI!")
    print(f"{'='*60}")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("start", type=int)
    parser.add_argument("end", type=int)
    args = parser.parse_args()
    load_and_save(args.start, args.end)
