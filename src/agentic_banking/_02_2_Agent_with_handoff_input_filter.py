from agents import Agent, Runner, function_tool, set_tracing_disabled
from agents.extensions.models.litellm_model import LitellmModel
import os
api_key = os.getenv("GEMINI_API_KEY")  
set_tracing_disabled(disabled=True)
MODEL=LitellmModel(model="gemini/gemini-2.0-flash", api_key=api_key)

def main():
    print("Welcome to agentic-banking!")
    triage_agent = Agent(
        name="Triage Assistant",
        
    )
    result = Runner.run_sync(triage_agent, "what is Banking?")
    print(result.final_output)
    print("Goodbye from agentic-banking!")
