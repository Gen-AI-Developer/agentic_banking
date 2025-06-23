from agents import Agent, Runner, function_tool, set_tracing_disabled
from agents.extensions.models.litellm_model import LitellmModel
import os
from pydantic import BaseModel
api_key = os.getenv("GEMINI_API_KEY")  
set_tracing_disabled(disabled=True)

class AdditionResult(BaseModel):
    result: int

@function_tool
def addition(a: int, b: int) -> AdditionResult:
    """
    Adds two integers together.
"""
    print(f"Adding {a} and {b}")
    return AdditionResult(result=a + b)

def main():
    print("Welcome to agentic-banking!")
    agent = Agent(
        name="Banking Assistant",
        instructions="You are example agent you nothing do special.",
        model=LitellmModel(model="gemini/gemini-2.0-flash", api_key=api_key,),
        tools=[addition],
        # tool_use_behavior='stop_on_first_tool'
    )
    result = Runner.run_sync(agent, "what is 2 plus 2?")
    print(result.final_output)
    print("Goodbye from agentic-banking!")
