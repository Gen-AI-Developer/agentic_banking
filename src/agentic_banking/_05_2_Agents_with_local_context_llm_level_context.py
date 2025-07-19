from agents import Agent, RunContextWrapper, Runner, function_tool, set_tracing_disabled, AgentHooks, RunHooks
from agents.extensions.models.litellm_model import LitellmModel
from pydantic import BaseModel
import os
import asyncio
api_key = os.getenv("GEMINI_API_KEY")  
set_tracing_disabled(disabled=True)

class UserInfo(BaseModel):
    name: str
    age: int

class CustomeRunHooks(RunHooks):
    def on_agent_start(self, context:RunContextWrapper[UserInfo]):
        print(f"RunHOok : Run started: {context.context.name}")

    def on_agent_end(self, run):
        print(f"Run ended: {run.id}")

class CustomeAgentHooks(AgentHooks):
    def on_start(self,context: RunContextWrapper[UserInfo], agent):
        print(f"AgentHOoK: Agent started: {agent.name} + {context.context.name}")

    def on_end(self, agent):
        print(f"Agent ended: {agent.name}")




def main():
    userinfor = UserInfo(name="John Doe", age=30)
    print("Welcome to agentic-banking!")
    agent = Agent[UserInfo](
        name="Banking Assistant",
        instructions="You are a helpful assistant",
        model=LitellmModel(model="gemini/gemini-2.0-flash", api_key=api_key,),
        hooks=CustomeAgentHooks(),
    )
    result = Runner.run_sync(agent, "what is the name of the user?", context=userinfor)
    print(f"Result of First Agent: {result.final_output}")

    agent2 = Agent(
        name="Banking Assistant",
        instructions="You are a helpful assistant",
        model=LitellmModel(model="gemini/gemini-2.0-flash", api_key=api_key,),
    )
    result2 = Runner.run_sync(agent2, "what is the name of the user?", context=userinfor, hooks=CustomeRunHooks())
    print(result2.final_output)
    print("Goodbye from agentic-banking!")

if __name__ == "__main__":
    main()