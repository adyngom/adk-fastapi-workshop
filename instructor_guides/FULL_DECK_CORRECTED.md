# Building Production-Ready AI Agents with Google ADK

## From Concepts to Deployment: A Hands-On Workshop

**Workshop Duration:** 2 hours (extensible to full day)

**What You'll Build Today:**
- Your first AI agent
- Multi-agent systems
- Production-ready workflows

---

**Prerequisites:**
- Basic Python knowledge helpful but not required
- Google Cloud account (free tier works)
- Curiosity about AI automation

---

# Workshop Agenda

## Part 1: Foundations (30 minutes)
- Why agentic AI matters now
- ADK core concepts & architecture
- Agent types and when to use them

## Part 2: Hands-On Building (45 minutes)
- **Exercise 1:** Your first agent (15 min)
- Multi-agent patterns & orchestration
- **Exercise 2:** Building a multi-agent system (30 min)

## Part 3: Production Practices (30 minutes)
- State management & memory
- Testing and evaluation strategies
- Security, deployment & best practices

## Part 4: Wrap-Up (15 minutes)
- Q&A and troubleshooting
- Advanced features & roadmap
- Resources and next steps

---

**Full-Day Extension Topics:**
- Advanced multi-agent patterns
- Voice agents with Gemini Live
- Enterprise deployment deep-dive
- Building custom tools & integrations

---

# Why Agentic AI Matters Now

## The Evolution of AI Applications

**Traditional AI (2022-2023):**
- Single-shot responses
- No decision-making capability
- Human drives every action
- Limited context awareness

**Agentic AI (2024-2025):**
- Multi-step reasoning
- Autonomous tool usage
- Goal-oriented behavior
- Persistent memory and learning

## Real-World Impact

**Customer Service:** Agents handle complex inquiries across multiple systems
**Data Analysis:** Automated research, synthesis, and reporting
**Software Development:** Code generation, testing, and debugging
**Business Operations:** Workflow automation and decision support

## The Problem ADK Solves

❌ **Old Approach:** Build massive "super agents" that do everything  
✅ **ADK Approach:** Teams of specialized agents that collaborate

*Just like software engineering teams—experts working together beats one generalist*

---

# What is Google's Agent Development Kit (ADK)?

## Open-Source Framework for Production AI Agents

**Launched:** April 2025 at Google Cloud NEXT  
**Current Version:** v1.17.0 (October 2025)  
**Release Cadence:** Bi-weekly updates

## Three Core Principles

### 1. Model-Agnostic
- Works with Gemini, GPT-4o, Claude, Mistral, and 100+ models
- No vendor lock-in
- Switch models without code changes

### 2. Deployment-Agnostic
- Local development with built-in Web UI
- Enterprise scale on Vertex AI Agent Engine
- Custom infrastructure (Cloud Run, etc.)

### 3. Framework-Compatible
- Integrate tools from LangChain, CrewAI, LlamaIndex
- Use existing investments
- ADK as orchestration layer, not replacement

## Who's Using It?

**Google Products:** Agentspace, Customer Engagement Suite  
**Enterprise Customers:** Renault Group, Box, Revionics  
**Developers:** 25+ official sample agents, growing community

---

# ADK Architecture: Building Blocks

## The Three-Layer Model

```
┌─────────────────────────────────────┐
│     ORCHESTRATION LAYER             │
│  (Coordinator agents, routing)      │
└─────────────────────────────────────┘
           ↓         ↓         ↓
┌─────────────┐ ┌─────────────┐ ┌─────────────┐
│  AGENT 1    │ │  AGENT 2    │ │  AGENT 3    │
│  (Research) │ │  (Analysis) │ │  (Writing)  │
└─────────────┘ └─────────────┘ └─────────────┘
       ↓               ↓               ↓
┌──────────────────────────────────────────────┐
│            TOOL ECOSYSTEM                     │
│  APIs • Databases • Search • Code Execution   │
└──────────────────────────────────────────────┘
```

## Key Components

**Agents:** Autonomous decision-makers with specific responsibilities  
**Tools:** Functions agents can invoke (Google Search, APIs, custom code)  
**Memory:** Persistent state across conversations  
**Sessions:** Manage multi-turn interactions

## Philosophy: Code-First Development

- Treat agents as software components
- Version control with Git
- Unit testing with pytest
- CI/CD pipelines
- Standard software engineering practices

---

# Three Types of Agents in ADK

## 1. LLM Agents
**Brain:** Language model makes decisions  
**Use When:** Flexibility and context-understanding needed

**Example:**
```python
from google.adk.agents import Agent

customer_service_agent = Agent(
    name="customer_service",
    description="Handles customer inquiries with empathy",
    model="gemini-2.0-flash",
    instruction="Be professional and empathetic. Help customers with orders and issues.",
    tools=[search_orders, update_status, send_email]
)
```

## 2. Workflow Agents
**Brain:** Predefined logic executes deterministically  
**Use When:** Steps are known and repeatable

**Types:**
- **SequentialAgent:** Step-by-step pipeline (A → B → C)
- **ParallelAgent:** Concurrent execution (A + B + C simultaneously)
- **LoopAgent:** Iterative refinement (repeat until quality threshold met)

## 3. Custom Agents
**Brain:** Your specialized logic  
**Use When:** Unique requirements that neither LLM nor workflow patterns address

**Example Use Cases:**
- Integration with legacy systems
- Complex business logic
- Specialized algorithms

## Choosing the Right Type

**LLM Agents:** "Handle customer complaints professionally"  
**Workflow Agents:** "Process refund: check order → verify eligibility → issue credit"  
**Custom Agents:** "Calculate risk score using our proprietary model"

---

# Tools: Giving Agents Superpowers

## What Are Tools?

Tools are functions that agents can invoke to interact with the world:
- Search the web
- Query databases
- Call APIs
- Execute code
- Send notifications

## Built-In Tools

**Google Services:**
- Google Search
- BigQuery
- Vertex AI Search
- Code Execution

**External Integrations:**
- OpenAPI specifications (any REST API)
- Model Context Protocol (MCP) tools
- LangChain tools
- Custom Python functions

## Creating Custom Tools

**It's as simple as writing a function with a good docstring:**

```python
def calculate_shipping_cost(weight: float, destination: str) -> float:
    """Calculate shipping cost based on package weight and destination.
    
    Args:
        weight: Package weight in pounds
        destination: Destination country code (US, CA, UK, etc.)
        
    Returns:
        Shipping cost in USD
    """
    # Your business logic here
    return base_rate + weight * rate_per_pound
```

The LLM reads the docstring to understand when and how to use your tool!

## Agent-as-a-Tool Pattern

**Powerful concept:** Any agent can become a tool for another agent

```python
from google.adk.agents import Agent
from google.adk.tools.agent_tool import AgentTool

coordinator = Agent(
    name="coordinator",
    model="gemini-2.0-flash",
    description="Coordinates specialist agents",
    instruction="Delegate to the appropriate specialist based on the query.",
    tools=[
        AgentTool(agent=travel_agent),
        AgentTool(agent=news_agent),
        AgentTool(agent=weather_agent)
    ]
)
```

---

# 🛠️ HANDS-ON: Explore Your First Agent (15 minutes)

## Exercise Goal
Understand how ADK agents work by exploring the greeting_agent already running

## You Already Have a Working Agent!

**Open**: http://localhost/adk

You should see `greeting_agent` - this is a real ADK agent running in Google's official ADK Web interface.

## Part 1: Interact with the Agent (5 min)

### 1. Select greeting_agent
- Click dropdown at top left
- Select "greeting_agent"

### 2. Send a Message
```
Hello! I'm attending the ADK workshop at DevFest Atlanta.
```

### 3. Watch the Response
- Agent greets you
- Asks for your name
- Notice the friendly, workshop-focused tone

## Part 2: Explore Events Timeline (5 min)

### Click "Events" Tab

You'll see the agent lifecycle:

**Event 1: agent_start**
- Agent begins processing your message
- Click to expand

**Event 2: agent_response**
- LLM generates the response
- Expand to see:
  - Request: Your message + agent instructions
  - Response: Generated text
  - Metadata: Model used, timing

**Event 3: agent_end**
- Processing complete

**Key insight**: This is how you debug agents! Every step is visible.

## Part 3: Understand the Code (5 min)

### Open the Agent Definition

**File**: `adk_agents/greeting_agent/agent.py`

```python
from google.adk.agents import Agent

root_agent = Agent(
    name="greeting_agent",
    model="gemini-2.0-flash-exp",
    description="A friendly assistant that greets users and helps them get started with ADK",
    instruction="""You are a helpful and friendly assistant for the ADK Workshop.

Your role is to:
1. Greet users warmly
2. Ask for their name if they haven't provided it
3. Greet them by name once you know it
4. Be enthusiastic about helping them learn about Google's Agent Development Kit (ADK)
5. Keep responses concise and friendly

Remember to be encouraging and supportive as they learn about building AI agents!
"""
)
```

### Notice the Key Parts

**name**: `"greeting_agent"` - Must match folder name
**model**: `"gemini-2.0-flash-exp"` - Which LLM to use
**description**: What this agent does (used for routing in multi-agent)
**instruction**: The personality and behavior rules

### Try This: Modify the Agent

1. Edit the `instruction` in `agent.py`
2. Change tone from "friendly" to "professional and concise"
3. Restart: `docker compose restart adk-web`
4. Send same message again
5. See the personality change!

## What You Learned

✅ **ADK agents have 4 key parts**:
- name, model, description, instruction

✅ **Events tab is your debugging superpower**:
- See every step the agent takes
- Inspect requests and responses
- Understand decision-making

✅ **ADK Web is for development**:
- Test agents interactively
- Debug issues visually
- Share demos with stakeholders

✅ **Same agent, multiple interfaces**:
- greeting_agent works in ADK Web
- Same agent works in Custom Frontend (localhost)
- Single source of truth!

## Next Steps

In Exercise 2, you'll see multiple agents working together using the same patterns!

---

**Key Takeaway**: You don't need to build from scratch to learn. Exploring working code is often faster and more educational!

---

# Multi-Agent Orchestration Patterns

## Why Multiple Agents?

**Single Agent Problem:** "Instruction overload"
- Too many responsibilities
- Conflicting priorities
- Hard to maintain and debug

**Multi-Agent Solution:** Specialized collaboration
- Clear responsibilities
- Easier to test and improve
- Mirrors how human teams work

## Four Essential Patterns

### 1. Router Pattern (Hub-and-Spoke)
```
        User Query
             ↓
    [Coordinator Agent]
      /      |      \
   Agent1  Agent2  Agent3
 (Flights)(Hotels)(Activities)
```
**Use:** When query can be handled by ONE specialist

### 2. Sequential Pipeline
```
User Query → Research → Draft → Edit → Fact-Check → Output
```
**Use:** When tasks have clear dependencies

### 3. Parallel + Synthesis
```
             Query
              /|\
             / | \
        [A1][A2][A3] ← Run concurrently
             \|/
         [Synthesizer]
              ↓
           Output
```
**Use:** When tasks are independent but results need combining

### 4. Iterative Refinement
```
Generator → Reviewer → Good enough? → Output
     ↑___________|_____ Not yet _____|
```
**Use:** When quality improves through iteration

## Key Insight
**Start simple, add complexity only when needed**

---

# Pattern 1: Specialized Team (Router)

## The Travel Planner Example

**Scenario:** User asks "Plan a 3-day trip to Tokyo"

### Architecture
```python
from google.adk.agents import Agent
from google.adk.tools.agent_tool import AgentTool

# Specialist agents
flight_agent = Agent(
    name="flight_specialist",
    description="Searches and books flights",
    model="gemini-2.0-flash",
    instruction="Search for flights and provide best options.",
    tools=[FlightSearchAPI(), PriceComparisonTool()]
)

hotel_agent = Agent(
    name="hotel_specialist",
    description="Finds and books accommodations",
    model="gemini-2.0-flash",
    instruction="Find hotels based on traveler preferences and budget.",
    tools=[HotelSearchAPI(), ReviewAnalyzer()]
)

activity_agent = Agent(
    name="activity_specialist",
    description="Recommends activities and experiences",
    model="gemini-2.0-flash",
    instruction="Suggest activities based on interests and trip duration.",
    tools=[GoogleSearch(), LocalGuideTool()]
)

# Coordinator uses AgentTool to wrap sub-agents
travel_coordinator = Agent(
    name="travel_coordinator",
    description="Coordinates travel planning across flights, hotels, and activities",
    model="gemini-2.0-flash",
    instruction="Delegate to specialists and synthesize their responses.",
    tools=[
        AgentTool(agent=flight_agent),
        AgentTool(agent=hotel_agent),
        AgentTool(agent=activity_agent)
    ]
)
```

## How It Works

1. **User Query** → Coordinator receives request
2. **Routing Decision** → Coordinator reads agent descriptions, decides who can help
3. **Delegation** → Coordinator invokes appropriate specialist(s)
4. **Synthesis** → Coordinator combines results into cohesive plan
5. **Response** → User receives complete itinerary

## Benefits

✅ Each agent has focused expertise  
✅ Easy to add new specialists (restaurant_agent, transport_agent)  
✅ Can swap out specialists without affecting others  
✅ Clear separation of concerns

## When to Use

- Query could be handled by one specialist OR needs multiple
- Specialists have distinct tool sets
- New capabilities added incrementally

---

# Pattern 2: Sequential Pipeline

## The Content Creation Assembly Line

**Scenario:** Generate a blog post from scratch to publish-ready

### Architecture
```python
from google.adk.agents import Agent
from google.adk.agents.workflows import SequentialAgent

# Define specialists
researcher = Agent(
    name="researcher",
    description="Gathers facts and sources",
    model="gemini-2.0-flash",
    instruction="Search for accurate information and reliable sources.",
    tools=[GoogleSearch(), ScholarSearch()],
    output_key="research_findings"
)

writer = Agent(
    name="writer",
    description="Creates engaging content",
    model="gemini-2.0-flash",
    instruction="Use research from {research_findings} to write engaging content.",
    output_key="draft_content"
)

editor = Agent(
    name="editor",
    description="Refines language and structure",
    model="gemini-2.0-flash",
    instruction="Edit this draft: {draft_content}. Improve clarity and flow.",
    output_key="edited_content"
)

fact_checker = Agent(
    name="fact_checker",
    description="Verifies claims and citations",
    model="gemini-2.0-flash",
    instruction="Verify facts in: {edited_content}. Check all claims.",
    output_key="final_content"
)

# Chain them together
content_pipeline = SequentialAgent(
    name="content_pipeline",
    agents=[researcher, writer, editor, fact_checker]
)
```

## How State Flows

```
User: "Write about quantum computing breakthroughs"
  ↓
Researcher: gathers data → stores in research_findings
  ↓
Writer: reads {research_findings} → creates draft → stores in draft_content
  ↓
Editor: reads {draft_content} → improves writing → stores in edited_content
  ↓
Fact-Checker: reads {edited_content} → verifies → stores in final_content
  ↓
User receives: final_content
```

## State Dictionary
All agents share a dictionary that accumulates results:
```python
{
    "research_findings": "...",
    "draft_content": "...",
    "edited_content": "...",
    "final_content": "..."
}
```

## When to Use

- Tasks have clear dependencies (can't edit before writing)
- Each step adds value to previous step's output
- Order matters for quality

---

# Pattern 3: Parallel + Synthesis

## Competitive Analysis at Scale

**Scenario:** Research 3 competitors simultaneously, then compare

### Architecture
```python
from google.adk.agents import Agent
from google.adk.agents.workflows import ParallelAgent, SequentialAgent

# Specialist researchers
competitor_a_researcher = Agent(
    name="CompetitorA_analyst",
    description="Researches Competitor A",
    model="gemini-2.0-flash",
    instruction="Research Competitor A thoroughly using web search and financial data.",
    tools=[WebSearch(), FinancialDataAPI()],
    output_key="competitor_a_data"
)

competitor_b_researcher = Agent(
    name="CompetitorB_analyst",
    description="Researches Competitor B",
    model="gemini-2.0-flash",
    instruction="Research Competitor B thoroughly using web search and financial data.",
    tools=[WebSearch(), FinancialDataAPI()],
    output_key="competitor_b_data"
)

competitor_c_researcher = Agent(
    name="CompetitorC_analyst",
    description="Researches Competitor C",
    model="gemini-2.0-flash",
    instruction="Research Competitor C thoroughly using web search and financial data.",
    tools=[WebSearch(), FinancialDataAPI()],
    output_key="competitor_c_data"
)

# Parallel execution
parallel_research = ParallelAgent(
    name="parallel_research",
    agents=[competitor_a_researcher, competitor_b_researcher, competitor_c_researcher]
)

# Synthesis agent
synthesis_agent = Agent(
    name="synthesizer",
    description="Compares and analyzes competitor data",
    model="gemini-2.0-flash",
    instruction="""Analyze:
    - Competitor A: {competitor_a_data}
    - Competitor B: {competitor_b_data}
    - Competitor C: {competitor_c_data}

    Provide comparative analysis and strategic insights."""
)

# Complete workflow
competitive_analysis = SequentialAgent(
    name="competitive_analysis",
    agents=[parallel_research, synthesis_agent]
)
```

## Execution Timeline

**Sequential Approach:** 30 seconds × 3 = 90 seconds  
**Parallel Approach:** 30 seconds (all at once!) + 10 seconds synthesis = 40 seconds

```
Sequential: [A]──[B]──[C]──[Synthesis]  (90s)
Parallel:   [A]
            [B]──[Synthesis]             (40s)
            [C]
```

## When to Use

- Tasks are independent (no shared dependencies)
- Time is critical
- Data from multiple sources needs combining
- Comparing alternatives or options

---

# 🛠️ HANDS-ON: Build a Multi-Agent System (30 minutes)

## Exercise Goal
Create a news analysis system with specialized agents

## System Architecture

```
User Query: "Summarize tech news from today"
     ↓
[Coordinator Agent]
     ↓
  ┌──┴──┐
[News Gatherer] ← Searches for articles
     ↓
[Summarizer] ← Creates concise summary
     ↓
[Sentiment Analyzer] ← Analyzes tone
     ↓
Final Report to User
```

## Implementation Steps

### Step 1: Create Project Structure (5 min)
```bash
mkdir news-analyzer
cd news-analyzer
touch news_system.py
```

### Step 2: Define Specialist Agents (10 min)
```python
from google.adk.agents import Agent
from google.adk.agents.workflows import SequentialAgent
from google.adk.tools import google_search

# Agent 1: News gatherer
news_gatherer = Agent(
    name="news_gatherer",
    description="Searches for latest news articles",
    model="gemini-2.0-flash",
    instruction="Search for recent news about: {topic}. Find credible sources.",
    tools=[google_search],
    output_key="news_articles"
)

# Agent 2: Summarizer
summarizer = Agent(
    name="summarizer",
    description="Creates concise summaries",
    model="gemini-2.0-flash",
    instruction="Summarize these articles: {news_articles}. Be concise and objective.",
    output_key="summary"
)

# Agent 3: Sentiment analyzer
sentiment_analyzer = Agent(
    name="sentiment_analyzer",
    description="Analyzes sentiment and tone",
    model="gemini-2.0-flash",
    instruction="Analyze sentiment in: {summary}. Identify overall tone and key themes.",
    output_key="analysis"
)
```

### Step 3: Create Pipeline (5 min)
```python
news_pipeline = SequentialAgent(
    name="news_analysis_pipeline",
    agents=[news_gatherer, summarizer, sentiment_analyzer]
)
```

### Step 4: Test It! (10 min)
```python
# Run the pipeline
result = news_pipeline.run({
    "topic": "artificial intelligence regulation 2025"
})

# Access the final analysis
print("=== News Analysis ===")
print(result.get("analysis"))

# Or see all accumulated state
from pprint import pprint
print("\n=== Full State ===")
pprint(result)
```

## Challenge Extensions

**Easy:** Add a fact-checker agent to verify claims  
**Medium:** Make it parallel—analyze multiple topics simultaneously  
**Hard:** Add a trending topics agent that suggests what to research

---

# State Management & Memory

## Understanding State in Multi-Agent Systems

### Shared State Dictionary
All agents in a workflow share a common dictionary:

```python
# Initial state
state = {"user_query": "Plan a trip to Paris"}

# After agent1 runs
state = {
    "user_query": "Plan a trip to Paris",
    "flight_options": [...],  # agent1's output_key
}

# After agent2 runs
state = {
    "user_query": "Plan a trip to Paris",
    "flight_options": [...],
    "hotel_options": [...],   # agent2's output_key
}
```

### Accessing Previous Results

**Method 1: Placeholder syntax in instruction**
```python
from google.adk.agents import Agent

agent2 = Agent(
    name="hotel_agent",
    model="gemini-2.0-flash",
    description="Books hotels based on attractions",
    instruction="Book hotels near these attractions: {attractions_list}"
)
```

**Method 2: Access full state dictionary**
```python
def custom_logic(state):
    flights = state["flight_options"]
    hotels = state["hotel_options"]
    # Your logic here
```

## Memory Management

### Types of Memory

**1. Session Memory (Short-term)**
- Persists within a conversation
- Automatically managed by ADK
- Great for context in multi-turn chats

**2. Long-term Memory**
- Persists across sessions
- Integrated with Vertex AI Memory Bank
- Remember user preferences, past decisions

### Controlling Memory Loading

```python
from google.adk.agents import Agent
from google.adk.tools import PreloadMemoryTool

agent = Agent(
    name="assistant",
    model="gemini-2.0-flash",
    description="Assistant with memory control",
    instruction="Help users and remember their preferences.",
    tools=[PreloadMemoryTool()],  # Explicit memory control
    # Now agent decides WHEN to load memories
    # Reduces token usage
)
```

## Best Practices

### ✅ Do's
- Use clear, descriptive output_key names
- Document what each agent adds to state
- Keep state dictionary flat when possible
- Use PreloadMemoryTool for cost optimization

### ❌ Don'ts
- Don't store massive objects in state
- Don't assume state structure—validate it
- Don't use conflicting output_key names
- Don't load all memory by default in production

## Custom Session Services

For advanced needs (custom databases, existing systems):

```python
class MySessionService(BaseSessionService):
    async def create_session(self, session_id):
        # Your custom logic
        pass
    
    async def get_session(self, session_id):
        # Your custom logic
        pass
```

---

# Testing & Evaluation Strategies

## Why Testing Matters for AI Agents

**Traditional Software:** Deterministic behavior, predictable outputs  
**AI Agents:** Non-deterministic, need different testing approaches

**Risks Without Testing:**
- Hallucinations make it to production
- Agent uses wrong tools
- Security vulnerabilities
- Degraded performance over time

## ADK Evaluation Framework

### 1. Define Test Cases

Create `evaluation.test.json`:
```json
{
  "test_cases": [
    {
      "name": "customer_refund_scenario",
      "input": "I want a refund for order #12345",
      "expected_behavior": {
        "tool_used": "check_order_status",
        "sentiment": "professional",
        "includes": ["order status", "refund policy"]
      }
    },
    {
      "name": "multiple_issues",
      "input": "My order is late and damaged",
      "expected_behavior": {
        "tools_used": ["check_order", "open_ticket"],
        "tone": "empathetic"
      }
    }
  ]
}
```

### 2. Run Evaluations

**Command Line:**
```bash
adk eval --config evaluation.test.json --agent my_agent.py
```

**Web UI:**
- Visual interface for running tests
- Compare results side-by-side
- Export results for analysis

### 3. Custom Evaluators

```python
from google.adk.eval import BaseEvaluator

class RougeEvaluator(BaseEvaluator):
    """Measures summary quality using ROUGE-1 score"""

    def evaluate(self, predicted, expected):
        score = self.calculate_rouge(predicted, expected)
        return {
            "score": score,
            "passed": score > 0.7
        }
```

## Testing Strategy Pyramid

```
           [Integration Tests]
          (End-to-end workflows)
               /        \
          [Agent Tests]
        (Individual agent behavior)
           /              \
     [Tool Tests]     [Unit Tests]
  (Tool functionality) (Helper functions)
```

## What to Test

### ✅ Response Quality
- Accuracy of information
- Relevance to query
- Tone and style

### ✅ Tool Usage
- Correct tool selection
- Proper parameter passing
- Error handling

### ✅ Execution Path
- Correct agent routing
- State transitions
- Loop termination

### ✅ Edge Cases
- Missing information
- Ambiguous queries
- Error scenarios

## Monitoring in Production

**Key Metrics:**
- Response latency
- Tool call success rate
- User feedback (thumbs up/down)
- Error frequency
- Cost per interaction (tokens used)

**ADK Agent Engine UI provides:**
- Real-time trace logs
- Performance dashboards
- Session replay
- Alert configuration
