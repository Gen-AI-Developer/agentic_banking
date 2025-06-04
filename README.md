# Learning Open AI Agents SDK with Example in a Hardway by SafdarAliShah

This repository demonstrates a comprehensive journey through the configuration and usage of agents using the [OpenAI Agents SDK](https://github.com/openai/openai-agents). Each example in the `src/agentic_banking/` directory explores a different aspect or feature of agentic workflows, showcasing how agents can be set up, extended, and utilized in various scenarios.

## Project Goals

- **Showcase all available agent configuration options** in the OpenAI Agents SDK.
- Provide **step-by-step examples** for each major feature, including model selection, dynamic instructions, tool integration, context management, guardrails, streaming, and more.
- Serve as a reference for developers looking to leverage agentic patterns in their own applications.

## Directory Structure

- `01_Agents.py` — Basic agent creation and usage.
- `01.1_Agents_with_Model_setting.py` — Setting custom models for agents.
- `01.2_Agents_with_Dynamic_instruction.py` — Using dynamic instructions.
- `02_Agent_with_handoff.py` — Agent handoff scenarios.
- `02.1_Agent_with_Triage_agent.py` — Triage agent patterns.
- `03_Agent_with_Tool.py` — Integrating tools with agents.
- `03.1_Agent_with_Hosted_tools.py` — Using hosted tools.
- `03.1.1_Agent_with_Custom_function_tool.py` — Custom function tools.
- `03.2_Agents_with_Agents_as_tools.py` — Using agents as tools for other agents.
- `03.2.1_Agent_as_a_Customizing_tool_agent.py` — Customizing agent-as-tool.
- `03.3_Forcing_tool_use_on_Agent.py` — Forcing tool use in agents.
- `03.3.1_Agents_with_tools_Errors.py` — Handling tool errors.
- `04.1_Agents_with_Runner_run.py` — Running agents with the `Runner.run` method.
- `04.2_Agents_with_Runner_sync.py` — Synchronous agent execution.
- `04.3_Agents_with_Runner_async.py` — Asynchronous agent execution.
- `05_Agents_with_local_context.py` — Local context management.
- `05.1_Agents_with_local_context_Agent_level_context.py` — Agent-level context.
- `05.2_Agents_with_local_context_llm_level_context.py` — LLM-level context.
- `06_Agents_with_llm_Context.py` — LLM context usage.
- `07_Agents_with_Guardrails.py` — Input/output guardrails.
- `07.1_Agents_with_input_Guardrails.py` — Input guardrails.
- `07.2_Agents_with_ouput_Guardrails.py` — Output guardrails.
- `08_Agents_with_Streaming.py` — Streaming responses.
- `08_Agents_with_streaming_Raw_response_events.py` — Streaming raw response events.
- `08_Agents_with_streaming_Run_item_events _and_agent_events.py` — Streaming run item and agent events.
- `09_Agents_with_Structure_output.py` — Structured outputs.
- `10_Agent_with_Lifecycle.py` — Agent lifecycle management.
- `10.1.Agent_with_Lifecycle_run_hooks.py` — Lifecycle run hooks.
- `10.2.Agent_with_Lifecycle_agent_hooks.py` — Lifecycle agent hooks.
- `11_Agent_Cloning_copying_agents.py` — Cloning/copying agents.
- `12_Running_Agents_Exceptions.py` — Handling exceptions during agent runs.
- `13_Agent_tracing.py` — Agent tracing and debugging.

## Getting Started

1. **Install dependencies:**
   ```sh
   pip install -e .
   ```

2. **Set up environment variables:**
   - Copy `.env.example` to `.env` and fill in your API keys.

3. **Run an example:**
   ```sh
   python src/agentic_banking/01_Agents.py
   ```

## Suggestions for Additional Examples

- **Custom Memory Integration:** Plug in custom memory backends or strategies.
- **Multi-Agent Collaboration:** Multiple agents collaborating on a task.
- **Advanced Tool Chaining:** Chaining multiple tools or tool outputs.
- **Agent Evaluation/Testing:** Systematic testing and evaluation of agent outputs.

---

Feel free to update this README as your project evolves!