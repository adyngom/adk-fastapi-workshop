# Mini-Apps Monorepo - Complete Setup Guide

**Structure:** npm workspaces monorepo
**Shared Library:** `@adk-course/shared` (components, hooks, types)
**Apps:** 10 standalone Next.js apps (01-10)

---

## 🏗️ Architecture

```
mini-apps/
├── package.json              # Root - defines workspaces
├── _shared/                  # Shared library workspace
│   ├── package.json          # @adk-course/shared
│   ├── index.ts              # Exports
│   ├── components/           # Reusable React components
│   ├── hooks/                # Custom hooks
│   ├── lib/                  # Utilities
│   └── types.ts              # Shared TypeScript types
│
├── 01-greeting-chat/         # Next.js app workspace
│   ├── package.json          # Depends on @adk-course/shared
│   ├── next.config.js
│   ├── tsconfig.json
│   ├── tailwind.config.ts
│   ├── app/
│   │   ├── layout.tsx
│   │   ├── page.tsx
│   │   └── globals.css
│   └── components/
│       └── ADKGreetingChat.tsx
│
├── 02-customer-service/      # Next.js app workspace
│   └── (same structure)
...
└── 10-agent-ops-dashboard/   # Next.js app workspace
    └── (same structure)
```

---

## 🚀 Installation & Setup

### One-Time Setup (From mini-apps/ root):

```bash
# Navigate to mini-apps directory
cd /Users/adjidiortraore/Code/adk-fastapi-workshop/mini-apps

# Install all workspaces (shared + all apps)
npm install

# This installs:
# - _shared dependencies
# - 01-greeting-chat dependencies (including @adk-course/shared)
# - 02-customer-service dependencies
# - etc.
```

**npm workspaces automatically:**
- Links `@adk-course/shared` to all apps
- Hoists common dependencies (react, next, etc.)
- Creates single node_modules at root

---

## 🎯 Running Individual Apps

### From mini-apps root:

```bash
# Run greeting-chat
npm run dev:greeting
# Opens on http://localhost:3001

# Run customer-service
npm run dev:customer
# Opens on http://localhost:3002

# Run financial-dashboard
npm run dev:financial
# Opens on http://localhost:3003
```

### From individual app directory:

```bash
cd 01-greeting-chat
npm run dev
# Opens on configured port (3001)
```

---

## 📦 How Shared Library Works

### In _shared/index.ts:

```typescript
export { ToolCallCard } from './components/ToolCallCard';
export { LoadingSpinner } from './components/LoadingSpinner';
export type * from './types';
```

### In any app (e.g., greeting-chat):

```typescript
import { ToolCallCard, LoadingSpinner } from '@adk-course/shared';
import type { Message, ToolCall } from '@adk-course/shared';
```

**No relative imports needed!** Just `@adk-course/shared`.

---

## 🔧 Adding New Shared Components

### Step 1: Create component in _shared/

```bash
cd _shared/components
# Create NewComponent.tsx
```

### Step 2: Export from _shared/index.ts

```typescript
export { NewComponent } from './components/NewComponent';
```

### Step 3: Use in any app

```typescript
import { NewComponent } from '@adk-course/shared';
```

**Changes to shared library are immediately available in all apps!**

---

## 🎨 Shared Components Created

**Currently available:**

```typescript
// Components
import { ToolCallCard } from '@adk-course/shared';
import { LoadingSpinner, ThreeDotsLoader } from '@adk-course/shared';

// Types
import type {
  Message,
  ToolCall,
  AgentStatus,
  ConnectionStatus,
  AgentMetrics
} from '@adk-course/shared';

// Utilities
import { cn } from '@adk-course/shared';  // className merger
```

**To add more:**
- Create in `_shared/components/`
- Export from `_shared/index.ts`
- Use in any app!

---

## 🔌 Backend Integration

### All apps connect to FastAPI backend:

**Default:** http://localhost:8000/api/agents/chat

**Via Next.js rewrite (configured in each app's next.config.js):**

```javascript
async rewrites() {
  return [
    {
      source: '/api/agents/:path*',
      destination: 'http://localhost:8000/api/agents/:path*',
    },
  ];
}
```

**In component:**
```typescript
// Can use relative URL (Next.js rewrites to FastAPI)
fetch('/api/agents/chat', {
  method: 'POST',
  body: JSON.stringify({ message, agent: 'greeting_agent' })
})
```

**No CORS issues!** Next.js handles the proxy.

---

## 📝 Creating New Mini-App

### Quick Template:

```bash
# Copy greeting-chat as template
cp -r 01-greeting-chat 05-brand-intel-hub

cd 05-brand-intel-hub

# Update package.json name
# Update port in package.json scripts (3005)
# Replace components/ADKGreetingChat.tsx with your new component
# Update app/page.tsx to import new component

npm install
npm run dev
```

---

## 🎯 Development Workflow

### Working on Multiple Apps:

**Terminal 1:** Run FastAPI backend
```bash
cd /path/to/adk-fastapi-workshop
./.idx/start-services.sh
```

**Terminal 2:** Run greeting-chat
```bash
cd mini-apps
npm run dev:greeting
```

**Terminal 3:** Run customer-service
```bash
cd mini-apps
npm run dev:customer
```

**All apps can run simultaneously** (different ports)!

---

## 🐛 Troubleshooting

### "Cannot find module '@adk-course/shared'"

**Fix:**
```bash
# From mini-apps root
npm install
```

This installs shared library and links it to all workspaces.

---

### "Port 3000 already in use"

**Fix:** Each app uses different port (configured in package.json)
- greeting-chat: 3001
- customer-service: 3002
- etc.

---

### "Module not found: 'lucide-react'"

**Fix:**
```bash
# From mini-apps root
npm install lucide-react --workspace=_shared
```

Or individual app:
```bash
cd 01-greeting-chat
npm install lucide-react
```

---

### Backend connection fails

**Check:**
1. FastAPI running? `curl http://localhost:8000/health`
2. greeting_agent exists? `ls adk_agents/greeting_agent/`
3. API endpoint correct? Should be `/api/agents/chat`

---

## ✅ Setup Complete Checklist

**From mini-apps/ root:**

- [ ] `npm install` completed successfully
- [ ] `_shared/node_modules` exists
- [ ] `01-greeting-chat/node_modules` exists
- [ ] Can import from '@adk-course/shared' without errors
- [ ] `npm run dev:greeting` starts app on port 3001
- [ ] FastAPI backend running on port 8000
- [ ] Can send message and get response

**Total setup time:** 5-10 minutes (just npm install!)

---

## 🎬 Ready for Recording!

**Mini-app 1 (greeting-chat) is ready to demo!**

**For Module 3 recording:**
1. Start greeting-chat UI (localhost:3001)
2. Show it working (result-first hook!)
3. Then teach how to build it (follow script)

**Next apps:**
- Use Gemini prompts from GEMINI_PROMPTS_FOR_UI_GENERATION.md
- Each app imports from `@adk-course/shared`
- Build 2-3 hours each
- All follow same monorepo pattern

---

**Monorepo is production-ready!** 🚀
