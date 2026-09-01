import { Lesson, LessonStatus, LessonTask, LessonMaterial } from '../types';

// Parses Notion date strings (e.g. ranges or single dates) to YYYY-MM-DD
export const cleanNotionDate = (dateVal: any): string => {
  if (!dateVal || !dateVal.start) return '';
  const start = dateVal.start;
  // If it's a timestamp, take just the date portion
  return start.split('T')[0];
};

// Find cell property by key synonyms
const getProp = (properties: any, synonyms: string[]): any => {
  for (const key of Object.keys(properties)) {
    const lowerKey = key.toLowerCase().trim();
    if (synonyms.some(syn => lowerKey.includes(syn))) {
      return properties[key];
    }
  }
  return null;
};

// Extracts plain text from different property types
export const extractPropertyValue = (prop: any): any => {
  if (!prop) return null;
  
  switch (prop.type) {
    case 'number':
      return prop.number;
    case 'title':
      return prop.title.map((t: any) => t.plain_text).join('');
    case 'rich_text':
      return prop.rich_text.map((t: any) => t.plain_text).join('');
    case 'date':
      return prop.date ? cleanNotionDate(prop.date) : '';
    case 'select':
      return prop.select ? prop.select.name : '';
    case 'status':
      return prop.status ? prop.status.name : '';
    case 'checkbox':
      return prop.checkbox;
    case 'url':
      return prop.url || '';
    case 'files':
      return prop.files.map((f: any) => ({
        name: f.name,
        url: f.type === 'file' ? f.file.url : (f.external ? f.external.url : '')
      }));
    default:
      return null;
  }
};

// Main database row parser
export const parseDatabaseRow = (page: any, index: number): { lesson: Lesson; documents: LessonMaterial[] } => {
  const props = page.properties;
  
  // Extract fields using synonyms
  const rawNum = extractPropertyValue(getProp(props, ['raqam', 'number', 'dars #', '#', 'id', 'dars raqami', '№']));
  let lessonNumber = typeof rawNum === 'number' ? rawNum : parseInt(String(rawNum), 10);
  if (isNaN(lessonNumber)) {
    lessonNumber = index + 1;
  }
  
  const title = extractPropertyValue(getProp(props, ['mavzu', 'topic', 'sarlavha', 'name', 'title'])) || `${lessonNumber}-dars`;
  const date = extractPropertyValue(getProp(props, ['sana', 'date'])) || '';
  const theory = extractPropertyValue(getProp(props, ['nazariya', 'theory', 'description', 'tavsif', 'notes', 'izoh'])) || '';
  const practice = extractPropertyValue(getProp(props, ['amaliyot', 'practice', 'topshiriq'])) || '';
  const homework = extractPropertyValue(getProp(props, ['uyga vazifa', 'homework', 'vazifa'])) || 'Berilmagan.';
  const time = extractPropertyValue(getProp(props, ['vaqt', 'time'])) || '14:00 - 16:00';
  const isExam = extractPropertyValue(getProp(props, ['imtihon', 'exam', 'isexam'])) === true || 
                 [12, 24, 36, 48, 60, 72].includes(lessonNumber);
  
  // Status mapping
  const rawStatus = String(extractPropertyValue(getProp(props, ['holat', 'status'])) || '').toLowerCase();
  let status: LessonStatus = 'planned';
  if (rawStatus.includes('comple') || rawStatus.includes('o\'tildi') || rawStatus.includes('bajar')) {
    status = 'completed';
  } else if (rawStatus.includes('pend') || rawStatus.includes('navbat') || rawStatus.includes('kutil')) {
    status = 'pending';
  }

  // Parse attachments
  const filesList = extractPropertyValue(getProp(props, ['hujjat', 'attachments', 'files'])) || [];
  const materials: LessonMaterial[] = filesList.map((file: any, fIdx: number) => ({
    id: `mat-notion-${lessonNumber}-${fIdx}`,
    name: file.name,
    type: file.name.split('.').pop()?.toLowerCase() || 'link',
    url: file.url
  }));

  // Tasks
  const tasks: LessonTask[] = [];
  if (practice) {
    tasks.push({
      id: `task-notion-${lessonNumber}-1`,
      title: "Amaliy topshiriq",
      type: "practical",
      question: practice,
      answer: "Bajarildi."
    });
  }

  const content = isExam 
    ? `### Imtihon Tafsilotlari\n\n**Mavzu:** ${title}\n\n**Nazorat savollari:** ${theory || 'Oraliq imtihon.'}`
    : `### Dars Konspekti\n\n**Mavzu:** ${theory || title}\n\n**Amaliyot:** ${practice || 'Sinfda amaliy topshiriq.'}`;

  const lesson: Lesson = {
    id: page.id || `les-notion-${lessonNumber}`,
    lessonNumber,
    title,
    date,
    time,
    status,
    description: theory || title,
    content,
    homework,
    materials: materials.slice(0, 3), // limit inside lesson representation
    tasks
  };

  return { lesson, documents: materials };
};

// Notion Page Blocks parser (for unstructured markdown pages)
export const parsePageBlocks = (blocks: any[]): { lessons: Lesson[]; documents: LessonMaterial[] } => {
  const lessons: Lesson[] = [];
  const documents: LessonMaterial[] = [];
  
  let currentLesson: Partial<Lesson> | null = null;
  let currentBlockType: 'theory' | 'practice' | 'homework' | null = null;
  let theoryAcc = '';
  let practiceAcc = '';
  let homeworkAcc = '';
  let lessonCount = 0;

  const saveCurrent = () => {
    if (currentLesson) {
      const num = currentLesson.lessonNumber || (lessonCount + 1);
      const isExam = [12, 24, 36, 48, 60, 72].includes(num);
      const title = currentLesson.title || `${num}-dars`;
      const theory = theoryAcc.trim();
      const practice = practiceAcc.trim();
      
      const content = isExam 
        ? `### Imtihon Tafsilotlari\n\n**Mavzu:** ${title}\n\n**Nazorat savollari:** ${theory || 'Oraliq imtihon.'}`
        : `### Dars Konspekti\n\n**Mavzu:** ${theory || title}\n\n**Amaliyot:** ${practice || 'Sinfda amaliy topshiriq.'}`;

      const tasks: LessonTask[] = [];
      if (practice) {
        tasks.push({
          id: `task-block-${num}-1`,
          title: "Amaliy topshiriq",
          type: "practical",
          question: practice,
          answer: "Bajarildi."
        });
      }

      lessons.push({
        id: currentLesson.id || `les-notion-block-${num}`,
        lessonNumber: num,
        title,
        date: '',
        time: '14:00 - 16:00',
        status: 'planned',
        description: theory || title,
        content,
        homework: homeworkAcc.trim() || 'Berilmagan.',
        materials: [],
        tasks
      });
      lessonCount++;
    }
  };

  blocks.forEach((block: any) => {
    const type = block.type;
    let text = '';
    
    // Extract text from text blocks
    if (block[type]?.rich_text) {
      text = block[type].rich_text.map((t: any) => t.plain_text).join('');
    }

    // Capture attachments from file or link blocks
    if (type === 'file' || type === 'pdf') {
      const name = block[type].name || 'Notion_File';
      const url = block[type].type === 'file' ? block[type].file.url : block[type].external.url;
      documents.push({
        id: block.id,
        name,
        type: name.split('.').pop()?.toLowerCase() || 'pdf',
        url
      });
    }

    // Check for dars headers (e.g. "### 1-dars", "### Dars 1: ...", "1-dars — ...")
    const isHeader = type === 'heading_1' || type === 'heading_2' || type === 'heading_3';
    const darsMatch = isHeader && (
      text.match(/^(\d+)[-–\s]*dars\s*[-–:\s]*(.*)/i) || 
      text.match(/^dars\s*(\d+)\s*[-–:\s]*(.*)/i)
    );

    if (darsMatch) {
      // Save previous lesson
      saveCurrent();
      
      // Initialize new lesson
      const num = parseInt(darsMatch[1], 10);
      const title = darsMatch[2].trim() || `${num}-dars`;
      
      currentLesson = {
        id: block.id,
        lessonNumber: num,
        title
      };
      
      // Reset accumulators
      theoryAcc = '';
      practiceAcc = '';
      homeworkAcc = '';
      currentBlockType = 'theory'; // default to theory
    } else if (currentLesson) {
      const lowerText = text.toLowerCase().trim();
      
      // Check block triggers for categories
      if (lowerText.startsWith('mavzu:') || lowerText.startsWith('nazariya:')) {
        currentBlockType = 'theory';
        text = text.substring(text.indexOf(':') + 1);
      } else if (lowerText.startsWith('amaliyot:') || lowerText.startsWith('topshiriq:')) {
        currentBlockType = 'practice';
        text = text.substring(text.indexOf(':') + 1);
      } else if (lowerText.startsWith('uyga vazifa:') || lowerText.startsWith('vazifa:') || lowerText.startsWith('homework:')) {
        currentBlockType = 'homework';
        text = text.substring(text.indexOf(':') + 1);
      }

      // Append to accumulator
      if (text.trim() !== '') {
        if (currentBlockType === 'theory') theoryAcc += ' ' + text;
        else if (currentBlockType === 'practice') practiceAcc += ' ' + text;
        else if (currentBlockType === 'homework') homeworkAcc += ' ' + text;
      }
    }
  });

  // Save the final lesson
  saveCurrent();

  return { lessons, documents };
};
