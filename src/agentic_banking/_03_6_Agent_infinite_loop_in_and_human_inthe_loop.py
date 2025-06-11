from agents import Agent, Runner, function_tool, set_tracing_disabled, ModelSettings
from agents.extensions.models.litellm_model import LitellmModel
import os,time
api_key = os.getenv("GEMINI_API_KEY")  
set_tracing_disabled(disabled=True)

@function_tool
def human_in_the_loop(input_text: str) -> str:
    """
    This function simulates a human in the loop
    """
    print(f"Human in the loop: {input_text}")
    return "Human response to: " + input_text

def main():
    print("Welcome to Human in the Loop Example")
    time.sleep(1)
    print("This example shows how to use an agent with a human in the loop.")
    time.sleep(1)
    print("The agent will call the human in the loop function with a text input.")
    time.sleep(1)
    print("It will then return the response from the human in the loop function.")
    time.sleep(1)
    print("This is an infinite loop example, so it will keep running until you stop it.")
    time.sleep(1)
    agent = Agent(
        name="Banking Assistant",
        instructions="You are example agent you nothing do special.",
        model=LitellmModel(model="gemini/gemini-2.0-flash", api_key=api_key,),
        tools=[human_in_the_loop],
        model_settings=ModelSettings(
            tool_choice="required",  
        ),
        reset_tool_choice=False,
    )
    result = Runner.run_sync(agent, "hello, i need to call human_in_the_loop with this text 'hello world'",max_turns=3)
    print("Agent finished running.") 
    print(result.final_output)
    print("Goodbye from agentic-banking!")
