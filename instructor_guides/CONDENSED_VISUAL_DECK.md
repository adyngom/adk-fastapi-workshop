# Building Production AI Agents with Google ADK
## DevFest Atlanta 2025

**Workshop**: 2 hours hands-on
**What you'll learn**: ADK + FastAPI integration
**What you'll build**: Multi-agent systems

---

# Your Starter Template

**Already running for you:**

- 🎨 **Custom Chat UI**: http://localhost
- 🔍 **ADK Web Debugger**: http://localhost/adk
- 📡 **FastAPI Backend**: http://localhost:8000/docs

**Three interfaces, one agent.**

Today: Understand → Explore → Extend

---

# Why Multi-Agent Systems?

## The Problem
❌ One "super agent" trying to do everything
- Instruction overload
- Hard to debug
- Difficult to improve

## The ADK Solution
✅ Specialized agents collaborating
- Clear responsibilities
- Easy to test
- Simple to extend

**Just like software teams: experts working together > one generalist**

---

# Google's Agentic Stack

**Agent Development Kit (ADK)**
Open-source toolkit for building agents

**Model Context Protocol (MCP)**
Standardized tools and context

**Vertex AI Agent Engine**
Managed deployment platform

**Agent2Agent (A2A)**
Agent communication protocol

---

# ADK: Code-First Agent Framework

✅ **Build Fast**
- Minimal boilerplate
- Built-in dev UI
- Hot reload

✅ **Flexible**
- Any model (Gemini, GPT, Claude)
- MCP tools
- Deploy anywhere

✅ **Production-Ready**
- Testing framework
- Monitoring
- Security callbacks

---

# Anatomy of an ADK Agent

```python
from google.adk.agents import Agent

root_agent = Agent(
    name="greeting_agent",
    model="gemini-2.0-flash",
    description="What this agent does",
    instruction="How it should behave",
    tools=[...]  # Optional capabilities
)
```

**That's it!** 5 lines to create an intelligent agent.

---

# 🛠️ Exercise 1: Explore greeting_agent

## Open ADK Web
http://localhost/adk

## Try It
1. Select `greeting_agent`
2. Send a message
3. Click **Events** tab ← The magic!

## What You'll See
- `agent_start` - Processing begins
- `agent_response` - LLM generates text
- `agent_end` - Complete

**Expand events** to see instructions, model calls, responses

**This is how you debug agents!**

---

# Multi-Agent Patterns

## Pattern 1: Router (Hub-and-Spoke)
```
Coordinator → Delegates to specialists
```
**Use**: Query handled by ONE expert

## Pattern 2: Sequential Pipeline
```
Agent A → Agent B → Agent C
```
**Use**: Tasks have dependencies

## Pattern 3: Parallel + Synthesis
```
[A, B, C] → Run together → Combine
```
**Use**: Independent tasks, faster results

---

# Agent-as-Tool Pattern

**Powerful concept**: Agents can use other agents as tools

```python
from google.adk.tools.agent_tool import AgentTool

coordinator = Agent(
    name="coordinator",
    model="gemini-2.0-flash",
    instruction="Delegate to appropriate specialist.",
    tools=[
        AgentTool(agent=researcher),
        AgentTool(agent=writer),
        AgentTool(agent=analyst)
    ]
)
```

**Coordinator reads agent descriptions, routes intelligently**

---

# 🛠️ Exercise 2: Multi-Agent News Analysis

## The System
1. **News Gatherer** - Searches web
2. **Summarizer** - Creates concise summary
3. **Sentiment Analyzer** - Analyzes tone

**Sequential pipeline**: Gatherer → Summarizer → Analyzer

## Code Walkthrough
We'll explore working code together

## What You'll Learn
- How agents pass state
- Using `output_key` and `{placeholders}`
- Debugging multi-agent flows in Events tab

---

# Production Considerations

## Security
- Input validation (before_model_callback)
- Output filtering (after_model_callback)
- Human-in-the-loop for sensitive ops

## Testing
- ADK eval framework
- Custom evaluators
- Continuous monitoring

## Deployment
- **Dev**: ADK web
- **Production**: Cloud Run, Vertex AI Agent Engine
- **Your choice**: GKE, on-prem, anywhere

---

# What's Next?

## Post-Workshop
✅ Complete Google Codelabs
✅ Explore github.com/google/adk-samples
✅ Try DeepLearning.AI ADK course

## Your Git Tags
```bash
git checkout v0-starter-template  # What we covered
# Future: v1-custom-tools, v2-multi-agent, etc.
```

## Keep Building
- Start simple
- Add complexity when needed
- Production patterns from day one

---

# Thank You!

**You now have**:
- Working triple-interface system
- Understanding of ADK fundamentals
- Multi-agent patterns
- Production-ready starting point

**Resources**:
- Repo: github.com/[your-repo]
- Docs: cloud.google.com/vertex-ai/docs/adk
- Community: Google ADK samples

**Go build something amazing!** 🚀

---
