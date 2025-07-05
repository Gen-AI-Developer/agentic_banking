from agents import Agent, ModelSettings, Runner, function_tool, set_default_openai_api, set_default_openai_client, set_tracing_disabled
from agents.extensions.models.litellm_model import LitellmModel
import os
from openai import AsyncOpenAI
from pydantic import BaseModel
api_key = os.getenv("GEMINI_API_KEY")  
set_tracing_disabled(disabled=True)

BASE_URL = os.getenv("BASE_URL") or "https://generativelanguage.googleapis.com/v1beta/openai/"
API_KEY = os.getenv("GEMINI_API_KEY") #or userdata.get("GEMINI_API_KEY")
MODEL_NAME = os.getenv("MODEL_NAME") or "gemini-2.0-flash"


if not BASE_URL or not API_KEY or not MODEL_NAME:
    raise ValueError("Please set BASE_URL, GEMINI_API_KEY, MODEL_NAME via env var or code.")

# Create OpenAI client
client = AsyncOpenAI(
    base_url=BASE_URL,
    api_key=API_KEY,
)

# Configure the client
set_default_openai_client(client=client, use_for_tracing=True)
set_default_openai_api("chat_completions")


class StructureOutput(BaseModel):
    capital: str = None
    country: str = None
    weather: str = None

class CustomOutput(BaseModel):
    output: str = None

@function_tool
def get_capital_and_country(country: str) -> StructureOutput:
    """Function to get the capital and country information.
    Returns a StructureOutput with capital, and country."""
    if country.lower() == "france":
        return StructureOutput(capital="Paris", country="France")
    elif country.lower() == "germany":
        return StructureOutput(capital="Berlin", country="Germany")
    else:
        return StructureOutput(capital="Unknown", country=country)
@function_tool
def get_weather(city: str) -> str:
    """Function to get the weather for a given city."""
    if city.lower() == "paris":
        return "Sunny"
    elif city.lower() == "berlin":
        return "Cloudy"
    else:
        return "Weather data not available"

def main():
    print("Welcome to AI Assistant")
    agent = Agent(
        name="AI Assistant",
        instructions="You are a helpfull assistant",
        # model=LitellmModel(model="gemini/gemini-2.0-flash", api_key=api_key,),
        model =MODEL_NAME,
        output_type=CustomOutput,  # Specify the output type
        tools=[get_capital_and_country,get_weather], # Register the function tool
        tool_use_behavior="run_llm_again",
        model_settings=ModelSettings(
            tool_choice="required",
            # parallel_tool_calls=True,
        )
    )
    result = Runner.run_sync(agent, "what is the capital of France and what country is it in?")
    print(result.final_output)
    print("Goodbye from AI Assistant!")
