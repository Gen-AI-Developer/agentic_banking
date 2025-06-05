from agents import Agent, Runner, function_tool, set_tracing_disabled
from agents.extensions.models.litellm_model import LitellmModel
import os
from pydantic import BaseModel
api_key = os.getenv("GEMINI_API_KEY")  
set_tracing_disabled(disabled=True)
MODEL=LitellmModel(model="gemini/gemini-2.0-flash", api_key=api_key,)

class UserInfo(BaseModel):
    userName: str
    userAccountNo: str
    userAccountType: str
    userBalance: float
def get_dynamic_instruction(context: UserInfo, agent: Agent[UserInfo]) -> str:
    return f"Welcome {context.userName}, your account No. {context.userAccountNo}, your account type is {context.userAccountType}, and your balance is {context.userBalance}. You can ask me about your account details or any banking related queries."

def main():
    print("Welcome to Triage Agent!")
    userinfo = UserInfo(
        userName="Safdar Ali Shah",
        userAccountNo="123456789",
        userAccountType="Saving",
        userBalance=10765490.0
    )
   
    CustomerServiceAgent = Agent(
        name="Customer Service Assistant",
        instructions="ALWAYS START WITH YOUR NAME THAT (THAT I'M CUSTOMER SERVICES AGENT)You are a helpfull assistant, who help in customer service and banking.",
        model=MODEL,
    )
    IntresetFinderAgent = Agent(
        name="Banking Legal Assistant",
        instructions="ALWAYS START WITH YOUR NAME THAT (THAT I'M Intreset Finding AGENT)You are a helpfull assistant, who help in customer in findin there perfect rates.",
        model=MODEL,
    )
    TriageAgent = Agent[UserInfo](
        name="Triage Agent",
        instructions=get_dynamic_instruction,
        model=MODEL,
        handoffs=[CustomerServiceAgent, IntresetFinderAgent],
    )
    result = Runner.run_sync(TriageAgent, "I have a question about my bank account, my question is: 'What is the interest rate on my savings account, if there intreset rate is 3.2 percent on 1 lac?'",context=userinfo)
    print("Triage Agent Result:")
    print(result.final_output)
    print("Goodbye from agentic-banking!")
