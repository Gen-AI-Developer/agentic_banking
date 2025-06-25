from agents import Agent, Runner, function_tool, set_tracing_disabled
from openai.types.responses import ResponseTextDeltaEvent
from agents.extensions.models.litellm_model import LitellmModel
from agents.tracing.processor_interface import TracingProcessor
import os
import asyncio
api_key = os.getenv("GEMINI_API_KEY")  
set_tracing_disabled(disabled=True)

class CustomTracingProcessor(TracingProcessor):
    """Custom tracing processor that implements the TracingProcessor interface."""
    def __init__(self):
        self.name = "CustomTracingProcessor"
        self.traces =[]
        self.spans=[]
    
    def __repr__(self):
        return f"CustomTracingProcessor(name={self.name})"

    def on_trace_start(self, trace):
        print(f"Trace started: {trace} with id {trace.id} and name {trace.name}")
        self.traces.append(trace)

    def on_trace_end(self, trace):
        print(f"Trace ended: {trace}")

    def on_span_start(self, span):
        print(f"Span started: {span}")

    def on_span_end(self, span):
        print(f"Span ended: {span}")

    def shutdown(self):
        print("Shutting down tracing processor")

    def force_flush(self):
        print("Forcing flush of spans/traces")

async def main():
    print("Welcome to AI")
    agent = Agent(
        name="Assistant",
        instructions="You are a helpfull assistant",
        model=LitellmModel(model="gemini/gemini-2.0-flash", api_key=api_key,),
    )
    result = Runner.run_streamed(agent, "what is today date?")
    async for event in result.stream_events:
        if event.type == "raw_response_event" and isinstance(event.data, ResponseTextDeltaEvent):
            print(event.raw_response, end="", flush=True)
        pass

    print("Goodbye from ai!")

if __name__ == "__main__":
    asyncio.run(main())