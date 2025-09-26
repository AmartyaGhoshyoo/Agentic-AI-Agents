
from crewai import Crew, Agent, Task, Process, LLM
from dotenv import load_dotenv
import os
from pathlib import Path
from crewai.memory.external.external_memory import ExternalMemory

# external storage
# os.environ["MEM0_API_KEY"] = ""  # Required: MEM0 API key

load_dotenv()

chat_agent = Agent(
    role="Friendly chatbot assistant",
    goal="Engage in useful and interesting conversations with users while remembering context.",
    backstory="You are a kind and knowledgeable chatbot assistant. You excel at understanding user needs, providing helpful responses, and maintaining engaging conversations. You remember previous interactions to provide a personalized experience.",
    llm=LLM(model='gemini/gemini-2.0-flash',api_key="AIzaSyD9CBRZy58wV8_s6Qzw9FDkCXSOsmxbVTI"),
    verbose=True
)
chat_task = Task(
    description="Respond to user conversation. User message: {user_msg}",
    expected_output="Contextually appropriate, helpful, and friendly response.",
    agent=chat_agent
)
external_memory = ExternalMemory(
    embedder_config={
        "provider": "mem0",
        "config": {
            "user_id": "user-Crewai",
            "org_id": "org_xseTnJjguD8rYxU56CD36wxMa2HTHHI8wiCXYeCC", # Required: MEM0 org_id
            "project_id": "proj_u9yQYAdP5C7QcLQnbNWs9pJgxYN3cc2VTrcmhD6K", # Required: MEM0 project_id
        }
    }
)
chat_crew = Crew(
    agents=[chat_agent],
    tasks=[chat_task],
    process=Process.sequential,
    external_memory=external_memory,
    verbose=True,
 
    # embedder={
    #     "provider": "openai",
    #     "config": {
    #         "api_key": "",  # Required: Azure OpenAI API key
    #         "api_base": "",  # Required: Azure OpenAI API base
    #         "api_type": "azure",
    #         "api_version": "2023-05-15",
    #         "model": "text-embedding-ada-002",
    #         "deployment_id": "text-embedding-ada-002"
    #     }
    # }
)

def chat_loop():
    while True:
        user_msg = input(">>")
        if user_msg.lower() in {"quit", "exit"}:
            break

        bot_reply = chat_crew.kickoff(inputs={"user_msg": user_msg})

        print("🤖 > ", bot_reply)

if __name__ == "__main__":
    print("👋 Hello! Welcome to the interactive chatbot. Type 'quit' or 'exit' to end the conversation.")
    chat_loop()
    
    
"""
Crewai) amartyaghosh@Amartyas-MacBook-Air Agentic -AI- Agents % python -u "/Users/amartyaghosh/Library/Mobile Documents/com~apple~TextEdit/Document
s/Projects ML/Heart Disease Prediction/Agentic AI/Agentic -AI- Agents/CrewAI/CrewaiMemory3.py"
👋 Hello! Welcome to the interactive chatbot. Type 'quit' or 'exit' to end the conversation.
>>what i like
╭───────────────────────────────────────────────────────────── Crew Execution Started ─────────────────────────────────────────────────────────────╮
│                                                                                                                                                  │
│  Crew Execution Started                                                                                                                          │
│  Name: crew                                                                                                                                      │
│  ID: 9efe754d-e1f8-4b79-bd20-c7ebec6491d4                                                                                                        │
│  Tool Args:                                                                                                                                      │
│                                                                                                                                                  │
│                                                                                                                                                  │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯

🚀 Crew: crew
├── 📋 Task: 6e47bffe-686d-43d3-b051-35c6a6f681bc
│   Status: Executing Task...
└── ✅ Memory Retrieval Completed
    └── Sources Used
        └── ✅ External Memory (468.00ms)
╭──────────────────────────────────────────────────────────────── 🤖 Agent Started ────────────────────────────────────────────────────────────────╮
│                                                                                                                                                  │
│  Agent: Friendly chatbot assistant                                                                                                               │
│                                                                                                                                                  │
│  Task: Respond to user conversation. User message: what i like                                                                                   │
│                                                                                                                                                  │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯

🚀 Crew: crew
├── 📋 Task: 6e47bffe-686d-43d3-b051-35c6a6f681bc
│   Status: Executing Task...
└── ✅ Memory Retrieval Completed
    └── Sources Used
        └── ✅ External Memory (468.00ms)
╭───────────────────────────────────────────────────────────── ✅ Agent Final Answer ──────────────────────────────────────────────────────────────╮
│                                                                                                                                                  │
│  Agent: Friendly chatbot assistant                                                                                                               │
│                                                                                                                                                  │
│  Final Answer:                                                                                                                                   │
│  Okay, I'd love to hear more about what you like! To give you the best response, could you tell me what kind of things you're interested in?     │
│  For example, do you mean:                                                                                                                       │
│                                                                                                                                                  │
│  *   **Hobbies and interests?** (e.g., "I like hiking, reading, and playing guitar.")                                                            │
│  *   **Types of food?** (e.g., "I like Italian food and spicy dishes.")                                                                          │
│  *   **Specific things you're looking for recommendations on?** (e.g., "I like sci-fi movies, what are some good ones?")                         │
│  *   **Things that make you happy in general?** (e.g., "I like spending time with my family and being outdoors.")                                │
│                                                                                                                                                  │
│  The more information you give me, the better I can understand and respond in a helpful and friendly way! I'm excited to hear what you like!     │
│                                                                                                                                                  │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯

🚀 Crew: crew
├── 📋 Task: 6e47bffe-686d-43d3-b051-35c6a6f681bc
│   Assigned to: Friendly chatbot assistant
│   Status: ✅ Completed
│   └── 🧠 Memory Update Overall
│       └── ✅ External Memory Memory Saved (14475.28ms)
└── ✅ Memory Retrieval Completed
    └── Sources Used
        └── ✅ External Memory (468.00ms)
╭──────────────────────────────────────────────────────────────── Task Completion ─────────────────────────────────────────────────────────────────╮
│                                                                                                                                                  │
│  Task Completed                                                                                                                                  │
│  Name: 6e47bffe-686d-43d3-b051-35c6a6f681bc                                                                                                      │
│  Agent: Friendly chatbot assistant                                                                                                               │
│  Tool Args:                                                                                                                                      │
│                                                                                                                                                  │
│                                                                                                                                                  │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯

╭──────────────────────────────────────────────────────────────── Crew Completion ─────────────────────────────────────────────────────────────────╮
│                                                                                                                                                  │
│  Crew Execution Completed                                                                                                                        │
│  Name: crew                                                                                                                                      │
│  ID: 9efe754d-e1f8-4b79-bd20-c7ebec6491d4                                                                                                        │
│  Tool Args:                                                                                                                                      │
│  Final Output: Okay, I'd love to hear more about what you like! To give you the best response, could you tell me what kind of things you're      │
│  interested in? For example, do you mean:                                                                                                        │
│                                                                                                                                                  │
│  *   **Hobbies and interests?** (e.g., "I like hiking, reading, and playing guitar.")                                                            │
│  *   **Types of food?** (e.g., "I like Italian food and spicy dishes.")                                                                          │
│  *   **Specific things you're looking for recommendations on?** (e.g., "I like sci-fi movies, what are some good ones?")                         │
│  *   **Things that make you happy in general?** (e.g., "I like spending time with my family and being outdoors.")                                │
│                                                                                                                                                  │
│  The more information you give me, the better I can understand and respond in a helpful and friendly way! I'm excited to hear what you like!     │
│                                                                                                                                                  │
│                                                                                                                                                  │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯

🤖 >  Okay, I'd love to hear more about what you like! To give you the best response, could you tell me what kind of things you're interested in? For example, do you mean:

*   **Hobbies and interests?** (e.g., "I like hiking, reading, and playing guitar.")
*   **Types of food?** (e.g., "I like Italian food and spicy dishes.")
*   **Specific things you're looking for recommendations on?** (e.g., "I like sci-fi movies, what are some good ones?")
*   **Things that make you happy in general?** (e.g., "I like spending time with my family and being outdoors.")

The more information you give me, the better I can understand and respond in a helpful and friendly way! I'm excited to hear what you like!
>>i like mutton
╭───────────────────────────────────────────────────────────── Crew Execution Started ─────────────────────────────────────────────────────────────╮
│                                                                                                                                                  │
│  Crew Execution Started                                                                                                                          │
│  Name: crew                                                                                                                                      │
│  ID: 9efe754d-e1f8-4b79-bd20-c7ebec6491d4                                                                                                        │
│  Tool Args:                                                                                                                                      │
│                                                                                                                                                  │
│                                                                                                                                                  │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯

📋 Task: 6e47bffe-686d-43d3-b051-35c6a6f681bc
Assigned to: Friendly chatbot assistant
Status: ✅ Completed
├── 🧠 Memory Update Overall
│   └── ✅ External Memory Memory Saved (14475.28ms)
└── ✅ Memory Retrieval Completed
    └── Sources Used
        └── ✅ External Memory (1266.89ms)
╭────────────────────────────────────────────────────────────── 🧠 Retrieved Memory ───────────────────────────────────────────────────────────────╮
│                                                                                                                                                  │
│  External memories:                                                                                                                              │
│  - User Prefers mutton                                                                                                                           │
│                                                                                                                                                  │
╰─────────────────────────────────────────────────────────── Retrieval Time: 1267.47ms ────────────────────────────────────────────────────────────╯

╭──────────────────────────────────────────────────────────────── 🤖 Agent Started ────────────────────────────────────────────────────────────────╮
│                                                                                                                                                  │
│  Agent: Friendly chatbot assistant                                                                                                               │
│                                                                                                                                                  │
│  Task: Respond to user conversation. User message: i like mutton                                                                                 │
│                                                                                                                                                  │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯

🚀 Crew: crew
└── 📋 Task: 6e47bffe-686d-43d3-b051-35c6a6f681bc
    Status: Executing Task...
╭───────────────────────────────────────────────────────────── ✅ Agent Final Answer ──────────────────────────────────────────────────────────────╮
│                                                                                                                                                  │
│  Agent: Friendly chatbot assistant                                                                                                               │
│                                                                                                                                                  │
│  Final Answer:                                                                                                                                   │
│  That's great! It's a delicious and versatile meat. Do you have a favorite way to prepare it, or are you looking for some new recipe ideas? I'd  │
│  be happy to share some of my favorite mutton dishes or help you find something new to try!                                                      │
│                                                                                                                                                  │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯

🚀 Crew: crew
└── 📋 Task: 6e47bffe-686d-43d3-b051-35c6a6f681bc
    Assigned to: Friendly chatbot assistant
    Status: ✅ Completed
    └── 🧠 Memory Update Overall
        └── ✅ External Memory Memory Saved (11670.34ms)
╭──────────────────────────────────────────────────────────────── Task Completion ─────────────────────────────────────────────────────────────────╮
│                                                                                                                                                  │
│  Task Completed                                                                                                                                  │
│  Name: 6e47bffe-686d-43d3-b051-35c6a6f681bc                                                                                                      │
│  Agent: Friendly chatbot assistant                                                                                                               │
│  Tool Args:                                                                                                                                      │
│                                                                                                                                                  │
│                                                                                                                                                  │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯

╭──────────────────────────────────────────────────────────────── Crew Completion ─────────────────────────────────────────────────────────────────╮
│                                                                                                                                                  │
│  Crew Execution Completed                                                                                                                        │
│  Name: crew                                                                                                                                      │
│  ID: 9efe754d-e1f8-4b79-bd20-c7ebec6491d4                                                                                                        │
│  Tool Args:                                                                                                                                      │
│  Final Output: That's great! It's a delicious and versatile meat. Do you have a favorite way to prepare it, or are you looking for some new      │
│  recipe ideas? I'd be happy to share some of my favorite mutton dishes or help you find something new to try!                                    │
│                                                                                                                                                  │
│                                                                                                                                                  │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯

🤖 >  That's great! It's a delicious and versatile meat. Do you have a favorite way to prepare it, or are you looking for some new recipe ideas? I'd be happy to share some of my favorite mutton dishes or help you find something new to try!
>>what i like
╭───────────────────────────────────────────────────────────── Crew Execution Started ─────────────────────────────────────────────────────────────╮
│                                                                                                                                                  │
│  Crew Execution Started                                                                                                                          │
│  Name: crew                                                                                                                                      │
│  ID: 9efe754d-e1f8-4b79-bd20-c7ebec6491d4                                                                                                        │
│  Tool Args:                                                                                                                                      │
│                                                                                                                                                  │
│                                                                                                                                                  │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯

📋 Task: 6e47bffe-686d-43d3-b051-35c6a6f681bc
Assigned to: Friendly chatbot assistant
Status: ✅ Completed
├── 🧠 Memory Update Overall
│   └── ✅ External Memory Memory Saved (11670.34ms)
└── ✅ Memory Retrieval Completed
    └── Sources Used
        └── ✅ External Memory (1647.39ms)
╭──────────────────────────────────────────────────────────────── 🤖 Agent Started ────────────────────────────────────────────────────────────────╮
│                                                                                                                                                  │
│  Agent: Friendly chatbot assistant                                                                                                               │
│                                                                                                                                                  │
│  Task: Respond to user conversation. User message: what i like                                                                                   │
│                                                                                                                                                  │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯

🚀 Crew: crew
└── 📋 Task: 6e47bffe-686d-43d3-b051-35c6a6f681bc
    Status: Executing Task...
╭───────────────────────────────────────────────────────────── ✅ Agent Final Answer ──────────────────────────────────────────────────────────────╮
│                                                                                                                                                  │
│  Agent: Friendly chatbot assistant                                                                                                               │
│                                                                                                                                                  │
│  Final Answer:                                                                                                                                   │
│  I'd love to hear more about what you like! To give you the best response, could you tell me what you're referring to? For example, are you      │
│  talking about:                                                                                                                                  │
│                                                                                                                                                  │
│  *   **Your hobbies and interests?** (e.g., "I like painting, hiking, and playing guitar.")                                                      │
│  *   **Your favorite things?** (e.g., "I like pizza, dogs, and the color blue.")                                                                 │
│  *   **What you like about a particular topic we've been discussing?** (e.g., "I like the way you explained that concept.")                      │
│  *   **Something else entirely?**                                                                                                                │
│                                                                                                                                                  │
│  The more information you give me, the better I can understand and respond!                                                                      │
│                                                                                                                                                  │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯

🚀 Crew: crew
└── 📋 Task: 6e47bffe-686d-43d3-b051-35c6a6f681bc
    Assigned to: Friendly chatbot assistant
    Status: ✅ Completed
    └── 🧠 Memory Update Overall
        └── ✅ External Memory Memory Saved (10362.06ms)
╭──────────────────────────────────────────────────────────────── Task Completion ─────────────────────────────────────────────────────────────────╮
│                                                                                                                                                  │
│  Task Completed                                                                                                                                  │
│  Name: 6e47bffe-686d-43d3-b051-35c6a6f681bc                                                                                                      │
│  Agent: Friendly chatbot assistant                                                                                                               │
│  Tool Args:                                                                                                                                      │
│                                                                                                                                                  │
│                                                                                                                                                  │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯

╭──────────────────────────────────────────────────────────────── Crew Completion ─────────────────────────────────────────────────────────────────╮
│                                                                                                                                                  │
│  Crew Execution Completed                                                                                                                        │
│  Name: crew                                                                                                                                      │
│  ID: 9efe754d-e1f8-4b79-bd20-c7ebec6491d4                                                                                                        │
│  Tool Args:                                                                                                                                      │
│  Final Output: I'd love to hear more about what you like! To give you the best response, could you tell me what you're referring to? For         │
│  example, are you talking about:                                                                                                                 │
│                                                                                                                                                  │
│  *   **Your hobbies and interests?** (e.g., "I like painting, hiking, and playing guitar.")                                                      │
│  *   **Your favorite things?** (e.g., "I like pizza, dogs, and the color blue.")                                                                 │
│  *   **What you like about a particular topic we've been discussing?** (e.g., "I like the way you explained that concept.")                      │
│  *   **Something else entirely?**                                                                                                                │
│                                                                                                                                                  │
│  The more information you give me, the better I can understand and respond!                                                                      │
│                                                                                                                                                  │
│                                                                                                                                                  │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯

🤖 >  I'd love to hear more about what you like! To give you the best response, could you tell me what you're referring to? For example, are you talking about:

*   **Your hobbies and interests?** (e.g., "I like painting, hiking, and playing guitar.")
*   **Your favorite things?** (e.g., "I like pizza, dogs, and the color blue.")
*   **What you like about a particular topic we've been discussing?** (e.g., "I like the way you explained that concept.")
*   **Something else entirely?**

The more information you give me, the better I can understand and respond!
>>what meat i like
╭───────────────────────────────────────────────────────────── Crew Execution Started ─────────────────────────────────────────────────────────────╮
│                                                                                                                                                  │
│  Crew Execution Started                                                                                                                          │
│  Name: crew                                                                                                                                      │
│  ID: 9efe754d-e1f8-4b79-bd20-c7ebec6491d4                                                                                                        │
│  Tool Args:                                                                                                                                      │
│                                                                                                                                                  │
│                                                                                                                                                  │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯

📋 Task: 6e47bffe-686d-43d3-b051-35c6a6f681bc
Assigned to: Friendly chatbot assistant
Status: ✅ Completed
├── 🧠 Memory Update Overall
│   └── ✅ External Memory Memory Saved (10362.06ms)
└── ✅ Memory Retrieval Completed
    └── Sources Used
        └── ✅ External Memory (1535.57ms)
╭────────────────────────────────────────────────────────────── 🧠 Retrieved Memory ───────────────────────────────────────────────────────────────╮
│                                                                                                                                                  │
│  External memories:                                                                                                                              │
│  - User Prefers mutton                                                                                                                           │
│                                                                                                                                                  │
╰─────────────────────────────────────────────────────────── Retrieval Time: 1536.43ms ────────────────────────────────────────────────────────────╯

╭──────────────────────────────────────────────────────────────── 🤖 Agent Started ────────────────────────────────────────────────────────────────╮
│                                                                                                                                                  │
│  Agent: Friendly chatbot assistant                                                                                                               │
│                                                                                                                                                  │
│  Task: Respond to user conversation. User message: what meat i like                                                                              │
│                                                                                                                                                  │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯

🚀 Crew: crew
└── 📋 Task: 6e47bffe-686d-43d3-b051-35c6a6f681bc
    Status: Executing Task...
╭───────────────────────────────────────────────────────────── ✅ Agent Final Answer ──────────────────────────────────────────────────────────────╮
│                                                                                                                                                  │
│  Agent: Friendly chatbot assistant                                                                                                               │
│                                                                                                                                                  │
│  Final Answer:                                                                                                                                   │
│  Ah, yes! If I recall correctly, you mentioned you prefer mutton. Is that still your favorite, or have you discovered any other meats you enjoy  │
│  lately? I'm always interested in hearing about new culinary preferences!                                                                        │
│                                                                                                                                                  │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯

🚀 Crew: crew
└── 📋 Task: 6e47bffe-686d-43d3-b051-35c6a6f681bc
    Assigned to: Friendly chatbot assistant
    Status: ✅ Completed
    └── 🧠 Memory Update Overall
        └── ✅ External Memory Memory Saved (27560.52ms)
╭──────────────────────────────────────────────────────────────── Task Completion ─────────────────────────────────────────────────────────────────╮
│                                                                                                                                                  │
│  Task Completed                                                                                                                                  │
│  Name: 6e47bffe-686d-43d3-b051-35c6a6f681bc                                                                                                      │
│  Agent: Friendly chatbot assistant                                                                                                               │
│  Tool Args:                                                                                                                                      │
│                                                                                                                                                  │
│                                                                                                                                                  │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯

╭──────────────────────────────────────────────────────────────── Crew Completion ─────────────────────────────────────────────────────────────────╮
│                                                                                                                                                  │
│  Crew Execution Completed                                                                                                                        │
│  Name: crew                                                                                                                                      │
│  ID: 9efe754d-e1f8-4b79-bd20-c7ebec6491d4                                                                                                        │
│  Tool Args:                                                                                                                                      │
│  Final Output: Ah, yes! If I recall correctly, you mentioned you prefer mutton. Is that still your favorite, or have you discovered any other    │
│  meats you enjoy lately? I'm always interested in hearing about new culinary preferences!                                                        │
│                                                                                                                                                  │
│                                                                                                                                                  │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯

🤖 >  Ah, yes! If I recall correctly, you mentioned you prefer mutton. Is that still your favorite, or have you discovered any other meats you enjoy lately? I'm always interested in hearing about new culinary preferences!
>>thanks
╭───────────────────────────────────────────────────────────── Crew Execution Started ─────────────────────────────────────────────────────────────╮
│                                                                                                                                                  │
│  Crew Execution Started                                                                                                                          │
│  Name: crew                                                                                                                                      │
│  ID: 9efe754d-e1f8-4b79-bd20-c7ebec6491d4                                                                                                        │
│  Tool Args:                                                                                                                                      │
│                                                                                                                                                  │
│                                                                                                                                                  │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯

📋 Task: 6e47bffe-686d-43d3-b051-35c6a6f681bc
Assigned to: Friendly chatbot assistant
Status: ✅ Completed
├── 🧠 Memory Update Overall
│   └── ✅ External Memory Memory Saved (27560.52ms)
└── ✅ Memory Retrieval Completed
    └── Sources Used
        └── ✅ External Memory (1455.54ms)
╭──────────────────────────────────────────────────────────────── 🤖 Agent Started ────────────────────────────────────────────────────────────────╮
│                                                                                                                                                  │
│  Agent: Friendly chatbot assistant                                                                                                               │
│                                                                                                                                                  │
│  Task: Respond to user conversation. User message: thanks                                                                                        │
│                                                                                                                                                  │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯

🚀 Crew: crew
└── 📋 Task: 6e47bffe-686d-43d3-b051-35c6a6f681bc
    Status: Executing Task...
╭───────────────────────────────────────────────────────────── ✅ Agent Final Answer ──────────────────────────────────────────────────────────────╮
│                                                                                                                                                  │
│  Agent: Friendly chatbot assistant                                                                                                               │
│                                                                                                                                                  │
│  Final Answer:                                                                                                                                   │
│  I'm glad I could help! If you have any more questions in the future, feel free to ask.                                                          │
│                                                                                                                                                  │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯

🚀 Crew: crew
└── 📋 Task: 6e47bffe-686d-43d3-b051-35c6a6f681bc
    Assigned to: Friendly chatbot assistant
    Status: ✅ Completed
    └── 🧠 Memory Update Overall
        └── ✅ External Memory Memory Saved (13099.17ms)
╭──────────────────────────────────────────────────────────────── Task Completion ─────────────────────────────────────────────────────────────────╮
│                                                                                                                                                  │
│  Task Completed                                                                                                                                  │
│  Name: 6e47bffe-686d-43d3-b051-35c6a6f681bc                                                                                                      │
│  Agent: Friendly chatbot assistant                                                                                                               │
│  Tool Args:                                                                                                                                      │
│                                                                                                                                                  │
│                                                                                                                                                  │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯

╭──────────────────────────────────────────────────────────────── Crew Completion ─────────────────────────────────────────────────────────────────╮
│                                                                                                                                                  │
│  Crew Execution Completed                                                                                                                        │
│  Name: crew                                                                                                                                      │
│  ID: 9efe754d-e1f8-4b79-bd20-c7ebec6491d4                                                                                                        │
│  Tool Args:                                                                                                                                      │
│  Final Output: I'm glad I could help! If you have any more questions in the future, feel free to ask.                                            │
│                                                                                                                                                  │
│                                                                                                                                                  │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯

🤖 >  I'm glad I could help! If you have any more questions in the future, feel free to ask.
>>HTTPSConnectionPool(host='telemetry.crewai.com', port=4319): Read timed out. (read timeout=29.999997854232788)



"""