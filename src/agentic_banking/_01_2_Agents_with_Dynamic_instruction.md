# _01_2_Agents_with_Dynamic_instruction

Let’s break down the concept of dynamic instructions in the context of the OpenAI Agents SDK, specifically for an agent like a "Triage agent." I’ll explain the provided example line by line and then provide additional examples to deepen your understanding for your quiz and exam preparation. The purpose of dynamic instructions is to allow flexibility in generating agent prompts based on runtime context, such as user data or environmental variables, rather than hardcoding instructions at agent creation.

---

### Explanation of the Provided Example

Here’s the code you provided:

```python
def dynamic_instructions(
    context: RunContextWrapper[UserContext], agent: Agent[UserContext]
) -> str:
    return f"The user's name is {context.context.name}. Help them with their questions."


agent = Agent[UserContext](
    name="Triage agent",
    instructions=dynamic_instructions,
)
```

#### Line-by-Line Breakdown

1. **Function Definition:**
   ```python
   def dynamic_instructions(
       context: RunContextWrapper[UserContext], agent: Agent[UserContext]
   ) -> str:
   ```
   - **Purpose:** This defines a function named `dynamic_instructions` that generates a custom prompt for the agent at runtime.
   - **Parameters:**
     - `context: RunContextWrapper[UserContext]`: This is a wrapper object that provides access to the runtime context, including user-specific data. The `UserContext` type likely contains user-related information, such as a name, preferences, or session details.
     - `agent: Agent[UserContext]`: This is the agent instance, allowing the function to access properties of the agent, such as its name or configuration.
   - **Return Type:** The function returns a string (`-> str`), which will be used as the agent’s instructions or prompt.
   - **Depth:** The `RunContextWrapper` is a generic type, and `UserContext` is a custom type defining the structure of user data. This setup allows the function to dynamically tailor instructions based on runtime conditions.

2. **Dynamic Prompt Generation:**
   ```python
   return f"The user's name is {context.context.name}. Help them with their questions."
   ```
   - **Purpose:** This line creates a string that will guide the agent’s behavior.
   - **Details:**
     - `context.context.name`: The `context` object (from `RunContextWrapper`) has a nested `context` attribute (likely due to the wrapper structure) that holds a `UserContext` object. The `name` field is accessed to retrieve the user’s name.
     - The f-string dynamically inserts the user’s name into the prompt, personalizing it.
     - The second part, “Help them with their questions,” is a static instruction, telling the agent its primary role.
   - **Depth:** This approach allows the agent to adapt its behavior based on who is interacting with it, making responses more relevant and personalized.

3. **Agent Creation:**
   ```python
   agent = Agent[UserContext](
       name="Triage agent",
       instructions=dynamic_instructions,
   )
   ```
   - **Purpose:** This creates an agent instance that will use the dynamic instructions provided by the function.
   - **Details:**
     - `Agent[UserContext]`: This is a generic type, indicating the agent works with a `UserContext` type for contextual data.
     - `name="Triage agent"`: The agent is named “Triage agent,” suggesting its role is to categorize, prioritize, or route user queries (e.g., in a support or helpdesk scenario).
     - `instructions=dynamic_instructions`: Instead of a static string, the `instructions` parameter is set to the `dynamic_instructions` function. At runtime, the agent will call this function to get its prompt.
   - **Depth:** The use of a function for `instructions` enables flexibility. The agent can adapt its behavior based on the user, the agent’s state, or other runtime factors.

#### Purpose of the Code
- **Overall Goal:** This code sets up a "Triage agent" that dynamically generates its instructions based on the user’s context, specifically their name. The agent’s role is to assist users with their questions, and the dynamic instructions ensure the prompt is personalized.
- **Why Dynamic Instructions?** Unlike static instructions (e.g., `instructions="Help users with questions"`), dynamic instructions allow the agent to adapt to varying contexts, such as user identity, time of day, or specific query types, making it more versatile for triage tasks.

---

### Additional Examples of Dynamic Instructions

Below, I’ll provide more examples of dynamic instructions for a "Triage agent" to illustrate different use cases. Each example builds on the concept, showing how to leverage context and agent properties for varied scenarios. I’ll explain each line in depth.

#### Example 1: Dynamic Instructions Based on User Role
This example tailors instructions based on whether the user is a customer, admin, or guest.

```python
def dynamic_instructions(
    context: RunContextWrapper[UserContext], agent: Agent[UserContext]
) -> str:
    user_role = context.context.role if hasattr(context.context, 'role') else 'guest'
    if user_role == 'customer':
        return f"Welcome, {context.context.name}! As a customer, I’ll help you with billing, orders, or support queries. Ask away!"
    elif user_role == 'admin':
        return f"Hello, {context.context.name}! As an admin, I can assist with system config, user management, or logs. What do you need?"
    else:
        return f"Hi, {context.context.name}! As a guest, I can provide general info or guide you to sign up. What’s your question?"


agent = Agent[UserContext](
    name="Triage agent",
    instructions=dynamic_instructions,
)
```

**Line-by-Line Explanation:**

1. **Function Definition:**
   ```python
   def dynamic_instructions(
       context: RunContextWrapper[UserContext], agent: Agent[UserContext]
   ) -> str:
   ```
   - **Purpose:** Defines a function to generate dynamic instructions.
   - **Parameters:** Takes `context` (runtime user data) and `agent` (the agent instance).
   - **Return Type:** Returns a string for the agent’s prompt.
   - **Depth:** The function will inspect the user’s context to customize the agent’s behavior.

2. **Role Extraction:**
   ```python
   user_role = context.context.role if hasattr(context.context, 'role') else 'guest'
   ```
   - **Purpose:** Retrieves the user’s role from the context.
   - **Details:**
     - `context.context.role`: Accesses the `role` attribute from the `UserContext` object within the wrapper.
     - `hasattr(context.context, 'role')`: Checks if the `role` attribute exists to avoid errors.
     - If no role is found, defaults to `'guest'`.
   - **Depth:** This handles cases where the context might not include a role, ensuring the agent still functions.

3. **Conditional Logic for Customer:**
   ```python
   if user_role == 'customer':
       return fsig"Welcome, {context.context.name}! As a customer, I’ll help you with billing, orders, or support queries. Ask away!"
   ```
   - **Purpose:** Provides tailored instructions for customers.
   - **Details:**
     - Uses the user’s name for personalization.
     - Specifies the agent’s triage role: handling billing, orders, or support.
     - Encourages the user to ask questions.
   - **Depth:** This focuses the agent on customer-specific tasks, a key aspect of triage.

4. **Conditional Logic for Admin:**
   ```python
   elif user_role == 'admin':
       return f"Hello, {context.context.name}! As an admin, I can assist with system config, user management, or logs. What do you need?"
   ```
   - **Purpose:** Customizes instructions for admin users.
   - **Details:**
     - Personalizes with the user’s name.
     - Lists admin-specific tasks: system configuration, user management, and logs.
   - **Depth:** This shifts the agent’s focus to technical or administrative triage tasks.

5. **Default Case for Guest:**
   ```python
   else:
       return f"Hi, {context.context.name}! As a guest, I can provide general info or guide you to sign up. What’s your question?"
   ```
   - **Purpose:** Handles users without a defined role (guests).
   - **Details:**
     - Uses a friendly greeting with the user’s name.
     - Offers basic help or signup guidance, suitable for guests.
   - **Depth:** Ensures the agent remains useful even for unknown users.

6. **Agent Creation:**
   ```python
   agent = Agent[UserContext](
       name="Triage agent",
       instructions=dynamic_instructions,
   )
   ```
   - **Purpose:** Creates a "Triage agent" that uses the dynamic function.
   - **Details:** The agent calls `dynamic_instructions` at runtime to get tailored prompts based on the user’s role.
   - **Depth:** This setup makes the agent versatile for triaging queries from different user types.

**Purpose of This Example:**
- The goal is to make the Triage agent adapt its behavior based on the user’s role, directing customers, admins, and guests to appropriate help areas. This is ideal for a support system where queries need to be routed differently.

---

#### Example 2: Async Dynamic Instructions Based on Time of Day
This example uses an async function to adjust instructions based on the time of day, simulating a scenario where the agent’s availability or focus changes.

```python
from datetime import datetime
import asyncio

async def dynamic_instructions(
    context: RunContextWrapper[UserContext], agent: Agent[UserContext]
) -> str:
    current_hour = datetime.now().hour
    if current_hour < 12:
        greeting = "Good morning"
        focus = "starting your day, such as checking status or basic troubleshooting"
    elif current_hour < 18:
        greeting = "Good afternoon"
        focus = "ongoing tasks, like updates or issue resolution"
    else:
        greeting = "Good evening"
        focus = "wrapping up, such as reports or urgent fixes"
    return f"{greeting}, {context.context.name}! The Triage agent is here to assist with {focus}. What can I help you with today?"

agent = Agent[UserContext](
    name="Triage agent",
    instructions=dynamic_instructions,
)
```

**Line-by-Line Explanation:**

1. **Imports:**
   ```python
   from datetime import datetime
   import asyncio
   ```
   - **Purpose:** Imports necessary modules.
   - **Details:**
     - `datetime`: Used to get the current time.
     - `asyncio`: Supports async functionality, as this is an async function.
   - **Depth:** The OpenAI Agents SDK supports both regular and async functions, making this valid for dynamic instructions.

2. **Async Function Definition:**
   ```python
   async def dynamic_instructions(
       context: RunContextWrapper[UserContext], agent: Agent[UserContext]
   ) -> str:
   ```
   - **Purpose:** Defines an async function to generate dynamic instructions.
   - **Details:** The `async` keyword allows the function to handle asynchronous operations, though none are used here beyond time checking.
   - **Depth:** Async functions are useful if the instructions need to fetch data (e.g., from a database) or perform I/O operations.

3. **Get Current Hour:**
   ```python
   current_hour = datetime.now().hour
   ```
   - **Purpose:** Retrieves the current hour (0-23) to determine the time of day.
   - **Details:** Uses `datetime.now()` to get the current time and `.hour` to extract the hour.
   - **Depth:** This allows the agent to adapt its tone and focus based on time, which can be useful for triage in time-sensitive contexts.

4. **Conditional Logic for Morning:**
   ```python
   if current_hour < 12:
       greeting = "Good morning"
       focus = "starting your day, such as checking status or basic troubleshooting"
   ```
   - **Purpose:** Sets instructions for morning hours (before 12 PM).
   - **Details:**
     - `greeting`: A friendly, time-appropriate salutation.
     - `focus`: Specifies morning-relevant triage tasks, like status checks.
   - **Depth:** This tailors the agent’s tone and priorities to the time of day.

5. **Conditional Logic for Afternoon:**
   ```python
   elif current_hour < 18:
       greeting = "Good afternoon"
       focus = "ongoing tasks, like updates or issue resolution"
   ```
   - **Purpose:** Adjusts instructions for afternoon (12 PM to 6 PM).
   - **Details:** Sets a greeting and focus for midday tasks, such as updates.
   - **Depth:** This keeps the agent relevant for ongoing work.

6. **Conditional Logic for Evening:**
   ```python
   else:
       greeting = "Good evening"
       focus = "wrapping up, such as reports or urgent fixes"
   ```
   - **Purpose:** Handles evening hours (6 PM onward).
   - **Details:** Uses an evening greeting and focuses on end-of-day tasks.
   - **Depth:** This aligns the agent with late-day triage needs.

7. **Dynamic Prompt:**
   ```python
   return f"{greeting}, {context.context.name}! The Triage agent is here to assist with {focus}. What can I help you with today?"
   ```
   - **Purpose:** Combines the greeting, user’s name, and focus into a tailored prompt.
   - **Details:** Personalizes with the name and adjusts focus based on time.
   - **Depth:** This makes the agent feel responsive and context-aware.

8. **Agent Creation:**
   ```python
   agent = Agent[UserContext](
       name="Triage agent",
       instructions=dynamic_instructions,
   )
   ```
   - **Purpose:** Creates a Triage agent using the async dynamic instructions.
   - **Details:** The agent calls the async function at runtime to get its prompt.
   - **Depth:** The async nature allows flexibility for future expansions, like fetching time from a server.

**Purpose of This Example:**
- The goal is to make the Triage agent adapt its tone and focus based on the time of day, enhancing user experience and relevance for triage tasks like status checks or urgent fixes.

---

#### Example 3: Dynamic Instructions Based on Query Priority
This example adjusts instructions based on a priority level in the context, useful for triaging urgent versus routine queries.

```python
def dynamic_instructions(
    context: RunContextWrapper[UserContext], agent: Agent[UserContext]
) -> str:
    priority = getattr(context.context, 'priority', 'low')
    if priority == 'high':
        return f"Urgent alert, {context.context.name}! The Triage agent is prioritizing your critical issue. Describe your problem, and I’ll escalate it quickly!"
    elif priority == 'medium':
        return f"Attention, {context.context.name}! The Triage agent is here for your moderate issue. Tell me about it, and I’ll route it appropriately."
    else:
        return f"Hi, {context.context.name}! The Triage agent is ready for your routine query. What’s the issue, and I’ll guide you to a solution."


agent = Agent[UserContext](
    name="Triage agent",
    instructions=dynamic_instructions,
)
```

**Line-by-Line Explanation:**

1. **Function Definition:**
   ```python
   def dynamic_instructions(
       context: RunContextWrapper[UserContext], agent: Agent[UserContext]
   ) -> str:
   ```
   - **Purpose:** Defines a function to generate dynamic instructions.
   - **Details:** Takes context and agent as inputs, returns a string.
   - **Depth:** This sets the stage for priority-based customization.

2. **Priority Extraction:**
   ```python
   priority = getattr(context.context, 'priority', 'low')
   ```
   - **Purpose:** Gets the priority level from the context.
   - **Details:**
     - `getattr(context.context, 'priority', 'low')`: Safely accesses the `priority` attribute, defaulting to `'low'` if missing.
   - **Depth:** Using `getattr` prevents errors if the context lacks a priority field.

3. **High Priority Case:**
   ```python
   if priority == 'high':
       return f"Urgent alert, {context.context.name}! The Triage agent is prioritizing your critical issue. Describe your problem, and I’ll escalate it quickly!"
   ```
   - **Purpose:** Tailors instructions for high-priority issues.
   - **Details:**
     - Uses an urgent tone and mentions escalation.
     - Personalizes with the user’s name.
   - **Depth:** This focuses the agent on rapid triage for critical issues.

4. **Medium Priority Case:**
   ```python
   elif priority == 'medium':
       return f"Attention, {context.context.name}! The Triage agent is here for your moderate issue. Tell me about it, and I’ll route it appropriately."
   ```
   - **Purpose:** Handles medium-priority queries.
   - **Details:** Indicates moderate urgency and routing focus.
   - **Depth:** This balances urgency and standard triage processes.

5. **Low Priority Case:**
   ```python
   else:
       return f"Hi, {context.context.name}! The Triage agent is ready for your routine query. What’s the issue, and I’ll guide you to a solution."
   ```
   - **Purpose:** Addresses routine, low-priority queries.
   - **Details:** Uses a casual tone and offers guidance.
   - **Depth:** This ensures all queries are handled, even non-urgent ones.

6. **Agent Creation:**
   ```python
   agent = Agent[UserContext](
       name="Triage agent",
       instructions=dynamic_instructions,
   )
   ```
   - **Purpose:** Creates a Triage agent with dynamic, priority-based instructions.
   - **Details:** The agent adapts its behavior based on query priority.
   - **Depth:** This is key for triage, as priority determines routing and response urgency.

**Purpose of This Example:**
- The goal is to enable the Triage agent to adjust its tone and actions based on query priority, ensuring urgent issues are escalated and routine ones are handled appropriately.

---

### Key Takeaways for Your Quiz and Exam
- **Dynamic Instructions Purpose:** They allow agents to adapt prompts at runtime based on context (e.g., user name, role, time, priority), unlike static instructions.
- **Function Structure:** Takes `context` (runtime data) and `agent` (agent instance), returns a string. Can be regular or async.
- **Triage Agent Role:** A Triage agent categorizes, prioritizes, and routes queries, making dynamic instructions ideal for adapting to user needs.
- **Flexibility:** Examples show customization by user role, time of day, and query priority, all relevant for triage scenarios.

These examples and explanations cover the concept comprehensively. Practice these variations to understand how dynamic instructions enhance agent flexibility for your upcoming quiz and exam! Let me know if you’d like more examples or deeper clarification.