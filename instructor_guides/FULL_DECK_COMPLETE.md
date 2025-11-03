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

---

# Security & Best Practices

## Security Principles for Production Agents

### 1. Input Validation & Screening

**Before LLM Processing:**
```python
def before_model_callback(request):
    """Intercept and validate input before LLM sees it"""
    
    # Check for injection attempts
    if contains_malicious_patterns(request.input):
        raise SecurityException("Blocked: potential injection")
    
    # Sanitize input
    clean_input = sanitize(request.input)
    request.input = clean_input
    
    return request
```

**Use Cases:**
- Block prompt injection attempts
- Filter PII (personally identifiable information)
- Enforce content policies
- Rate limiting per user

### 2. Output Validation & Moderation

**After LLM Response:**
```python
def after_model_callback(response):
    """Validate output before returning to user"""
    
    # Check for prohibited content
    if contains_prohibited_content(response.text):
        return sanitized_response()
    
    # Verify no PII leaked
    if contains_pii(response.text):
        response.text = redact_pii(response.text)
    
    return response
```

### 3. Tool Confirmation (HITL - Human-in-the-Loop)

**For Sensitive Operations:**
```python
from adk.tools import ToolConfirmation

delete_database = Tool(
    name="delete_database",
    function=delete_db,
    confirmation=ToolConfirmation(
        required=True,
        message="⚠️ Delete database {database_name}? This cannot be undone."
    )
)
```

**When to Use HITL:**
- Financial transactions
- Data deletion
- External communications (emails, posts)
- Access control changes

### 4. Scoped Permissions

**Principle of Least Privilege:**
```python
# ❌ Bad: Agent has full database access
agent = LLMAgent(
    name="customer_service",
    tools=[full_database_access]
)

# ✅ Good: Agent has limited, specific access
agent = LLMAgent(
    name="customer_service",
    tools=[
        read_customer_info,      # Read-only
        update_customer_address, # Specific write
        # NO delete operations
    ]
)
```

### 5. Audit Logging

**Track Everything:**
```python
logger.info({
    "timestamp": now(),
    "agent": agent_name,
    "user": user_id,
    "query": sanitized_query,
    "tools_used": [tool_names],
    "outcome": "success/failure",
    "tokens_used": count
})
```

## Best Practices from slide18.html

### Design Principles
- **Single responsibility per agent** - Each agent does ONE thing well
- **Clear agent descriptions** - Enables proper routing
- **Comprehensive tool docstrings** - LLM needs context
- **Separation of concerns** - Keep logic modular

### State Management
- **Use shared dictionaries** - Standard pattern for passing state
- **Define clear output_key parameters** - Know what each agent contributes
- **PreloadMemoryTool for control** - Optimize token usage
- **Custom session services when needed** - Integrate existing systems

### Testing Strategy
- **Unit test individual agents** - Verify behavior in isolation
- **Integration test workflows** - Test agent collaboration
- **Use evaluation framework** - Systematic quality assurance
- **Track metrics over time** - Detect degradation early

### Security & Safety
- **Implement callbacks for validation** - Defense in depth
- **Use HITL for sensitive operations** - Human oversight
- **Configure content filters** - Block inappropriate content
- **Scope identity permissions** - Least privilege principle

## Production Readiness Checklist

```
□ Input validation implemented
□ Output moderation configured
□ HITL for sensitive operations
□ Scoped permissions verified
□ Audit logging enabled
□ Rate limiting configured
□ Error handling comprehensive
□ Monitoring dashboards set up
□ Evaluation suite created
□ Documentation complete
□ Team trained on incident response
```

---

# Deployment Options: From Dev to Production

## Development → Production Journey

```
Local Dev → Testing → Staging → Production
(Web UI)   (CI/CD)   (Preview)  (Vertex AI)
```

## 1. Local Development

### ADK Web UI
```bash
adk web
# Opens browser at localhost:8080
```

**Features:**
- Interactive chat interface
- Event inspection & debugging
- Latency trace logs
- Voice/microphone input support
- HTML artifact rendering
- Export conversations to JSON

**Perfect for:**
- Rapid prototyping
- Testing agent behavior
- Debugging tool calls
- Demonstrating to stakeholders

## 2. Cloud Run (Containerized Deployment)

```bash
# Build container
docker build -t my-agent .

# Deploy to Cloud Run
gcloud run deploy my-agent \
  --image gcr.io/project/my-agent \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated
```

**Benefits:**
- Auto-scaling (0 to N instances)
- Pay only for actual usage
- Simple HTTP endpoint
- Quick deployment

**Best for:**
- APIs and webhooks
- Microservices architecture
- Cost-sensitive workloads

## 3. Vertex AI Agent Engine (Managed Service)

### Deploy via CLI
```bash
adk deploy \
  --agent-path ./my_agent.py \
  --display-name "Customer Service Agent" \
  --description "Handles customer inquiries" \
  --memory-service vertex \
  --region us-central1
```

### Features
- **Fully managed infrastructure** - No server management
- **Auto-scaling** - Handles traffic spikes
- **Integrated monitoring** - Agent Engine UI dashboard
- **Session management** - Built-in persistence
- **100+ pre-built connectors** - BigQuery, AlloyDB, APIs
- **Security controls** - IAM, VPC, content filtering

### Agent Engine UI
Access at: console.cloud.google.com/vertex-ai/agents

**Capabilities:**
- List and manage all deployed agents
- View and manage sessions
- Real-time trace logs
- Performance metrics (latency, requests, CPU)
- Debug agent actions
- Configure security policies

**Best for:**
- Enterprise production deployments
- Mission-critical applications
- Need for observability
- Compliance requirements

## 4. Custom Infrastructure

**When you need:**
- Existing infrastructure integration
- Specific runtime requirements
- Custom scaling logic
- Hybrid cloud deployment

**ADK is containerizable:**
- Kubernetes deployments
- On-premises servers
- Edge computing
- Multi-cloud strategies

## Deployment Architecture Patterns

### Pattern 1: API Gateway
```
User → API Gateway → Cloud Run → Agent
```
Good for: Public-facing applications

### Pattern 2: Event-Driven
```
Event → Pub/Sub → Cloud Function → Agent
```
Good for: Background processing, workflows

### Pattern 3: Enterprise Hub
```
Application → Vertex AI → [Agent1, Agent2, Agent3]
```
Good for: Multiple agents, shared infrastructure

## Scaling Considerations

| Deployment Type | Scale | Cost | Management | Use Case |
|----------------|-------|------|------------|----------|
| Local | Single user | Free | Manual | Development |
| Cloud Run | 100s requests/sec | Low | Minimal | APIs, webhooks |
| Vertex AI | 1000s+ requests/sec | Medium | Managed | Production apps |
| Custom K8s | Unlimited | Variable | High | Enterprise scale |

## Production Deployment Checklist

```
□ Environment variables configured
□ API credentials secured (Secret Manager)
□ Monitoring and alerting set up
□ Logging configured
□ Rate limiting implemented
□ Health check endpoints created
□ Backup and disaster recovery planned
□ Load testing completed
□ Documentation updated
□ Team trained on deployment
```

---

# Advanced Features & Future Roadmap

## Recent Innovations (v1.0 - v1.17.0)

### Hot Reload (v1.6.1)
**Continuous development mode:**
```bash
adk web --reload_agents
# Agents automatically reload when you edit code
# No more stop/restart cycles!
```

**Impact:** 10x faster development iteration

### Agent2Agent Protocol (A2A)
**Vendor-neutral agent communication standard**

```python
# ADK agent calling agent from another framework
response = await adk_agent.call_a2a_agent(
    endpoint="https://other-framework.com/agent",
    message="Analyze this data"
)
```

**Industry Support:**
- ✅ Microsoft (Azure AI Foundry, Copilot Studio)
- ✅ SAP (Joule AI assistant)
- ✅ Zoom (Agentspace integration)
- ✅ Auth0 (secure multi-agent communication)

**Impact:** Build agent ecosystems, not silos

### Agent Config (YAML-based)
**No-code agent creation:**

```yaml
agent:
  name: customer_service
  description: Handles customer inquiries
  model: gemini-2.0-flash
  tools:
    - google_search
    - check_order_status
  instructions: |
    Be professional and empathetic.
    Always verify order numbers.
```

**Impact:** Non-programmers can build agents

### Voice & Multimodal (Gemini Live API)

**Real-time conversational agents:**
```python
voice_agent = LLMAgent(
    name="voice_assistant",
    model="gemini-2.0-flash-live",
    streaming=True,
    audio_config=AudioConfig(
        input_encoding="LINEAR16",
        output_encoding="LINEAR16"
    )
)
```

**Use Cases:**
- Customer service hotlines
- Virtual assistants
- Accessibility applications
- Interactive tutoring

**Learn More:** DeepLearning.AI course "Building Live Voice Agents with Google's ADK"

## What's Coming (Roadmap Highlights)

### Advanced Context Caching
**Problem:** Repeated context consumes tokens  
**Solution:** Smart caching reduces costs by 60-80%

```python
agent = LLMAgent(
    name="analyst",
    context_caching=True,  # Reuse context across calls
    cache_ttl=3600         # Cache for 1 hour
)
```

### Enhanced Contribution Guidelines
**Community-driven development:**
- Easier process for contributing tools
- Plugin marketplace
- Community agent templates

### MCP (Model Context Protocol) Expansion
**More pre-built integrations:**
- Slack, Notion, Jira
- GitHub, GitLab
- Salesforce, HubSpot
- Database connectors

### Multi-Modal Evolution
**Beyond voice:**
- Image understanding
- Video analysis
- Document processing
- Real-time video streaming

## Learning Resources

### Official Resources
📚 **Documentation:** cloud.google.com/vertex-ai/docs/adk  
🎥 **Intro Video:** "Introducing Agent Development Kit" (25 min)  
💻 **Codelab:** "ADK Crash Course" (interactive tutorial)  
📦 **Samples:** github.com/google/adk-samples (25+ examples)

### Structured Learning
🎓 **DeepLearning.AI Course:**
- "Building Live Voice Agents with Google's ADK"
- Taught by Google ML Engineers
- Covers sessions, callbacks, multi-agent orchestration

### Community
💬 **ADK Community Calls:** Monthly (announced via social)  
🏆 **Hackathons:** Watch for next event (previous: May-June 2025)  
📰 **Release Notes:** bi-weekly updates

## Sample Agent Catalog

**By Domain:**
- `academic-research` - Literature review and citation
- `blog-writer` - Content creation pipeline
- `customer-service` - Support ticket handling
- `data-engineering` - ETL workflows
- `financial-advisor` - Portfolio analysis
- `marketing-agency` - Campaign planning
- `medical-pre-authorization` - Healthcare workflows
- `personalized-shopping` - E-commerce recommendations
- `travel-concierge` - Trip planning
- `software-bug-assistant` - Code debugging

**By Pattern:**
- `realtime-conversational-agent` - Voice interactions
- `RAG implementations` - Retrieval-augmented generation
- `sequential-workflows` - Pipeline examples
- `parallel-agents` - Concurrent execution

## Quick Wins for Your Organization

### Week 1: Proof of Concept
- Clone relevant sample agent
- Customize for your use case
- Demo to stakeholders

### Week 2: Pilot
- Build custom tools for your APIs
- Test with real users
- Gather feedback

### Month 1: Production
- Deploy to Vertex AI Agent Engine
- Implement monitoring
- Establish evaluation pipeline

### Month 2: Scale
- Add more specialist agents
- Optimize costs and performance
- Train team on best practices

---

# Workshop Wrap-Up & Next Steps

## What We Covered Today

### ✅ Foundations
- Why multi-agent systems beat monolithic approaches
- ADK's three core principles (model-agnostic, deployment-agnostic, framework-compatible)
- Agent types: LLM, Workflow, Custom

### ✅ Hands-On Experience
- Built your first agent
- Created a multi-agent news analysis system
- Explored real patterns: router, sequential, parallel, iterative

### ✅ Production Readiness
- State management and memory
- Testing and evaluation strategies
- Security best practices
- Deployment options

## Key Takeaways

### 1. Start Simple, Scale Smart
```
Single Agent → Specialized Team → Complex Orchestration
```
Don't over-engineer. Add complexity only when needed.

### 2. Agents Are Software Components
Apply familiar patterns:
- Single responsibility principle
- Separation of concerns
- Version control and CI/CD
- Comprehensive testing

### 3. Production is Different from Prototype
**Must have:**
- Input/output validation
- Human-in-the-loop for sensitive ops
- Monitoring and alerting
- Evaluation framework

### 4. The Future is Multi-Agent
Google's bet: Specialized agents collaborating > Single super agent

## Your Next Steps

### Immediate (This Week)
1. **Explore Samples**
   - Clone github.com/google/adk-samples
   - Find one similar to your use case
   - Run it locally

2. **Complete ADK Crash Course**
   - Interactive codelab at codelabs.developers.google.com
   - Hands-on exercises
   - ~2 hours

3. **Join Community**
   - Star the GitHub repo
   - Join next community call
   - Follow release notes

### Short Term (Next 2 Weeks)
1. **Build a Proof of Concept**
   - Identify a use case in your organization
   - Start with single agent
   - Demo to stakeholders

2. **Learn Testing**
   - Write evaluation test cases
   - Run automated tests
   - Track metrics

3. **Study DeepLearning.AI Course** (if building voice agents)
   - Comprehensive coverage
   - Taught by Google engineers

### Medium Term (Next Month)
1. **Pilot with Real Users**
   - Deploy to Cloud Run or Vertex AI
   - Gather feedback
   - Iterate based on usage

2. **Implement Best Practices**
   - Add security callbacks
   - Set up monitoring
   - Create documentation

3. **Scale Your System**
   - Add specialist agents
   - Optimize performance
   - Train your team

## Resources Cheat Sheet

### Documentation & Guides
- **Official Docs:** cloud.google.com/vertex-ai/docs/adk
- **API Reference:** Complete SDK documentation
- **Architecture Guide:** Design patterns and best practices

### Video & Interactive Learning
- **Intro Video:** youtube.com/watch?v=zgrOwow_uTQ (25 min)
- **Codelab:** codelabs.developers.google.com/onramp
- **DeepLearning.AI Course:** Voice agents masterclass

### Code & Examples
- **Samples Repo:** github.com/google/adk-samples
- **Starter Templates:** 25+ production-quality agents
- **Community Contributions:** Growing ecosystem

### Support & Community
- **Stack Overflow:** Tag `google-adk`
- **GitHub Issues:** Bug reports and feature requests
- **Community Calls:** Monthly updates and Q&A

## Common Pitfalls to Avoid

❌ **Building a single agent that does everything**  
✅ Break into specialists with clear responsibilities

❌ **No testing until production**  
✅ Build evaluation suite from day one

❌ **Ignoring security until too late**  
✅ Implement callbacks and validation early

❌ **Over-engineering from the start**  
✅ Start simple, add complexity as needed

❌ **Not monitoring in production**  
✅ Set up logging and metrics before launch

## Q&A Time

**Open floor for questions:**
- Technical questions about implementation
- Use case discussions
- Troubleshooting exercises
- Career and learning paths
- Enterprise adoption strategies

## Stay Connected

**Share your builds:**
- Tag us on social media
- Contribute to open source
- Write about your experiences

**We want to see:**
- Novel use cases
- Creative agent combinations
- Performance optimizations
- Best practice innovations

---

## Thank You!

**Remember:** The best way to learn is by building.

Start small, iterate fast, deploy confidently.

**You now have the tools to build production-ready multi-agent systems. Go build something amazing! 🚀**

---

# Troubleshooting Common Issues

## Setup & Installation

### Problem: `pip install google-cloud-adk` fails
**Solutions:**
```bash
# Update pip first
pip install --upgrade pip

# Use Python 3.9+ (3.11+ recommended)
python --version

# Try with explicit Python version
python3.11 -m pip install google-cloud-adk

# Use virtual environment
python -m venv adk-env
source adk-env/bin/activate  # On Windows: adk-env\Scripts\activate
pip install google-cloud-adk
```

### Problem: Import errors or missing dependencies
**Solutions:**
```bash
# Verify installation
pip show google-cloud-adk

# Install specific version
pip install google-cloud-adk==1.17.0

# Check for conflicts
pip check
```

## Authentication & Credentials

### Problem: "Could not automatically determine credentials"
**Solutions:**
```bash
# Set up Application Default Credentials
gcloud auth application-default login

# Or set environment variable
export GOOGLE_APPLICATION_CREDENTIALS="/path/to/key.json"

# Verify credentials
gcloud auth list
```

### Problem: API not enabled
**Error:** "API [aiplatform.googleapis.com] not enabled"
**Solution:**
```bash
gcloud services enable aiplatform.googleapis.com
gcloud services enable cloudaicompanion.googleapis.com
```

## Agent Behavior Issues

### Problem: Agent not using tools correctly
**Symptoms:** Agent tries to answer without searching, uses wrong tool

**Solutions:**
1. **Improve tool docstrings:**
```python
# ❌ Bad docstring
def search(query):
    """Searches"""
    
# ✅ Good docstring
def search(query: str) -> list:
    """Search the web for current information.
    
    Use this when you need up-to-date information, recent news,
    or facts that might have changed since your training.
    
    Args:
        query: Search terms or question to look up
        
    Returns:
        List of relevant search results with titles and snippets
    """
```

2. **Make agent description more specific:**
```python
# ❌ Vague
description="A helpful agent"

# ✅ Specific
description="Searches recent tech news and provides summaries of major developments"
```

3. **Add explicit instructions:**
```python
instructions="""
ALWAYS use the search tool for current events.
NEVER make up information about recent dates.
"""
```

### Problem: Agent loops infinitely
**Symptoms:** LoopAgent never terminates, keeps refining

**Solutions:**
```python
loop_agent = LoopAgent(
    name="refinement_loop",
    agents=[generator, reviewer],
    max_iterations=5,  # Add hard limit
    stop_condition=lambda state: state.get("quality_score", 0) > 0.8
)
```

### Problem: State not passing between agents
**Symptoms:** Agent can't access previous agent's output

**Solutions:**
```python
# Ensure output_key is set
agent1 = LLMAgent(
    output_key="research_data"  # ← Must set this
)

# Reference it correctly in next agent
agent2 = LLMAgent(
    instructions="Analyze this data: {research_data}"  # ← Use placeholder
)
```

## Performance Issues

### Problem: Slow responses
**Causes & Solutions:**

1. **Too many tool calls:**
```python
# Add caching
agent = LLMAgent(
    name="fast_agent",
    model="gemini-2.0-flash",  # Faster model
    tools=[limited_tool_set],   # Fewer tools to choose from
)
```

2. **Memory loading everything:**
```python
# Use PreloadMemoryTool instead of auto-load
tools=[PreloadMemoryTool(), other_tools]
```

3. **Sequential when could be parallel:**
```python
# ❌ Slow sequential
workflow = SequentialAgent(agents=[a, b, c])  # If independent

# ✅ Fast parallel
workflow = ParallelAgent(agents=[a, b, c])    # Run simultaneously
```

### Problem: High costs (token usage)
**Solutions:**
1. Use smaller models for simple tasks
2. Implement context caching
3. Use PreloadMemoryTool
4. Truncate unnecessary history
5. Cache tool results when possible

## Deployment Issues

### Problem: Works locally but fails in Cloud Run
**Common causes:**
- Missing environment variables
- Insufficient permissions
- Timeout too short
- Memory limits

**Solutions:**
```bash
# Increase timeout and memory
gcloud run deploy my-agent \
  --timeout=300 \
  --memory=2Gi \
  --set-env-vars="KEY=value"
```

### Problem: Cannot access Vertex AI after deployment
**Solution:**
```bash
# Grant service account proper permissions
gcloud projects add-iam-policy-binding PROJECT_ID \
  --member="serviceAccount:SERVICE_ACCOUNT" \
  --role="roles/aiplatform.user"
```

## Getting Help

### Debug Mode
```python
import logging
logging.basicConfig(level=logging.DEBUG)

# Or in ADK
agent = LLMAgent(
    name="debug_agent",
    verbose=True  # Show all tool calls and decisions
)
```

### Check Trace Logs
```python
# Access execution details
result = agent.run(query)
print(result.trace)  # See step-by-step execution
```

### Community Support
- **GitHub Issues:** github.com/google/adk/issues
- **Stack Overflow:** Tag `google-adk`
- **Community Calls:** Ask during monthly calls

## Emergency Debugging Checklist

When things go wrong, check these in order:

```
□ Python version correct (3.9+)
□ ADK installed (`pip show google-cloud-adk`)
□ Credentials configured (`gcloud auth list`)
□ Required APIs enabled
□ Tool docstrings comprehensive
□ output_key set on all agents
□ Placeholders match output_key names
□ Max iterations set on LoopAgents
□ Verbose/debug mode enabled
□ Check trace logs for actual behavior
```

---

# Real-World Use Cases & Success Patterns

## Enterprise Production Deployments

### Renault Group - Automotive Manufacturing
**Challenge:** Complex supply chain coordination across global operations  
**Solution:** Multi-agent system for logistics optimization
- Inventory management agents
- Supplier coordination agents
- Quality control monitoring

**Results:** Improved coordination, reduced response time

### Box - Cloud Content Management
**Challenge:** Enterprise content search and management at scale  
**Solution:** Intelligent document processing and retrieval
- Document analysis agents
- Search optimization
- Access control coordination

### Revionics - Retail Analytics
**Challenge:** Real-time pricing optimization across thousands of SKUs  
**Solution:** Multi-agent analytics pipeline
- Market research agents
- Competitive analysis
- Price optimization recommendation

## Proven Patterns by Industry

### Financial Services

**Use Case:** Fraud Detection System
```
Customer Transaction
    ↓
[Transaction Analyzer] → Risk assessment
    ↓
[Pattern Matcher] → Historical comparison
    ↓
[Compliance Checker] → Regulatory validation
    ↓
[Alert Generator] → (If suspicious) Human review
```

**Key Agents:**
- Real-time transaction monitor
- Historical pattern analyzer
- Compliance verification
- Alert escalation

**Impact:** Faster detection, fewer false positives

### Healthcare

**Use Case:** Medical Pre-Authorization
```
Authorization Request
    ↓
[Eligibility Checker] → Insurance validation
    ↓
[Medical Necessity Reviewer] → Clinical guidelines
    ↓
[Prior Auth Lookup] → Historical approvals
    ↓
[Decision Synthesizer] → Approve/Deny/Escalate
```

**Key Agents:**
- Insurance eligibility verification
- Medical guidelines checker
- Prior authorization database search
- Clinical decision support

**Sample:** `medical-pre-authorization` in github.com/google/adk-samples

### E-Commerce

**Use Case:** Personalized Shopping Assistant
```
User Query: "Need running shoes for marathon training"
    ↓
[Preference Analyzer] → Extract requirements
    ↓
[Product Searcher] → Find matches
    ↓
[Review Analyzer] → Check ratings
    ↓
[Comparison Agent] → Create recommendations
```

**Key Agents:**
- Customer preference extraction
- Inventory search
- Review sentiment analysis
- Price comparison
- Recommendation synthesis

**Sample:** `personalized-shopping` in adk-samples

### Customer Service

**Use Case:** Intelligent Support Ticket Routing
```
Support Ticket
    ↓
[Classifier] → Categorize issue
    ↓
[Priority Scorer] → Assess urgency
    ↓
[Router] → Assign to specialist
    ↓
[Specialist Agents] → Technical/Billing/General
    ↓
[Quality Reviewer] → Before sending response
```

**Key Benefits:**
- 80% automated resolution
- 24/7 availability
- Consistent quality
- Human escalation when needed

**Sample:** `customer-service` in adk-samples

### Marketing & Content

**Use Case:** Multi-Channel Campaign Generator
```
Campaign Brief
    ↓
[Research Agent] → Market/competitor analysis
    ↓
[Parallel Execution] → Email + Social + Blog
    ↓
[Email Writer] [Social Creator] [Blog Author]
    ↓
[Brand Reviewer] → Consistency check
    ↓
[Performance Predictor] → Expected metrics
```

**Key Agents:**
- Market research
- Content generation (by channel)
- Brand consistency checker
- A/B testing recommendation

**Sample:** `marketing-agency` in adk-samples

### Data Engineering

**Use Case:** Automated ETL Pipeline
```
Raw Data Sources
    ↓
[Schema Detector] → Understand structure
    ↓
[Data Validator] → Check quality
    ↓
[Transformer] → Clean and reshape
    ↓
[Loader] → BigQuery/warehouse
    ↓
[Monitor] → Data quality metrics
```

**Key Agents:**
- Schema inference
- Data validation
- Transformation logic
- Load coordination
- Quality monitoring

**Sample:** `data-engineering` in adk-samples

## Hackathon Winners (May-June 2025)

### Grand Prize: Travel Planning Suite
**Multi-agent system combining:**
- Flight optimization
- Hotel recommendations
- Local experience curation
- Budget management
- Itinerary generation

**Why it won:** Comprehensive multi-agent orchestration, real API integrations

### Runner-Up: Code Review Assistant
**Agents:**
- Security vulnerability scanner
- Performance analyzer
- Style checker
- Documentation generator
- PR summary creator

**Why it stood out:** Practical developer tool, immediate value

## Patterns That Work

### ✅ Start with Core Value
- Identify ONE high-value workflow
- Build minimum viable agent system
- Prove ROI before expanding

### ✅ Human-in-the-Loop for Trust
- Keep humans involved in critical decisions
- Use HITL for sensitive operations
- Build confidence gradually

### ✅ Incremental Specialist Addition
```
Week 1: Single agent → proves concept
Week 2: Add one specialist → shows collaboration
Week 3: Add coordinator → demonstrates orchestration
Week 4: Optimize and scale
```

### ✅ Measure Everything
- Response accuracy
- Task completion rate
- User satisfaction
- Time saved
- Cost per transaction

## Anti-Patterns to Avoid

### ❌ Building Everything at Once
**Problem:** Complex system, hard to debug  
**Solution:** Start with one agent, add incrementally

### ❌ No Fallback to Human
**Problem:** System fails on edge cases  
**Solution:** Always have escalation path

### ❌ Ignoring the 80/20 Rule
**Problem:** Trying to handle every edge case  
**Solution:** Automate the 80%, human handles the 20%

### ❌ Over-Promising Capabilities
**Problem:** Unrealistic expectations  
**Solution:** Start with narrow, well-defined scope

## Your Turn: Brainstorm Session

**Think about your organization:**

1. What repetitive tasks could be automated?
2. What decisions require multiple data sources?
3. What processes involve multiple steps?
4. What workflows need 24/7 availability?
5. What tasks are done inconsistently by humans?

**Ideal ADK candidates:**
- Clear inputs and outputs
- Measurable success criteria
- Access to necessary data/APIs
- Tolerance for learning period
- Human oversight possible

## Getting Started Template

```python
# Step 1: Define the problem
PROBLEM = "Automated customer order status updates"

# Step 2: List required capabilities
CAPABILITIES = [
    "Query order database",
    "Check shipping status",
    "Format response professionally",
    "Escalate complex issues"
]

# Step 3: Map to agents
# - Order lookup agent (database query)
# - Shipping tracker agent (API integration)
# - Response formatter agent (LLM)
# - Escalation handler (HITL)

# Step 4: Build MVP
# Start with order lookup only
# Add others incrementally

# Step 5: Test and iterate
```

## Success Metrics from Real Deployments

**Customer Service:**
- 70-80% automated resolution
- 3x faster response time
- 24/7 availability
- Consistent quality

**Data Analysis:**
- 10x faster report generation
- 90% accuracy on structured queries
- Reduced analyst burden

**Content Creation:**
- 5x productivity increase
- Maintained quality standards
- Faster iteration cycles

**Process Automation:**
- 60-80% time savings
- Reduced human error
- Better audit trails

---

**The key insight:** Real-world success comes from identifying high-value, well-scoped problems and applying the right multi-agent pattern, not from building the most complex system possible.

---

# ADK Quick Reference Cheat Sheet

## Essential Commands

```bash
# Installation
pip install google-cloud-adk

# Start Web UI
adk web

# Start Web UI with hot reload
adk web --reload_agents

# Check version
adk --version

# Deploy to Vertex AI
adk deploy --agent-path ./agent.py --display-name "My Agent"

# Run evaluations
adk eval --config eval.test.json --agent agent.py
```

## Agent Types Quick Reference

```python
# LLM Agent (flexible, context-aware)
from adk import LLMAgent
agent = LLMAgent(
    name="assistant",
    description="What this agent does",
    model="gemini-2.0-flash",
    tools=[tool1, tool2],
    instructions="How to behave",
    output_key="result_key"  # For passing state
)

# Sequential Agent (step-by-step)
from adk import SequentialAgent
pipeline = SequentialAgent(
    name="pipeline",
    agents=[agent1, agent2, agent3]
)

# Parallel Agent (concurrent execution)
from adk import ParallelAgent
parallel = ParallelAgent(
    name="parallel",
    agents=[agent1, agent2, agent3]
)

# Loop Agent (iterative refinement)
from adk import LoopAgent
loop = LoopAgent(
    name="loop",
    agents=[generator, reviewer],
    max_iterations=5,
    stop_condition=lambda state: state.get("approved", False)
)
```

## Creating Custom Tools

```python
def my_tool(param1: str, param2: int) -> dict:
    """Comprehensive description of what this tool does.
    
    The LLM reads this docstring to understand when and how to use the tool.
    Be specific about parameters and return values.
    
    Args:
        param1: Description of first parameter
        param2: Description of second parameter
        
    Returns:
        Dictionary with result data
    """
    # Your logic here
    return {"result": "data"}

# Use in agent
agent = LLMAgent(
    name="agent",
    tools=[my_tool]
)
```

## State Management Patterns

```python
# Setting output key
agent1 = LLMAgent(
    name="researcher",
    output_key="research_data"  # Stores result here
)

# Reading from state
agent2 = LLMAgent(
    name="analyzer",
    instructions="Analyze this: {research_data}"  # Reads from state
)

# Accessing full state in custom code
def process_state(state: dict):
    research = state.get("research_data")
    analysis = state.get("analysis_result")
    # Your logic
```

## Memory Tools

```python
from adk.tools import PreloadMemoryTool

# Explicit memory control (reduces token usage)
agent = LLMAgent(
    name="agent",
    tools=[PreloadMemoryTool(), other_tools]
)
```

## Security & Callbacks

```python
# Input validation
def before_model_callback(request):
    # Validate and sanitize input
    if is_malicious(request.input):
        raise SecurityException("Blocked")
    return request

# Output validation
def after_model_callback(response):
    # Check and filter output
    if contains_pii(response.text):
        response.text = redact(response.text)
    return response

# Human-in-the-loop
from adk.tools import ToolConfirmation

risky_tool = Tool(
    function=delete_function,
    confirmation=ToolConfirmation(
        required=True,
        message="⚠️ Confirm deletion?"
    )
)
```

## Model Selection Guide

```python
# Fast and cheap (most tasks)
model="gemini-2.0-flash"

# High quality (complex reasoning)
model="gemini-2.0-pro"

# Other providers (via LiteLLM)
model="gpt-4o"              # OpenAI
model="claude-3-opus"       # Anthropic
model="mistral-large"       # Mistral
```

## Common Patterns

### Router Pattern
```python
coordinator = LLMAgent(
    name="coordinator",
    tools=[specialist1, specialist2, specialist3]
)
```

### Sequential Pipeline
```python
workflow = SequentialAgent(
    agents=[step1, step2, step3]
)
```

### Parallel + Synthesis
```python
parallel = ParallelAgent(agents=[a, b, c])
synthesizer = LLMAgent(
    instructions="Combine: {a_result}, {b_result}, {c_result}"
)
final = SequentialAgent(agents=[parallel, synthesizer])
```

### Iterative Refinement
```python
loop = LoopAgent(
    agents=[generator, critic],
    max_iterations=5,
    stop_condition=lambda s: s.get("quality") > 0.8
)
```

## Testing & Evaluation

```json
// evaluation.test.json
{
  "test_cases": [
    {
      "name": "test_case_1",
      "input": "User query",
      "expected_behavior": {
        "tool_used": "search",
        "contains": ["keyword1", "keyword2"]
      }
    }
  ]
}
```

```bash
# Run tests
adk eval --config evaluation.test.json --agent agent.py
```

## Deployment Quick Start

```bash
# Local development
adk web

# Cloud Run
gcloud run deploy agent --image IMAGE_URL

# Vertex AI Agent Engine
adk deploy \
  --agent-path ./agent.py \
  --display-name "My Agent" \
  --region us-central1
```

## Debugging Tricks

```python
# Enable verbose mode
agent = LLMAgent(name="agent", verbose=True)

# Enable debug logging
import logging
logging.basicConfig(level=logging.DEBUG)

# Check trace
result = agent.run(query)
print(result.trace)  # See execution steps
```

## Key URLs

| Resource | URL |
|----------|-----|
| Documentation | cloud.google.com/vertex-ai/docs/adk |
| Samples | github.com/google/adk-samples |
| Codelab | codelabs.developers.google.com/onramp |
| Intro Video | youtube.com/watch?v=zgrOwow_uTQ |
| DeepLearning.AI | deeplearning.ai (search: ADK) |

## Built-in Tools

```python
from adk.tools import (
    GoogleSearchTool,        # Web search
    CodeExecutionTool,       # Run Python code
    PreloadMemoryTool,       # Memory control
)

# Google Cloud tools
from google.cloud.adk.tools import (
    BigQueryTool,            # Query BigQuery
    VertexAISearchTool,      # Enterprise search
)
```

## Common Error Solutions

| Error | Solution |
|-------|----------|
| Import error | `pip install google-cloud-adk` |
| Auth error | `gcloud auth application-default login` |
| API not enabled | `gcloud services enable aiplatform.googleapis.com` |
| Agent loops | Add `max_iterations` to LoopAgent |
| State not passing | Check `output_key` and placeholder `{key}` match |
| Slow responses | Use faster model or reduce tool count |

## Best Practices Checklist

```
□ One responsibility per agent
□ Comprehensive tool docstrings
□ Clear agent descriptions
□ Set output_key for state passing
□ Use placeholders {key} correctly
□ Implement callbacks for security
□ Add HITL for sensitive operations
□ Write evaluation test cases
□ Enable logging and monitoring
□ Start simple, add complexity incrementally
```

## Pro Tips

💡 **Use the Web UI for development** - Visual debugging saves hours  
💡 **Hot reload is your friend** - `--reload_agents` flag  
💡 **State is just a dictionary** - Keep it simple  
💡 **Read the samples** - 25+ production examples  
💡 **Start with one agent** - Prove value before expanding  
💡 **Test early and often** - Build evaluation suite from day 1  
💡 **Monitor in production** - Use Agent Engine UI dashboard  

## Emergency Contact

**When stuck:**
1. Check this cheat sheet
2. Read error message carefully
3. Search github.com/google/adk/issues
4. Ask on Stack Overflow (tag: google-adk)
5. Attend community call

---

**Print this slide and keep it handy while building!**
