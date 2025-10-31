"""
News Analysis Pipeline - Exercise 2
Demonstrates sequential multi-agent workflow with state passing
"""
from google.adk.agents import Agent, SequentialAgent
from news_pipeline.sub_agents.news_gatherer.agent import root_agent as news_gatherer
from news_pipeline.sub_agents.summarizer.agent import root_agent as summarizer
from news_pipeline.sub_agents.sentiment_analyzer.agent import root_agent as sentiment_analyzer

# Sequential Pipeline - Chaining the agents
# Gatherer finds news -> Summarizer condenses -> Analyzer evaluates sentiment
root_agent = SequentialAgent(
    name="news_analysis_pipeline",
    agents=[news_gatherer, summarizer, sentiment_analyzer]
)
