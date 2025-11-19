# Bonus Content - Instructor Guide

**Duration:** 15-20 minutes (optional, at end of workshop)
**Purpose:** Tease paid Masterclass while providing immediate value
**Format:** Quick demos + "Try this tonight" challenges

---

## 🎯 Delivery Strategy

### Option 1: End of Workshop (if time permits)
- Position: "You've mastered the patterns. Let's see what else ADK can do!"
- Energy: Keep it high-energy, "here's more cool stuff"
- Close: "This is just a taste. Masterclass goes deep on all of this."

### Option 2: Separate "What's Next" Session (15 min)
- After main workshop completion
- Positioned as "bridge" to Masterclass
- More formal masterclass positioning

### Option 3: Pre-Recorded Video (send after workshop)
- Record 4 demos
- Send as follow-up email
- Include Masterclass sign-up link

---

## 📋 Delivery Outline

### Introduction (1 minute)

**Script:**
> "Amazing work today! You've built 9 production-ready agents. But ADK has even MORE
> powerful features we haven't touched yet. Let me show you 4 quick demos that'll
> blow your mind. These are preview features - we go deep on all of them in the
> paid Masterclass."

---

## Demo 1: Google Search Tool (5 minutes)

### Setup (before workshop or during break)

Ensure one agent uses Gemini 2+ model and has google_search imported.

### Live Demo

**Open:** `adk_agents/content_pipeline/agent.py` (or create demo agent)

**Show current code:**
```python
research_agent = Agent(
    model="gemini-2.0-flash-exp",
    instruction="Research topics...",
    # NO TOOLS YET
)
```

**Add google_search:**
```python
from google.adk.tools import google_search

research_agent = Agent(
    model="gemini-2.0-flash",  # Gemini 2+ required
    instruction="Research topics using real-time Google Search",
    tools=[google_search]  # ← ADD THIS
)
```

**Test in ADK Web:**
```
Query: "What are the latest AI agent production patterns from 2024?"
```

**Expected:** Agent performs actual Google Search and cites sources!

**Talking Points:**
- "This is REAL Google Search, not simulated"
- "Gemini 2+ models only (Gemini 1.5 won't work)"
- "Citations automatic, required to display in production"
- "Amazing for research, news, real-time data agents"
- **Masterclass:** "We build complete news agent with search + fact-checking"

---

## Demo 2: Code Execution (5 minutes)

### Live Demo

**Create demo agent (or use existing):**

```python
from google.adk.code_executors import BuiltInCodeExecutor

calculator_agent = Agent(
    model="gemini-2.0-flash",
    name="code_genius",
    instruction="Write and execute Python code to solve problems",
    code_executor=BuiltInCodeExecutor()
)
```

**Test Query 1:** "Calculate compound interest on $10k at 5% for 10 years"

**Agent writes code:**
```python
principal = 10000
rate = 0.05
time = 10
amount = principal * (1 + rate) ** time
print(f"${amount:,.2f}")
```

**Test Query 2:** "Generate a bar chart showing project timeline"

**Agent writes:**
```python
import matplotlib.pyplot as plt
# ... creates chart
```

**Talking Points:**
- "Agent WRITES the code, then EXECUTES it"
- "Can do calculations, data analysis, visualizations"
- "Production: Use GKE Code Executor (sandboxed, secure)"
- **Masterclass:** "We build data analyst that queries BigQuery + generates charts"

---

## Demo 3: Multi-Model Magic (5 minutes)

### Live Demo

**Show model flexibility:**

```python
from google.adk.models.lite_llm import LiteLlm

# Current: Gemini
agent = Agent(model="gemini-2.0-flash-exp", ...)

# Switch to OpenAI GPT-4o
agent = Agent(
    model=LiteLlm(model="openai/gpt-4o"),
    # Everything else stays the same!
)

# Or Anthropic Claude
agent = Agent(
    model=LiteLlm(model="anthropic/claude-3-7-sonnet-latest"),
    # Still works!
)

# Or local Ollama (private, offline)
agent = Agent(
    model=LiteLlm(model="ollama_chat/mistral-small3.1"),
    # Runs on your machine!
)
```

**Test same query on different models:**
```
Query: "Explain quantum computing in simple terms"

Gemini: [Response]
GPT-4o: [Different style response]
Claude: [Different perspective]
```

**Talking Points:**
- "Same agent code, different models"
- "Each model has strengths (GPT-4o reasoning, Claude context, Ollama privacy)"
- "LiteLLM gives access to 100+ models"
- **Masterclass:** "Build orchestrator that routes to best model per task"

---

## Demo 4: Production Deployment (5 minutes)

### Show Deployment Options

**Don't actually deploy (no time), just SHOW the commands:**

#### Cloud Run (Easiest)
```bash
# Build
docker build -t gcr.io/my-project/customer-service .

# Deploy (ONE command)
gcloud run deploy customer-service \
  --image gcr.io/my-project/customer-service \
  --region us-central1

# Result: Production API in 5 minutes
```

**Talking Points:**
- "Cloud Run: 5 minutes to production"
- "Auto-scaling (0 to thousands of users)"
- "HTTPS automatic"

#### GKE (Enterprise)
```bash
# Secure, sandboxed code execution
gke_executor = GkeCodeExecutor(
    namespace="agent-sandbox",
    timeout_seconds=600
)

agent = Agent(
    code_executor=gke_executor  # Production-grade security
)
```

**Talking Points:**
- "GKE: For enterprises needing control"
- "gVisor sandboxing (kernel-level isolation)"
- "Your infrastructure, your rules"

#### Agent Engine (Managed)
```bash
# Fully managed by Google
adk deploy --project=my-project
# Done! Google handles everything
```

**Talking Points:**
- "Agent Engine: Easiest production deployment"
- "Session management, API, monitoring - all automatic"

### Enterprise Features Teaser

**Show Apigee example (don't implement):**

```python
from google.adk.models.apigee_llm import ApigeeLlm

# ALL traffic goes through Apigee governance
governed_model = ApigeeLlm(
    model="apigee/gemini-2.0-flash",
    proxy_url="https://your-apigee.com"
)
```

**Apigee gives you:**
- 🛡️ Model Armor (prevents prompt injection)
- 💰 Token limits (cost control per user)
- ⚡ Semantic caching (80% faster, 99% cheaper)
- 📊 Analytics (who uses what)

**Talking Points:**
- "Enterprise needs governance"
- "Apigee wraps models with security + cost control"
- **Masterclass:** "Set up complete Apigee gateway with policies"

---

## 🎓 Masterclass Positioning

### How to Present It

**DO:**
- ✅ Emphasize value: "Today = patterns. Masterclass = production deployment"
- ✅ Show concrete outcomes: "You'll deploy to Cloud Run with monitoring"
- ✅ Create urgency: "Limited seats, early bird pricing"
- ✅ Offer immediate value: "BONUS_CONTENT.md has try-tonight challenges"

**DON'T:**
- ❌ Hard sell - focus on value
- ❌ Dismiss today's workshop - they learned real patterns
- ❌ Make masterclass sound required - it's next-level, not remedial

### Suggested Positioning

> "Today you learned the patterns - single, sequential, parallel, verification.
> These patterns are EVERYTHING you need to build agents.
>
> The Masterclass is about taking those patterns to PRODUCTION:
> - How to deploy securely to Cloud Run or GKE
> - How to optimize costs with intelligent model routing
> - How to add enterprise governance with Apigee
> - How to implement real BigQuery and RAG integration
>
> You can 100% do that yourself with the docs. The Masterclass gives you a
> guided path, hands-on practice, and production deployment in one day.
>
> Check out BONUS_CONTENT.md - it has quick examples you can try tonight!"

---

## 🎯 Success Metrics for Bonus Section

**Student Feedback:**
- [ ] "Wow, didn't know ADK could do that!"
- [ ] "I want to try google_search tonight"
- [ ] "Interested in the Masterclass"
- [ ] "Clear what the Masterclass offers"

**Deliverables:**
- [ ] Demonstrated 4 advanced features (5 min each)
- [ ] Positioned Masterclass value clearly
- [ ] Gave immediate "try tonight" challenges
- [ ] Collected email sign-ups for Masterclass

---

## 📊 Quick Demo Checklist

Before presenting bonus content:

- [ ] BONUS_CONTENT.md file reviewed
- [ ] One agent ready with google_search (for demo)
- [ ] LiteLLM installed (for model switching demo)
- [ ] Cloud Run deployment command ready (don't execute, just show)
- [ ] Masterclass pricing/sign-up link ready
- [ ] Energy high (this is the exciting "what's next!")

---

## 💰 Masterclass Value Proposition

**Today's Workshop (4 hours - $X):**
- ✅ 9 agent patterns mastered
- ✅ Production-ready code
- ✅ Real business use cases
- ✅ Foundation for everything

**Paid Masterclass (Full day - $XXX):**
- ✅ Deploy to Cloud Run + GKE (hands-on)
- ✅ BigQuery + RAG integration (real databases)
- ✅ Multi-model orchestrator (cost optimization)
- ✅ Apigee governance (enterprise security)
- ✅ Full observability (monitoring, logging, tracing)
- ✅ Production checklist and certification

**ROI Calculation:**
```
Today: $X → Learn patterns
Masterclass: $XXX → Deploy to production

Alternative:
- 40 hours figuring out deployment yourself
- 20 hours on monitoring setup
- 15 hours on cost optimization
= 75 hours × $150/hour = $11,250

Masterclass: 6 hours × guided expertise = $XXX
Savings: $10,000+ in implementation time
```

**Position as investment, not cost.**

---

## 🎁 Post-Workshop Follow-Up

### Email Template (send same day)

**Subject:** 🎉 Workshop Complete + Bonus Content Inside!

**Body:**

> Hi [Name],
>
> Amazing work today! You built 9 production-ready AI agents - that's incredible.
>
> **Three things for you:**
>
> 1. **Bonus Content:** Check out BONUS_CONTENT.md in the repo
>    - Google Search integration (2 min to add)
>    - Multi-model strategies (try GPT-4o or Claude)
>    - Production deployment guide
>    - Try these tonight!
>
> 2. **Git Tags:** All 9 steps are tagged
>    ```bash
>    git tag --list  # See all checkpoints
>    git checkout step-5-financial-advisor  # Review any step
>    ```
>
> 3. **Masterclass Preview:** We're running a full-day deep dive:
>    - Production deployment (Cloud Run + GKE)
>    - BigQuery + RAG integration
>    - Multi-model orchestration
>    - Enterprise governance (Apigee)
>
>    [EARLY BIRD SIGN-UP LINK]
>    Limited to 20 participants, 30% off if you register this week.
>
> Questions? Reply to this email!
>
> Thanks for being an amazing participant!
>
> [Your name]

---

**Instructor: You're ready to deliver the bonus content and position the Masterclass!**
