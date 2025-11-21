# Ultimate AI Agents Masterclass - Complete Course Structure

**Total Duration:** 12-14 hours
**Modules:** 9
**Recording Plan:** 1 module per day × 9 days
**Target:** Pre-edited version ready in 9 days

---

## 📁 Directory Structure

```
course-content/
├── COURSE_STRUCTURE.md           ← This file (master outline)
├── RECORDING_SCHEDULE_9DAYS.md   ← Daily recording plan
├── _templates/                    ← Reusable slide templates
│   ├── slide-template.key
│   ├── intro-slide.png
│   └── outro-slide.png
│
├── module-1-foundation/
│   ├── recording-script/
│   │   ├── 01-hook.md            ← First 30 seconds (hook)
│   │   ├── 02-overview.md        ← Module overview
│   │   ├── 03-content.md         ← Main teaching content
│   │   ├── 04-demo.md            ← Demo walkthrough
│   │   └── 05-recap.md           ← Summary and next preview
│   ├── slides/
│   │   └── module-1-slides.key   ← Keynote/PowerPoint
│   ├── exercises/
│   │   ├── README.md             ← Exercise instructions
│   │   └── starter-code/         ← Starter files
│   ├── solutions/
│   │   └── complete-code/        ← Full solution
│   └── assets/
│       └── diagrams/             ← Architecture diagrams
│
├── module-2-python/
│   └── [same structure]
│
├── module-3-single-agents/
│   └── [same structure]
│
... [modules 4-9 follow same pattern]
```

---

## 🎬 Module Breakdown (Recording Format)

### Each Module Has 6 Parts:

1. **Hook (30 sec):**
   - "By end of this module, you'll..."
   - Creates anticipation

2. **Overview (2-3 min):**
   - What we're covering
   - Why it matters
   - Learning objectives

3. **Content (60-90 min):**
   - Teaching with code demos
   - Architecture explanations
   - Best practices
   - Common pitfalls

4. **Exercise Introduction (5 min):**
   - "Now you try..."
   - Clear instructions
   - Expected outcome

5. **Solution Walkthrough (10-15 min):**
   - Step-by-step solution
   - Explain the "why" not just "what"
   - Alternative approaches

6. **Recap & Next (3 min):**
   - What you learned
   - How it connects to next module
   - Call to action

**Total per module:** 90-120 minutes content = 2-3 hours recording (with retakes)

---

## 📊 Complete Module Outline

### MODULE 1: The Modern AI Agent Stack (90 min)
**Day 1 of recording**

**Learning Objectives:**
- Understand AI agents vs LLMs vs chatbots
- Compare ADK vs LangChain vs CrewAI
- Set up development environment
- Get API keys and verify setup

**Content Sections:**
1. What is an AI Agent? (15 min)
   - LLM: Language model (base capability)
   - Chatbot: LLM + conversation memory
   - Agent: LLM + tools + reasoning + autonomy
   - Examples: ChatGPT (chatbot) vs AutoGPT (agent)

2. The Google AI Ecosystem (20 min)
   - Gemini API vs Vertex AI (when to use which)
   - ADK: Google's agent framework
   - Why ADK for enterprise (vs LangChain)

3. Framework Comparison (25 min)
   - ADK: Google-native, production-ready
   - LangChain: Flexibility, many integrations
   - CrewAI: Role-based, opinionated
   - AutoGen: Microsoft, multi-agent conversations
   - Decision matrix: Which framework for which use case

4. Environment Setup (20 min)
   - Python 3.11+ installation
   - Virtual environment best practices
   - ADK installation
   - Getting Gemini API key
   - Verifying setup with "adk --version"

5. ADK Web Introduction (10 min)
   - Built-in development UI
   - How to use it for testing
   - Events tab, State tab, Artifacts tab

**Exercise:** Install ADK and verify setup
**Solution:** Walkthrough of common installation issues

**Slides Needed:**
- AI agent landscape diagram
- Framework comparison matrix
- Google ecosystem overview
- Setup checklist

---

### MODULE 2: Python for Production Agents (90 min)
**Day 2 of recording**

**Learning Objectives:**
- Master async/await for agents
- Use Pydantic for structured output
- Write production-ready type hints
- Handle errors gracefully

**Content Sections:**
1. Async/Await Explained (30 min)
   - Why agents need async (concurrent execution)
   - Sync vs async code examples
   - Common pitfalls (blocking the event loop)
   - When to use async vs sync

2. Pydantic Models (25 min)
   - Structured output from LLMs
   - Data validation
   - Type safety
   - Real example: Customer support ticket model

3. Type Hints in Production (20 min)
   - Why they matter (not just documentation)
   - Tool function signatures
   - IDE autocomplete benefits
   - Runtime type checking

4. Error Handling Patterns (15 min)
   - Try/except in agent tools
   - Graceful degradation
   - User-friendly error messages
   - Logging best practices

**Exercise:** Build async function with Pydantic model
**Solution:** Complete customer data validator

**Slides Needed:**
- Async vs sync flow diagram
- Pydantic validation example
- Type hints benefits
- Error handling patterns

---

### MODULE 3: Single Agents with Custom Tools (90 min)
**Day 3 of recording**
*Maps to workshop Step 1*

**Learning Objectives:**
- Build first ADK agent
- Create custom Python function tools
- Write effective instructions
- Test with ADK Web
- Enable voice input

**Content Sections:**
1. Agent Class Structure (20 min)
   - name, model, description, instruction, tools
   - Each parameter explained
   - Why instructions matter (shapes behavior)

2. Building greeting_agent (30 min)
   - Step-by-step code walkthrough
   - Creating get_company_info tool
   - Creating get_current_time tool
   - Tool signatures and docstrings

3. Testing Strategies (15 min)
   - ADK Web UI walkthrough
   - Events tab (see tool calls)
   - run_debug() helper (quick testing)
   - Debugging common issues

4. Voice Input Feature (10 min)
   - ADK 1.18 feature
   - Which models support it
   - When to use voice
   - Limitations (only simple agents)

5. Production Patterns (15 min)
   - When to use single agents
   - Tool design best practices
   - Instruction engineering tips

**Exercise:** Customize company_info, add team_members tool
**Solution:** Complete greeting_agent with 3 tools

**Slides Needed:**
- Agent architecture diagram
- Tool function anatomy
- Instruction engineering tips
- Voice input demo

**Code Files:**
- adk_agents/greeting_agent/ (already exists!)

---

### MODULE 4: Sequential Workflows (120 min)
**Day 4 of recording**
*Maps to workshop Steps 2-4*

**Learning Objectives:**
- Build SequentialAgent workflows
- Understand state passing
- Implement decision gates
- Handle compliance workflows

**Content Sections:**
1. When to Use Sequential (15 min)
   - Dependent tasks (A needs B's output)
   - Examples: Triage → Research → Respond
   - Sequential vs Parallel decision matrix

2. Building customer_service Agent (35 min)
   - 3-agent workflow: triage → research → respond
   - State passing (automatic via history)
   - Testing sequential execution
   - Debugging with Events tab

3. Pattern Reuse: content_pipeline (25 min)
   - Same Sequential pattern, different domain
   - 4-agent workflow: research → draft → optimize → publish
   - Domain adaptation strategies

4. Decision Gates: medical_authorization (30 min)
   - Conditional execution (workflow can stop early)
   - Validation at each stage
   - Compliance and audit requirements
   - Real-world healthcare example

5. Sequential Best Practices (15 min)
   - When to stop workflow early
   - Error handling in workflows
   - Performance considerations
   - Production deployment tips

**Exercise:** Build 3-agent support workflow
**Solution:** Complete customer_service with escalation logic

**Slides Needed:**
- Sequential workflow diagram
- State passing visualization
- Decision gate flowchart
- Pattern reusability examples

**Code Files:**
- adk_agents/customer_service/
- adk_agents/content_pipeline/
- adk_agents/medical_authorization/

---

### MODULE 5: Parallel Execution & Synthesis (120 min)
**Day 5 of recording**
*Maps to workshop Steps 5-6*

**Learning Objectives:**
- Build ParallelAgent systems
- Understand when Parallel > Sequential
- Implement synthesis patterns
- Measure performance gains

**Content Sections:**
1. The Paradigm Shift (15 min)
   - Dependent vs Independent tasks
   - When Parallel makes sense
   - Performance benefits (4x faster demo!)
   - Real-world use cases

2. Building financial_advisor (40 min)
   - 4 parallel analysts: data, trading, execution, risk
   - Why these are independent
   - Synthesis agent combines perspectives
   - Testing parallel execution (timestamps!)

3. Pattern Reuse: brand_intelligence (25 min)
   - Same Parallel pattern, different domain
   - 4 researchers: news, social, trends, competitors
   - Multi-source intelligence gathering

4. Synthesis Patterns (25 min)
   - Why synthesis is critical
   - Combining diverse outputs
   - Resolving conflicts between analysts
   - Creating cohesive recommendations

5. Performance Optimization (15 min)
   - Measuring parallel vs sequential
   - When to use Parallel
   - Cost implications (more API calls)
   - Production considerations

**Exercise:** Add 5th analyst to financial_advisor
**Solution:** sentiment_analyst integrated into workflow

**Slides Needed:**
- Sequential vs Parallel comparison
- Performance benchmark graphs
- Parallel execution timeline
- Synthesis pattern diagram

**Code Files:**
- adk_agents/financial_advisor/
- adk_agents/brand_intelligence/

---

### MODULE 6: Memory & Context Management (120 min)
**Day 6 of recording**
*NEW content - premium value*

**Learning Objectives:**
- Implement session memory (Redis)
- Add long-term memory (Vector DB)
- Build RAG systems
- Manage agent context

**Content Sections:**
1. Memory Types (15 min)
   - Session memory: Redis (short-term)
   - Long-term memory: Vector DB (semantic)
   - When agents need to remember

2. Redis Session Memory (25 min)
   - Workshop already uses Redis
   - Session state management
   - Conversation history
   - Practical demo

3. Vector Databases for Semantic Memory (40 min)
   - ChromaDB or Pinecone setup
   - Embedding generation
   - Semantic search
   - RAG pattern implementation

4. RAG Deep Dive (30 min)
   - Retrieval-Augmented Generation explained
   - Document ingestion pipeline
   - Query → Retrieve → Generate pattern
   - Production examples

5. Context Window Management (10 min)
   - Token limits and costs
   - Summarization strategies
   - What to remember vs forget

**Exercise:** Add ChromaDB to customer_service agent
**Solution:** Agent remembers past support tickets

**Slides Needed:**
- Memory types comparison
- RAG architecture diagram
- Vector database workflow
- Context management strategies

**Code Files:**
- NEW: customer_service_with_memory/
- ChromaDB integration example
- RAG pipeline code

---

### MODULE 7: Production Tools & Integration (120 min)
**Day 7 of recording**
*Maps to workshop Step 7 + Bonus content*

**Learning Objectives:**
- Use Gemini built-in tools
- Integrate MCP for databases
- Connect to external services
- Use multi-model strategies

**Content Sections:**
1. Gemini Built-In Tools (30 min)
   - Google Search (real-time data!) - **THE $100 STOCK FIX**
   - Code Execution (calculations, charts)
   - BigQuery tools (natural language → SQL)
   - Limitations and workarounds

2. MCP (Model Context Protocol) (35 min)
   - What is MCP
   - MCP Toolbox for PostgreSQL
   - GitHub MCP Server
   - Building custom MCP servers

3. LangChain Tools Integration (20 min)
   - Stack Overflow API
   - Third-party tool libraries
   - Adapters for external APIs

4. Multi-Model Strategies (25 min)
   - Using OpenAI GPT-4o via LiteLLM
   - Using Anthropic Claude
   - Using Ollama (local/privacy)
   - Fallback chains

5. Real-World Integration (10 min)
   - Database connections
   - API rate limiting
   - Error handling
   - Cost considerations

**Exercise:** Add Google Search to financial_advisor
**Solution:** Real-time stock data agent

**Slides Needed:**
- Built-in tools overview
- MCP architecture
- Multi-model comparison
- Integration patterns

**Code Files:**
- adk_agents/software_assistant/ (MCP examples)
- financial_advisor_with_search/ (NEW)
- multi_model_example/ (NEW)

---

### MODULE 8: Complex Orchestration (120 min)
**Day 8 of recording**
*Maps to workshop Steps 8-9*

**Learning Objectives:**
- Combine Sequential + Parallel patterns
- Use Agent-to-Agent (A2A) patterns
- Build verification systems
- Create audit trails

**Content Sections:**
1. Complex Orchestration Patterns (20 min)
   - When to combine Sequential + Parallel
   - project_management example
   - A2A pattern (agents calling agents as tools)

2. Building project_management (30 min)
   - Task breakdown → Parallel analysis → Synthesis
   - Sequential outer, Parallel inner
   - Real project planning demo

3. Verification & Accountability (35 min)
   - AP2-inspired patterns (Ayo's charity advisor)
   - Independent verification
   - Role separation for security
   - Building verified_recommendations agent

4. Audit Trails & Compliance (25 min)
   - Why audit trails matter
   - BigQuery logging (ADK 1.18)
   - Session rewind for debugging
   - Cryptographic verification

5. Production Security (10 min)
   - Input validation
   - Output sanitization
   - Secrets management
   - Rate limiting

**Exercise:** Add audit logging to medical_authorization
**Solution:** Complete audit trail with BigQuery

**Slides Needed:**
- Complex orchestration diagram
- AP2 architecture
- Audit trail flow
- Security checklist

**Code Files:**
- adk_agents/project_management/
- adk_agents/verified_recommendations/

---

### MODULE 9: Cloud Deployment & Operations (120 min)
**Day 9 of recording**
*NEW content - enterprise value*

**Learning Objectives:**
- Containerize agents with Docker
- Deploy to Cloud Run
- Set up monitoring and logging
- Implement CI/CD pipelines

**Content Sections:**
1. Docker Containerization (30 min)
   - Multi-stage builds (optimize image size)
   - Environment variables and secrets
   - docker-compose for local testing
   - Container best practices

2. Cloud Run Deployment (35 min)
   - Why Cloud Run (serverless, auto-scaling)
   - Deploying customer_service agent (live!)
   - Custom domains and HTTPS
   - Environment configuration

3. Monitoring & Observability (30 min)
   - Cloud Logging integration
   - Cloud Monitoring metrics
   - Custom dashboards
   - Cost tracking and alerts

4. Cost Optimization (15 min)
   - Semantic caching (80% savings!)
   - Model selection strategies
   - Request batching
   - Apigee AI Gateway intro

5. CI/CD Pipeline (10 min)
   - GitHub Actions example
   - Automated testing
   - Deployment automation
   - Rollback strategies

**Exercise:** Deploy greeting_agent to Cloud Run
**Solution:** Complete deployment with monitoring

**Slides Needed:**
- Docker multi-stage diagram
- Cloud Run architecture
- Monitoring dashboard examples
- CI/CD pipeline flow

**Code Files:**
- Dockerfiles (already have these!)
- deployment/ configs
- monitoring/ dashboard configs

---

## 🎯 Course Learning Path

```
Module 1: Foundation
    ↓ (You understand the landscape)
Module 2: Python Skills
    ↓ (You can write production Python)
Module 3: Single Agents
    ↓ (You've built your first agent)
Module 4: Sequential Workflows
    ↓ (You can build multi-step processes)
Module 5: Parallel Execution
    ↓ (You can optimize for speed)
Module 6: Memory & RAG
    ↓ (Your agents remember and learn)
Module 7: Production Tools
    ↓ (Your agents access real-time data)
Module 8: Complex Orchestration
    ↓ (You can build enterprise systems)
Module 9: Cloud Deployment
    ↓ (You can deploy to production)

OUTCOME: You build enterprise AI agent systems
```

---

## 📝 What Already Exists (Huge Head Start!)

### From Workshop Materials:

✅ **All 9 agents** in `adk_agents/`
- Code complete
- READMEs comprehensive
- Production-ready

✅ **Exercises** in `.workshop/exercises/step-1/`
- Can expand for all modules

✅ **Solutions** in `.workshop/solutions/step-1/`
- Can expand for all modules

✅ **Documentation** (6,000+ lines)
- Can repurpose for course scripts

✅ **Progression system**
- Maps perfectly to modules

✅ **Bonus content**
- Becomes Module 7 material

**What You Need to Create:**
- Recording scripts (detailed talking points)
- Slides (architecture diagrams, key concepts)
- Modules 6 additions (Memory/RAG code)
- Module 9 additions (Deployment configs)

**Estimate:** 30-40% of content already exists! Just needs formatting for course.

---

## ⏱️ 9-Day Recording Schedule

### Recording Intensity Options:

**Option A: "Sprint Mode" (3-4 hrs/day)**
- Day 1: Module 1
- Day 2: Module 2
- Day 3: Module 3
- Day 4: Module 4
- Day 5: Module 5
- Day 6: Module 6 (need to code examples first)
- Day 7: Module 7
- Day 8: Module 8
- Day 9: Module 9

**Total:** 9 days × 3-4 hours = 27-36 hours recording

**Option B: "Sustainable Pace" (2-3 hrs/day + weekend)**
- Weekdays: 2-3 hours recording per day
- Weekends: 4-6 hours (catch up, create missing code examples)
- **Total:** Still 9 days, less burnout

---

## 🎬 Daily Recording Template

**Each day follows same pattern:**

### Morning (Prep - 30 min):
1. Review recording script
2. Open code files needed
3. Test demos work
4. Set up screen recording

### Recording Session (2-3 hours):
1. Record intro/hook (5 min)
2. Record content sections (90 min)
3. Record exercise intro (5 min)
4. Record solution walkthrough (15 min)
5. Record recap (5 min)

### Evening (Review - 30 min):
1. Watch recording (spot major errors)
2. Note retakes needed
3. Prepare for next day

**Total daily commitment:** 3-4 hours

---

## 🎥 Recording Best Practices

### Setup:
- **Screen:** VS Code (left) + Running app (right)
- **Font:** 16-18pt (readable in 1080p)
- **Theme:** Dark (easier on eyes)
- **Audio:** Close to mic, quiet room
- **Slides:** Picture-in-picture or separate segments

### During Recording:
- **Energy:** High at start, maintain throughout
- **Pace:** Moderate (not too fast, students follow along)
- **Pauses:** Pause between sections (easier editing)
- **Mistakes:** Say "Let me redo that" and pause 3 seconds (easy to cut)
- **Code:** Type slowly, explain as you code

### Quality Checks:
- **Audio clear:** No background noise, consistent volume
- **Video clear:** Code readable, UI visible
- **Content clear:** Explanations make sense
- **Demos work:** Test before recording (but real mistakes OK, shows debugging)

---

## 📦 Deliverables by End of Day 9

### Content:
- [ ] 9 modules recorded (pre-edited, 12-14 hours total)
- [ ] All code examples working
- [ ] Exercises created for each module
- [ ] Solutions complete

### Organization:
- [ ] All files in course-content/ directory structure
- [ ] Recording scripts completed (reference for editing)
- [ ] Slides created (export as PDF for students)

### Next Steps Ready:
- [ ] Editing list (where to cut, what to polish)
- [ ] Missing content identified (if any)
- [ ] Platform upload ready (files organized)

---

## 🎯 Success Criteria for 9-Day Sprint

**Minimum Viable (Good enough to edit):**
- [ ] All 9 modules recorded (even if imperfect)
- [ ] Audio clear (no major issues)
- [ ] Demos work (core functionality shown)
- [ ] Key concepts explained

**Ideal (Polish later):**
- [ ] Smooth delivery (few retakes needed)
- [ ] All slides complete
- [ ] Professional transitions
- [ ] Perfect code demos

**Remember:** Pre-edited version is the goal. Editing will polish it later!

---

## 💪 You Can Do This!

**You have:**
- ✅ All content mapped out (9 agents = 9 modules)
- ✅ Energy and momentum (workshop just succeeded!)
- ✅ Proven teaching ability (40 engaged students)
- ✅ Production code ready (9 agents complete)

**9 days = 1 module per day**

**That's it. Just repeat the teaching you did today, but recorded.**

**Ready to start tonight? Let's create the detailed recording scripts and slide outlines next!**
