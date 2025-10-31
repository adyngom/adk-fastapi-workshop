"""
Competitive Analysis - Exercise 3
Demonstrates parallel execution + synthesis pattern
"""
from google.adk.agents import Agent, ParallelAgent, SequentialAgent
from competitive_analysis.sub_agents.competitor_a.agent import root_agent as competitor_a
from competitive_analysis.sub_agents.competitor_b.agent import root_agent as competitor_b
from competitive_analysis.sub_agents.competitor_c.agent import root_agent as competitor_c
from competitive_analysis.sub_agents.synthesizer.agent import root_agent as synthesizer

# Parallel Research - All three analysts work simultaneously
parallel_research = ParallelAgent(
    name="parallel_research",
    description="Researches multiple competitors concurrently",
    sub_agents=[competitor_a, competitor_b, competitor_c]
)

# Complete Workflow: Parallel research, then synthesis
# This is faster than sequential: 3 agents run at once, then combine
root_agent = SequentialAgent(
    name="competitive_analysis",
    description="Parallel competitive research with synthesis",
    sub_agents=[parallel_research, synthesizer]
)
