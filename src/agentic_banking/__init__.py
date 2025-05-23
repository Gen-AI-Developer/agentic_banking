from agents import Agent, Runner, function_tool, set_tracing_disabled
from agents.extensions.models.litellm_model import LitellmModel
import os
api_key = os.getenv("GEMINI_API_KEY")  
set_tracing_disabled(disabled=True)

def main() -> None:
    agent = Agent(
        name="Assistant",
        instructions="You are a helpful assistant.",
        tools=[],
        model=LitellmModel(model="gemini/gemini-2.0-flash", api_key=api_key),
    )
    result = Runner.run_sync(agent, "What is the weather in New York?")
    print(result.final_output)
    print("Goodbye from agentic-banking!")
