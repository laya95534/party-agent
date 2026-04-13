from smolagents import CodeAgent, tool, InferenceClientModel

@tool
def calculator(expression: str) -> str:
    """
    Evaluate a mathematical expression.

    Args:
        expression: A math expression like '2+2'
    """
    return str(eval(expression))

@tool
def suggest_menu(occasion: str) -> str:
    """
    Suggest menu for party.

    Args:
        occasion: type of party
    """
    if occasion == "casual":
        return "Pizza, snacks, drinks"
    elif occasion == "formal":
        return "3-course dinner"
    elif occasion == "superhero":
        return "High-energy buffet"
    return "Custom menu"

@tool
def get_weather(city: str) -> str:
    """
    Get weather info.

    Args:
        city: city name
    """
    return "Sunny, 32°C"

agent = CodeAgent(
    tools=[calculator, suggest_menu, get_weather],
    model=InferenceClientModel(model_id="Qwen/Qwen2.5-Coder-7B-Instruct"),
    max_steps=3,
    verbosity_level=2
)

if __name__ == "__main__":
    print(agent.run(
    "ONLY use these tools: calculator and suggest_menu. "
    "First call suggest_menu with 'superhero'. "
    "Then use calculator for 100+200. "
    "Do not use any other tools. "
    "Return clean final answer."
))