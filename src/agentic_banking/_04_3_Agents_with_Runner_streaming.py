import asyncio
from agents import Agent, Runner, function_tool, set_tracing_disabled
from agents.extensions.models.litellm_model import LitellmModel
import os
api_key = os.getenv("GEMINI_API_KEY")  
set_tracing_disabled(disabled=True)

async def main():
    print("Welcome to agentic-banking!")
    agent = Agent(
        name="Banking Assistant",
        instructions="You are a helpfull assistant, who help in customer service and banking.",
        model=LitellmModel(model="gemini/gemini-2.0-flash", api_key=api_key,),
    )
    result = Runner.run_streamed(agent, "what is Banking?")
    async for event in result.stream_events():
        print(f"\n Event {event.type}: {event}")
        if event.type == "raw_response_event":
            pass
            # print(f"\n Event name:{event.type} ==  {event.name}")
            # print(f"\n Event type:{event.type} ==   {event.type}")
            # print(f"\n Event data:{event.type} ==   {event.data}")
    print("Goodbye from agentic-banking!")

if __name__ == "__main__":
    # Run the main function using asyncio
    # This is necessary to run async functions in Python
    # It allows us to use the event loop to run our async code
    # This is a common pattern in Python for running async code
    # It is necessary to run async functions in Python   
    asyncio.run(main())