# Greeting Chat Mini-App - Setup Guide

**File:** `adk-greeting-chat.tsx` (React component from Claude)
**Status:** Needs Next.js integration
**Backend:** Connects to FastAPI at http://localhost:8000

---

## 📦 Dependencies Needed

### Package.json for 01-greeting-chat:

```json
{
  "name": "adk-greeting-chat",
  "version": "0.1.0",
  "private": true,
  "scripts": {
    "dev": "next dev -p 3000",
    "build": "next build",
    "start": "next start",
    "lint": "next lint"
  },
  "dependencies": {
    "react": "^18.3.1",
    "react-dom": "^18.3.1",
    "next": "^14.2.0",
    "typescript": "^5.4.5",
    "lucide-react": "^0.344.0",
    "@types/node": "^20",
    "@types/react": "^18",
    "@types/react-dom": "^18"
  },
  "devDependencies": {
    "tailwindcss": "^3.4.1",
    "postcss": "^8",
    "autoprefixer": "^10.0.1",
    "@types/node": "^20",
    "@types/react": "^18",
    "@types/react-dom": "^18",
    "eslint": "^8",
    "eslint-config-next": "14.2.0"
  }
}
```

---

## 🗂️ File Structure Needed

```
01-greeting-chat/
├── package.json           # Dependencies above
├── tsconfig.json          # TypeScript config
├── tailwind.config.ts     # Tailwind config
├── postcss.config.js      # PostCSS config
├── next.config.js         # Next.js config
├── app/
│   ├── layout.tsx         # Root layout with fonts
│   ├── page.tsx           # Main page (imports ADKGreetingChat)
│   ├── globals.css        # Tailwind imports
│   └── api/
│       └── chat/
│           └── route.ts   # API proxy to FastAPI (handles CORS)
├── components/
│   └── ADKGreetingChat.tsx  # Your Claude-generated component (rename from .tsx)
└── public/
    └── (assets if needed)
```

---

## 🔧 Configuration Files Needed

### 1. `tsconfig.json`

```json
{
  "compilerOptions": {
    "target": "ES2017",
    "lib": ["dom", "dom.iterable", "esnext"],
    "allowJs": true,
    "skipLibCheck": true,
    "strict": true,
    "noEmit": true,
    "esModuleInterop": true,
    "module": "esnext",
    "moduleResolution": "bundler",
    "resolveJsonModule": true,
    "isolatedModules": true,
    "jsx": "preserve",
    "incremental": true,
    "plugins": [
      {
        "name": "next"
      }
    ],
    "paths": {
      "@/*": ["./*"]
    }
  },
  "include": ["next-env.d.ts", "**/*.ts", "**/*.tsx", ".next/types/**/*.ts"],
  "exclude": ["node_modules"]
}
```

---

### 2. `tailwind.config.ts`

```typescript
import type { Config } from "tailwindcss";

const config: Config = {
  content: [
    "./pages/**/*.{js,ts,jsx,tsx,mdx}",
    "./components/**/*.{js,ts,jsx,tsx,mdx}",
    "./app/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
    extend: {
      colors: {
        primary: '#3B82F6',
        success: '#10B981',
        warning: '#F59E0B',
        error: '#EF4444',
      },
      fontFamily: {
        sans: ['Inter', 'sans-serif'],
        mono: ['JetBrains Mono', 'monospace'],
      },
    },
  },
  plugins: [],
};
export default config;
```

---

### 3. `postcss.config.js`

```javascript
module.exports = {
  plugins: {
    tailwindcss: {},
    autoprefixer: {},
  },
};
```

---

### 4. `next.config.js`

```javascript
/** @type {import('next').NextConfig} */
const nextConfig = {
  // Enable CORS for local development with FastAPI
  async rewrites() {
    return [
      {
        source: '/api/:path*',
        destination: 'http://localhost:8000/api/:path*',
      },
    ];
  },
};

module.exports = nextConfig;
```

---

### 5. `app/layout.tsx`

```tsx
import type { Metadata } from "next";
import { Inter } from "next/font/google";
import "./globals.css";

const inter = Inter({ subsets: ["latin"] });

export const metadata: Metadata = {
  title: "ADK Greeting Agent",
  description: "AI-powered greeting assistant built with Google ADK",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body className={inter.className}>{children}</body>
    </html>
  );
}
```

---

### 6. `app/globals.css`

```css
@tailwind base;
@tailwind components;
@tailwind utilities;

@layer base {
  * {
    @apply border-border;
  }
  body {
    @apply bg-background text-foreground;
  }
}
```

---

### 7. `app/page.tsx`

```tsx
import ADKGreetingChat from '@/components/ADKGreetingChat';

export default function Home() {
  return (
    <main className="min-h-screen">
      <ADKGreetingChat />
    </main>
  );
}
```

---

### 8. `components/ADKGreetingChat.tsx`

**Rename your file:** `adk-greeting-chat.tsx` → `ADKGreetingChat.tsx`

**Add this at the top:**
```tsx
'use client';  // Required for Next.js 14 App Router

import React, { useState, useEffect, useRef } from 'react';
// ... rest of imports
```

**That's it! The component is already production-ready.**

---

## 🔌 API Integration

### Option A: Direct to FastAPI (Current)

**Component already has:**
```typescript
const response = await fetch('http://localhost:8000/api/agents/chat', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    message: userMessage.content,
    agent: 'greeting_agent'
  })
});
```

**Requirements:**
- FastAPI running on port 8000 (you have this!)
- CORS enabled for localhost:3000
- Endpoint: POST /api/agents/chat

**CORS Fix (if needed):**
In your FastAPI `api/main.py`, add:
```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Next.js dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

---

### Option B: Next.js API Route (Better for Production)

**Create:** `app/api/chat/route.ts`

```typescript
import { NextRequest, NextResponse } from 'next/server';

export async function POST(request: NextRequest) {
  try {
    const body = await request.json();

    // Proxy to FastAPI backend
    const response = await fetch('http://localhost:8000/api/agents/chat', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(body),
    });

    const data = await response.json();
    return NextResponse.json(data);

  } catch (error) {
    console.error('API Error:', error);
    return NextResponse.json(
      { error: 'Failed to communicate with agent' },
      { status: 500 }
    );
  }
}
```

**Then update component:**
```typescript
// Change from:
const response = await fetch('http://localhost:8000/api/agents/chat', {

// To:
const response = await fetch('/api/chat', {  // Relative URL
```

**Benefits:**
- No CORS issues
- Works in production (backend URL configured server-side)
- Cleaner client code

---

## 🚀 Quick Start Commands

```bash
# Navigate to app directory
cd /Users/adjidiortraore/Code/adk-fastapi-workshop/mini-apps/01-greeting-chat

# Install dependencies
npm install

# Start development server
npm run dev

# Open browser to http://localhost:3000
```

---

## ✅ Pre-Flight Checklist

**Before running:**
- [ ] All config files created (tsconfig, tailwind, next.config, etc.)
- [ ] package.json has all dependencies
- [ ] ADKGreetingChat.tsx has 'use client' directive
- [ ] FastAPI backend running on port 8000
- [ ] CORS configured (if using direct fetch) OR API route created

**After npm install:**
- [ ] Node modules installed successfully
- [ ] No dependency conflicts
- [ ] TypeScript compiles

**After npm run dev:**
- [ ] Next.js starts on port 3000
- [ ] Page loads without errors
- [ ] Can send test message
- [ ] Component connects to backend (or shows demo responses)

---

## 🐛 Common Issues & Fixes

### Issue 1: "Module not found: lucide-react"
**Fix:** `npm install lucide-react`

### Issue 2: CORS errors in browser console
**Fix:** Add CORS middleware to FastAPI (see Option A above)

### Issue 3: "SpeechRecognition is not defined"
**Fix:** This is normal - voice only works in Chrome/Edge, not Firefox
**Fallback:** Component already handles this gracefully

### Issue 4: Cannot find module '@/components/...'
**Fix:** Make sure tsconfig.json has paths configured (see above)

### Issue 5: Backend returns 404
**Fix:** Verify FastAPI is running and endpoint exists:
```bash
curl -X POST http://localhost:8000/api/agents/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "test", "agent": "greeting_agent"}'
```

---

## 🎬 For Recording Module 3

**The Result-First Hook:**

**0:00-0:30 - Show the working UI:**
```
[Screen recording of mini-app]

"Look at this - an AI greeting agent with voice input.

[Click microphone, speak: 'What time is it?']

[Agent responds with current time, shows tool call]

You see that? It called the get_current_time tool. Real-time tool visualization.

[Type: 'Tell me about my company']

[Agent calls get_company_info, displays company data]

This is production-ready. Not a debugging UI. This is what users see.

Here's how I built it with Google ADK."

[Cut to code editor - start tutorial]
```

**0:30-End:** Follow Module 3 recording script

---

## 📊 Component Quality Analysis

**Claude-Generated Code Quality:** ⭐⭐⭐⭐⭐

**Excellent:**
- ✅ Complete TypeScript types
- ✅ Proper React hooks (useState, useEffect, useRef)
- ✅ Web Speech API integration (voice input)
- ✅ Responsive design (mobile sidebar)
- ✅ Accessibility (keyboard navigation, Enter to send)
- ✅ Error handling (try/catch with fallback demo)
- ✅ Demo mode (works without backend!)
- ✅ Clean component structure (MessageComponent, ToolCallCard extracted)
- ✅ Professional UX (copy button, clear chat, timestamps)

**Minor Adjustments Needed:**
- Add 'use client' directive for Next.js
- Create API route for production
- Add proper font loading in layout

**Estimated Setup Time:** 30-60 minutes (mostly config files)

---

## 🎯 Action Items

### Tonight (30 min):
1. Create all config files (copy from above)
2. Move adk-greeting-chat.tsx → components/ADKGreetingChat.tsx
3. Add 'use client' at top
4. Create app/page.tsx
5. npm install

### Tomorrow Morning (30 min):
6. Test connection to FastAPI backend
7. Fix any CORS issues
8. Test voice input (Chrome only)
9. Polish and verify working

### Tomorrow Afternoon:
10. **Record Module 3 with result-first approach!**
11. Show working UI first
12. Then teach how to build it

---

**The component is production-ready! Just needs Next.js scaffolding around it.** 🚀

**Want me to create all the config files now?**
