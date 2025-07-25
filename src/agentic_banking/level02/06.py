import time
from typing import Any
from agents import Agent, FunctionTool, ModelSettings, RunContextWrapper, Runner, function_tool, set_tracing_disabled
from agents.extensions.models.litellm_model import LitellmModel
import os
import asyncio
from agents import enable_verbose_stdout_logging
from agents.agent import StopAtTools
enable_verbose_stdout_logging()
from pydantic import BaseModel, ConfigDict
api_key = os.getenv("GEMINI_API_KEY")  
set_tracing_disabled(disabled=True)

modelsettings = ModelSettings(
    max_tokens=200,
    temperature=0.2,
    top_p=0.95,
    # top_k=40,
    tool_choice="none",  # No tool choice, we will use the function tool directly   

)
class FunctionArguments(BaseModel):
    name: str
    age: int
    email: str
    model_config = ConfigDict(extra="forbid")

async def do_some_work(data: str) -> str:
    print(f"do_some_work function with data: {data}")
    print("Processing data...")
    asyncio.sleep(2)  # Simulating some processing time
    return f"Tool Processed data: {data}"

async def run_function(context: RunContextWrapper[Any],args:str)-> str:
    print(f"Run_function with context: {context}, and args: {args}")
    parsed = FunctionArguments.model_validate_json(args)
    return await do_some_work(f"Username: {parsed.name}, Age: {parsed.age}, Email: {parsed.email}")

mytool = FunctionTool(
    name="user_info_tool",
    description="Process user information from the input string.",
    params_json_schema=FunctionArguments.model_json_schema(),
    on_invoke_tool=run_function,
    strict_json_schema=True,
    is_enabled=False,  # Initially disabled
)  

@function_tool
async def get_weather_updates_website(city: str) -> str:
    """
    Fetches weather updates for a given city from a website.
    """
    print(f"Fetching weather updates for {city} from the website...")
    # Simulate fetching weather updates
    await asyncio.sleep(10)
    return f"Weather updates for {city}: Sunny, 25°C"

mytool.is_enabled = True  # Enable the tool
async def main():
    home_work_agent = Agent(
        name="Homework Assistant",
        instructions="You are a helpful assistant for homework tasks.",
        model=LitellmModel(model="gemini/gemini-2.0-flash", api_key=api_key,),
        tools=[mytool, get_weather_updates_website],  # Add the tool to the
        handoff_description="You can Special Agent for Homework.",
    )
    print("Welcome to Assistant!")
    agent = Agent(
        name="Assistant",
        instructions="You are a helpfull assistant",
        model=LitellmModel(model="gemini/gemini-2.0-flash", api_key=api_key,),
        tool_use_behavior=StopAtTools(stop_at_tool_names=['user_info_tool']),
        handoffs=[home_work_agent],  # Add the homework agent as a handoff
        # tool_use_behavior="stop_on_first_tool",
        # model_settings=ModelSettings(
        #     max_tokens=200,
        #     temperature=0.2,
        #     top_p=0.95,
        #     top_k=40,
        #     tool_choice="none",
        # ),
        tools=[mytool,get_weather_updates_website],  # Add the tool to the agent
    )
    result = await Runner.run(agent, "process this user info: name John Doe, age 30, email programmersafdar@live.com, and get weather updates for city = peshawar, homework = write a short story on -why to travel around the world-",max_turns=4)
    print(result.final_output)
    print("Goodbye from Assistant!")

if __name__ == "__main__":
    asyncio.run(main())
        # Uncomment the line below to run the main function when this script is executed
    # main()
    # Note: The main function is not called automatically in this script, you can call it