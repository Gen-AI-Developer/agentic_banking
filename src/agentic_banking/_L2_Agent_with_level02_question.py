import asyncio
from agents import Agent, Runner, set_tracing_disabled
from agents.extensions.models.litellm_model import LitellmModel
import os
from agents import Agent, handoff, RunContextWrapper
from pydantic import BaseModel
from agents.run import Runner

gemini_api_key = os.getenv("GEMINI_API_KEY")  
if gemini_api_key:
   print("key is provided")# Debugging line to check if the key is loaded
else:
    print("GEMINI_API_KEY is not set. Please set it in your environment variables.")
set_tracing_disabled(disabled=True)


async def main():
    print("================================")
    agent = Agent(
        name="Assistant",
        model=LitellmModel(model="gemini/gemini-2.0-flash", api_key=gemini_api_key),
    )
    runner = Runner()
    result = await runner.run(agent_name=agent, input="write an article on System Engineering for Absolute Beginners")
    print(result.final_output)
    print("================================")


if __name__ == "__main__":
    asyncio.run(main())