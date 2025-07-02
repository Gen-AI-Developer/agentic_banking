from agents import Agent, Runner, set_tracing_disabled, RunContextWrapper
from agents.extensions.models.litellm_model import LitellmModel
import os
from dataclasses import asdict


# from rich import print
from pydantic import BaseModel

# from agentic_banking import printt
from agentic_banking.printt import printt
api_key = os.getenv("GEMINI_API_KEY")  
set_tracing_disabled(disabled=True)
MODEL=LitellmModel(model="gemini/gemini-2.0-flash", api_key=api_key,)

class UserInfo(BaseModel):
    """
    User information model to hold user details for the Triage Agent.
    This model includes user name, account number, account type, account balance, and currency.
    Attributes:
        userName (str): The name of the user.
        userAccountNo (str): The account number of the user.
        userAccountType (str): The type of account (e.g., Saving, Current).
        userAccountBalance (float): The current balance in the user's account.
        userAccountCurrency (str): The currency of the user's account, default is "PKR".
    """
    userName: str
    userAccountNo: str
    userAccountType: str
    userAccountBalance: float
    userAccountCurrency: str = "PKR"  # Default currency, can be changed if needed

def get_dynamic_instruction(context: RunContextWrapper[UserInfo], agent: Agent[UserInfo]) -> str:
    return f"""
    ALWAYS START WITH YOUR NAME THAT (THAT I'M Intreset Finding AGENT)
        You are a helpfull assistant, who help customer in 
        finding Annual Per Return on Investment (APRI) which is  Interest on Savings. 
        You will be provided with the user's account balance and interest rate.
        Calculate the interest on the user's savings based on the provided interest rate.
        The interest rate will be provided in percentage.
        Use the formula: Interest = (Balance * Interest Rate) / 100
        Respond with the calculated interest amount in the same currency as the user's account balance.
        For example, if the user's account balance is in PKR, respond with the interest amount in PKR.
        
    You use These Detailed provided according to customer need and use, 
    which is Customer / User name :  {context.context.userName}, 
    Customer / User account No. {context.context.userAccountNo}, 
    Customer / User account type is {context.context.userAccountType}, 
    Customer / User Account balance is {context.context.userAccountBalance}, 
    and Customer / User account currency is {context.context.userAccountCurrency}."""

def main():
    print("Welcome to Triage Agent!")

    userinfo = UserInfo(
        userName="Safdar Ali Shah",
        userAccountNo="123456789",
        userAccountType="Saving",
        userAccountBalance=10765490.0,
        userAccountCurrency="PKR"  # Default currency, can be changed if needed
    )
   
    CustomerServiceAgent = Agent(
        name="Customer Service Assistant",
        instructions="ALWAYS START WITH YOUR NAME THAT (THAT I'M CUSTOMER SERVICES AGENT)You are a helpfull assistant, who help in customer service and banking.",
        model=MODEL,
    )
    InterestFinderAgent = Agent(
        name="Banking Interest Finder Assistant",
        instructions=get_dynamic_instruction,
        model=MODEL,
    )
    TriageAgent = Agent[UserInfo](
        name="Triage Agent",
        instructions="Your are a Triage Agent, who triage the customer request and handoff to the appropriate agent based on the user's needs.",
        model=MODEL,
        # handoffs=[CustomerServiceAgent, InterestFinderAgent],
    )


    # def print_tree(data, prefix=""):
    #     if isinstance(data, dict):
    #         for i, (key, value) in enumerate(data.items()):
    #             is_last = i == len(data) - 1
    #             connector = "└── " if is_last else "├── "
    #             print(f"{prefix}{connector}{key}:", end="")
    #             if isinstance(value, (dict, list)):
    #                 print()
    #                 new_prefix = prefix + ("    " if is_last else "│   ")
    #                 print_tree(value, new_prefix)
    #             else:
    #                 print(f" {value}")
    #     elif isinstance(data, list):
    #         for i, item in enumerate(data):
    #             is_last = i == len(data) - 1
    #             connector = "└── " if is_last else "├── "
    #             print(f"{prefix}{connector}Item {i}")
    #             new_prefix = prefix + ("    " if is_last else "│   ")
    #             print_tree(item, new_prefix)
    #     else:
    #         print(f"{prefix}{data}")

    TriageAgent.handoffs.append(CustomerServiceAgent)
    TriageAgent.handoffs.append(InterestFinderAgent)
    result = Runner.run_sync(TriageAgent, "I have a question about my bank account, my question is: Calculate the APRI on my savings in my account, if the Interest rate is 3.2 percent?",context=userinfo)
    print(result.final_output)
    printt(asdict(result))
    # print_tree(asdict(result))
    print("Goodbye from agentic-banking!")
