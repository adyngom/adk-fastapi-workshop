"""Resource Allocator Agent"""
from google.adk.agents import Agent

root_agent = Agent(
    name="resource_allocator",
    description="Suggests necessary resources for a given list of tasks.",
    model="gemini-2.0-flash",
    instruction="You are a Resource Allocator. Given a list of tasks for a project, suggest the necessary resources for each task. Resources can include specific roles (e.g., 'Frontend Developer', 'UI Designer'), skills required, and potential tools or software needed.",
    output_key="resource_allocation"
)
