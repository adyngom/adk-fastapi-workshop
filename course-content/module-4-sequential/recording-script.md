# Module 4: Sequential Workflows - Recording Script

**Duration:** 120 minutes (longest module!)
**Recording Time:** 4-5 hours
**Energy:** Moderate to high (this is exciting!)
**Focus:** Multi-agent workflows

---

## 🎬 HOOK (30 sec)

**SAY:**
"Hello and welcome to Module 4. Okay, so this is where agents become really powerful - we're going to build multi-agent workflows that automate entire business processes.

By the end of this module, you'll have built three different Sequential workflows: a customer service system, a content creation pipeline, and a medical authorization workflow. These are real production patterns you can use in your business.

Let's build this!"

---

## 🎬 OVERVIEW (3 min)

**SAY:**
"All right, here's what we're covering. This is a big module - we're going from single agents to multi-agent systems.

First, I'm going to show you when to use Sequential workflows. There's a decision matrix - dependent tasks use Sequential, independent tasks use Parallel. We'll make this very clear.

Then we're going to build the customer service agent together - three agents working in sequence: triage, then research, then respond. I'm going to code this live with you.

After that, we'll look at the content creation pipeline - same Sequential pattern, but different business domain. This shows you how the pattern transfers.

And finally, medical authorization with decision gates - where the workflow can stop early if validation fails. This is important for production.

By the end, you'll master Sequential workflows. Okay, let's start with the fundamental question: When do you use Sequential?"

---

## 🎬 WHEN TO USE SEQUENTIAL (15 min)

**[Show slide: Sequential vs Parallel Decision Matrix]**

**SAY:**
"So let me show you when to use Sequential workflows. The rule is simple: If task B needs task A's output, use Sequential.

Examples of Sequential workflows:
- **Customer support:** Triage the issue, THEN research solutions, THEN write response
  - Why Sequential? Research needs to know the category and priority from triage
  - Why not Parallel? Can't research before you know what you're researching!

- **Content creation:** Research topic, THEN write draft, THEN optimize
  - Why Sequential? Draft needs research data
  - Why not Parallel? Can't write about something you haven't researched

- **Medical authorization:** Intake data, THEN verify eligibility, THEN medical review
  - Why Sequential? Can't verify eligibility without patient data
  - Why not Parallel? Each step depends on the previous

You see the pattern? **Dependent tasks = Sequential.**

Now contrast with Parallel (we'll cover this in Module 5):
- **Financial analysis:** Four analysts can all analyze the same stock at the same time
  - Why Parallel? All looking at same data, tasks are independent
  - Why not Sequential? No reason to wait

All right, so that's the decision. If tasks depend on each other, use Sequential. Got it? Perfect.

Now let's build our first Sequential workflow - customer service."

---

## 🎬 BUILDING CUSTOMER_SERVICE (35 min)

**[Fresh VS Code]**

**SAY:**
"Okay, so let's build a customer service system from scratch. This is going to be three agents: triage, research, and response.

Let me create the folder structure:
[Type: mkdir customer_service]
[Type: cd customer_service]
[Type: touch __init__.py agent.py .env]

There you go.

Now, here's the pattern: We're going to define three separate Agent objects, then wrap them in a SequentialAgent. Let me show you:

[Open agent.py]

So I'm just going to start with the imports:
[Type:
```python
'''
Customer Service - 3-agent Sequential workflow
'''
from google.adk.agents import Agent, SequentialAgent
```
]

We need both Agent (for sub-agents) and SequentialAgent (the wrapper). Perfect.

All right, now let's build the first agent - triage. This agent categorizes and prioritizes customer issues:

[Type:
```python

# ============================================================
# SUB-AGENT 1: Triage Agent
# ============================================================

triage_agent = Agent(
    name='triage_agent',
    model='gemini-2.0-flash-exp',
    description='Analyzes customer issues and assigns priority',
    instruction='''You are a customer service triage specialist.

Your role:
1. Analyze the customer's issue
2. Categorize it (technical, billing, product, account, other)
3. Assign priority:
   - P0 (Critical): Service outage, security breach
   - P1 (High): Major functionality broken, payment issues
   - P2 (Medium): Feature not working as expected
   - P3 (Low): Minor bugs, questions

4. Extract key information: product affected, error messages

Output in this format:
{
    "category": "...",
    "priority": "P0/P1/P2/P3",
    "summary": "One-sentence issue summary",
    "key_details": {...}
}

Be thorough but concise.'''
)
```
]

There you go. You see the instruction? It's very detailed - tells the agent exactly what to do and how to format output. This is important for Sequential workflows because the next agent needs to understand this output.

All right, now the second agent - research:

[Type:
```python

# ============================================================
# SUB-AGENT 2: Research Agent
# ============================================================

research_agent = Agent(
    name='research_agent',
    model='gemini-2.0-flash-exp',
    description='Searches knowledge base for solutions',
    instruction='''You are a customer service research specialist.

You receive a triaged issue. Your role:

1. Review the category, priority, and details
2. Search for:
   - Similar past tickets and resolutions
   - Knowledge base articles
   - Known bugs or workarounds

3. Recommend a solution

Output format:
{
    "similar_tickets": [...],
    "recommended_solution": "Step-by-step solution",
    "escalate": true/false
}

Base your research on the triage details.'''
)
```
]

Perfect. This agent takes the triage output and finds solutions. You see how the instruction references 'You receive a triaged issue'? That's the state passing - it knows it's second in the sequence.

Okay, one more - the response agent:

[Type:
```python

# ============================================================
# SUB-AGENT 3: Response Agent
# ============================================================

response_agent = Agent(
    name='response_agent',
    model='gemini-2.0-flash-exp',
    description='Generates empathetic customer responses',
    instruction='''You are a customer service response specialist.

You receive:
- Triage analysis (category, priority, details)
- Research findings (solutions, workarounds)

Your role: Craft a helpful, professional response.

Structure:
1. Acknowledge the issue empathetically
2. Provide clear solution steps
3. Set expectations

Tone: Professional but friendly, empathetic, confident.

Output a complete customer response ready to send.'''
)
```
]

There you go - three specialized agents. Now let's wrap them in a SequentialAgent:

[Type:
```python

# ============================================================
# ROOT AGENT: Sequential Workflow
# ============================================================

root_agent = SequentialAgent(
    name='customer_service',
    description='3-agent support workflow: triage → research → respond',
    sub_agents=[
        triage_agent,
        research_agent,
        response_agent
    ]
)
```
]

And like that, we have a Sequential workflow! Command S.

Let me show you what happens when this runs. The SequentialAgent:
1. Runs triage_agent first → Gets category and priority
2. Runs research_agent second → Gets solutions (sees triage output in history)
3. Runs response_agent third → Writes response (sees both triage and research)

State passes automatically through conversation history. You don't have to manually pass data. Perfect.

Now let's test it."

**[Terminal]**

**SAY:**
"So from the parent directory, let's launch ADK Web:
[Type: adk web]

There you go. Select 'customer_service' from the dropdown.

Now let's send a test issue:
[Type: 'Customer cannot login after password reset']

[Send]

Watch what happens in the Events tab...

[Show Events tab]

You see that? Look at the sequence:
1. triage_agent ran - categorized as P1, technical
2. research_agent ran - found solution about session clearing
3. response_agent ran - generated the customer email

All three ran in order. And the final response is what the customer sees - a helpful solution with empathy.

This is Sequential workflows. Three specialized agents working together to solve one problem.

All right, let's keep going. I want to show you how this pattern transfers to other domains."

---

## 🎬 PATTERN REUSE: CONTENT_PIPELINE (25 min)

**SAY:**
"Okay, so now let me show you something cool. The exact same Sequential pattern works for completely different business problems.

Let's look at content creation - the content_pipeline agent.

[Open adk_agents/content_pipeline/agent.py]

You see this? Four agents: research, draft, optimize, publish.

Same pattern as customer_service, but different domain.

Customer service: Triage → Research → Respond
Content creation: Research → Draft → Optimize → Publish

Both are Sequential workflows where each step needs the previous step's output.

Let me show you the research agent:
[Show research_agent code]

It searches for recent articles and statistics. Then the draft agent:
[Show draft_agent code]

It uses that research to write the article. Then optimizer:
[Show optimizer_agent]

Improves SEO and readability. And publisher:
[Show publisher_agent]

Formats for different platforms - Medium, LinkedIn, company blog.

Let's test this:
[Switch to ADK Web, select content_pipeline]
[Type: 'Write a short article about AI agents']

[Show Events tab as it runs]

There you go - all four agents running in sequence. Research found sources, draft used them, optimizer improved it, publisher formatted it.

Same pattern. Different business use case.

This is very important - once you learn Sequential, you can apply it to any multi-step business process. Approval workflows, data pipelines, anything where steps depend on each other.

Perfect. Now let me show you decision gates."

---

## 🎬 DECISION GATES: MEDICAL_AUTHORIZATION (30 min)

**[Show slide: Decision Gates in Sequential Workflows]**

**SAY:**
"All right, so decision gates. Not all Sequential workflows run all agents every time. Sometimes you want to stop early if conditions aren't met.

Let me show you the medical authorization agent - this is a healthcare pre-authorization workflow.

[Open medical_authorization/agent.py]

Four agents: intake, verification, medical_review, authorization.

But here's the key: Each agent can stop the workflow. Let me show you:

**Intake agent:**
[Show intake_agent instruction]

If the request is incomplete (missing patient ID, missing procedure codes), it stops here. Output says 'incomplete'. Verification doesn't run.

**Verification agent:**
[Show verification_agent instruction]

If the patient isn't eligible or procedure isn't covered, it stops here. Output says 'denied'. Medical review doesn't run.

**Medical review agent:**
[Show medical_review_agent instruction]

If not medically necessary, it stops and denies. Authorization doesn't run.

Only if all three gates pass does the authorization agent run and approve.

Let me demonstrate:
[ADK Web, test with incomplete request]

[Type: 'Pre-auth for knee surgery, patient John Smith']
(Intentionally missing Member ID)

[Run]

You see that? Workflow stopped at intake_agent. It said 'incomplete - missing member ID'. The other three agents never ran.

Now let's try with complete data:
[Type complete authorization request with all fields]

[Run - show Events tab]

There you go! All four agents ran. Intake extracted data, verification checked eligibility (approved), medical review checked necessity (approved), authorization generated the approval number.

This is decision gates. Workflows can stop early, saving processing time and API costs.

For production, this is critical - don't waste money processing invalid requests all the way through."

---

## 🎬 SEQUENTIAL BEST PRACTICES (15 min)

**[Show slide: Sequential Workflow Best Practices]**

**SAY:**
"Okay, so let me give you five best practices for Sequential workflows:

**1. Specialized agents** - Each agent does ONE thing well
- Triage doesn't try to solve - just categorizes
- Research doesn't write responses - just finds solutions
- Response doesn't research - just writes

**2. Clear output formats** - Tell each agent what the next agent needs
- If next agent needs JSON, specify the exact format
- If next agent needs analysis, say what to analyze

**3. Use decision gates** - Stop early when appropriate
- Check completeness before processing
- Validate before expensive operations
- Fail fast with clear error messages

**4. Test individual agents** - Before testing the full workflow
[Show run_debug example:
```python
from google.adk import run_debug
run_debug(triage_agent, 'Customer login issue')
```
]

Test each agent independently, then test the sequence.

**5. Monitor in production** - Use callbacks to log each step
- Know which agent succeeded/failed
- Track processing time per agent
- Debug issues faster

All right, those are the best practices. Now let's do the exercise."

---

## 🎬 EXERCISE (5 min)

**SAY:**
"Okay, your turn. Build a 3-agent Sequential workflow for support ticket routing:

**Agent 1:** Categorize ticket (bug, feature request, question)
**Agent 2:** Assign to the right team (engineering, product, support)
**Agent 3:** Generate notification with context

Use the customer_service agent as a template. Exercise instructions are in module-4/exercises/.

Take 20-30 minutes. Pause the video. Solution next."

---

## 🎬 SOLUTION (15 min)

**SAY:**
"All right, let's walk through the solution.

[Show complete solution with narration]

First agent categorizes:
[Walk through code]

Second agent assigns:
[Walk through code]

Third agent notifies:
[Walk through code]

Wrap in SequentialAgent:
[Show wrapper]

There you go. And when you test it, all three run in sequence. Perfect."

---

## 🎬 RECAP (3 min)

**SAY:**
"Okay, so Module 4 complete. Let's recap:

You understand when to use Sequential - when tasks depend on each other.
You built three different Sequential workflows - customer service, content pipeline, medical authorization.
You learned about decision gates - workflows can stop early.
You know best practices - specialized agents, clear outputs, test individually.

In Module 5, we're going to learn the opposite pattern - Parallel execution. When tasks are independent, we run them all at the same time. 4x faster.

This is the paradigm shift. See you in Module 5!"

---

## 📝 RECORDING NOTES

**Critical Moments:**
- Events tab showing all 3 agents running in sequence
- State passing demonstration (research uses triage output)
- Decision gate stopping workflow early

**Ady Voice:**
- "Let me show you..."
- "You see that?"
- "There you go"
- "This is very important"
- Live coding narration

**Total Segments:** ~12
**Estimated Recording:** 4 hours with retakes
