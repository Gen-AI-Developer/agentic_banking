from agents import Agent, Runner, function_tool, set_tracing_disabled, RunConfig, ModelSettings, AgentHooks,enable_verbose_stdout_logging
from agents.extensions.models.litellm_model import LitellmModel
import os
from dataclasses import asdict

enable_verbose_stdout_logging()
from agentic_banking import printt
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

@function_tool
def biology_exper_tool(input: str) -> str:
    """
    This function is used to print answers related to biology for the user.
    """
    return " Bio means nothing and logy means not studying. So biology is not studying nothing."

def main():
    
    print("Welcome to AI Assistant!")
    special_task_agent_astool = Agent(
        name="Special Task Agent",
        instructions="You are a special task agent that can handle specific tasks.",
        model=LitellmModel(model="gemini/gemini-2.0-flash", api_key=api_key,),
        handoff_description="This agent is designed to handle special tasks.",
        )
    homework_agent = Agent(
        name="Homework Assistant",
        instructions="You are a helpful assistant for homework questions.",
        model=LitellmModel(model="gemini/gemini-2.0-flash", api_key=api_key,),
        handoff_description="This agent is designed to assist with homework tasks.",
        )
    agent = Agent(
        name="AI Assistant",
        instructions="You are a helpful assistant that can answer questions and hand off to other agents if needed.",
        model=LitellmModel(model="gemini/gemini-2.0-flash", api_key=api_key,),
        tool_use_behavior="run_llm_again",
        handoffs=[homework_agent],
        tools=[biology_exper_tool, special_task_agent_astool.as_tool(
            tool_name="special_task_agent_tool_astool", 
            tool_description="This tool handles special tasks."
        )],
        # tools=[biology_exper],
        # tool_use_behavior="run_llm_again",
        # hooks=MyCustomAgentHooks(),
        )
    # print("-------------------")
    # print(agent.tools)
    # print(agent.name)
    # print(agent.instructions)
    # print(agent.model)
    # print(agent.hooks)
    # print(agent.tool_use_behavior)
    # print(agent.handoff_description)
    # print(agent.get_all_tools())
    # print("-------------------")
    # print(agent.get_system_prompt())
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
    result = Runner.run_sync(agent, "HomeWork Task 1: write a short defination of physics?, Special Task: writw a short defination of Biology?", max_turns=2)
    # print(result.final_output)
    # printt.printt(result)
    # print(asdict(result))
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
    print(result.final_output)
    # print("Goodbye from agentic-banking!")

if __name__ == "__main__":
    main()
    # Uncomment the line below to run the main function when this script is executed
    # main()