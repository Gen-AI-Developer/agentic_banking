from agents import Agent, Runner, WebSearchTool, function_tool, set_tracing_disabled
from agents.extensions.models.litellm_model import LitellmModel
import os

from litellm import FileSearchTool
api_key = os.getenv("GEMINI_API_KEY")  
set_tracing_disabled(disabled=True)

def main():
    print("Welcome to agentic-banking!")
    agent = Agent(
        name="Banking Assistant",
        instructions="You are a helpfull assistant, who help in customer service and banking.",
        model=LitellmModel(model="gemini/gemini-2.0-flash", api_key=api_key,),
        tools=[WebSearchTool(),FileSearchTool()],
    )
    result = Runner.run_sync(agent, "what is Banking?")
    print(result.final_output)
    print("Goodbye from agentic-banking!")
