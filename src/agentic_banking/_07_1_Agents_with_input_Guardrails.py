import asyncio
from agents import Agent, GuardrailFunctionOutput, InputGuardrailTripwireTriggered, RunContextWrapper, Runner, TResponseInputItem, function_tool, input_guardrail, set_tracing_disabled
from agents.extensions.models.litellm_model import LitellmModel
import os
from pydantic import BaseModel

api_key = os.getenv("GEMINI_API_KEY")  
set_tracing_disabled(disabled=True)

class BankingQuestion(BaseModel):
    is_banking_question: bool
    reason: str 

guardrail_agent = Agent(
    name="Guardrail Agent",
    instructions="You are a guardrail agent that checks for whether the query or question is related to Banking or Not.",
    model=LitellmModel(model="gemini/gemini-2.0-flash", api_key=api_key,),
    output_type=BankingQuestion,
)

@input_guardrail
async def math_guardrails(context: RunContextWrapper[None], agent: Agent,input: str | list[TResponseInputItem]) -> GuardrailFunctionOutput:
    """
    Guardrail function to check if the input text contains question / query / operation related to Banking.
    If it doesn't, it returns a message indicating that other than banking operations are not allowed.
    """
    guardrail_agent_response = await Runner.run(guardrail_agent, input,context=context.context)
    return GuardrailFunctionOutput(
            output_info=guardrail_agent_response.final_output,
            tripwire_triggered=guardrail_agent_response.final_output.reason,
        )

async def main():
    print("Welcome to agentic-banking!")
    agent = Agent(
        name="Banking Assistant",
        instructions="You are a helpfull assistant, who help in customer service and banking.",
        model=LitellmModel(model="gemini/gemini-2.0-flash", api_key=api_key,),
        input_guardrails=[math_guardrails],
    )
    try :
        result = await Runner.run(agent, "what is Banking?")
        print(result.final_output)
    except InputGuardrailTripwireTriggered as e:
        print(f"Guardrail Tripwire Triggered: {e}")
    print("Goodbye from agentic-banking!")

if __name__ == "__main__":
    asyncio.run(main())