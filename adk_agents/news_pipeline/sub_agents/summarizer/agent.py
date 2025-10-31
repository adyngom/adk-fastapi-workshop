"""Summarizer Agent - Creates concise news summaries"""
from google.adk.agents import Agent

root_agent = Agent(
    name="summarizer",
    description="Creates concise summaries of news articles",
    model="gemini-2.0-flash",
    instruction="Summarize these news articles: {news_articles}. Be concise, factual, and objective. Highlight key points and main developments.",
    output_key="summary"
)
