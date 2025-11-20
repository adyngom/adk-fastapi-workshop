# Morning Testing Checklist - 4 Hours Before Workshop

**Goal:** Verify everything works. Don't debug deeply - just confirm no critical failures.

**Time:** 4 hours before 12pm EST = Start at 8am EST

---

## ⏰ Hour 1 (8:00-9:00 AM): Smoke Test All 9 Agents

**Goal:** One query per agent, verify it responds. Quick pass/fail.

### Environment Setup (5 min)

```bash
# Pull latest
cd ~/Code/adk-fastapi-workshop
git pull origin main

# Check git tags
git tag --list  # Should show 10 tags

# Verify agents exist
ls adk_agents/  # Should show 9 directories
```

### IDX Workspace (10 min)

```bash
# Open your instructor IDX workspace
# Run: ./.idx/start-services.sh
# Verify all services started (PIDs shown)

# Check both UIs:
# - Port 3002: ADK Web
# - Port 8501: Streamlit

# Both should show 9 agents in dropdown/sidebar
```

### Rapid Agent Testing (40 min)

**Test each agent with ONE query. Just verify it responds (don't check quality).**

#### ✅ Step 1: greeting_agent
- [ ] **Query:** "What time is it?"
- [ ] **Expect:** Shows current EST time
- [ ] **Bonus:** Click microphone in ADK Web (voice works?)
- [ ] **Time:** 2 min

#### ✅ Step 2: customer_service
- [ ] **Query:** "Customer can't login after password reset"
- [ ] **Expect:** Multi-paragraph response with solution
- [ ] **Check:** Events tab shows 3 agents ran (triage → research → response)
- [ ] **Time:** 3 min

#### ✅ Step 3: content_pipeline
- [ ] **Query:** "Write a short article about AI agents"
- [ ] **Expect:** Article with headline and sections
- [ ] **Check:** Events tab shows 4 agents ran sequentially
- [ ] **Time:** 3 min

#### ✅ Step 4: medical_authorization
- [ ] **Query:** "Pre-auth for knee surgery, patient John Smith, Member ID ABC123"
- [ ] **Expect:** Authorization decision (approved/denied/pending)
- [ ] **Check:** Events tab shows 4 agents (intake → verify → review → authorize)
- [ ] **Time:** 3 min

#### ✅ Step 5: financial_advisor
- [ ] **Query:** "Analyze AAPL stock for moderate risk, long-term investor"
- [ ] **Expect:** Investment recommendation with strategies
- [ ] **Check:** Events tab shows 4 analysts + synthesis (PARALLEL timing!)
- [ ] **Time:** 5 min (parallel takes longer to generate comprehensive output)

#### ✅ Step 6: brand_intelligence
- [ ] **Query:** "Analyze Tesla brand perception"
- [ ] **Expect:** Brand intelligence report
- [ ] **Check:** Events tab shows 4 researchers + synthesis (parallel)
- [ ] **Time:** 5 min

#### ✅ Step 7: software_assistant
- [ ] **Query:** "Fix: 500 error when uploading files over 10MB"
- [ ] **Expect:** Solution with implementation steps
- [ ] **Check:** 3 agents ran (analyzer → searcher → solution generator)
- [ ] **Time:** 3 min

#### ✅ Step 8: project_management
- [ ] **Query:** "Plan a project to migrate monolith to microservices"
- [ ] **Expect:** Comprehensive project plan
- [ ] **Check:** Task breakdown → 3 parallel analysts → synthesis
- [ ] **Time:** 5 min

#### ✅ Step 9: verified_recommendations
- [ ] **Query:** "Recommend a charity for climate change donation, $10k"
- [ ] **Expect:** Verified recommendations with audit trail
- [ ] **Check:** All 5 agents ran (analyzer → researcher → parallel verifiers → recommender → auditor)
- [ ] **Time:** 5 min

### Quick Status Check (5 min)

```bash
# Count passed tests
# Expected: 9/9 agents working

# If any failed:
# - Note which one
# - Note the error
# - Move on (don't debug yet)

# Critical failures (MUST fix):
# - Step 1 (greeting) - students start here
# - Step 2 (customer_service) - teaches Sequential
# - Step 5 (financial_advisor) - teaches Parallel

# Nice-to-have (can demo if broken):
# - Steps 3, 4, 6, 7, 8, 9 - can show code instead of running
```

---

## ⏰ Hour 2 (9:00-10:00 AM): Deep Test Critical Agents

**Goal:** Test the agents students will ask most questions about.

### 🎯 Step 1: greeting_agent (10 min)

**Test all 3 tools:**

- [ ] **Query 1:** "Tell me about my company"
  - **Tool called:** get_company_info()
  - **Expect:** Acme Corporation details

- [ ] **Query 2:** "What time is it?"
  - **Tool called:** get_current_time()
  - **Expect:** Current EST time + date

- [ ] **Query 3:** "What's the workshop structure?"
  - **Tool called:** get_workshop_roadmap()
  - **Expect:** 9 agents across 4 phases

- [ ] **Voice test:** Click microphone in ADK Web
  - **Expect:** Can speak query, agent responds

**Practice explaining:**
- "This is the foundation. Every agent has name, model, description, instruction, and tools."
- "Tools are just Python functions with docstrings."
- "Voice only works with simple agents using Gemini 2+ models."

---

### 🎯 Step 2: customer_service (15 min)

**Test Sequential workflow understanding:**

- [ ] **Query:** "Customer says website keeps logging them out every 5 minutes"

- [ ] **Check Events tab carefully:**
  - Agent 1 (triage): Should categorize as P1/P2, technical
  - Agent 2 (research): Should suggest session timeout or cookie issues
  - Agent 3 (response): Should craft empathetic response with solution

- [ ] **Test state passing:**
  - Does research reference triage priority?
  - Does response use research findings?
  - State should flow automatically

**Practice explaining:**
- "Sequential means dependent. Each agent needs the previous one's output."
- "State passes automatically through conversation history - no manual management."
- "Final agent output is what user sees. Check Events tab for intermediate steps."

---

### 🎯 Step 5: financial_advisor (15 min)

**Test Parallel execution:**

- [ ] **Query:** "Analyze Microsoft stock for conservative investor, $50k to invest"

- [ ] **Check Events tab for parallel execution:**
  - Look at timestamps - all 4 analysts should have similar times
  - Should NOT be sequential (30 sec → 60 sec → 90 sec → 120 sec)
  - Should BE parallel (all around 30-40 sec mark)

- [ ] **Check synthesis quality:**
  - Does it reference ALL 4 analysts?
  - "from_data_analyst: ..., from_trading_analyst: ..., from_execution_analyst: ..., from_risk_analyst: ..."
  - Should combine perspectives, not just list them

**Practice explaining:**
- "This is the paradigm shift. Sequential = dependent tasks. Parallel = independent tasks."
- "All 4 analysts analyze the same stock from different angles simultaneously."
- "Performance: 4x faster than sequential would be."
- "Synthesis is what makes it valuable - combines 4 outputs into 1 recommendation."

---

### 🎯 Step 7: software_assistant (10 min)

**Test MCP concept (simulated):**

- [ ] **Query:** "Bug: Users getting timeout errors on data export"

- [ ] **Verify workflow:**
  - Analyzer: Extracts error, component, priority
  - Searcher: Simulates searching DB + GitHub + Stack Overflow
  - Solution: Generates fix with implementation steps

- [ ] **Check citations:**
  - Should reference "similar tickets", "GitHub issues", "Stack Overflow"
  - Even though simulated, pattern should be clear

**Practice explaining:**
- "Workshop simulates MCP tools to focus on patterns, not infrastructure."
- "Production code examples in README show real MCP integration."
- "MCP Toolbox for databases is new in ADK 1.18 - production-ready."

---

### 🎯 Step 9: verified_recommendations (10 min)

**Test verification and audit:**

- [ ] **Query:** "Recommend a charity for education in Africa, $25k donation"

- [ ] **Verify all 5 stages:**
  - Analyzer: Assesses stakes (high - $25k)
  - Researcher: Finds 3-5 candidate charities
  - Parallel verifiers: Independent verification + risk assessment
  - Recommender: Ranked recommendations (only verified ones)
  - Auditor: Complete decision trail

- [ ] **Check audit trail:**
  - Should include timestamps
  - Should show which agent made which decision
  - Should reference sources for verification

**Practice explaining:**
- "This is inspired by Ayo Adedeji's charity advisor using AP2 protocol."
- "Key insight: When agents handle money, you need accountability."
- "Independent verification - verifier doesn't know which candidate researcher prefers."
- "Complete audit trail - can replay the entire decision process."

---

## ⏰ Hour 3 (10:00-11:00 AM): Presentation Prep

**Goal:** Know what you'll say for each agent.

### Write Your Teaching Notes (30 min)

**For each agent, write 2-3 key points:**

```markdown
STEP 1 - greeting_agent:
1. Foundation: name, model, description, instruction, tools
2. Tools are Python functions with docstrings
3. Voice works with simple agents (Gemini 2+ models)

STEP 2 - customer_service:
1. Sequential = dependent tasks (triage BEFORE research)
2. State passes automatically (no manual management)
3. Check Events tab to see all agents (only final shows in chat)

STEP 5 - financial_advisor:
1. PARADIGM SHIFT: Parallel for independent tasks
2. 4x faster (all analysts work simultaneously)
3. Synthesis combines perspectives into one recommendation

[Continue for all 9...]
```

### Prepare Examples (15 min)

**For each pattern, have a real-world example:**

- **Sequential:** Any multi-step process (approve → process → notify)
- **Parallel:** Any decision needing multiple expert views (due diligence, product launch)
- **Sequential + Parallel:** Any complex workflow (project planning, M&A analysis)

### Review Potential Questions (15 min)

Go through "Questions Students Will Ask" section in audio briefing.
Prepare short, clear answers for:
- When to use Sequential vs Parallel
- Voice input limitations
- Built-in tools restrictions
- A2A vs ParallelAgent
- Production readiness

---

## ⏰ Hour 4 (11:00 AM-12:00 PM): Final Tech Check + Buffer

### Tech Check (30 min)

**IDX Environment:**
- [ ] Workspace open
- [ ] All 9 agents showing in both UIs
- [ ] Services running (check PIDs)
- [ ] Can access port 3002 (ADK Web)
- [ ] Can access port 8501 (Streamlit)

**Backup API Keys:**
- [ ] Have 3-5 backup keys ready
- [ ] Test 1 backup key (create test agent, verify it works)
- [ ] Write them down somewhere accessible

**Screen Share:**
- [ ] Test screen share in YouTube studio
- [ ] Audio working
- [ ] Can see IDX workspace clearly
- [ ] Text is readable

**Materials Ready:**
- [ ] workshop_progression.yaml open
- [ ] STUDENT_SETUP_CHECKLIST.md open (for helping stuck students)
- [ ] Backup API keys list
- [ ] Water, coffee, snacks

### Pre-Workshop Student Checks (11:45 AM - 12:00 PM)

When students arrive early:

```markdown
Quick checks to ask in chat:
1. "Can everyone see the Streamlit UI?"
2. "Does it show 'Agents Loaded: 9'?"
3. "Can you select greeting_agent and send a message?"

Common issues:
- Streamlit blank: Check .streamlit/config.toml exists
- Agents not loading: Re-run start-services.sh
- API key error: Paste backup key

Goal: Everyone ready by 12:00 sharp
```

### Breathing Room (11:45-12:00)

**Don't start prep at 11:45. Be ready by 11:30.**

11:30-11:45: Relax, breathe, review key points
11:45-12:00: Help students with setup issues
12:00: START!

---

## 🚨 Critical Failure Scenarios

**If greeting_agent doesn't work:**
- Everyone starts here - MUST fix immediately
- Check: Is API key valid?
- Check: Are services running?
- Fallback: Everyone use ADK Web on port 3002 instead of Streamlit

**If Streamlit doesn't load for students:**
- Use ADK Web (port 3002) as primary
- Streamlit is nicer, but ADK Web works fine
- Don't spend 20 minutes debugging Streamlit - move on

**If auto-discovery broken (0 agents show):**
- Check: api/agents/manager.py discover_agents function
- Quick fix: Restart services
- Nuclear option: Students checkout step-1 tag, use just greeting_agent

**If YouTube stream fails:**
- Have Zoom backup link ready
- Or use Google Meet
- Audio > perfect video

---

## 🎯 Success Criteria for Testing

**Minimum viable:**
- [ ] 7 of 9 agents working (Steps 1, 2, 3, 5, 7, 8, 9)
- [ ] Both UIs accessible (Streamlit OR ADK Web - at least one)
- [ ] Can switch between agents
- [ ] Test queries respond (even if not perfect quality)

**Ideal:**
- [ ] All 9 agents working
- [ ] Both UIs working (Streamlit AND ADK Web)
- [ ] Events tab shows correct execution patterns (sequential vs parallel)
- [ ] Voice input works on greeting_agent

**Nice to have:**
- [ ] All tools being called correctly
- [ ] Response quality high
- [ ] No lag or performance issues

---

## 📊 Testing Log Template

**As you test, track results:**

```
8:00 AM - Environment Setup
✅ Git pull successful
✅ 9 agents in adk_agents/
✅ 10 git tags present

8:15 AM - IDX Services
✅ start-services.sh executed
✅ Streamlit: PID 1234
✅ ADK Web: PID 1235
✅ FastAPI: PID 1236

8:20 AM - Agent Smoke Tests
✅ greeting_agent - responded to time query
✅ customer_service - generated support response
✅ content_pipeline - wrote article outline
✅ medical_authorization - generated auth decision
✅ financial_advisor - provided stock analysis
✅ brand_intelligence - brand health report
✅ software_assistant - bug solution provided
✅ project_management - project plan created
✅ verified_recommendations - charity recommendation

RESULT: 9/9 agents working ✅

8:45 AM - Critical Path Deep Tests
[Focus on steps 1, 2, 5, 9...]
```

---

## 🎓 Quick Reference: What Each Agent Does

**Keep this handy during workshop:**

| Step | Agent | Test Query | Expected Output |
|------|-------|------------|-----------------|
| 1 | greeting_agent | "What time is it?" | Current EST time |
| 2 | customer_service | "Login issue after password reset" | Support response with solution |
| 3 | content_pipeline | "Write about AI testing" | Article with headline + sections |
| 4 | medical_authorization | "Pre-auth for knee surgery" | Approval/denial decision |
| 5 | financial_advisor | "Analyze AAPL, moderate risk" | Investment recommendation |
| 6 | brand_intelligence | "Analyze Nike brand health" | Brand intelligence report |
| 7 | software_assistant | "Fix 500 error on file upload" | Bug solution with steps |
| 8 | project_management | "Plan microservices migration" | Comprehensive project plan |
| 9 | verified_recommendations | "Recommend climate charity, $10k" | Verified recommendations + audit |

---

## 🔧 Quick Fixes for Common Issues

### Agent Not Responding
```bash
# Check services running
ps aux | grep -E "streamlit|adk|uvicorn"

# Restart if needed
pkill -f streamlit
pkill -f "adk web"
./.idx/start-services.sh
```

### API Key Error
```bash
# Check key in .env
cat .env | grep GOOGLE_API_KEY

# Test key works
curl -H "Content-Type: application/json" \
  -d '{"contents":[{"parts":[{"text":"test"}]}]}' \
  "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash-exp:generateContent?key=YOUR_KEY"
```

### Agents Not Auto-Discovered
```bash
# Check each agent has agent.py with root_agent
for dir in adk_agents/*/; do
  if grep -q "root_agent" "$dir/agent.py" 2>/dev/null; then
    echo "✅ $(basename $dir)"
  else
    echo "❌ $(basename $dir) - missing root_agent"
  fi
done
```

### Streamlit Blank Screen
```bash
# Check config exists
cat .streamlit/config.toml

# If missing, create it:
mkdir -p .streamlit
cat > .streamlit/config.toml << 'EOF'
[server]
enableCORS = false
enableXsrfProtection = false
serverAddress = "0.0.0.0"
EOF

# Restart Streamlit
pkill -f streamlit
streamlit run streamlit_apps/workshop_ui/app.py --server.port 8501 --server.address 0.0.0.0 &
```

---

## 📋 Final Pre-Workshop Checklist (11:30 AM)

### 30 Minutes Before Students Arrive

**Technical:**
- [ ] IDX workspace open and tested
- [ ] All 9 agents verified working
- [ ] Streamlit UI accessible
- [ ] ADK Web accessible (backup)
- [ ] Screen share tested
- [ ] Audio tested

**Materials:**
- [ ] workshop_progression.yaml open (reference)
- [ ] Backup API keys ready (written down)
- [ ] STUDENT_SETUP_CHECKLIST.md open (for helping students)
- [ ] YouTube Studio open (stream ready)

**Personal:**
- [ ] Water/coffee available
- [ ] Bathroom break taken
- [ ] Phone on silent
- [ ] Comfortable for 4 hours
- [ ] Deep breath - you're ready! 🧘

### Student Arrival (11:45 AM)

**In YouTube chat, ask:**
1. "👋 Who's here? Type 'ready' if your Streamlit UI is showing 9 agents"
2. "🚨 Anyone stuck on setup? Let me know NOW in chat"
3. "📊 Quick poll: Can everyone see greeting_agent in the UI?"

**Help stuck students:**
- Guide to STUDENT_SETUP_CHECKLIST.md
- Offer backup API key if theirs doesn't work
- If multiple students stuck, do 5-min group troubleshooting session before starting

### Start Time (12:00 PM Sharp)

**Opening:**
```
"Welcome everyone! I'm excited to teach you production AI agent patterns today.

We're building 9 agents over 4 hours. Not calculators or weather bots - real
systems that automate customer service, financial analysis, content creation,
and high-stakes decisions.

By 4 PM, you'll know how to build enterprise AI agent systems.

Let's start with Step 1..."
```

---

## 💡 Pro Tips

**Energy Management:**
- Take 5-min break every hour
- Stand and stretch during breaks
- Keep water nearby
- High energy for intro and finale, steady middle

**Student Engagement:**
- Ask questions: "Why Sequential here instead of Parallel?"
- Check understanding: "Everyone following? Type Y in chat"
- Celebrate progress: "You just built your first multi-agent workflow!"

**Time Management:**
- Set timer for each phase
- If running over, cut exercises (increase demo ratio)
- Protect Phase 1 and 2 time (foundation)
- Phase 3 and 4 can be demo-heavy if needed

**Technical:**
- Share screen showing both code AND UI
- Use Events tab liberally - makes patterns visible
- Zoom in on code when showing details
- Keep pace moderate - let them follow along

---

## 🎁 Bonus Content Decision (If Time Permits)

**If finishing early (before 3:45 PM):**
- Deliver all 4 bonus demos (Google Search, Code Execution, Multi-Model, Deployment)
- Full masterclass teaser
- Q&A

**If finishing on time (3:45-4:00 PM):**
- Just Google Search demo (2 min - most impressive)
- Quick masterclass mention
- Q&A

**If running late (after 4:00 PM):**
- Skip bonus
- Mention BONUS_CONTENT.md in follow-up email
- End at 4:15 max (respect their time)

---

## ✅ You're Ready When...

- [ ] All 9 agents tested (at least smoke test)
- [ ] Steps 1, 2, 5, 9 tested deeply
- [ ] Teaching points written down
- [ ] Tech checked (screen share, audio, services)
- [ ] Backup plans ready (API keys, fallback UI)
- [ ] Calm and confident

**Expected completion: 11:30 AM**
**Buffer time: 11:30-11:45 AM**
**Student arrival: 11:45 AM**
**Workshop start: 12:00 PM**

---

## 🌟 Remember

You've built something exceptional. The agents are production-ready. The documentation is comprehensive. The progression is well-designed.

The manual setup works (you tested it with fresh account and made a video).

The workshop materials are polished and professional.

You know this content deeply - you helped build it.

Trust your preparation. Trust the materials. Trust yourself.

**You've got this! 🚀**

---

**Print this checklist or keep it on second monitor tomorrow morning.**
**Follow it step by step. Don't overthink. Just test and verify.**
**You'll be ready with time to spare.**
