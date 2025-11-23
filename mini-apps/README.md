# Mini-Apps - Production UI for Each Course Module

**Purpose:** Real production UIs for each agent pattern
**Framework:** Next.js 14 + React + Tailwind CSS
**Strategy:** "Show the result first" - students see working UI, then learn to build it

---

## 📱 Architecture

### Shared Component Library (`_shared/`)
Reusable components across all mini-apps:
- Chat interfaces
- Agent status cards
- Loading states
- Code displays
- Metrics visualization

### Individual Mini-Apps
Each module gets a focused, standalone UI:

| Module | App | Purpose |
|--------|-----|---------|
| 3 | `01-greeting-chat` | Simple chat with tool visualization + voice |
| 4 | `02-customer-service` | Support ticket dashboard |
| 4 | `03-content-studio` | Content creation interface |
| 5 | `04-financial-dashboard` | Stock analysis with 4 analysts |
| 5 | `05-brand-intel-hub` | Brand intelligence research |
| 6 | `06-knowledge-base` | Document Q&A with RAG |
| 7 | `07-dev-assistant` | Bug fixing with MCP integration |
| 8 | `08-project-planner` | Project planning tool |
| 8 | `09-verification-portal` | High-stakes decisions with audit |
| 9-14 | `10-agent-ops-dashboard` | Production monitoring & ops |

---

## 🎯 Design Principles

**1. Result-First:**
- Show working UI immediately
- Clear value proposition
- "This is what users see"

**2. Production-Ready:**
- Not debugging UIs (ADK Web is for that)
- Real business interfaces
- Deploy-ready styling

**3. Educational:**
- Visualize agent execution
- Show tool calls
- Display state passing

**4. Reusable:**
- Shared components minimize duplication
- Consistent design language
- Fast to build new apps

---

## 🚀 Quick Start

### Prerequisites:
```bash
# Install Node.js 18+ and npm
node --version  # Should be 18+
```

### Setup Shared Library:
```bash
cd mini-apps/_shared
npm install
```

### Run Any Mini-App:
```bash
cd mini-apps/01-greeting-chat
npm install
npm run dev
# Opens on localhost:3000
```

---

## 🎬 YouTube "Result-First" Format

**Each mini-app becomes a YouTube video:**

**HOOK (0:00-0:30):**
[Screen recording of mini-app working]
"Look at this - [describe what it does]
This [solves X problem] in [Y seconds]
Here's how I built it."

**BUILD (0:30-End):**
[Follow course module content]
- Agent code
- UI code
- Integration
- Testing

**RESULT (Last 2 min):**
[Full demo of finished app]
"And like that, production-ready AI system.
Full course: [link]"

---

## 🛠️ Tech Stack

**Frontend:**
- Next.js 14 (React framework)
- TypeScript (type safety)
- Tailwind CSS (styling)
- shadcn/ui (components)

**Backend:**
- FastAPI (already built!)
- WebSockets (real-time)
- ADK agents (already built!)

**Deployment:**
- Vercel (frontend) - Free tier!
- Cloud Run (backend) - Already covered in Module 9

---

## 📊 Value Proposition

**For students:**
- Not just code - deployable systems
- Real UIs, not debugging tools
- Production-ready from day one

**For course business:**
- Higher price point justified ($1,500 for 14 apps)
- YouTube hooks (show results = engagement)
- Differentiation (Brandon shows ADK Web, you show production UIs)

**For workshops:**
- Demo mini-apps live
- Students see immediate value
- "Take this code home and deploy it"

---

**This is the missing piece - production UIs make everything real!**
