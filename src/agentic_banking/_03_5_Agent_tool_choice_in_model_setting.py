from agents import Agent, Runner, function_tool, set_tracing_disabled, ModelSettings
from agents.extensions.models.litellm_model import LitellmModel
import os
api_key = os.getenv("GEMINI_API_KEY")  
set_tracing_disabled(disabled=True)

@function_tool
def addition(a: int, b: int) -> int:
    """
    Adds two integers together.
"""
    print(f"Adding {a} and {b}")
    return a + b
@function_tool
def subtraction(a: int, b: int) -> int:
    """
    Adds two integers together.
"""
    print(f"Adding {a} and {b}")
    return a - b
def main():
    print("Welcome to agentic-banking!")
    agent = Agent(
        name="Banking Assistant",
        instructions="You are example agent you nothing do special.",
        model=LitellmModel(model="gemini/gemini-2.0-flash", api_key=api_key,),
        tools=[addition, subtraction],
        model_settings=ModelSettings(
            tool_choice="auto",  
            # Purpose: Controls how the model interacts with external tools (e.g., code interpreters, APIs).
            # Explanation:
            # Type: Literal["auto", "required", "none"] | str | None, meaning it can be one of three specific strings, another string (e.g., a specific tool name), or None.
            # Options:
            # "auto": Model decides whether to use tools.
            # "required": Forces tool use.
            # "none": Disables tool use.
            # str: Could specify a particular tool, depending on the API.
            # Default: None, likely letting the API decide.

            # For more information, see: ModelSettings.md file in the same documentation.
        )
    )
    result = Runner.run_sync(agent, "what is 2 plus 2 then - 2 ?")
    print(result.final_output)
    print("Goodbye from agentic-banking!")
