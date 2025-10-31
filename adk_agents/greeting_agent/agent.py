"""
Greeting Agent - ADK Workshop Demo
Demonstrates basic agent with custom Python function tools
"""
from google.adk.agents import Agent
from .tools import get_workshop_info, get_current_time, list_available_agents

# Create the greeting agent (must be named root_agent for ADK web)
root_agent = Agent(
    name="greeting_agent",
    model="gemini-2.0-flash-exp",
    description="A friendly assistant that greets users and provides workshop information",
    instruction="""You are a helpful and friendly assistant for the ADK Workshop.

Your role is to:
1. Greet users warmly
2. Ask for their name if they haven't provided it
3. Greet them by name once you know it
4. Be enthusiastic about helping them learn about Google's Agent Development Kit (ADK)
5. Use the available tools when asked about:
   - Workshop details (use get_workshop_info)
   - Current time (use get_current_time)
   - Available agents (use list_available_agents)
6. Keep responses concise and friendly

Remember to be encouraging and supportive as they learn about building AI agents!
""",
    tools=[get_workshop_info, get_current_time, list_available_agents]
)
