from agents import Agent, Runner, function_tool, set_tracing_disabled
from agents.extensions.models.litellm_model import LitellmModel
import os
api_key = os.getenv("GEMINI_API_KEY")  
set_tracing_disabled(disabled=True)

def main():
    print("Welcome to agentic-banking!")
    tool_agent = Agent(
        name="Cooking Assistant",
        instructions="You are a helpful assistant, who helps in cooking and recipes.",
        model=LitellmModel(model="gemini/gemini-2.0-flash", api_key=api_key,),
    )
    agent = Agent(
        name="Assistant",
        instructions="You are a helpfull assistant, who help everyone in any way you can.",
        model=LitellmModel(model="gemini/gemini-2.0-flash", api_key=api_key,),
        tools=[tool_agent.as_tool(
            tool_name="Cooking Assistant",
            tool_description="A helpful assistant for cooking and recipes."
        )]
    )
    result = Runner.run_sync(agent, "how to cook chiken roast?")
    print(result.final_output)
    print("Goodbye from agentic-banking!")
