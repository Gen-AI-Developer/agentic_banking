from agents import Agent, Runner, function_tool, set_tracing_disabled
from agents.extensions.models.litellm_model import LitellmModel
import os
api_key = os.getenv("GEMINI_API_KEY")  
set_tracing_disabled(disabled=True)

def main():
    print("Welcome to AI Assistant with Lifecycle (Agent-Run) Hooks!")
    open_ai_expert_agent = Agent(
        name="Expert_OpenAI_Agents_SDK",
        instructions="You are a helpfull Open AI Agents SDK Expert Assistant, answer in a concise way.",
        model=LitellmModel(model="gemini/gemini-2.0-flash", api_key=api_key,),
        handoff_description="This agent is specialized in OpenAI Agents SDK related questions. If the question is not related to OpenAI Agents SDK, it will handoff to the Triage Agent.",
    )
    Triage_agent = Agent(
        name="Triage Agent",
        instructions="You are a helpfull Triage Agent, you will triage the question and pass it to the appropriate agent.",
        model=LitellmModel(model="gemini/gemini-2.0-flash", api_key=api_key,),
        handoff=[open_ai_expert_agent]
    )
    result = Runner.run_sync(Triage_agent, "what is agent as per Open AI?")
    print(result.final_output)
    print("Goodbye from AI Assistant with Lifecycle (Agent-Run) Hooks!")
