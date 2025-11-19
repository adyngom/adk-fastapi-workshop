"""
Custom tools for greeting_agent
Demonstrates how to create simple Python functions as agent tools
"""
from datetime import datetime


def get_company_info() -> dict:
    """Get information about the user's company and current AI initiative.

    This tool provides details about the organization and ongoing AI agent projects.

    INSTRUCTOR NOTE: Students will customize this with their own company/project
    information as their first hands-on exercise in the workshop.

    Returns:
        dict: Company information including name, industry, and current AI initiatives
    """
    return {
        "company_name": "Acme Corporation",
        "industry": "Technology & Innovation",
        "location": "San Francisco, CA",
        "current_initiative": "Enterprise AI Agent Platform",
        "use_cases": [
            "Customer service automation",
            "Financial analysis & reporting",
            "Content creation pipelines",
            "Software development assistance"
        ],
        "team_size": "12 engineers, 3 product managers",
        "goal": "Deploy production-ready AI agents for enterprise workflows"
    }


def get_current_time() -> dict:
    """Get the current time in Atlanta timezone.

    Returns:
        dict: Current time information including time, timezone, and formatted string
    """
    from datetime import timezone, timedelta

    # Eastern Time is UTC-5 (EST) or UTC-4 (EDT)
    # Using EST for consistency with workshop location
    eastern = timezone(timedelta(hours=-5))
    now = datetime.now(eastern)

    return {
        "current_time": now.strftime("%I:%M %p"),
        "date": now.strftime("%B %d, %Y"),
        "timezone": "EST (Eastern Standard Time)",
        "formatted": now.strftime("%A, %B %d, %Y at %I:%M %p EST")
    }


def get_workshop_roadmap() -> dict:
    """Get the complete 9-agent workshop progression.

    Shows all agents students will build, from foundation to production-grade systems.

    Returns:
        dict: Workshop roadmap with all 9 agents and their patterns
    """
    return {
        "workshop_title": "Building Production AI Agents with ADK + FastAPI",
        "total_agents": 9,
        "duration": "4 hours",
        "phases": [
            {
                "name": "Phase 1: Foundation",
                "agents": ["greeting_agent"],
                "pattern": "Single Agent"
            },
            {
                "name": "Phase 2: Real Workflows",
                "agents": ["customer_service", "content_pipeline", "medical_authorization"],
                "pattern": "Sequential Workflows"
            },
            {
                "name": "Phase 3: Intelligent Decision-Making",
                "agents": ["financial_advisor", "brand_intelligence"],
                "pattern": "Parallel + Synthesis"
            },
            {
                "name": "Phase 4: Production-Grade Systems",
                "agents": ["software_assistant", "project_management", "verified_recommendations"],
                "pattern": "Complex Multi-Agent with Verification"
            }
        ],
        "current_step": 1,
        "next_agent": "customer_service",
        "progression_file": "workshop_progression.yaml"
    }
