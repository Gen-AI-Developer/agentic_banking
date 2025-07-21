### Handsoffs in depth
input_filter

input_filter=handoff_filters.remove_all_tools,
___
### is_enabled()
Remember is_enabled() attribute can be used both in Handoffs and tool-calling.
is_enabled class-attribute instance-attribute
___
### Difference between Handoff and agent_as_tool
What is the difference between use of handoff and agent_as_tool?
answer: The question may be different but understand the concept.
In handoffs, the control is transferred to the new agent and in agent_as_tool, agent is used as a tool whose output goes back to the triage agent and control remains with the source agent.
___
### Tool_use_behaviour
If you leave tool_use_behaviour to default, what will be the Agent loop?

Most scenarios contained multiple concepts at a time which means that covering one topic and leaving the other may create problems for you during quiz.
is_enabled() was used in combination with dynamic instructions and tool calling which made it complicated.
Only after thorough reading of question and code and understanding everything, you will be able to answer correctly.
___
```Note```
De ta Callable hm pass keday shi. which means che yaw function ke mung sa check koo aw da aghe function return True ya False v aw da aghe pa base mung handoff enable ya disable kawoo.
___
```Note```
Daa der scenarios ke use shaway wo. Daa lag check kayi. Da de use cases da ChatGPT na tapos okayi. Kho awal warla link warkayi da SDK che response ye accurate v


___

is_enabled: (
    bool
    | Callable[
        [RunContextWrapper[Any], AgentBase[Any]],
        MaybeAwaitable[bool],
    ]
) = True
```Note```

Whether the handoff is enabled. Either a bool or a Callable that takes the run context and agent and returns whether the handoff is enabled. You can use this to dynamically enable/disable a handoff based on your context/state.
___
### ModelSettings
understand what is top p , top k , temperature...
https://openai.github.io/openai-agents-python/ref/model_settings/
___
### Agentic Workflows with Prompt Engineering Guide

GPT-4.1
GPT-4.1 excels at agentic workflows, which involve autonomous, multi-step problem-solving processes.
The model was trained with diverse agentic problem-solving trajectories and achieves state-of-the-art results on benchmarks like SWE-bench Verified, solving 55% of problems.
To fully utilize agentic capabilities, three types of system prompt reminders are recommended:
Persistence: Ensures the model continues working on a problem until fully resolved, avoiding premature turn termination. Example:

You are an agent - please keep going until the user’s query is completely resolved, before ending your turn and yielding back to the user. Only terminate your turn when you are sure that the problem is solved.
Tool-calling: Encourages the model to use available tools to avoid hallucination or guessing. Example:

If you are not sure about file content or codebase structure pertaining to the user’s request, use your tools to read files and gather the relevant information: do NOT guess or make up an answer.
Planning (Optional): Prompts the model to explicitly plan and reflect on tool calls rather than chaining calls silently, improving problem-solving quality. Example:

`You MUST plan extensively before each function call, and reflect extensively on the outcomes of the previous function calls. DO NOT do this entire process by making function calls only, as this can impair your ability to solve the problem and think insightfully.
These instructions transform GPT-4.1 from a chatbot-like assistant into an autonomous, eager agent that drives interactions forward independently.`
___


### Guardrials Class

https://openai.github.io/openai-agents-python/guardrails/
___
### Result Class
https://openai.github.io/openai-agents-python/results/
___

### Funciton_Error

Handling errors in function tools
When you create a function tool via @function_tool, you can pass a failure_error_function. This is a function that provides an error response to the LLM in case the tool call crashes.

By default (i.e. if you don't pass anything), it runs a default_tool_error_function which tells the LLM an error occurred.
If you pass your own error function, it runs that instead, and sends the response to the LLM.
If you explicitly pass None, then any tool call errors will be re-raised for you to handle. This could be a ModelBehaviorError if the model produced invalid JSON, or a UserError if your code crashed, etc.
If you are manually creating a FunctionTool object, then you must handle errors inside the on_invoke_tool function.
___


Block/non-blocking process.
___
Event Loop depth
___
Fibonacci sequence in tools call example
___

use handsoff in clone parent agent....
___


Cloning/copying agents
By using the clone() method on an agent, you can duplicate an Agent, and optionally change any properties you like.


pirate_agent = Agent(
    name="Pirate",
    instructions="Write like a pirate",
    model="o3-mini",
)

robot_agent = pirate_agent.clone(
    name="Robot",
    instructions="Write like a robot",
)
___

### Context management
Context is an overloaded term. There are two main classes of context you might care about:

Context available locally to your code: this is data and dependencies you might need when tool functions run, during callbacks like on_handoff, in lifecycle hooks, etc.
Context available to LLMs: this is data the LLM sees when generating a response.
___
