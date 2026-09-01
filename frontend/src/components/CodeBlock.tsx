import React, { useState } from 'react';
import { Copy, Check, Terminal, Code2 } from 'lucide-react';

interface CodeBlockProps {
  code: string;
  language?: string;
  filename?: string;
  showLineNumbers?: boolean;
  isTerminal?: boolean;
}

export const CodeBlock: React.FC<CodeBlockProps> = ({
  code,
  language = 'python',
  filename,
  showLineNumbers = true,
  isTerminal = false,
}) => {
  const [copied, setCopied] = useState(false);

  const handleCopy = () => {
    navigator.clipboard.writeText(code.trim());
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  };

  // Basic Python Syntax Highlighter
  const highlightPython = (rawCode: string) => {
    const lines = rawCode.trim().split('\n');
    return lines.map((line, lIdx) => {
      // Comment
      if (line.trim().startsWith('#')) {
        return (
          <span key={lIdx} className="text-slate-500 italic">
            {line}
          </span>
        );
      }

      // Tokenize simple keywords
      const words = line.split(/(\s+|[()[\]{},.:"'])/);
      const highlightedTokens = words.map((token, tIdx) => {
        if (/^(def|class|import|from|return|if|elif|else|for|while|in|and|or|not|is|None|True|False|try|except|finally|raise|as|with|yield|lambda|break|continue)$/.test(token)) {
          return <span key={tIdx} className="text-purple-400 font-semibold">{token}</span>;
        }
        if (/^(print|len|range|int|float|str|bool|list|dict|set|tuple|type|input|sum|max|min|abs|enumerate|zip|open)$/.test(token)) {
          return <span key={tIdx} className="text-cyan-400 font-semibold">{token}</span>;
        }
        if (/^(".*?"|'.*?')$/.test(token)) {
          return <span key={tIdx} className="text-emerald-300">{token}</span>;
        }
        if (/^\d+(\.\d+)?$/.test(token)) {
          return <span key={tIdx} className="text-amber-400">{token}</span>;
        }
        if (token.startsWith('#')) {
          return <span key={tIdx} className="text-slate-500 italic">{token}</span>;
        }
        return <span key={tIdx} className="text-slate-200">{token}</span>;
      });

      return (
        <div key={lIdx} className="table-row font-['JetBrains_Mono',monospace]">
          {showLineNumbers && (
            <span className="table-cell select-none pr-4 text-right text-[12px] text-slate-600 dark:text-slate-600 font-mono w-8">
              {lIdx + 1}
            </span>
          )}
          <span className="table-cell pl-2 whitespace-pre leading-[1.7] text-[13.5px]">
            {highlightedTokens}
          </span>
        </div>
      );
    });
  };

  if (isTerminal || language === 'text' || language === 'output') {
    return (
      <div className="my-5 rounded-xl border border-slate-800 bg-[#090D16] shadow-xl overflow-hidden font-['JetBrains_Mono',monospace]">
        {/* Terminal Header */}
        <div className="bg-[#0F172A] px-4 py-2.5 flex items-center justify-between border-b border-slate-800">
          <div className="flex items-center gap-2">
            <div className="w-3 h-3 rounded-full bg-rose-500/80" />
            <div className="w-3 h-3 rounded-full bg-amber-500/80" />
            <div className="w-3 h-3 rounded-full bg-emerald-500/80" />
            <span className="ml-2 text-[11px] font-mono text-slate-400 flex items-center gap-1.5">
              <Terminal className="w-3.5 h-3.5 text-emerald-400" />
              <span>Natija (Terminal Output)</span>
            </span>
          </div>
          <button
            onClick={handleCopy}
            className="flex items-center gap-1 text-[11px] font-mono text-slate-400 hover:text-slate-200 transition-colors"
          >
            {copied ? <Check className="w-3.5 h-3.5 text-emerald-400" /> : <Copy className="w-3.5 h-3.5" />}
            <span>{copied ? 'Nusxalandi!' : 'Nusxalash'}</span>
          </button>
        </div>

        {/* Terminal Output */}
        <pre className="p-4 text-xs font-mono text-emerald-400 bg-[#060911] leading-relaxed overflow-x-auto">
          <code>
            <span className="text-slate-500 select-none">$ </span>
            {code.trim()}
          </code>
        </pre>
      </div>
    );
  }

  return (
    <div className="my-6 rounded-xl border border-slate-800 bg-[#0B1120] shadow-xl overflow-hidden font-['JetBrains_Mono',monospace]">
      {/* Code Header */}
      <div className="bg-[#0F172A] px-4 py-2.5 flex items-center justify-between border-b border-slate-800">
        <div className="flex items-center gap-2">
          <Code2 className="w-4 h-4 text-purple-400" />
          <span className="text-[11px] font-mono text-slate-300 font-bold uppercase tracking-wider">
            {filename || language || 'python'}
          </span>
        </div>

        <button
          onClick={handleCopy}
          className="flex items-center gap-1.5 px-2.5 py-1 rounded-md text-[11px] font-mono text-slate-300 hover:text-white bg-slate-800/80 hover:bg-slate-700 transition-all border border-slate-700"
        >
          {copied ? (
            <>
              <Check className="w-3.5 h-3.5 text-emerald-400" />
              <span className="text-emerald-400 font-bold">Nusxalandi!</span>
            </>
          ) : (
            <>
              <Copy className="w-3.5 h-3.5 text-slate-400" />
              <span>Nusxalash</span>
            </>
          )}
        </button>
      </div>

      {/* Code Content */}
      <div className="p-4 bg-[#090D16] overflow-x-auto text-[#E2E8F0] font-['JetBrains_Mono',monospace]">
        <div className="table w-full">
          {highlightPython(code)}
        </div>
      </div>
    </div>
  );
};
