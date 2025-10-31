"""News Gatherer Agent - Searches for latest news articles"""
from google.adk.agents import Agent
from google.adk.tools import google_search

root_agent = Agent(
    name="news_gatherer",
    description="Searches for latest news articles on a given topic",
    model="gemini-2.0-flash",
    instruction="Search for recent, credible news about the topic. Focus on reputable sources from the last 24-48 hours.",
    tools=[google_search],
    output_key="news_articles"
)
