# Greeting Agent

**Step 1 of 9** | **Duration:** 30 minutes | **Difficulty:** Beginner

## Overview

A friendly workshop assistant that demonstrates the foundational concepts of building AI agents with Google's Agent Development Kit (ADK). This agent uses custom Python function tools to provide information about your company, team, and current time.

## Learning Objectives

By completing this agent, you will understand:

- ✅ **ADK Agent Class Structure** - How to define agents with name, model, description, and instruction
- ✅ **Custom Tool Creation** - Writing Python functions that agents can call
- ✅ **Tool Function Signatures** - Proper docstrings and type hints for ADK tools
- ✅ **Agent Instructions** - Crafting effective prompts that shape agent behavior
- ✅ **Testing with ADK Web** - Using the built-in UI for agent development
- ✅ **Voice Input** - Optional feature with gemini-2.0-flash models (ADK 1.18+)

## Pattern Demonstrated

**Single Agent with Custom Tools**

```
greeting_agent (Agent)
├── model: gemini-2.0-flash-exp
├── instruction: [Agent personality and behavior]
└── tools:
    ├── get_company_info()
    ├── get_current_time()
    └── get_team_members() [Exercise]
```

This is the foundational pattern for all ADK agents. Every agent you build will follow this basic structure.

## Business Value

While the greeting agent itself is a learning tool, the pattern it demonstrates is used for:
- **Customer onboarding assistants** - Guide new users through setup
- **Internal knowledge bases** - Answer employee questions about company info
- **Interactive documentation** - Help developers find information quickly

## Architecture

### Agent Definition (`agent.py`)

```python
from google.adk.agents import Agent
from .tools import get_company_info, get_current_time

root_agent = Agent(
    name="greeting_agent",
    model="gemini-2.0-flash-exp",
    description="Friendly workshop assistant",
    instruction="You are a helpful assistant...",
    tools=[get_company_info, get_current_time]
)
```

**Key Concepts:**
- `name`: Identifier for the agent (used in UI dropdowns)
- `model`: Which Gemini model to use (flash-exp supports voice)
- `description`: Brief summary of agent's purpose
- `instruction`: Detailed prompt that shapes agent behavior
- `tools`: List of Python functions the agent can call

### Custom Tools (`tools.py`)

```python
def get_company_info() -> dict:
    """Get information about the user's company.

    Returns:
        dict: Company name, industry, location, initiatives
    """
    return {
        "company_name": "Acme Corporation",
        "industry": "Technology",
        # ... more fields
    }
```

**Tool Requirements:**
1. **Type hints**: Return type must be specified
2. **Docstring**: Explains what the tool does (ADK uses this!)
3. **Returns dict**: Structured data the agent can understand

## Files

```
greeting_agent/
├── agent.py          # Agent definition
├── tools.py          # Custom tool functions
├── .env              # API key (GOOGLE_API_KEY)
└── README.md         # This file
```

## Setup

### Prerequisites

- Python 3.11+
- Google Gemini API key
- ADK 1.18+ installed

### Configuration

1. **API Key**: Set in `greeting_agent/.env` or root `.env`
   ```bash
   GOOGLE_API_KEY=your_api_key_here
   ```

2. **Model**: Update in `agent.py` if needed
   ```python
   model="gemini-2.0-flash-exp"  # Supports voice
   ```

## Running the Agent

### Option 1: ADK Web UI (Recommended)

```bash
# From project root
adk web
```

- Opens on port 3002
- Select "greeting_agent" from dropdown
- Supports voice input (click microphone icon)
- Shows tool calling in real-time

### Option 2: Streamlit Workshop UI

```bash
# From project root
streamlit run streamlit_apps/workshop_ui/app.py --server.port 8501
```

- Opens on port 8501
- Select agent from sidebar
- More user-friendly for demos
- No voice support (yet)

### Option 3: CLI

```bash
# From project root
adk run greeting_agent
```

## Example Interactions

### Basic Greeting
```
User: "Hello! What can you help me with?"
Agent: "Hi there! I'm your workshop assistant. I can help you with:
        - Information about your company and current AI initiatives
        - Details about your development team
        - Current date and time
        What would you like to know?"
```

### Company Information
```
User: "Tell me about my company"
Agent: [Calls get_company_info()]
       "You work at Acme Corporation, a Technology company based in..."
```

### Tool Combination
```
User: "What time is it and who's on my team?"
Agent: [Calls get_current_time() and get_team_members()]
       "It's currently 3:45 PM EST. Your team includes..."
```

## Exercises

See `.workshop/exercises/step-1/` for hands-on exercises:

1. **Customize Company Info** - Update `get_company_info()` with your data
2. **Add Team Tool** - Create `get_team_members()` function
3. **Modify Personality** - Make the agent more enthusiastic

Solutions available in `.workshop/solutions/step-1/`

## Success Criteria

Before moving to Step 2, verify:

- [ ] Agent loads in ADK Web without errors
- [ ] All tools are callable (check logs when testing)
- [ ] Agent provides helpful responses
- [ ] Custom company info displays correctly
- [ ] Voice input works (optional - compatible models only)

## Common Issues

### Tool Not Being Called

**Problem:** Agent responds without using tools

**Solution:**
- Check docstring clearly describes what tool does
- Make question more explicit: "Use the company info tool to tell me about my company"
- Verify tool is in the `tools=[]` list in `agent.py`

### Agent Not Found

**Problem:** Agent doesn't appear in ADK Web dropdown

**Solution:**
- Check `root_agent` variable name in `agent.py`
- Ensure no syntax errors (check console)
- Restart ADK Web: `pkill -f "adk web"` then restart

### Voice Not Working

**Problem:** Microphone icon doesn't appear or doesn't work

**Solution:**
- Requires `gemini-2.0-flash-live` or compatible model
- ADK 1.18+ required
- Browser must have microphone permissions
- Voice only works with simple Agent type (not SequentialAgent)

## Next Steps

Once you've completed the exercises and verified all success criteria, proceed to:

**Step 2: Customer Service Sequential Workflow**

Preview: Build a 3-agent pipeline (triage → research → respond) that demonstrates how agents pass state in sequential workflows. This is where real business value starts to emerge!

## References

- [ADK Documentation](https://google.github.io/adk-docs/)
- [Agent Class API](https://google.github.io/adk-docs/agents/agent/)
- [Custom Tools Guide](https://google.github.io/adk-docs/tools/custom-tools/)
- [Workshop Progression](../../workshop_progression.yaml)

---

**Tags:** `step-1-greeting-agent`, `beginner`, `single-agent`, `custom-tools`
