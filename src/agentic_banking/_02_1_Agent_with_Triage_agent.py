from agents import Agent, Runner, function_tool, set_tracing_disabled
from agents.extensions.models.litellm_model import LitellmModel
import os
api_key = os.getenv("GEMINI_API_KEY")  
set_tracing_disabled(disabled=True)
MODEL=LitellmModel(model="gemini/gemini-2.0-flash", api_key=api_key,)
def main():
    print("Welcome to Triage Agent!")
   
    CustomerServiceAgent = Agent(
        name="Customer Service Assistant",
        instructions="ALWAYS START WITH YOUR NAME THAT (THAT I'M CUSTOMER SERVICES AGENT)You are a helpfull assistant, who help in customer service and banking.",
        model=MODEL,
    )
    BankingLegalAgent = Agent(
        name="Banking Legal Assistant",
        instructions="ALWAYS START WITH YOUR NAME THAT (THAT I'M BANKING LEGAL AGENT)You are a helpfull assistant, who help in customer in banking legal matters.",
        model=MODEL,
    )
    TriageAgent = Agent(
        name="Triage Agent",
        instructions="You are a helpful triage agent who decides which agent to handoff the request to. You will always handoff to Customer Service Agent.",
        model=MODEL,
        handoffs=[CustomerServiceAgent, BankingLegalAgent],
    )
    result = Runner.run_sync(TriageAgent, "I have a question about my bank account, my question is: 'What is the interest rate on my savings account?'")
    print("Triage Agent Result:")
    print(result.final_output)
    print("Goodbye from agentic-banking!")
