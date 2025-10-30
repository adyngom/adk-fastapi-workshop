"""
Custom tool examples for ADK agents
"""

def calculator_tool(expression: str) -> dict:
    """
    Safely evaluate mathematical expressions.
    
    Args:
        expression: A mathematical expression to evaluate (e.g., "2 + 2", "10 * 5")
    
    Returns:
        dict: Result of the calculation or error message
    """
    try:
        allowed_names = {
            "abs": abs, "round": round, "min": min, "max": max,
            "pow": pow, "sum": sum
        }
        result = eval(expression, {"__builtins__": {}}, allowed_names)
        return {"result": result, "expression": expression}
    except Exception as e:
        return {"error": str(e), "expression": expression}

def get_weather(location: str) -> dict:
    """
    Get current weather for a location.
    
    Args:
        location: City name or location
    
    Returns:
        dict: Weather information
    """
    # Placeholder - integrate with actual weather API
    return {
        "location": location,
        "temperature": "72°F",
        "condition": "Sunny",
        "humidity": "45%"
    }
