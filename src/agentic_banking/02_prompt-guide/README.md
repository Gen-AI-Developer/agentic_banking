# **GPT-4.1 Prompting Guide**
---

### 🚀 **GPT-4.1: The Ultimate Prompting Guide**  
*Unlock next-gen AI capabilities with these battle-tested strategies!*

#### **🌟 Key Advancements**  
- **Massive Leap** from GPT-4o: Superior coding, instruction following, and **1M-token context** support.  
- **Literal Instruction Follower**: Less inference, more precision. A single clear sentence can correct its behavior!  
- **Agentic Powerhouse**: Solves **55% of SWE-bench problems** – perfect for coding workflows.  

---

### 🛠️ **Agentic Workflows: Build Smarter Agents**  
#### **System Prompt Essentials**  
1. **Persistence**:  
   - *Prompt*: "Keep going until the user’s query is **completely resolved**."  
2. **Tool-Calling**:  
   - *Prompt*: "Use tools to read files – **NEVER guess**."  
3. **Planning (Optional)**:  
   - *Prompt*: "Plan before each function call and reflect afterward – **don’t chain silently**."  

#### **Tool-Calling Pro Tips**  
- **Define tools via API** (not manual prompts) – boosts success by **2%**.  
- **Name tools clearly**: Add detailed descriptions and examples in an `# Examples` prompt section.  
- Use OpenAI’s **[Prompt Playground](https://platform.openai.com/playground)** for prototyping.  

#### **SWE-bench Champion Prompt**  
- Features **rigorous testing reminders**:  
  > "Test code **rigorously** – handle edge cases! Failing to test is the #1 failure mode."  
- Includes a Python tool for executing code/applying patches ([See full example](#)).  

---

### 📚 **Long Context: Master 1M Tokens**  
- **Needle-in-a-Haystack**: Works flawlessly at scale!  
- **Tune Context Reliance**:  
  - *Strict*: "Only use provided context – respond ‘I don’t know’ otherwise."  
  - *Flexible*: "Use context first, then basic knowledge if confident."  
- **Prompt Placement**: Put instructions **at both start/end** of long context for best results.  
- **Delimiter Battle Royale**:  
  - ✅ **XML/Formatted Text**: `<doc id="1" title="Fox">...</doc>` or `ID:1 | TITLE: Fox`  
  - ❌ **JSON**: Avoid for large documents – performance dips.  

---

### 💡 **Chain-of-Thought (CoT) Mastery**  
- **Not a Reasoning Model**: But prompt it to "think step-by-step" for complex tasks.  
- **Basic CoT Starter**:  
  > "First, analyze needed documents → Print TITLE/ID → Format as list."  
- **Advanced CoT Template**:  
  ```markdown  
  1. **Query Analysis**: Break down ambiguous asks.  
  2. **Context Analysis**: Rate doc relevance [high/medium/low].  
  3. **Synthesis**: Summarize key docs.  
  ```  

---

### 📜 **Instruction Following: Precision Control**  
#### **Workflow for Perfect Prompts**  
1. Start with **high-level "Response Rules"**.  
2. Add **subsections** (e.g., `# Sample Phrases`).  
3. Specify **step-by-step workflows** (e.g., ordered lists).  
4. Debug conflicts: GPT-4.1 **prioritizes later instructions**.  

#### **Customer Service MVP Prompt**  
- **Rules**:  
  - Always greet: "Hi, you’ve reached NewTelco!"  
  - **Never discuss** politics/religion/legal advice.  
  - Use tools for factual queries.  
- **Tool Integration**:  
  - `lookup_policy_document(topic="family plans")`  
  - `get_user_account_info(phone="(123) 456-7890")`  
- **Output Format**: Include citations like `[Family Plan Policy](ID-010)`.  

---

### ⚙️ **General Prompt Engineering Gems**  
#### **Prompt Structure Template**  
```markdown  
# Role: [Agent Role]  
# Instructions:  
## Sub-Category 1  
- Rule 1  
## Reasoning Steps  
1. Step 1  
2. Step 2  
# Output Format:  
- Use [specific format]  
# Examples  
## Example 1  
User: ...  
Assistant: ...  
```  

#### **Critical Caveats**  
- Avoid forcing tools without data: Add *"Ask users for missing info"*.  
- Prevent repetitive sample phrases: *"Vary wording!"*  
- **Parallel tool calls** may need `parallel_tool_calls=False` if buggy.  

---

### 🔧 **Appendix: Diff Generation Superpowers**  
#### **V4A Diff Format (Recommended)**  
```bash  
*** Update File: path/to/file.py  
@@ class BaseClass  
-    pass  
+    raise NotImplementedError()  
```  
- **No line numbers**: Uses context (3 lines above/below) + `@@` scoping.  
- **Reference Implementation**: Pure-Python `apply_patch.py` provided.  

#### **Alternative Diff Formats**  
- **SEARCH/REPLACE**:  
  ```python  
  >>>> SEARCH  
  def search(): pass  
  ====  
  def search(): raise Error  
  <<<< REPLACE  
  ```  
- **Pseudo-XML**:  
  ```xml  
  <edit><file>path.py</file>  
  <old_code>pass</old_code>  
  <new_code>raise Error</new_code></edit>  
  ```  

---

### 💎 **Golden Advice**  
> "**AI engineering is empirical** – build evals, iterate often, and celebrate small wins!"  

Equip yourself with these strategies, and you’ll harness GPT-4.1’s full potential! 🎯✨  

--- 
**Enjoy the journey – happy prompting!** 🚀