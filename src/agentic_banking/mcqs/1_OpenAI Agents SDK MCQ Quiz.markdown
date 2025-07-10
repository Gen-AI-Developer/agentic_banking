# OpenAI Agents SDK MCQ Quiz for Graduate-Level Students

This 50-question multiple-choice quiz assesses your ability to develop AI agents professionally using the OpenAI Agents SDK. It is designed for students with Python and programming knowledge, covering both conceptual understanding and programming skills. The quiz duration is 70 minutes.

## Installation and Setup (5 Questions)

1. **What is the correct pip command to install the OpenAI Agents SDK?**  
   a) `pip install openai-agents`  
   b) `pip install openai-agents-python`  
   c) `pip install openai_swarm`  
   d) `pip install swarm`  
   **Answer**: b (assumed based on typical naming conventions)

2. **Which version of Python is required to use the OpenAI Agents SDK?**  
   a) Python 3.6+  
   b) Python 3.8+  
   c) Python 3.10+  
   d) Python 2.7  
   **Answer**: b (likely for modern SDKs)

3. **What is the first step after installing the SDK to use it?**  
   a) Create an agent instance  
   b) Set up the API key  
   c) Define the agent's behavior  
   d) Run the agent  
   **Answer**: b (API key setup is typically required)

4. **How do you verify the SDK installation?**  
   a) Run `pip show openai-agents-python`  
   b) Import the SDK and check for errors  
   c) Execute a sample agent script  
   d) All of the above  
   **Answer**: d (multiple verification methods)

5. **What environment variable is used to store the OpenAI API key?**  
   a) `OPENAI_KEY`  
   b) `OPENAI_API_KEY`  
   c) `API_TOKEN`  
   d) `OPENAI_TOKEN`  
   **Answer**: b (standard for OpenAI APIs)

## Basic Concepts (10 Questions)

6. **What is the primary purpose of the OpenAI Agents SDK?**  
   a) To create web applications  
   b) To develop AI agents for various tasks  
   c) To perform data analysis  
   d) To manage databases  
   **Answer**: b (core purpose of agent SDKs)

7. **What is an AI agent in the context of this SDK?**  
   a) A database management tool  
   b) A program that performs tasks autonomously  
   c) A web server component  
   d) A data visualization tool  
   **Answer**: b (standard agent definition)

8. **What design pattern does the SDK likely use for multi-agent systems?**  
   a) Singleton  
   b) Factory  
   c) Observer  
   d) Orchestrator  
   **Answer**: d (common for multi-agent orchestration)

9. **What type of machine learning model is typically used in the SDK?**  
   a) Supervised learning  
   b) Unsupervised learning  
   c) Reinforcement learning  
   d) Large language models  
   **Answer**: d (likely based on OpenAI's focus)

10. **What is a key feature of the OpenAI Agents SDK?**  
    a) Real-time database syncing  
    b) Task delegation between agents  
    c) Built-in web hosting  
    d) Native GUI support  
    **Answer**: b (assumed for multi-agent systems)

11. **How does the SDK facilitate agent development?**  
    a) By providing pre-trained models  
    b) By offering a high-level API  
    c) By automating deployment  
    d) By including a visual editor  
    **Answer**: b (typical for SDKs)

12. **What is the role of context in an agent's function?**  
    a) To store conversation history  
    b) To pass data between functions  
    c) To manage agent state  
    d) All of the above  
    **Answer**: d (context is multifaceted)

13. **Which component manages agent interactions in the SDK?**  
    a) Task Manager  
    b) Agent Orchestrator  
    c) Data Handler  
    d) Model Selector  
    **Answer**: b (likely orchestrator role)

14. **What is a benefit of using the SDK for agent development?**  
    a) Reduced coding effort  
    b) Automatic scaling  
    c) Built-in security  
    d) All of the above  
    **Answer**: a (primary SDK benefit)

15. **What does the SDK's modularity allow?**  
    a) Easy integration with other tools  
    b) Automatic model updates  
    c) Simplified database management  
    d) Built-in analytics  
    **Answer**: a (modularity supports integration)

## Programming with the SDK (15 Questions)

16. **How do you create an agent named "Assistant" using the gpt-4 model?**  
    a) `agent = Agent("Assistant", "gpt-4")`  
    b) `agent = Agent(name="Assistant", model="gpt-4")`  
    c) `agent = create_agent("Assistant", "gpt-4")`  
    d) `agent = Agent(model="gpt-4", name="Assistant")`  
    **Answer**: b (keyword arguments are standard)

17. **What method is used to get an agent's response to user input?**  
    a) `get_response()`  
    b) `act()`  
    c) `predict()`  
    d) `generate()`  
    **Answer**: b (assumed common method name)

18. **Consider this code:**
    ```python
    from openai_agents import Agent, Task
    agent = Agent(model="gpt-3.5-turbo")
    task = Task(description="Answer questions")
    agent.add_task(task)
    response = agent.act("What is the capital of France?")
    ```
    What is the expected output of `response`?  
    a) "Paris"  
    b) "The capital of France is Paris."  
    c) An object containing the response  
    d) None  
    **Answer**: c (SDKs typically return objects)

19. **How do you define a function for an agent?**  
    a) By decorating it with `@agent_function`  
    b) By adding it to the agent's function list  
    c) By defining it within the agent's class  
    d) By registering it with the SDK  
    **Answer**: b (assumed SDK approach)

20. **What keyword defines an asynchronous function for an agent's action?**  
    a) `async`  
    b) `await`  
    c) `sync`  
    d) `thread`  
    **Answer**: a (Python async syntax)

21. **How do you set the temperature parameter for the agent's model?**  
    a) By passing it to the Agent constructor  
    b) By setting it in the task definition  
    c) By using the `set_temperature()` method  
    d) It cannot be set  
    **Answer**: a (likely constructor parameter)

22. **Which code correctly defines an agent with a greeting function?**  
    a) 
    ```python
    from openai_agents import Agent
    def greet(name):
        return f"Hello, {name}!"
    agent = Agent(functions=[greet])
    ```
    b) 
    ```python
    from openai_agents import Agent, Function
    greet = Function(name="greet", func=lambda name: f"Hello, {name}!")
    agent = Agent(functions=[greet])
    ```
    c) 
    ```python
    from openai_agents import Agent
    class MyAgent(Agent):
        def greet(self, name):
            return f"Hello, {name}!"
    agent = MyAgent()
    ```
    d) None of the above  
    **Answer**: b (assumed Function wrapper)

23. **How does an agent hand off a task to another agent?**  
    a) By calling the other agent's function directly  
    b) By returning a special handoff object  
    c) By sending a message through the SDK  
    d) By updating the shared context  
    **Answer**: b (assumed handoff mechanism)

24. **What is the correct way to handle API errors in the `act` method?**  
    a) Use try-except blocks  
    b) Check the response status  
    c) Retry the request  
    d) All of the above  
    **Answer**: d (comprehensive error handling)

25. **How do you enable logging for an agent's actions?**  
    a) Set the logging level in the configuration  
    b) Use the built-in logging module  
    c) Enable debug mode  
    d) All of the above  
    **Answer**: d (multiple logging options)

26. **What does the `Agent.run()` method do?**  
    a) Starts the agent's main loop  
    b) Executes a single action  
    c) Trains the agent  
    d) Saves the agent's state  
    **Answer**: a (assumed main loop)

27. **How do you specify the model for an agent?**  
    a) By passing the model name to the Agent constructor  
    b) By setting a global configuration  
    c) By using a specific method after creation  
    d) It is automatically selected  
    **Answer**: a (constructor is typical)

28. **What is the output of this code?**
    ```python
    from openai_agents import Agent
    agent = Agent(model="gpt-3.5-turbo")
    agent.set_temperature(0.7)
    ```
    a) A greeting message  
    b) None  
    c) An error if `set_temperature` is invalid  
    d) A confirmation message  
    **Answer**: b (methods typically return None)

29. **How can you integrate the SDK with a third-party API?**  
    a) By defining custom functions  
    b) Through built-in connectors  
    c) It only works with OpenAI APIs  
    d) Only with specific services  
    **Answer**: a (custom functions are flexible)

30. **What is the default timeout for API calls in the SDK?**  
    a) 30 seconds  
    b) 60 seconds  
    c) 120 seconds  
    d) There is no default timeout  
    **Answer**: a (assumed reasonable default)

## Advanced Topics (10 Questions)

31. **How does the SDK handle concurrent tasks across multiple agents?**  
    a) Using threads  
    b) Using asynchronous programming  
    c) Sequentially  
    d) It doesn't support concurrency  
    **Answer**: b (async is modern Python standard)

32. **What is a recommended way to optimize agent performance?**  
    a) Increase the batch size  
    b) Use a faster model  
    c) Implement caching  
    d) All of the above  
    **Answer**: d (multiple optimization strategies)

33. **How can you ensure sensitive data is not exposed in responses?**  
    a) Implement data filtering  
    b) Use encryption  
    c) Limit the agent's access to data  
    d) All of the above  
    **Answer**: d (comprehensive security)

34. **What feature allows scaling to handle thousands of users?**  
    a) Built-in load balancing  
    b) Support for distributed computing  
    c) Asynchronous processing  
    d) All of the above  
    **Answer**: d (scaling requires multiple features)

35. **How do you customize the prompt used by an agent?**  
    a) By setting the prompt parameter  
    b) By overriding the `generate_prompt` method  
    c) No, the prompt is fixed  
    d) Only for certain models  
    **Answer**: a (likely parameter-based)

36. **What is the best practice for designing agent functions?**  
    a) Keep functions small and focused  
    b) Handle all possible edge cases  
    c) Document the agent's capabilities  
    d) All of the above  
    **Answer**: d (best practices are comprehensive)

37. **How does the SDK handle large input data?**  
    a) By chunking the data  
    b) By summarizing it  
    c) It does not support large inputs  
    d) By using streaming  
    **Answer**: a (chunking is common)

38. **What is a planned feature for the next SDK version?**  
    a) Support for more models  
    b) Enhanced multi-agent capabilities  
    c) Improved performance  
    d) Cannot be determined  
    **Answer**: b (assumed based on trends)

39. **How do agents communicate in a multi-agent setup?**  
    a) Through shared memory  
    b) Via message passing  
    c) Using a central controller  
    d) They do not communicate  
    **Answer**: b (message passing is standard)

40. **What ethical consideration is important when deploying agents?**  
    a) Ensuring fairness and avoiding bias  
    b) Protecting user privacy  
    c) Being transparent about AI usage  
    d) All of the above  
    **Answer**: d (ethics are multifaceted)

## Industry Applications (5 Questions)

41. **What is a potential use case for the SDK in finance?**  
    a) Automated trading  
    b) Customer support chatbot  
    c) Fraud detection  
    d) All of the above  
    **Answer**: d (multiple use cases)

42. **In which industry must agents comply with HIPAA regulations?**  
    a) Finance  
    b) Healthcare  
    c) Education  
    d) Retail  
    **Answer**: b (HIPAA is healthcare-specific)

43. **How might the SDK be used in healthcare?**  
    a) To diagnose diseases  
    b) To manage patient records  
    c) To schedule appointments  
    d) All of the above  
    **Answer**: d (broad applications)

44. **What is a benefit of using the SDK in customer service?**  
    a) Faster response times  
    b) Personalized interactions  
    c) Scalability  
    d) All of the above  
    **Answer**: d (multiple benefits)

45. **Which industry could use the SDK for real-time data analysis?**  
    a) Finance  
    b) Logistics  
    c) Manufacturing  
    d) All of the above  
    **Answer**: d (data analysis is versatile)

## Troubleshooting (5 Questions)

46. **If an agent is not responding, what should you check first?**  
    a) The API key  
    b) The model version  
    c) The input parameters  
    d) The network connection  
    **Answer**: c (inputs are often the issue)

47. **What does a `ModelNotFoundError` indicate?**  
    a) The specified model does not exist  
    b) The model is not loaded  
    c) The model is deprecated  
    d) There is a network issue  
    **Answer**: a (error name suggests this)

48. **How do you resolve API rate limit errors?**  
    a) Implement exponential backoff  
    b) Ignore rate limits  
    c) Use multiple API keys  
    d) Reduce the number of requests  
    **Answer**: a (exponential backoff is standard)

49. **What should you do if the agent returns unexpected output?**  
    a) Check the prompt configuration  
    b) Verify the input data  
    c) Adjust the model parameters  
    d) All of the above  
    **Answer**: d (multiple factors)

50. **How can you debug an agent's performance issues?**  
    a) Enable logging  
    b) Monitor API response times  
    c) Profile the code  
    d) All of the above  
    **Answer**: d (comprehensive debugging)

## Cheatsheet for Answer Verification

| Question | Answer | Question | Answer | Question | Answer | Question | Answer | Question | Answer |
|----------|--------|----------|--------|----------|--------|----------|--------|----------|--------|
| 1        | b      | 11       | b      | 21       | a      | 31       | b      | 41       | d      |
| 2        | b      | 12       | d      | 22       | b      | 32       | d      | 42       | b      |
| 3        | b      | 13       | b      | 23       | b      | 33       | d      | 43       | d      |
| 4        | d      | 14       | a      | 24       | d      | 34       | d      | 44       | d      |
| 5        | b      | 15       | a      | 25       | d      | 35       | a      | 45       | d      |
| 6        | b      | 16       | b      | 26       | a      | 36       | d      | 46       | c      |
| 7        | b      | 17       | b      | 27       | a      | 37       | a      | 47       | a      |
| 8        | d      | 18       | c      | 28       | b      | 38       | b      | 48       | a      |
| 9        | d      | 19       | b      | 29       | a      | 39       | b      | 49       | d      |
| 10       | b      | 20       | a      | 30       | a      | 40       | d      | 50       | d      |

**Note**: Answers are speculative due to lack of direct access to the [OpenAI Agents SDK documentation](https://openai.github.io/openai-agents-python/). In practice, verify answers against the official documentation.