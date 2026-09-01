import Papa from 'papaparse';
import { Lesson, LessonStatus } from '../types';

// Helper to parse dates from Notion (handles ranges like "2026-09-01 -> 2026-09-02", "Sep 1, 2026" and empty values)
export const parseNotionDate = (dateStr: string): string => {
  if (!dateStr || dateStr.trim() === '') return '';
  
  // Extract start date if it is a range (e.g. "2026-09-01 -> 2026-09-02" or "2026-09-01 to 2026-09-02")
  let cleanDate = dateStr.split('->')[0].split('to')[0].trim();
  
  // Check if it's already YYYY-MM-DD
  if (/^\d{4}-\d{2}-\d{2}$/.test(cleanDate)) {
    return cleanDate;
  }
  
  // Try JS parsing
  const timestamp = Date.parse(cleanDate);
  if (!isNaN(timestamp)) {
    const d = new Date(timestamp);
    const y = d.getFullYear();
    const m = String(d.getMonth() + 1).padStart(2, '0');
    const day = String(d.getDate()).padStart(2, '0');
    return `${y}-${m}-${day}`;
  }
  
  return cleanDate;
};

// Maps dynamic headers to our Lesson properties
const mapHeaders = (headers: string[]) => {
  const mapping: { [key: string]: number } = {};
  
  headers.forEach((header, index) => {
    const lower = header.toLowerCase().trim();
    
    if (lower.includes('raqam') || lower.includes('number') || lower === '#' || lower === 'id' || lower === 'dars') {
      mapping['lessonNumber'] = index;
    } else if (lower.includes('sarlavha') || lower.includes('title') || lower.includes('nomi') || lower === 'name' || lower.includes('mavzu')) {
      mapping['title'] = index;
    } else if (lower.includes('sana') || lower.includes('date')) {
      mapping['date'] = index;
    } else if (lower.includes('holat') || lower.includes('status')) {
      mapping['status'] = index;
    } else if (lower.includes('tavsif') || lower.includes('description') || lower.includes('konspekt') || lower.includes('content')) {
      mapping['description'] = index;
    } else if (lower.includes('vazifa') || lower.includes('homework') || lower.includes('uyga')) {
      mapping['homework'] = index;
    } else if (lower.includes('vaqt') || lower.includes('time')) {
      mapping['time'] = index;
    }
  });
  
  return mapping;
};

// Parse CSV content using Papa Parse
export const parseCSVLessons = (csvText: string): Lesson[] => {
  const parsed = Papa.parse<string[]>(csvText, {
    skipEmptyLines: true,
  });
  
  if (parsed.errors.length > 0) {
    console.warn('Papa Parse errors:', parsed.errors);
  }
  
  const rows = parsed.data;
  if (rows.length < 2) return []; // Needs header + at least 1 data row
  
  const headers = rows[0];
  const mapping = mapHeaders(headers);
  const dataRows = rows.slice(1);
  
  return dataRows.map((row, rIdx) => {
    const getVal = (field: string, fallback = '') => {
      const colIdx = mapping[field];
      return colIdx !== undefined && row[colIdx] !== undefined ? row[colIdx].trim() : fallback;
    };
    
    // Determine lesson number
    let lessonNumber = parseInt(getVal('lessonNumber'), 10);
    if (isNaN(lessonNumber)) {
      lessonNumber = rIdx + 1; // Fallback to index
    }
    
    const title = getVal('title') || `${lessonNumber}-dars`;
    const rawDate = getVal('date');
    const date = parseNotionDate(rawDate);
    const time = getVal('time') || '14:00 - 16:00';
    
    // Map status
    let status: LessonStatus = 'planned';
    const rawStatus = getVal('status').toLowerCase();
    if (rawStatus.includes('bajar') || rawStatus.includes('o\'tildi') || rawStatus.includes('completed') || rawStatus.includes('done')) {
      status = 'completed';
    } else if (rawStatus.includes('kutil') || rawStatus.includes('progress') || rawStatus.includes('doing') || rawStatus.includes('pending')) {
      status = 'pending';
    }
    
    const description = getVal('description');
    const homework = getVal('homework');
    
    // Create lesson
    return {
      id: `les-imported-${lessonNumber}-${Date.now()}-${rIdx}`,
      lessonNumber,
      title,
      date,
      time,
      status,
      description,
      content: `### Dars Konspekti\n\n${description || 'Ushbu dars uchun konspekt kiritilmagan.'}`,
      homework: homework || 'Berilmagan.',
      materials: [],
      tasks: []
    };
  });
};

// Parse Markdown content
export const parseMarkdownLessons = (mdText: string): Lesson[] => {
  // Normalize newlines
  const text = mdText.replace(/\r\n/g, '\n');
  
  // Find headings starting with ###
  const sections = text.split(/\n###\s+/);
  if (sections.length < 2) return [];
  
  const lessons: Lesson[] = [];
  
  sections.slice(1).forEach((section, index) => {
    const lines = section.split('\n');
    const heading = lines[0].trim();
    const remainingText = lines.slice(1).join('\n');
    
    // Match lesson number and title: e.g. "1-dars — Muhit" or "Dars 1: Muhit"
    let lessonNumber = index + 1;
    let title = heading;
    
    const headingMatch = heading.match(/^(\d+)[-–\s]*dars\s*[-–:\s]*(.*)/i) || heading.match(/^dars\s*(\d+)\s*[-–:\s]*(.*)/i);
    if (headingMatch) {
      lessonNumber = parseInt(headingMatch[1], 10);
      title = headingMatch[2].trim() || `${lessonNumber}-dars`;
    }
    
    // Parse fields
    const getField = (regex: RegExp): string => {
      const match = remainingText.match(regex);
      return match ? match[1].trim() : '';
    };
    
    const mavzu = getField(/\*\*Mavzu:\*\*(.*?)(?=\n\*\*|$)/i) || getField(/\*\*Qamrov:\*\*(.*?)(?=\n\*\*|$)/i);
    const amaliyot = getField(/\*\*Amaliyot:\*\*(.*?)(?=\n\*\*|$)/i) || getField(/\*\*Topshiriqlar:\*\*(.*?)(?=\n\*\*|$)/i);
    const uygaVazifa = getField(/\*\*Uyga vazifa:\*\*(.*?)(?=\n\*\*|$)/i) || getField(/\*\*Baholash:\*\*(.*?)(?=\n\*\*|$)/i);
    
    const description = mavzu || title;
    
    // Build content markdown
    let content = `### Dars Konspekti\n\n**Mavzu:** ${description}`;
    if (amaliyot) {
      content += `\n\n**Amaliyot:** ${amaliyot}`;
    }
    
    lessons.push({
      id: `les-imported-${lessonNumber}-${Date.now()}-${index}`,
      lessonNumber,
      title,
      date: '', // Will be updated on import or generated dynamically
      time: '14:00 - 16:00',
      status: 'planned',
      description,
      content,
      homework: uygaVazifa || 'Berilmagan.',
      materials: [],
      tasks: amaliyot ? [
        {
          id: `t-imported-${lessonNumber}-1`,
          title: "Amaliy topshiriq",
          type: "practical",
          question: amaliyot,
          answer: "Bajarildi."
        }
      ] : []
    });
  });
  
  return lessons;
};
