# Software Assistant Agent

**Step 7 of 9** | **Duration:** 20 minutes | **Difficulty:** Advanced

## Overview

Developer assistance agent demonstrating **Model Context Protocol (MCP)** integration patterns. Shows how to connect agents to databases, GitHub, and other external services.

This is a **conceptual demonstration** - the workshop version simulates MCP tools, but shows production patterns students can implement with real MCP servers.

## Learning Objectives

- ✅ **MCP Integration Patterns** - How agents access databases and external services
- ✅ **Database Tool Access** - MCP Toolbox for structured data
- ✅ **GitHub Integration** - MCP server for issue tracking
- ✅ **Multi-Source Knowledge** - Combining internal DB + GitHub + Stack Overflow
- ✅ **Production Patterns** - Real-world tool integration architecture

## Pattern Demonstrated

**Sequential with External Tool Integration**

```
software_assistant (SequentialAgent)
├── analyzer_agent
│   └── Parse bug report → Extract searchable info
│   └── PRODUCTION: Uses MCP Toolbox to query ticket database
│
├── searcher_agent
│   └── Search: Internal DB + GitHub + Stack Overflow
│   └── PRODUCTION: Uses GitHub MCP Server + LangChain tools
│
└── solution_generator
    └── Generate fix from similar issue resolutions
    └── PRODUCTION: Uses RAG with vector search
```

## ADK 1.18+ Features Showcase

### MCP Toolbox for Databases (NEW in 1.18)

```python
from google.adk.tools import McpToolset

# Connect to MCP Toolbox server
mcp_tools = McpToolset(
    server_url="http://localhost:5000",
    toolset_name="database_tools"
)

# Use in agent
analyzer_agent = Agent(
    name="analyzer",
    tools=[mcp_tools],  # Now agent can query database!
    ...
)
```

**What it enables:**
- SQL queries as agent tools
- Vector search for similar issues (RAG)
- Database CRUD operations
- Structured data access

### GitHub MCP Server

```python
github_tools = McpToolset(
    server_url="https://github-mcp-server.com",
    auth_token=os.getenv("GITHUB_PERSONAL_ACCESS_TOKEN")
)

searcher_agent.tools = [github_tools]
```

**What it enables:**
- Search GitHub issues/PRs
- Fetch issue details
- Read PR comments
- Access repository metadata

### McpInstructionProvider (NEW in 1.18)

```python
from google.adk.tools import McpInstructionProvider

# Better prompts for MCP tools
instruction_provider = McpInstructionProvider(
    mcp_server_url="http://localhost:5000"
)
```

**Benefit:** Improved tool descriptions and context

### LangChain Tools Integration

```python
from langchain.tools import StackExchangeAPIWrapper
from google.adk.tools import LangChainTool

# Use any LangChain tool with ADK
stackoverflow = LangChainTool(StackExchangeAPIWrapper())
searcher_agent.tools = [stackoverflow]
```

## Architecture

### Workflow with External Tool Integration

```
User: "Fix: Login page freezes after 3 failed attempts"

    ↓

[ANALYZER AGENT]
Extracts: error="page freeze", component="login", trigger="3 failed attempts"
Priority: P0-Critical
🔧 PRODUCTION TOOL: Query tickets DB via MCP Toolbox
   SELECT * FROM tickets WHERE title LIKE '%login%freeze%'

    ↓

[SEARCHER AGENT]
Searches 3 sources simultaneously (simulated in workshop):

🔧 PRODUCTION TOOL: MCP Toolbox (PostgreSQL with vector search)
   - Find similar tickets using RAG
   - Vector similarity search on error descriptions

🔧 PRODUCTION TOOL: GitHub MCP Server
   - Search open/closed issues: "login freeze failed attempts"
   - Found: Issue #789 "Login lockout not clearing session"

🔧 PRODUCTION TOOL: LangChain StackOverflow
   - Search questions about login freezing
   - Found: Accepted answer about session management

Results: 3 similar issues found, all resolved with session clear logic

    ↓

[SOLUTION GENERATOR]
Root cause: Session not invalidating after failed attempts
Solution: Add session.clear() after failed login
Code: if (failed_attempts >= 3) { session.invalidate(); }
Testing: Try 3 failed logins, verify page doesn't freeze

    ↓

Developer gets actionable solution with code + tests
```

## Business Value

- **Engineering velocity** - Faster bug resolution
- **Knowledge retention** - Similar issues never solved twice
- **Reduced escalations** - Juniors can solve with AI assistance
- **Cross-repo learning** - GitHub knowledge accessible
- **Community knowledge** - Stack Overflow integrated

Use cases:
- IT support ticket resolution
- Developer debugging assistance
- Knowledge base as code
- Legacy system documentation

## Files

```
software_assistant/
├── agent.py          # 3 sub-agents + production MCP notes
├── .env              # API key
├── __init__.py       # Package marker
└── README.md         # This file
```

## Workshop vs Production

### Workshop Version (What Students Build)

**Simulated tools** - Agents describe what they'd search:
- "I would query the tickets database for..."
- "I would search GitHub issues for..."
- "I would look up Stack Overflow for..."

**Why simulate:**
- No database setup needed
- No GitHub PAT required
- Focus on agent patterns, not infrastructure
- 5-minute workshop setup

### Production Version (What Students Deploy Next)

**Real MCP tools** - Agents actually query:
- PostgreSQL ticket database
- GitHub repositories
- Stack Overflow API
- Documentation with RAG

**Implementation guide in README** - Shows exact code to add real tools

## Example Interaction

**Request:**
```
Bug Report:
Users are reporting intermittent 500 errors when uploading files >10MB.
Error appears in logs as "Request Entity Too Large".
Affects production environment, multiple customers complaining.
```

**Analyzer Output:**
```json
{
  "bug_summary": {
    "title": "File upload 500 error for files >10MB",
    "category": "backend/API",
    "priority": "P1-High",
    "component": "File upload service"
  },
  "technical_details": {
    "error_message": "Request Entity Too Large",
    "symptoms": "Intermittent 500 errors",
    "threshold": "Files >10MB"
  },
  "search_queries": [
    "Request Entity Too Large file upload",
    "nginx upload size limit",
    "HTTP 413 payload too large"
  ]
}
```

**Searcher Output:**
```json
{
  "similar_internal_tickets": [
    {
      "ticket_id": "TICK-456",
      "resolution": "Increased nginx client_max_body_size to 50M",
      "effectiveness": "Worked"
    }
  ],
  "github_issues": [
    {
      "repo": "nginx/nginx",
      "issue": 789,
      "solution": "Configure client_max_body_size in nginx.conf"
    }
  ],
  "stackoverflow_solutions": [
    {
      "title": "Nginx file upload 413 error",
      "accepted_answer": "Add client_max_body_size 50M; to http block",
      "votes": 234
    }
  ]
}
```

**Solution Generator Output:**
```json
{
  "root_cause_analysis": {
    "likely_cause": "Nginx default upload limit (1MB) blocking large files",
    "confidence": "High - identical error in 3 similar cases"
  },
  "recommended_solutions": [
    {
      "solution_id": 1,
      "approach": "Increase nginx upload size limit",
      "implementation_steps": [
        "1. Edit /etc/nginx/nginx.conf",
        "2. Add to http block: client_max_body_size 50M;",
        "3. Test config: sudo nginx -t",
        "4. Reload: sudo nginx -s reload"
      ],
      "code_example": "http {\n    client_max_body_size 50M;\n}",
      "estimated_effort": "5 minutes",
      "testing_steps": [
        "Upload 15MB test file",
        "Verify no 500 error",
        "Check logs for successful upload"
      ]
    }
  ],
  "citations": [
    "Internal TICK-456 (same fix)",
    "GitHub nginx/nginx #789",
    "Stack Overflow Q12345 (234 votes)"
  ]
}
```

## Success Criteria

- [ ] Correctly analyzes bug reports
- [ ] Simulates multi-source search
- [ ] Generates actionable solutions
- [ ] Cites sources appropriately
- [ ] Tested with 3 different bug types

## Production Implementation Guide

### Adding Real MCP Toolbox (PostgreSQL)

1. **Install MCP Toolbox:**
   ```bash
   # Download from: https://googleapis.github.io/genai-toolbox
   curl -O https://storage.googleapis.com/genai-toolbox/v0.6.0/linux/amd64/toolbox
   chmod +x toolbox
   ```

2. **Create tools.yaml:**
   ```yaml
   postgresql:
     kind: postgres
     host: 127.0.0.1
     database: tickets_db
     user: ${DB_USER}

   tools:
     search-tickets:
       query: "SELECT * FROM tickets WHERE title LIKE $1 OR description LIKE $1"
   ```

3. **Start MCP server:**
   ```bash
   ./toolbox --tools-file=tools.yaml
   ```

4. **Add to agent:**
   ```python
   from google.adk.tools import McpToolset

   db_tools = McpToolset(
       server_url="http://localhost:5000",
       toolset_name="tickets"
   )

   analyzer_agent.tools = [db_tools]
   ```

### Adding GitHub MCP Server

See: https://github.com/github/github-mcp-server

```python
github_tools = McpToolset(
    server_url="https://mcp.github.com",
    auth_token=os.getenv("GITHUB_PERSONAL_ACCESS_TOKEN")
)
```

### Adding Stack Overflow (LangChain)

```python
from langchain.tools import StackExchangeAPIWrapper
from google.adk.tools import LangChainTool

stackoverflow = LangChainTool(StackExchangeAPIWrapper())
searcher_agent.tools = [stackoverflow]
```

## Next Steps

**Step 8: Project Management (A2A Pattern)**

Preview: Already exists! We'll enhance it with agent-to-a2a pattern where agents call other agents as tools. Sequential + Parallel combined with advanced orchestration.

## References

- [ADK MCP Documentation](https://google.github.io/adk-docs/tools/mcp/)
- [MCP Toolbox](https://googleapis.github.io/genai-toolbox)
- [GitHub MCP Server](https://github.com/github/github-mcp-server)
- [ADK Samples - Software Bug Assistant](https://github.com/google/adk-samples/tree/main/python/agents/software-bug-assistant)

---

**Tags:** `step-7-software-assistant`, `advanced`, `mcp-integration`, `database-tools`, `production-patterns`
