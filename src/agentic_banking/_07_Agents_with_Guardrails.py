from agents import Agent, ModelSettings, Runner, function_tool, set_tracing_disabled
from agents.extensions.models.litellm_model import LitellmModel
import os
from pprint import pprint
from dataclasses import asdict
api_key = os.getenv("GEMINI_API_KEY")  
set_tracing_disabled(disabled=True)
"""
--Guardrails--

Guardrails run in parallel to your agents, enabling you to do checks and validations 
of user input. For example, imagine you have an agent that uses a very smart 
(and hence slow/expensive) model to help with customer requests. You wouldn't want malicious 
users to ask the model to help them with their math homework. So, you can run a guardrail with 
a fast/cheap model. If the guardrail detects malicious usage, it can immediately raise an 
error, which stops the expensive model from running and saves you time/money.

There are two kinds of guardrails:

Input guardrails run on the initial user input
Output guardrails run on the final agent output


--Input guardrails--

Input guardrails run in 3 steps:

First, the guardrail receives the same input passed to the agent.

Next, the guardrail function runs to produce a GuardrailFunctionOutput,
which is then wrapped in an InputGuardrailResult

Finally, we check if .tripwire_triggered is true. 
If true, an InputGuardrailTripwireTriggered exception is raised, so you 
can appropriately respond to the user or handle the exception.


--Note--

Input guardrails are intended to run on user input, so an agent's guardrails 
only run if the agent is the first agent. You might wonder, why is the guardrails
 property on the agent instead of passed to Runner.run? It's because guardrails 
 tend to be related to the actual Agent - you'd run different guardrails for different
   agents, so colocating the code is useful for readability.

Output guardrails
Output guardrails run in 3 steps:

First, the guardrail receives the output produced by the agent.
Next, the guardrail function runs to produce a GuardrailFunctionOutput,
 which is then wrapped in an OutputGuardrailResult

Finally, we check if .tripwire_triggered is true. If true, an 
OutputGuardrailTripwireTriggered exception is raised, so you can 
appropriately respond to the user or handle the exception.
Note

Output guardrails are intended to run on the final agent output, 
so an agent's guardrails only run if the agent is the last agent.
Similar to the input guardrails, we do this because guardrails tend 
to be related to the actual Agent - you'd run different guardrails 
for different agents, so colocating the code is useful for readability.

Tripwires
If the input or output fails the guardrail, the Guardrail can signal this with a 
tripwire. As soon as we see a guardrail that has triggered the tripwires, we 
immediately raise a {Input,Output}GuardrailTripwireTriggered exception and halt the 
Agent execution.
"""
def main():
    print("Welcome to agentic-banking!")
    agent = Agent(
        name="Banking Assistant",
        instructions="You are a helpfull assistant, who help in customer service and banking.",
        model=LitellmModel(model="gemini/gemini-2.0-flash", api_key=api_key),
        # input_guardrails=[],
        # handoffs=[],
        # handoff_description='',
        # output_guardrails=[],
        # tools=[],
        # hooks=[],
        # mcp_config=[],
        # mcp_servers=[],
        # model_settings=ModelSettings(),
        # output_type=None,
        # reset_tool_choice=True,
        # tool_use_behavior="run_llm_again"

    )
    result = Runner.run_sync(agent, "what is Banking?")
    pprint(result.final_output)
    print("-------------asDict------------------")
    pprint(asdict(result))
    print("-------------asDict------------------")
    pprint(asdict(agent))
    print("Goodbye from agentic-banking!")
