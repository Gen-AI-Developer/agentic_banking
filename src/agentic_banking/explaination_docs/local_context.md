In the **OpenAI Agents SDK**, **local context** refers to information passed only to a **specific tool** or **call** within a step, rather than shared globally across all steps.

---

### ✅ **Example: Using Local Context in a Tool Call**

```python
from openai import AssistantEventHandler

class MyHandler(AssistantEventHandler):
    def on_tool_call(self, tool_call):
        if tool_call.name == "get_weather":
            # Local context for just this tool
            location = tool_call.input.get("location", "New York")
            return {"temperature": "25°C", "location": location}
```

### 🧠 **Concept:**

* Local context → only applies to one tool/step (e.g., the input to `get_weather`)
* **Not shared** with other tools or turns

---

### 🧪 More Explicit Example with Local Context in Tool Input

```python
agent.run(
    input="What's the weather in Lahore?",
    tools=[get_weather_tool],
    context={
        "tool_input": {
            "get_weather": {
                "location": "Lahore"  # ← local context specific to this tool
            }
        }
    }
)
```

Only the `get_weather` tool sees `"Lahore"` — other tools don’t get this unless specified.

---

Let me know if you want the same in JSON or full agent setup.
