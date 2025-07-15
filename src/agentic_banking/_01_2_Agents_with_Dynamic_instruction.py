from agents import Agent, Runner, function_tool, set_tracing_disabled, RunContextWrapper
from agents.extensions.models.litellm_model import LitellmModel
import os
from pydantic import BaseModel
api_key = os.getenv("GEMINI_API_KEY")  
set_tracing_disabled(disabled=True)

class UserInfo(BaseModel):
    userName:str
    userAccountNo: str
    userAccountType:str
    userBalance:float

def get_dynamic_instruction(context: RunContextWrapper[UserInfo], agent: Agent[UserInfo]) -> str:
    "your account No. {context.context.userAccountNo} your account type is {context.context.userAccountType} and your balance is {context.context.userBalance}. You can ask me about your account details or any banking related queries."
    return f"Welcome {context.context.userName}, " \
           f"your account No. {context.context.userAccountNo}, " \
           f"your account type is {context.context.userAccountType}, " \
           f"and your balance is {context.context.userBalance}. " \
           f"You can ask me about your account details or any banking related queries."
def main():
    userinfo = UserInfo(
        userName="Safdar Ali Shah",
        userAccountNo="123456789",
        userAccountType="Saving",
        userBalance=10765490.0
    )
    print(userinfo)
    dynamicInstruction = f"Your are expert at Banking Operation, this is user data he may ask any question {userinfo}"
    print("Welcome to agentic-banking!")
    agent = Agent[UserInfo](
        name="Banking Assistant",
        instructions=userinfo,
        model=LitellmModel(model="gemini/gemini-2.0-flash", api_key=api_key,),

    )
    result = Runner.run_sync(agent, "what is my bank account Number and balance?",context=userinfo, max_turns=3  )
    print(result.final_output)
    print("Goodbye from agentic-banking!")