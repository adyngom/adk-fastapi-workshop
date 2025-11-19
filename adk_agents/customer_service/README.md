# Customer Service Agent

**Step 2 of 9** | **Duration:** 30 minutes | **Difficulty:** Intermediate

## Overview

A 3-agent Sequential workflow that automates customer support ticket handling. Demonstrates how agents pass state through a multi-step process: triage → research → respond.

This is the first step beyond single agents - you'll learn how to compose multiple specialized agents into a coordinated workflow.

## Learning Objectives

By completing this agent, you will understand:

- ✅ **SequentialAgent Pattern** - How to chain multiple agents in sequence
- ✅ **State Passing** - How context flows from one agent to the next
- ✅ **Sub-Agent Composition** - Combining specialized agents into workflows
- ✅ **Role-Based Architecture** - Each agent has a specific responsibility
- ✅ **output_key Usage** - Exposing intermediate results (optional)

## Pattern Demonstrated

**Sequential Multi-Agent Workflow**

```
customer_service (SequentialAgent)
├── triage_agent (Agent)
│   └── Role: Categorize & prioritize issue
│   └── Output: {category, priority, key_details}
│
├── research_agent (Agent)
│   └── Role: Find solutions from KB/past tickets
│   └── Output: {solutions, workarounds, escalation}
│
└── response_agent (Agent)
    └── Role: Generate empathetic customer response
    └── Output: Complete email/message to customer
```

**Key Concept:** Each agent receives the output of the previous agent automatically. The final agent's output is what the user sees.

## Business Value

Real-world impact:
- **70% reduction** in support response time
- **Consistent quality** - every ticket gets thorough research
- **24/7 availability** - automated triage even outside business hours
- **Knowledge retention** - captures solutions for future tickets
- **Scalability** - handles volume spikes without adding headcount

Use cases:
- SaaS customer support
- E-commerce order issues
- Technical product support
- Account management

## ADK 1.18+ Features

### Visual Agent Builder
- **Available:** ✅
- **Usage:** Instructor can demo building this 3-agent workflow using natural language in Visual Agent Builder
- **Benefit:** See how "Build a support workflow with triage, research, and response agents" → complete Sequential Agent

### run_debug() Helper
- **Available:** ✅
- **Usage:** Test each sub-agent independently before composing
  ```python
  from google.adk import run_debug

  # Test triage agent alone
  run_debug(triage_agent, "Customer can't login after password reset")

  # Test research agent alone (with mock triage output)
  run_debug(research_agent, '{"category": "technical", "priority": "P1"}')
  ```

### Callback Management
- **Available:** ✅
- **Usage:** Log each sequential step for debugging
  ```python
  def after_agent_callback(agent_name, result):
      print(f"✓ {agent_name} completed")
      print(f"  Output: {result[:100]}...")  # First 100 chars

  root_agent.after_agent_callback = after_agent_callback
  ```

## Architecture

### Workflow Flow

```
User Input: "I can't login to my account. I reset my password but still getting 'invalid credentials' error."

    ↓

[TRIAGE AGENT]
Analyzes issue → Assigns P1 priority → Category: Technical
Output: {
    "category": "technical",
    "priority": "P1",
    "summary": "Login failure post password reset",
    "key_details": {
        "product": "authentication system",
        "error": "invalid credentials",
        "impact": "user completely blocked"
    }
}

    ↓

[RESEARCH AGENT]
Searches KB → Finds: "Password reset requires session clear"
Output: {
    "recommended_solution": "Clear browser cache and cookies, then try login",
    "knowledge_base_articles": [
        {"title": "Password Reset Best Practices", "url": "..."}
    ],
    "escalate": false
}

    ↓

[RESPONSE AGENT]
Crafts empathetic response → Provides step-by-step solution
Output: "Hi! Thanks for reaching out. I understand how frustrating it is to be locked out...
         Here's what should fix this: 1. Clear your browser cache... 2. Try logging in again..."

    ↓

User receives complete, helpful response
```

### Agent Responsibilities

| Agent | Input | Processing | Output |
|-------|-------|------------|--------|
| **Triage** | Raw customer message | Categorize + prioritize | Structured issue summary |
| **Research** | Issue summary | Search KB + past tickets | Solutions + workarounds |
| **Response** | Issue + solutions | Craft empathetic message | Ready-to-send response |

## Files

```
customer_service/
├── agent.py          # 3 sub-agents + SequentialAgent root
├── .env              # API key (GOOGLE_API_KEY)
├── __init__.py       # Package marker
└── README.md         # This file
```

## Setup

### Prerequisites

- Completed Step 1 (greeting_agent)
- ADK 1.18+ installed
- Google Gemini API key

### Configuration

API key is shared with greeting_agent - uses root `.env` by default.

If you want agent-specific config:
```bash
cp .env.example .env
# Add your GOOGLE_API_KEY
```

## Running the Agent

### Option 1: ADK Web UI

```bash
# From project root
adk web
```

- Select "customer_service" from dropdown
- Watch each agent execute in sequence
- See intermediate outputs in "Events" tab

### Option 2: Streamlit Workshop UI

```bash
streamlit run streamlit_apps/workshop_ui/app.py --server.port 8501
```

- Select "Customer Service" from sidebar
- More user-friendly for demos
- Shows final response (hides internal workflow)

### Option 3: run_debug() Quick Test

```bash
python -c "
from google.adk import run_debug
from adk_agents.customer_service.agent import root_agent

run_debug(root_agent, 'Customer cant login after password reset')
"
```

## Example Interactions

### Example 1: Technical Issue (P1)

**User:**
```
Hi, I'm trying to export my data but keep getting a timeout error.
I've been trying for 2 hours and have a deadline tomorrow. Please help!
```

**Triage Output:**
```json
{
  "category": "technical",
  "priority": "P1",
  "summary": "Data export timeout preventing user from meeting deadline",
  "key_details": {
    "product": "data export feature",
    "error": "timeout",
    "impact": "blocking work, time-sensitive"
  }
}
```

**Research Output:**
```json
{
  "recommended_solution": "Export in smaller batches (max 10k rows per export)",
  "workaround": "Use API endpoint /api/export with pagination",
  "knowledge_base_articles": [
    {"title": "Large Dataset Export Best Practices"}
  ],
  "escalate": false
}
```

**Final Response:**
```
Hi there! I completely understand the urgency - deadline pressure is stressful!

Here's what's happening: Our export feature times out on very large datasets
(typically >50k rows). This is a known limitation we're actively working on.

IMMEDIATE SOLUTION:
1. Break your export into smaller batches (10k rows max):
   - Filter by date range, then export each week separately
   - Or export by category/department

2. FASTER option - use our API:
   GET /api/export?start=0&limit=10000
   (I can send detailed API docs if helpful)

This should get you the data within 30 minutes. If you hit any issues, reply
immediately and I'll personally make sure you get your export before your deadline.

Would you like the API documentation, or prefer to stick with the batch export approach?
```

### Example 2: Billing Question (P2)

**User:**
```
I was charged twice this month. Can you explain why?
```

**Triage:**
- Category: billing
- Priority: P2 (not blocking, but money involved)

**Research:**
- Finds: "Mid-month plan upgrades result in prorated charges"
- Checks: User upgraded plan on March 15

**Response:**
```
Hi! I can explain what happened with your billing.

I see you upgraded from Basic to Pro on March 15. Here's the breakdown:

Charge 1 ($29): Your original Basic plan for March 1-31
Charge 2 ($45): Prorated Pro plan for March 15-31 (16 days)

Next month (April), you'll only see one charge of $89 for the full Pro plan.

The double charge this month is normal when upgrading mid-cycle - you're
paying for both the Basic plan you used, plus the Pro features for the
remainder of the month.

Does that make sense? Happy to clarify further!
```

## Exercises

See `.workshop/exercises/step-2/` for hands-on exercises:

1. **Add escalation detection** - Insert 4th agent that flags when to involve humans
2. **Track customer_id** - Pass customer context through all agents
3. **Add sentiment analysis** - Detect angry customers and adjust response tone

Solutions available in `.workshop/solutions/step-2/`

## Success Criteria

Before moving to Step 3, verify:

- [ ] All 3 agents execute in correct sequence
- [ ] Triage agent categorizes issues correctly
- [ ] Research agent provides relevant solutions
- [ ] Response agent crafts helpful messages
- [ ] State flows properly between agents (check Events tab)
- [ ] Tested with at least 3 different issue types

## Common Issues

### Agents Not Running in Sequence

**Problem:** Only seeing response_agent output, skipping triage/research

**Solution:**
- SequentialAgent runs all sub-agents but only returns final output
- Check "Events" tab in ADK Web to see all intermediate steps
- Each sub-agent runs sequentially, but output might not show in chat

### State Not Passing Between Agents

**Problem:** Research agent doesn't seem to use triage output

**Solution:**
- Sequential agents automatically pass context
- Previous agent outputs are in conversation history
- If research agent ignores triage, improve its instruction to explicitly look for triage data

### Response Too Generic

**Problem:** Final response doesn't reference specific issue details

**Solution:**
- Response agent should reference both triage AND research outputs
- Update response agent instruction to say: "Review the triage analysis and research findings before crafting response"

## Understanding Sequential Workflows

**Key Concepts:**

1. **Automatic Context Passing**
   - Each agent sees the entire conversation history
   - Previous agent outputs are part of that history
   - No manual state management needed

2. **Final Output Only**
   - User sees only the last agent's response
   - Intermediate outputs are in the background
   - Use ADK Web "Events" to debug

3. **Agent Specialization**
   - Each agent is an expert in ONE thing
   - Triage doesn't try to solve - just categorizes
   - Research doesn't write responses - just finds solutions
   - Response doesn't research - just writes

4. **When to Use Sequential**
   - Multi-step processes (approve → process → notify)
   - Pipelines (collect → validate → transform)
   - Handoffs (triage → assign → execute)

## Next Steps

Once you've completed the exercises and verified all success criteria, proceed to:

**Step 3: Content Creation Pipeline**

Preview: Same Sequential pattern, different domain. You'll build researcher → drafter → optimizer → publisher workflow. Plus: integrate Google Search tool!

## Debugging Tips

### Test Individual Agents

```python
from google.adk import run_debug
from adk_agents.customer_service.agent import triage_agent, research_agent, response_agent

# Test triage alone
run_debug(triage_agent, "Customer can't export data")

# Test research (mock previous triage output)
mock_triage = '{"category": "technical", "priority": "P1", "summary": "Data export timeout"}'
run_debug(research_agent, mock_triage)
```

### Add Logging

```python
def log_agent_completion(agent_name, result):
    print(f"\n{'='*50}")
    print(f"Agent: {agent_name}")
    print(f"{'='*50}")
    print(result)
    print(f"{'='*50}\n")

root_agent.after_agent_callback = log_agent_completion
```

### Check Events Tab

In ADK Web:
1. Submit a query
2. Click "Events" tab
3. Expand each agent execution
4. See exactly what each agent received and produced

## References

- [ADK Documentation - Sequential Agents](https://google.github.io/adk-docs/agents/sequential/)
- [Workshop Progression](../../workshop_progression.yaml) - Full roadmap
- [ADK Samples - Customer Service](https://github.com/google/adk-samples/tree/main/python/agents/customer-service) - Production example
- [Step 1 - Greeting Agent](../greeting_agent/README.md) - Previous step

---

**Tags:** `step-2-customer-service`, `intermediate`, `sequential-agent`, `multi-agent-workflow`
