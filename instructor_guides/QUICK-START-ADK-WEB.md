# ⚡ Quick Start: ADK Web Interface

> **You're almost there!** The agent is loaded and ready.

---

## ✅ Current Status

**All services running**:
- ✅ ADK Web Server: http://localhost:3002
- ✅ Custom Frontend: http://localhost
- ✅ FastAPI Backend: http://localhost:8000
- ✅ greeting_agent: Loaded and ready

---

## 🎯 Next Steps

### 1. Refresh Your Browser

**Hard refresh** the ADK Web page:
- **Mac**: Cmd + Shift + R
- **Windows**: Ctrl + Shift + R

### 2. Select the Agent

You should now see **"greeting_agent"** in the dropdown at the top left:

```
Select an agent ▼  →  greeting_agent ✓
```

If not visible:
- Check dropdown is expanded
- Refresh page again
- Check logs: `docker compose logs adk-web`

### 3. Test the Agent

**Send a message**:
```
Hello! I'm testing the ADK workshop setup.
```

**Expected response**:
```
Hi! Welcome to the ADK Workshop! I'm here to help you learn
about Google's Agent Development Kit. To make this more personal,
what's your name?
```

### 4. Explore Events

1. **Click "Events" tab** (top of interface)
2. **You should see**:
   - Event 1: `agent_start`
   - Event 2: `agent_response`
   - Event 3: `agent_end`

3. **Click on any event** to expand
4. **Inspect**:
   - Request: Instructions, message, model
   - Response: Generated text, metadata

---

## 🎓 For Workshop Teaching

### Demo Flow

**1. Show Both Interfaces** (Side by side):
- Left screen: http://localhost (Custom UI)
- Right screen: http://localhost:3002 (ADK Web)

**2. Send Same Message to Both**:
```
"Explain what Google ADK is in one sentence"
```

**3. Compare**:
- Custom UI: Beautiful streaming experience
- ADK Web: Events timeline showing what happened

**4. Deep Dive in ADK Web**:
- Events tab → Walk through each event
- Show request structure
- Show response generation
- Explain agent lifecycle

---

## 🐛 Still Having Issues?

### Agent Not in Dropdown

**Check agent discovery**:
```bash
# See if agent is loaded
docker compose logs adk-web | grep "greeting_agent"

# Should see: /apps/greeting_agent/ endpoints
```

**Verify structure**:
```bash
docker compose exec adk-web ls -la /app/adk_agents/greeting_agent/

# Must have:
# - __init__.py
# - agent.py
# - .env
```

### 401 Unauthorized Error

**Check API key**:
```bash
# View agent's .env
docker compose exec adk-web cat /app/adk_agents/greeting_agent/.env

# Should show: GOOGLE_API_KEY=AIza...
```

**Re-sync if needed**:
```bash
./scripts/sync-env.sh
docker compose restart adk-web
```

### Events Tab Empty

**Cause**: Need to send a message first

**Solution**:
1. Send any message in Messages tab
2. Switch to Events tab
3. Events should now appear

---

## 📊 What Success Looks Like

```
✓ ADK Web Interface loads
✓ "greeting_agent" appears in dropdown
✓ Can select greeting_agent
✓ Can send messages and get responses
✓ Events tab shows agent lifecycle
✓ Can expand events to see details
✓ State tab accessible (empty for now)
✓ Sessions tab shows current session
```

---

## 🎉 You're All Set!

**Three working interfaces**:
1. Custom Chat UI - http://localhost
2. ADK Web (proxy) - http://localhost/adk
3. ADK Web (direct) - http://localhost:3002

**Perfect for workshop demonstrations!**

Try them all and see how they work together! 🚀

---

**Last Updated**: October 30, 2025
