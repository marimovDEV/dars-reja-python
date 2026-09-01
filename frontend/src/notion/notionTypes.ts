import { Lesson, LessonMaterial } from '../types';

export interface NotionConnectionInfo {
  success: boolean;
  sourceType: 'database' | 'page';
  sourceName: string;
}

export interface NotionSyncSummary {
  lessonsFound: number;
  documentsFound: number;
  warnings: string[];
}

export interface NotionPreviewResponse {
  success: boolean;
  summary: NotionSyncSummary;
  lessons: Lesson[];
  documents: LessonMaterial[];
  warnings: string[];
}

export interface NotionSettings {
  notionUrl: string;
  sourceType: 'database' | 'page' | 'none';
  sourceName: string;
  lastSyncTime?: string;
  lessonsSynced?: number;
  documentsSynced?: number;
}
