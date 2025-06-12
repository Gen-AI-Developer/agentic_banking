from agents import Agent, Runner, function_tool, set_tracing_disabled
from agents.extensions.models.litellm_model import LitellmModel
import os
api_key = os.getenv("GEMINI_API_KEY")  
set_tracing_disabled(disabled=True)

@function_tool(name_override="do_some_work_tool",failure_error_function=None)
def do_some_work(data: str) -> str:
    print(f"do_some_work function with data: {data}")
    print("Processing data...")
    return f"Processed data: {data}"

def main():
    print("Welcome to Assistant!")
    agent = Agent(
        name="Assistant",
        instructions="You are a helpfull assistant",
        model=LitellmModel(model="gemini/gemini-2.0-flash", api_key=api_key,),
    )
    result = Runner.run_sync(agent, "what is Banking?")
    print(result.final_output)
    print("Goodbye from Assistant!")
