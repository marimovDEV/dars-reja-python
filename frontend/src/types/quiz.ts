export interface QuizQuestion {
  question: string;
  type: 'single_choice';
  options: [string, string, string, string];
  correctOptionIndex: number;
  explanation: string;
  lessonId: number;
  durationSeconds: number;
}

export interface Quiz {
  id: string;
  title: string;
  lessonIds: number[];
  questions: QuizQuestion[];
  questionsCount: number;
  createdAt: string;
}

export interface QuizGenConfig {
  lessonIds: number[];
  questionCount: number;
  difficulty: 'easy' | 'medium' | 'hard' | 'mixed';
  includeCodeQuestions: boolean;
  language: string;
}

export interface PlayerScore {
  rank?: number;
  socketId?: string;
  nickname: string;
  score: number;
  lastPoints?: number;
  streak?: number;
}
