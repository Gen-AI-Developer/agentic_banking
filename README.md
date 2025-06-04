# Learning Open AI Agents SDK with Example in a Hardway by SafdarAliShah

This repository demonstrates a comprehensive journey through the configuration and usage of agents using the [OpenAI Agents SDK](https://github.com/openai/openai-agents). Each example in the `src/agentic_banking/` directory explores a different aspect or feature of agentic workflows, showcasing how agents can be set up, extended, and utilized in various scenarios.

## Project Goals

- **Showcase all available agent configuration options** in the OpenAI Agents SDK.
- Provide **step-by-step examples** for each major feature, including model selection, dynamic instructions, tool integration, context management, guardrails, streaming, and more.
- Serve as a reference for developers looking to leverage agentic patterns in their own applications.

## Directory Structure

- `src/agentic_banking/01_Agents.py` — Basic agent creation and usage.
- `src/agentic_banking/01.1_Agents_with_Model_setting.py` — Setting custom models for agents.
- `src/agentic_banking/01.2_Agents_with_Dynamic_instruction.py` — Using dynamic instructions.
- `src/agentic_banking/02_Agent_with_handoff.py` — Agent handoff scenarios.
- `src/agentic_banking/02.1_Agent_with_Triage_agent.py` — Triage agent patterns.
- `src/agentic_banking/03_Agent_with_Tool.py` — Integrating tools with agents.
- `src/agentic_banking/03.1_Agents_with_tools_Errors.py` — Handling tool errors.
- `src/agentic_banking/03.2_Agents_with_Agents_as_tools.py` — Using agents as tools for other agents.
- `src/agentic_banking/04.1_Agents_with_Runner_run.py` — Running agents with the `Runner.run` method.
- `src/agentic_banking/04.2_Agents_with_Runner_sync.py` — Synchronous agent execution.
- `src/agentic_banking/04.3_Agents_with_Runner_async.py` — Asynchronous agent execution.
- `src/agentic_banking/05_Agents_with_local_context.py` — Local context management.
- `src/agentic_banking/05.1_Agents_with_local_context_Agent_level_context.py` — Agent-level context.
- `src/agentic_banking/05.2_Agents_with_local_context_llm_level_context.py` — LLM-level context.
- `src/agentic_banking/06_Agents_with_llm_Context.py` — LLM context usage.
- `src/agentic_banking/07_Agents_with_Guardrails.py` — Input/output guardrails.
- `src/agentic_banking/07.1_Agents_with_input_Guardrails.py` — Input guardrails.
- `src/agentic_banking/07.2_Agents_with_ouput_Guardrails.py` — Output guardrails.
- `src/agentic_banking/08_Agents_with_Streaming.py` — Streaming responses.
- `src/agentic_banking/09_Agents_with_Structure_output.py` — Structured outputs.
- `src/agentic_banking/10.Agent_with_Lifecycle.py` — Agent lifecycle management.

## Getting Started

1. **Install dependencies:**
   ```sh
   pip install -e .