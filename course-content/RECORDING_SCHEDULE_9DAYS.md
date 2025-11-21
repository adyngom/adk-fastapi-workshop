# 9-Day Recording Sprint - Daily Checklist

**Goal:** Record all 9 modules in 9 days (pre-edited version)
**Commitment:** 3-4 hours/day
**Start:** Tonight!
**Finish:** 9 days from now

---

## 📋 Daily Template (Repeat for Each Module)

### Morning Prep (30 min)
- [ ] Review recording script for today's module
- [ ] Open all code files needed
- [ ] Test demos work (no surprises during recording!)
- [ ] Set up screen recording software
- [ ] Quick audio check

### Recording Block (2-3 hours)
- [ ] Record intro/hook (5 min content = 10 min with retakes)
- [ ] Record main content (90 min content = 2 hours with retakes)
- [ ] Record exercise intro (5 min)
- [ ] Record solution (15 min = 20 min with retakes)
- [ ] Record recap (5 min)

### Evening Review (30 min)
- [ ] Watch recording (spot major errors only)
- [ ] Note: "Redo section X tomorrow morning if needed"
- [ ] Prepare tomorrow's module (review script)
- [ ] Celebrate! One module done! 🎉

**Total:** 3-4 hours/day

---

## 🗓️ DAY 1: Module 1 - Foundation

**Duration:** 90 minutes content

### Pre-Recording Checklist:
- [ ] Slides: AI landscape, framework comparison, setup steps
- [ ] Code: None needed (theory module)
- [ ] Demos: Show aistudio.google.com, API key creation
- [ ] Screen: Browser tabs ready (ADK docs, AI Studio)

### Recording Segments:
1. **Hook (30 sec):** "By end of this module, you'll understand the AI agent landscape and have ADK installed"
2. **What is an AI Agent?** (15 min) - Whiteboard/slides
3. **Framework Comparison** (25 min) - Comparison matrix slide
4. **Environment Setup** (30 min) - Live demo: Python, ADK install
5. **ADK Web Intro** (10 min) - Quick tour
6. **Exercise intro** (5 min): "Install ADK and verify"
7. **Solution** (5 min): Troubleshooting common issues
8. **Recap** (2 min): "You now understand agents and have environment ready"

### Files to Create Before Recording:
- slides/module-1-landscape.key (5-10 slides)
- recording-script/module-1-script.md (detailed outline)

**Evening:** Review footage, prepare Module 2

---

## 🗓️ DAY 2: Module 2 - Python for Production

**Duration:** 90 minutes content

### Pre-Recording Checklist:
- [ ] Slides: Async flow diagram, Pydantic examples
- [ ] Code: async_examples.py, pydantic_examples.py
- [ ] Demos: async vs sync comparison, validation examples
- [ ] Screen: VS Code with examples ready

### Recording Segments:
1. **Hook:** "Master async/await - it's simpler than you think"
2. **Async/Await** (30 min) - Live coding demo
3. **Pydantic Models** (25 min) - Build customer model
4. **Type Hints** (20 min) - Show IDE autocomplete benefits
5. **Error Handling** (15 min) - Try/except patterns
6. **Exercise:** Build async validator with Pydantic
7. **Solution:** Complete code walkthrough
8. **Recap:** "You can now write production Python for agents"

### Files to Create Before Recording:
- slides/module-2-python.key
- code/async_examples.py
- code/pydantic_customer_model.py
- recording-script/module-2-script.md

---

## 🗓️ DAY 3: Module 3 - Single Agents

**Duration:** 90 minutes content

### Pre-Recording Checklist:
- [ ] Slides: Agent structure diagram
- [ ] Code: adk_agents/greeting_agent/ (already exists!)
- [ ] Demos: Build greeting_agent step-by-step
- [ ] Screen: Fresh directory, build from scratch

### Recording Segments:
1. **Hook:** "Build your first AI agent in next 90 minutes"
2. **Agent Structure** (20 min) - Explain each parameter
3. **Building greeting_agent** (30 min) - Code from scratch
4. **Custom Tools** (20 min) - get_company_info, get_current_time
5. **Testing** (10 min) - ADK Web + run_debug()
6. **Voice Input** (10 min) - Demo microphone feature
7. **Exercise:** Customize company_info
8. **Solution:** Add team_members tool
9. **Recap:** "You built your first production agent"

### Files Already Exist:
- ✅ adk_agents/greeting_agent/
- ✅ .workshop/exercises/step-1/
- ✅ .workshop/solutions/step-1/

### Just Need:
- slides/module-3-single-agents.key
- recording-script/module-3-script.md

---

## 🗓️ DAY 4: Module 4 - Sequential Workflows

**Duration:** 120 minutes content (longest module!)

### Pre-Recording Checklist:
- [ ] Slides: Sequential flow diagram, state passing visual
- [ ] Code: All 3 agents (customer_service, content_pipeline, medical_authorization)
- [ ] Demos: Build customer_service from scratch
- [ ] Screen: adk_agents/ directory ready

### Recording Segments:
1. **Hook:** "Build multi-agent workflows that automate entire business processes"
2. **When Sequential** (15 min) - Decision matrix
3. **customer_service Build** (35 min) - 3-agent workflow
4. **Pattern Reuse** (25 min) - content_pipeline same pattern
5. **Decision Gates** (30 min) - medical_authorization
6. **Best Practices** (15 min) - Production tips
7. **Exercise:** Build support workflow
8. **Solution:** Complete with escalation
9. **Recap:** "You can now build multi-step automated workflows"

### Files Already Exist:
- ✅ adk_agents/customer_service/
- ✅ adk_agents/content_pipeline/
- ✅ adk_agents/medical_authorization/

### Just Need:
- slides/module-4-sequential.key
- recording-script/module-4-script.md

---

## 🗓️ DAY 5: Module 5 - Parallel Execution

**Duration:** 120 minutes content

### Pre-Recording Checklist:
- [ ] Slides: Parallel vs Sequential comparison, performance graphs
- [ ] Code: financial_advisor, brand_intelligence (already exist!)
- [ ] Demos: Show parallel execution in Events tab (timestamp proof!)
- [ ] Screen: ADK Web ready for parallel demo

### Recording Segments:
1. **Hook:** "4x faster analysis with parallel execution"
2. **Paradigm Shift** (15 min) - Dependent vs independent tasks
3. **financial_advisor** (40 min) - Build 4 analysts + synthesis
4. **Performance Demo** (15 min) - Parallel vs sequential timing comparison
5. **brand_intelligence** (25 min) - Pattern reuse
6. **Synthesis Patterns** (15 min) - Combining perspectives
7. **Exercise:** Add 5th analyst
8. **Solution:** sentiment_analyst integration
9. **Recap:** "You know when Parallel beats Sequential"

### Files Already Exist:
- ✅ adk_agents/financial_advisor/
- ✅ adk_agents/brand_intelligence/

### Just Need:
- slides/module-5-parallel.key (with performance graphs!)
- recording-script/module-5-script.md

---

## 🗓️ DAY 6: Module 6 - Memory & RAG

**Duration:** 120 minutes content

⚠️ **PREP NEEDED:** Build example code BEFORE recording day

### Pre-Recording Checklist:
- [ ] **Code to create:** customer_service_with_memory/ (ChromaDB integration)
- [ ] **Code to create:** rag_example/ (document ingestion + search)
- [ ] Slides: Memory types, RAG architecture
- [ ] Demos: ChromaDB setup, vector search demo

### Recording Segments:
1. **Hook:** "Make your agents remember and learn"
2. **Memory Types** (15 min) - Session vs long-term
3. **Redis Session Memory** (25 min) - Workshop already uses this
4. **Vector Databases** (40 min) - ChromaDB setup, embeddings
5. **RAG Deep Dive** (30 min) - Document ingestion, retrieval, generation
6. **Context Management** (10 min) - Token limits, summarization
7. **Exercise:** Add ChromaDB to customer_service
8. **Solution:** Agent remembers past tickets
9. **Recap:** "Your agents now have memory"

### Files to Create (Day 5 evening or Day 6 morning):
- module-6/code/customer_service_with_chromadb/
- module-6/code/rag_pipeline/
- module-6/code/document_ingestion.py
- slides/module-6-memory.key
- recording-script/module-6-script.md

**Prep Time:** 2-3 hours (create code examples)

---

## 🗓️ DAY 7: Module 7 - Production Tools

**Duration:** 120 minutes content

### Pre-Recording Checklist:
- [ ] **Code to create:** financial_advisor_with_search/ (Google Search integration)
- [ ] **Code to create:** multi_model_example/ (LiteLLM)
- [ ] Slides: Built-in tools overview, MCP architecture
- [ ] Demos: **THE $175 → $269 STOCK FIX!** (your magic moment)

### Recording Segments:
1. **Hook:** "Two lines of code for real-time data"
2. **THE PROBLEM Demo** (10 min) - Show financial_advisor with $175 (outdated)
3. **Google Search Tool** (20 min) - Add it, show $269 (real-time!) 🎆
4. **Code Execution** (20 min) - Calculations, charts
5. **BigQuery Tools** (15 min) - Natural language → SQL
6. **MCP Integration** (30 min) - Database access patterns
7. **Multi-Model** (15 min) - OpenAI, Claude, Ollama via LiteLLM
8. **Exercise:** Add Google Search to research agent
9. **Solution:** Real-time data agent
10. **Recap:** "Your agents access real-time data and external services"

### Files to Create (Day 6 evening):
- module-7/code/financial_advisor_with_search/
- module-7/code/multi_model_comparison/
- module-7/code/mcp_database_example/
- slides/module-7-tools.key
- recording-script/module-7-script.md

**Prep Time:** 2 hours

---

## 🗓️ DAY 8: Module 8 - Complex Orchestration

**Duration:** 120 minutes content

### Pre-Recording Checklist:
- [ ] Slides: Complex orchestration diagram, AP2 architecture
- [ ] Code: project_management, verified_recommendations (already exist!)
- [ ] Demos: Sequential + Parallel combined, verification flow
- [ ] Screen: Both agents ready to demo

### Recording Segments:
1. **Hook:** "Combine everything: Sequential + Parallel + Verification"
2. **Complex Orchestration** (20 min) - When to combine patterns
3. **project_management** (30 min) - Sequential + Parallel together
4. **A2A Pattern** (20 min) - Agents calling agents as tools
5. **verified_recommendations** (30 min) - AP2-inspired, Ayo's story
6. **Audit Trails** (15 min) - BigQuery logging, accountability
7. **Exercise:** Add audit logging
8. **Solution:** Complete audit trail
9. **Recap:** "You can build enterprise systems with accountability"

### Files Already Exist:
- ✅ adk_agents/project_management/
- ✅ adk_agents/verified_recommendations/

### Just Need:
- slides/module-8-orchestration.key
- recording-script/module-8-script.md

---

## 🗓️ DAY 9: Module 9 - Cloud Deployment

**Duration:** 120 minutes content

⚠️ **PREP NEEDED:** Deployment configs ready

### Pre-Recording Checklist:
- [ ] **Verify:** Dockerfiles work (already have these!)
- [ ] **Verify:** Cloud Run deployment tested
- [ ] Slides: Docker diagram, Cloud Run architecture
- [ ] Demos: Live deployment to Cloud Run (record actual deployment!)

### Recording Segments:
1. **Hook:** "Deploy your agents to production in next 2 hours"
2. **Docker Containerization** (30 min) - Multi-stage builds
3. **Cloud Run Deployment** (35 min) - **LIVE DEPLOYMENT DEMO!**
4. **Monitoring** (25 min) - Cloud Logging, dashboards
5. **Cost Optimization** (15 min) - Caching, model selection
6. **CI/CD** (10 min) - GitHub Actions example
7. **Exercise:** Deploy greeting_agent to Cloud Run
8. **Solution:** Complete with monitoring
9. **Recap:** "You can now deploy production AI agents!"

### Files Already Exist:
- ✅ Dockerfiles
- ✅ docker-compose.yml

### Need to Create:
- deployment/cloud-run/
- deployment/monitoring/
- .github/workflows/deploy.yml
- slides/module-9-deployment.key
- recording-script/module-9-script.md

**Prep Time:** 2-3 hours (create deployment configs)

---

## 📊 Progress Tracker

**Use this to track daily progress:**

| Day | Module | Status | Recording Time | Notes |
|-----|--------|--------|----------------|-------|
| 1 | Foundation | ⏸️ Not started | Target: 3-4 hrs | Theory, slides-heavy |
| 2 | Python Skills | ⏸️ Not started | Target: 3-4 hrs | Code examples |
| 3 | Single Agents | ⏸️ Not started | Target: 3 hrs | Use greeting_agent |
| 4 | Sequential | ⏸️ Not started | Target: 4 hrs | Longest module |
| 5 | Parallel | ⏸️ Not started | Target: 3.5 hrs | Performance demos |
| 6 | Memory & RAG | ⏸️ Not started | Target: 4 hrs | **Prep needed!** |
| 7 | Tools & MCP | ⏸️ Not started | Target: 4 hrs | **Magic moment!** |
| 8 | Orchestration | ⏸️ Not started | Target: 3.5 hrs | AP2 story |
| 9 | Deployment | ⏸️ Not started | Target: 4 hrs | Live deploy! |

**Update daily:** Change ⏸️ to ✅ when complete!

---

## 🎯 Prep Work Summary (Before Each Day)

### Modules Ready to Record (Minimal Prep):
- ✅ **Day 1:** Module 1 (just need slides)
- ✅ **Day 2:** Module 2 (need code examples - 1 hour prep)
- ✅ **Day 3:** Module 3 (greeting_agent exists!)
- ✅ **Day 4:** Module 4 (all 3 agents exist!)
- ✅ **Day 5:** Module 5 (both agents exist!)
- ✅ **Day 8:** Module 8 (both agents exist!)

### Modules Need Code Creation:
- ⚠️ **Day 6:** Module 6 (ChromaDB example - 2-3 hours prep)
- ⚠️ **Day 7:** Module 7 (financial_advisor_with_search - 1 hour prep)
- ⚠️ **Day 9:** Module 9 (deployment configs - 2 hours prep)

**Strategy:** Do prep work the evening before or morning of recording day.

---

## 🚀 Rapid Prep Guide

### Day 5 Evening (Prep for Day 6):
**Create Memory & RAG examples** (2-3 hours)

```python
# customer_service_with_chromadb/
# Quick ChromaDB integration example

import chromadb
from google.adk.agents import Agent

# Initialize ChromaDB
client = chromadb.Client()
collection = client.create_collection("support_tickets")

# Add memory to customer_service
# Store past tickets, retrieve similar ones
```

**Don't make it perfect - just working example for demo!**

---

### Day 6 Evening (Prep for Day 7):
**Create Google Search example** (1 hour)

```python
# financial_advisor_with_search/
# Add google_search to data_analyst

from google.adk.tools import google_search

data_analyst = Agent(
    model="gemini-2.0-flash",
    tools=[google_search],
    instruction="Use Google Search for current market data..."
)

# This is your MAGIC MOMENT - $175 → real price!
```

---

### Day 8 Evening (Prep for Day 9):
**Create deployment configs** (2 hours)

```bash
# deployment/cloud-run/
# - deploy.sh (gcloud commands)
# - .env.production (environment template)
# - monitoring/ (Cloud Logging queries)

# .github/workflows/
# - deploy.yml (CI/CD pipeline)
```

**Use workshop docker-compose.yml as reference!**

---

## ⏰ Time Management Tips

### If Recording Faster Than Expected:
- ✅ **Great!** Take a break, review footage
- ✅ Get ahead on prep for next module
- ✅ Create extra slides or diagrams

### If Running Behind (over 4 hours):
- ⚠️ **Don't worry** - better quality than rushed
- ⚠️ Skip solution walkthrough (students have written solutions)
- ⚠️ Simplify slides (fewer is OK)
- ⚠️ Extend to 10-11 days if needed

### If Major Issue (demo breaks, need to recode):
- 🚨 **Pause recording**
- 🚨 Fix the issue
- 🚨 Resume next day (skip day, don't force it)
- 🚨 Better to take 12 days than rush broken content

---

## 📦 What You'll Have After 9 Days

### Content:
- ✅ 9 modules recorded (12-14 hours video)
- ✅ Raw footage (ready for editing)
- ✅ All demos working
- ✅ Key concepts explained

### Organization:
- ✅ course-content/ directory with all materials
- ✅ Slides for each module
- ✅ Code examples organized
- ✅ Exercises and solutions

### Next Steps:
- ✅ Editing (can hire editor or do yourself)
- ✅ Platform upload (Gumroad)
- ✅ Launch to workshop students

**You'll be ready to launch in January!**

---

## 🎬 Recording Environment Checklist

### Before Day 1 (Setup Once):
- [ ] Screen recording software installed (OBS, ScreenFlow)
- [ ] Audio tested (clear, no background noise)
- [ ] VS Code theme set (dark, large font 16-18pt)
- [ ] Quiet space confirmed (no interruptions 3-4 hours)
- [ ] Water, coffee, snacks ready
- [ ] Phone on silent

### Before Each Recording Day:
- [ ] Review script (know what you're teaching)
- [ ] Test demos (no surprises!)
- [ ] Fresh mindset (not tired)
- [ ] 3-4 hour block free (no meetings)

### During Recording:
- [ ] High energy (even if tired - coffee helps!)
- [ ] Pace moderate (students follow along)
- [ ] Pause between sections (easier editing)
- [ ] If mistake: "Let me redo that" + 3-second pause

### After Recording:
- [ ] Quick watch (spot major errors)
- [ ] Celebrate! (one module done!)
- [ ] Prep tomorrow's module

---

## 💪 Motivation & Mindset

### Day 1-3: **"This is fun!"**
- Energy high (workshop just succeeded)
- Content fresh (you just taught it)
- Momentum building

### Day 4-6: **"The grind"**
- Novelty wears off
- Might feel repetitive
- **Push through** - you're halfway!

### Day 7-9: **"Almost there!"**
- End in sight
- Best content (tools, deployment)
- Final push to finish line

### Day 10: **"DONE!"**
- 🎉 Celebrate!
- 12-14 hours of content recorded
- Ready for editing phase
- You just created a $300k/year asset

---

## 🎯 Daily Affirmations

**Before recording each day, remind yourself:**

✅ "I'm teaching what I know - I just taught this successfully"
✅ "Pre-edited version is the goal - doesn't need to be perfect"
✅ "One module per day - just focus on today"
✅ "Editing will polish it - just get content recorded"
✅ "This asset will generate revenue for years"

**After each day:**
✅ "One module done! 8 to go!" (or 7, or 6...)
✅ "Progress over perfection"
✅ "I'm building something valuable"

---

## 📋 Master Checklist (Print This!)

**Before Starting (Tonight):**
- [ ] Read COURSE_STRUCTURE.md (complete outline)
- [ ] Read this schedule (9-day plan)
- [ ] Create slides for Module 1 (tonight if possible)
- [ ] Set recording start date
- [ ] Block calendar (3-4 hours/day × 9 days)

**Daily Routine (Repeat 9 times):**
- [ ] Morning: Review script, test demos
- [ ] Recording: 2-3 hours focused work
- [ ] Evening: Review footage, prep tomorrow
- [ ] Update progress tracker
- [ ] Celebrate daily win! 🎉

**After Day 9:**
- [ ] All 9 modules recorded ✅
- [ ] Editing list created
- [ ] Platform setup ready
- [ ] Launch timeline confirmed

---

## 🎁 Support Materials Being Created

I'm creating:
1. ✅ **Course directory structure** (done)
2. ✅ **This 9-day schedule** (done)
3. ⏳ **Detailed recording scripts** (next - one per module)
4. ⏳ **Slide outlines** (next - key points per slide)
5. ⏳ **Code prep checklist** (what to build for Modules 6, 7, 9)

**Want me to create the detailed recording scripts for all 9 modules now?**

Each script will have:
- Exact talking points
- Demo steps
- Transition phrases
- Timing targets

**This way you can just read and record!**

Ready to create those scripts? 🎬
