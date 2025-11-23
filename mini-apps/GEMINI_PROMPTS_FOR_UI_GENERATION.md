# Gemini Prompts for Mini-App UI Generation

**Purpose:** Detailed prompts for Gemini/Claude to generate React/Next.js UIs
**Usage:** Copy prompt → Paste into Gemini 2.5 Pro or Claude → Get complete UI code
**Style:** Modern, professional, production-ready

---

## 🎨 Shared Design System (Use in ALL Prompts)

**Global Design Tokens:**
```
Colors:
- Primary: #3B82F6 (blue) - ADK brand, actions, links
- Success: #10B981 (green) - completed, verified, success states
- Warning: #F59E0B (yellow) - pending, caution
- Error: #EF4444 (red) - errors, critical, stop
- Neutral Gray: #6B7280 (text), #F3F4F6 (backgrounds)

Typography:
- Font: Inter (headers: SemiBold 600, body: Regular 400)
- Code: JetBrains Mono

Components:
- Use shadcn/ui components (https://ui.shadcn.com)
- Tailwind CSS for styling
- Lucide React for icons

Layout:
- Max width: 1200px centered
- Padding: 16px mobile, 24px desktop
- Rounded corners: 8px
- Shadows: subtle (shadow-sm, shadow-md)
```

---

## 📱 MINI-APP 1: Greeting Chat (Module 3)

### Prompt for Gemini:

```
Create a modern React/Next.js chat interface for an AI greeting agent with the following specifications:

DESIGN REQUIREMENTS:
- Modern, clean chat interface similar to ChatGPT
- Colors: Blue (#3B82F6) primary, Green (#10B981) for success
- Typography: Inter font family
- Dark mode optional but preferred
- Mobile responsive

UI COMPONENTS NEEDED:

1. HEADER:
   - Title: "Greeting Agent - Your AI Assistant"
   - Subtitle: "Powered by Google ADK"
   - Voice input toggle button (microphone icon)
   - Status indicator (connected/disconnected)

2. CHAT AREA (Main):
   - Message list (scrollable, auto-scroll to bottom)
   - User messages: Right-aligned, blue background (#3B82F6)
   - Agent messages: Left-aligned, gray background (#F3F4F6)
   - Timestamp on each message
   - Avatar icons (user icon, robot icon for agent)

3. TOOL CALL VISUALIZATION (Special message type):
   When agent calls a tool, show:
   - Tool name badge (e.g., "🔧 get_company_info")
   - Expandable details section (click to see parameters/results)
   - Success indicator (green checkmark)
   - Example:
     ```
     🔧 Called get_company_info()
     [Expand] → Shows: { "company_name": "Acme Corp", ... }
     ```

4. INPUT AREA (Bottom, sticky):
   - Text input field (multi-line, auto-expand up to 5 lines)
   - Send button (paper airplane icon, blue, disabled when empty)
   - Voice input button (microphone icon, toggle on/off)
   - Character count (subtle, gray)
   - Placeholder: "Ask about the company, time, or workshop..."

5. SIDEBAR (Optional, collapsible on mobile):
   - "Sample Questions" list:
     • "What time is it?"
     • "Tell me about my company"
     • "What's the workshop structure?"
   - Click to populate input

FUNCTIONALITY:

State Management:
- messages: array of {role: 'user'|'agent', content: string, timestamp, toolCalls?: []}
- isLoading: boolean (agent is thinking)
- connectionStatus: 'connected'|'disconnected'

API Integration:
- POST to /api/chat endpoint
- Body: { message: string, agent: 'greeting_agent' }
- Response: { response: string, toolCalls?: [] }
- WebSocket for streaming (optional but nice)

Tool Call Rendering:
- When response includes toolCalls array
- Render each as expandable card
- Show tool name, parameters, results
- Green success indicator

Voice Input (if enabled):
- Use Web Speech API
- Show recording indicator
- Transcribe to text input
- Auto-send on speech end

TECHNICAL STACK:
- Next.js 14 (App Router)
- TypeScript
- Tailwind CSS
- shadcn/ui components (Button, Card, Input, ScrollArea)
- Lucide React icons
- (Optional) Framer Motion for animations

FILE STRUCTURE:
```
01-greeting-chat/
├── app/
│   ├── page.tsx          # Main chat interface
│   ├── layout.tsx        # Root layout
│   └── api/
│       └── chat/
│           └── route.ts  # API endpoint (proxy to FastAPI)
├── components/
│   ├── ChatMessage.tsx   # Individual message component
│   ├── ToolCall.tsx      # Tool call visualization
│   ├── ChatInput.tsx     # Input with voice support
│   └── Sidebar.tsx       # Sample questions sidebar
├── lib/
│   └── api.ts            # API client functions
└── package.json
```

EXAMPLE INTERACTION FLOW:
1. User types: "What time is it?"
2. Click send → Message appears (user, right-aligned)
3. Loading indicator appears
4. Agent response arrives with toolCalls: [{ name: 'get_current_time', result: {...} }]
5. Show tool call card: "🔧 get_current_time" (expandable)
6. Show agent message: "It's currently 11:45 PM EST..."

ACCESSIBILITY:
- Keyboard navigation (Enter to send, Escape to cancel)
- ARIA labels for screen readers
- Focus states visible
- High contrast text

NICE-TO-HAVES:
- Message markdown rendering (bold, italic, code blocks)
- Copy message button
- Clear chat button
- Export conversation
- Dark/light mode toggle

Please generate:
1. Complete Next.js app structure
2. All component code (TypeScript)
3. API route (proxy to http://localhost:8000/api/agents/chat)
4. Tailwind config with design tokens
5. README with setup instructions

Make it production-ready, not a prototype. Focus on clean code and good UX.
```

---

## 📱 MINI-APP 2: Customer Service Portal (Module 4)

### Prompt for Gemini:

```
Create a customer support ticket dashboard UI for an AI-powered customer service system with Sequential workflow visualization.

DESIGN REQUIREMENTS:
- Professional support portal aesthetic (Zendesk/Intercom style)
- Colors: Blue primary, Green (resolved), Yellow (pending), Red (urgent)
- Typography: Inter font
- Dashboard layout with forms and visualization

UI COMPONENTS:

1. HEADER:
   - Title: "AI Customer Service Portal"
   - Stats bar: Total tickets, Avg response time, Resolution rate
   - Create ticket button (top-right, prominent)

2. TICKET SUBMISSION FORM (Left side, 40% width):
   - Customer name input
   - Email input
   - Issue category dropdown (Technical, Billing, Product, Account, Other)
   - Description textarea (multi-line)
   - Urgency selector (Critical, High, Medium, Low)
   - Submit button (blue, full-width)

3. AGENT WORKFLOW VISUALIZATION (Center, 35% width):
   Shows 3-agent Sequential flow in real-time:

   ```
   ┌─────────────┐
   │ 1. TRIAGE   │ ← Currently active (pulsing blue border)
   │  Analyzing  │    Shows: "Categorizing issue..."
   └─────────────┘
         ↓
   ┌─────────────┐
   │ 2. RESEARCH │ ← Waiting (gray)
   │   Pending   │
   └─────────────┘
         ↓
   ┌─────────────┐
   │ 3. RESPONSE │ ← Waiting (gray)
   │   Pending   │
   └─────────────┘
   ```

   As each agent completes:
   - Box turns green with checkmark
   - Shows completion time
   - Next agent activates (blue pulsing)
   - Display key output (e.g., "Priority: P1", "Found 3 similar tickets")

4. RESPONSE PANEL (Right side, 25% width):
   Initially empty/collapsed.
   When workflow completes:
   - Expands with animation
   - Shows final customer response
   - Email preview style
   - Copy response button
   - Send email button (simulated)

5. PAST TICKETS LIST (Bottom, scrollable):
   - Table view of processed tickets
   - Columns: ID, Issue, Priority, Status, Response Time
   - Click to view details
   - Filter by priority/status

FUNCTIONALITY:

Workflow States:
- idle: No ticket submitted
- processing: Agents running (show which agent is active)
- completed: All agents done, response ready
- error: Something failed

Sequential Agent Tracking:
- triageAgent: { status: 'running'|'complete', output: { category, priority }, time: number }
- researchAgent: { status: 'pending'|'running'|'complete', output: { solution }, time: number }
- responseAgent: { status: 'pending'|'running'|'complete', output: string, time: number }

API Integration:
- POST /api/agents/chat with agent: 'customer_service'
- WebSocket for real-time updates (agent status changes)
- Parse response to update workflow visualization

Animations:
- Agent boxes pulse when active
- Smooth transitions between states
- Confetti or success animation when complete
- Progress bar showing overall completion (33%, 66%, 100%)

TECH STACK:
- Next.js 14 + TypeScript
- Tailwind CSS
- shadcn/ui (Form, Card, Badge, ScrollArea)
- Framer Motion (animations)
- Lucide icons

FILE STRUCTURE:
```
02-customer-service/
├── app/
│   ├── page.tsx              # Main dashboard
│   └── api/chat/route.ts     # API proxy
├── components/
│   ├── TicketForm.tsx        # Left panel
│   ├── WorkflowViz.tsx       # Center panel (Sequential visualization)
│   ├── ResponsePanel.tsx     # Right panel
│   ├── AgentStage.tsx        # Individual agent box in workflow
│   └── TicketHistory.tsx     # Bottom table
└── lib/
    └── workflow.ts           # State management for 3-agent flow
```

KEY FEATURE: Sequential workflow visualization
- Must clearly show agent 1 → agent 2 → agent 3 progression
- Real-time updates as each completes
- Visual proof of "state passing" concept
- Students SEE the Sequential pattern, not just read about it

EXAMPLE INTERACTION:
1. User fills form: "Customer can't login after password reset"
2. Click Submit
3. Workflow starts:
   - Triage box activates (blue pulse) → "Analyzing..." → Complete (green ✓) → Shows "P1 - Technical"
   - Research box activates → "Searching knowledge base..." → Complete → Shows "Found: Clear cache solution"
   - Response box activates → "Generating response..." → Complete → Shows preview
4. Full response appears in right panel
5. User can copy/send

This visually demonstrates Sequential workflow from Module 4!

Generate complete production-ready code with excellent UX and smooth animations.
```

---

## 📱 MINI-APP 3: Content Studio (Module 4)

### Prompt for Gemini:

```
Create a content creation studio UI for an AI content pipeline with 4-agent Sequential workflow: Research → Draft → Optimize → Publish.

DESIGN:
- Creative studio aesthetic (Notion/Medium editor style)
- Colors: Blue (primary), Purple (creative), Green (publish ready)
- Clean, minimal, focus on the content

UI LAYOUT:

1. LEFT SIDEBAR (20%):
   - Topic input
   - Target audience selector
   - Platform selector (Medium, LinkedIn, Blog, Dev.to)
   - Generate button

2. CENTER EDITOR (60%):
   - Shows content as it's created
   - Tabs: Draft | Optimized | Formatted
   - Live markdown preview
   - Word count, reading time

3. RIGHT SIDEBAR (20%):
   - Pipeline Progress (4 stages):
     ```
     📚 Research     [✓] 12s
     ✍️  Draft       [✓] 45s
     ⚡ Optimize     [⏳] Running...
     🚀 Publish      [ ] Pending
     ```
   - Shows active stage with spinner
   - Click stage to see details

4. WORKFLOW DETAILS (Expandable):
   - Research: Shows sources found
   - Draft: Shows outline + sections
   - Optimize: Shows SEO keywords, readability score
   - Publish: Shows formatted content for platform

INTERACTION FLOW:
1. Enter topic: "AI agent production patterns"
2. Select audience: "Senior developers"
3. Select platform: "Medium"
4. Click Generate
5. Watch pipeline stages complete (animated)
6. Read final article in editor
7. Copy or export

Sequential visualization with 4 stages instead of 3.
Make it feel like a professional content tool, not a debug UI.

Next.js 14 + TypeScript + Tailwind + shadcn/ui.
```

---

## 📱 MINI-APP 4: Financial Dashboard (Module 5) ⭐

### Prompt for Gemini:

```
Create a financial analysis dashboard for AI-powered stock analysis with 4 PARALLEL analysts + synthesis.

DESIGN:
- Professional fintech aesthetic (Bloomberg/Robinhood style)
- Dark mode (financial data reads better dark)
- Colors: Blue (data), Green (buy), Red (sell), Gold (neutral)

UI LAYOUT:

1. TOP BAR:
   - Stock ticker input (large, prominent)
   - Risk profile selector (Conservative, Moderate, Aggressive)
   - Time horizon selector (Short, Medium, Long-term)
   - Analyze button

2. PARALLEL ANALYSTS GRID (4 cards, 2x2 or 1x4):

   Each analyst card shows:
   - Analyst icon and name
   - Status: Analyzing... (spinner) | Complete (checkmark) | Error
   - Completion time
   - Key metric (preview of their analysis)
   - Click to expand full analysis

   Cards:
   ```
   ┌─────────────────┐  ┌─────────────────┐
   │ 📊 DATA ANALYST │  │ 📈 TRADING      │
   │ Status: ✓ 8s   │  │ Status: ✓ 10s  │
   │ Price: $269    │  │ Strategy: Buy  │
   └─────────────────┘  └─────────────────┘

   ┌─────────────────┐  ┌─────────────────┐
   │ 🎯 EXECUTION    │  │ ⚠️  RISK        │
   │ Status: ✓ 7s   │  │ Status: ✓ 9s   │
   │ Limit orders   │  │ Risk: Moderate │
   └─────────────────┘  └─────────────────┘
   ```

3. SYNTHESIS PANEL (Bottom, full-width):
   - Activates AFTER all 4 analysts complete
   - Animated entrance
   - Shows: Combined recommendation
   - Highlights: Buy/Hold/Sell decision
   - Includes insights from all 4 analysts
   - Action plan (numbered steps)

4. THE $175 PROBLEM INDICATOR (Top-right corner):
   - Shows: "Data Age: 6 months old ⚠️"
   - Tooltip: "Price may be outdated. Using LLM training data."
   - In Module 7 version, this becomes: "Real-time data ✓"

KEY FEATURES:

Parallel Execution Visualization:
- All 4 analyst cards show spinners SIMULTANEOUSLY
- Progress bars sync (all start together)
- Different completion times (realistic - data: 8s, trading: 10s, etc.)
- Visual proof they're running in parallel, not sequential

Synthesis Animation:
- Waits for all 4 analysts
- Panel slides up from bottom
- Shows "Combining perspectives..." briefly
- Then displays unified recommendation

Comparison Mode (Optional):
- Toggle: "Show with/without real-time data"
- Demonstrates Module 5 problem vs Module 7 fix
- Side-by-side: $175 (old) vs $273 (real-time)

TECHNICAL:
- Next.js 14 + TypeScript
- Tailwind CSS
- shadcn/ui (Card, Badge, Button, Tabs)
- Framer Motion (analyst card animations)
- Chart.js or Recharts (if showing price charts)

FILE STRUCTURE:
```
04-financial-dashboard/
├── app/page.tsx
├── components/
│   ├── AnalystCard.tsx       # Reusable for 4 analysts
│   ├── SynthesisPanel.tsx
│   ├── StockInput.tsx
│   └── DataAgeIndicator.tsx  # The $175 warning
└── lib/
    └── formatters.ts         # Currency, percentages, etc.
```

INTERACTION:
1. Enter: AAPL
2. Select: Moderate risk, Long-term
3. Click Analyze
4. Watch: All 4 analysts start simultaneously (PARALLEL!)
5. See: Cards complete at different times
6. Wait: Synthesis panel slides up
7. Read: Unified recommendation with action plan

Must feel like a professional financial tool.
Emphasis on PARALLEL execution visualization - this is the teaching moment.

Generate complete production-ready code.
```

---

## 📱 MINI-APP 5: Brand Intelligence Hub (Module 5)

### Prompt for Gemini:

```
Create a brand intelligence research dashboard with 4 parallel researchers + synthesis.

DESIGN:
- Marketing/analytics aesthetic (similar to Brandwatch or Mention)
- Light mode, clean, data-focused
- Colors: Blue, Purple (social), Orange (trends), Red (competitors)

UI COMPONENTS:

1. SEARCH BAR (Top, prominent):
   - Brand name input (large)
   - Industry selector
   - Analyze button

2. PARALLEL RESEARCHERS (4 columns, equal width):

   Each column is a different source:
   ```
   ┌──────────────┐ ┌──────────────┐ ┌──────────────┐ ┌──────────────┐
   │ 📰 NEWS      │ │ 💬 SOCIAL    │ │ 📊 TRENDS    │ │ 🎯 COMPETE   │
   │ Searching... │ │ Searching... │ │ Searching... │ │ Searching... │
   │              │ │              │ │              │ │              │
   │ [Spinner]    │ │ [Spinner]    │ │ [Spinner]    │ │ [Spinner]    │
   └──────────────┘ └──────────────┘ └──────────────┘ └──────────────┘
   ```

   When complete:
   - Shows top 3-5 findings per source
   - Sentiment badges (Positive, Negative, Neutral)
   - Clickable cards to expand
   - Completion time

3. SYNTHESIS SECTION (Bottom, expands when ready):
   - Waits for all 4 researchers
   - Animated entrance
   - Executive summary
   - Key insights
   - Opportunities/Threats identified
   - Overall brand health score (0-100 with color coding)

4. EXPORT OPTIONS:
   - PDF report
   - CSV data
   - Share link

Parallel visualization is key - all 4 columns populate simultaneously.
Make it feel like a professional brand monitoring tool.

Next.js 14 + TypeScript + Tailwind + shadcn/ui.
```

---

## 📱 MINI-APP 6: Knowledge Base Search (Module 6)

### Prompt for Gemini:

```
Create a document Q&A interface with RAG (Retrieval-Augmented Generation) visualization.

DESIGN:
- Library/documentation aesthetic (Algolia DocSearch style)
- Clean, focused on reading
- Colors: Blue (primary), Green (found), Purple (semantic search)

UI COMPONENTS:

1. DOCUMENT UPLOAD AREA (Top):
   - Drag-and-drop zone
   - File list (shows uploaded PDFs, TXTs, MD files)
   - "Indexing..." status when processing
   - Total documents indexed counter

2. SEARCH/QUERY INTERFACE (Center):
   - Large search input: "Ask a question about your documents..."
   - Search button
   - Example questions (pills, click to populate)

3. RAG VISUALIZATION (Appears when query is made):

   Shows 3 stages:
   ```
   Question: "How do I build Sequential agents?"
      ↓
   [📚 RETRIEVAL]
   Searching 247 documents...
   Found 5 relevant sections:
   • "Sequential Workflows" (score: 0.94)
   • "Agent Patterns" (score: 0.87)
   • "State Passing" (score: 0.82)
      ↓
   [🤖 GENERATION]
   Using retrieved context to answer...
      ↓
   [✅ ANSWER]
   ```

4. ANSWER DISPLAY:
   - Markdown formatted answer
   - Source citations (links to documents)
   - Confidence score
   - "Retrieved context" expandable section (shows actual chunks used)

5. CONTEXT VIEWER (Expandable):
   - Shows the 5 retrieved document chunks
   - Highlighted relevant parts
   - Similarity scores
   - "This is how RAG works" educational overlay

KEY FEATURE: RAG visualization
- Students SEE retrieval happening
- See context being used
- Understand RAG is not magic - it's search + generate

Technical: Next.js 14 + TypeScript + Tailwind
File upload handling + Markdown rendering + Syntax highlighting

Make it feel like a professional documentation search tool (Algolia/Elastic style).
```

---

## 📱 MINI-APP 7: Dev Assistant (Module 7)

### Prompt for Gemini:

```
Create a developer bug-fixing assistant UI with MCP multi-source search visualization.

DESIGN:
- Developer tool aesthetic (GitHub/Linear style)
- Dark mode
- Code-focused
- Colors: Blue, Green (solution), Red (error), Purple (external sources)

UI COMPONENTS:

1. BUG INPUT AREA (Top):
   - Error message textarea (large)
   - Affected component input
   - Priority selector (P0-P3)
   - Environment tags (Browser, OS, Version)
   - Analyze button

2. MCP SEARCH VISUALIZATION (Center):

   Shows 3 parallel searches in real-time:
   ```
   ┌──────────────────┐  ┌──────────────────┐  ┌──────────────────┐
   │ 🗄️  DATABASE     │  │ 🐙 GITHUB        │  │ 📚 STACK OVERFLOW│
   │ Searching...     │  │ Searching...     │  │ Searching...     │
   │ 247 past tickets │  │ 15 repos         │  │ 1000+ questions  │
   └──────────────────┘  └──────────────────┘  └──────────────────┘
   ```

   When found:
   - Shows top 3 similar issues per source
   - Relevance scores
   - Resolution status
   - Click to view details

3. SOLUTION CARDS (Bottom):
   - Primary solution (most likely fix)
   - Alternative solutions (if primary fails)
   - Each card shows:
     • Implementation steps (numbered)
     • Code snippet (syntax highlighted)
     • Success probability
     • Estimated time
     • Sources cited

4. MCP CONNECTION STATUS (Top-right):
   - Shows connected sources:
     ✓ PostgreSQL (tickets DB)
     ✓ GitHub MCP Server
     ✓ Stack Overflow API
   - Visual indicators (green = connected)

KEY FEATURE: MCP visualization
- Students see multi-source search
- Understand external tool integration
- See how knowledge is aggregated

Technical: Next.js 14 + TypeScript + Tailwind
Code highlighting (Prism.js or Shiki)
Tabs for multiple solutions

Make it feel like a professional IDE assistant.
```

---

## 📱 MINI-APP 8: Project Planner (Module 8)

### Prompt for Gemini:

```
Create a project planning tool UI showing Sequential + Parallel combined orchestration.

DESIGN:
- Project management tool aesthetic (Linear/Asana style)
- Clean, professional
- Colors: Blue, Green, Orange, Purple for different agents

UI COMPONENTS:

1. PROJECT INPUT (Left, 30%):
   - Project name
   - Description (textarea)
   - Timeline estimate
   - Team size
   - Submit button

2. ORCHESTRATION VISUALIZATION (Center, 45%):

   Shows the complex workflow:
   ```
   [1. TASK BREAKDOWN] Sequential Step 1
         ↓
   ┌─────────────────────────────────────┐
   │ [2. PARALLEL ANALYSTS]              │ Sequential Step 2
   │  ┌─────┐  ┌─────┐  ┌─────┐        │ (contains Parallel!)
   │  │RES. │  │RISK │  │TIME │        │
   │  └─────┘  └─────┘  └─────┘        │
   └─────────────────────────────────────┘
         ↓
   [3. SYNTHESIS] Sequential Step 3
   ```

   Animated to show:
   - Task breakdown runs FIRST (sequential)
   - Then 3 analysts run SIMULTANEOUSLY (parallel)
   - Then synthesis runs LAST (sequential)

3. PROJECT PLAN OUTPUT (Right, 25%):
   - Executive summary
   - Timeline (Gantt-style)
   - Resource allocation
   - Risk mitigation
   - Download plan button

KEY FEATURE: Nested pattern visualization
- Clearly shows Sequential containing Parallel
- This is the "complex orchestration" from Module 8
- Visual proof of pattern nesting

Technical: Next.js 14 + TypeScript + Tailwind
Gantt chart library (if showing timeline)

Professional PM tool aesthetic.
```

---

## 📱 MINI-APP 9: Verification Portal (Module 8)

### Prompt for Gemini:

```
Create a high-stakes decision verification portal (charity/investment recommendations) with independent verification tracks and audit trail.

DESIGN:
- Trust-focused aesthetic (banking/financial portal style)
- Colors: Blue (primary), Green (verified), Yellow (pending verification), Red (failed verification)
- Security/compliance visual language

UI COMPONENTS:

1. REQUEST FORM (Top):
   - Decision type (Charity donation, Investment, Vendor selection)
   - Amount ($)
   - Criteria (checkboxes: High impact, Transparent, Low overhead, etc.)
   - Submit button

2. THREE-TRACK WORKFLOW VISUALIZATION (Center):

   Shows 3 parallel tracks:
   ```
   ┌─────────────────┐
   │ RESEARCH TRACK  │ → Finding candidates...
   │ [⏳ Running]    │
   └─────────────────┘

   ┌─────────────────┐
   │ VERIFICATION    │ → Checking credentials...
   │ [⏳ Running]    │ → (Independent from research!)
   └─────────────────┘

   ┌─────────────────┐
   │ AUDIT TRACK     │ → Logging decisions...
   │ [⏳ Running]    │
   └─────────────────┘
   ```

3. CANDIDATE CARDS (When research completes):
   - Shows 3-5 candidates
   - Each card has:
     • Name and description
     • Verification score (0-100) from independent track
     • Risk score (0-100)
     • Status badges (Verified ✓, Pending ⏳, Failed ✗)
     • Audit trail button

4. AUDIT TRAIL VIEWER (Expandable):
   - Timeline of every decision
   - Which agent made which determination
   - Sources checked
   - Timestamps
   - Downloadable audit log

5. FINAL RECOMMENDATION:
   - Top 3 verified candidates
   - Only shows those that passed verification
   - Clear reasoning
   - "Why this is trustworthy" explanation

KEY FEATURE: Independent verification visualization
- Research and Verification run in PARALLEL (separate tracks)
- Verification doesn't know which candidate Research prefers
- Shows "role separation" from AP2 protocol
- Audit trail proves accountability

This is the "trustworthy AI" moment from Module 8.

Make it feel secure, professional, compliance-ready.
Banking/fintech level trust indicators.

Next.js 14 + TypeScript + Tailwind + shadcn/ui.
```

---

## 📱 MINI-APP 10: Agent Ops Dashboard (Modules 9-14)

### Prompt for Gemini:

```
Create a unified operations dashboard for production AI agent monitoring, covering: Deployment status, Callbacks/logs, Evaluation results, A2A communication, and Cost metrics.

DESIGN:
- DevOps/monitoring tool aesthetic (Datadog/Grafana style)
- Dark mode
- Data-dense but organized
- Colors: Blue (primary), Green (healthy), Yellow (warning), Red (error)

UI LAYOUT:

1. TOP NAVIGATION:
   - Tabs: Overview | Agents | Deployments | Callbacks | Evaluation | A2A Graph | Costs
   - Time range selector (Last hour, 24h, 7d, 30d)
   - Refresh button

2. OVERVIEW TAB:
   - Key metrics cards (4 across):
     • Total Requests (24h)
     • Avg Response Time
     • Success Rate (%)
     • Total Cost ($)
   - Live agent status list:
     • greeting_agent: Running (green dot)
     • customer_service: Running
     • financial_advisor: Running
     • etc.

3. DEPLOYMENTS TAB (Module 9):
   - List of deployed agents
   - Platform badges (Cloud Run, GKE, Agent Engine)
   - URL/endpoint
   - Last deploy time
   - Health status
   - Quick actions (Logs, Metrics, Redeploy)

4. CALLBACKS TAB (Module 10):
   - Real-time log stream
   - Filterable (agent, tool, model callbacks)
   - Shows: before_agent, after_agent, tool calls, LLM requests
   - Color-coded by type
   - Search/filter bar

5. EVALUATION TAB (Module 12):
   - Eval suite results
   - Pass/Fail status
   - Quality scores
   - Trajectory analysis
   - Regression detection
   - Charts (score over time)

6. A2A GRAPH TAB (Module 13):
   - Visual graph of agents calling other agents
   - Nodes: Agents
   - Edges: Calls between agents
   - Click node to see agent details
   - Shows dynamic routing

7. COSTS TAB:
   - Cost breakdown by agent
   - Token usage graphs
   - Model distribution (Flash vs Pro)
   - Cost per request
   - Optimization suggestions

This is a PRODUCTION monitoring tool.
Should feel like real DevOps dashboard.
Multiple data visualizations.

Next.js 14 + TypeScript + Tailwind
Charts: Recharts or Chart.js
Graph: React Flow (for A2A visualization)

Make it look like enterprise monitoring software.
```

---

## 📱 MINI-APPS 6, 7 (Shorter Prompts)

### App 6: Knowledge Base (Module 6)
```
Document Q&A interface with RAG visualization.
- Upload documents area
- Search interface
- Shows: Query → Retrieval (5 chunks) → Generation (answer)
- Retrieved context display (expandable)
- Source citations
Make it feel like Algolia DocSearch or Notion AI.
```

### App 7: Dev Assistant (Module 7)
```
Bug fixing interface with MCP multi-source search.
- Error input form
- 3 parallel search sources: DB, GitHub, Stack Overflow
- Solution cards with code snippets
- MCP connection status indicators
Make it feel like GitHub Copilot or Cursor.
```

---

## 🎯 Usage Instructions

### For Each Mini-App:

**Step 1:** Copy the prompt for desired app
**Step 2:** Paste into Gemini 2.5 Pro or Claude Sonnet
**Step 3:** Get complete code (pages, components, API routes)
**Step 4:** Save to respective `/mini-apps/[app-name]/` directory
**Step 5:** npm install && npm run dev
**Step 6:** Test with your ADK agent backend
**Step 7:** Polish and adjust as needed

### Shared Components:

Build once, import into all apps:
- ChatInterface
- AgentCard
- LoadingSpinner
- ToolCallDisplay
- MetricsCard

**Time saved:** 1-2 hours per app by reusing components

---

## 📊 Estimated Build Time

**Shared Library:** 6-8 hours (one-time investment)
**Per Mini-App:** 2-3 hours each (with AI generation + customization)

**Total for 10 mini-apps:**
- Shared: 8 hours
- 10 apps × 2.5 hours = 25 hours
- **Total: 33 hours** (~4-5 days if focused)

**With Gemini doing heavy lifting:**
- Gemini generates 70-80% of code
- You customize and integrate
- Much faster than coding from scratch

---

## 🚀 Recommended Build Order

**Week 1:**
1. Shared component library
2. App 1: greeting-chat (simplest, tests integration)
3. App 4: financial-dashboard (has the $175 → $269 magic moment!)
4. App 9: verification-portal (shows AP2 accountability)

**Why these first:** Highest YouTube potential, best hooks

**Week 2:**
5-10. Build remaining apps

**Then:** Record all modules with result-first approach

---

**These prompts will generate 80% of the UI code. You polish and integrate!** 🚀
