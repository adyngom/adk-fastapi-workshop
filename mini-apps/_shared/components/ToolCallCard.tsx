import React, { useState } from 'react';
import { ChevronDown, ChevronUp } from 'lucide-react';
import type { ToolCall } from '../types';

interface ToolCallCardProps {
  toolCall: ToolCall;
}

export const ToolCallCard: React.FC<ToolCallCardProps> = ({ toolCall }) => {
  const [expanded, setExpanded] = useState(false);

  return (
    <div className="bg-white border border-gray-200 rounded-lg shadow-sm overflow-hidden">
      <button
        onClick={() => setExpanded(!expanded)}
        className="w-full px-3 py-2 flex items-center justify-between hover:bg-gray-50 transition-colors"
      >
        <div className="flex items-center gap-2">
          <span className="text-green-500">✓</span>
          <span className="text-sm font-medium text-gray-700">🔧 {toolCall.name}</span>
        </div>
        {expanded ? (
          <ChevronUp className="w-4 h-4 text-gray-400" />
        ) : (
          <ChevronDown className="w-4 h-4 text-gray-400" />
        )}
      </button>

      {expanded && (
        <div className="px-3 py-2 bg-gray-50 border-t border-gray-200 text-xs font-mono">
          {toolCall.parameters && (
            <div className="mb-2">
              <div className="font-semibold text-gray-600 mb-1">Parameters:</div>
              <pre className="text-gray-800 overflow-x-auto whitespace-pre-wrap">
                {JSON.stringify(toolCall.parameters, null, 2)}
              </pre>
            </div>
          )}
          {toolCall.result && (
            <div>
              <div className="font-semibold text-gray-600 mb-1">Result:</div>
              <pre className="text-gray-800 overflow-x-auto whitespace-pre-wrap">
                {JSON.stringify(toolCall.result, null, 2)}
              </pre>
            </div>
          )}
        </div>
      )}
    </div>
  );
};
