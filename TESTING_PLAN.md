# Complete Testing Plan - Local Docker & IDX

**Goal**: Validate all improvements work in both environments before workshop

---

## 🐳 Part 1: Local Docker Testing

### Test 1: Clean Build

```bash
# Clean everything
docker compose down -v
docker system prune -f

# Fresh build
docker compose up -d --build

# Wait for services to start
sleep 10

# Check all containers running
docker compose ps
```

**Expected**:
- ✅ 4 containers: api, adk-web, frontend, redis (all "Up")
- ✅ All health checks passing

---

### Test 2: Auto-Discovery Verification

```bash
# Check discovery logs
docker compose logs api | grep "Discovered"

# Should show:
# Discovered 3 agents: ['competitive_analysis', 'greeting_agent', 'news_pipeline']
```

**Expected**:
- ✅ Shows exact agent count
- ✅ Lists all 3 agents alphabetically
- ✅ No errors in logs

---

### Test 3: Agent List API

```bash
# Test the endpoint
curl -s http://localhost:8000/api/agents/list | jq

# Should return JSON array with 3 agents
```

**Expected output**:
```json
[
  {
    "name": "competitive_analysis",
    "description": "Parallel competitive research with synthesis",
    "capabilities": ["chat", "streaming"],
    "status": "active"
  },
  {
    "name": "greeting_agent",
    "description": "A friendly assistant that greets users...",
    "capabilities": ["chat", "streaming", "tools"],
    "status": "active"
  },
  {
    "name": "news_pipeline",
    "description": "Sequential news analysis...",
    "capabilities": ["chat", "streaming"],
    "status": "active"
  }
]
```

**Verify**:
- ✅ All 3 agents present
- ✅ greeting_agent shows "tools" in capabilities
- ✅ Descriptions match agent definitions

---

### Test 4: Custom Frontend - Tool Calling

**Steps**:
1. Open: http://localhost
2. Select: "Greeting Agent"
3. Send: "What time is it?"

**Expected**:
- ✅ Status shows "Connected" (green)
- ✅ Agent responds with current EST time
- ✅ Time is correct (not UTC)
- ✅ Response includes tool result data

**Also test**:
- "What are the workshop details?" → Should call get_workshop_info()
- "What agents are available?" → Should call list_available_agents()

---

### Test 5: ADK Web - Tool Calling

**Steps**:
1. Open: http://localhost:3002
2. Select: "greeting_agent" from dropdown
3. Send: "What time is it?"
4. Click "Events" tab

**Expected**:
- ✅ Shows tool call event: `get_current_time`
- ✅ Shows tool result with time data
- ✅ Response uses tool result
- ✅ Trace tab shows complete execution flow

---

### Test 6: API Documentation

**Steps**:
1. Open: http://localhost:8000/docs
2. Find: GET /api/agents/list
3. Click: "Try it out" → "Execute"

**Expected**:
- ✅ Returns 200 OK
- ✅ Response shows all 3 agents
- ✅ Swagger UI renders correctly

---

### Test 7: Streamlit Integration

```bash
# Start Streamlit (optional profile)
docker compose --profile streamlit up -d

# Wait for build
sleep 30

# Check it's running
docker compose ps streamlit-chat
```

**Then**:
1. Open: http://localhost:8501
2. Should see: "ADK Agent Chat" interface
3. Sidebar: Agent selector
4. Select: greeting_agent
5. Send: "Hello, what time is it?"

**Expected**:
- ✅ Streamlit UI loads
- ✅ Agent dropdown populated from API
- ✅ Shows agent description
- ✅ Chat works
- ✅ Response includes tool result
- ✅ Session persists across messages

---

### Test 8: Add New Agent (Live Test)

**Create a simple test agent**:

```bash
# Create directory
mkdir -p adk_agents/test_agent

# Create agent.py
cat > adk_agents/test_agent/agent.py << 'EOF'
from google.adk.agents import Agent

root_agent = Agent(
    name="test_agent",
    model="gemini-2.0-flash-exp",
    description="Simple test agent for validation",
    instruction="You are a helpful test agent. Just echo back what the user says."
)
EOF

# Restart services
docker compose restart api adk-web

# Check logs
docker compose logs api | grep "Discovered"
```

**Expected**:
- ✅ Shows 4 agents now (includes test_agent)
- ✅ http://localhost dropdown shows "test_agent"
- ✅ http://localhost:3002 selector shows "test_agent"
- ✅ curl http://localhost:8000/api/agents/list shows test_agent

**Test it works**:
- Send message in custom UI
- Should respond (echo behavior)

**Cleanup**:
```bash
rm -rf adk_agents/test_agent
docker compose restart api adk-web
# Back to 3 agents
```

---

### Local Testing Checklist Summary

- [ ] All containers start successfully
- [ ] Auto-discovery logs show 3 agents
- [ ] /api/agents/list returns 3 agents with correct metadata
- [ ] Custom frontend (localhost) connects via WebSocket
- [ ] Greeting agent uses get_current_time() tool correctly
- [ ] Time shows in EST (not UTC)
- [ ] ADK Web (localhost:3002) shows tool calls in Events tab
- [ ] API docs (localhost:8000/docs) accessible
- [ ] Streamlit (localhost:8501) loads and connects to backend
- [ ] Adding new agent: Auto-discovered without code changes
- [ ] Removing agent: Disappears from all interfaces

**If all ✅: Local baseline validated!**

---

## 🌐 Part 2: IDX Testing

### Prerequisites

Before testing in IDX:
- [ ] All local tests passed
- [ ] Latest changes pushed to main branch
- [ ] .env.template has all required variables

---

### Test 1: Fresh IDX Workspace

**Option A**: Open in IDX Button
1. Click: "Open in IDX" from README
2. Wait for onCreate (~90 seconds)
3. Check: Does .venv exist?
4. Check: Does .env exist?

**Option B**: Manual Clone (Recovery Path)
1. In IDX: `git clone https://github.com/adyngom/adk-fastapi-workshop.git`
2. Run: `./.idx/manual-setup.sh`
3. Should complete in ~2 minutes

**Expected**:
- ✅ .venv created
- ✅ Dependencies installed
- ✅ .env file exists
- ✅ Setup completes in < 5 minutes

---

### Test 2: Add API Key

```bash
# Edit .env file in IDX
# Add: GOOGLE_API_KEY=your_actual_key_here

# Verify
cat .env | grep GOOGLE_API_KEY
```

**Expected**:
- ✅ Key visible in .env
- ✅ Starts with "AIza"

---

### Test 3: Start Services

```bash
# Start all services
./.idx/start-services.sh

# Check output
# Should show PIDs for all 3 services
```

**Expected output**:
```
🚀 Starting ADK Workshop Services...
✅ Virtual environment activated
✅ API key configured
📦 Starting Redis...
🐍 Starting FastAPI backend on port 8000...
   FastAPI PID: XXXX
🔍 Starting ADK Web on port 3002...
   ADK Web PID: XXXX
🎨 Starting Frontend on port 8080...
   Frontend PID: XXXX
✅ All services started successfully!
```

---

### Test 4: Check Auto-Discovery in IDX

```bash
# Check if agents were discovered
tail -50 /tmp/api.log | grep "Discovered"
```

**Expected**:
- ✅ "Discovered 3 agents: ['competitive_analysis', 'greeting_agent', 'news_pipeline']"
- ✅ Each agent loaded successfully

---

### Test 5: Access Ports in IDX

**IDX shows port forwarding notifications**:
- Look for notifications: "Port 8080 available"
- Or check Ports panel (View → Ports)

**Get URLs**:
- Port 8080: `https://8080-firebase-adk-fastapi-workshop-XXXXX.cluster.idx.dev`
- Port 3002: `https://3002-firebase-adk-fastapi-workshop-XXXXX.cluster.idx.dev`
- Port 8000: `https://8000-firebase-adk-fastapi-workshop-XXXXX.cluster.idx.dev`

**Click each to verify**:
- [ ] Port 8080 opens custom chat UI
- [ ] Port 3002 opens ADK Web interface
- [ ] Port 8000 opens Swagger docs

---

### Test 6: Custom Frontend in IDX

**Steps**:
1. Open port 8080 URL
2. Should show: "ADK Workshop Chat"
3. Status should be: "Connected" (green)
4. Dropdown shows: 3 agents

**Test tool calling**:
1. Select: "Greeting Agent"
2. Send: "What time is it?"
3. Wait for response

**Expected**:
- ✅ Receives streaming response
- ✅ Shows EST time (correct timezone)
- ✅ Time is accurate
- ✅ Markdown renders properly

---

### Test 7: ADK Web in IDX

**Steps**:
1. Open port 3002 URL
2. Redirects to /dev-ui/ (correct)
3. Select: "greeting_agent"
4. Send: "What time is it?"
5. Check: Events tab

**Expected**:
- ✅ Shows tool call: get_current_time
- ✅ Shows tool result with data
- ✅ Response includes tool result
- ✅ Trace tab shows execution

---

### Test 8: Agent List API in IDX

```bash
# In IDX terminal, get your port 8000 URL
# Then test the endpoint

curl -s https://8000-YOUR-IDX-URL/api/agents/list | jq
```

**Or in browser**:
- Open: https://8000-YOUR-IDX-URL/api/agents/list

**Expected**:
- ✅ Returns JSON with 3 agents
- ✅ Each has name, description, capabilities, status

---

### Test 9: Add New Agent in IDX

**Live test of auto-discovery**:

```bash
# Create test agent
mkdir -p adk_agents/idx_test_agent

cat > adk_agents/idx_test_agent/agent.py << 'EOF'
from google.adk.agents import Agent

root_agent = Agent(
    name="idx_test_agent",
    model="gemini-2.0-flash-exp",
    description="Testing auto-discovery in IDX",
    instruction="You are a test agent. Just say 'Test successful!' to any message."
)
EOF

# Restart FastAPI
pkill -f uvicorn
source .venv/bin/activate
export PYTHONPATH=$(pwd):$PYTHONPATH
.venv/bin/uvicorn api.main:app --host 0.0.0.0 --port 8000 --reload > /tmp/api.log 2>&1 &

# Check discovery
sleep 3
tail -20 /tmp/api.log | grep "Discovered"
```

**Expected**:
- ✅ Shows 4 agents discovered
- ✅ Includes idx_test_agent
- ✅ Appears in frontend dropdown
- ✅ Works when tested

**Cleanup**:
```bash
rm -rf adk_agents/idx_test_agent
# Restart again, back to 3 agents
```

---

### IDX Testing Checklist Summary

- [ ] Fresh IDX workspace opens successfully
- [ ] Manual setup script works (if onCreate failed)
- [ ] .env created from template
- [ ] API key added
- [ ] All services start (FastAPI, ADK Web, Frontend)
- [ ] Port forwarding works for all 3 ports
- [ ] Custom UI (8080) connects via WebSocket
- [ ] Auto-discovery finds 3 agents
- [ ] /api/agents/list returns correct data
- [ ] Tool calling works (correct EST time)
- [ ] ADK Web shows tool execution in Events tab
- [ ] Adding new agent: Auto-discovered
- [ ] Setup time: < 5 minutes

**If all ✅: IDX setup validated!**

---

## 📊 Complete Testing Matrix

| Feature | Local Docker | IDX | Notes |
|---------|-------------|-----|-------|
| Clean build | ✅ Tested | ⏳ Pending | |
| Auto-discovery | ✅ Working | ⏳ Pending | Shows 3 agents |
| /api/agents/list | ✅ Working | ⏳ Pending | Returns metadata |
| Custom frontend | ✅ Working | ⏳ Pending | WebSocket connects |
| Tool calling | ✅ Working | ⏳ Pending | EST timezone correct |
| ADK Web | ✅ Working | ⏳ Pending | Events tab shows tools |
| Streamlit | 🔄 Optional | ❌ Skip | Not needed for workshop |
| Add new agent | ✅ Working | ⏳ Pending | Auto-discovered |
| Setup time | ~5 min | Target: <5 min | |

---

## 🚀 Quick Test Script (Copy-Paste)

### For Local Docker:

```bash
# === DOCKER QUICK TEST ===

echo "=== Test 1: Clean Build ==="
docker compose down -v
docker compose up -d --build
sleep 10
docker compose ps

echo ""
echo "=== Test 2: Auto-Discovery ==="
docker compose logs api | grep "Discovered"

echo ""
echo "=== Test 3: Agent List API ==="
curl -s http://localhost:8000/api/agents/list | jq '.[].name'

echo ""
echo "=== Test 4: Health Check ==="
curl -s http://localhost:8000/api/health | jq

echo ""
echo "Now open browser and test:"
echo "  - http://localhost (Custom UI - send 'What time is it?')"
echo "  - http://localhost:3002 (ADK Web - check Events tab)"
echo "  - http://localhost:8000/docs (API docs)"
echo ""
echo "Expected: Tools work, time is EST, all interfaces responsive"
```

---

### For IDX:

```bash
# === IDX QUICK TEST ===

echo "=== Test 1: Manual Setup ==="
./.idx/manual-setup.sh

echo ""
echo "=== Test 2: Add API Key ==="
echo "Edit .env and add your GOOGLE_API_KEY"
echo "Press Enter when done..."
read

echo ""
echo "=== Test 3: Start Services ==="
./.idx/start-services.sh

echo ""
echo "=== Test 4: Verify Auto-Discovery ==="
sleep 3
tail -30 /tmp/api.log | grep "Discovered"

echo ""
echo "=== Test 5: Check Services ==="
ps aux | grep -E "uvicorn|adk web|http.server" | grep -v grep

echo ""
echo "Now test in browser:"
echo "  1. Go to Ports panel (View → Ports)"
echo "  2. Open port 8080 (Custom UI)"
echo "  3. Send: 'What time is it?'"
echo "  4. Open port 3002 (ADK Web)"
echo "  5. Test same message, check Events tab"
echo ""
echo "Expected: Same results as local Docker"
```

---

## 🐛 Common Issues & Solutions

### Issue: Auto-discovery finds 0 agents

**Check**:
```bash
ls -la adk_agents/
# Should show 3 directories

ls adk_agents/greeting_agent/agent.py
# Should exist
```

**Fix**: Ensure directories exist and agent.py files present

---

### Issue: Tools not showing in capabilities

**Reason**: Agent doesn't have tools defined

**Check**:
```bash
grep "tools=" adk_agents/greeting_agent/agent.py
# Should show: tools=[get_workshop_info, get_current_time, list_available_agents]
```

---

### Issue: WebSocket won't connect in IDX

**Debug**:
```bash
# Check if FastAPI is running
ps aux | grep uvicorn

# Check logs
tail -20 /tmp/api.log

# Common issues:
# - ModuleNotFoundError: Check PYTHONPATH
# - Port conflict: Kill and restart
# - API key missing: Add to .env
```

---

### Issue: Wrong time displayed

**Check**:
```bash
# Verify timezone code
grep "timezone(timedelta" adk_agents/greeting_agent/tools.py
# Should show: eastern = timezone(timedelta(hours=-5))
```

---

## ✅ Success Criteria

### Local Docker:
- All containers healthy
- Auto-discovery working
- API endpoints functional
- Tools execute in both UIs
- Time displays correctly (EST)

### IDX:
- Setup completes in < 5 minutes
- All services start without errors
- Same functionality as local Docker
- No dependency conflicts
- No manual file creation needed

### Both:
- Add new agent → Auto-discovered
- No FastAPI code changes needed
- Students can follow ADD_NEW_AGENT.md successfully

---

## 📋 Pre-Workshop Validation

**Before 25-student deep dive**:

1. **Run complete test suite locally** ✅
2. **Run complete test suite in IDX** ⏳
3. **Have 2-3 people test IDX setup** ⏳
4. **Time their setup** (should be < 5 min)
5. **Document any issues** not in TROUBLESHOOTING.md
6. **Update QUICK-START.md** with any learnings

---

## 🎯 What to Report

After testing, document:

**Timing**:
- Local Docker build time: ___ minutes
- Local test completion: ___ minutes
- IDX setup time: ___ minutes
- IDX test completion: ___ minutes

**Issues Found**:
- List any errors or unexpected behavior
- Note any unclear documentation
- Record any manual steps needed

**Success Metrics**:
- X/11 tests passed (Local Docker)
- X/9 tests passed (IDX)
- Setup time: ___ vs 5 min target
- Tool calling: Working / Not working
- Auto-discovery: Working / Not working

---

**Ready to test!** Start with local Docker (faster iteration), then validate in IDX.
