# FastAPI + ADK Wrapper Architecture

**Purpose**: Understand how ADK agents are integrated with FastAPI for production applications

---

## 🎯 Why This Matters

**ADK Web** (Google's UI) is great for:
- ✅ Debugging agent behavior
- ✅ Visualizing tool calls
- ✅ Development and testing

**FastAPI Wrapper** is needed for:
- ✅ Production web applications
- ✅ Custom user experiences
- ✅ API integrations
- ✅ Mobile apps
- ✅ Business logic integration
- ✅ Authentication/authorization
- ✅ Custom frontends (React, Streamlit, etc.)

**This workshop teaches both**: ADK Web for development, FastAPI for production.

---

## 🏗️ Architecture Overview

```
┌─────────────────────────────────────────────────────────────┐
│                     USER INTERFACES                         │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐    │
│  │ Custom Chat  │  │  ADK Web UI  │  │  Streamlit   │    │
│  │ (port 80)    │  │  (port 3002) │  │  (port 8501) │    │
│  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘    │
│         │                 │                  │             │
└─────────┼─────────────────┼──────────────────┼─────────────┘
          │                 │                  │
          │                 │                  │
┌─────────▼─────────────────┼──────────────────▼─────────────┐
│              FASTAPI BACKEND (port 8000)                    │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌──────────────────────────────────────────────┐          │
│  │            api/main.py                       │          │
│  │  - WebSocket: /ws/chat/{session_id}         │          │
│  │  - REST: /api/agents/list                   │          │
│  │  - REST: /api/agents/chat                   │          │
│  └────────────────┬─────────────────────────────┘          │
│                   │                                         │
│  ┌────────────────▼─────────────────────────────┐          │
│  │         agents/manager.py                    │          │
│  │  - AgentManager class                        │          │
│  │  - Discovers agents from adk_agents/         │          │
│  │  - Loads ADK agent objects                   │          │
│  │  - Manages sessions (in-memory)              │          │
│  │  - Streams responses                         │          │
│  └────────────────┬─────────────────────────────┘          │
│                   │                                         │
└───────────────────┼─────────────────────────────────────────┘
                    │
┌───────────────────▼─────────────────────────────────────────┐
│                 ADK AGENTS LAYER                            │
├─────────────────────────────────────────────────────────────┤
│  adk_agents/                                                │
│    ├── greeting_agent/                                      │
│    │     ├── agent.py  (root_agent = Agent(...))           │
│    │     └── tools.py  (Python functions)                  │
│    ├── news_pipeline/                                       │
│    │     ├── agent.py  (root_agent = SequentialAgent)      │
│    │     └── sub_agents/...                                │
│    └── competitive_analysis/                                │
│          ├── agent.py  (root_agent = Sequential+Parallel)  │
│          └── sub_agents/...                                │
└─────────────────────────────────────────────────────────────┘
                    │
                    │ Uses
                    ↓
┌─────────────────────────────────────────────────────────────┐
│              GOOGLE GEMINI API                              │
│         (Model execution + tool calling)                    │
└─────────────────────────────────────────────────────────────┘
```

---

## 🔄 Complete Request Flow

### Example: User asks "What time is it?"

**Step 1: Frontend → FastAPI**
```javascript
// frontend/index.html
ws.send(JSON.stringify({
    message: "What time is it?",
    agent: "greeting_agent"
}));
```

**Step 2: FastAPI WebSocket Endpoint**
```python
# api/main.py:75
@app.websocket("/ws/chat/{session_id}")
async def websocket_chat(websocket: WebSocket, session_id: str):
    data = await websocket.receive_text()
    message_data = json.loads(data)

    # Call agent manager
    async for chunk in agent_manager.stream_chat(
        session_id=session_id,
        message=message_data.get("message"),
        agent_name=message_data.get("agent")
    ):
        await websocket.send_json(chunk)
```

**Step 3: Agent Manager Lookup**
```python
# agents/manager.py:62
async def stream_chat(self, session_id, message, agent_name):
    # Get the ADK agent object
    adk_agent = self.agents[agent_name]  # greeting_agent object
```

**Step 4: Run ADK Agent**
```python
# agents/manager.py:88
from google.adk.runners import run_agent

async for event in run_agent(adk_agent, context={"user_message": message}, stream=True):
    if hasattr(event, 'text') and event.text:
        yield {"type": "chunk", "content": event.text, "agent": agent_name}
```

**Step 5: ADK Executes (Behind the Scenes)**
```
ADK Agent:
  1. Reads instruction: "When user asks time, ALWAYS call get_current_time()"
  2. Sees tools: [get_workshop_info, get_current_time, list_available_agents]
  3. Decides: Need to call get_current_time()
  4. Executes: get_current_time() → {"current_time": "03:17 PM", ...}
  5. Generates: "It is Monday, November 03, 2025 at 03:17 PM EST."
  6. Streams response back
```

**Step 6: Response Stream Back**
```
run_agent() yields events
    ↓
agent_manager.stream_chat() yields chunks
    ↓
WebSocket sends JSON: {"type": "chunk", "content": "It is...", "agent": "greeting_agent"}
    ↓
Frontend receives and renders with markdown
```

---

## 📁 Component Deep Dive

### 1. `agents/manager.py` - The Bridge

**Responsibilities**:
- Load ADK agents from `adk_agents/` directory
- Store agent objects in registry
- Provide streaming interface compatible with FastAPI
- Manage conversation sessions
- Handle errors gracefully

**Key Methods**:

```python
class AgentManager:
    def __init__(self):
        self.agents: Dict[str, any] = {}      # ADK agent objects
        self.sessions: Dict[str, List] = {}   # Conversation history

    async def initialize(self):
        """Called on FastAPI startup - loads all agents"""
        # Current: Hardcoded list
        # Future: Auto-discovery

    async def _load_adk_agent(self, agent_name: str):
        """Import and store one ADK agent"""
        module = importlib.import_module(f"{agent_name}.agent")
        self.agents[agent_name] = module.root_agent

    async def stream_chat(self, session_id, message, agent_name):
        """Execute agent and stream response"""
        adk_agent = self.agents[agent_name]
        async for event in run_agent(adk_agent, ...):
            yield chunk
```

**Design Decision**: Why not use ADK directly in FastAPI routes?
- ✅ Separation of concerns (agents vs API)
- ✅ Can swap agent implementations
- ✅ Centralized session management
- ✅ Easier to add middleware (auth, logging, rate limiting)

---

### 2. `api/main.py` - FastAPI Application

**Responsibilities**:
- Create FastAPI app
- Initialize AgentManager on startup
- Provide WebSocket endpoint for chat
- Handle CORS
- Serve API documentation

**Key Pattern**: Lifespan Events
```python
@asynccontextmanager
async def lifespan(app: FastAPI):
    global agent_manager

    # Startup: Create and initialize manager
    agent_manager = AgentManager()
    await agent_manager.initialize()

    yield

    # Shutdown: Cleanup
    await agent_manager.cleanup()
```

**Why WebSocket instead of REST?**
- ✅ Real-time streaming (see agent thinking)
- ✅ Bidirectional communication
- ✅ Tool calls visible as they happen
- ✅ Better UX (progressive response)

---

### 3. `adk_agents/` - Agent Definitions

**Structure**:
```
adk_agents/
  └── {agent_name}/
       ├── agent.py          # REQUIRED: Must export root_agent
       ├── tools.py          # Optional: Custom Python functions
       └── sub_agents/       # Optional: For multi-agent workflows
            └── {sub_name}/
                 └── agent.py
```

**Contract**: Every agent must:
1. Be in `adk_agents/{agent_name}/` directory
2. Have `agent.py` file
3. Export variable named `root_agent`
4. `root_agent` is an ADK `Agent`, `SequentialAgent`, or `ParallelAgent`

---

### 4. Frontend - WebSocket Client

**Current**: Generic chat UI that works with any agent

**Data Format**:
```javascript
// Send
{
  "message": "User's message here",
  "agent": "greeting_agent"
}

// Receive
{
  "type": "chunk",           // or "complete", "error"
  "content": "Response text",
  "agent": "greeting_agent"
}
```

**Rendering**: Uses marked.js to render markdown in responses

---

## 🔄 Current Limitations & Fixes

### Limitation 1: Hardcoded Agent Registration
**Current**:
```python
# agents/manager.py:29-31
await self._load_adk_agent("greeting_agent")
await self._load_adk_agent("news_pipeline")
await self._load_adk_agent("competitive_analysis")
```

**Fix**: Auto-discovery
```python
async def initialize(self):
    agents = self._discover_agents()  # Scan adk_agents/
    for agent_name in agents:
        await self._load_adk_agent(agent_name)
```

**Benefit**: Add agent by creating directory, no code changes needed

---

### Limitation 2: Generic Frontend Only
**Current**: One chat UI for all agents

**Fix**: Per-agent frontends
```
frontends/
  ├── default/           # Generic chat (current frontend/)
  ├── news_pipeline/     # Custom: Shows news cards, sentiment chart
  └── competitive_analysis/  # Custom: Comparison table, charts
```

**Routing**: NGINX serves appropriate frontend based on URL

---

### Limitation 3: No Streamlit Integration
**Future**: Streamlit apps per agent
```
streamlit_apps/
  └── news_dashboard/
       ├── app.py         # Streamlit UI
       ├── requirements.txt
       └── config.toml
```

**Integration**: Streamlit → FastAPI backend via HTTP/WebSocket

---

## 📝 Repeatable Pattern for New Agents

### Current Process (Manual):
1. Create `adk_agents/new_agent/agent.py`
2. Define `root_agent = Agent(...)`
3. **Manually add** to `manager.py` initialize()
4. Restart Docker
5. Test in generic frontend

### Future Process (Auto-discovery):
1. Create `adk_agents/new_agent/agent.py`
2. Define `root_agent = Agent(...)`
3. ~~Manually add to manager.py~~ **← AUTOMATIC**
4. Restart Docker
5. **Agent appears in dropdown automatically**

**Optional**: Create custom frontend in `frontends/new_agent/`

---

---

## ✅ Implementation Status

### ✅ Implemented: Auto-Discovery

**Code**: `agents/manager.py:42-84`

```python
def _discover_agents(self, adk_agents_path: Path) -> List[str]:
    """Scan adk_agents/ for valid agents"""
    agents = []
    for item in adk_agents_path.iterdir():
        if not item.is_dir() or item.name.startswith('_'):
            continue
        agent_file = item / "agent.py"
        if agent_file.exists():
            content = agent_file.read_text()
            if 'root_agent' in content:
                agents.append(item.name)
    return sorted(agents)
```

**Result**: New agents auto-discovered on restart!

**Test**:
```bash
curl http://localhost:8000/api/agents/list | jq
# Shows all discovered agents with metadata
```

---

### ✅ Implemented: Agent List API

**Code**: `api/routes/agents.py:19-40`

```python
@router.get("/list", response_model=List[AgentInfo])
async def list_agents():
    """List all available agents discovered from adk_agents/"""
    agent_infos = []
    for agent_name, agent_obj in _agent_manager.agents.items():
        info = AgentInfo(
            name=agent_name,
            description=agent_obj.description,
            capabilities=["chat", "streaming", "tools"] if agent_obj.tools else ["chat"],
            status="active"
        )
        agent_infos.append(info)
    return agent_infos
```

**Access**: GET http://localhost:8000/api/agents/list

---

### ✅ Implemented: Streamlit Integration

**Files**:
- `streamlit_apps/generic_chat/app.py` - Full-featured chat UI
- `streamlit_apps/generic_chat/requirements.txt` - Dependencies
- `Dockerfile.streamlit` - Container definition
- `docker-compose.yml` - Streamlit service (profile: streamlit)

**Start**:
```bash
docker compose --profile streamlit up -d
# Access: http://localhost:8501
```

**Features**:
- Agent selector (pulls from /api/agents/list)
- Chat interface
- Session persistence
- Error handling
- Clear chat button

---

### 🔄 Future: Per-Agent Frontends

**Planned structure**:
```
frontends/
  ├── default/           # Generic chat (current frontend/)
  ├── news_pipeline/     # Custom: News cards, sentiment charts
  └── weather_agent/     # Custom: Weather widget, forecast table
```

**NGINX routing** (to implement):
```nginx
location ~ ^/agents/(.+) {
    alias /usr/share/nginx/frontends/$1;
    try_files $uri $uri/ /index.html;
}
```

---

## 📚 Documentation Created

1. **`docs/FASTAPI_WRAPPER_ARCHITECTURE.md`** (this file)
   - Complete architecture explanation
   - Data flow diagrams
   - Component responsibilities

2. **`docs/ADD_NEW_AGENT.md`**
   - Step-by-step agent creation
   - Complete examples
   - Testing checklist
   - Common mistakes

3. **`docs/STREAMLIT_INTEGRATION.md`**
   - Why Streamlit for agent UIs
   - Integration patterns
   - Complete examples
   - Best practices

---

## 🎓 For Workshop Instructors

### Teaching the Wrapper

**Slide 1**: Show the architecture diagram
- Three layers: Frontend, FastAPI, ADK Agents
- Single source of truth: `adk_agents/`

**Slide 2**: Live demo auto-discovery
1. Show existing agents
2. Create new simple agent
3. Restart services
4. Agent appears automatically

**Slide 3**: Show tool execution
- ADK Web: Events tab shows tool calls
- Custom UI: Same agent, same tools
- Point: One agent, multiple interfaces

**Slide 4**: Explain why this matters
- Development: ADK Web
- Production: Custom frontend
- Internal tools: Streamlit
- Same agent works everywhere

### Key Teaching Points

**For students to understand**:
1. ADK agents are defined once (`adk_agents/`)
2. FastAPI wrapper discovers and loads them
3. Multiple frontends can use same backend
4. Tools work automatically (no frontend changes needed)

**Common questions**:
- Q: "Why not use ADK Web in production?"
- A: "ADK Web is for debugging. Production needs custom UX, auth, business logic."

- Q: "Do we need to update FastAPI when adding agents?"
- A: "No! Just create agent directory, restart services."

- Q: "Can we use REST instead of WebSocket?"
- A: "Yes! `/api/agents/chat` endpoint (non-streaming). WebSocket is for real-time streaming."

---

## 🚀 Next Steps

**You now have**:
- ✅ Auto-discovery (no hardcoded agent lists)
- ✅ REST API for agent listing
- ✅ Streamlit integration template
- ✅ Complete documentation

**To teach students**:
1. Show them ADD_NEW_AGENT.md
2. Have them create their own agent
3. Watch it appear automatically
4. (Optional) Create custom Streamlit UI

**For your 99 Agents Masterclass**:
- Expand to per-agent frontends
- Add authentication/authorization
- Production deployment patterns
- Advanced Streamlit dashboards

---

## 🎯 The Repeatable Pattern (For Instructors)

### The Core Insight

**Single Source of Truth**: `adk_agents/{agent_name}/agent.py`

Everything else is automatic:
- ✅ Discovery (manager scans directory)
- ✅ Loading (imports root_agent)
- ✅ API exposure (/api/agents/list shows it)
- ✅ Frontend integration (dropdown populates)
- ✅ ADK Web (shows it too)

**One agent definition → Works everywhere**

---

### Scaling to 99 Agents

**Problem**: How to manage 99 agents without chaos?

**Solution**: Convention over configuration

**Convention**:
```
adk_agents/
  ├── {agent_name}/       # Snake_case name
  │    ├── agent.py       # Must export root_agent
  │    ├── tools.py       # Optional: Custom functions
  │    └── sub_agents/    # Optional: For workflows
  └── ... (98 more)
```

**Result**:
- Add agent = Create directory + agent.py
- Remove agent = Delete directory
- Update agent = Edit agent.py
- No FastAPI code changes ever needed!

---

### When Students Ask: "How does it work?"

**Explain in layers**:

**Layer 1: Agent Definition** (What they create)
```python
# adk_agents/my_agent/agent.py
root_agent = Agent(
    name="my_agent",
    instruction="...",
    tools=[...]
)
```

**Layer 2: Auto-Discovery** (Automatic)
```python
# agents/manager.py discovers this agent
# by scanning adk_agents/ directory
```

**Layer 3: FastAPI Exposure** (Automatic)
```python
# /ws/chat/{session_id} endpoint uses agent
# /api/agents/list shows agent metadata
```

**Layer 4: Frontend Access** (Automatic)
```javascript
// Frontend queries /api/agents/list
// Populates dropdown
// User selects agent
// WebSocket routes to that agent
```

**One directory → Four layers working together!**

---

### Design Decisions Explained

**Decision 1**: Why auto-discovery vs manual registration?

**Manual** (old way):
- ❌ Edit manager.py every time
- ❌ Easy to forget
- ❌ Merge conflicts with multiple developers
- ❌ Doesn't scale to 99 agents

**Auto-discovery** (new way):
- ✅ Just add directory
- ✅ Can't forget
- ✅ No merge conflicts
- ✅ Scales infinitely

**Decision 2**: Why import actual ADK agents vs parsing text?

**Text parsing** (old way):
- ❌ Can't access tools
- ❌ Can't use ADK's built-in features
- ❌ Brittle (breaks with syntax changes)

**Import real objects** (new way):
- ✅ Tools work automatically
- ✅ All ADK features available
- ✅ Type-safe
- ✅ Easier to debug

**Decision 3**: Why WebSocket vs REST?

**Both are provided!**
- WebSocket (`/ws/chat`): Streaming, real-time, tool calls visible
- REST (`/api/agents/chat`): Simple request/response, easier integration

**Use WebSocket for**: Chat UIs, real-time dashboards
**Use REST for**: Simple integrations, mobile apps, third-party services

---

## 🔬 Advanced: Understanding the Manager

### The AgentManager Class Lifecycle

**1. Initialization** (FastAPI startup):
```python
# api/main.py lifespan
agent_manager = AgentManager()
await agent_manager.initialize()
```

**2. Discovery**:
```python
# agents/manager.py
discovered = self._discover_agents(adk_agents_path)
# Returns: ['agent_a', 'agent_b', 'agent_c']
```

**3. Loading**:
```python
for agent_name in discovered:
    module = importlib.import_module(f"{agent_name}.agent")
    self.agents[agent_name] = module.root_agent
```

**4. Ready to Serve**:
```python
# Now self.agents contains:
{
    'greeting_agent': Agent(name="greeting_agent", ...),
    'news_pipeline': SequentialAgent(...),
    'competitive_analysis': SequentialAgent(...)
}
```

**5. Request Handling**:
```python
async def stream_chat(session_id, message, agent_name):
    adk_agent = self.agents[agent_name]  # Get agent object
    async for event in run_agent(adk_agent, ...):  # Execute
        yield chunk  # Stream back
```

**6. Cleanup** (FastAPI shutdown):
```python
await agent_manager.cleanup()
```

---

### Memory and State Management

**Current**: In-memory sessions
```python
self.sessions: Dict[str, List] = {}
# session_id → conversation history
```

**Limitations**:
- Lost on restart
- Not shared across instances
- No persistence

**Production**:
Use Redis or database:
```python
import redis
r = redis.Redis(host='redis', port=6379)

def get_session(session_id):
    history = r.get(f"session:{session_id}")
    return json.loads(history) if history else []

def save_session(session_id, history):
    r.set(f"session:{session_id}", json.dumps(history), ex=3600)
```

---

## 🎯 Quick Reference for Instructors

### File Locations Cheat Sheet

| What | Where | When to Edit |
|------|-------|--------------|
| Agent definitions | `adk_agents/{name}/agent.py` | Always (this is where agents live) |
| Custom tools | `adk_agents/{name}/tools.py` | When agent needs custom Python functions |
| Auto-discovery logic | `agents/manager.py` | Rarely (only to change discovery rules) |
| WebSocket endpoint | `api/main.py` | Rarely (works for all agents) |
| REST endpoints | `api/routes/agents.py` | When adding new API features |
| Generic frontend | `frontend/index.html` | When improving shared UI |
| Streamlit apps | `streamlit_apps/{name}/app.py` | For custom agent dashboards |

**90% of time**: Only edit files in `adk_agents/`!

---

## ✅ Workshop Learning Objectives Met

**Students learn**:
1. ✅ How to define ADK agents
2. ✅ How to create custom tools
3. ✅ How ADK integrates with FastAPI
4. ✅ Why auto-discovery is better than manual registration
5. ✅ How one agent works in multiple interfaces
6. ✅ How to build custom UIs (Streamlit)
7. ✅ Production-ready patterns

**Instructors can teach**:
1. ✅ Live demo: Create agent, auto-discovered
2. ✅ Show tool calling in both UIs
3. ✅ Explain wrapper benefits
4. ✅ Students create their own agent
5. ✅ (Advanced) Students build Streamlit UI

---

**This architecture supports the full workshop journey from basics to production!** 🚀