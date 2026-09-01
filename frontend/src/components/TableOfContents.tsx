import React, { useEffect, useState } from 'react';
import { List, ChevronRight } from 'lucide-react';

interface HeadingItem {
  id: string;
  text: string;
  level: number; // 2 or 3
}

interface TableOfContentsProps {
  content: string;
  onSelectHeading?: () => void;
}

export const TableOfContents: React.FC<TableOfContentsProps> = ({ content, onSelectHeading }) => {
  const [headings, setHeadings] = useState<HeadingItem[]>([]);
  const [activeId, setActiveId] = useState<string>('');

  useEffect(() => {
    // Parse markdown headings ## and ###
    const lines = content.split('\n');
    const items: HeadingItem[] = [];
    let count = 0;

    lines.forEach((line) => {
      const match = line.match(/^(#{2,3})\s+(.+)$/);
      if (match) {
        const level = match[1].length; // 2 or 3
        const rawText = match[2].trim().replace(/[*_`]/g, '');
        const slug = rawText.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-+|-+$/g, '');
        const id = `heading-${count++}-${slug}`;
        items.push({ id, text: rawText, level });
      }
    });

    setHeadings(items);
  }, [content]);

  useEffect(() => {
    // Scroll active heading observer
    const handleScroll = () => {
      const headingElements = document.querySelectorAll('h2[id], h3[id]');
      let currentId = '';

      headingElements.forEach((el) => {
        const rect = el.getBoundingClientRect();
        if (rect.top <= 160) {
          currentId = el.id;
        }
      });

      if (currentId) {
        setActiveId(currentId);
      }
    };

    const container = document.getElementById('lesson-documentation-view');
    if (container) {
      container.addEventListener('scroll', handleScroll);
    }
    return () => {
      if (container) {
        container.removeEventListener('scroll', handleScroll);
      }
    };
  }, [headings]);

  if (headings.length === 0) return null;

  const scrollToHeading = (id: string) => {
    const el = document.getElementById(id);
    if (el) {
      el.scrollIntoView({ behavior: 'smooth', block: 'start' });
      setActiveId(id);
      if (onSelectHeading) onSelectHeading();
    }
  };

  return (
    <aside className="w-full lg:w-64 shrink-0 sticky top-24 max-h-[calc(100vh-120px)] overflow-y-auto pr-2 scrollbar-none font-sans">
      <div className="p-4 rounded-2xl bg-white dark:bg-slate-900/80 backdrop-blur-md border border-slate-200 dark:border-slate-800/80 shadow-xs space-y-3">
        <div className="flex items-center gap-2 text-xs font-extrabold uppercase tracking-widest text-slate-400 dark:text-slate-500 border-b border-slate-100 dark:border-slate-800 pb-2">
          <List className="w-4 h-4 text-blue-500" />
          <span>Mundarija</span>
        </div>

        <nav className="space-y-1 text-xs">
          {headings.map((item) => {
            const isActive = activeId === item.id;
            return (
              <button
                key={item.id}
                onClick={() => scrollToHeading(item.id)}
                className={`w-full text-left py-1.5 px-2 rounded-lg transition-all flex items-center justify-between group cursor-pointer ${
                  item.level === 3 ? 'pl-5 text-[11px]' : 'font-semibold'
                } ${
                  isActive
                    ? 'bg-blue-50 dark:bg-blue-950/60 text-blue-600 dark:text-blue-400 font-bold'
                    : 'text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-white hover:bg-slate-100 dark:hover:bg-slate-800/50'
                }`}
              >
                <span className="truncate">{item.text}</span>
                {isActive && <ChevronRight className="w-3 h-3 text-blue-500 shrink-0" />}
              </button>
            );
          })}
        </nav>
      </div>
    </aside>
  );
};
