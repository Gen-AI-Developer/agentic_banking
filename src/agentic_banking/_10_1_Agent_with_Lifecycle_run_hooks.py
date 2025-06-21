from agents import Agent, Runner, function_tool, set_tracing_disabled, RunHooks , AgentHooks
from agents.extensions.models.litellm_model import LitellmModel
import os
api_key = os.getenv("GEMINI_API_KEY")  
set_tracing_disabled(disabled=True)

class MyCustomRunHook(RunHooks):
    async def on_agent_start(self, context, agent) -> None:
        print(f"RH:-> Agent: {agent.name} is stated.")

    async def on_agent_end(self, context, agent, output) -> None:
        print(f"RH:-> Agent {agent.name} has completed")

# def on_agent_start() -> None:
#     print(f"Agent: is started.")
# def on_agent_end() -> None:
#     print(f"Agent has completed")

def main():
    print("Welcome to agentic-banking!")
    agent = Agent(
        name="Assistant",
        instructions="You are a helpfull assistant, who help customer ",
        model=LitellmModel(model="gemini/gemini-2.0-flash", api_key=api_key,),
    )
    result = Runner.run_sync(agent, "what is today date?",hooks=MyCustomRunHook())
    print(result.final_output)
    print("Goodbye from agentic-banking!")
