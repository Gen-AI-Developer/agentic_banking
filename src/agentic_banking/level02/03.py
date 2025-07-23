import time
from typing import Any
from agents import Agent, FunctionTool, RunContextWrapper, Runner, set_tracing_disabled
from agents.extensions.models.litellm_model import LitellmModel
import os
from pydantic import BaseModel, ConfigDict
api_key = os.getenv("GEMINI_API_KEY")  
set_tracing_disabled(disabled=True)

class FunctionArguments(BaseModel):
    name: str
    age: int
    email: str
    model_config = ConfigDict(extra="forbid")

def do_some_work(data: str) -> str:
    print(f"do_some_work function with data: {data}")
    print("Processing data...")
    time.sleep(2)  # Simulating some processing time
    return f"Processed data: {data}"

async def run_function(context: RunContextWrapper[Any],args:str)-> str:
    print(f"Run_function with context: {context}, and args: {args}")
    parsed = FunctionArguments.model_validate_json(args)
    return do_some_work(f"Username: {parsed.name}, Age: {parsed.age}, Email: {parsed.email}")

mytool = FunctionTool(
    name="user_info_tool",
    description="Process user information from the input string.",
    params_json_schema=FunctionArguments.model_json_schema(),
    on_invoke_tool=run_function,
    strict_json_schema=True,
    is_enabled=False,  # Initially disabled
)   
def main():
    print("Welcome to Assistant!")
    agent = Agent(
        name="Assistant",
        instructions="You are a helpfull assistant",
        model=LitellmModel(model="gemini/gemini-2.0-flash", api_key=api_key,),
        tools=[mytool],
    )
    result = Runner.run_sync(agent, "process this user info: name John Doe, age 30, email programmersafdar@live.com")
    print(result.final_output)
    print("Goodbye from Assistant!")
