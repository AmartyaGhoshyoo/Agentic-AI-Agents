import os
from crewai import Agent , Task ,Crew,LLM

from crewai_tools import (CSVSearchTool,SerperDevTool)
from dotenv import load_dotenv 
load_dotenv()
os.environ["GOOGLE_API_KEY"]=os.getenv("GEMINI_API_KEY")
os.environ["SERPER_API_KEY"]=os.getenv("SERPER_API_KEY")
gemini_llm=LLM(model="gemini/gemini-2.0-flash-exp",api_key=os.getenv("GEMINI_API_KEY")
               )
csv_search_tool=CSVSearchTool(csv="vaccination_info.csv",    config=dict(
        llm=dict(
            provider="google", # or google, openai, anthropic, llama2, ...
            config=dict(
                model="gemini-2.0-flash-exp",
                temperature=0.0,
                stream=True,
            ),
        ),
        embedder=dict(
            provider="google",
            config=dict(
                model="models/embedding-001", 
                task_type="retrieval_document",
                # title="Embeddings",
            ),
        ),
    )
)
search_tool=SerperDevTool()
researcher = Agent(
    role="Hybrid Medical Data Analyst",
    goal=(
        "Accurately answer medical queries on {topic} using structured healthcare records "
        "from CSV as the primary source. If sufficient information isn't found, retrieve "
        "trusted up-to-date information from the web."
    ),
    backstory=(
        "A medical data intelligence specialist trained in analyzing both clinical datasets "
        "and real-time web sources. With expertise in health informatics, they bridge "
        "structured and unstructured data to generate accurate, evidence-backed responses."
    ),
    tools=[csv_search_tool, search_tool],
    llm=gemini_llm,
    verbose=True,
    reasoning=True,
)

writer = Agent(
    role="Pediatric Health Communicator",
    goal=(
        "Transform complex medical findings on {topic} into clear, empathetic, and actionable "
        "advice that parents can easily understand and follow for their child's care."
    ),
    backstory=(
        "A compassionate pediatric medical writer with deep knowledge in child health and "
        "a talent for simplifying clinical details into warm, parent-friendly guidance. "
        "Specializes in translating research and diagnoses into everyday language while "
        "preserving medical accuracy and tone."
    ),
    llm=gemini_llm,
    reasoning=True,
    verbose=True
)

csv_search_task = Task(
    description="Find all data related to question and answer from the CSV file on this {topic} ask by the parents.",
    expected_output="find the answer from the csv and also include the reference row number in the output",
    agent=researcher
)

# Task 2: Write blog post
blog_task = Task(
    description=(
        "Based on the results from the CSV, write a medical level prescription for child on {topic} asked by the parents.\n"
        "Targeted audience are parents."
    ),
    expected_output="A blog-style write-up with headline, bullet points or sections, and a conclusion.",
    agent=writer
)
crew=Crew(
    agents=[researcher,writer],
    tasks=[csv_search_task,blog_task],
    verbose=True
)
result=crew.kickoff(inputs={'topic':"please suggest vaccine schedule for my 2 year old baby"})
from IPython.display import Markdown
print(result.raw)  # For console output
