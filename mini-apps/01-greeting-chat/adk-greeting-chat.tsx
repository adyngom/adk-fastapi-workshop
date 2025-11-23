import React, { useState, useEffect, useRef } from 'react';
import { Send, Mic, MicOff, ChevronDown, ChevronUp, Copy, Trash2, Menu, X, Check } from 'lucide-react';

// Types
interface ToolCall {
  name: string;
  parameters?: Record<string, any>;
  result?: any;
}

interface Message {
  id: string;
  role: 'user' | 'agent';
  content: string;
  timestamp: Date;
  toolCalls?: ToolCall[];
}

const ADKGreetingChat = () => {
  const [messages, setMessages] = useState<Message[]>([]);
  const [inputValue, setInputValue] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [connectionStatus, setConnectionStatus] = useState<'connected' | 'disconnected'>('disconnected');
  const [isRecording, setIsRecording] = useState(false);
  const [sidebarOpen, setSidebarOpen] = useState(false);
  const [copiedId, setCopiedId] = useState<string | null>(null);
  
  const messagesEndRef = useRef<HTMLDivElement>(null);
  const recognitionRef = useRef<any>(null);

  // Sample questions
  const sampleQuestions = [
    "What time is it?",
    "Tell me about my company",
    "What's the workshop structure?",
    "Who is the workshop instructor?",
    "What are the workshop prerequisites?"
  ];

  // Auto-scroll to bottom
  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages]);

  // Initialize connection (simulated)
  useEffect(() => {
    const timer = setTimeout(() => {
      setConnectionStatus('connected');
    }, 1000);
    return () => clearTimeout(timer);
  }, []);

  // Initialize Web Speech API
  useEffect(() => {
    if ('webkitSpeechRecognition' in window || 'SpeechRecognition' in window) {
      const SpeechRecognition = (window as any).webkitSpeechRecognition || (window as any).SpeechRecognition;
      recognitionRef.current = new SpeechRecognition();
      recognitionRef.current.continuous = false;
      recognitionRef.current.interimResults = false;

      recognitionRef.current.onresult = (event: any) => {
        const transcript = event.results[0][0].transcript;
        setInputValue(transcript);
        setIsRecording(false);
      };

      recognitionRef.current.onerror = () => {
        setIsRecording(false);
      };

      recognitionRef.current.onend = () => {
        setIsRecording(false);
      };
    }
  }, []);

  const toggleVoiceInput = () => {
    if (!recognitionRef.current) {
      alert('Speech recognition is not supported in your browser');
      return;
    }

    if (isRecording) {
      recognitionRef.current.stop();
      setIsRecording(false);
    } else {
      recognitionRef.current.start();
      setIsRecording(true);
    }
  };

  const sendMessage = async () => {
    if (!inputValue.trim() || isLoading) return;

    const userMessage: Message = {
      id: Date.now().toString(),
      role: 'user',
      content: inputValue.trim(),
      timestamp: new Date()
    };

    setMessages(prev => [...prev, userMessage]);
    setInputValue('');
    setIsLoading(true);

    try {
      // API call to FastAPI backend
      const response = await fetch('http://localhost:8000/api/agents/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          message: userMessage.content,
          agent: 'greeting_agent'
        })
      });

      if (!response.ok) throw new Error('API request failed');

      const data = await response.json();

      const agentMessage: Message = {
        id: (Date.now() + 1).toString(),
        role: 'agent',
        content: data.response || 'I received your message!',
        timestamp: new Date(),
        toolCalls: data.toolCalls || []
      };

      setMessages(prev => [...prev, agentMessage]);
    } catch (error) {
      // Fallback demo response if API is not available
      const demoResponse = getDemoResponse(userMessage.content);
      setMessages(prev => [...prev, demoResponse]);
    } finally {
      setIsLoading(false);
    }
  };

  // Demo response generator (for when API is unavailable)
  const getDemoResponse = (userInput: string): Message => {
    const lowerInput = userInput.toLowerCase();
    
    if (lowerInput.includes('time')) {
      return {
        id: (Date.now() + 1).toString(),
        role: 'agent',
        content: "It's currently 11:45 PM EST. Would you like me to check the time in a different timezone?",
        timestamp: new Date(),
        toolCalls: [{
          name: 'get_current_time',
          parameters: { timezone: 'EST' },
          result: { time: '23:45:00', timezone: 'EST', formatted: '11:45 PM EST' }
        }]
      };
    } else if (lowerInput.includes('company')) {
      return {
        id: (Date.now() + 1).toString(),
        role: 'agent',
        content: "Your company is **Acme Corporation**, a leading provider of innovative solutions. Founded in 2010, we specialize in cloud-based technologies and AI-driven products.",
        timestamp: new Date(),
        toolCalls: [{
          name: 'get_company_info',
          parameters: {},
          result: {
            company_name: 'Acme Corporation',
            founded: 2010,
            industry: 'Technology',
            specialization: 'Cloud & AI Solutions'
          }
        }]
      };
    } else if (lowerInput.includes('workshop')) {
      return {
        id: (Date.now() + 1).toString(),
        role: 'agent',
        content: "The **Google ADK Workshop** is structured in 12 modules, progressing from beginner to expert level. It covers agent creation, tool integration, multimodal inputs, and deployment strategies.",
        timestamp: new Date(),
        toolCalls: [{
          name: 'get_workshop_info',
          parameters: { section: 'structure' },
          result: {
            total_modules: 12,
            duration: '3+ hours',
            levels: ['Beginner', 'Intermediate', 'Expert'],
            topics: ['Agent Basics', 'Tool Integration', 'Multimodal', 'Deployment']
          }
        }]
      };
    }
    
    return {
      id: (Date.now() + 1).toString(),
      role: 'agent',
      content: "I'm your AI assistant powered by Google ADK! I can help you with information about the company, current time, and workshop details. What would you like to know?",
      timestamp: new Date()
    };
  };

  const handleSampleQuestion = (question: string) => {
    setInputValue(question);
    setSidebarOpen(false);
  };

  const clearChat = () => {
    if (confirm('Clear all messages?')) {
      setMessages([]);
    }
  };

  const copyMessage = (content: string, id: string) => {
    navigator.clipboard.writeText(content);
    setCopiedId(id);
    setTimeout(() => setCopiedId(null), 2000);
  };

  const handleKeyPress = (e: React.KeyboardEvent) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      sendMessage();
    }
  };

  return (
    <div className="flex h-screen bg-gray-50">
      {/* Sidebar */}
      <div className={`${sidebarOpen ? 'translate-x-0' : '-translate-x-full'} md:translate-x-0 fixed md:relative z-20 w-64 h-full bg-white border-r border-gray-200 transition-transform duration-300 ease-in-out`}>
        <div className="p-4 border-b border-gray-200 flex justify-between items-center">
          <h3 className="font-semibold text-gray-900">Sample Questions</h3>
          <button onClick={() => setSidebarOpen(false)} className="md:hidden text-gray-500 hover:text-gray-700">
            <X className="w-5 h-5" />
          </button>
        </div>
        <div className="p-4 space-y-2">
          {sampleQuestions.map((question, idx) => (
            <button
              key={idx}
              onClick={() => handleSampleQuestion(question)}
              className="w-full text-left px-3 py-2 rounded-lg text-sm text-gray-700 hover:bg-blue-50 hover:text-blue-600 transition-colors"
            >
              {question}
            </button>
          ))}
        </div>
      </div>

      {/* Main Chat Area */}
      <div className="flex-1 flex flex-col max-w-4xl mx-auto w-full">
        {/* Header */}
        <div className="bg-white border-b border-gray-200 px-4 py-4 shadow-sm">
          <div className="flex items-center justify-between">
            <div className="flex items-center gap-3">
              <button
                onClick={() => setSidebarOpen(!sidebarOpen)}
                className="md:hidden text-gray-500 hover:text-gray-700"
              >
                <Menu className="w-5 h-5" />
              </button>
              <div>
                <h1 className="text-xl font-semibold text-gray-900">Greeting Agent</h1>
                <p className="text-sm text-gray-500">Powered by Google ADK</p>
              </div>
            </div>
            <div className="flex items-center gap-3">
              <div className="flex items-center gap-2">
                <div className={`w-2 h-2 rounded-full ${connectionStatus === 'connected' ? 'bg-green-500' : 'bg-red-500'}`} />
                <span className="text-sm text-gray-600 capitalize">{connectionStatus}</span>
              </div>
              {messages.length > 0 && (
                <button
                  onClick={clearChat}
                  className="p-2 text-gray-500 hover:text-red-600 hover:bg-red-50 rounded-lg transition-colors"
                  title="Clear chat"
                >
                  <Trash2 className="w-4 h-4" />
                </button>
              )}
            </div>
          </div>
        </div>

        {/* Messages Area */}
        <div className="flex-1 overflow-y-auto p-4 space-y-4">
          {messages.length === 0 && (
            <div className="text-center py-12">
              <div className="text-6xl mb-4">🤖</div>
              <h2 className="text-2xl font-semibold text-gray-900 mb-2">Welcome to ADK Greeting Agent</h2>
              <p className="text-gray-600 mb-6">Ask about the company, time, or workshop details to get started!</p>
              <div className="flex flex-wrap gap-2 justify-center max-w-md mx-auto">
                {sampleQuestions.slice(0, 3).map((q, idx) => (
                  <button
                    key={idx}
                    onClick={() => handleSampleQuestion(q)}
                    className="px-4 py-2 bg-blue-50 text-blue-600 rounded-lg text-sm hover:bg-blue-100 transition-colors"
                  >
                    {q}
                  </button>
                ))}
              </div>
            </div>
          )}

          {messages.map((message) => (
            <MessageComponent
              key={message.id}
              message={message}
              onCopy={copyMessage}
              isCopied={copiedId === message.id}
            />
          ))}

          {isLoading && (
            <div className="flex items-start gap-3">
              <div className="w-8 h-8 rounded-full bg-gray-200 flex items-center justify-center flex-shrink-0">
                🤖
              </div>
              <div className="bg-gray-100 rounded-lg px-4 py-3">
                <div className="flex gap-1">
                  <div className="w-2 h-2 bg-gray-400 rounded-full animate-bounce" style={{ animationDelay: '0ms' }} />
                  <div className="w-2 h-2 bg-gray-400 rounded-full animate-bounce" style={{ animationDelay: '150ms' }} />
                  <div className="w-2 h-2 bg-gray-400 rounded-full animate-bounce" style={{ animationDelay: '300ms' }} />
                </div>
              </div>
            </div>
          )}

          <div ref={messagesEndRef} />
        </div>

        {/* Input Area */}
        <div className="bg-white border-t border-gray-200 p-4">
          <div className="max-w-3xl mx-auto">
            <div className="flex gap-2 items-end">
              <div className="flex-1 relative">
                <textarea
                  value={inputValue}
                  onChange={(e) => setInputValue(e.target.value)}
                  onKeyPress={handleKeyPress}
                  placeholder="Ask about the company, time, or workshop..."
                  rows={1}
                  className="w-full px-4 py-3 pr-12 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent resize-none"
                  style={{ minHeight: '52px', maxHeight: '150px' }}
                />
                <div className="absolute right-3 bottom-3 text-xs text-gray-400">
                  {inputValue.length}
                </div>
              </div>
              <button
                onClick={toggleVoiceInput}
                className={`p-3 rounded-lg transition-colors ${
                  isRecording 
                    ? 'bg-red-500 text-white hover:bg-red-600' 
                    : 'bg-gray-100 text-gray-600 hover:bg-gray-200'
                }`}
                title="Voice input"
              >
                {isRecording ? <MicOff className="w-5 h-5" /> : <Mic className="w-5 h-5" />}
              </button>
              <button
                onClick={sendMessage}
                disabled={!inputValue.trim() || isLoading}
                className="p-3 bg-blue-500 text-white rounded-lg hover:bg-blue-600 disabled:bg-gray-300 disabled:cursor-not-allowed transition-colors"
                title="Send message"
              >
                <Send className="w-5 h-5" />
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

// Message Component
const MessageComponent: React.FC<{
  message: Message;
  onCopy: (content: string, id: string) => void;
  isCopied: boolean;
}> = ({ message, onCopy, isCopied }) => {
  const isUser = message.role === 'user';

  return (
    <div className={`flex ${isUser ? 'justify-end' : 'justify-start'} items-start gap-3`}>
      {!isUser && (
        <div className="w-8 h-8 rounded-full bg-gray-200 flex items-center justify-center flex-shrink-0">
          🤖
        </div>
      )}
      
      <div className={`max-w-[70%] ${isUser ? 'order-1' : ''}`}>
        <div className={`rounded-lg px-4 py-3 ${
          isUser ? 'bg-blue-500 text-white' : 'bg-gray-100 text-gray-900'
        }`}>
          <div className="prose prose-sm max-w-none">
            {message.content.split('**').map((part, idx) => 
              idx % 2 === 0 ? part : <strong key={idx}>{part}</strong>
            )}
          </div>
        </div>

        {/* Tool Calls */}
        {message.toolCalls && message.toolCalls.length > 0 && (
          <div className="mt-2 space-y-2">
            {message.toolCalls.map((toolCall, idx) => (
              <ToolCallCard key={idx} toolCall={toolCall} />
            ))}
          </div>
        )}

        <div className="flex items-center gap-2 mt-1 px-1">
          <span className="text-xs text-gray-500">
            {message.timestamp.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })}
          </span>
          <button
            onClick={() => onCopy(message.content, message.id)}
            className="text-gray-400 hover:text-gray-600 transition-colors"
            title="Copy message"
          >
            {isCopied ? <Check className="w-3 h-3" /> : <Copy className="w-3 h-3" />}
          </button>
        </div>
      </div>

      {isUser && (
        <div className="w-8 h-8 rounded-full bg-blue-500 flex items-center justify-center flex-shrink-0">
          👤
        </div>
      )}
    </div>
  );
};

// Tool Call Card Component
const ToolCallCard: React.FC<{ toolCall: ToolCall }> = ({ toolCall }) => {
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
        {expanded ? <ChevronUp className="w-4 h-4 text-gray-400" /> : <ChevronDown className="w-4 h-4 text-gray-400" />}
      </button>
      
      {expanded && (
        <div className="px-3 py-2 bg-gray-50 border-t border-gray-200 text-xs font-mono">
          {toolCall.parameters && (
            <div className="mb-2">
              <div className="font-semibold text-gray-600 mb-1">Parameters:</div>
              <pre className="text-gray-800 overflow-x-auto">{JSON.stringify(toolCall.parameters, null, 2)}</pre>
            </div>
          )}
          {toolCall.result && (
            <div>
              <div className="font-semibold text-gray-600 mb-1">Result:</div>
              <pre className="text-gray-800 overflow-x-auto">{JSON.stringify(toolCall.result, null, 2)}</pre>
            </div>
          )}
        </div>
      )}
    </div>
  );
};

export default ADKGreetingChat;