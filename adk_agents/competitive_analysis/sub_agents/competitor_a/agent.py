"""Competitor A Research Agent"""
from google.adk.agents import Agent
from google.adk.tools import google_search

root_agent = Agent(
    name="competitor_a_analyst",
    description="Researches Competitor A (Google in AI/Cloud space)",
    model="gemini-2.0-flash",
    instruction="Research Google's latest AI and Cloud offerings. Focus on new products, features, and market position.",
    tools=[google_search],
    output_key="competitor_a_data"
)
