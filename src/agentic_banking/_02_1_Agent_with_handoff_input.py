from agents import Agent, Runner, set_tracing_disabled
from agents.extensions.models.litellm_model import LitellmModel
import os
from agents import Agent, handoff, RunContextWrapper
gemini_api_key = os.getenv("GEMINI_API_KEY")  
if gemini_api_key:
   print("key is provided")# Debugging line to check if the key is loaded
else:
    print("GEMINI_API_KEY is not set. Please set it in your environment variables.")
set_tracing_disabled(disabled=True)
from pydantic import BaseModel

class EscalationData(BaseModel):
    reason: str

async def on_handoff(ctx: RunContextWrapper[None], input_data: EscalationData):
    print(f"Escalation agent called with reason: {input_data.reason}")

agent = Agent(name="Escalation agent")

handoff_obj = handoff(
    agent=agent,
    on_handoff=on_handoff,
    input_type=EscalationData,
)
def main():
    print("Welcome to agentic-banking!")
    agent = Agent(
        name="Banking Assistant",
        instructions="You are a helpfull assistant, who help in customer service and banking.",
        model=LitellmModel(model="gemini/gemini-2.0-flash", api_key=gemini_api_key ,),
        handoffs=[handoff_obj],
    )
    result = Runner.run_sync(agent, "I was charged twice for a transaction; please resolve this issue.")
    print(result.final_output)
    print("Goodbye from agentic-banking!")
