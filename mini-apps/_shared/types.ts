// Shared TypeScript types across all mini-apps

export interface ToolCall {
  name: string;
  parameters?: Record<string, any>;
  result?: any;
  timestamp?: Date;
  duration?: number;
}

export interface Message {
  id: string;
  role: 'user' | 'agent' | 'system';
  content: string;
  timestamp: Date;
  toolCalls?: ToolCall[];
  metadata?: Record<string, any>;
}

export interface AgentStatus {
  name: string;
  status: 'idle' | 'running' | 'complete' | 'error';
  startTime?: Date;
  endTime?: Date;
  duration?: number;
  output?: any;
}

export type ConnectionStatus = 'connected' | 'disconnected' | 'connecting';

export interface AgentMetrics {
  requestCount: number;
  avgResponseTime: number;
  successRate: number;
  totalCost: number;
  tokenUsage: {
    input: number;
    output: number;
    total: number;
  };
}
