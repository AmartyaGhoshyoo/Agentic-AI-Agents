"""
NOTE: Worked Crewai Chroma memory only
"""


import os
os.environ['CREWAI_DISABLE_TELEMETRY'] = 'true'
os.environ['CREWAI_TELEMETRY_ENABLED'] = 'false'
os.environ['CHROMA_TELEMETRY'] = 'false'
os.environ['OTEL_SDK_DISABLED'] = 'true'
from dotenv import load_dotenv
from mem0 import Memory
from crewai import Crew, Agent, Task, Process, LLM
from crewai_tools import SerperDevTool
from crewai.memory.external.external_memory import ExternalMemory
load_dotenv()
os.makedirs('CrewAI_Storage',exist_ok=True)
os.environ["CREWAI_STORAGE_DIR"] = "CrewAI_Storage"
from crewai.utilities.paths import db_storage_path
storage_path = db_storage_path()
print(f"CrewAI storage location: {storage_path}")

# List all CrewAI storage directories
if os.path.exists(storage_path):
    print("\nStored files and directories:")
    for item in os.listdir(storage_path):
        item_path = os.path.join(storage_path, item)
        if os.path.isdir(item_path):
            print(f"📁 {item}/")
            # Show ChromaDB collections
            if os.path.exists(item_path):
                for subitem in os.listdir(item_path):
                    print(f"   └── {subitem}")
        else:
            print(f"📄 {item}")
else:
    print("No CrewAI storage directory found yet.")
os.environ['SERPER_API_KEY'] = os.getenv("SERPER_API_KEY")
# llm = LLM(model='gemini/gemini-2.0-flash',api_key="AIzaSyD9CBRZy58wV8_s6Qzw9FDkCXSOsmxbVTI")
llm=LLM(model='gpt-4.1-mini')

def create_travel_agent():
    search_tool = SerperDevTool()
    return Agent(
        role="Personalized Travel Planner Agent",
        goal="Plan personalized travel itineraries, if you already have the information in your external memory , don't search again directly put that",
        backstory=(
            "You are a seasoned travel planner, known for your meticulous attention "
            "to detail. You suggest places to visit, stay, and eat based on the user's needs"
            "You have the access to the memory, if you can't retrive anything then search websites"
        ),
        memory=True,
        allow_delegation=False,   # ✅ Enable memory
        llm=llm,
        verbose=True,
        tools=[search_tool],
    )
def create_planning_task(agent, destination: str):
    return Task(
        description=f"Find places to live, eat, and visit in {destination}. **IMPORTANT Don't search again if you already have the information on ",
        expected_output=f"A detailed list of places to live, eat, and visit in {destination}.",
        agent=agent,
    )
def setup_crew(agents: list, tasks: list):
    return Crew(
        agents=agents,
        tasks=tasks,
        memory=True,
    #     memory_config={
    #     "provider": "mem0",
    #     "config": {
    #         "user_id": "john",
    #         "local_mem0_config": {
    # "llm": {
    #     "provider": "gemini",
    #     "config": {
    #         "model": "gemini-2.0-flash-001",
    #         "temperature": 0.2,
    #         "max_tokens": 2000,
    #     }
    # },
    # "vector_store": {
    #     "provider": "chroma",
    #     "config": {
    #         "collection_name": "CrewAI",
    #         "path": "CrewAI_Database",
    #     }
    # },
    # "embedder": {
    #     "provider": "gemini",
    #     "config": {
    #         "model": "models/text-embedding-004"
    #     }
    # }
    #         },
    #         "infer": True # Optional defaults to True
    #     },
    # },
        process=Process.sequential,
    # embedder={
    #     "provider": "openai",
    #     "config": {
    #         "model": "text-embedding-3-small"  # or "text-embedding-3-large"
    #     }
    # },
    # },
        verbose=True,
        
    )
def plan_trip(destination: str):
    travel_agent = create_travel_agent()
    planning_task = create_planning_task(travel_agent, destination)
    crew = setup_crew([travel_agent], [planning_task])
    return crew.kickoff()

if __name__ == "__main__":
    result = plan_trip("san fransisco")
    print("Final result:\n", result)


# from google import genai

# client = genai.Client(api_key="AIzaSyD9CBRZy58wV8_s6Qzw9FDkCXSOsmxbVTI")

# response = client.models.generate_content(
#     model="gemini-2.5-flash",
#     contents="Explain how AI works in a few words",
    
# )
# print(response.text)