# Modules 3-9 Recording Scripts - Consolidated

**Note:** Full detailed scripts in individual module folders. This is quick reference.

---

## MODULE 3: Single Agents (90 min) - recording-script.md

**Hook:** "Build your first AI agent in next 90 minutes"

**Structure:**
1. Agent class structure (20 min) - name, model, description, instruction, tools explained
2. Build greeting_agent from scratch (30 min) - Live coding with full narration
   - "So I'm just going to create agent.py..."
   - Build step-by-step
   - Add get_company_info and get_current_time tools
3. Testing strategies (15 min) - ADK Web, run_debug(), Events tab
4. Voice input demo (10 min) - ADK 1.18 feature
5. Production patterns (15 min)

**Exercise:** Customize company_info, add team_members tool
**Files Ready:** ✅ adk_agents/greeting_agent/

**Ady Voice:**
- "Let me show you how agents work..."
- "So I'm creating a new file here..."
- "There you go - our first agent!"
- "This is very important - the instruction shapes behavior"

---

## MODULE 4: Sequential Workflows (120 min)

**Hook:** "Automate entire business processes with multi-agent workflows"

**Structure:**
1. When Sequential (15 min) - Dependent tasks, decision matrix
2. customer_service build (35 min) - Triage → Research → Respond
   - Build each agent with narration
   - Show state passing in Events tab
   - "You see that? Research uses triage output automatically"
3. Pattern reuse: content_pipeline (25 min) - Same pattern, content domain
4. Decision gates: medical_authorization (30 min) - Workflow can stop early
5. Best practices (15 min)

**Exercise:** Build 3-agent support workflow with escalation
**Files Ready:** ✅ All 3 agents exist

**Key Moment:** Events tab showing sequential execution with state flow

---

## MODULE 5: Parallel Execution (120 min)

**Hook:** "4x faster analysis with parallel execution - this is the paradigm shift"

**Structure:**
1. Independent vs dependent (15 min) - When Parallel beats Sequential
2. financial_advisor build (40 min) - 4 analysts + synthesis
   - Show all 4 running simultaneously in Events tab
   - **THE $175 PROBLEM** - "Wait, this says $175 but real price is $273!"
   - "We'll fix this in Module 7 with Google Search tool"
3. Performance demo (15 min) - Time parallel vs sequential
4. brand_intelligence (25 min) - Same pattern, different domain
5. Synthesis patterns (25 min)

**Exercise:** Add 5th analyst (sentiment_analyst)
**Files Ready:** ✅ Both agents exist

**Magic Setup:** Show outdated stock price, tease Module 7 fix!

---

## MODULE 6: Memory & RAG (120 min)

**Hook:** "Make your agents remember and learn from past conversations"

**Structure:**
1. Memory types (15 min) - Session vs long-term
2. Redis session memory (25 min) - Workshop already uses this
3. Vector databases (40 min) - ChromaDB setup, embeddings, semantic search
   - Live demo: Store documents, query with natural language
4. RAG deep dive (30 min) - Retrieval-Augmented Generation
   - Document ingestion pipeline
   - Query → Retrieve → Generate pattern
5. Context management (10 min)

**Exercise:** Add ChromaDB to customer_service
**Code to Create:** customer_service_with_memory/, rag_pipeline/
**Prep:** 2-3 hours (Day 5 evening)

---

## MODULE 7: Production Tools (120 min) ⭐

**Hook:** "Two lines of code transform your agent from stale to real-time"

**Structure:**
1. **THE $175 FIX** (30 min) - MAGIC MOMENT!
   - "Remember Module 5? Agent said AAPL was $175"
   - "Real price today: $273"
   - "Let me show you the fix..." [Add google_search tool]
   - Re-run: "There you go - $269! Real-time data!"
   - "THIS is why built-in tools matter"
2. Code execution (20 min) - Agent writes and runs Python
3. BigQuery tools (15 min) - Natural language to SQL
4. MCP integration (30 min) - Database access patterns
5. Multi-model (15 min) - OpenAI, Claude, Ollama via LiteLLM

**Exercise:** Add Google Search to research agent
**Code to Create:** financial_advisor_with_search/, multi_model_examples/
**Prep:** 1-2 hours (Day 6 evening)

**Critical:** This is your "WOW" moment - $175 → real price with 2 lines!

---

## MODULE 8: Complex Orchestration (120 min)

**Hook:** "Combine everything - Sequential + Parallel + Verification"

**Structure:**
1. Complex patterns (20 min) - When to combine
2. project_management (30 min) - Sequential outer, Parallel inner
3. Agent-to-Agent (20 min) - Agents calling agents as tools
4. verified_recommendations (30 min) - **Ayo's AP2 charity advisor story**
   - "When agents handle money, you need accountability"
   - Independent verification, audit trails
   - Role separation for security
5. BigQuery audit logging (15 min) - ADK 1.18 feature

**Exercise:** Add audit logging to medical_authorization
**Files Ready:** ✅ Both agents exist

**Story Time:** Tell Ayo Adedeji's charity advisor example (engaging!)

---

## MODULE 9: Cloud Deployment (120 min)

**Hook:** "Deploy your agents to production - this is the final piece"

**Structure:**
1. Docker containerization (30 min) - Multi-stage builds
2. Cloud Run deployment (35 min) - **LIVE DEPLOYMENT!**
   - Actually deploy customer_service agent
   - Show URL, test it live
   - "And like that, we are live!"
3. Monitoring (25 min) - Cloud Logging, dashboards
4. Cost optimization (15 min) - Caching, model selection, Apigee intro
5. CI/CD (10 min) - GitHub Actions automation

**Exercise:** Deploy greeting_agent to Cloud Run
**Code to Create:** deployment/cloud-run/, monitoring/, .github/workflows/
**Prep:** 2 hours (Day 8 evening)

**Exciting Moment:** Live deployment, show it working in production!

---

## 🎯 VOICE CONSISTENCY ACROSS ALL MODULES

**Every module uses:**
- Opening: "Hello and welcome to Module [N]. Okay, so today..."
- Demos: "So I'm just going to... There you go. Perfect."
- Emphasis: "This is very important because..."
- Transitions: "All right, let's keep going..."
- Problems: "You might try this first... but you'll get an error..."
- Success: "There you go!", "Perfect!", "And like that, we have it working"
- Closing: "That's all for Module [N]. See you in the next one!"

**Pacing:** Moderate, clear, with pauses
**Energy:** Calm and steady (your natural style)
**Approach:** Problem-first, live narration, practical

---

## ✅ ALL 9 MODULES OUTLINED

**Modules 1-2:** Foundation (theory + Python)
**Modules 3-5:** Core patterns (workshop content)
**Modules 6-7:** Premium features (new content needed)
**Modules 8-9:** Enterprise (workshop + deployment)

**Total:** 12-14 hours content
**Recording:** 9 days, one per day
**Your voice:** Natural, conversational, practical
**Structure:** Clear, proven, gradual complexity

**Now creating full detailed scripts for Modules 3-9...**
