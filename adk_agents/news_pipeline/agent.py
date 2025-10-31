"""
News Analysis Pipeline - Exercise 2
Demonstrates sequential multi-agent workflow with state passing
"""
from google.adk.agents import Agent, SequentialAgent
from google.adk.tools import google_search

# Agent 1: News Gatherer
news_gatherer = Agent(
    name="news_gatherer",
    description="Searches for latest news articles on a given topic",
    model="gemini-2.0-flash",
    instruction="Search for recent, credible news about: {topic}. Focus on reputable sources.",
    tools=[google_search],
    output_key="news_articles"
)

# Agent 2: Summarizer
summarizer = Agent(
    name="summarizer",
    description="Creates concise summaries of news articles",
    model="gemini-2.0-flash",
    instruction="Summarize these articles: {news_articles}. Be concise, factual, and objective. Highlight key points.",
    output_key="summary"
)

# Agent 3: Sentiment Analyzer
sentiment_analyzer = Agent(
    name="sentiment_analyzer",
    description="Analyzes sentiment and tone of news summaries",
    model="gemini-2.0-flash",
    instruction="Analyze sentiment in: {summary}. Identify overall tone (positive/negative/neutral) and key themes.",
    output_key="analysis"
)

# Sequential Pipeline - Chaining the agents
root_agent = SequentialAgent(
    name="news_analysis_pipeline",
    agents=[news_gatherer, summarizer, sentiment_analyzer]
)
