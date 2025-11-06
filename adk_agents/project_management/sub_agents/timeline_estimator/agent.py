"""Timeline Estimator Agent"""
from google.adk.agents import Agent

root_agent = Agent(
    name="timeline_estimator",
    description="Estimates the duration for each task and the overall project.",
    model="gemini-2.0-flash",
    instruction="You are a Timeline Estimator. Given a list of tasks for a project, estimate the time required to complete each task (e.g., in hours or days). Also, provide an estimated total duration for the project, considering potential dependencies between tasks (e.g., some tasks might need to be done sequentially, while others can be done in parallel).",
    output_key="timeline_estimation"
)
