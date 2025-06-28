from agents import Agent, Runner, function_tool, set_tracing_disabled
from agents.extensions.models.litellm_model import LitellmModel
import os
api_key = os.getenv("GEMINI_API_KEY")  
set_tracing_disabled(disabled=True)

class StructureOutput:
    capital: str
    country: str

def main():
    print("Welcome to AI Assistant")
    agent = Agent(
        name="AI Assistant",
        instructions="You are a helpfull assistant",
        model=LitellmModel(model="gemini/gemini-2.0-flash", api_key=api_key,),
        output_type=StructureOutput,  # Specify the output type
    )
    result = Runner.run_sync(agent, "what is the capital of France and what country is it in?")
    print(result.final_output)
    print("Goodbye from agentic-banking!")
