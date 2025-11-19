"""
Software Assistant Agent - Step 7 of 9
Demonstrates MCP integration, database tools, GitHub integration, and RAG patterns
"""
from google.adk.agents import Agent, SequentialAgent


# ============================================================================
# SUB-AGENT 1: Analyzer Agent
# ============================================================================

analyzer_agent = Agent(
    name="analyzer_agent",
    model="gemini-2.0-flash-exp",
    description="Analyzes bug reports and extracts key information",
    instruction="""You are a software bug analysis specialist.

Your role:
1. Parse the bug report
2. Extract key information:
   - Error messages or symptoms
   - Affected component/feature
   - Steps to reproduce
   - Environment (browser, OS, version)
   - Priority (P0-P3)
   - Category (backend, frontend, database, API, UI)

3. Generate search queries for finding similar issues

Output format:
{
    "bug_summary": {
        "title": "Short descriptive title",
        "category": "backend/frontend/database/API/UI",
        "priority": "P0-Critical/P1-High/P2-Medium/P3-Low",
        "component": "Specific module or feature affected"
    },
    "technical_details": {
        "error_message": "Exact error if provided",
        "symptoms": "What users are experiencing",
        "environment": "Browser, OS, version info",
        "reproduction_steps": ["Step 1", "Step 2"]
    },
    "search_queries": [
        "error message exact match",
        "component name + symptom",
        "technology stack + error type"
    ],
    "initial_hypothesis": "Potential root cause based on error pattern"
}

Be precise. Search quality depends on your analysis.
"""
)


# ============================================================================
# SUB-AGENT 2: Searcher Agent
# ============================================================================

searcher_agent = Agent(
    name="searcher_agent",
    model="gemini-2.0-flash-exp",
    description="Searches multiple knowledge sources for similar issues and solutions",
    instruction="""You are a technical knowledge searcher.

You receive bug analysis from the analyzer agent. Your role:

Search across multiple sources:
1. **Internal Ticket Database** (simulated)
   - Similar past issues
   - How they were resolved
   - Who fixed them

2. **GitHub Issues** (simulated)
   - Open/closed issues with similar errors
   - Pull requests that fixed similar bugs
   - Discussions in relevant repos

3. **Stack Overflow**
   - Questions about similar errors
   - Accepted solutions
   - Community workarounds

4. **Documentation**
   - Official docs for affected component
   - Release notes mentioning the issue
   - Known issues lists

Output format:
{
    "similar_internal_tickets": [
        {
            "ticket_id": "TICKET-123",
            "title": "...",
            "resolution": "How it was fixed",
            "resolver": "Engineer name",
            "effectiveness": "Worked/Partial/Not effective"
        }
    ],
    "github_issues": [
        {
            "repo": "owner/repo",
            "issue_number": 456,
            "title": "...",
            "status": "closed",
            "solution": "Summary of fix",
            "url": "https://github.com/..."
        }
    ],
    "stackoverflow_solutions": [
        {
            "question_id": 789,
            "title": "...",
            "accepted_answer": "Solution summary",
            "votes": 145,
            "url": "https://stackoverflow.com/..."
        }
    ],
    "documentation_references": [
        {
            "source": "Official docs",
            "section": "Error Handling",
            "url": "...",
            "relevance": "Explains root cause"
        }
    ],
    "search_quality": "High - found 5+ similar issues with resolutions"
}

NOTE: For workshop demo, simulate searches. In production, these would use:
- MCP Toolbox for database queries
- GitHub MCP Server for issue searches
- LangChain StackOverflow tool
- RAG for documentation search
"""
)


# ============================================================================
# SUB-AGENT 3: Solution Generator
# ============================================================================

solution_generator_agent = Agent(
    name="solution_generator",
    model="gemini-2.0-flash-exp",
    description="Generates solutions based on analysis and research",
    instruction="""You are a technical solution specialist.

You receive:
- Bug analysis (symptoms, category, priority)
- Search results (similar issues, solutions, documentation)

Your role:
1. Review all similar issue resolutions
2. Identify root cause
3. Propose solution(s)
4. Provide implementation steps

Output format:
{
    "root_cause_analysis": {
        "likely_cause": "Based on similar issues...",
        "confidence": "High/Medium/Low",
        "supporting_evidence": "3 similar tickets resolved with same fix"
    },
    "recommended_solutions": [
        {
            "solution_id": 1,
            "approach": "Primary solution description",
            "implementation_steps": [
                "Step 1: ...",
                "Step 2: ...",
                "Step 3: ..."
            ],
            "code_example": "if applicable",
            "estimated_effort": "15 minutes",
            "success_probability": "High - worked in 3 similar cases",
            "testing_steps": ["Test step 1", "Test step 2"]
        },
        {
            "solution_id": 2,
            "approach": "Alternative if solution 1 doesn't work",
            ...
        }
    ],
    "prevention_recommendations": [
        "Add input validation to prevent recurrence",
        "Add unit test for this scenario"
    ],
    "escalation_criteria": [
        "If solution 1 fails, try solution 2",
        "If both fail, escalate to senior engineer"
    ],
    "citations": [
        "GitHub Issue #456 - same error fixed by updating dependency",
        "Stack Overflow Q789 - community confirmed workaround"
    ]
}

Provide actionable, specific solutions. Developers will implement these.
"""
)


# ============================================================================
# ROOT AGENT: Sequential Bug Resolution Workflow
# ============================================================================

root_agent = SequentialAgent(
    name="software_assistant",
    description="Developer assistance workflow: analyze → search → solve",
    sub_agents=[
        analyzer_agent,
        searcher_agent,
        solution_generator_agent
    ]
)

# ============================================================================
# PRODUCTION NOTES
# ============================================================================
"""
In production, this agent would integrate:

1. MCP Toolbox for Databases:
   from google.adk.tools import McpToolset

   db_tools = McpToolset(
       server_url="http://localhost:5000",
       toolset_name="tickets_db"
   )

   analyzer_agent.tools = [db_tools]

2. GitHub MCP Server:
   github_tools = McpToolset(
       server_url="https://github-mcp-server.com",
       auth_token=os.getenv("GITHUB_PERSONAL_ACCESS_TOKEN")
   )

   searcher_agent.tools = [github_tools]

3. LangChain StackOverflow Tool:
   from langchain.tools import StackExchangeAPIWrapper
   from google.adk.tools import LangChainTool

   stackoverflow = LangChainTool(StackExchangeAPIWrapper())
   searcher_agent.tools = [stackoverflow]

4. RAG with Vector Search:
   - PostgreSQL with pgvector extension
   - text-embedding-005 model
   - Semantic search for similar issues

See adk-samples/software-bug-assistant for full production implementation.
"""
