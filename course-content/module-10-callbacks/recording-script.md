# Module 10: Callbacks & Lifecycle Hooks - Recording Script

**Duration:** 90 minutes
**Energy:** Moderate to high (powerful production feature!)
**Focus:** Observability and control

---

## 🎬 HOOK

**SAY:**
"Hello and welcome to Module 10 - Advanced Production Patterns.

Okay, so in the core modules, we built agents that work. Now we're going to make them observable and controllable for production. Today we're covering callbacks - the lifecycle hooks that let you intercept every stage of agent execution.

By the end, you'll be able to log every agent decision, track costs in real-time, implement custom routing, and debug complex multi-agent systems.

This is production observability. Let's build it!"

---

## 🎬 OVERVIEW

**SAY:**
"All right, here's what callbacks let you do. Every agent has a lifecycle - things that happen before it runs, while it's running, and after it runs. Callbacks are hooks into that lifecycle.

We're going to cover:
- Before/after agent callbacks (execution tracking)
- Before/after tool callbacks (tool usage monitoring)
- Before/after model callbacks (LLM request/response logging)
- Real-world use cases: cost tracking, custom metrics, debugging

This is how you know what your agents are doing in production. Let's start with the agent lifecycle."

---

## 🎬 AGENT LIFECYCLE EXPLAINED (15 min)

**[Show slide: Agent Lifecycle Diagram]**

**SAY:**
"So let me show you what happens when an agent runs. There's a specific sequence:

1. **Before Agent** - Agent is about to execute
2. Agent thinks and decides what to do
3. **Before Tool** - Agent decided to call a tool, about to execute it
4. Tool executes
5. **After Tool** - Tool finished, got result
6. **Before Model** - Agent about to call the LLM
7. LLM generates response
8. **After Model** - LLM returned response
9. Agent processes result
10. **After Agent** - Agent finished execution

At each of these points, you can inject your own code - callbacks. Let me show you how."

---

## 🎬 BEFORE/AFTER AGENT CALLBACKS (20 min)

**SAY:**
"Okay, so let's add callbacks to track agent execution. I'm going to modify the greeting_agent:

[Open greeting_agent code]

[Type:
```python
def before_agent(agent_name, user_message):
    '''Called before agent starts'''
    print(f'▶️  {agent_name} starting...')
    print(f'   User query: {user_message}')

def after_agent(agent_name, result):
    '''Called after agent finishes'''
    print(f'✅ {agent_name} completed')
    print(f'   Result length: {len(str(result))} chars')

root_agent = Agent(
    name='greeting_agent',
    model='gemini-2.0-flash-exp',
    instruction='...',
    tools=[...],
    before_agent_callback=before_agent,  # ← Hook it in
    after_agent_callback=after_agent
)
```
]

There you go. Now let's test it:

[Run agent]

You see that? Before the agent runs, we see the starting message. After it completes, we see the completion message.

This is very useful for debugging multi-agent systems. You can track: Which agent is running? How long did it take? What was the output?

Perfect. Now let's add tool callbacks."

---

## 🎬 TOOL CALLBACKS (20 min)

**SAY:**
"All right, tool callbacks. This is how you monitor tool usage - which tools get called, how often, with what parameters.

[Add tool callbacks:
```python
def before_tool(tool_name, parameters):
    '''Called before tool executes'''
    print(f'🔧 Calling tool: {tool_name}')
    print(f'   Parameters: {parameters}')

def after_tool(tool_name, result):
    '''Called after tool returns'''
    print(f'✅ Tool {tool_name} completed')
    print(f'   Result: {result}')

root_agent = Agent(
    ...
    before_tool_callback=before_tool,
    after_tool_callback=after_tool
)
```
]

[Test - show tool calls logged]

There you go - now you see every tool call with parameters and results.

For production, you'd log this to a database:
[Show production example logging to BigQuery]

Perfect. Now model callbacks for cost tracking."

---

## 🎬 MODEL CALLBACKS FOR COST TRACKING (20 min)

**SAY:**
"Okay, so model callbacks. This is how you track LLM requests - costs, token usage, latency.

[Add model callbacks:
```python
def before_model(request):
    '''Called before LLM request'''
    print(f'📤 LLM request:')
    print(f'   Tokens in prompt: {count_tokens(request)}')

def after_model(response):
    '''Called after LLM responds'''
    print(f'📥 LLM response:')
    print(f'   Tokens generated: {response.usage.output_tokens}')
    print(f'   Cost: ${calculate_cost(response)}')

root_agent = Agent(
    ...
    before_model_callback=before_model,
    after_model_callback=after_model
)
```
]

[Demo - show cost tracking in real-time]

There you go - now you're tracking costs per request. For production at scale, this is critical.

You can aggregate this data:
[Show example dashboard with cost metrics]

This is how you control your AI spend. Perfect."

---

## 🎬 REAL-WORLD USE CASES (15 min)

**SAY:**
"Let me show you three real production use cases for callbacks:

**Use Case 1: Cost Attribution**
[Code example - tracking costs per customer/team]

**Use Case 2: Quality Monitoring**
[Code example - logging low-confidence responses for review]

**Use Case 3: Custom Routing**
[Code example - routing complex queries to better models]

These are production patterns. This is how you operate agents at scale."

---

## 🎬 RECAP

**SAY:**
"Module 10 complete. You learned the agent lifecycle, before/after callbacks for agents, tools, and models. You can now track execution, monitor costs, and debug production systems.

Module 11: Artifacts and file handling - working with images, PDFs, audio beyond just text.

See you there!"

---
