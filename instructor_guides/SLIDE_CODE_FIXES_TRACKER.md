# 🔧 Slide Code Fixes Tracker

> **Goal**: Fix all code examples to match ADK v1.17 API
> **Deadline**: Tonight (workshop tomorrow)
> **Strategy**: Divide and conquer

---

## ✅ VERIFIED CORRECT ADK SYNTAX

From official adk-demos repository:

```python
# Imports
from google.adk.agents import Agent
from google.adk.tools.agent_tool import AgentTool
from google.adk.agents.workflows import SequentialAgent, ParallelAgent, LoopAgent

# Single agent
root_agent = Agent(
    name="agent_name",
    model="gemini-2.0-flash",
    description="What this agent does",
    instruction="How to behave",  # ✅ SINGULAR!
    tools=[tool1, tool2],
    output_key="result_key"
)

# Agent-as-tool (multi-agent)
coordinator = Agent(
    name="coordinator",
    model="gemini-2.0-flash",
    description="Coordinates specialists",
    instruction="Delegate to appropriate specialists.",
    tools=[
        AgentTool(agent=specialist1),  # ✅ Wrap in AgentTool!
        AgentTool(agent=specialist2),
    ]
)

# Alternative: sub_agents parameter
coordinator = Agent(
    name="coordinator",
    model="gemini-2.0-flash",
    sub_agents=[specialist1, specialist2]  # ✅ Alternative approach
)
```

---

## 📋 SLIDES STATUS

### ✅ FIXED (Claude)

- [x] **Slide 6**: Agent Types
  - Fixed: `LLMAgent` → `Agent`
  - Fixed: Added `instruction` parameter
  - Fixed: Import statement

- [x] **Slide 10**: Specialized Team Pattern
  - Fixed: All imports
  - Fixed: `instructions` → `instruction`
  - Fixed: Agent-as-tool with `AgentTool()` wrapper
  - Added: `model` parameter to all agents

- [x] **Slide 11**: Sequential Pipeline
  - Fixed: Import from `google.adk.agents.workflows`
  - Fixed: `LLMAgent` → `Agent`
  - Fixed: `instructions` → `instruction`
  - Added: `model` parameter to all agents

- [x] **Slide 12**: Parallel + Synthesis
  - Fixed: All imports
  - Fixed: `instructions` → `instruction`
  - Added: `model` parameter to all agents

### 🔄 IN PROGRESS (You - Code Assist)

- [ ] **Slide 13**: Exercise 2 (News Analysis)
  - Fix: `from adk import` → `from google.adk.agents import`
  - Fix: `instructions` → `instruction`
  - Add: `model` parameter
  - Verify: Full multi-agent system works

- [ ] **Slide 15**: Testing & Evaluation
  - Verify: Eval framework syntax current
  - Check: Test case structure

### ⏭️ PENDING (Quick fixes)

- [ ] **Slide 7**: Tools
  - Check: Tool definition syntax
  - Verify: Docstring examples

- [ ] **Slide 8**: Exercise 1
  - Simplify: Make it exploration, not coding
  - Reference: greeting_agent at localhost/adk

- [ ] **Slide 14**: State Management
  - Fix: `instructions` → `instruction` in examples
  - Verify: State dictionary syntax

### ✅ NO CODE (Concepts only)

- Slides 1-5: Intro, agenda, why ADK, architecture
- Slides 9: Multi-agent patterns overview (diagrams)
- Slides 16-19: Security, deployment, roadmap, wrap-up
- Slides 20-22: Troubleshooting, use cases, cheat sheet

---

## 🎯 CODE ASSIST FOCUS AREAS

### Slide 13: Exercise 2 - News Analysis System

**Current code location**: `docs/slides/slide_13_exercise_multi_agent.md` lines 638-682

**Issues to fix**:
1. Import statement
2. `LLMAgent` → `Agent`
3. `instructions` → `instruction`
4. Add `model` parameter
5. Verify output_key usage

**Target syntax**:
```python
from google.adk.agents import Agent
from google.adk.agents.workflows import SequentialAgent

news_gatherer = Agent(
    name="news_gatherer",
    description="Searches for latest news articles",
    model="gemini-2.0-flash",
    instruction="Search for recent news about: {topic}",
    tools=[GoogleSearchTool()],
    output_key="news_articles"
)
# ... etc
```

### Slide 15: Testing Framework

**Current code location**: `docs/slides/slide_15_testing_evaluation.md`

**Check**:
- Eval JSON format still valid?
- `adk eval` command syntax current?
- Custom evaluator class structure

---

## ⏰ TIME ESTIMATE

**Per slide**: 10-15 minutes (read, fix, verify)

**Remaining**:
- Slide 7: 10 min
- Slide 8: 15 min (needs redesign)
- Slide 13: 15 min (CODE ASSIST)
- Slide 14: 10 min
- Slide 15: 10 min (CODE ASSIST)

**Total**: ~60 minutes

**Parallel work**: Cut to 30-40 minutes!

---

## 🔍 COMMON FIXES NEEDED

### Global Find/Replace

In all slide files:
1. `instructions=` → `instruction=`
2. `from adk import` → `from google.adk.agents import`
3. `LLMAgent(` → `Agent(`

### Pattern-Specific

**Multi-agent** (slides 10, 13):
- Wrap sub-agents: `tools=[AgentTool(agent=sub)]`
- Or use: `sub_agents=[sub1, sub2]`

**All agents need**:
- `name`
- `model`
- `description`
- `instruction` (if LLM-based)

---

## ✅ VERIFICATION CHECKLIST

Before considering a slide "done":

- [ ] All imports correct
- [ ] `instruction` (singular) used
- [ ] `root_agent =` for file exports
- [ ] `model` parameter present
- [ ] Agent-as-tool uses `AgentTool()` wrapper
- [ ] Workflow imports from `.workflows`
- [ ] No `LLMAgent` references (use `Agent`)

---

## 📊 PROGRESS TRACKER

**Fixed**: 4/15 slides with code (27%)
**In Progress**: 2 slides (Code Assist)
**Remaining**: 3 slides (quick fixes)

**ETA to completion**: 30-40 minutes (with parallel work)

---

## 🚀 AFTER CODE FIXES

Once all code is verified:

1. Commit fixes
2. Re-stitch slides into FULL_SLIDE_DECK.md
3. Upload to Gamma or use for speaker notes
4. Get some sleep!
5. Workshop tomorrow 🎉

---

**Last Updated**: October 30, 2025, 9:45 PM
**Status**: Actively fixing in parallel
**Next**: Complete remaining slides, commit, rest!
