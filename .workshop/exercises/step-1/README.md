# Step 1: Single Agent with Custom Tools

**Duration:** 30 minutes
**Difficulty:** Beginner
**Agent:** `greeting_agent`

## Learning Objectives

By the end of this step, you will:
- ✅ Understand ADK Agent class structure
- ✅ Create custom Python function tools
- ✅ Write effective agent instructions
- ✅ Test agents with ADK Web and Streamlit UI
- ✅ Enable voice input (optional)

## Exercises

### Exercise 1.1: Customize Company Info

**File:** `adk_agents/greeting_agent/tools.py`

**Task:** Update `get_company_info()` with your organization's data

**Steps:**
1. Open `adk_agents/greeting_agent/tools.py`
2. Find the `get_company_info()` function
3. Replace "Acme Corporation" with your company name
4. Update industry, location, and use cases to match your organization
5. Save the file

**Test:**
```
# In ADK Web (port 3002) or Streamlit (port 8501), ask:
"Tell me about my company"
```

Expected: Agent responds with YOUR company information.

**Hints:**
- No need to restart anything - hot reload should work
- If changes don't appear, try refreshing the browser
- Check console for any Python syntax errors

---

### Exercise 1.2: Add New Tool - get_team_members()

**File:** `adk_agents/greeting_agent/tools.py`

**Task:** Create a function that returns your team roster

**Steps:**
1. In `tools.py`, create a new function below `get_company_info()`
2. Name it `get_team_members()`
3. Add a docstring explaining what it does
4. Return a dict with team member information

**Template:**
```python
def get_team_members() -> dict:
    """Get the current team roster and roles.

    Returns information about team members including names,
    roles, and areas of responsibility.

    Returns:
        dict: Team member information
    """
    return {
        "team": [
            {"name": "Your Name", "role": "Tech Lead", "focus": "AI Agents"},
            # Add more team members...
        ],
        "total_members": 1
    }
```

**Don't forget:**
1. Import the function in `agent.py`:
   ```python
   from .tools import get_company_info, get_current_time, get_team_members
   ```

2. Add to tools list:
   ```python
   tools=[get_company_info, get_current_time, get_team_members]
   ```

**Test:**
```
# Ask the agent:
"Who is on my team?"
```

Expected: Agent calls your new tool and displays team members.

**Common Issues:**
- **Tool not showing:** Restart ADK Web (`pkill -f "adk web"` then `.idx/start-services.sh`)
- **Agent doesn't use tool:** Make sure docstring clearly describes what the tool does
- **Import error:** Check function name matches in import statement

---

### Exercise 1.3: Modify Agent Personality

**File:** `adk_agents/greeting_agent/agent.py`

**Task:** Make the agent more enthusiastic and friendly

**Steps:**
1. Open `adk_agents/greeting_agent/agent.py`
2. Find the `instruction` field
3. Modify the tone - make it more enthusiastic
4. Optional: Add appropriate emoji to responses

**Example Change:**
```python
# BEFORE:
instruction="You are a friendly workshop assistant..."

# AFTER:
instruction="You are an ENTHUSIASTIC workshop assistant who LOVES helping developers build amazing AI agents! You're energetic, supportive, and use appropriate emoji to make conversations fun. When users ask questions, you respond with excitement and clear, actionable information. 🚀"
```

**Test:**
```
# Ask any question and observe the tone:
"What can you help me with?"
```

Expected: More enthusiastic, energetic responses.

---

## Success Criteria

Before moving to Step 2, verify:

- [ ] Agent responds with YOUR company information (not Acme Corp)
- [ ] `get_team_members()` tool works and returns your team
- [ ] Agent personality reflects your instruction changes
- [ ] Tested in both ADK Web (3002) and Streamlit (8501)
- [ ] Voice input works (optional - only with compatible models)

## Next Steps

Once you've completed all exercises, you're ready for **Step 2: Customer Service Sequential Workflow**.

Preview: You'll build a 3-agent pipeline that triages → researches → responds to support tickets, learning how agents pass state in sequential workflows.

## Solutions

If you get stuck, check `.workshop/solutions/step-1/` for complete working code.

Or checkout the git tag:
```bash
git checkout step-1-greeting-agent
```

## Questions?

- Check the main `workshop_progression.yaml` for detailed agent architecture
- Ask instructor for clarification
- Review ADK documentation: https://google.github.io/adk-docs/
