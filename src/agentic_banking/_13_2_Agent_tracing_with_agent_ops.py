from agents import Agent, Runner, function_tool, set_tracing_disabled
from openai.types.responses import ResponseTextDeltaEvent
from agents.extensions.models.litellm_model import LitellmModel
import os
import agentops
import asyncio
api_key = os.getenv("GEMINI_API_KEY")  
set_tracing_disabled(disabled=True)
agents_ops_api_key = os.getenv("AGENT_OPS_API_KEY")

agentops.init(api_key=agents_ops_api_key)
# agentops.monitor()
async def main():
    print("Welcome to AI")
    agent = Agent(
        name="Assistant",
        instructions="You are a helpfull assistant",
        model=LitellmModel(model="gemini/gemini-2.0-flash", api_key=api_key,),
    )
    result = Runner.run_streamed(agent, "what is today date?")
    async for event in result.stream_events:
        if event.type == "raw_response_event" and isinstance(event.data, ResponseTextDeltaEvent):
            print(event.raw_response, end="", flush=True)
        pass

    print("Goodbye from ai!")

if __name__ == "__main__":
    asyncio.run(main())