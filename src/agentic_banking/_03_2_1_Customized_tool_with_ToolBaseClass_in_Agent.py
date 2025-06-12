from typing import Any
from agents import Agent, RunContextWrapper, Runner, function_tool, set_tracing_disabled
from agents.extensions.models.litellm_model import LitellmModel
import os
from pydantic import BaseModel
api_key = os.getenv("GEMINI_API_KEY")  
set_tracing_disabled(disabled=True)

class FunctionArguments(BaseModel):
    name: str
    age: int
    email: str
def do_some_work(data: str) -> str:
    return {"Status":"done", "data": data}

async def run_function(context: RunContextWrapper[Any],args:str)-> str:
    parsed = FunctionArguments.model_validate_json(args)
    return do_some_work(f"Username: {parsed.name}, Age: {parsed.age}, Email: {parsed.email}")
    

def main():
    print("Welcome to agentic-banking!")
    agent = Agent(
        name="Banking Assistant",
        instructions="You are a helpfull assistant, who help in customer service and banking.",
        model=LitellmModel(model="gemini/gemini-2.0-flash", api_key=api_key,),
    )
    result = Runner.run_sync(agent, "what is Banking?")
    print(result.final_output)
    print("Goodbye from agentic-banking!")
