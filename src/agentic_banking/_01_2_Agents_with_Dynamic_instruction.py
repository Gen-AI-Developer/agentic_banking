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
    return f"Welcome {context.context.userName}, your account type is {context.context.userAccountType} and your balance is {context.context.userBalance}. You can ask me about your account details or any banking related queries."
@function_tool
def get_user_info(context: RunContextWrapper[UserInfo], agent: Agent[UserInfo]) -> str:
    return f"User Name: {context.context.userName}, Account Type: {context.context.userAccountType}, Balance: {context.context.userBalance}"  

def main():
    userinfo = UserInfo(
        userName="Safdar Ali Shah",
        userAccount="123456789",
        userAccountType="Saving",
        userBalance=10765490.0
    )

    print("Welcome to agentic-banking!")
    agent = Agent[UserInfo](
        name="Banking Assistant",
        instructions=get_dynamic_instruction,
        model=LitellmModel(model="gemini/gemini-2.0-flash", api_key=api_key,),
        context=userinfo,
    )
    result = Runner.run_sync(agent, "what is Banking?")
    print(result.final_output)
    print("Goodbye from agentic-banking!")