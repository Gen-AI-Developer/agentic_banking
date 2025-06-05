from agents import Agent, Runner, function_tool, set_tracing_disabled, RunContextWrapper
from agents.extensions.models.litellm_model import LitellmModel
import os
from pydantic import BaseModel
api_key = os.getenv("GEMINI_API_KEY")  
set_tracing_disabled(disabled=True)

class UserInfo(BaseModel):
    userName:str
    userAccount: str
    userAccountType:str
    userBalance:float

def get_dynamic_instruction(context: RunContextWrapper[UserInfo], agent: Agent[UserInfo]) -> str:
    return f"Welcome {context.user.userName}, your account type is {context.user.userAccountType} and your balance is {context.user.userBalance}. You can ask me about your account details or any banking related queries."
    

def main():
    userinfo = UserInfo(
        userName="Safdar Ali Shah",
        userAccount="123456789",
        userAccountType="Saving",
        userBalance=1000.0
    )

    print("Welcome to agentic-banking!")
    agent = Agent[UserInfo](
        name="Banking Assistant",
        instructions="You are a helpfull assistant, who help in customer service and banking.",
        model=LitellmModel(model="gemini/gemini-2.0-flash", api_key=api_key,),
    )
    result = Runner.run_sync(agent, "what is Banking?")
    print(result.final_output)
    print("Goodbye from agentic-banking!")
