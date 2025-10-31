"""Competitor C Research Agent"""
from google.adk.agents import Agent
from google.adk.tools import google_search

root_agent = Agent(
    name="competitor_c_analyst",
    description="Researches Competitor C (Amazon in AI/Cloud space)",
    model="gemini-2.0-flash",
    instruction="Research Amazon's latest AI and Cloud offerings. Focus on AWS AI services, Bedrock, and market strategy.",
    tools=[google_search],
    output_key="competitor_c_data"
)
