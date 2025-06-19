from agents import Agent, Runner, function_tool, set_tracing_disabled
from agents.extensions.models.litellm_model import LitellmModel
import os
api_key = os.getenv("GEMINI_API_KEY")  
set_tracing_disabled(disabled=True)

def main():
    print("Welcome to agentic-banking!")
    agent = Agent(
        name="Assistant",
        instructions="You are a Master of Creating Jokes out of programming.",
        tools=[],
        model=LitellmModel(model="gemini/gemini-2.0-flash", api_key=api_key,),
        model_settings={}
    )
    result = Runner.run_sync(agent, "What is the best joke on java and C#?")
    print(result.final_output)
    print("Goodbye from agentic-banking!")
