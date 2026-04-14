from smolagents import DuckDuckGoSearchTool, Tool
import random
from huggingface_hub import list_models

# Web Search Tool
search_tool = DuckDuckGoSearchTool()

# Weather Tool
class WeatherInfoTool(Tool):
    name = "weather_info"
    description = "Fetch weather information for a location"
    inputs = {
        "location": {"type": "string", "description": "City name"}
    }
    output_type = "string"

    def forward(self, location: str):
        weather_conditions = [
            {"condition": "Rainy", "temp": 15},
            {"condition": "Clear", "temp": 25},
            {"condition": "Windy", "temp": 20}
        ]
        data = random.choice(weather_conditions)
        return f"Weather in {location}: {data['condition']}, {data['temp']}°C"

weather_tool = WeatherInfoTool()

# Hugging Face Hub Tool
class HubStatsTool(Tool):
    name = "hub_stats"
    description = "Get most downloaded model from Hugging Face"
    inputs = {
        "author": {"type": "string", "description": "Author name"}
    }
    output_type = "string"

    def forward(self, author: str):
        try:
            models = list(list_models(author=author, sort="downloads", direction=-1, limit=1))
            if models:
                m = models[0]
                return f"Top model by {author}: {m.id} ({m.downloads} downloads)"
            return "No models found"
        except Exception as e:
            return str(e)

hub_tool = HubStatsTool()