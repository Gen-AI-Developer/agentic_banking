from agents import Agent, Runner, set_tracing_disabled, AgentHooks
from agents.extensions.models.litellm_model import LitellmModel
import os
api_key = os.getenv("GEMINI_API_KEY")  
set_tracing_disabled(disabled=True)

class MyCustomAgentHooks(AgentHooks):
    async def on_start(self, context, agent) -> None:
        print(f"AH:-> Agent: {agent.name} is started.")

    async def on_end(self, context, agent, output) -> None:
        print(f"AH:-> Agent {agent.name} has completed")

def main():
    print("Welcome to agentic-ai!")
    agent = Agent(
        name="Assistant",
        instructions="You are a helpfull assistant",
        model=LitellmModel(model="gemini/gemini-2.0-flash", api_key=api_key,),
        hooks=MyCustomAgentHooks(),
    )
    result = Runner.run_sync(agent, "what is today date?")
    print(result.final_output)
    print("Goodbye from agentic-ai!")
