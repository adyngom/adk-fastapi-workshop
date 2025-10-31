"""Sentiment Analyzer Agent - Analyzes tone and themes in news"""
from google.adk.agents import Agent

root_agent = Agent(
    name="sentiment_analyzer",
    description="Analyzes sentiment and tone of news summaries",
    model="gemini-2.0-flash",
    instruction="Analyze sentiment in: {summary}. Identify if it's positive, negative, or neutral. Highlight key themes and implications.",
    output_key="analysis"
)
