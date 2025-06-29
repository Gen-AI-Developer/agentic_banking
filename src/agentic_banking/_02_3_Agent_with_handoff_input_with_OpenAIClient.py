from agents import Agent, Runner, set_tracing_disabled
import os
from agents import Agent, handoff, RunContextWrapper
from pydantic import BaseModel
from agents import (
    AsyncOpenAI,
    OpenAIChatCompletionsModel,
    RunConfig
)

gemini_api_key = os.getenv("GEMINI_API_KEY")  

if gemini_api_key:
   print("key is provided")# Debugging line to check if the key is loaded
else:
    print("GEMINI_API_KEY is not set. Please set it in your environment variables.")



#Reference: https://ai.google.dev/gemini-api/docs/openai
external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)

config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)

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
        instructions="You are a helpfull assistant, who help in customer service and banking. if you incounter any issue/problems/escalation, you can handoff to escalation agent.",
        handoffs=[handoff_obj],
    )
    result = Runner.run_sync(agent, "I was charged twice for a transaction; please resolve this issue.",run_config=config)
    print(result.final_output)
    print("Goodbye from agentic-banking!")
