from agents import Agent, ModelSettings, Runner, function_tool, set_tracing_disabled
from agents.extensions.models.litellm_model import LitellmModel
import os
api_key = os.getenv("GEMINI_API_KEY")  
set_tracing_disabled(disabled=True)
mode_setting = ModelSettings(
    # tool_choice="required",
    # tool_choice="customizedToolForAnyJob"
)

@function_tool
def customizedToolForAnyJob():
    """ this sample tool function which will perform any job"""
    pass

def main():
    print("Welcome to agentic-banking!")
    agent = Agent(
        name="Banking Assistant",
        instructions="You are a helpfull assistant, who help in customer service and banking.",
        model=LitellmModel(model="gemini/gemini-2.0-flash", api_key=api_key,),
        model_settings=ModelSettings(
        #    tool_choice="required",  # This forces the agent to use tools
             tool_choice="customizedToolForAnyJob"
        ),
    )
    result = Runner.run_sync(agent, "what is Banking?",)
    print(result.final_output)
    print("Goodbye from agentic-banking!")
