# 🧪 ADK Web Testing Guide

> **Status**: All services running! Ready to test
> **Date**: October 30, 2025

---

## ✅ Services Status

All containers are UP and healthy:

```bash
✓ adk-workshop-adk-web    (Port 3002) - ADK Web Interface
✓ adk-workshop-api        (Port 8000) - FastAPI Backend
✓ adk-workshop-frontend   (Port 80)   - Custom Chat UI
✓ adk-workshop-redis      (Port 6379) - Session Storage
```

---

## 🌐 Access URLs

| Service | Direct URL | Proxied URL | Purpose |
|---------|-----------|-------------|---------|
| **Custom Frontend** | http://localhost | - | Beautiful chat UI |
| **ADK Web** | http://localhost:3002 | http://localhost/adk | Developer debugging |
| **FastAPI Docs** | http://localhost:8000/docs | http://localhost/docs | API documentation |
| **Health Check** | http://localhost:8000/api/health | http://localhost/api/health | Service status |

---

## 🧪 Test Scenarios

### Test 1: Verify ADK Web Loads

1. **Open**: http://localhost:3002
2. **Expected**: ADK Web interface loads with:
   - "greeting_agent" in agent selector
   - Tabs: Messages, Events, State, Artifacts, Sessions
   - Chat input box at bottom

✅ **Pass**: Interface loads
❌ **Fail**: Check logs with `docker compose logs adk-web`

---

### Test 2: Send a Message

1. **In ADK Web**, type: "Hello! I'm testing the ADK workshop"
2. **Click Send**
3. **Expected**:
   - Response appears (may take 2-3 seconds)
   - Agent greets you and asks for your name

✅ **Pass**: Agent responds appropriately
❌ **Fail**: Check for 401 errors (API key issue)

---

### Test 3: Inspect Events

1. **Click "Events" tab** (top of interface)
2. **Expected to see**:
   - Multiple event cards in timeline
   - `agent_start` event
   - `agent_response` event
   - `agent_end` event

3. **Click on an event to expand**
4. **Expected**:
   - Request section showing:
     - instructions
     - message
     - model
   - Response section showing:
     - generated text
     - metadata

✅ **Pass**: Events show detailed information
❌ **Fail**: Events empty (WebSocket issue)

---

### Test 4: Compare Both Interfaces

**Test both UIs work with same backend**:

1. **Open Custom UI**: http://localhost
   - Send: "Hi from custom UI"
   - Note the response

2. **Open ADK Web**: http://localhost:3002
   - Send: "Hi from ADK web"
   - Note the response

3. **Expected**: Both work independently with streaming responses

✅ **Pass**: Both interfaces work
❌ **Fail**: One interface not responding

---

### Test 5: Proxied Access (NGINX)

1. **Open**: http://localhost/adk (note: no port)
2. **Expected**: ADK Web loads through NGINX proxy
3. **Send message**: "Testing proxy"
4. **Expected**: Works same as direct access

✅ **Pass**: Proxy works correctly
❌ **Fail**: 502 Bad Gateway (NGINX config issue)

---

## 🎓 Workshop Demonstration Flow

### Demo Script for Attendees

#### Part 1: The Magic (2 min)

**Show Custom UI**:
```
1. Open http://localhost
2. "Look at this beautiful chatbot we've built"
3. Send: "Explain what an AI agent is in one sentence"
4. "Notice how it streams word-by-word - great UX!"
```

---

#### Part 2: Under the Hood (5 min)

**Switch to ADK Web**:
```
1. Open http://localhost:3002
2. "Now let's see what's actually happening..."
3. Send same message: "Explain what an AI agent is in one sentence"
4. Click Events tab
5. Walk through each event:

   EVENT 1: agent_start
   - "The agent receives your message"
   - Expand: Show instructions passed to model
   - Show message in conversation history

   EVENT 2: agent_response
   - "The LLM generates a response"
   - Expand: Show full response text
   - Show metadata (model used, timing, etc.)

   EVENT 3: agent_end
   - "Processing complete!"
```

---

#### Part 3: Deep Dive (3 min)

**Explore the Interface**:
```
1. State Tab:
   - "This is where agents store memory"
   - Currently empty (will use later)

2. Sessions Tab:
   - "Each conversation gets a unique session"
   - Can create multiple sessions
   - Isolate different conversations

3. Events Details:
   - "Every interaction is logged"
   - Perfect for debugging
   - See exact LLM inputs/outputs
```

---

## 🐛 Known Issues & Solutions

### Issue 1: "greeting_agent not found"

**Cause**: Agent structure incorrect

**Check**:
```bash
# Verify structure
ls adk_agents/greeting_agent/

# Should have:
# - __init__.py
# - agent.py
# - .env
```

**Fix**: Ensure folder name matches agent name in `agent.py`

---

### Issue 2: 401 Unauthorized

**Cause**: API key not set or invalid

**Check**:
```bash
# View ADK agent .env
cat adk_agents/greeting_agent/.env

# Should show your API key
```

**Fix**:
```bash
# Re-sync API key
./scripts/sync-env.sh

# Restart
docker compose restart adk-web
```

---

### Issue 3: Events Not Appearing

**Cause**: WebSocket connection issue

**Fix**:
1. Hard refresh browser: Cmd+Shift+R (Mac) or Ctrl+Shift+R (Windows)
2. Check browser console for errors
3. Verify WebSocket connection in DevTools → Network → WS

---

### Issue 4: Slow Response Times

**Cause**: Cold start or network latency

**Normal**:
- First message: 2-5 seconds (model warming up)
- Subsequent messages: 1-2 seconds

**If consistently slow** (>10 seconds):
- Check network connection
- Verify API key has quota
- Check `docker compose logs adk-web` for errors

---

## 📊 Success Criteria

### ✅ All Systems Go When:

- [ ] ADK Web loads at http://localhost:3002
- [ ] Can send message and get response
- [ ] Events tab shows agent lifecycle
- [ ] Can expand events to see details
- [ ] NGINX proxy works at http://localhost/adk
- [ ] Custom UI still works at http://localhost
- [ ] No errors in `docker compose logs`

---

## 🎯 Next Steps for Workshop

### 1. Add Custom Tools (Module 2)

Create `/adk_agents/greeting_agent/tools.py`:

```python
from datetime import datetime

def get_workshop_info() -> dict:
    """Get information about the ADK workshop.

    Returns:
        dict: Workshop details
    """
    return {
        "name": "Google ADK Workshop",
        "location": "DevFest Atlanta",
        "date": "October 30, 2025",
        "duration": "2 hours",
        "focus": "Building AI Agents with Google ADK"
    }
```

Then update `agent.py`:
```python
from .tools import get_workshop_info

agent = Agent(
    name="greeting_agent",
    tools=[get_workshop_info],
    instructions="Use get_workshop_info when asked about the workshop."
)
```

**Demo in ADK Web**: Events will show tool_call and tool_result!

---

### 2. Add Multi-Agent System (Module 3)

Create more agents:
- `/adk_agents/researcher_agent/`
- `/adk_agents/writer_agent/`
- `/adk_agents/router_agent/`

**Demo**: Show agents calling each other in Events timeline!

---

### 3. Update Slides

Add to presentation:
- Screenshot of ADK Web Events tab
- Live demo switching between UIs
- Debugging exercise using Events

---

## 📸 Screenshots to Capture

For workshop slides:

1. **ADK Web Homepage**
   - Clean interface with agent selector
   - Tab bar visible
   - Chat input

2. **Events Tab with Timeline**
   - Multiple events visible
   - Event types labeled
   - Expand button visible

3. **Expanded Event Detail**
   - Request section with instructions
   - Response section with generated text
   - Metadata visible

4. **Tool Call Event** (after adding tools)
   - tool_call event
   - Parameters shown
   - tool_result event
   - Result data visible

---

## 🎉 Success!

You now have:

✅ **Dual Interface Architecture**
- Custom UI for user experience
- ADK Web for developer insight

✅ **Professional Teaching Setup**
- Show the magic (Custom UI)
- Explain the magic (ADK Web)
- Debug in real-time (Events tab)

✅ **Google-Native Tooling**
- Official ADK web interface
- Perfect for DevFest
- Showcases Google's ecosystem

---

**Ready to demo!** Open both interfaces side-by-side and start exploring! 🚀

---

**Created**: October 30, 2025
**Tested**: All services verified working
**Contact**: Workshop instructor
