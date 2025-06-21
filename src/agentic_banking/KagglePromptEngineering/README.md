# Prompt Engineering: A Comprehensive Briefing

**Date:** October 26, 2023
**Author:** Lee Boonstra (February 2025)

---
## 1. Executive Summary

Prompt engineering is the iterative process of designing high-quality text inputs (prompts) to guide Large Language Models (LLMs) to produce accurate and desirable outputs. It is accessible to everyone—not just data scientists or ML engineers—but requires careful attention to:

* Model configurations
* Word choice
* Style and tone
* Structure and context

Effective prompt engineering helps solve issues like ambiguous or inaccurate responses. It's widely applicable in tasks such as:

* Text summarization
* Information extraction
* Question answering
* Code generation/translation

---

## 2. Introduction to Prompt Engineering

A **prompt** is the input an LLM uses to predict output. While simple in appearance, crafting good prompts is complex and iterative.

> "Prompts might need to be optimized for your specific model, regardless of whether you use Gemini language models in Vertex AI, GPT, Claude, or an open-source model like Gemma or LLaMA."

Bad prompts can lead to:

* Ambiguous responses
* Inaccurate output
* Poor performance

Effective prompt design involves optimizing:

* Prompt length
* Style and structure
* Task specificity

---

## 3. LLM Output Configuration

### 3.1 Output Length

* Token count impacts **cost**, **speed**, and **energy usage**.
* Shorter prompts ≠ concise answers (just cut off early).
* Critical for techniques like **ReAct** to avoid post-response "useless tokens".

### 3.2 Sampling Controls

LLMs use probabilities to generate tokens. Key settings:

#### Temperature

* Controls randomness.
* **Lower = deterministic**, **higher = creative**.
* `0` = greedy decoding (most probable token always chosen).

#### Top-K

* Limits sampling to top K tokens.
* **Higher** = more creative
* **Lower** = more factual
* `Top-K=1` = greedy decoding

#### Top-P (Nucleus Sampling)

* Chooses from tokens that make up a probability mass `P` (e.g., 0.95).

> "If you set temperature to 0, top-K and top-P become irrelevant."

### Recommended Settings

| Use Case                       | Temp | Top-P | Top-K |
| ------------------------------ | ---- | ----- | ----- |
| Balanced (Creative + Coherent) | 0.2  | 0.95  | 30    |
| Creative Results               | 0.9  | 0.99  | 40    |
| Less Creative Results          | 0.1  | 0.9   | 20    |
| Single Correct Answer          | 0    | -     | -     |

> ⚠️ **Repetition Loop Bug:** Happens at extreme low/high temperatures. Adjust temperature, Top-K, and Top-P accordingly.

---

## 4. Prompting Techniques

### 4.1 General Prompting / Zero-Shot

* No examples provided
* Suitable for classification tasks
* Use: `Temperature = 0.1`, `Top-P = 1`, `Top-K = disabled`

### 4.2 One-Shot & Few-Shot

* Provide 1 (or a few) examples to guide format/style

### 4.3 System, Contextual, and Role Prompting

* **System Prompting**: Sets purpose, capabilities, output format, tone.
* **Contextual Prompting**: Gives background or task-relevant details.
* **Role Prompting**: Assigns a persona to guide behavior/tone (e.g., teacher, travel guide).

### 4.4 Step-Back Prompting

* LLM "steps back" to reflect on the problem
* Improves reasoning and final output

### 4.5 Chain of Thought (CoT)

* Promotes step-by-step reasoning
* Boosts accuracy for complex tasks (e.g., math/code)
* Combine with one/few-shot examples
* Use `Temperature = 0` for deterministic output

### 4.6 Self-Consistency

* Sends same prompt multiple times with high temp
* Uses majority voting to select final answer
* More accurate, but expensive

### 4.7 Tree of Thoughts (ToT)

* Explores **multiple reasoning paths** (not just one chain)
* Suited for complex decision-making

### 4.8 ReAct (Reason + Act)

* Mixes reasoning with tool use
* Builds action loops like:

  1. Thought
  2. Action
  3. Observation
  4. Update
* Great for early agent behavior modeling

### 4.9 Automatic Prompt Engineering (APE)

* LLM generates and tests variants of prompts
* Evaluates with BLEU/ROUGE
* Reduces manual work and enhances performance

---

## 5. Code Prompting

LLMs excel at code tasks:

* **Writing Code:** Generates snippets (e.g., Python, Bash).

  > "Always read and test the code—LLMs may hallucinate or repeat training data."
* **Explaining Code:** Breaks down functionality.
* **Translating Code:** Converts between languages (e.g., Bash ↔ Python).
* **Debugging & Reviewing:** Identifies errors, suggests improvements.

---

## 6. Multimodal Prompting

Uses **multiple input formats**, like:

* Text + Images
* Text + Audio
* Code + Instructions

Enables broader LLM capabilities for diverse tasks.

---

## 7. Best Practices for Prompt Engineering

* **Keep it Simple**: Clear, concise, understandable.
* **Be Specific**: Define format, length, tone.
* **Control Token Length**: Use config limits or phrase it directly (e.g., *“Explain quantum physics in a tweet-length message.”*)
* **Use Variables**: Dynamic prompts like `{city}`, useful in apps.
* **Try Different Formats**: Questions, statements, and instructions may yield different results.
* **Request Structured Output**: Prefer `JSON` for clarity, but validate/fix malformed JSON using tools like `json-repair`.
* **Collaborate**: Work with other prompt engineers to iterate faster.
* **Document Attempts**:

  * Track in a structured format (e.g., Google Sheet)
  * Log:

    * Prompt name
    * Goal
    * Model used
    * Config (Temp, Tokens, Top-K/P)
    * Full prompt and output
* **Version and Automate**: Store prompts separately from code. Use tests and benchmarks for regression.

> 🔁 Prompt engineering is an **iterative process**: Craft → Test → Analyze → Refine — and repeat with every model/config update.

---
