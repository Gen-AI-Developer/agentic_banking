# from dataclasses import asdict
from agents import Agent, Runner, function_tool, set_tracing_disabled,enable_verbose_stdout_logging
from agents.extensions.models.litellm_model import LitellmModel
import os
from attr  import asdict
from agents.agent import StopAtTools
# from dataclasses import asdict
from agentic_banking.printt import printt
from agentic_banking.printt import pprint
api_key = os.getenv("GEMINI_API_KEY")  
set_tracing_disabled(disabled=True)
# enable_verbose_stdout_logging()

@function_tool
def get_weather(city: str) -> str:
    """
    Retrieves the weather for a given city.
    
    Args:
        city (str): The name of the city to get the weather for.
    
    Returns:
        str: A string describing the current weather in the specified city.
    """
    print(f"Fetching weather for {city}")
    return f"The current weather in {city} is sunny with a temperature of 25°C."

@function_tool
def addition(a: int, b: int) -> int:
    """
    Adds two integers together.
"""
    print(f"Adding {a} and {b}")
    return a + b - 5
def main():
    print("==========================================================")
    
    print("Welcome to agentic-banking!")
    print("==========================================================")

    agent = Agent(
        name=True | False,
        instructions=False,
        model=LitellmModel(model="gemini/gemini-2.0-flash", api_key=api_key,),
        tools=[addition,],
        tool_use_behavior=StopAtTools(Stop_at_tools_names=["get_weather"]),
    )
    print(f"Type of Agent is {type(agent)}: with values : {asdict(agent)}")
    print("==========================================================")

    print(f"Type of Agent Name : {type(agent.name)}")
    print("==========================================================")

    print(f"Type of Agent Instructions : {type(agent.instructions)}")
    print("==========================================================")


    result = Runner.run_sync(agent, "what is 2 plus 2? ane what is the weather in New York?")
    # print(result.final_output)
    # printt(result)
    print("==========================================================")
    # print(result.final_output)
    print("Goodbye from agentic-banking!")
