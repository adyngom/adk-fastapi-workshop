"""
Generic Streamlit Chat Interface for ADK Agents
Works with any agent via FastAPI backend
"""
import streamlit as st
import requests
import json
import os
from typing import Optional

# Configuration
API_URL = os.getenv("API_URL", "http://localhost:8000")

# Page configuration
st.set_page_config(
    page_title="ADK Agent Chat",
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
        margin-bottom: 1rem;
    }
    .agent-info {
        padding: 1rem;
        background-color: #f0f2f6;
        border-radius: 0.5rem;
        margin-bottom: 1rem;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []
if "session_id" not in st.session_state:
    import time
    st.session_state.session_id = f"streamlit_{int(time.time())}"
if "previous_agent" not in st.session_state:
    st.session_state.previous_agent = None

# Sidebar - Agent Selection
with st.sidebar:
    st.header("🤖 Agent Selection")

    # Fetch available agents
    try:
        agents_response = requests.get(f"{API_URL}/api/agents/list", timeout=5)
        agents_response.raise_for_status()
        agents = agents_response.json()

        if agents:
            # Agent selector
            selected_agent_name = st.selectbox(
                "Choose an agent",
                options=[agent["name"] for agent in agents],
                format_func=lambda name: next(
                    (agent["description"] for agent in agents if agent["name"] == name),
                    name
                )
            )

            # Show agent details
            selected_agent = next(a for a in agents if a["name"] == selected_agent_name)

            st.markdown("### Agent Details")
            st.markdown(f"**Name**: {selected_agent['name']}")
            st.markdown(f"**Description**: {selected_agent['description']}")

            if selected_agent.get("capabilities"):
                st.markdown("**Capabilities**:")
                for cap in selected_agent["capabilities"]:
                    st.markdown(f"- {cap}")

            # Clear chat when agent changes
            if st.session_state.previous_agent != selected_agent_name:
                if st.session_state.previous_agent is not None:  # Don't clear on first load
                    st.session_state.messages = []
                    import time
                    st.session_state.session_id = f"streamlit_{int(time.time())}"
                    st.info(f"Switched to {selected_agent_name}. Chat history cleared.")
                st.session_state.previous_agent = selected_agent_name

        else:
            st.warning("No agents available")
            selected_agent_name = None

    except requests.exceptions.RequestException as e:
        st.error(f"Cannot connect to API: {e}")
        st.info(f"Make sure FastAPI is running at {API_URL}")
        selected_agent_name = None

    # Clear chat button
    if st.button("Clear Chat History", type="secondary"):
        st.session_state.messages = []
        st.rerun()

# Main chat interface
st.markdown('<h1 class="main-header">💬 ADK Agent Chat</h1>', unsafe_allow_html=True)

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if selected_agent_name:
    if prompt := st.chat_input("Type your message..."):
        # Add user message to chat
        st.session_state.messages.append({"role": "user", "content": prompt})

        with st.chat_message("user"):
            st.markdown(prompt)

        # Get response from agent
        with st.chat_message("assistant"):
            message_placeholder = st.empty()

            try:
                # Call FastAPI backend
                response = requests.post(
                    f"{API_URL}/api/agents/chat",
                    json={
                        "message": prompt,
                        "agent": selected_agent_name,
                        "session_id": st.session_state.session_id
                    },
                    timeout=30
                )

                response.raise_for_status()
                result = response.json()

                # Display response
                assistant_message = result.get("message", "No response")
                message_placeholder.markdown(assistant_message)

                # Add to history
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": assistant_message
                })

            except requests.exceptions.Timeout:
                error_msg = "Request timed out. The agent might be processing a complex query."
                message_placeholder.error(error_msg)
                st.session_state.messages.append({"role": "assistant", "content": error_msg})

            except requests.exceptions.RequestException as e:
                error_msg = f"Error communicating with backend: {e}"
                message_placeholder.error(error_msg)
                st.session_state.messages.append({"role": "assistant", "content": error_msg})

else:
    st.info("👈 Select an agent from the sidebar to start chatting")

# Footer
st.markdown("---")
st.markdown(f"**Session ID**: `{st.session_state.session_id}` | **API**: `{API_URL}`")
