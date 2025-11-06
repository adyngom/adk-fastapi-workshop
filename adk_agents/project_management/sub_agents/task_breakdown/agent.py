"""Task Breakdown Specialist Agent"""
from google.adk.agents import Agent

root_agent = Agent(
    name="task_breakdown_specialist",
    description="Breaks down project descriptions into actionable tasks.",
    model="gemini-2.0-flash",
    instruction="You are a Task Breakdown Specialist. Your goal is to take a high-level project description and break it down into a comprehensive list of specific, actionable tasks. Ensure the tasks are clear, concise, and cover all aspects of the project described.",
    output_key="task_list"
)
