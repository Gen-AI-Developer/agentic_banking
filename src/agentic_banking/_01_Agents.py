from agents import Agent, Runner, function_tool, set_tracing_disabled, RunConfig, ModelSettings, AgentHooks
from agents.extensions.models.litellm_model import LitellmModel
import os
api_key = os.getenv("GEMINI_API_KEY")  
set_tracing_disabled(disabled=True)

# modelsetting = ModelSettings(
#     tool_choice="auto",
# )
# myconfig = RunConfig(
#     model_settings=modelsetting,
# )


# input_list = [
#     {"role": "user",
#     "content": "What is Asyncio?"},
#     {"role": "user",
#     "content": "What is Physics",}
# ]

class MyCustomAgentHooks(AgentHooks):
    async def on_start(self, context, agent) -> None:
        print(f"AH:-> Agent: {agent.name} is started.")

    async def on_end(self, context, agent, output) -> None:
        print(f"AH:-> Agent {agent.name} has completed")
    
    async def on_tool_start(self, context, agent, tool):
        return await super().on_tool_start(context, agent, tool)
    
    async def on_tool_end(self, context, agent, tool, result):
        print(f"AH:-> Tool {tool.name} has completed with result: {result}")
        return await super().on_tool_end(context, agent, tool, result)

@function_tool
def biology_exper(input: str) -> str:
    """
    This function is used to print answers related to biology for the user.
    """
    return " Bio means nothing and logy means not studying. So biology is not studying nothing."

def main():
    print("Welcome to AI Assistant!")
    agent = Agent(
        name="AI Assistant",
        instructions="You are a helpful assistant",
        model=LitellmModel(model="gemini/gemini-2.0-flash", api_key=api_key,),
        tools=[biology_exper],
        tool_use_behavior="run_llm_again",
        hooks=MyCustomAgentHooks(),
        )
    print(agent.tools)
    # ai_expert_agent : Agent = Agent(
    #     name="ai Assistant",
    #     model=LitellmModel(model="gemini/gemini-2.0-flash", api_key=api_key,),
    #     handoff_description="AI Expert Agent",
    # )
    # physics_expert_agent : Agent = Agent(
    #     name="physic Assistant",
    #     model=LitellmModel(model="gemini/gemini-2.0-flash", api_key=api_key,),
    #     handoff_description="Physics Expert Agent",
    # )
    # triage_agent : Agent = Agent(
    #     name="Triage Agent",
    #     tools=[biology_exper],
    #     tool_use_behavior="run_llm_again",
    #     instructions="You are a triage agent that decides which expert agent to hand off the question to also print the name of agent.",
    #     model=LitellmModel(model="gemini/gemini-2.0-flash", api_key=api_key,),
    #     handoffs=[ai_expert_agent, physics_expert_agent],
    # )
# max_turns=2, run_config=myconfig
    result = Runner.run_sync(agent, "what is biology?", )
    print(result.final_output)

    pass
    # print("Welcome to agentic-banking!")
    # """
    # This is a simple example of how to use the Agentic Banking framework.
    # It creates an agent that can answer questions about banking.
    # """
    # agent = Agent(
    #     name="Banking Assistant",
    #     instructions="You are a helpfull assistant, who help in customer service and banking.",
    #     model=LitellmModel(model="gemini/gemini-2.0-flash", api_key=api_key,),
    # )
    # result = Runner.run_sync(agent, "Banking?", max_turns=1,run_config=myconfig)
    # print(result.final_output)
    # print("Goodbye from agentic-banking!")
