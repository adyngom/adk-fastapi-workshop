"""
SOLUTION: Custom tools for greeting_agent
Demonstrates how to create simple Python functions as agent tools
"""
from datetime import datetime


def get_company_info() -> dict:
    """Get information about the user's company and current AI initiative.

    This tool provides details about the organization and ongoing AI agent projects.

    Returns:
        dict: Company information including name, industry, and current AI initiatives
    """
    # SOLUTION: Updated with example company data
    return {
        "company_name": "TechVentures Inc",
        "industry": "SaaS & Enterprise Software",
        "location": "Austin, TX",
        "current_initiative": "AI-Powered Customer Success Platform",
        "use_cases": [
            "Automated customer onboarding",
            "Intelligent ticket routing and resolution",
            "Predictive churn analysis",
            "Content generation for help articles"
        ],
        "team_size": "8 engineers, 2 data scientists, 2 product managers",
        "goal": "Deploy AI agents to reduce support costs by 40% while improving satisfaction"
    }


def get_current_time() -> dict:
    """Get the current time in Eastern timezone.

    Returns:
        dict: Current time information including time, timezone, and formatted string
    """
    from datetime import timezone, timedelta

    # Eastern Time is UTC-5 (EST) or UTC-4 (EDT)
    eastern = timezone(timedelta(hours=-5))
    now = datetime.now(eastern)

    return {
        "current_time": now.strftime("%I:%M %p"),
        "date": now.strftime("%B %d, %Y"),
        "timezone": "EST (Eastern Standard Time)",
        "formatted": now.strftime("%A, %B %d, %Y at %I:%M %p EST")
    }


# SOLUTION: Exercise 1.2 - New tool for team members
def get_team_members() -> dict:
    """Get the current team roster and roles.

    Returns information about team members including names,
    roles, and areas of responsibility.

    Returns:
        dict: Team member information with names, roles, and focus areas
    """
    return {
        "team": [
            {
                "name": "Sarah Chen",
                "role": "Tech Lead",
                "focus": "AI Agent Architecture",
                "experience": "5 years"
            },
            {
                "name": "Marcus Johnson",
                "role": "Senior Engineer",
                "focus": "FastAPI Integration",
                "experience": "4 years"
            },
            {
                "name": "Priya Patel",
                "role": "Data Scientist",
                "focus": "ML Models & RAG",
                "experience": "3 years"
            },
            {
                "name": "Alex Rodriguez",
                "role": "Product Manager",
                "focus": "Customer Success AI",
                "experience": "6 years"
            },
            {
                "name": "Jordan Lee",
                "role": "Engineer",
                "focus": "UI/UX & Streamlit",
                "experience": "2 years"
            }
        ],
        "total_members": 5,
        "departments": ["Engineering", "Data Science", "Product"],
        "currently_hiring": True,
        "open_positions": ["ML Engineer", "DevOps Engineer"]
    }
