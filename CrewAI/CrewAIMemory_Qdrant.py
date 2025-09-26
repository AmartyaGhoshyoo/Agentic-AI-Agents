'''
NOTE: Qdrant external memory not working

'''

import os
from dotenv import load_dotenv
from mem0 import Memory
from crewai import Crew, Agent, Task, Process, LLM
from crewai_tools import SerperDevTool
from crewai.memory.external.external_memory import ExternalMemory
from crewai.memory.short_term.short_term_memory import ShortTermMemory
from crewai.memory.entity.entity_memory import EntityMemory
load_dotenv()
# os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')
os.environ['SERPER_API_KEY'] = os.getenv("SERPER_API_KEY")
# llm = LLM(model='gemini/gemini-2.0-flash',api_key="AIzaSyD9CBRZy58wV8_s6Qzw9FDkCXSOsmxbVTI")
llm=LLM(model='gpt-4.1-mini')
# config = {
#     "llm": {
#         "provider": "openai",
#         "config": {
#             "model": "gpt-4.1-mini",
#             "temperature": 0.2,
#             "max_tokens": 2000,
#         }
#     },
#     "vector_store": {
#         "provider": "qdrant",
#         "config": {
#             "collection_name": "CrewAI",
#             "host": "localhost",
#             "port": 6333,
#         }
#     },
#     "embedder": {
#         "provider": "openai",
#         "config": {
#             "model": "text-embedding-3-small"
#         }
#     }
# }
external_memory = ExternalMemory(
    embedder_config={
        "provider": "mem0",
        "config": {
            "user_id": "john",
            "local_mem0_config": {
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
            "collection_name": "CrewAI_2",
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
            },
            "infer": True 
        },
    }
)
# mem0_oss_embedder_config={
#         "provider": "mem0",
#         "config": {
#             "user_id": "Henry",
#             "local_mem0_config": {
#     "llm": {
#         "provider": "gemini",
#         "config": {
#             "model": "gemini-2.0-flash-001",
#             "temperature": 0.2,
#             "max_tokens": 2000,
#             "api_key":"AIzaSyD9CBRZy58wV8_s6Qzw9FDkCXSOsmxbVTI"
#         }
#     },
#     "vector_store": {
#         "provider": "qdrant",
#         "config": {
#             "collection_name": "CrewAI",
#             "host": "0.0.0.0",
#             "port": 6333,
#         }
#     },
#     "embedder": {
#         "provider": "gemini",
#         "config": {
#             "model": "models/text-embedding-004",
#             "api_key":"AIzaSyD9CBRZy58wV8_s6Qzw9FDkCXSOsmxbVTI"
#         }
#     }
#             },
#             "infer":True # Optional defaults to True
#         },
#     }

# # m = Memory.from_config(config)
# short_term_memory_mem0_oss = ShortTermMemory(embedder_config=mem0_oss_embedder_config) # Short Term Memory with Mem0 OSS
# entity_memory_mem0_oss = EntityMemory(embedder_config=mem0_oss_embedder_config) # Entity Memory with Mem0 OSS

def create_travel_agent():
    search_tool = SerperDevTool()
    return Agent(
        role="Personalized Travel Planner Agent",
        goal="Plan personalized travel itineraries",
        backstory=(
            "You are a seasoned travel planner, known for your meticulous attention "
            "to detail. You suggest places to visit, stay, and eat based on the user's needs."
        ),
        allow_delegation=False, 
        llm=llm,
        verbose=True,
        tools=[search_tool],
    )
def create_planning_task(agent, destination: str):
    return Task(
        description=f"Find places to live, eat, and visit in {destination}.",
        expected_output=f"A detailed list of places to live, eat, and visit in {destination}.",
        agent=agent,
    )
def setup_crew(agents: list, tasks: list):
    return Crew(
        agents=agents,
        tasks=tasks,
        # memory=True,
        # short_term_memory=short_term_memory_mem0_oss, # or short_term_memory_mem0_client
        # entity_memory=entity_memory_mem0_oss, # or entity_memory_mem0_client
        process=Process.sequential,
        external_memory=external_memory,
        verbose=True,
    )

def plan_trip(destination: str):
    travel_agent = create_travel_agent()
    planning_task = create_planning_task(travel_agent, destination)
    crew = setup_crew([travel_agent], [planning_task])
    return crew.kickoff()

if __name__ == "__main__":
    result = plan_trip("San Francisco")
    print("Final result:\n", result)
