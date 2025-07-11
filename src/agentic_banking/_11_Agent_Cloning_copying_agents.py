from agents import Agent, ModelSettings, Runner, function_tool, set_tracing_disabled
from agents.extensions.models.litellm_model import LitellmModel
import os
api_key = os.getenv("GEMINI_API_KEY")  
set_tracing_disabled(disabled=True)

@function_tool
async def weather_tool(city: str)-> str:
    return f"Weather at {city} is sunny"
def main():
    print("Welcome to agentic-banking!")
    weather_agent = Agent(
        name="Weather Assistant",
        instructions="You are a helpfull weather assistant",
        model=LitellmModel(model="gemini/gemini-2.0-flash", api_key=api_key,),
        tools=[weather_tool],
        model_settings=ModelSettings(
            temperature=0.8
        )
        # tool_use_behavior="stop_on_first_tool"
    )
    robot_agent = weather_agent.clone(
        name="Robot Assistant",
        instructions="You are a robot assistant",
        model=LitellmModel(model="gemini/gemini-2.0-flash", api_key=api_key,),
        # tool_use_behavior="stop_on_first_tool"   
    )
    robot_agent = weather_agent.clone(
        name="Assistant",
        instructions="You are a assistant",
        model=LitellmModel(model="gemini/gemini-2.0-flash", api_key=api_key,),
        # tool_use_behavior="stop_on_first_tool"   
    )

    result = Runner.run_sync(robot_agent, "whats the weather condition in New york city?")
    print(result.final_output)
    print(result.last_agent.name)
    print("Goodbye from agentic-banking!")
