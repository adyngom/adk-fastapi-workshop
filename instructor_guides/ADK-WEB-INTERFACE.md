# 🔍 ADK Web Interface Guide

> **Purpose**: Learn how to use Google's ADK Web Interface for debugging, monitoring, and understanding your AI agents.

---

## 🎯 What is ADK Web?

**ADK Web** is Google's official developer interface for the Agent Development Kit. It provides:

- **Real-time event viewer** - See every step your agent takes
- **State inspector** - Examine agent memory and context
- **Session management** - Handle multiple conversations
- **Tool call visualization** - Watch function calls in action
- **Request/Response debugging** - Inspect LLM interactions

---

## 🌐 Accessing ADK Web

### In This Workshop

We run **two interfaces side-by-side**:

| Interface | URL | Purpose |
|-----------|-----|---------|
| **Custom Frontend** | http://localhost | Beautiful user experience |
| **ADK Web** | http://localhost/adk | Developer debugging view |

**Or access directly**:
- ADK Web: http://localhost:3002

---

## 🚀 Getting Started

### 1. Start All Services

```bash
# Make sure your .env file has GOOGLE_API_KEY set
docker compose up -d
```

### 2. Verify ADK Web is Running

```bash
# Check container status
docker compose ps adk-web

# Should show: "Up" status on port 3002
```

### 3. Open ADK Web Interface

Navigate to: **http://localhost/adk** or **http://localhost:3002**

---

## 🎨 Interface Overview

### Main Components

```
┌─────────────────────────────────────────────────────┐
│  ADK Web Interface                                   │
├──────────────┬──────────────────────────────────────┤
│  Agent       │  greeting_agent ▼                     │
│  Selector    │                                       │
├──────────────┼──────────────────────────────────────┤
│              │                                       │
│  Tab Bar     │  [Messages] [Events] [State]         │
│              │  [Artifacts] [Sessions]               │
│              │                                       │
├──────────────┴──────────────────────────────────────┤
│                                                      │
│  Chat Area                                           │
│  - User messages                                     │
│  - Agent responses                                   │
│  - Tool calls                                        │
│                                                      │
├──────────────────────────────────────────────────────┤
│  Input Box: Type your message here...        [Send] │
└──────────────────────────────────────────────────────┘
```

---

## 📊 Key Features

### 1. **Messages Tab** - Chat View

**What it shows**: The conversation between you and the agent

**Use it for**:
- Testing agent responses
- Verifying instructions are followed
- Seeing streaming responses

**Example**:
```
You: Hello! What's your name?
Agent: Hi! I'm the greeting agent. What's your name?
```

---

### 2. **Events Tab** - The Magic Happens Here! ✨

**What it shows**: Every step the agent takes, in order

**Event Types**:
- `agent_start` - Agent begins processing
- `tool_call` - Agent wants to use a tool
- `tool_result` - Tool returns data
- `agent_response` - Agent generates response
- `agent_end` - Processing complete

**Example Event**:
```json
{
  "event_type": "agent_response",
  "timestamp": "2025-10-30T13:00:00Z",
  "agent": "greeting_agent",
  "request": {
    "instructions": "You are a helpful assistant...",
    "message": "Hello!"
  },
  "response": {
    "text": "Hi! I'm the greeting agent. What's your name?"
  }
}
```

**Pro Tip**: Click on any event to expand and see full details!

---

### 3. **State Tab** - Agent Memory

**What it shows**: Data the agent stores between messages

**Use cases**:
- Check conversation history
- Verify memory persistence
- Debug state issues

**Example State**:
```json
{
  "user_name": "Sarah",
  "conversation_started": "2025-10-30T13:00:00Z",
  "messages_count": 5
}
```

---

### 4. **Sessions Tab** - Conversation Management

**What it shows**: All active and past sessions

**Features**:
- Create new session (fresh start)
- Switch between sessions
- View session history
- Delete old sessions

**Session ID Format**: `session_1730304000000`

---

### 5. **Artifacts Tab** - Generated Content

**What it shows**: Files, images, or documents created by agents

**Use cases**:
- View generated code
- Download agent outputs
- Inspect multi-modal content

*(Advanced feature - used with file-generating agents)*

---

## 🔍 Debugging Workflows

### Scenario 1: Agent Not Following Instructions

**Problem**: Agent gives wrong type of response

**Debug Steps**:
1. Go to **Events** tab
2. Find the `agent_response` event
3. Click to expand
4. Check `request.instructions` field
5. Verify instructions are correct

**What to look for**:
- Are instructions being passed correctly?
- Is the model parameter correct?
- Are there conflicting instructions?

---

### Scenario 2: Tool Call Not Working

**Problem**: Agent doesn't use your custom tool

**Debug Steps**:
1. Send a message that should trigger the tool
2. Go to **Events** tab
3. Look for `tool_call` event
4. If missing: Agent didn't recognize when to use tool
5. If present: Check `tool_result` for errors

**Common Issues**:
- Tool description not clear enough
- Tool not registered in agent
- Tool function has errors

**Example Event Sequence**:
```
1. agent_start
2. tool_call: get_weather(city="Atlanta")
3. tool_result: {"temperature": 75, "conditions": "sunny"}
4. agent_response: "It's 75°F and sunny in Atlanta!"
5. agent_end
```

---

### Scenario 3: Slow Responses

**Problem**: Agent takes too long to respond

**Debug Steps**:
1. Go to **Events** tab
2. Check timestamps between events
3. Identify which step is slow

**Common Bottlenecks**:
- Tool execution time (external API calls)
- Large context windows (too much history)
- Complex instructions (LLM processing time)

**Example Analysis**:
```
12:00:00.100 - agent_start
12:00:00.150 - tool_call (50ms) ✅ Fast
12:00:05.000 - tool_result (4850ms) ⚠️  SLOW!
12:00:05.500 - agent_response (500ms) ✅ Fast
```

---

## 🎓 Workshop Teaching Uses

### For Instructors

#### Show & Tell Flow:

1. **Start with Custom UI** (http://localhost)
   - Show the "magic" - beautiful streaming chat
   - Attendees see the end result first
   - "Wow" moment

2. **Switch to ADK Web** (http://localhost/adk)
   - "Now let's look under the hood..."
   - Open Events tab
   - Walk through each event step-by-step
   - Show request/response structure

3. **Deep Dive**
   - Show how instructions are passed
   - Demonstrate tool calling
   - Inspect state changes
   - Compare different agent responses

---

### Teaching Examples

#### Example 1: Basic Agent Flow

**Script**:
1. Open Custom UI, send "Hello!"
2. Show streaming response
3. Switch to ADK Web → Events tab
4. Walk through: "Here's what actually happened..."
   - Agent received message
   - Checked instructions
   - Generated response
   - Streamed back to UI

---

#### Example 2: Tool Calling

**Script**:
1. "Let's give our agent a calculator tool"
2. Send: "What's 23 * 47?"
3. Watch Custom UI for response
4. Switch to ADK Web → Events
5. Show tool_call event: `calculator(23, 47)`
6. Show tool_result event: `1081`
7. Show agent incorporating result into response

---

#### Example 3: Multi-Agent Debugging

**Script**:
1. "We have 3 agents working together"
2. Show message flow in Events tab
3. "Agent 1 calls Agent 2 as a tool"
4. "Agent 2 returns data to Agent 1"
5. "Agent 1 synthesizes final answer"

---

## 🛠️ Advanced Features

### Custom Agent Configuration

Edit `/adk_agents/greeting_agent/agent.py`:

```python
agent = Agent(
    name="greeting_agent",  # Must match folder name!
    model="gemini-2.0-flash-exp",
    description="A friendly workshop assistant",
    instructions="""
    You are a helpful assistant for the ADK Workshop.
    - Greet users warmly
    - Ask for their name
    - Be enthusiastic about ADK!
    """
)
```

**Hot Reload**: Restart ADK web to see changes
```bash
docker compose restart adk-web
```

---

### Adding Custom Tools

Create `/adk_agents/greeting_agent/tools.py`:

```python
def get_current_time() -> dict:
    """Get the current time in Atlanta.

    Returns:
        dict: Current time information
    """
    import datetime
    now = datetime.datetime.now()
    return {
        "current_time": now.strftime("%I:%M %p"),
        "timezone": "EST"
    }
```

Then add to agent:

```python
from .tools import get_current_time

agent = Agent(
    name="greeting_agent",
    model="gemini-2.0-flash-exp",
    tools=[get_current_time],
    instructions="Use get_current_time when asked about the time."
)
```

---

## 🐛 Troubleshooting

### ADK Web Won't Start

**Symptom**: Container keeps restarting

**Check**:
```bash
docker compose logs adk-web
```

**Common Causes**:
1. **Missing API key**
   - Check `.env` has `GOOGLE_API_KEY`
   - Run `./scripts/sync-env.sh`

2. **Invalid agent structure**
   - Ensure folder name matches agent name
   - Check `__init__.py` imports agent

3. **Port conflict**
   - Another service using port 3002
   - Change port in `docker-compose.yml`

---

### Can't See Events

**Symptom**: Events tab is empty

**Solutions**:
1. Refresh the page
2. Send a message to trigger events
3. Check browser console for errors
4. Verify WebSocket connection

---

### Tool Calls Not Showing

**Symptom**: Tool calls don't appear in Events

**Checklist**:
- [ ] Tool is registered in agent's `tools=[]` list
- [ ] Tool has proper docstring
- [ ] Tool has return type annotation
- [ ] Agent instructions mention when to use tool

---

## 📚 Comparison: Custom UI vs ADK Web

| Feature | Custom UI | ADK Web | Best For |
|---------|-----------|---------|----------|
| **User Experience** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | End users |
| **Debugging** | ⭐⭐ | ⭐⭐⭐⭐⭐ | Developers |
| **Event Inspection** | ❌ | ✅ | Teaching |
| **State Viewing** | ❌ | ✅ | Debugging |
| **Tool Visualization** | ❌ | ✅ | Understanding |
| **Session Management** | ⭐⭐ | ⭐⭐⭐⭐⭐ | Testing |
| **Production Ready** | ✅ | ❌ | Deployment |

---

## 🎯 Workshop Integration

### Slide 8: Exercise 1 - Your First Agent

**Add this section**:

```markdown
### Exploring Your Agent with ADK Web

1. Open http://localhost/adk
2. Send message: "Hello! I'm [your name]"
3. Click **Events** tab
4. Observe the agent lifecycle:
   - agent_start
   - agent_response
   - agent_end
5. Click each event to see request/response

**Discussion**:
- What information is in the instructions?
- How does the agent maintain context?
- Where is the model specified?
```

---

### Slide 13: Exercise 2 - Multi-Agent System

**Add debugging walkthrough**:

```markdown
### Debugging Multi-Agent Communication

1. Send complex task requiring multiple agents
2. Open ADK Web → Events tab
3. Follow the agent chain:
   ```
   Router Agent → Researcher Agent
   Researcher Agent → Writer Agent
   Writer Agent → Router Agent
   ```
4. Expand each event to see:
   - Which agent handled each step
   - What data was passed between agents
   - How long each agent took

**Challenge**: Find where Agent A calls Agent B as a tool
```

---

## 📖 Further Reading

### Official Documentation
- [ADK Documentation](https://cloud.google.com/vertex-ai/docs/adk)
- [ADK Samples Repository](https://github.com/google/adk-samples)
- [Gemini API Docs](https://ai.google.dev/gemini-api/docs)

### Video Resources
- [ADK Masterclass](https://www.youtube.com/watch?v=P4VFL9nIaIA)
- Google Cloud Next sessions on ADK

---

## ✅ Quick Reference

### Common Commands

```bash
# Start ADK web
docker compose up -d adk-web

# View logs
docker compose logs -f adk-web

# Restart after changes
docker compose restart adk-web

# Stop ADK web
docker compose stop adk-web

# Rebuild after major changes
docker compose build adk-web
docker compose up -d adk-web
```

### URLs Cheat Sheet

- Custom Frontend: http://localhost
- ADK Web (via proxy): http://localhost/adk
- ADK Web (direct): http://localhost:3002
- FastAPI Docs: http://localhost:8000/docs
- API Health: http://localhost:8000/api/health

---

## 🎉 Next Steps

Now that you understand ADK Web:

1. **Experiment**: Try different instructions and see Events change
2. **Add Tools**: Create custom tools and watch them execute
3. **Build Multi-Agent**: See agent collaboration in real-time
4. **Debug Issues**: Use Events tab to troubleshoot problems

**Remember**: ADK Web is your X-ray vision into agent behavior!

---

**Last Updated**: October 30, 2025
**For Workshop**: Google DevFest ADK Workshop
