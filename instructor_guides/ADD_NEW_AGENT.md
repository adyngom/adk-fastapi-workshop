# How to Add a New Agent - Step by Step

**Goal**: Understand the repeatable pattern for adding agents to the workshop

---

## 🎯 The Simple Pattern

### Before Auto-Discovery (OLD - Don't do this):
1. Create agent files
2. **Manually edit `agents/manager.py`** to add agent
3. Restart services
4. Manually update frontend dropdown

### After Auto-Discovery (NEW - Current):
1. Create agent files
2. ~~Edit manager.py~~ **← AUTOMATIC**
3. Restart services
4. ~~Update dropdown~~ **← AUTOMATIC**

**One directory = One agent. That's it!**

---

## 📋 Complete Checklist

### Step 1: Create Agent Directory

```bash
cd adk_agents/
mkdir my_new_agent
cd my_new_agent
```

**Convention**: Use lowercase with underscores (snake_case)

---

### Step 2: Create `agent.py` File

**File**: `adk_agents/my_new_agent/agent.py`

```python
"""
My New Agent - Description of what it does
"""
from google.adk.agents import Agent
from .tools import my_tool_function  # Optional: if you have custom tools

# REQUIRED: Must be named root_agent for discovery
root_agent = Agent(
    name="my_new_agent",
    model="gemini-2.0-flash-exp",
    description="Brief description shown in agent list",
    instruction="""You are an agent that does X.

    Your responsibilities:
    1. Do something specific
    2. Use tools when needed
    3. Return structured responses

    Always be helpful and accurate.
    """,
    tools=[my_tool_function]  # Optional: List of Python functions
)
```

**Required Elements**:
- ✅ Must export variable named `root_agent`
- ✅ Can be `Agent`, `SequentialAgent`, or `ParallelAgent`
- ✅ Must have `name` parameter
- ✅ Must have `instruction` parameter (what the agent does)

---

### Step 3: Create Tools (Optional)

**File**: `adk_agents/my_new_agent/tools.py`

```python
"""
Custom tools for my_new_agent
"""

def my_tool_function(param1: str, param2: int = 10) -> dict:
    """Brief description of what this tool does.

    The docstring is read by the LLM to understand when to use the tool.
    Be clear and specific!

    Args:
        param1: Description of first parameter
        param2: Description of second parameter (optional)

    Returns:
        dict: Description of what's returned
    """
    # Your implementation
    result = do_something(param1, param2)

    return {
        "result": result,
        "param1_used": param1,
        "param2_used": param2
    }


def another_tool() -> str:
    """Another tool example - returns string instead of dict"""
    return "Simple string result"
```

**Tool Requirements**:
- ✅ Must have good docstring (LLM reads this!)
- ✅ Type hints help but aren't required
- ✅ Can return dict, str, int, list, etc.
- ✅ Synchronous functions only (ADK handles async)

---

### Step 4: Restart Services

```bash
# Docker:
docker compose restart api adk-web

# IDX:
pkill -f uvicorn && pkill -f "adk web"
./.idx/start-services.sh
```

**That's it!** No code changes to manager.py needed.

---

### Step 5: Verify Agent Loaded

**Check logs**:
```bash
# Docker
docker compose logs api | grep "Discovered"

# Should show:
# Discovered 4 agents: ['competitive_analysis', 'greeting_agent', 'my_new_agent', 'news_pipeline']
```

**Check API**:
```bash
curl http://localhost:8000/api/agents/list | jq
```

**Check frontends**:
- Custom UI dropdown should show "My New Agent"
- ADK Web selector should show "my_new_agent"

---

## 📁 Complete Example: Weather Agent

### Directory Structure
```
adk_agents/
  └── weather_agent/
       ├── agent.py
       └── tools.py
```

### `agent.py`
```python
"""
Weather Agent - Provides weather information
"""
from google.adk.agents import Agent
from .tools import get_weather, get_forecast

root_agent = Agent(
    name="weather_agent",
    model="gemini-2.0-flash-exp",
    description="Provides current weather and forecasts",
    instruction="""You are a helpful weather assistant.

    When users ask about weather:
    1. Ask for location if not provided
    2. Use get_weather() for current conditions
    3. Use get_forecast() for future predictions
    4. Present information clearly with temperature, conditions, and recommendations

    Always mention the location you're providing weather for.
    """,
    tools=[get_weather, get_forecast]
)
```

### `tools.py`
```python
"""
Weather tools - Mock implementation for demo
Production would call real weather API
"""

def get_weather(location: str) -> dict:
    """Get current weather for a location.

    Args:
        location: City name or zip code

    Returns:
        dict: Current weather conditions
    """
    # Mock implementation
    return {
        "location": location,
        "temperature": 72,
        "conditions": "Partly cloudy",
        "humidity": 65,
        "wind_speed": 8,
        "feels_like": 70,
        "last_updated": "2025-11-03 15:00:00"
    }


def get_forecast(location: str, days: int = 3) -> dict:
    """Get weather forecast for a location.

    Args:
        location: City name or zip code
        days: Number of days to forecast (1-7)

    Returns:
        dict: Multi-day forecast
    """
    # Mock implementation
    return {
        "location": location,
        "forecast": [
            {"date": "2025-11-04", "high": 75, "low": 55, "conditions": "Sunny"},
            {"date": "2025-11-05", "high": 68, "low": 50, "conditions": "Rainy"},
            {"date": "2025-11-06", "high": 70, "low": 52, "conditions": "Cloudy"}
        ]
    }
```

### Test It

```bash
# Restart services
docker compose restart api adk-web

# Test in custom UI: http://localhost
# Select "Weather Agent"
# Ask: "What's the weather in Atlanta?"

# Test in ADK Web: http://localhost:3002
# Select "weather_agent"
# Check Events tab to see tool calls
```

---

## 🔄 Multi-Agent Workflows

### Sequential Pipeline Example

**Directory**:
```
adk_agents/
  └── data_pipeline/
       ├── agent.py
       └── sub_agents/
            ├── extractor/
            │    └── agent.py
            ├── transformer/
            │    └── agent.py
            └── loader/
                 └── agent.py
```

**Main agent.py**:
```python
from google.adk.agents import SequentialAgent
from data_pipeline.sub_agents.extractor.agent import root_agent as extractor
from data_pipeline.sub_agents.transformer.agent import root_agent as transformer
from data_pipeline.sub_agents.loader.agent import root_agent as loader

root_agent = SequentialAgent(
    name="data_pipeline",
    description="ETL pipeline: extract, transform, load",
    sub_agents=[extractor, transformer, loader]
)
```

**Each sub-agent** is a regular `Agent(...)` with its own instruction and tools.

---

### Parallel Execution Example

**Main agent.py**:
```python
from google.adk.agents import ParallelAgent, SequentialAgent, Agent

# Three parallel researchers
researcher_a = Agent(name="researcher_a", instruction="Research topic A", ...)
researcher_b = Agent(name="researcher_b", instruction="Research topic B", ...)
researcher_c = Agent(name="researcher_c", instruction="Research topic C", ...)

# Parallel execution
parallel_research = ParallelAgent(
    name="parallel_research",
    sub_agents=[researcher_a, researcher_b, researcher_c]
)

# Synthesis agent
synthesizer = Agent(name="synthesizer", instruction="Combine results", ...)

# Root: Sequential (parallel then synthesize)
root_agent = SequentialAgent(
    name="research_workflow",
    description="Parallel research with synthesis",
    sub_agents=[parallel_research, synthesizer]
)
```

---

## 🧪 Testing Your New Agent

### 1. Check Discovery

```bash
# Check logs during startup
docker compose logs api | grep "Discovered"

# Expected:
# Discovered 4 agents: [..., 'my_new_agent', ...]
```

### 2. Check Loading

```bash
# Check if agent loaded without errors
docker compose logs api | grep "Loaded ADK agent: my_new_agent"

# If you see errors, check:
# - Does agent.py exist?
# - Does it export root_agent?
# - Are imports correct?
```

### 3. Test in ADK Web

http://localhost:3002
- Select your agent from dropdown
- Send test message
- Check Events tab for tool calls
- Verify response makes sense

### 4. Test in Custom UI

http://localhost
- Select your agent
- Send test message
- Verify streaming works
- Check markdown rendering

### 5. Test via API

```bash
curl http://localhost:8000/api/agents/list | jq
# Should include your agent

# Or visit:
http://localhost:8000/docs
# Try the /api/agents/list endpoint
```

---

## 🚫 Common Mistakes

### Mistake 1: Wrong Variable Name
❌ `agent = Agent(...)`
✅ `root_agent = Agent(...)`

**Why**: Auto-discovery looks for `root_agent`

---

### Mistake 2: Circular Imports
❌ Importing from `api/` or `agents/` in agent files

**Why**: ADK agents should be self-contained

**Solution**: Keep tools in same directory as agent

---

### Mistake 3: Missing __init__.py
If you have sub_agents/ folder, you need:
```
sub_agents/
  ├── __init__.py  ← Don't forget!
  └── my_sub/
       └── agent.py
```

---

### Mistake 4: Forgetting to Restart
**Agent changes require restart**:
- Code changes: Restart API and ADK Web
- New agents: Restart both
- Tool changes: Restart both

---

## 📊 Agent Patterns Comparison

| Pattern | When to Use | Example |
|---------|-------------|---------|
| **Single Agent + Tools** | Simple tasks, custom functions | greeting_agent, weather_agent |
| **Sequential Pipeline** | Ordered steps, state passing | news_pipeline, ETL, data processing |
| **Parallel + Synthesis** | Independent research, speed optimization | competitive_analysis, multi-source research |

---

## 🎨 Optional: Custom Frontend (Future)

**Current**: One generic chat UI for all agents

**Future**: Per-agent custom frontends
```
frontends/
  ├── default/           # Generic chat (current)
  ├── weather_agent/     # Custom: Weather cards, icons
  └── data_pipeline/     # Custom: Progress bars, data viz
```

**See**: `docs/PER_AGENT_FRONTENDS.md` (coming soon)

---

## 🔄 Streamlit Integration (Future)

**Current**: Vanilla JS frontend

**Future**: Streamlit dashboard per agent
```
streamlit_apps/
  └── news_dashboard/
       ├── app.py         # Streamlit code
       ├── requirements.txt
       └── api_client.py  # Connects to FastAPI
```

**See**: `docs/STREAMLIT_INTEGRATION.md` (next)

---

## ✅ Success Checklist

When adding a new agent, verify:

- [ ] Directory created in `adk_agents/`
- [ ] `agent.py` exists with `root_agent` variable
- [ ] Tools (if any) in `tools.py`
- [ ] Restart shows agent discovered in logs
- [ ] Agent appears in both UI dropdowns
- [ ] Agent responds to test messages
- [ ] Tools execute correctly (check ADK Web Events)
- [ ] Works in both Custom UI and ADK Web

---

## 🚀 Next Steps

**You now understand**:
- ✅ How to create ADK agents
- ✅ How they're discovered automatically
- ✅ How they integrate with FastAPI
- ✅ How to test them

**Coming next**:
- Custom frontends per agent
- Streamlit integration
- Production patterns (auth, rate limiting, etc.)

---

**Time to add an agent**: 5-10 minutes (mostly writing the instruction!)
**No code changes needed** in FastAPI layer - just add to `adk_agents/`!
