# Content Pipeline Agent

**Step 3 of 9** | **Duration:** 30 minutes | **Difficulty:** Intermediate

## Overview

A 4-agent Sequential workflow that automates content creation from research to publication. Demonstrates the same Sequential pattern as customer_service but in a different business domain.

Students reinforce Sequential workflow concepts while learning how to adapt patterns across domains.

## Learning Objectives

By completing this agent, you will understand:

- ✅ **Pattern Reuse** - Same Sequential pattern, different business use case
- ✅ **4-Agent Workflow** - Extended pipeline beyond 3 agents
- ✅ **Domain Adaptation** - How to apply ADK patterns to any workflow
- ✅ **Output Transformation** - Each agent transforms input into different format
- ✅ **Content Quality** - Research → creativity → optimization → distribution

## Pattern Demonstrated

**Sequential Multi-Agent Content Pipeline**

```
content_pipeline (SequentialAgent)
├── research_agent (Agent)
│   └── Role: Find sources, stats, expert quotes
│   └── Output: {topic, sources, statistics, quotes}
│
├── draft_agent (Agent)
│   └── Role: Write initial 800-1200 word article
│   └── Output: Complete draft with sections
│
├── optimizer_agent (Agent)
│   └── Role: SEO + readability + engagement
│   └── Output: Optimized content with formatting hints
│
└── publisher_agent (Agent)
    └── Role: Format for target platform (Medium, Blog, LinkedIn)
    └── Output: Ready-to-publish formatted content
```

**Key Learning:** Same SequentialAgent pattern from Step 2, but content creation is a different transformation pipeline than customer support.

## Business Value

Real-world impact:
- **3x faster** content production
- **Consistent quality** across all articles
- **SEO optimized** by default
- **Multi-platform** ready (Medium, LinkedIn, Blog, Dev.to)
- **Research-backed** - no more guessing at topics

Use cases:
- Company blogs and thought leadership
- Developer content (tutorials, how-tos)
- Marketing articles and case studies
- Technical documentation

## ADK 1.18+ Features

### Visual Agent Builder
- **Available:** ✅
- **Usage:** "Build a content pipeline with research, drafting, optimization, and publishing agents"
- **Benefit:** AI assistant generates 4-agent workflow from natural language description

### run_debug() Helper
- **Available:** ✅
- **Usage:** Test each content stage independently
  ```python
  from google.adk import run_debug

  # Test research alone
  run_debug(research_agent, "Write about AI agent patterns in production")

  # Test draft with mock research output
  mock_research = '{"topic": "AI Agents", "sources": [...]}'
  run_debug(draft_agent, mock_research)
  ```

## Architecture

### Workflow Flow

```
User Input: "Write an article about building production-ready AI agents"

    ↓

[RESEARCH AGENT]
Searches for sources, trends, expert opinions
Output: {
    "topic": "Production-Ready AI Agent Patterns",
    "target_audience": "Software engineers building AI systems",
    "key_angles": [
        "Testing and observability",
        "Error handling and fallbacks",
        "Cost optimization"
    ],
    "sources": [
        {"title": "Google ADK Best Practices", "url": "...", ...},
        {"title": "Agent Testing Strategies", "url": "...", ...}
    ],
    "statistics": [
        {"stat": "70% of AI projects fail in production", "source": "Gartner 2024"}
    ]
}

    ↓

[DRAFT AGENT]
Writes 800-1200 word article using research
Output: Complete markdown article with:
- Compelling headline
- Introduction with hook
- 3-5 main sections with examples
- Statistics and quotes integrated
- Conclusion with CTA

    ↓

[OPTIMIZER AGENT]
SEO + readability + engagement improvements
Output: Optimized version with:
- Better headline (click-optimized)
- Meta description
- Keywords identified
- Formatting hints added
- Visual placeholders

    ↓

[PUBLISHER AGENT]
Formats for target platform
Output: {
    "platform": "Medium",
    "formatted_content": "[Ready to paste]",
    "metadata": {
        "title": "...",
        "description": "...",
        "tags": ["ai-agents", "production", ...]
    }
}

    ↓

User gets publish-ready content
```

### Agent Responsibilities

| Agent | Input | Processing | Output |
|-------|-------|------------|--------|
| **Research** | Topic | Find sources, stats, quotes | Research brief |
| **Draft** | Research brief | Write 800-1200 word article | Complete draft |
| **Optimizer** | Draft | SEO + readability + engagement | Optimized content |
| **Publisher** | Optimized content | Format for platform | Ready-to-publish |

## Files

```
content_pipeline/
├── agent.py          # 4 sub-agents + SequentialAgent root
├── .env              # API key (GOOGLE_API_KEY)
├── __init__.py       # Package marker
└── README.md         # This file
```

## Running the Agent

### Option 1: ADK Web UI

```bash
adk web
```

- Select "content_pipeline" from dropdown
- Enter topic: "Building production AI agents"
- Watch 4-agent pipeline execute
- Final output is publish-ready content

### Option 2: Streamlit Workshop UI

```bash
streamlit run streamlit_apps/workshop_ui/app.py --server.port 8501
```

- Select "Content Pipeline"
- More user-friendly for demos
- Shows final formatted content

### Option 3: run_debug() Quick Test

```python
from google.adk import run_debug
from adk_agents.content_pipeline.agent import root_agent

run_debug(root_agent, "Write about testing AI agents in production")
```

## Example Interactions

### Example 1: Technical Tutorial

**User:**
```
Write a tutorial about implementing retry logic in AI agents
```

**Research Output:**
```json
{
  "topic": "Implementing Retry Logic in AI Agents",
  "target_audience": "Python developers building AI agents",
  "key_angles": [
    "Why retries matter for production systems",
    "Common retry patterns (exponential backoff, circuit breaker)",
    "ADK built-in retry mechanisms"
  ],
  "sources": [
    {"title": "ADK Retry Plugin Documentation", "url": "..."},
    {"title": "Designing Resilient Systems", "url": "..."}
  ],
  "statistics": [
    {"stat": "API calls fail 1-5% of the time", "source": "AWS reliability report"}
  ]
}
```

**Draft Output:**
```markdown
# Never Let Your AI Agent Give Up: A Guide to Retry Logic

When your AI agent calls an external API and gets a timeout, what happens?
Does it fail silently? Throw an error? Or does it try again intelligently?

According to AWS reliability reports, API calls fail 1-5% of the time in production...

## Why Retries Matter

[800+ words with code examples, statistics, expert quotes]

## Implementing Exponential Backoff

```python
# Code example from research
```

## Conclusion
Production AI agents need resilience. Start with these patterns today.
```

**Optimizer Output:**
```markdown
[SEO-optimized version with]:
- Headline: "Never Let Your AI Agent Give Up: Implementing Retry Logic (with Python Examples)"
- Meta: "Learn how to implement exponential backoff, circuit breakers, and retry logic..."
- Keywords: retry logic, AI agents, exponential backoff, resilient systems
- [IMAGE: Diagram of retry flow]
- [CODE: Python examples with syntax highlighting]
```

**Publisher Output:**
```json
{
  "platform": "Dev.to",
  "formatted_content": "---\ntitle: Never Let Your AI Agent Give Up...\ntags: python, ai, agents...",
  "metadata": {
    "title": "...",
    "tags": ["python", "ai", "agents", "production"],
    "cover_image": "Suggested: Retry flow diagram"
  }
}
```

### Example 2: Business Case Study

**User:**
```
Write a case study about how AI agents reduced customer support costs
```

**Result:** Complete case study with statistics, quotes, SEO optimization, formatted for company blog

## Common Issues

### Research Agent Finding Generic Sources

**Problem:** Research includes obvious, low-value sources

**Solution:**
- Be specific in your topic: "Advanced AI agent patterns" vs "AI agents"
- Ask for recent sources: "Include articles from last 3 months"
- Specify expertise level: "For experienced developers, not beginners"

### Draft Too Short/Long

**Problem:** Article doesn't meet length requirements

**Solution:**
- Draft agent targets 800-1200 words by default
- For longer: "Write a comprehensive 2000-word guide"
- For shorter: "Write a concise 500-word overview"

### Optimizer Changing Meaning

**Problem:** SEO optimization alters technical accuracy

**Solution:**
- Review optimized version carefully
- Technical accuracy > SEO
- You can ask optimizer to "maintain technical precision while optimizing"

### Platform Formatting Issues

**Problem:** Publisher output doesn't match platform requirements

**Solution:**
- Specify platform clearly: "Format for Medium with proper markdown"
- Check platform's content guidelines
- Publisher agent can adapt to most platforms

## Understanding Content Pipelines

**Key Concepts:**

1. **Research-Driven Content**
   - Quality starts with quality research
   - Statistics and quotes add credibility
   - Sources inform direction and depth

2. **Transformation Pipeline**
   - Research → Draft: Information → Narrative
   - Draft → Optimizer: Narrative → SEO + Engagement
   - Optimizer → Publisher: Universal → Platform-specific

3. **Each Agent is an Expert**
   - Researcher doesn't write
   - Writer doesn't optimize
   - Optimizer doesn't format
   - Clear separation of concerns

4. **When to Use Content Pipelines**
   - Regular blog/article production
   - Multi-platform content distribution
   - SEO-focused content marketing
   - Research-heavy tutorials/guides

## Success Criteria

Before moving to Step 4, verify:

- [ ] All 4 agents execute in sequence
- [ ] Research agent finds relevant sources
- [ ] Draft agent produces coherent articles
- [ ] Optimizer improves SEO and readability
- [ ] Publisher formats for at least 2 platforms
- [ ] Tested with 3 different content types

## Next Steps

Once you've completed the exercises and verified all success criteria, proceed to:

**Step 4: Medical Authorization Workflow**

Preview: Sequential workflow with compliance, validation, and decision gates. Learn how to handle structured data extraction and regulatory requirements.

## Debugging Tips

### Test Individual Agents

```python
from adk_agents.content_pipeline.agent import (
    research_agent, draft_agent, optimizer_agent, publisher_agent
)
from google.adk import run_debug

# Test each independently
run_debug(research_agent, "Topic: AI agents in healthcare")
run_debug(draft_agent, '[Mock research JSON from previous output]')
```

### Compare Agent Outputs

```python
# Run full pipeline
result = run_debug(root_agent, "Write about agent testing")

# Check each transformation
# - Did research find quality sources?
# - Did draft use the research?
# - Did optimizer improve readability?
# - Is publisher output platform-ready?
```

### Measure Content Quality

- **Research:** 5+ quality sources, recent (<6 months), diverse perspectives
- **Draft:** 800-1200 words, clear structure, examples included
- **Optimizer:** Flesch-Kincaid score 60+, keywords naturally integrated
- **Publisher:** Platform-specific formatting correct

## Comparison with Step 2

**Customer Service (Step 2):**
- Input: Problem description
- Output: Solution response
- Focus: Support workflow

**Content Pipeline (Step 3):**
- Input: Topic idea
- Output: Published article
- Focus: Content creation workflow

**Same Pattern, Different Domain** - This is key! SequentialAgent works for ANY multi-step business process.

## References

- [ADK Documentation - Sequential Agents](https://google.github.io/adk-docs/agents/sequential/)
- [Workshop Progression](../../workshop_progression.yaml)
- [ADK Samples - Blog Writer](https://github.com/google/adk-samples/tree/main/python/agents/blog-writer)
- [Step 2 - Customer Service](../customer_service/README.md) - Same pattern

---

**Tags:** `step-3-content-pipeline`, `intermediate`, `sequential-agent`, `content-creation`
