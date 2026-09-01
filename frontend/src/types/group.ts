export interface Group {
  id: string;
  name: string;
  startDate: string;
  scheduleDays: string;
  scheduleTime: string;
  studentCount?: number;
  telegramLink?: string;
  notes?: string;
  completedCount: number;
  currentLessonNumber: number;
  currentLessonTitle: string;
  totalLessons: number;
  createdAt: string;
}

export interface GroupFormData {
  name: string;
  startDate: string;
  scheduleDays: string;
  scheduleTime: string;
  studentCount?: number;
  telegramLink?: string;
  notes?: string;
}
