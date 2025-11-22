# Module 7: Production Tools & Integration - Recording Script

**Duration:** 120 min
**Prep Required:** Google Search example (1 hour)
**Energy:** HIGH! (This is the magic moment!)

---

## 🎬 HOOK

**SAY:**
"Hello and welcome to Module 7. This is the module I've been excited about.

Remember Module 5? The financial advisor said Apple stock was $175, but the real price was $273? Today we're fixing that. And the fix is literally two lines of code.

By the end of this module, you'll know how to give your agents real-time data with Google Search, code execution capabilities, database access, and you'll be able to use multiple AI models.

This is where agents become production-ready. Let's do this!"

---

## 🎬 THE $175 FIX - GOOGLE SEARCH TOOL (30 min) 🎆

**SAY:**
"Okay, so let's fix the stock price problem from Module 5. Real quick, let me show you the issue again.

[Open financial_advisor, run with AAPL]

You see? It says $175. But the real price is...

[Open Google in browser, search 'AAPL stock price']

$273. That's a $100 difference!

The problem: LLMs use training data. That data is months old.

The solution: Give the agent a tool to search Google for current data.

Watch this - I'm going to modify the data_analyst to use Google Search:

[Open financial_advisor code]

[Add at top:
```python
from google.adk.tools import google_search
```
]

So I'm importing the google_search tool. This is a built-in tool from Google - it just works.

Now in the data_analyst, I'm going to add it:

[Modify data_analyst:
```python
data_analyst = Agent(
    name='data_analyst_realtime',
    model='gemini-2.0-flash',  # ← Gemini 2+ required for built-in tools
    tools=[google_search],     # ← THE MAGIC LINE
    instruction='''Use Google Search to find CURRENT stock market data.

Search for:
- "AAPL stock price today"
- "Apple earnings recent"
- "AAPL analyst ratings"

Provide current, accurate data.'''
)
```
]

Two lines! That's it! 'from google.adk.tools import google_search' and 'tools=[google_search]'.

Command S. Now let's restart ADK Web:

[Restart: pkill -f 'adk web' && adk web]

Okay, loading...

[ADK Web opens]

Perfect. Now let's test the same query:

[Type: 'Analyze AAPL stock']

[Send]

Watch the Events tab... you see it? It's calling the google_search tool!

[Wait for completion]

[Read data_analyst output - should show current price near $269-$273]

There you go! It says $269! Real-time data from Google Search!

[Pause for impact]

THIS is the fix. Two lines of code transformed the agent from stale data to real-time accuracy.

And like that, we solved the $100 problem.

This is very important for production. Any agent that needs current data - news agents, market intelligence, research assistants - they NEED Google Search tool. Without it, they're using months-old information.

Perfect. Now let me show you the other built-in tools."

---

## 🎬 CODE EXECUTION TOOL (20 min)

**SAY:**
"All right, so Google has another built-in tool - code execution. This lets agents write and run Python code.

[Create code_execution_example]

[Show agent with BuiltInCodeExecutor]

[Demo: 'Calculate compound interest on $10k at 5% for 10 years']

[Agent writes code, executes it, returns result]

There you go! The agent wrote Python code and ran it. For data analysis, calculations, chart generation - super powerful.

Okay, let's keep going to MCP integration."

---

## 🎬 MCP INTEGRATION (30 min)

**SAY:**
"MCP - Model Context Protocol. This is how you connect agents to databases, APIs, external services.

[Show MCP Toolbox example from workshop]

In production, you'd set up an MCP server that exposes database operations as tools. The agent can then query your database with natural language.

[Demo the pattern - don't need working database, just show the code]

This is the architecture for production agents - MCP tools for all external integrations."

---

## 🎬 MULTI-MODEL STRATEGIES (15 min)

**SAY:**
"Real quick, let me show you how to use OpenAI, Claude, or Ollama instead of Gemini.

[Show LiteLLM examples]

Same agent code, different model. You can switch between GPT-4, Claude, even local models.

[Demo changing model with one line]

Perfect. This gives you flexibility."

---

## 🎬 RECAP (5 min)

**SAY:**
"Module 7 complete! You fixed the $175 problem with Google Search. You learned built-in tools, MCP integration, and multi-model strategies.

Module 8: We're combining everything - Sequential + Parallel + Verification. The final production patterns.

See you there!"

---
