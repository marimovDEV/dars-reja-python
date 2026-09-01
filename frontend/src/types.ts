export type LessonStatus = 'completed' | 'pending' | 'planned';

export interface LessonMaterial {
  id: string;
  name: string;
  type: 'pdf' | 'docx' | 'pptx' | 'xlsx' | 'link' | 'image' | 'zip';
  size?: string;
  url?: string;
  notionLinked?: boolean;
}

export interface LessonTask {
  id: string;
  title: string;
  type?: 'test' | 'oral' | 'written' | 'practical' | 'independent';
  question: string;
  answer?: string;
  hints?: string[];
}

export interface CodeExample {
  id: string;
  title: string;
  code: string;
  language: string;
  explanation: string; // Qatorma-qator kod tushuntirishi
}

export interface QuizQuestion {
  id: string;
  question: string;
  options: string[];
  correctIndex: number;
  explanation: string;
}

export interface LessonTeacherScenario {
  review15m?: string;   // 15 min - Avvalgi uyga vazifani tekshirish
  theory25m?: string;   // 25 min - Nazariya
  liveCode40m?: string; // 40 min - Ustoz bilan birga kod yozish
  practice30m?: string; // 30 min - Mustaqil amaliyot
  summary10m?: string;  // 10 min - Xulosa va uyga vazifa
  teacherTips?: string[];
}

export interface StudentResult {
  id: string;
  studentName: string;
  score: number; // 0..100
  passed: boolean;
  notes?: string;
}

export interface Lesson {
  id: string;
  lessonNumber: number;
  title: string;
  date: string;
  time: string;
  status: LessonStatus;
  goal?: string;                   // 1. Dars maqsadi
  description?: string;           // Dars tavsifi
  content: string;                // 2. To'liq nazariya (Markdown)
  scenario?: LessonTeacherScenario;// 3. O'qituvchi dars ssenariysi
  codeExamples?: CodeExample[];    // 4. Kod misollari va qatorma-qator izohi
  tasks?: LessonTask[];            // 5. Sinfdagi amaliy mashqlar
  independentTasks?: LessonTask[]; // 6. Mustaqil topshiriqlar
  homework: string;               // 7. Uyga vazifa
  quizQuestions?: QuizQuestion[];  // 8. Test savollari va javoblari
  materials?: LessonMaterial[];    // 9. PDF/video/link/fayllar
  studentResults?: StudentResult[];// 10. O'quvchi natijalari va dars bajarilish statistikasi
}
