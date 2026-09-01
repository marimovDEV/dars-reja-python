import { Client } from '@notionhq/client';
import dotenv from 'dotenv';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

// Load .env from backend workspace root
dotenv.config({ path: path.join(__dirname, '..', '..', '.env') });

const token = process.env.NOTION_TOKEN || '';

export const getNotionClient = (): Client | null => {
  if (!token || token.trim() === '' || token.includes('placeholder')) {
    return null;
  }
  return new Client({ auth: token });
};

export const isNotionTokenConfigured = (): boolean => {
  return !!token && token.trim() !== '' && !token.includes('placeholder');
};
