from agents import Agent, Runner, function_tool, set_tracing_disabled
from agents.extensions.models.litellm_model import LitellmModel
import os
api_key = os.getenv("GEMINI_API_KEY")  
set_tracing_disabled(disabled=True)

context=""" Explain Banking for a 5 year old. in 3 Lines"""

def main():
    print("Welcome to Assistant with Context")
    agent = Agent(
        name="Assistant",
        instructions="You are a helpfull assistant, who help in customer service and banking.",
        model=LitellmModel(model="gemini/gemini-2.0-flash", api_key=api_key,),
    )
    result = Runner.run_sync(agent, "what is Banking?",context=context, )
    print(result.final_output)
    print("Goodbye from Assistant with context!")
