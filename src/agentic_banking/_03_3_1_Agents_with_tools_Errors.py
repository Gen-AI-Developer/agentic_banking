from agents import Agent, Runner, function_tool, set_tracing_disabled, ModelSettings
from agents.extensions.models.litellm_model import LitellmModel
import os
api_key = os.getenv("GEMINI_API_KEY")  
set_tracing_disabled(disabled=True)

def handle_error(error: Exception) -> str:
    print(f"An error occurred: {error}")
    return "An error occurred while processing your request. Please try again later."

@function_tool(name_override="do_some_work_tool",failure_error_function=handle_error)
def do_some_work(data: str) -> str:
    print(f"do_some_work function with data: {data}")
    print("Processing data...")
    if not data:
        raise ValueError("No data provided to process.")
    # Simulate some processing
    if data == "error":
        raise RuntimeError("Simulated processing error.")
    return f"Processed data: {data}"

def main():
    print("Welcome to Assistant!")
    agent = Agent(
        name="Banking only Assistant",
        instructions="You are a helpfull Banking only assistant",
        model=LitellmModel(model="gemini/gemini-2.0-flash", api_key=api_key,),
        tools=[do_some_work],
        max_iterations=3,
        model_settings=ModelSettings(
            tool_choice="do_some_work"
        ),
        tool_use_behavior="stop_on_first_tool"
    )
    result = Runner.run_sync(agent, "what is Physics?")
    print(result.final_output)
    print("Goodbye from Assistant!")
