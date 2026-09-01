from django.db import models

class Lesson(models.Model):
    lesson_id = models.CharField(max_length=100, unique=True)
    lesson_number = models.IntegerField(default=1)
    title = models.CharField(max_length=255)
    date = models.CharField(max_length=100, blank=True, default='')
    time = models.CharField(max_length=100, blank=True, default='14:00 - 16:00')
    status = models.CharField(max_length=50, default='planned')
    goal = models.TextField(blank=True, default='')
    description = models.TextField(blank=True, default='')
    content = models.TextField(blank=True, default='')
    scenario = models.JSONField(default=dict, blank=True)
    code_examples = models.JSONField(default=list, blank=True)
    tasks = models.JSONField(default=list, blank=True)
    independent_tasks = models.JSONField(default=list, blank=True)
    homework = models.TextField(blank=True, default='')
    quiz_questions = models.JSONField(default=list, blank=True)
    materials = models.JSONField(default=list, blank=True)
    student_results = models.JSONField(default=list, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['lesson_number']

    def __str__(self):
        return f"{self.lesson_number}-dars: {self.title}"

    def to_dict(self):
        return {
            "id": self.lesson_id,
            "lessonNumber": self.lesson_number,
            "title": self.title,
            "date": self.date,
            "time": self.time,
            "status": self.status,
            "goal": self.goal or f"{self.title} mavzusini mukammal o'zlashtirish",
            "description": self.description,
            "content": self.content,
            "scenario": self.scenario or {},
            "codeExamples": self.code_examples or [],
            "tasks": self.tasks or [],
            "independentTasks": self.independent_tasks or [],
            "homework": self.homework,
            "quizQuestions": self.quiz_questions or [],
            "materials": self.materials or [],
            "studentResults": self.student_results or []
        }


class Group(models.Model):
    group_id = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=255)
    start_date = models.DateField()
    schedule_days = models.CharField(max_length=255, default="Dush / Chor / Juma")
    schedule_time = models.CharField(max_length=100, default="14:00 - 16:00")
    student_count = models.IntegerField(null=True, blank=True, default=0)
    telegram_link = models.URLField(max_length=500, blank=True, default="")
    notes = models.TextField(blank=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name

    def to_dict(self):
        # Calculate current lesson number and stats based on lesson progress
        progress_qs = self.lesson_progress.all().select_related('lesson')
        completed_count = progress_qs.filter(status='completed').count()
        current_progress = progress_qs.filter(status='current').first()
        
        if current_progress:
            current_lesson_num = current_progress.lesson.lesson_number
            current_title = current_progress.lesson.title
        elif completed_count > 0:
            current_lesson_num = min(completed_count + 1, 72)
            current_progress_obj = progress_qs.filter(lesson__lesson_number=current_lesson_num).first()
            current_title = current_progress_obj.lesson.title if current_progress_obj else f"{current_lesson_num}-dars"
        else:
            current_lesson_num = 1
            first_obj = progress_qs.filter(lesson__lesson_number=1).first()
            current_title = first_obj.lesson.title if first_obj else "1-dars"

        return {
            "id": self.group_id,
            "name": self.name,
            "startDate": self.start_date.strftime("%Y-%m-%d") if self.start_date else "",
            "scheduleDays": self.schedule_days,
            "scheduleTime": self.schedule_time,
            "studentCount": self.student_count or 0,
            "telegramLink": self.telegram_link or "",
            "notes": self.notes or "",
            "completedCount": completed_count,
            "currentLessonNumber": current_lesson_num,
            "currentLessonTitle": current_title,
            "totalLessons": progress_qs.count() or 72,
            "createdAt": self.created_at.strftime("%Y-%m-%d %H:%M:%S")
        }


class GroupLessonProgress(models.Model):
    STATUS_CHOICES = [
        ("planned", "Rejalashtirilgan"),
        ("current", "Jarayonda"),
        ("completed", "O‘tildi"),
        ("cancelled", "Qoldirildi"),
    ]

    group = models.ForeignKey(
        Group,
        on_delete=models.CASCADE,
        related_name="lesson_progress"
    )
    lesson = models.ForeignKey(
        Lesson,
        on_delete=models.CASCADE
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="planned"
    )
    scheduled_at = models.DateTimeField(null=True, blank=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    notes = models.TextField(blank=True, default="")

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["group", "lesson"],
                name="unique_group_lesson_progress"
            )
        ]
        ordering = ['lesson__lesson_number']

    def __str__(self):
        return f"{self.group.name} - {self.lesson.lesson_number}-dars ({self.status})"

    def to_dict(self):
        lesson_data = self.lesson.to_dict()
        lesson_data["status"] = self.status
        lesson_data["scheduledAt"] = self.scheduled_at.strftime("%Y-%m-%d %H:%M") if self.scheduled_at else lesson_data.get("date", "")
        lesson_data["completedAt"] = self.completed_at.strftime("%Y-%m-%d %H:%M") if self.completed_at else ""
        lesson_data["teacherNotes"] = self.notes or ""
        return lesson_data
