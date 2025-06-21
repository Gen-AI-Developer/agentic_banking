from agents import Agent, Runner, function_tool, set_tracing_disabled, RunConfig, ModelSettings
from agents.extensions.models.litellm_model import LitellmModel
import os
api_key = os.getenv("GEMINI_API_KEY")  
set_tracing_disabled(disabled=True)

modelsetting = ModelSettings(
    max_tokens=100,
    temperature=0.5,
    top_p=0.9,
)
myconfig = RunConfig(
    model_settings=modelsetting,
)
def main():
    print("Welcome to agentic-banking!")
    """
    This is a simple example of how to use the Agentic Banking framework.
    It creates an agent that can answer questions about banking.
    """
    agent = Agent(
        name="Banking Assistant",
        instructions="You are a helpfull assistant, who help in customer service and banking.",
        model=LitellmModel(model="gemini/gemini-2.0-flash", api_key=api_key,),
    )
    result = Runner.run_sync(agent, "Banking?", max_turns=1,run_config=myconfig)
    print(result.final_output)
    print("Goodbye from agentic-banking!")
