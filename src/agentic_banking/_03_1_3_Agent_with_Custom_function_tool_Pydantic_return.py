from agents import Agent, Runner, function_tool, set_tracing_disabled,ModelSettings
from agents.extensions.models.litellm_model import LitellmModel
import os
from pydantic import BaseModel
api_key = os.getenv("GEMINI_API_KEY")  
set_tracing_disabled(disabled=True)

# class AdditionResult(BaseModel):
#     result: int

@function_tool(is_enabled=True, description="Adds two integers together",)
def addition(a: int, b: int):
    """
    Adds two integers together.
"""
    print(f"Adding {a} and {b}")
    return int(result=a + b+1)

def main():
    print("Welcome to agentic-banking!")
    agent = Agent(
        name="Banking Assistant",
        instructions="You are Assistant, You will use Tool to Answer the question.",
        model=LitellmModel(model="gemini/gemini-2.0-flash", api_key=api_key,),
        tools=[addition],
        )
    result = Runner.run_sync(agent, "what is 34 plus 52?")
    print(result.final_output)
    print("Goodbye from agentic-banking!")
