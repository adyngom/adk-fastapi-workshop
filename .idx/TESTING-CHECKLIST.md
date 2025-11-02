# ✅ IDX Testing Checklist

Before announcing IDX setup to students, verify everything works.

---

## 🧪 Pre-Workshop Testing

### Test 1: Fresh Account Setup

**Tester**: Use a test Google account (not your main)

**Steps**:
- [ ] Click "Open in IDX" button from README
- [ ] IDX workspace opens in browser
- [ ] onCreate runs automatically (watch progress bar)
- [ ] Dependencies install successfully (~60 seconds)
- [ ] `.venv` folder created
- [ ] `.env` file exists

**Expected time**: 90-120 seconds

---

### Test 2: API Key Configuration

- [ ] Open `.env` file in IDX
- [ ] File already exists (created from template)
- [ ] Add test API key
- [ ] Save file (no errors)

**Expected time**: 30 seconds

---

### Test 3: Service Startup

```bash
./.idx/start-services.sh
```

**Verify**:
- [ ] Redis starts successfully
- [ ] FastAPI starts on port 8000
- [ ] ADK Web starts on port 3002
- [ ] Frontend starts on port 8080
- [ ] No error messages in output
- [ ] All PIDs displayed

**Expected time**: 10 seconds

---

### Test 4: Port Forwarding

**IDX should show port notifications**:
- [ ] Port 8080 forwarding notification
- [ ] Port 3002 forwarding notification
- [ ] Port 8000 forwarding notification

**Click each notification**:
- [ ] Opens in new tab with HTTPS URL
- [ ] Format: `https://8080-idx-projectname-randomid.cluster.idx.dev`

---

### Test 5: Custom Frontend

**Open port 8080 URL**:
- [ ] Chat UI loads
- [ ] Title: "🤖 ADK Workshop Chat"
- [ ] Agent dropdown shows all 3 agents
- [ ] Status shows "Connected" (green)

**Test interaction**:
- [ ] Select "Greeting Agent"
- [ ] Send message: "Hello!"
- [ ] Receives streaming response
- [ ] Markdown renders correctly

---

### Test 6: ADK Web Interface

**Open port 3002 URL**:
- [ ] ADK Web interface loads
- [ ] Shows agent selector dropdown
- [ ] Lists all 3 agents:
  - greeting_agent
  - news_pipeline
  - competitive_analysis

**Test greeting_agent**:
- [ ] Select greeting_agent
- [ ] Send message: "What time is it?"
- [ ] Agent calls get_current_time() tool
- [ ] Events tab shows tool_call
- [ ] Events tab shows tool_result
- [ ] Response includes time

---

### Test 7: Sequential Pipeline

**In ADK Web**:
- [ ] Select news_pipeline
- [ ] Send: "Analyze tech news from today"
- [ ] Events tab shows 3-agent sequence:
  - news_gatherer
  - summarizer
  - sentiment_analyzer
- [ ] State accumulates through pipeline
- [ ] Final response shows analysis

**In Custom Frontend**:
- [ ] Select "News Pipeline (Sequential)"
- [ ] Send same message
- [ ] Streams response
- [ ] Markdown formatting works

---

### Test 8: Parallel Execution

**In ADK Web**:
- [ ] Select competitive_analysis
- [ ] Send: "Compare AI platforms"
- [ ] Events show parallel execution
- [ ] 3 analysts run concurrently
- [ ] Synthesizer combines results

---

### Test 9: Git Tag Navigation

```bash
# In IDX terminal
git checkout v1-exercise-1
```

**Verify**:
- [ ] Code changes
- [ ] Restart services works
- [ ] greeting_agent has tools

```bash
git checkout v2-exercise-2
```

- [ ] news_pipeline agent exists
- [ ] Works in both interfaces

```bash
git checkout main
```

- [ ] All 3 agents present

---

## 🐛 Common Issues & Solutions

### Issue: onCreate didn't complete

**Symptom**: No .venv folder

**Solution**:
```bash
# Manually run onCreate
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install -r requirements-adk.txt
```

---

### Issue: Services fail to start

**Symptom**: start-services.sh errors

**Debug**:
```bash
# Check Python
python --version  # Should be 3.11

# Check ADK
adk --version

# Check .env
cat .env | grep GOOGLE_API_KEY

# Try manual start
source .venv/bin/activate
cd api
uvicorn main:app --host 0.0.0.0 --port 8000
# Check for errors
```

---

### Issue: Ports not accessible

**Symptom**: Can't open port URLs

**Solution**:
- Check "Ports" tab in IDX (bottom panel)
- Click "Open in Browser" for each port
- Verify firewall not blocking
- Try incognito window

---

### Issue: WebSocket won't connect

**Symptom**: Custom UI shows "Disconnected"

**Check**:
- FastAPI running on port 8000?
- WebSocket endpoint working?
- Check browser console for errors
- Try from API docs: `http://YOUR_IDX:8000/docs`

---

## ✅ Success Criteria

### All Green When:

- [ ] Fresh account can open in IDX
- [ ] onCreate completes without errors
- [ ] All services start successfully
- [ ] All 3 interfaces accessible
- [ ] All 3 agents work in both UIs
- [ ] Tool calling works (greeting_agent)
- [ ] Sequential pipeline works (news_pipeline)
- [ ] Parallel execution works (competitive_analysis)
- [ ] Git tags navigation works
- [ ] Markdown rendering works
- [ ] No setup took longer than 5 minutes

---

## 📊 Time Tracking

**Test this multiple times with different people**:

| Tester | Setup Time | Issues | Notes |
|--------|------------|--------|-------|
| Person 1 | ___ min | | |
| Person 2 | ___ min | | |
| Person 3 | ___ min | | |

**Target**: 95% of testers under 5 minutes

---

## 🎯 Recommendations

Based on testing:

**If > 80% success rate**: ✅ Use for workshop
**If 50-80% success**: ⚠️ Have Docker backup ready
**If < 50% success**: ❌ Stick with Docker, improve IDX

---

**Last Updated**: November 2025
**Status**: Ready for testing
**Next**: Test with 3-5 people before workshop
