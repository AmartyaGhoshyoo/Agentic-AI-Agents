'''
NOTE: Not working with custom implementation

'''


from ast import Pass
from agents.memory.session import SessionABC
from agents.items import TResponseInputItem
from typing import List
import os
from mem0 import Memory
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
        "provider": "chroma",
        "config": {
            "collection_name": "test",
            "path": "OpenAI-Mem0-db",
            # Optional: ChromaDB Cloud configuration
            # "api_key": "your-chroma-cloud-api-key",
            # "tenant": "your-chroma-cloud-tenant-id",
        }
    },
            "embedder": {
        "provider": "openai",
        "config": {
            "model": "text-embedding-3-small"
        }
    }
}
m=Memory.from_config(config)
class MyCustomSession(SessionABC):
    def __init__(self,session_id:str):
        self.session_id=session_id
        
    async def get_items(self,limit:int| None=None) -> List[TResponseInputItem]:
        result=m.get(agent_id=self.session_id)
        return result
    async def add_items(self, items: List[TResponseInputItem]) -> None:
        Pass
        
