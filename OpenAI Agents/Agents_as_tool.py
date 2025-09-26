"""
🔧 Agents as Tools (Manager pattern)

How it works:
The customer-facing agent always talks to the user.
When it needs domain expertise, it calls a tool (which is actually another agent wrapped as a tool).
But the conversation never leaves the customer-facing agent — it just queries sub-agents for help and then responds to the user in its own voice.

When to use:

You want one consistent agent persona that always interacts with the user.

Sub-agents are just “helpers” behind the scenes (they don’t directly interact with the user).

Example: A customer-facing chatbot that always says “Hello! I’ll take care of that,” but internally calls a booking or refund tool.

Good if you want tight control over tone, branding, and flow.

🤝 Handoffs

How it works:
The triage agent starts the conversation.
Once it detects the topic (booking vs refund), it hands off control to the specialized sub-agent.
From then on, the sub-agent directly interacts with the user with its own instructions/personality.

When to use:

You want the specialized agent to fully take over (not just return data).

Each agent has its own distinct voice/personality (e.g., booking agent speaks politely, refund agent is more procedural).

Example: “Triage Agent” greets you → realizes you need a refund → hands you off to the Refund Agent, who then continues the conversation.

Good if you want modularity where agents are like departments in a company, each owning the conversation once engaged.

⚖️ Quick Comparison
Feature	Tools               (Manager)	                            Handoffs
Who talks to the user?	    Always the main agent	                Sub-agent after handoff
Control over tone	        Centralized (one voice)	                Distributed (each agent has its own voice)
Best for	                Single branded assistant with helpers	Modular specialized agents handling entire tasks
Example	Customer chatbot that “uses” booking/refund tools but replies itself	Triage agent routes you to “Booking Dept” or “Refund Dept” and they handle you directly

"""
import asyncio
from agents import Agent,ItemHelpers,MessageOutputItem,Runner,trace
"""
This example shows the agents-as-tools pattern. The frontline agent receives a user message and
then picks which agents to call, as tools. In this case, it picks from a set of translation
agents.
"""

spanish_agent = Agent(
    name="spanish_agent",
    instructions="You translate the user's message to Spanish",
    handoff_description="An english to spanish translator",
)

french_agent = Agent(
    name="french_agent",
    instructions="You translate the user's message to French",
    handoff_description="An english to french translator",
)

italian_agent = Agent(
    name="italian_agent",
    instructions="You translate the user's message to Italian",
    handoff_description="An english to italian translator",
)

orchestrator_agent = Agent(
    name="orchestrator_agent",
    instructions=(
        "You are a translation agent. You use the tools given to you to translate."
        "If asked for multiple translations, you call the relevant tools in order."
        "You never translate on your own, you always use the provided tools."
    ),
    tools=[
        spanish_agent.as_tool(
            tool_name="translate_to_spanish",
            tool_description="Translate the user's message to Spanish",
        ),
        french_agent.as_tool(
            tool_name="translate_to_french",
            tool_description="Translate the user's message to French",
        ),
        italian_agent.as_tool(
            tool_name="translate_to_italian",
            tool_description="Translate the user's message to Italian",
        ),
    ],
)

synthesizer_agent = Agent(
    name="synthesizer_agent",
    instructions="You inspect translations, correct them if needed, and produce a final concatenated response.",
)


async def main():
    msg=input("Hi! What would you like translated, and which languages? ")
    with trace("Orchestrator evaluator"):
        print(orchestrator_agent.model)
        orchestrator_result=await Runner.run(orchestrator_agent,msg)
        for item in orchestrator_result.new_items:
            if isinstance(item,MessageOutputItem):
                text=ItemHelpers.text_message_output(item)
                if text:
                    print(f"  -Translation step: {text}")
        synthesizer_result= await Runner.run(synthesizer_agent,orchestrator_result.to_input_list())
    print(f"\n\nFinal response:\n{synthesizer_result.final_output}")


if __name__=='__main__':
    asyncio.run(main())