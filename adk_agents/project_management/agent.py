"""Project Manager Root Agent"""
from google.adk.agents import Agent, ParallelAgent, SequentialAgent
from google.adk.tools.agent_tool import AgentTool
from project_management.sub_agents.task_breakdown.agent import root_agent as task_breakdown
from project_management.sub_agents.resource_allocator.agent import root_agent as resource_allocator
from project_management.sub_agents.risk_assessor.agent import root_agent as risk_assessor
from project_management.sub_agents.timeline_estimator.agent import root_agent as timeline_estimator

# Parallel analysis of the tasks
parallel_analysis = ParallelAgent(
    name="parallel_project_analysis",
    description="Analyzes tasks for resources, risks, and timeline concurrently",
    sub_agents=[resource_allocator, risk_assessor, timeline_estimator]
)

# Synthesizer agent to combine all reports
synthesizer = Agent(
    name="project_plan_synthesizer",
    description="Synthesizes all analysis into a final project plan.",
    model="gemini-2.0-flash",
    instruction="You are a Project Manager. Synthesize the provided task list, resource allocation, risk assessment, and timeline estimation into a comprehensive and well-structured project plan. The final output should be easy for stakeholders to read and understand.",
)

# Complete Workflow: Task Breakdown -> Parallel Analysis -> Synthesis
root_agent = SequentialAgent(
    name="project_management_team",
    description="A team of AI agents that creates comprehensive project plans.",
    sub_agents=[task_breakdown, parallel_analysis, synthesizer]
)
