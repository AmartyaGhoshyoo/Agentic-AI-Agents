
from json import load
import os
from pathlib import Path
from typing import Optional 
# from agno.agent import Agent
from agents import Agent,Runner
# from agno.media import Image
# from agno.models.openai import OpenAIChat
from mem0 import MemoryClient
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
            "collection_name": "Openai_test",
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
# m=Memory.from_config(config)
m=MemoryClient()
agent = Agent(
    name="Personal Agent",
    model='gpt-4.1-nano',
    instructions="Reply Very concisely",

)

async def chat_user(
    user_input: Optional[str]=None, 

    user_id: str= 'Amartya',
    
    
)->str:

    if user_input:
        memories = m.search(user_input, user_id=user_id)
        memory_context = "\n".join(f"- {m['memory']}" for m in memories['results'])
        prompt = f"""
                Here is what I remember about the user:
                {memory_context}

                User question:
                {user_input}
                """
         # Store the interaction in memory
        result=await Runner.run(agent,prompt)
        interaction_message = [{"role": "user", "content": f"User: {user_input}\nAssistant: {result.final_output}"}]
        m.add(interaction_message, user_id=user_id)
        return result.final_output           
    return "No user input "

import asyncio
while True:
    query=input('Bot: ')
    response=asyncio.run(chat_user(
        query,user_id='Amartya'
    ))
    print('Bot: ',response)
    
    


