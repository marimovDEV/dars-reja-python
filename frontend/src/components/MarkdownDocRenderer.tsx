import React from 'react';
import Markdown from 'react-markdown';
import remarkGfm from 'remark-gfm';
import { CodeBlock } from './CodeBlock';
import { DocCallout, CalloutType } from './DocCallout';

interface MarkdownDocRendererProps {
  content: string;
}

export const MarkdownDocRenderer: React.FC<MarkdownDocRendererProps> = ({ content }) => {
  let headingIndex = 0;

  return (
    <div className="prose dark:prose-invert max-w-none text-slate-700 dark:text-slate-300 font-['Inter',sans-serif] text-[16px] leading-[1.75]">
      <Markdown
        remarkPlugins={[remarkGfm]}
        components={{
          h1: ({ children }) => (
            <h1 className="text-3xl font-extrabold text-slate-900 dark:text-white mt-8 mb-5 tracking-tight flex items-center gap-2">
              {children}
            </h1>
          ),
          h2: ({ children }) => {
            const rawText = String(children).replace(/[*_`]/g, '');
            const id = `heading-${headingIndex++}-${rawText.toLowerCase().replace(/[^a-z0-9]+/g, '-')}`;
            return (
              <h2
                id={id}
                className="text-2xl font-bold text-slate-900 dark:text-slate-100 mt-12 mb-4 pt-6 border-t border-slate-200 dark:border-slate-800 scroll-mt-28"
              >
                {children}
              </h2>
            );
          },
          h3: ({ children }) => {
            const rawText = String(children).replace(/[*_`]/g, '');
            const id = `heading-${headingIndex++}-${rawText.toLowerCase().replace(/[^a-z0-9]+/g, '-')}`;
            return (
              <h3
                id={id}
                className="text-lg font-bold text-slate-900 dark:text-slate-200 mt-7 mb-3 scroll-mt-28"
              >
                {children}
              </h3>
            );
          },
          p: ({ children }) => (
            <p className="my-4 text-slate-700 dark:text-slate-300 leading-relaxed text-[16px]">
              {children}
            </p>
          ),
          code: ({ inline, className, children, ...props }: any) => {
            const match = /language-(\w+)/.exec(className || '');
            const codeString = String(children).replace(/\n$/, '');

            if (!inline && (match || codeString.includes('\n'))) {
              const lang = match ? match[1] : 'python';
              const isTerminal = lang === 'text' || lang === 'output' || codeString.startsWith('$');
              return (
                <CodeBlock
                  code={codeString}
                  language={lang}
                  isTerminal={isTerminal}
                />
              );
            }

            return (
              <code
                className="font-['JetBrains_Mono',monospace] text-[13.5px] font-semibold bg-slate-100 dark:bg-slate-800 text-amber-700 dark:text-amber-300 px-1.5 py-0.5 rounded border border-slate-200 dark:border-slate-700"
                {...props}
              >
                {children}
              </code>
            );
          },
          blockquote: ({ children }) => {
            const textStr = String(children);
            let type: CalloutType = 'info';
            if (textStr.includes('OGOHLANTIRISH') || textStr.includes('XATO')) type = 'error';
            else if (textStr.includes('MASLAHAT') || textStr.includes('Eslatma')) type = 'tip';

            return <DocCallout type={type}>{children}</DocCallout>;
          },
          table: ({ children }) => (
            <div className="my-6 overflow-x-auto rounded-xl border border-slate-200 dark:border-slate-800 shadow-xs">
              <table className="w-full text-left text-xs border-collapse">
                {children}
              </table>
            </div>
          ),
          thead: ({ children }) => (
            <thead className="bg-slate-100 dark:bg-slate-800/80 text-slate-900 dark:text-white font-bold border-b border-slate-200 dark:border-slate-700 uppercase tracking-wider text-[11px]">
              {children}
            </thead>
          ),
          th: ({ children }) => (
            <th className="py-3 px-4 font-bold">{children}</th>
          ),
          td: ({ children }) => (
            <td className="py-3 px-4 border-t border-slate-100 dark:border-slate-800/60 font-mono text-[13px] text-slate-700 dark:text-slate-300">
              {children}
            </td>
          ),
          ul: ({ children }) => (
            <ul className="my-4 space-y-2 list-disc list-inside text-slate-700 dark:text-slate-300 text-[15px]">
              {children}
            </ul>
          ),
          ol: ({ children }) => (
            <ol className="my-4 space-y-2 list-decimal list-inside text-slate-700 dark:text-slate-300 text-[15px]">
              {children}
            </ol>
          ),
          hr: () => <hr className="my-8 border-slate-200 dark:border-slate-800" />
        }}
      >
        {content}
      </Markdown>
    </div>
  );
};
