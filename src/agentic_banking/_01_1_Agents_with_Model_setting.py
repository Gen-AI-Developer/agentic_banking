from agents import Agent, Runner, function_tool, set_tracing_disabled, ModelSettings
from agents.extensions.models.litellm_model import LitellmModel
import os

geminikey = os.getenv("GEMINI_API_KEY")  
# if geminikey:
#     print(geminikey)
set_tracing_disabled(disabled=True)

MODEL = LitellmModel(model="gemini/gemini-2.0-flash", api_key=geminikey)  # Removed the trailing comma

@function_tool
def addition(first_int: int, second_int: int) -> int:
    """
    This is addition tool
    args: first_int and second_int
    return: first_int + second_int
    """
    return first_int + second_int  # Corrected the return statement

def main():
    print("Welcome to agentic-banking!")
    agent = Agent(
        name="Assistant",
        instructions="You are a helpful assistant, You always call tools to get help, and call the tools",
        model=MODEL,
        tools=[addition],
        tool_use_behavior="run_llm_again",
        model_settings=ModelSettings(
            tool_choice="required",
            temperature=0.2,  # Lower temperature for more deterministic responses
            max_tokens=100,  # Increase max tokens for longer responses
            top_p=0.9,  # Use top-p sampling for more diverse outputs
            frequency_penalty=0.5,  # Reduce repetition
        )
    )
    result = Runner.run_sync(agent, "3+3")
    print(result.final_output)
    print("Goodbye from agentic-banking!")

if __name__ == "__main__":
    main()

'''
- **temperature=0.2**: Controls randomness. Lower value (e.g., 0.2) makes outputs more focused 
    and deterministic, prioritizing likely responses.
- **max_tokens=100**: Sets the maximum length of the response in tokens (words, subwords). 
    Higher value (e.g., 100) allows longer outputs.
- **top_p=0.9**: Enables top-p sampling. Considers the top 90% probability mass for token selection, 
    balancing diversity and coherence.
- **frequency_penalty=0.5**: Reduces repetition. Higher value (e.g., 0.5) penalizes already-used tokens,
     encouraging varied word choice.
- **presence_penalty=0.5**: Encourages new topics. Higher value (e.g., 0.5) boosts novelty by penalizing
     tokens related to prior context. This is commented out for Gemini as it does not support presence_penalty.
'''