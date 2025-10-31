"""
Greeting Agent - ADK Workshop Demo
A simple agent that greets users and demonstrates ADK capabilities
"""
from google.genai import types
from google.adk.agents import Agent

# Create the greeting agent (must be named root_agent for ADK web)
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
