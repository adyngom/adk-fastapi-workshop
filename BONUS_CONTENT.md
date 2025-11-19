# 🎁 Bonus Content: Beyond the 9 Agents

**Workshop Time:** Optional 15-20 minutes at the end (or pre-masterclass teaser)

This bonus content introduces **advanced ADK capabilities** that go beyond the core 9-agent workshop. These topics are covered in-depth in our **paid follow-up Masterclass**.

---

## 🚀 What We'll Cover (Quick Preview)

1. **Gemini Built-In Tools** - Powerful tools that only work with Gemini models
2. **Multi-Model Strategies** - Using OpenAI, Anthropic, Ollama alongside Gemini
3. **Production Deployment** - GKE, Cloud Run, Agent Engine
4. **Enterprise Features** - Apigee AI Gateway, monitoring, cost control

**Goal:** Give you a taste of production-ready features. Full implementation in Masterclass.

---

## 1️⃣ Gemini Built-In Tools (Gemini 2+ Models Only)

### What Are Built-In Tools?

ADK provides **production-ready tools** that work ONLY with Gemini 2+ models:

#### 🔍 Google Search Tool
```python
from google.adk.agents import Agent
from google.adk.tools import google_search

search_agent = Agent(
    model="gemini-2.0-flash",  # Gemini 2+ required
    name="search_expert",
    instruction="You can search Google for real-time information",
    tools=[google_search]
)
```

**Use Cases:**
- News agents (real-time updates)
- Research assistants (current information)
- Market intelligence (latest trends)

**Example from our workshop:**
- Step 3 (content_pipeline) **could** use google_search in research_agent
- Step 6 (brand_intelligence) **could** use google_search for news

**Limitation:** ⚠️ Only ONE built-in tool per agent (workaround exists for google_search)

---

#### 💻 Code Execution Tool
```python
from google.adk.agents import Agent
from google.adk.code_executors import BuiltInCodeExecutor

coding_agent = Agent(
    model="gemini-2.0-flash",
    name="code_expert",
    instruction="You can write and execute Python code",
    code_executor=BuiltInCodeExecutor()
)
```

**Use Cases:**
- Data analysis agents (run calculations)
- Visualization agents (generate charts)
- Automation scripts (execute code)

**Example:**
```python
# User: "Calculate the compound interest on $10k at 5% for 10 years"
# Agent writes and executes:
principal = 10000
rate = 0.05
time = 10
amount = principal * (1 + rate) ** time
print(f"Final amount: ${amount:,.2f}")

# Output: Final amount: $16,288.95
```

---

#### 📊 BigQuery Tools (NEW - Production Data Access)
```python
from google.adk.tools import BigQueryToolset

bq_tools = BigQueryToolset(
    project_id="my-project",
    dataset_id="sales_data"
)

data_agent = Agent(
    model="gemini-2.0-flash",
    tools=[bq_tools],
    instruction="Analyze sales data using BigQuery"
)
```

**Capabilities:**
- `list_tables` - Explore available tables
- `get_table_info` - Schema and metadata
- `execute_sql` - Run SQL queries
- `ask_data_insights` - **Natural language to SQL!**
- `forecast` - Time series predictions with AI.FORECAST

**Example:**
```
User: "What were our top 5 products last quarter?"
Agent: [Executes SQL via BigQuery tool]
       SELECT product_name, SUM(revenue)
       FROM sales
       WHERE date >= '2024-07-01'
       GROUP BY product_name
       ORDER BY revenue DESC
       LIMIT 5
```

---

#### 🗄️ Additional Database Tools

**Spanner Tools** (ADK 1.11+)
- Execute SQL on Spanner
- Similarity search (vector search)

**Bigtable Tools** (ADK 1.12+)
- Query NoSQL data
- Time series data access

**Vertex AI RAG Engine**
- Private document search
- Grounding with your own data

---

### 🎓 Masterclass Preview: Built-In Tools Deep Dive

In the **Masterclass**, we'll build:

**Agent:** `data_analyst_pro`
- Uses BigQuery tools for real company data
- Code execution for calculations and visualizations
- Google Search for market context
- Combines all three in one intelligent system

**Learn:**
- Workarounds for multi-tool limitations
- Production BigQuery integration
- Secure code execution in GKE
- RAG with private documents

---

## 2️⃣ Multi-Model Strategies: Beyond Gemini

### Why Use Multiple Model Providers?

✅ **Cost optimization** - Use cheaper models for simple tasks
✅ **Specialized capabilities** - Each model has strengths
✅ **Redundancy** - Fallback if primary model unavailable
✅ **Compliance** - Some regions/industries require specific providers

### Supported Providers in ADK

| Provider | ADK Integration | Use Case |
|----------|----------------|----------|
| **Gemini** | Native (direct string) | Default, best ADK integration |
| **OpenAI** | LiteLLM wrapper | GPT-4o for complex reasoning |
| **Anthropic** | LiteLLM or Claude class | Claude for long context |
| **Ollama** | LiteLLM wrapper | Local/offline, privacy |
| **vLLM** | LiteLLM wrapper | Self-hosted, cost control |
| **Vertex AI Models** | Endpoint string | Fine-tuned, Model Garden |

---

### Quick Example: Using OpenAI GPT-4o

```python
from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm

# Set API key
import os
os.environ["OPENAI_API_KEY"] = "your_openai_key"

openai_agent = Agent(
    model=LiteLlm(model="openai/gpt-4o"),
    name="openai_expert",
    instruction="You are powered by GPT-4o",
    tools=[your_custom_tools]
)
```

**When to use OpenAI:**
- Complex reasoning tasks
- Creative writing
- Code generation
- Multi-modal (vision + text)

---

### Quick Example: Using Anthropic Claude

```python
from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm

# Set API key
os.environ["ANTHROPIC_API_KEY"] = "your_anthropic_key"

claude_agent = Agent(
    model=LiteLlm(model="anthropic/claude-3-7-sonnet-latest"),
    name="claude_expert",
    instruction="You are powered by Claude 3.7 Sonnet",
    tools=[your_custom_tools]
)
```

**When to use Claude:**
- Long context (200k tokens)
- Nuanced analysis
- Ethical reasoning
- Complex instructions

---

### Quick Example: Local Models with Ollama

```python
from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm

# Start Ollama: ollama serve
# Pull model: ollama pull mistral-small3.1

ollama_agent = Agent(
    model=LiteLlm(model="ollama_chat/mistral-small3.1"),
    name="local_expert",
    instruction="You run locally for privacy",
    tools=[your_custom_tools]
)
```

**When to use Ollama:**
- Privacy-sensitive data (runs locally)
- Offline environments
- Cost control (no API costs)
- Experimentation

---

### 🎯 Multi-Model Strategy Example

**Intelligent Cost Optimization:**

```python
# Use cheap/fast models for simple tasks
triage_agent = Agent(
    model="gemini-2.0-flash",  # Fast, cheap
    instruction="Quickly categorize this issue"
)

# Use powerful models for complex analysis
analysis_agent = Agent(
    model=LiteLlm(model="openai/gpt-4o"),  # Powerful, expensive
    instruction="Deep analysis of complex scenario"
)

# Use local models for sensitive data
privacy_agent = Agent(
    model=LiteLlm(model="ollama_chat/mistral-small3.1"),  # Local
    instruction="Analyze sensitive customer data (never leaves server)"
)
```

**Result:** 70% cost reduction while maintaining quality where it matters

---

### 🎓 Masterclass Preview: Multi-Model Orchestration

In the **Masterclass**, we'll build:

**Agent:** `intelligent_orchestrator`
- Routes tasks to optimal model based on:
  - Complexity (simple → flash, complex → gpt-4o)
  - Data sensitivity (private → ollama, public → cloud)
  - Cost budget (stay under $X per query)
  - Latency requirements (fast → flash, quality → pro)

**Learn:**
- Model selection strategies
- Fallback chains (primary fails → use secondary)
- Cost tracking and optimization
- Performance benchmarking

---

## 3️⃣ Production Deployment Options

### Quick Overview of Deployment Targets

| Platform | Best For | Setup Time | Features |
|----------|----------|------------|----------|
| **Local (IDX/Docker)** | Development | 5 minutes | Fast iteration |
| **Cloud Run** | Scalable APIs | 15 minutes | Auto-scaling, HTTPS |
| **GKE** | Enterprise | 1 hour | Full control, security |
| **Agent Engine** | Managed | 10 minutes | Fully managed, easy |

---

### Deployment Example: Cloud Run

```bash
# Build container
docker build -t gcr.io/my-project/customer-service .

# Push to registry
docker push gcr.io/my-project/customer-service

# Deploy to Cloud Run
gcloud run deploy customer-service \
  --image gcr.io/my-project/customer-service \
  --region us-central1 \
  --allow-unauthenticated \
  --set-env-vars GOOGLE_API_KEY=$GOOGLE_API_KEY
```

**Result:** Production API in minutes with auto-scaling

---

### Deployment Example: Agent Engine (Easiest)

```python
from google.adk.agents import Agent

root_agent = Agent(
    name="production_agent",
    model="gemini-2.0-flash",
    # ... agent definition
)

# Deploy with one command
# adk deploy --project=my-project --region=us-central1
```

**Agent Engine handles:**
- Hosting and scaling
- Session management
- API endpoints
- Monitoring

---

### Production Checklist Preview

✅ **Security:**
- [ ] Secrets in Secret Manager (not .env)
- [ ] Authentication/authorization
- [ ] Input validation and sanitization
- [ ] Rate limiting

✅ **Observability:**
- [ ] Logging to Cloud Logging
- [ ] Metrics to Cloud Monitoring
- [ ] Tracing with OpenTelemetry
- [ ] Cost tracking

✅ **Reliability:**
- [ ] Error handling and retries
- [ ] Fallback models
- [ ] Circuit breakers
- [ ] Health checks

✅ **Compliance:**
- [ ] Audit trails (BigQuery)
- [ ] Data retention policies
- [ ] GDPR/HIPAA if applicable
- [ ] Terms of service enforcement

---

## 4️⃣ Enterprise Features

### Apigee AI Gateway (ADK 1.18)

**What it does:** Wraps your AI models with enterprise governance.

```python
from google.adk.models.apigee_llm import ApigeeLlm

governed_model = ApigeeLlm(
    model="apigee/gemini-2.0-flash",
    proxy_url="https://your-apigee-proxy.com",
    custom_headers={"Authorization": "Bearer token"}
)

agent = Agent(
    model=governed_model,
    # Now ALL calls go through Apigee policies
)
```

**Apigee provides:**
- 🛡️ **Model Armor** - Threat protection (prompt injection, jailbreaks)
- 💰 **Token Limiting** - Cost control per user/team
- ⚡ **Semantic Caching** - 80% faster for repeated queries
- 📊 **Usage Analytics** - Who's using what, how much
- 🔄 **Model Routing** - Route to different models based on rules

**Example Policy:**
```yaml
# Apigee policy
if request.tokens > 10000:
  route_to: "gemini-pro"  # Use powerful model
else:
  route_to: "gemini-flash"  # Use cheaper model

if user.quota_exceeded:
  return: "Rate limit exceeded"
```

---

### Cost Optimization Strategies

**Production agents can get expensive. Here's how to control costs:**

#### Strategy 1: Model Selection by Task
```python
# Simple categorization: flash (cheap)
triage = Agent(model="gemini-2.0-flash", ...)

# Complex analysis: pro (expensive, but needed)
analysis = Agent(model="gemini-2.5-pro", ...)
```

**Savings:** 90% cost reduction on simple tasks

---

#### Strategy 2: Semantic Caching (via Apigee)
```
Query 1: "Analyze AAPL stock" → $0.10 (full model call)
Query 2: "Analyze AAPL stock" → $0.001 (cache hit!)
```

**Savings:** 99% on repeated queries

---

#### Strategy 3: Token Limiting
```python
generate_content_config=types.GenerateContentConfig(
    max_output_tokens=500  # Limit response length
)
```

**Savings:** Control max cost per query

---

#### Strategy 4: LiteLLM Fallbacks
```python
from google.adk.models.lite_llm import LiteLlm

# Try cheap model first, fallback to expensive
model = LiteLlm(
    model="gemini-2.0-flash",
    fallbacks=["gpt-4o", "claude-3-7-sonnet"]
)
```

**Savings:** Use expensive models only when needed

---

## 🎓 Paid Masterclass: What's Next?

### Masterclass Topics (Full Day Workshop)

#### Module 1: Advanced Built-In Tools (2 hours)
- **Google Search grounding** in production
  - Search suggestions UI requirements
  - Citation and attribution
  - Real-time data integration
- **Code Execution at scale**
  - GKE Code Executor (sandboxed, secure)
  - Resource limits and timeouts
  - Handling malicious code attempts
- **BigQuery integration**
  - Natural language to SQL
  - Time series forecasting
  - Data visualization agents
- **Vertex AI RAG Engine**
  - Build private knowledge bases
  - Document ingestion pipelines
  - Semantic search for enterprise data

**Hands-On Project:** Build a data analyst agent that queries your company database with natural language

---

#### Module 2: Multi-Model Orchestration (2 hours)
- **Cost optimization strategies**
  - Model routing based on complexity
  - Fallback chains for reliability
  - Token usage tracking and limits
- **Model-specific strengths**
  - When to use GPT-4o vs Claude vs Gemini
  - Benchmarking for your use case
  - A/B testing different models
- **Local models in production**
  - Ollama in Docker containers
  - vLLM deployment on GKE
  - Model serving best practices
- **Apigee AI Gateway**
  - Policy configuration
  - Semantic caching setup
  - Model Armor threat protection
  - Usage analytics and reporting

**Hands-On Project:** Build intelligent orchestrator that routes queries to optimal model

---

#### Module 3: Production Deployment (2 hours)
- **Deployment platforms compared**
  - Cloud Run: When and how
  - GKE: Enterprise patterns
  - Agent Engine: Fully managed
  - Hybrid: Multi-cloud strategies
- **Security hardening**
  - Secret management
  - Network policies
  - Identity and access management
  - Workload identity
- **Observability and monitoring**
  - Cloud Logging integration
  - Custom metrics in Cloud Monitoring
  - Distributed tracing
  - Cost attribution
- **CI/CD for agents**
  - Automated testing pipelines
  - Deployment workflows
  - Rollback strategies
  - Blue/green deployments

**Hands-On Project:** Deploy customer_service agent to Cloud Run with full observability

---

#### Module 4: Enterprise Patterns (2 hours)
- **Audit and compliance**
  - BigQuery logging plugin (ADK 1.18)
  - Cryptographic audit trails
  - Session rewind for debugging
  - Compliance reporting
- **High-availability patterns**
  - Multi-region deployment
  - Load balancing
  - Failover strategies
  - Disaster recovery
- **Advanced MCP integration**
  - Custom MCP servers
  - Database connection pooling
  - Authentication and authorization
  - MCP server deployment
- **Agent evaluations**
  - Building eval sets
  - LLM-as-judge patterns
  - Regression testing
  - Performance benchmarking

**Hands-On Project:** Build verified_recommendations with production BigQuery audit logging

---

## 💡 Quick Demos for Today (5 min each)

### Demo 1: Google Search in Action

**Enhance Step 3 (content_pipeline) research_agent:**

```python
from google.adk.tools import google_search

research_agent = Agent(
    model="gemini-2.0-flash",  # Gemini 2+ required
    name="research_agent",
    instruction="""Research topics using real-time Google Search.
    Find recent articles, statistics, and expert opinions.""",
    tools=[google_search]
)
```

**Test Query:** "Research AI agent production patterns from last 30 days"

**Result:** Real search results with citations!

---

### Demo 2: Code Execution Power

**Create quick demo agent:**

```python
from google.adk.code_executors import BuiltInCodeExecutor

calculator_agent = Agent(
    model="gemini-2.0-flash",
    name="advanced_calculator",
    instruction="Write and execute Python code to solve complex problems",
    code_executor=BuiltInCodeExecutor()
)
```

**Test Query:** "Calculate the ROI of our $500k AI investment if it saves 1000 hours/month at $150/hour"

**Agent writes and executes:**
```python
investment = 500000
hours_saved_monthly = 1000
hourly_rate = 150
annual_savings = hours_saved_monthly * 12 * hourly_rate
roi = (annual_savings - investment) / investment * 100

print(f"Annual savings: ${annual_savings:,}")
print(f"ROI: {roi:.1f}%")
print(f"Payback period: {investment / (hours_saved_monthly * hourly_rate):.1f} months")
```

**Output:**
```
Annual savings: $1,800,000
ROI: 260%
Payback period: 3.3 months
```

🔥 **This is powerful!**

---

### Demo 3: Multi-Model Fallback

```python
from google.adk.models.lite_llm import LiteLlm

# Primary: Gemini (cheap, fast)
# Fallback: GPT-4o (if Gemini errors)
resilient_model = LiteLlm(
    model="gemini/gemini-2.0-flash",
    fallbacks=["openai/gpt-4o"]
)

resilient_agent = Agent(
    model=resilient_model,
    instruction="I'm resilient - if one model fails, I use another"
)
```

**Test:** Simulate Gemini outage → Agent automatically uses GPT-4o

---

## 🎯 Today's Takeaway: What You Can Do NOW

### After This Workshop, You Can:

✅ **Immediately:**
1. Add `google_search` to any agent (Gemini 2+ models)
2. Enable `code_executor` for calculation agents
3. Use different models via LiteLLM (OpenAI, Claude, Ollama)

✅ **This Week:**
1. Deploy agents to Cloud Run (production-ready)
2. Set up basic monitoring
3. Implement cost controls

✅ **In Masterclass:**
1. Full BigQuery integration for enterprise data
2. Apigee AI Gateway for governance
3. Multi-model intelligent orchestration
4. Production observability and compliance

---

## 📚 Quick Reference

### Adding Google Search to Existing Agent

```python
from google.adk.tools import google_search

# Modify any agent from workshop:
# Step 3: content_pipeline/research_agent
# Step 6: brand_intelligence/news_researcher
# Step 7: software_assistant/searcher_agent

agent = Agent(
    model="gemini-2.0-flash",  # MUST be Gemini 2+
    tools=[google_search],     # Just add it!
    # ... rest of agent
)
```

### Switching to Different Model

```python
from google.adk.models.lite_llm import LiteLlm

# Change ANY agent's model:
agent.model = LiteLlm(model="openai/gpt-4o")
# OR
agent.model = LiteLlm(model="anthropic/claude-3-7-sonnet-latest")
# OR
agent.model = LiteLlm(model="ollama_chat/mistral-small3.1")
```

### Enabling Code Execution

```python
from google.adk.code_executors import BuiltInCodeExecutor

agent.code_executor = BuiltInCodeExecutor()
```

---

## 🚀 Join the Masterclass!

**What:** Full-Day Deep Dive - Production ADK Mastery
**When:** TBD (Sign up for early notification)
**Topics:**
- Built-in tools (Google Search, BigQuery, RAG)
- Multi-model strategies and cost optimization
- Production deployment (Cloud Run, GKE, Agent Engine)
- Enterprise features (Apigee, monitoring, compliance)
- Advanced patterns (evaluations, A/B testing, fine-tuning)

**You'll Deploy:**
- Data analyst with BigQuery + code execution
- Multi-model orchestrator with intelligent routing
- Production-grade system with full observability
- Enterprise agent with Apigee governance

**Investment:** $XXX (4x the value of today's workshop)
**Outcome:** Production-ready AI agent systems in your organization

---

## 📝 Additional Resources

### Built-In Tools
- [ADK Built-In Tools Docs](./docs/adk/adk-built-in-tools.md)
- [Google Search Grounding Guide](https://google.github.io/adk-docs/grounding/)
- [BigQuery Tools Reference](https://google.github.io/adk-docs/tools/bigquery/)

### Multi-Model
- [Using Different Models](./docs/adk/adk-use-different-models.md)
- [LiteLLM Providers](https://docs.litellm.ai/docs/providers)
- [Ollama Models](https://ollama.com/search?c=tools)

### Deployment
- [Deploy to Cloud Run](https://google.github.io/adk-docs/deploy/cloud-run/)
- [Deploy to GKE](https://google.github.io/adk-docs/deploy/gke/)
- [Agent Engine Guide](https://cloud.google.com/vertex-ai/docs/agent-engine)

---

**Questions about Masterclass? Ask your instructor!**

**Want early access?** Leave your email with the instructor for priority notification.

🎉 **Thank you for completing the workshop! Go build amazing AI systems!**
