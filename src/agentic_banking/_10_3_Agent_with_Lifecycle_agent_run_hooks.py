from agents import Agent, RunContextWrapper, Runner, function_tool, set_tracing_disabled, AgentHooks, RunHooks
from agents.extensions.models.litellm_model import LitellmModel
import os
api_key = os.getenv("GEMINI_API_KEY")  
set_tracing_disabled(disabled=True)

class MyCustomAgentHook(AgentHooks):
    async def on_start(self, context,agent) -> None:
        print(f"AH:-> Agent {agent.name} is starting its run.")

    async def on_end(self, context,agent,output) -> None:
        print(f"AH:->Agent {agent.name} has completed")

class MyCustomRunHook(RunHooks):
    async def on_agent_start(self,context,agent):
        print(f"RH:-> Run is started with agent: {agent.name}")

    async def on_agent_end(self,context, agent, output):
        print(f"RH:-> Run has completed with agent: {agent.name}")

def main():
    print("Welcome to AI Assistant with Lifecycle (Agent-Run) Hooks!")
    open_ai_expert_agent = Agent(
        name="Expert_OpenAI_Agents_SDK",
        instructions="You are a helpfull Open AI Agents SDK Expert Assistant, answer in a concise way.",
        model=LitellmModel(model="gemini/gemini-2.0-flash", api_key=api_key,),
        hooks=MyCustomAgentHook(),
        handoff_description="This agent is specialized in OpenAI Agents SDK related questions. If the question is not related to OpenAI Agents SDK, it will handoff to the Triage Agent.",
    )
    triage_agent = Agent(
        name="Triage Agent",
        instructions="You are a helpfull Triage Agent, you will triage the question and pass it to the appropriate agent.",
        model=LitellmModel(model="gemini/gemini-2.0-flash", api_key=api_key,),
        hooks=MyCustomAgentHook(),
        handoffs=[open_ai_expert_agent]
    )
    result = Runner.run_sync(triage_agent, "what is agent as per Open AI?",hooks=MyCustomRunHook())
    print(result.final_output)
    print("Goodbye from AI Assistant with Lifecycle (Agent-Run) Hooks!")
