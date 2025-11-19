"""
ADK Workshop UI - Production-Ready Streamlit Interface
Auto-discovers and runs ADK agents directly (no FastAPI dependency)
"""
import streamlit as st
import sys
import importlib
import asyncio
from pathlib import Path
from datetime import datetime
import os

# Page configuration
st.set_page_config(
    page_title="ADK Workshop",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: 700;
        color: #1f2937;
        margin-bottom: 1rem;
    }
    .agent-card {
        padding: 1rem;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 0.5rem;
        margin-bottom: 1rem;
    }
    .stChatMessage {
        background-color: #f8f9fa;
    }
</style>
""", unsafe_allow_html=True)

# Add adk_agents to Python path
project_root = Path(__file__).parent.parent.parent
adk_agents_path = project_root / "adk_agents"
sys.path.insert(0, str(adk_agents_path))

@st.cache_resource
def discover_agents():
    """Auto-discover all ADK agents from adk_agents/ directory"""
    agents = {}

    if not adk_agents_path.exists():
        st.error(f"adk_agents directory not found at {adk_agents_path}")
        return agents

    for item in adk_agents_path.iterdir():
        # Skip hidden directories and __pycache__
        if not item.is_dir() or item.name.startswith('_') or item.name.startswith('.'):
            continue

        agent_file = item / "agent.py"
        if not agent_file.exists():
            continue

        try:
            # Import agent module
            module = importlib.import_module(f"{item.name}.agent")

            if hasattr(module, 'root_agent'):
                root_agent = module.root_agent
                agents[item.name] = {
                    "agent": root_agent,
                    "name": getattr(root_agent, 'name', item.name),
                    "description": getattr(root_agent, 'description', f"ADK Agent: {item.name}"),
                    "model": getattr(root_agent, 'model', 'gemini-2.0-flash-exp')
                }
        except Exception as e:
            st.sidebar.warning(f"Failed to load {item.name}: {str(e)}")

    return agents

async def run_agent_streaming(agent, user_message):
    """Run ADK agent with streaming response"""
    from google import genai
    from google.genai import types

    # Get API key from environment
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        st.error("GOOGLE_API_KEY not found in environment!")
        return

    client = genai.Client(api_key=api_key)

    # Add date context
    current_date = datetime.now().strftime("%B %d, %Y")
    message_with_context = f"Today's date is {current_date}.\n\nUser: {user_message}"

    # Build config with agent's instruction and tools
    config = None
    if hasattr(agent, 'instruction'):
        config_params = {"system_instruction": agent.instruction}

        # Add tools if agent has them
        if hasattr(agent, 'tools') and agent.tools:
            config_params["tools"] = agent.tools

        config = types.GenerateContentConfig(**config_params)

    # Get model name
    model = agent.model if hasattr(agent, 'model') else "gemini-2.0-flash-exp"

    # Stream response
    response = await client.aio.models.generate_content_stream(
        model=model,
        contents=[types.Content(
            role="user",
            parts=[types.Part(text=message_with_context)]
        )],
        config=config
    )

    full_response = ""
    message_placeholder = st.empty()

    async for chunk in response:
        if chunk.text:
            full_response += chunk.text
            message_placeholder.markdown(full_response)

    return full_response

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = {}  # Per-agent message history
if "current_agent" not in st.session_state:
    st.session_state.current_agent = None

# Discover agents
agents = discover_agents()

if not agents:
    st.error("No agents found! Check adk_agents/ directory.")
    st.stop()

# Sidebar - Agent Selection
with st.sidebar:
    st.markdown("## 🤖 Agent Selection")

    # Create agent options with descriptions
    agent_options = {
        info["description"]: agent_name
        for agent_name, info in agents.items()
    }

    selected_description = st.selectbox(
        "Choose an agent",
        options=list(agent_options.keys())
    )

    selected_agent_name = agent_options[selected_description]
    selected_agent_info = agents[selected_agent_name]

    # Show agent details in styled card
    st.markdown(f"""
    <div class="agent-card">
        <h3>{selected_agent_info['name']}</h3>
        <p><strong>Model:</strong> {selected_agent_info['model']}</p>
        <p><strong>Type:</strong> {type(selected_agent_info['agent']).__name__}</p>
    </div>
    """, unsafe_allow_html=True)

    # Check if agent has tools
    if hasattr(selected_agent_info['agent'], 'tools') and selected_agent_info['agent'].tools:
        st.markdown("**🛠️ Tools Available:**")
        for tool in selected_agent_info['agent'].tools:
            tool_name = tool.__name__ if hasattr(tool, '__name__') else str(tool)
            st.markdown(f"- `{tool_name}`")

    # Clear chat button
    if st.button("🗑️ Clear Chat History", use_container_width=True):
        if selected_agent_name in st.session_state.messages:
            st.session_state.messages[selected_agent_name] = []
        st.rerun()

    st.markdown("---")
    st.markdown(f"**Agents Loaded:** {len(agents)}")
    st.markdown(f"**Workshop:** ADK + Production UI")

# Clear history when switching agents
if st.session_state.current_agent != selected_agent_name:
    st.session_state.current_agent = selected_agent_name
    if selected_agent_name not in st.session_state.messages:
        st.session_state.messages[selected_agent_name] = []

# Main chat interface
st.markdown('<h1 class="main-header">🤖 ADK Workshop Chat</h1>', unsafe_allow_html=True)

# Display chat history for current agent
current_messages = st.session_state.messages.get(selected_agent_name, [])

for message in current_messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Type your message..."):
    # Add user message
    current_messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    # Get agent response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                # Run agent asynchronously
                response = asyncio.run(
                    run_agent_streaming(selected_agent_info['agent'], prompt)
                )

                # Add to history
                current_messages.append({"role": "assistant", "content": response})
                st.session_state.messages[selected_agent_name] = current_messages

            except Exception as e:
                error_msg = f"Error: {str(e)}"
                st.error(error_msg)
                current_messages.append({"role": "assistant", "content": error_msg})

# Footer
st.markdown("---")
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown(f"**Agent:** {selected_agent_info['name']}")
with col2:
    st.markdown(f"**Messages:** {len(current_messages)}")
with col3:
    st.markdown(f"**Model:** {selected_agent_info['model']}")
