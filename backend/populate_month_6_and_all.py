import os
import sys
import django

# Setup Django Environment
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from lessons_app.models import Lesson

DOCS_DIR = os.path.join(os.path.dirname(__file__), "lesson_docs")
os.makedirs(DOCS_DIR, exist_ok=True)

# Helper function to generate full 19-section Markdown string
def generate_full_markdown(
    number: int,
    emoji: str,
    title: str,
    intro: str,
    abilities: list,
    goals: list,
    prereqs: list,
    terms: list,
    syntax_code: str,
    syntax_explanation: str,
    table_rows: list,
    examples: list,
    real_project_title: str,
    real_project_code: str,
    real_project_explanation: str,
    errors: list,
    tasks: dict,
    homework: list,
    quiz_questions: list,
    summary: list,
    next_lesson_title: str,
    resources: list
) -> str:
    md = []
    
    # 1. Title
    md.append(f"# {emoji} {number}. {title} — Dars dokumentatsiyasi\n")
    
    # 2. Intro (2-4 paragraphs)
    md.append(f"{intro}\n")
    
    # 3. Abilities
    md.append("## Bu mavzu orqali nimalar qilish mumkin\n")
    for item in abilities:
        md.append(f"- {item};")
    md.append("\n")

    # 4. Goals
    md.append("## Dars maqsadi\n")
    md.append("Bu dars oxirida o'quvchi:\n")
    for item in goals:
        md.append(f"- {item};")
    md.append("ni mustaqil bajara oladi.\n")

    # 5. Prerequisites
    md.append("## Kerakli oldingi bilimlar\n")
    md.append("Bu darsni tushunish uchun:\n")
    for item in prereqs:
        md.append(f"- {item};")
    md.append("bilinishi kerak.\n")

    # 6. Terms
    md.append("## Asosiy tushunchalar va atamalar\n")
    for t_name, t_def in terms:
        md.append(f"## {t_name} nima?\n")
        md.append(f"> **{t_name}** — {t_def}\n")

    # 7. Syntax
    md.append("## Sintaksis va uning izohi\n")
    md.append(f"```python\n{syntax_code}\n```\n")
    md.append(f"{syntax_explanation}\n")

    # 8. Tables
    md.append("## Jadvallar (Metodlar, parametrlar va klasslar)\n")
    md.append("| Nomi / Parametr | Vazifasi | Turi / Parametrlari | Misol | Ko'p uchraydigan xatosi |")
    md.append("|---|---|---|---|---|")
    for r in table_rows:
        md.append(f"| `{r[0]}` | {r[1]} | `{r[2]}` | `{r[3]}` | {r[4]} |")
    md.append("\n")

    # 9. Examples (8 working code examples)
    md.append("## Kod misollari (8 ta to'liq amaliy misol)\n")
    for idx, ex in enumerate(examples, start=1):
        md.append(f"### Misol {idx} — {ex['name']}\n")
        md.append(f"```python\n{ex['code']}\n```\n")
        if 'output' in ex:
            md.append(f"**Natija:**\n```text\n{ex['output']}\n```\n")
        md.append(f"**Izoh:** {ex['explanation']}\n")
        md.append(f"**Qachon ishlatiladi:** {ex['context']}\n")

    # 10. Real Project Example
    md.append(f"## Real loyiha misoli: {real_project_title}\n")
    md.append(f"```python\n{real_project_code}\n```\n")
    md.append(f"{real_project_explanation}\n")

    # 11. Common Errors
    md.append("## Ko'p uchraydigan xatolar\n")
    for idx, err in enumerate(errors, start=1):
        md.append(f"### Xato {idx}: {err['title']}\n")
        md.append(f"**Noto'g'ri:**\n```python\n{err['wrong']}\n```\n")
        md.append(f"**Nima uchun xato:** {err['reason']}\n")
        md.append(f"**To'g'ri:**\n```python\n{err['correct']}\n```\n")
        md.append(f"**Qanday oldini olish:** {err['fix']}\n")

    # 12. 3-Level Practical Tasks
    md.append("## 3 darajali amaliy topshiriqlar\n")
    md.append(f"### 1-topshiriq — Oson\n**Vazifa:** {tasks['easy']}\n")
    md.append(f"### 2-topshiriq — O'rta\n**Vazifa:** {tasks['medium']}\n")
    md.append(f"### 3-topshiriq — Murakkab\n**Vazifa:** {tasks['hard']}\n")

    # 13. Homework
    md.append("## Uyga vazifa\n")
    for idx, hw in enumerate(homework, start=1):
        md.append(f"{idx}. {hw};")
    md.append("\n")

    # 14. Quiz Questions
    md.append("## Test savollari\n")
    for idx, q in enumerate(quiz_questions, start=1):
        md.append(f"{idx}. {q['question']}")
    md.append("\n")

    # 15. Quiz Answers
    md.append("## Test javoblari\n")
    for idx, q in enumerate(quiz_questions, start=1):
        md.append(f"**{idx}.** {q['answer']}\n")

    # 16. Summary
    md.append("## Qisqa xulosa\n")
    md.append("Bu darsda:\n")
    for item in summary:
        md.append(f"- {item};")
    md.append("o'rganildi.\n")

    # 17. Next Lesson Link
    md.append(f"Keyingi **{number+1}-dars: {next_lesson_title}** da ushbu bilimlar yanada chuqurlashtiriladi.\n")

    # 18. Additional Resources
    md.append("## Qo'shimcha resurslar\n")
    for res in resources:
        md.append(f"- {res}")

    return "\n".join(md)

print("Helper ready. Now building complete datasets for 61-72...")
