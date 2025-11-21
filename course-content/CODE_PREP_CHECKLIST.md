# Code Preparation Checklist - What to Build Before Recording

**Goal:** Create missing code examples for Modules 6, 7, 9
**Time:** 5-7 hours total (spread across Days 5-8 evenings)

---

## 📦 Module 6: Memory & RAG (Prep Day 5 Evening - 2-3 hours)

### Example 1: customer_service_with_chromadb

**Create:** `course-content/module-6/code/customer_service_with_memory/`

**What to build:**
```python
# agent.py - customer_service with ChromaDB memory

import chromadb
from google.adk.agents import Agent, SequentialAgent

# Initialize ChromaDB
chroma_client = chromadb.Client()
tickets_collection = chroma_client.create_collection("support_tickets")

# Research agent with memory
research_agent = Agent(
    name="research_with_memory",
    model="gemini-2.0-flash-exp",
    instruction="""
    Search for similar past tickets using semantic search.
    When user describes issue, find similar resolved tickets.
    """,
    # Add tool that queries ChromaDB
)

# Helper function for memory
def store_ticket(ticket_id, description, resolution):
    """Store resolved ticket in memory"""
    tickets_collection.add(
        documents=[f"{description} | Resolution: {resolution}"],
        ids=[ticket_id]
    )

def search_similar_tickets(query, n_results=5):
    """Search for similar past tickets"""
    results = tickets_collection.query(
        query_texts=[query],
        n_results=n_results
    )
    return results
```

**Demo Script:**
1. Store 3-5 example tickets
2. Query: "Customer can't login"
3. Show similar tickets retrieved
4. Agent uses them for better solution

**Time:** 2 hours to build + test

---

### Example 2: rag_pipeline (Simple Document RAG)

**Create:** `course-content/module-6/code/rag_pipeline/`

**What to build:**
```python
# rag_agent.py - Simple RAG with ChromaDB

import chromadb
from google.adk.agents import Agent

# 1. Document ingestion
def ingest_documents(documents):
    """Ingest documents into vector DB"""
    collection = chroma_client.create_collection("docs")
    for i, doc in enumerate(documents):
        collection.add(
            documents=[doc],
            ids=[f"doc_{i}"]
        )

# 2. RAG agent
rag_agent = Agent(
    name="rag_assistant",
    model="gemini-2.0-flash-exp",
    instruction="""
    Answer questions using the retrieved context.
    When user asks a question:
    1. Retrieve relevant documents
    2. Use them to answer accurately
    3. Cite sources
    """
)

# 3. Query function
def query_with_rag(question):
    # Retrieve relevant docs
    results = collection.query(query_texts=[question], n_results=3)
    context = results['documents']

    # Add to agent prompt
    prompt = f"Context: {context}\n\nQuestion: {question}"
    return rag_agent.run(prompt)
```

**Demo Script:**
1. Ingest 5-10 ADK documentation snippets
2. Ask: "How do I build a Sequential agent?"
3. Show retrieved context
4. Agent answers using docs

**Time:** 1 hour to build + test

---

## 🔧 Module 7: Production Tools (Prep Day 6 Evening - 1-2 hours)

### Example 1: financial_advisor_with_search

**Create:** `course-content/module-7/code/financial_advisor_with_search/`

**What to build:**
```python
# agent.py - financial_advisor with Google Search

from google.adk.tools import google_search
from google.adk.agents import Agent, ParallelAgent, SequentialAgent

# Data analyst with REAL-TIME data
data_analyst = Agent(
    name="data_analyst_realtime",
    model="gemini-2.0-flash",  # Gemini 2+ required
    tools=[google_search],  # ← THE MAGIC LINE
    instruction="""
    Use Google Search to find CURRENT stock market data.

    Search for:
    - Current stock price
    - Recent news and earnings
    - Analyst ratings
    - Market sentiment

    Be specific with search queries:
    "AAPL stock price today"
    "Apple earnings Q3 2024"
    "AAPL analyst ratings November 2024"
    """
)

# Rest of financial_advisor (same as before)
trading_analyst = Agent(...)  # Copy from existing
execution_analyst = Agent(...)
risk_analyst = Agent(...)

parallel_analysts = ParallelAgent(
    sub_agents=[data_analyst, trading_analyst, execution_analyst, risk_analyst]
)

synthesis_agent = Agent(...)  # Same as before

root_agent = SequentialAgent(
    name="financial_advisor_realtime",
    sub_agents=[parallel_analysts, synthesis_agent]
)
```

**Demo Script (YOUR MAGIC MOMENT!):**
1. Show original financial_advisor: "AAPL $175"
2. Show real price on Google: "$273"
3. Add google_search tool (2 lines!)
4. Re-run: Now shows "$269-$273" (real-time!)
5. "THIS is why tools matter in production"

**Time:** 30 min to copy + modify + test

---

### Example 2: multi_model_comparison

**Create:** `course-content/module-7/code/multi_model_examples/`

**What to build:**
```python
# compare_models.py - Same agent, different models

from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm

# Version 1: Gemini (default)
gemini_agent = Agent(
    model="gemini-2.0-flash-exp",
    name="gemini_expert",
    instruction="Explain quantum computing simply"
)

# Version 2: OpenAI GPT-4o
openai_agent = Agent(
    model=LiteLlm(model="openai/gpt-4o"),
    name="gpt4_expert",
    instruction="Explain quantum computing simply"  # Same instruction!
)

# Version 3: Anthropic Claude
claude_agent = Agent(
    model=LiteLlm(model="anthropic/claude-3-7-sonnet-latest"),
    name="claude_expert",
    instruction="Explain quantum computing simply"
)

# Version 4: Ollama (local)
ollama_agent = Agent(
    model=LiteLlm(model="ollama_chat/mistral-small3.1"),
    name="ollama_expert",
    instruction="Explain quantum computing simply"
)

# Test function
def compare_responses(query):
    """Test same query on all 4 models"""
    print("GEMINI:", gemini_agent.run(query))
    print("\nGPT-4O:", openai_agent.run(query))
    print("\nCLAUDE:", claude_agent.run(query))
    print("\nOLLAMA:", ollama_agent.run(query))
```

**Demo Script:**
1. Ask same question to all 4 models
2. Compare responses (different styles!)
3. Explain when to use which
4. Show cost comparison

**Time:** 30 min to build + test (need API keys ready)

---

## ☁️ Module 9: Deployment (Prep Day 8 Evening - 2 hours)

### Example 1: Cloud Run Deployment

**Create:** `course-content/module-9/deployment/cloud-run/`

**Files needed:**

**deploy.sh:**
```bash
#!/bin/bash
# Deploy customer_service to Cloud Run

PROJECT_ID="your-project"
REGION="us-central1"
SERVICE_NAME="customer-service-agent"

# Build container
docker build -t gcr.io/$PROJECT_ID/$SERVICE_NAME .

# Push to registry
docker push gcr.io/$PROJECT_ID/$SERVICE_NAME

# Deploy to Cloud Run
gcloud run deploy $SERVICE_NAME \
  --image gcr.io/$PROJECT_ID/$SERVICE_NAME \
  --region $REGION \
  --allow-unauthenticated \
  --set-env-vars GOOGLE_API_KEY=$GOOGLE_API_KEY

echo "✅ Deployed to Cloud Run!"
echo "URL: [Cloud Run will show URL]"
```

**.env.production:**
```bash
# Production environment variables
GOOGLE_API_KEY=use_secret_manager_in_real_production
ENVIRONMENT=production
LOG_LEVEL=INFO
```

**Dockerfile.cloudrun:**
```dockerfile
# Multi-stage build (already have similar from workshop!)
FROM python:3.11-slim as builder

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

FROM python:3.11-slim
WORKDIR /app
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY . .

CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8080"]
```

**Time:** 1 hour to create files + test locally

---

### Example 2: Monitoring Dashboard

**Create:** `course-content/module-9/deployment/monitoring/`

**cloud-logging-queries.txt:**
```sql
-- Query for agent execution times
resource.type="cloud_run_revision"
jsonPayload.agent_name=~".*"
jsonPayload.execution_time_ms > 0

-- Query for errors
resource.type="cloud_run_revision"
severity="ERROR"
jsonPayload.agent_name=~".*"

-- Query for tool usage
resource.type="cloud_run_revision"
jsonPayload.tool_name=~".*"
```

**dashboard-config.json:**
```json
{
  "displayName": "AI Agent Monitoring",
  "widgets": [
    {
      "title": "Agent Execution Time",
      "xyChart": {...}
    },
    {
      "title": "Error Rate",
      "scorecard": {...}
    }
  ]
}
```

**Time:** 30 min to document queries

---

### Example 3: CI/CD Pipeline

**Create:** `course-content/module-9/.github/workflows/deploy.yml`

```yaml
name: Deploy to Cloud Run

on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2

      - name: Build Docker image
        run: docker build -t gcr.io/${{ secrets.GCP_PROJECT }}/agent .

      - name: Push to GCR
        run: docker push gcr.io/${{ secrets.GCP_PROJECT }}/agent

      - name: Deploy to Cloud Run
        run: |
          gcloud run deploy agent \
            --image gcr.io/${{ secrets.GCP_PROJECT }}/agent \
            --region us-central1
```

**Time:** 30 min to create and document

---

## ✅ Total Prep Time Summary

| Module | Prep Work | Time Estimate | When to Do |
|--------|-----------|---------------|------------|
| 1 | Slides only | 1 hour | Tonight or Day 1 morning |
| 2 | Code examples | 1 hour | Day 1 evening |
| 3 | None (exists!) | 0 | - |
| 4 | None (exists!) | 0 | - |
| 5 | None (exists!) | 0 | - |
| 6 | ChromaDB + RAG examples | 2-3 hours | Day 5 evening |
| 7 | Google Search + multi-model | 1-2 hours | Day 6 evening |
| 8 | None (exists!) | 0 | - |
| 9 | Deployment configs | 2 hours | Day 8 evening |
| **TOTAL** | | **7-9 hours** | Spread across evenings |

**Key Insight:** Most code EXISTS (workshop agents)! Only need to create Memory, Tools, and Deployment examples.

---

## 🚀 You're Ready to Start Tonight!

**Tonight (Day 0):**
1. Create slides for Module 1 (1 hour)
2. Review this schedule
3. Set start date (tomorrow?)
4. Get excited! 🎉

**Tomorrow (Day 1):**
Record Module 1 - Foundation (3 hours)

**9 days later:**
All modules recorded! 🎬

**Want me to create the detailed recording scripts now so you can just read and record?**

Each script will be like a teleprompter - exact words to say, demo steps, timing cues. Makes recording MUCH faster!

Ready? 🔥
