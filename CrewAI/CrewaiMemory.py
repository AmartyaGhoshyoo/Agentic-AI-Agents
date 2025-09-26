import os
from dotenv import load_dotenv
from mem0 import Memory
from crewai import Crew, Agent, Task, Process, LLM
from crewai_tools import SerperDevTool
from crewai.memory.external.external_memory import ExternalMemory
load_dotenv()
# os.environ['GOOGLE_API_KEY'] = os.getenv('GOOGLE_API_KEY')
# os.environ['CREWAI_DISABLE_TELEMETRY'] = 'true'
os.makedirs('CrewAI_Storage',exist_ok=True)
os.environ["CREWAI_STORAGE_DIR"] = "CrewAI_Storage"

os.environ['SERPER_API_KEY'] = os.getenv("SERPER_API_KEY")
# llm = LLM(model='gemini/gemini-2.0-flash',api_key="AIzaSyD9CBRZy58wV8_s6Qzw9FDkCXSOsmxbVTI")
llm=LLM(model='gpt-4.1-mini')

def create_travel_agent():
    search_tool = SerperDevTool()
    return Agent(
        role="Personalized Travel Planner Agent",
        goal="Plan personalized travel itineraries, if you already have the information , don't search again directly put that",
        backstory=(
            "You are a seasoned travel planner, known for your meticulous attention "
            "to detail. You suggest places to visit, stay, and eat based on the user's needs"
            "You have the access to the memory"
        ),
        memory=True,
        allow_delegation=False,   # ✅ Enable memory
        llm=llm,
        verbose=True,
        tools=[search_tool],
    )
def create_planning_task(agent, destination: str):
    return Task(
        description=f"Find places to live, eat, and visit in {destination}.",
        expected_output=f"A detailed list of places to live, eat, and visit in {destination}. **IMPORTANT Don't search again if you already have the information on ",
        agent=agent,
    )
def setup_crew(agents: list, tasks: list):
    return Crew(
        agents=agents,
        tasks=tasks,
        # memory=True,
        # external_memory=external_memory, # Separate from basic memory
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
        memory=True,
        # process=Process.sequential,
    embedder={
        "provider": "openai",
        "config": {
            "model": "text-embedding-3-small"  # or "text-embedding-3-large"
        }
    },
    # },
        verbose=True,
        
    )
def plan_trip(destination: str):
    travel_agent = create_travel_agent()
    planning_task = create_planning_task(travel_agent, destination)
    crew = setup_crew([travel_agent], [planning_task])
    return crew.kickoff()

if __name__ == "__main__":
    result = plan_trip("san franscio")
    print("Final result:\n", result)


# from google import genai

# client = genai.Client(api_key="AIzaSyD9CBRZy58wV8_s6Qzw9FDkCXSOsmxbVTI")

# response = client.models.generate_content(
#     model="gemini-2.5-flash",
#     contents="Explain how AI works in a few words",
    
# )
# print(response.text)