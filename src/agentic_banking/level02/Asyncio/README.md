### Materail To Check
1) [Python Async | Asynchronous IO Introduction
](https://www.youtube.com/watch?v=7LU1npoPmcg&ab_channel=VeryAcademy)
2) [AsyncIO and the Event Loop Explained
](https://www.youtube.com/watch?v=RIVcqT2OGPA&ab_channel=ArjanCodes)
3) [a-conceptual-overview-of-asyncio/readme.md at main · anordin95/a-conceptual-overview-of-asyncio
](https://github.com/anordin95/a-conceptual-overview-of-asyncio/tree/main)
4) [Learn Python's AsyncIO in 15 minutes
](https://www.youtube.com/watch?v=0GVLtTnebNA&ab_channel=Indently)
5) [Everything You Ever Wanted to Know About Asyncio | Asyncio That Just Makes Sense Pt 1
](https://www.youtube.com/watch?v=WYfzG3AdAzA&ab_channel=Don%27tUseThisCode%E2%80%A2JamesPowell)
1) [https://www.youtube.com/watch?v=Zag5wqLDorg&ab_channel=Don%27tUseThisCode%E2%80%A2JamesPowell](https://www.youtube.com/watch?v=Zag5wqLDorg&ab_channel=Don%27tUseThisCode%E2%80%A2JamesPowell)
2) [RealPython-Asyncio](https://realpython.com/async-io-python/)


### Key Points 
1) Runner.run_sync() in OpenAI Agents SDK is a blocking function. It runs the agent workflow synchronously in the main thread, preventing the asyncio event loop from processing other tasks until it completes. This can block the event loop if called within an async context without offloading (e.g., via loop.run_in_executor). For non-blocking execution, use Runner.run() or Runner.run_streamed() with await in an async function.
2) 