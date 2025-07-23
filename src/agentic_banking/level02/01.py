from agents import Agent, RunContextWrapper, Runner, function_tool, set_tracing_disabled, RunConfig, ModelSettings, AgentHooks
from agents.extensions.models.litellm_model import LitellmModel
import os
from agents import enable_verbose_stdout_logging, handoff
from dataclasses import asdict
from agents import Agent, handoff
from agents.extensions import handoff_filters
enable_verbose_stdout_logging()
from agentic_banking import printt

api_key = os.getenv("GEMINI_API_KEY")  
set_tracing_disabled(disabled=True)

def custom_on_handoff(context: RunContextWrapper[None]) -> str:
    return f"Custom handoff logic executed for agent: {context.agent.name} with context: {context.context}"

note_agent = Agent(
    name="Note Taking Agent",
    instructions="You are a helpful note-making assistant. You can make notes on various topics.",
    model=LitellmModel(model="gemini/gemini-2.0-flash", api_key=api_key),
)

custom_handoff = handoff(
    agent=note_agent,
    tool_name_override="custom_handoff_note_tool",  # Updated to a valid function name
    on_handoff=custom_on_handoff,
    input_filter=handoff_filters.remove_all_tools,
    tool_description_override="This is a custom handoff tool that allows the agent to make notes on various topics.",
)

@function_tool
def historytools(input: str) -> str:
    """
    This function is used to print answers related to history for the user.
    """
    return "History is the study of past events, particularly in human affairs."

def main():
    print("Welcome to AI Assistant!")
    math_agent = Agent(
        name="Math Assistant",
        instructions="You are a helpful Math assistant",
        model=LitellmModel(model="gemini/gemini-2.0-flash", api_key=api_key),
    )
    english_grammer_agent = Agent(
        name="English Grammar Assistant",
        instructions="You are a helpful English Grammar assistant",
        model=LitellmModel(model="gemini/gemini-2.0-flash", api_key=api_key),
    )
    biology_agent = Agent(
        name="Biology Assistant",
        instructions="You are a helpful Biology assistant",
        model=LitellmModel(model="gemini/gemini-2.0-flash", api_key=api_key),
    )
    Triage_agent = Agent(
        name="AI Assistant",
        instructions="You are a helpful assistant",
        model=LitellmModel(model="gemini/gemini-2.0-flash", api_key=api_key),
        tools=[historytools],
        model_settings=ModelSettings(
            tool_choice="required",
        ),
        handoffs=[biology_agent, math_agent, english_grammer_agent, custom_handoff],
        tool_use_behavior="stop_on_first_tool",
    )
    
    result = Runner.run_sync(Triage_agent, "write notes on Chernobyl Nuclear Disaster?", max_turns=2)
    print(result.final_output)

if __name__ == "__main__":
    main()