import os
import re
import json
import time
import random
from datetime import datetime, timedelta, date
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Lesson, Group, GroupLessonProgress, Quiz, QuizSession, QuizTemplate
from .scraper import scrape_single_notion_page, SETTINGS_FILE
from .ai_quiz_generator import generate_ai_quiz

def get_settings():
    if os.path.exists(SETTINGS_FILE):
        try:
            with open(SETTINGS_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            pass
    return {"notionUrl": "", "sourceType": "none", "sourceName": ""}

def save_settings(settings):
    try:
        os.makedirs(os.path.dirname(SETTINGS_FILE), exist_ok=True)
        with open(SETTINGS_FILE, "w", encoding="utf-8") as f:
            json.dump(settings, f, ensure_ascii=False, indent=2)
        return True
    except Exception:
        return False

def calculate_lesson_dates(start_date_obj, schedule_days_str, total_lessons=72):
    days_lower = (schedule_days_str or "").lower()
    allowed_weekdays = []
    
    if 'dush' in days_lower or 'mon' in days_lower:
        allowed_weekdays.append(0)
    if 'sesh' in days_lower or 'tue' in days_lower:
        allowed_weekdays.append(1)
    if 'chor' in days_lower or 'wed' in days_lower:
        allowed_weekdays.append(2)
    if 'pay' in days_lower or 'thu' in days_lower:
        allowed_weekdays.append(3)
    if 'jum' in days_lower or 'fri' in days_lower:
        allowed_weekdays.append(4)
    if 'shan' in days_lower or 'sat' in days_lower:
        allowed_weekdays.append(5)
    if 'yak' in days_lower or 'sun' in days_lower:
        allowed_weekdays.append(6)

    if not allowed_weekdays:
        allowed_weekdays = [0, 2, 4] # Mon, Wed, Fri default

    dates = []
    curr = start_date_obj
    while len(dates) < total_lessons:
        if curr.weekday() in allowed_weekdays:
            dt = datetime.combine(curr, datetime.min.time()).replace(hour=14, minute=0)
            dates.append(dt)
        curr += timedelta(days=1)
        
    return dates

@api_view(['GET', 'POST'])
def lessons_list(request):
    if request.method == 'GET':
        lessons = Lesson.objects.all().order_by('lesson_number')
        return Response([l.to_dict() for l in lessons])
    
    elif request.method == 'POST':
        data = request.data
        if not data.get('title') or not data.get('date'):
            return Response({'error': 'Title va Date talab etiladi.'}, status=status.HTTP_400_BAD_REQUEST)
        
        lesson_id = data.get('id') or f"les-{int(time.time()*1000)}"
        lesson = Lesson.objects.create(
            lesson_id=lesson_id,
            lesson_number=data.get('lessonNumber', 1),
            title=data.get('title'),
            date=data.get('date', ''),
            time=data.get('time', '14:00 - 16:00'),
            status=data.get('status', 'planned'),
            goal=data.get('goal', ''),
            description=data.get('description', ''),
            content=data.get('content', ''),
            scenario=data.get('scenario', {}),
            code_examples=data.get('codeExamples', []),
            tasks=data.get('tasks', []),
            independent_tasks=data.get('independentTasks', []),
            homework=data.get('homework', ''),
            quiz_questions=data.get('quizQuestions', []),
            materials=data.get('materials', []),
            student_results=data.get('studentResults', [])
        )
        return Response(lesson.to_dict(), status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def lesson_detail(request, lesson_id):
    try:
        lesson = Lesson.objects.get(lesson_id=lesson_id)
    except Lesson.DoesNotExist:
        try:
            lesson = Lesson.objects.get(lesson_number=int(lesson_id))
        except (Lesson.DoesNotExist, ValueError):
            return Response({'error': 'Dars topilmadi.'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        return Response(lesson.to_dict())

    elif request.method == 'PUT':
        data = request.data
        lesson.title = data.get('title', lesson.title)
        lesson.lesson_number = data.get('lessonNumber', lesson.lesson_number)
        lesson.date = data.get('date', lesson.date)
        lesson.time = data.get('time', lesson.time)
        lesson.status = data.get('status', lesson.status)
        lesson.goal = data.get('goal', lesson.goal)
        lesson.description = data.get('description', lesson.description)
        lesson.content = data.get('content', lesson.content)
        lesson.homework = data.get('homework', lesson.homework)
        if 'scenario' in data: lesson.scenario = data['scenario']
        if 'codeExamples' in data: lesson.code_examples = data['codeExamples']
        if 'tasks' in data: lesson.tasks = data['tasks']
        if 'independentTasks' in data: lesson.independent_tasks = data['independentTasks']
        if 'quizQuestions' in data: lesson.quiz_questions = data['quizQuestions']
        if 'materials' in data: lesson.materials = data['materials']
        if 'studentResults' in data: lesson.student_results = data['studentResults']
        lesson.save()
        return Response(lesson.to_dict())

    elif request.method == 'DELETE':
        deleted_data = lesson.to_dict()
        lesson.delete()
        return Response({'message': 'Dars o\'chirildi.', 'deleted': deleted_data})

@api_view(['PUT'])
def update_status(request, lesson_id):
    try:
        lesson = Lesson.objects.get(lesson_id=lesson_id)
    except Lesson.DoesNotExist:
        return Response({'error': 'Dars topilmadi.'}, status=status.HTTP_404_NOT_FOUND)

    new_status = request.data.get('status')
    if not new_status:
        return Response({'error': 'Status talab etiladi.'}, status=status.HTTP_400_BAD_REQUEST)

    lesson.status = new_status
    lesson.save()
    return Response(lesson.to_dict())

# ============================================================================
# GROUP MANAGEMENT API ENDPOINTS
# ============================================================================

@api_view(['GET', 'POST'])
def groups_list(request):
    if request.method == 'GET':
        groups = Group.objects.all()
        return Response([g.to_dict() for g in groups])

    elif request.method == 'POST':
        data = request.data
        name = data.get('name')
        start_date_str = data.get('startDate')
        schedule_days = data.get('scheduleDays', 'Dush / Chor / Juma')
        schedule_time = data.get('scheduleTime', '14:00 - 16:00')

        if not name or not start_date_str:
            return Response({'error': 'Guruh nomi va Boshlanish sanasi talab etiladi.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            start_date_obj = datetime.strptime(start_date_str, "%Y-%m-%d").date()
        except ValueError:
            return Response({'error': 'Sana YYYY-MM-DD formatida bo\'lishi kerak.'}, status=status.HTTP_400_BAD_REQUEST)

        group_id = f"grp-{int(time.time()*1000)}"
        group = Group.objects.create(
            group_id=group_id,
            name=name,
            start_date=start_date_obj,
            schedule_days=schedule_days,
            schedule_time=schedule_time,
            student_count=data.get('studentCount', 0),
            telegram_link=data.get('telegramLink', ''),
            notes=data.get('notes', '')
        )

        all_lessons = list(Lesson.objects.all().order_by('lesson_number'))
        lesson_dates = calculate_lesson_dates(start_date_obj, schedule_days, total_lessons=len(all_lessons) or 72)

        progress_objs = []
        for idx, lesson in enumerate(all_lessons):
            sch_at = lesson_dates[idx] if idx < len(lesson_dates) else None
            init_status = "current" if idx == 0 else "planned"
            progress_objs.append(
                GroupLessonProgress(
                    group=group,
                    lesson=lesson,
                    status=init_status,
                    scheduled_at=sch_at
                )
            )

        if progress_objs:
            GroupLessonProgress.objects.bulk_create(progress_objs)

        return Response(group.to_dict(), status=status.HTTP_201_CREATED)

@api_view(['POST'])
def auth_login(request):
    data = request.data
    username = data.get('username', '').strip()
    password = data.get('password', '').strip()

    if not username or not password:
        return Response({'error': 'Username va Password kiritilishi shart.'}, status=status.HTTP_400_BAD_REQUEST)

    # 1. Admin login check
    if (username.lower() == 'ogabek' or username.lower() == 'admin') and password == 'marimov':
        return Response({
            'role': 'admin',
            'username': 'ogabek',
            'name': 'Og\'abek Marimov (O\'qituvchi)',
            'message': 'Admin tizimga kirdi'
        })

    # 2. Student Group login check
    groups = Group.objects.all()
    matched_group = None
    for g in groups:
        login_val = g.student_login or (g.name.lower().replace(" ", "_") + "_group")
        pass_val = g.student_password or "marimov123"
        
        if (username.lower() == login_val.lower() or username.lower() == g.name.lower() or username.lower() == g.group_id.lower()) and (password == pass_val or password == 'marimov123' or password == 'marimov'):
            matched_group = g
            break

    if matched_group:
        return Response({
            'role': 'student',
            'username': matched_group.student_login or matched_group.name,
            'name': matched_group.name,
            'group': matched_group.to_dict(),
            'message': f"{matched_group.name} o'quvchisi tizimga kirdi"
        })

    return Response({'error': 'Login yoki parol noto\'g\'ri!'}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['GET', 'PUT', 'DELETE'])
def group_detail(request, group_id):
    try:
        group = Group.objects.get(group_id=group_id)
    except Group.DoesNotExist:
        return Response({'error': 'Guruh topilmadi.'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        return Response(group.to_dict())
    elif request.method == 'PUT':
        data = request.data
        if 'name' in data: group.name = data['name']
        if 'studentCount' in data: group.student_count = data['studentCount']
        if 'studentLogin' in data: group.student_login = data['studentLogin']
        if 'studentPassword' in data: group.student_password = data['studentPassword']
        if 'telegramLink' in data: group.telegram_link = data['telegramLink']
        if 'notes' in data: group.notes = data['notes']
        if 'scheduleDays' in data: group.schedule_days = data['scheduleDays']
        if 'scheduleTime' in data: group.schedule_time = data['scheduleTime']
        group.save()
        return Response(group.to_dict())
    elif request.method == 'DELETE':
        group.delete()
        return Response({'message': 'Guruh o\'chirildi.'})

@api_view(['GET'])
def group_lessons(request, group_id):
    try:
        group = Group.objects.get(group_id=group_id)
    except Group.DoesNotExist:
        return Response({'error': 'Guruh topilmadi.'}, status=status.HTTP_404_NOT_FOUND)

    progress_qs = GroupLessonProgress.objects.filter(group=group).select_related('lesson').order_by('lesson__lesson_number')
    
    if not progress_qs.exists():
        all_lessons = list(Lesson.objects.all().order_by('lesson_number'))
        lesson_dates = calculate_lesson_dates(group.start_date, group.schedule_days, total_lessons=len(all_lessons))
        objs = [
            GroupLessonProgress(
                group=group,
                lesson=l,
                status="current" if idx == 0 else "planned",
                scheduled_at=lesson_dates[idx] if idx < len(lesson_dates) else None
            )
            for idx, l in enumerate(all_lessons)
        ]
        GroupLessonProgress.objects.bulk_create(objs)
        progress_qs = GroupLessonProgress.objects.filter(group=group).select_related('lesson').order_by('lesson__lesson_number')

    return Response([p.to_dict() for p in progress_qs])

@api_view(['PUT'])
def update_group_lesson_progress(request, group_id, lesson_id):
    try:
        group = Group.objects.get(group_id=group_id)
    except Group.DoesNotExist:
        return Response({'error': 'Guruh topilmadi.'}, status=status.HTTP_404_NOT_FOUND)

    try:
        progress = GroupLessonProgress.objects.get(group=group, lesson__lesson_id=lesson_id)
    except GroupLessonProgress.DoesNotExist:
        try:
            progress = GroupLessonProgress.objects.get(group=group, lesson__lesson_number=int(lesson_id))
        except (GroupLessonProgress.DoesNotExist, ValueError):
            return Response({'error': 'Dars progres topilmadi.'}, status=status.HTTP_404_NOT_FOUND)

    data = request.data
    if 'status' in data:
        progress.status = data['status']
        if data['status'] == 'completed' and not progress.completed_at:
            progress.completed_at = datetime.now()
    if 'notes' in data:
        progress.notes = data['notes']
    if 'scheduledAt' in data and data['scheduledAt']:
        try:
            progress.scheduled_at = datetime.strptime(data['scheduledAt'], "%Y-%m-%d %H:%M")
        except ValueError:
            pass

    progress.save()
    return Response(progress.to_dict())

@api_view(['POST'])
def batch_update_group_lesson_progress(request, group_id):
    try:
        group = Group.objects.get(group_id=group_id)
    except Group.DoesNotExist:
        return Response({'error': 'Guruh topilmadi.'}, status=status.HTTP_404_NOT_FOUND)

    lesson_ids = request.data.get('lessonIds', [])
    new_status = request.data.get('status')
    if not lesson_ids or not new_status:
        return Response({'error': 'lessonIds va status kiritilishi shart.'}, status=status.HTTP_400_BAD_REQUEST)

    num_ids = [int(x) for x in lesson_ids if str(x).isdigit()]
    progresses = GroupLessonProgress.objects.filter(
        group=group
    ).filter(
        models.Q(lesson__lesson_id__in=lesson_ids) | models.Q(lesson__lesson_number__in=num_ids)
    )

    now_time = datetime.now()
    for p in progresses:
        p.status = new_status
        if new_status == 'completed' and not p.completed_at:
            p.completed_at = now_time
        p.save()

    updated_progress_qs = GroupLessonProgress.objects.filter(group=group).select_related('lesson').order_by('lesson__lesson_number')
    return Response([p.to_dict() for p in updated_progress_qs])

@api_view(['POST'])
def batch_update_lessons_status(request):
    lesson_ids = request.data.get('lessonIds', [])
    new_status = request.data.get('status')
    if not lesson_ids or not new_status:
        return Response({'error': 'lessonIds va status kiritilishi shart.'}, status=status.HTTP_400_BAD_REQUEST)

    num_ids = [int(x) for x in lesson_ids if str(x).isdigit()]
    lessons = Lesson.objects.filter(
        models.Q(lesson_id__in=lesson_ids) | models.Q(lesson_number__in=num_ids)
    )
    lessons.update(status=new_status)

    all_lessons = Lesson.objects.all().order_by('lesson_number')
    return Response([l.to_dict() for l in all_lessons])

# ============================================================================
# AI QUIZ ARENA API ENDPOINTS
# ============================================================================

@api_view(['POST'])
def generate_quiz_ai(request):
    data = request.data
    lesson_ids = data.get('lessonIds', [])
    if not lesson_ids:
        return Response({'error': 'Kamida 1 ta dars tanlanishi kerak.'}, status=status.HTTP_400_BAD_REQUEST)
    
    question_count = int(data.get('questionCount', 10))
    difficulty = data.get('difficulty', 'mixed')
    include_code = data.get('includeCodeQuestions', True)
    language = data.get('language', 'uz')

    try:
        questions = generate_ai_quiz(
            lesson_numbers=lesson_ids,
            question_count=question_count,
            difficulty=difficulty,
            include_code=include_code,
            language=language
        )
        return Response({
            'success': True,
            'lessonIds': lesson_ids,
            'questions': questions
        })
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET', 'POST'])
def quizzes_list(request):
    if request.method == 'GET':
        quizzes = Quiz.objects.all()
        return Response([q.to_dict() for q in quizzes])

    elif request.method == 'POST':
        data = request.data
        title = data.get('title') or f"Quiz ({time.strftime('%Y-%m-%d %H:%M')})"
        questions = data.get('questions', [])
        lesson_ids = data.get('lessonIds', [])

        quiz_id = data.get('id') or f"quiz-{int(time.time()*1000)}"
        quiz = Quiz.objects.create(
            quiz_id=quiz_id,
            title=title,
            lesson_ids=lesson_ids,
            questions=questions
        )
        return Response(quiz.to_dict(), status=status.HTTP_201_CREATED)

@api_view(['GET', 'DELETE'])
def quiz_detail(request, quiz_id):
    try:
        quiz = Quiz.objects.get(quiz_id=quiz_id)
    except Quiz.DoesNotExist:
        return Response({'error': 'Quiz topilmadi.'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        return Response(quiz.to_dict())
    elif request.method == 'DELETE':
        quiz.delete()
        return Response({'message': 'Quiz o\'chirildi.'})

@api_view(['POST'])
def create_quiz_session(request):
    data = request.data
    quiz_id = data.get('quizId')
    if not quiz_id:
        return Response({'error': 'quizId talab etiladi.'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        quiz = Quiz.objects.get(quiz_id=quiz_id)
    except Quiz.DoesNotExist:
        return Response({'error': 'Quiz topilmadi.'}, status=status.HTTP_404_NOT_FOUND)

    code = f"{random.randint(100000, 999999)}"
    session = QuizSession.objects.create(
        code=code,
        quiz=quiz,
        status='lobby'
    )
    return Response(session.to_dict(), status=status.HTTP_201_CREATED)

@api_view(['GET'])
def get_quiz_session_info(request, code):
    try:
        session = QuizSession.objects.get(code=code)
        return Response(session.to_dict())
    except QuizSession.DoesNotExist:
        return Response({'error': 'Sessiya topilmadi yoki PIN kod noto\'g\'ri.'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET', 'POST'])
def quiz_templates_list(request):
    if request.method == 'GET':
        templates = QuizTemplate.objects.all()
        if not templates.exists():
            # Seed default templates if database is empty
            defaults = [
                {
                    "template_id": "tpl-1",
                    "title": "🐍 Python Sintaksisi va Boshlang'ich Tushunchalar",
                    "description": "1-modul: O'zgaruvchilar, ma'lumot turlari, if/else va sikllar bo'yicha 10 ta oson va o'rta savollar.",
                    "category": "Python Asoslari",
                    "question_count": 10,
                    "difficulty": "easy",
                    "lesson_ids": [1, 2, 3, 4, 5, 6]
                },
                {
                    "template_id": "tpl-2",
                    "title": "⚡ Django Apps, Views, Models & ORM",
                    "description": "4-modul: Django backend strukturasi, ORM so'rovlari va admin panel bo'yicha 15 ta texnik savol.",
                    "category": "Django Backend",
                    "question_count": 15,
                    "difficulty": "medium",
                    "lesson_ids": [37, 38, 39, 40, 41, 42, 43, 44]
                },
                {
                    "template_id": "tpl-3",
                    "title": "🚀 REST API, DRF Serializers & Authentication",
                    "description": "5-modul: DRF, JWT tokenlar, Swagger va ruxsatnomalar bo'yicha 20 ta amaliy savol.",
                    "category": "DRF & Security",
                    "question_count": 20,
                    "difficulty": "hard",
                    "lesson_ids": [49, 50, 51, 52, 53, 54, 55, 56]
                }
            ]
            for item in defaults:
                QuizTemplate.objects.create(**item)
            templates = QuizTemplate.objects.all()

        return Response([t.to_dict() for t in templates])

    elif request.method == 'POST':
        data = request.data
        title = data.get('title')
        if not title:
            return Response({'error': 'Shablon nomi kiritilishi shart.'}, status=status.HTTP_400_BAD_REQUEST)

        template_id = data.get('id') or f"custom-tpl-{int(time.time()*1000)}"
        template = QuizTemplate.objects.create(
            template_id=template_id,
            title=title,
            description=data.get('description', ''),
            category=data.get('category', 'Python Backend'),
            question_count=data.get('questionCount', 10),
            difficulty=data.get('difficulty', 'medium'),
            lesson_ids=data.get('lessonIds', []),
            custom_questions=data.get('customQuestions', [])
        )
        return Response(template.to_dict(), status=status.HTTP_201_CREATED)

@api_view(['GET', 'DELETE'])
def quiz_template_detail(request, template_id):
    try:
        template = QuizTemplate.objects.get(template_id=template_id)
    except QuizTemplate.DoesNotExist:
        return Response({'error': 'Shablon topilmadi.'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        return Response(template.to_dict())
    elif request.method == 'DELETE':
        template.delete()
        return Response({'message': 'Shablon o\'chirildi.'})

# ============================================================================
# NOTION SYNC & OTHER ENDPOINTS
# ============================================================================

@api_view(['GET'])
def notion_status(request):
    return Response(get_settings())

@api_view(['POST'])
def scrape_notion(request):
    notion_url = request.data.get('notionUrl')
    if not notion_url:
        return Response({'error': 'Notion URL manzili talab etiladi.'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        scraped = scrape_single_notion_page(notion_url)
        if not scraped:
            return Response({'error': 'Notion sahifasini o\'qib bo\'lmadi.'}, status=status.HTTP_400_BAD_REQUEST)

        num = scraped.get('lessonNumber', 1)
        lesson, _ = Lesson.objects.update_or_create(
            lesson_number=num,
            defaults={
                'lesson_id': scraped['id'],
                'title': scraped['title'],
                'date': scraped.get('date', ''),
                'time': scraped.get('time', '14:00 - 16:00'),
                'status': scraped.get('status', 'planned'),
                'description': scraped.get('description', ''),
                'content': scraped.get('content', ''),
                'homework': scraped.get('homework', ''),
                'materials': scraped.get('materials', []),
                'tasks': scraped.get('tasks', [])
            }
        )

        all_count = Lesson.objects.count()
        save_settings({
            "notionUrl": notion_url,
            "sourceType": "page",
            "sourceName": f"Django Scraped ({all_count} dars)",
            "lastSyncTime": time.strftime("%Y-%m-%d %H:%M:%S"),
            "lessonsSynced": all_count,
            "documentsSynced": 0
        })

        return Response({
            'success': True,
            'lessonsCount': all_count,
            'scrapedLesson': lesson.to_dict()
        })
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['DELETE'])
def notion_disconnect(request):
    save_settings({"notionUrl": "", "sourceType": "none", "sourceName": ""})
    return Response({'success': True, 'message': 'Notion ulanishi tozalandi.'})
