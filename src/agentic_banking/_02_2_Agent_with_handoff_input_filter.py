from agents import Agent, Handoff, Runner, function_tool, set_tracing_disabled
from agents import handoff,handoffs, RunContextWrapper
from agents.extensions.models.litellm_model import LitellmModel
import os

from pydantic import BaseModel
api_key = os.getenv("GEMINI_API_KEY")  
set_tracing_disabled(disabled=True)
MODEL=LitellmModel(model="gemini/gemini-2.0-flash", api_key=api_key)

class UserLoginInfo(BaseModel):
    isUserLoggedin : bool = False

def summary_of_provided_context(context: RunContextWrapper[UserLoginInfo], agent:Agent):
    return f"This is context provided by is_enabled {context.context} with agent.name: {agent.name}"
    pass
def main():
    currentUser = UserLoginInfo(isUserLoggedin=True)
    print("Welcome to agentic-banking!")
    banking_agent = Agent(
        name="Banking Assistant",
        model=MODEL,
    )
    sport_agent = Agent(        
        name="Sport Assistant",
        
        model=MODEL,
    )
    triage_agent = Agent(
        name="Triage Assistant",
        model=MODEL,
        handoffs=[
            handoff(
                agent = banking_agent,
                tool_name_override="BankingAssistant",
                tool_description_override="Provides assistance with banking-related queries.",
                # is_enabled=True
                # input_filter=lambda input: "banking" in input.lower() or "finance" in input.lower()
            ),
            handoff(
                agent = sport_agent,
                tool_name_override="SportAssistant",
                tool_description_override="Provides assistance with sports-related queries.",
                # is_enabled=True
            )
        ]
    )
    result = Runner.run_sync(triage_agent, "what is Banking?",context=currentUser)
    print(result.final_output)
    print("Goodbye from agentic-banking!")
