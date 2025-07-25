import pprint
from agents import Agent, Runner, function_tool, set_tracing_disabled, RunContextWrapper, enable_verbose_stdout_logging, ModelSettings
from agents.extensions.models.litellm_model import LitellmModel
import os
from pydantic import BaseModel
from . import printt
api_key = os.getenv("GEMINI_API_KEY")  
set_tracing_disabled(disabled=True)
set
enable_verbose_stdout_logging()
class UserInfo(BaseModel):
    userName:str
    userAccountNo: str
    userAccountType:str
    userBalance:float
@function_tool
def get_user_info(context: RunContextWrapper[UserInfo],) -> UserInfo:
    """This function retrieves user information from the context.
    It returns the user information as a UserInfo object."""
    return context.context

def get_dynamic_instruction(context: RunContextWrapper[UserInfo], agent: Agent[UserInfo]) -> str:
    "your account No. {context.context.userAccountNo} your account type is {context.context.userAccountType} and your balance is {context.context.userBalance}. You can ask me about your account details or any banking related queries."
    return f"Welcome {context.context.userName}, " \
           f"your account No. {context.context.userAccountNo}, " \
           f"your account type is {context.context.userAccountType}, " \
           f"and your balance is {context.context.userBalance}. " \
           f"You can ask me about your account details or any banking related queries."
def main():
    userinfo = UserInfo(
        userName="alex",
        userAccountNo="123456789",
        userAccountType="Saving",
        userBalance=10765490.0
    )
    # print(userinfo)
    # dynamicInstruction = f"Your are expert at Banking Operation, this is user data he may ask any question {userinfo}"
    print("Welcome to agentic-banking!")
    agent = Agent[UserInfo](
        name="Banking Assistant",
        instructions=get_dynamic_instruction,
        tools=[get_user_info],
        tool_use_behavior='run_all_tools',  # Change to 'run_all_tools' to allow multiple tool calls
        # tool_use_behavior='stop_on_first_tool',
        model=LitellmModel(model="gemini/gemini-2.0-flash", api_key=api_key,),
        model_settings=ModelSettings(
            tool_choice="required",
        )

    )
    result = Runner.run_sync(agent, f"what is my bank account Number and balance?", context=userinfo, max_turns=3  )
    print(result.final_output)
    print("----------------------------------------------")
    # printt.printt(result)
    # pprint.pprint(result)
    print("Goodbye from agentic-banking!")