from agents import Agent, RunContextWrapper, Runner, function_tool, set_tracing_disabled, RunConfig, ModelSettings, AgentHooks
from agents.extensions.models.litellm_model import LitellmModel
import os
from agents import enable_verbose_stdout_logging,handoff
from dataclasses import asdict
from agents import Agent, handoff
from agents.extensions import handoff_filters
enable_verbose_stdout_logging()
from agentic_banking import printt
api_key = os.getenv("GEMINI_API_KEY")  
set_tracing_disabled(disabled=True)

# class MyCustomAgentHooks(AgentHooks):
#     async def on_start(self, context, agent) -> None:
#         print(f"AH:-> Agent: {agent.name} is started.")

#     async def on_end(self, context, agent, output) -> None:
#         print(f"AH:-> Agent {agent.name} has completed")
    
#     async def on_tool_start(self, context, agent, tool):
#         if (tool.name == "biology_exper"):
#             print(f"AH:-> {agent.name} called a tool with context {context.context} Tool {tool.name} is starting with input: {context.context}")
#         return await super().on_tool_start(context, agent, tool)
    
#     async def on_tool_end(self, context, agent, tool, result):
#         print(f"AH:-> {agent.name} called a Tool {tool.name} has completed with result: {result}")
#         return await super().on_tool_end(context, agent, tool, result)

# @function_tool
# def biology_exper(input: str) -> str:
#     """
#     This function is used to print answers related to biology for the user.
#     """
#     return " Bio means nothing and logy means not studying. So biology is not studying nothing."

def custom_on_handoff_(context: RunContextWrapper[None], agent: Agent) ->RunContextWrapper[None]:
    return f"Custom handoff logic executed for agent: {agent.name} with context: {context.context}"

note_agent = Agent(
    name="Note Taking Agent",
    instructions="You are a helpful note-making assistant. You can make notes on various topics.",
    model=LitellmModel(model="gemini/gemini-2.0-flash", api_key=api_key,),
)
custom_handoff = handoff(
    agent=note_agent,
    tool_name_override="Custom Handoff/Note Tool",
    on_handoff= custom_on_handoff_,
    input_filter=handoff_filters.remove_all_tools,
    tool_description_override="This is a custom handoff tool that allows the agent to make notes on various topics.",
)




@function_tool
def historyTools(input: str) -> str:
    """
    This function is used to print answers related to history for the user.
    """
    return "History is the study of past events, particularly in human affairs."
def main():
    print("Welcome to AI Assistant!")
    math_agent = Agent(
        name="Math Assistant",
        instructions="You are a helpful Math assistant",
        model=LitellmModel(model="gemini/gemini-2.0-flash", api_key=api_key,),

    )
    english_grammer_agent = Agent(
        name="English Grammar Assistant",
        instructions="You are a helpful English Grammar assistant",
        model=LitellmModel(model="gemini/gemini-2.0-flash", api_key=api_key,),
    )
    biology_agent = Agent(
        name="Biology Assistant",
        instructions="You are a helpful Biology assistant",
        model=LitellmModel(model="gemini/gemini-2.0-flash", api_key=api_key,),
    )
    Triage_agent = Agent(
        name="AI Assistant",
        instructions="You are a helpful assistant",
        model=LitellmModel(model="gemini/gemini-2.0-flash", api_key=api_key,),
        tools=[historyTools],
        model_settings=ModelSettings(
            tool_choice="required",
        ),
        handoffs=[biology_agent, math_agent, english_grammer_agent,custom_on_handoff_],
        tool_use_behavior="stop_on_first_tool",

        )
    
    result = Runner.run_sync(Triage_agent, "write notes on Chernobyl Nuclear Desaster?", max_turns=2)
    print(result.final_output)

if __name__ == "__main__":
    main()