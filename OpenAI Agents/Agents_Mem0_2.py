''''
Worked Perfectly
use only for user preferences


'''


from agents.memory.session import SessionABC
from agents import Agent, Runner
from agents.items import TResponseInputItem
from typing import List, Optional
from mem0 import Memory
import asyncio

# Mem0 config
config = {
    "llm": {
        "provider": "openai",
        "config": {
            "model": "gpt-4.1-mini",
            "temperature": 0.2,
            "max_tokens": 2000,
        }
    },
    "vector_store": {
        "provider": "qdrant",
        "config": {
            "collection_name": "Agnetic AI",
            "host": "localhost",
            "port": 6333,
        }
    },
    "embedder": {
        "provider": "openai",
        "config": {
            "model": "text-embedding-3-small"
        }
    }
}

m = Memory.from_config(config)


import os
from agents import Agent, Runner, function_tool





# Define memory tools for the agent
@function_tool
async def search_memory(query: str) -> str:
    """Search through past conversations and memories"""
    memories = m.search(query, user_id='alice',run_id="consultation-001")
    if memories and memories.get('results'):
        return "\n".join([f"- {mem['memory']}" for mem in memories['results']])
    return "No relevant memories found."

@function_tool
async def save_memory(content: str) -> str:
    """Save important information to memory"""
    m.add([{"role": "user", "content": content}], user_id='alice',run_id="consultation-001")
    return "Information saved to memory."

# Create agent with memory capabilities
agent = Agent(
    name="Personal Assistant",
    instructions="""You are a helpful personal assistant with memory capabilities.
    Use the search_memory tool to recall past conversations and user preferences.
    Use the save_memory tool to store important information about the user.
    Always personalize your responses based on available memory.""",
    tools=[search_memory, save_memory],
    model="gpt-4.1-mini",
)

async def chat_with_agent(user_input: str) -> str:
    # Run the agent (it will automatically use memory tools when needed)
    result =await Runner.run(agent, user_input)

    return result.final_output

# Example usaged
if __name__ == "__main__":
    import asyncio
    while True:
        query=input('User: ')
        result=asyncio.run(chat_with_agent(query))
        print(f'Bot: ',result)
        
        

    # memory will be retrieved using search_memory tool to answer the user query
    # response_2 = chat_with_agent(
    #     "what kinda food i like",
    #     user_id="alice"
    # )
    # print(response_2)