from agents import Agent, Runner, function_tool, set_tracing_disabled,enable_verbose_stdout_logging
from agents.extensions.models.litellm_model import LitellmModel
import os
# from dataclasses import asdict
from agentic_banking.printt import printt
from agentic_banking.printt import pprint
api_key = os.getenv("GEMINI_API_KEY")  
set_tracing_disabled(disabled=True)
enable_verbose_stdout_logging()
@function_tool
def addition(a: int, b: int) -> int:
    """
    Adds two integers together.
"""
    print(f"Adding {a} and {b}")
    return a + b - 5
def main():
    print("Welcome to agentic-banking!")
    agent = Agent(
        name=True,
        instructions=12345678920,
        model=LitellmModel(model="gemini/gemini-2.0-flash", api_key=api_key,),
        tools=[addition],
        tool_use_behavior='run_llm_again'
    )
    result = Runner.run_sync(agent, "what is 2 plus 2?")
    # print(result.final_output)
    # printt(result)
    pprint(result)
    print("Goodbye from agentic-banking!")
