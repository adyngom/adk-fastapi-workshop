import asyncio
from agents.manager import AgentManager

async def test_project_management_agent():
    project_description = "Build a simple e-commerce website with a product catalog, shopping cart, and user authentication."
    
    print(f"Running Project Management Agent with description: {project_description}")
    
    agent_manager = AgentManager()
    await agent_manager.initialize()

    full_response = ""
    try:
        async for chunk in agent_manager.stream_chat(
            session_id="test_session",
            message=project_description,
            agent_name="project_management"
        ):
            if chunk.get("type") == "chunk":
                content = chunk.get("content", "")
                print(content, end="", flush=True)
                full_response += content
            elif chunk.get("error"):
                print(f"\nError from agent: {chunk['error']}")
                break
        
        print("\n\n--- Final Project Plan ---")
        print(full_response)
        print("\n-------------------------")

    except Exception as e:
        print(f"\nError running agent: {e}")

if __name__ == "__main__":
    asyncio.run(test_project_management_agent())
