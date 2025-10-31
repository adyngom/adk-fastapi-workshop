"""Competitor B Research Agent"""
from google.adk.agents import Agent
from google.adk.tools import google_search

root_agent = Agent(
    name="competitor_b_analyst",
    description="Researches Competitor B (Microsoft in AI/Cloud space)",
    model="gemini-2.0-flash",
    instruction="Research Microsoft's latest AI and Cloud offerings. Focus on Azure AI, Copilot, and competitive positioning.",
    tools=[google_search],
    output_key="competitor_b_data"
)
