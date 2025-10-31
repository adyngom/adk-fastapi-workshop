"""
Custom tools for greeting_agent
Demonstrates how to create simple Python functions as agent tools
"""
from datetime import datetime


def get_workshop_info() -> dict:
    """Get information about the current ADK workshop.

    This tool provides details about the workshop including location,
    date, duration, and topics covered.

    Returns:
        dict: Workshop information including name, location, date, duration, and topics
    """
    return {
        "workshop_name": "Building Production AI Agents with Google ADK",
        "event": "DevFest Atlanta 2025",
        "date": "October 31, 2025",
        "duration": "2 hours",
        "location": "Atlanta, GA",
        "topics": [
            "ADK fundamentals",
            "Multi-agent systems",
            "Sequential and parallel patterns",
            "FastAPI integration",
            "Production deployment"
        ]
    }


def get_current_time() -> dict:
    """Get the current time in Atlanta timezone.

    Returns:
        dict: Current time information including time, timezone, and formatted string
    """
    now = datetime.now()
    return {
        "current_time": now.strftime("%I:%M %p"),
        "date": now.strftime("%B %d, %Y"),
        "timezone": "EST (Eastern Standard Time)",
        "formatted": now.strftime("%A, %B %d, %Y at %I:%M %p EST")
    }


def list_available_agents() -> dict:
    """List all available agents in this workshop.

    Returns:
        dict: Information about available agents and their purposes
    """
    return {
        "agents": [
            {
                "name": "greeting_agent",
                "type": "Single Agent",
                "purpose": "Friendly workshop assistant with custom tools",
                "demonstrates": "Basic agent + custom Python functions as tools"
            },
            {
                "name": "news_pipeline",
                "type": "Sequential Multi-Agent",
                "purpose": "News analysis with 3-agent pipeline",
                "demonstrates": "Sequential workflow, state passing, output_key usage"
            },
            {
                "name": "competitive_analysis",
                "type": "Parallel Multi-Agent",
                "purpose": "Competitive research with parallel execution",
                "demonstrates": "Parallel agents, performance optimization, synthesis"
            }
        ],
        "total_agents": 3,
        "patterns_covered": ["Single", "Sequential", "Parallel + Synthesis"]
    }
