"""
Simple ADK agent example
"""
from google import genai
from google.genai import types

def create_simple_agent():
    """Create a simple conversational agent"""
    
    # Define agent configuration
    agent_config = {
        "name": "simple_assistant",
        "description": "A helpful assistant that can answer questions",
        "model": "gemini-2.0-flash-exp",
        "generation_config": {
            "temperature": 0.7,
            "top_p": 0.95,
            "max_output_tokens": 8192,
        }
    }
    
    return agent_config

def create_specialized_agent():
    """Create a specialized agent with specific instructions"""
    
    agent_config = {
        "name": "code_reviewer",
        "description": "Reviews code for best practices, bugs, and security issues",
        "model": "gemini-2.0-flash-exp",
        "system_instruction": """You are an expert code reviewer. 
        Analyze code for:
        - Best practices and design patterns
        - Potential bugs and edge cases
        - Security vulnerabilities
        - Performance optimizations
        - Code clarity and maintainability
        
        Provide specific, actionable feedback.""",
        "generation_config": {
            "temperature": 0.3,
            "top_p": 0.9,
            "max_output_tokens": 8192,
        }
    }
    
    return agent_config
