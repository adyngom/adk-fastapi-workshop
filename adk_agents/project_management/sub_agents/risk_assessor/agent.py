"""Risk Assessor Agent"""
from google.adk.agents import Agent

root_agent = Agent(
    name="risk_assessor",
    description="Identifies potential risks and mitigation strategies for a project.",
    model="gemini-2.0-flash",
    instruction="You are a Risk Assessor. Given a project description and a list of tasks, identify potential risks that could impact the project's success (e.g., technical challenges, resource shortages, timeline delays). For each identified risk, propose a mitigation strategy.",
    output_key="risk_assessment"
)
