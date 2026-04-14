from smolagents import CodeAgent, InferenceClientModel
from retriever import guest_tool
from tools import search_tool, weather_tool, hub_tool

# Initialize model
model = InferenceClientModel()

# Final Alfred Agent
alfred = CodeAgent(
    tools=[guest_tool, search_tool, weather_tool, hub_tool],
    model=model,
    instructions="""
You are Alfred, an intelligent and charming gala assistant.

You help the host by:
- Providing guest information (use guest_info_retriever for known guests)
- Giving weather updates for planning events
- Searching latest world info when needed
- Sharing AI model insights using hub_stats

Rules:
- Use guest_info_retriever for guest-related queries
- Use weather_info for weather questions
- Use web search only if needed
- Keep answers concise, elegant, and helpful
"""
)

# Interactive mode
while True:
    query = input("\nAsk Alfred something (or type 'exit'): ")
    
    if query.lower() == "exit":
        print("Goodbye 👋")
        break

    response = alfred.run(query)
    print("\n🎩 Alfred says:")
    print(response)