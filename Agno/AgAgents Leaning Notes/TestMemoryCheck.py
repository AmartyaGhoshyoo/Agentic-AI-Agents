from agno.agent import Agent
from agno.memory.v2.db.sqlite import SqliteMemoryDb
from agno.memory.v2.memory import Memory
from agno.models.openai import OpenAIChat
from agno.storage.sqlite import SqliteStorage
from rich.pretty import pprint
from dotenv import load_dotenv
import os 
load_dotenv()
os.environ['OPENAI_API_KEY']=os.getenv('OPENAI_API_KEY')

# UserId for the memories
user_id = "ava"
# Database file for memory and storage
db_file = "tmp/agent.db"

# Initialize memory.v2
memory = Memory(
    # Use any model for creating memories
    model=OpenAIChat(id="gpt-4.1"),
    db=SqliteMemoryDb(table_name="user_memories", db_file=db_file),
)
# Initialize storage
storage = SqliteStorage(table_name="agent_sessions", db_file=db_file)

# Initialize Agent
memory_agent = Agent(
    model=OpenAIChat(id="gpt-4.1"),
    # Store memories in a database
    memory=memory,
    # Give the Agent the ability to update memories
    enable_agentic_memory=True,
    # OR - Run the MemoryManager after each response
    enable_user_memories=True,
    # Store the chat history in the database
    storage=storage,
    # Add the chat history to the messages
    add_history_to_messages=True,
    # Number of history runs
    num_history_runs=3,
    markdown=True,
)

memory.clear()
memory_agent.print_response(
    "My name is Ava and I like to ski.",
    user_id=user_id,
    stream=True,
    stream_intermediate_steps=True,
)
print("Memories about Ava:")
pprint(memory.get_user_memories(user_id=user_id))

memory_agent.print_response(
    "I live in san francisco, where should i move within a 4 hour drive?",
    user_id=user_id,
    stream=True,
    stream_intermediate_steps=True,
)
print("Memories about Ava:")
pprint(memory.get_user_memories(user_id=user_id))



"""
┏━ Message ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                                                                           ┃
┃ My name is Ava and I like to ski.                                         ┃
┃                                                                           ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
┏━ Tool Calls ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                                                                           ┃
┃ • update_user_memory(task=Add a memory that the user's name is Ava and    ┃
┃ she likes to ski.)                                                        ┃
┃                                                                           ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
┏━ Response (7.6s) ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                                                                           ┃
┃ Thanks for sharing, Ava! I've noted that you like to ski. If there's      ┃
┃ anything else you'd like me to remember, just let me know! ⛷️              ┃
┃                                                                           ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
Memories about Ava:
[
│   UserMemory(
│   │   memory="User's name is Ava.",
│   │   topics=['name'],
│   │   input="Add a memory that the user's name is Ava and she likes to ski.",
│   │   last_updated=datetime.datetime(2025, 8, 29, 14, 12, 42, 161187),
│   │   memory_id='4f5cdead-fe66-4e60-94e6-f1482dcf60c1'
│   ),
│   UserMemory(
│   │   memory='Ava likes to ski.',
│   │   topics=['interests', 'hobbies'],
│   │   input="Add a memory that the user's name is Ava and she likes to ski.",
│   │   last_updated=datetime.datetime(2025, 8, 29, 14, 12, 42, 167994),
│   │   memory_id='eeca4499-b874-4e38-b804-6b2484b820fa'
│   )
]
┏━ Message ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                                                                           ┃
┃ I live in san francisco, where should i move within a 4 hour drive?       ┃
┃                                                                           ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
┏━ Response (9.0s) ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                                                                           ┃
┃ That’s a great question, Ava! Here are some fantastic places you can      ┃
┃ consider moving to within a 4-hour drive from San Francisco, catering to  ┃
┃ different lifestyles and interests—including your love for skiing:        ┃
┃                                                                           ┃
┃                               1. Lake Tahoe                               ┃
┃                                                                           ┃
┃  • Why: World-class skiing in the winter (Heavenly, Squaw Valley,         ┃
┃    Northstar), beautiful lake and hiking in the summer.                   ┃
┃  • Vibe: Mountain/lake town, outdoor adventure, ski community.            ┃
┃                                                                           ┃
┃                               2. Sacramento                               ┃
┃                                                                           ┃
┃  • Why: State capital, growing food scene, more affordable than SF, close ┃
┃    to Tahoe for skiing.                                                   ┃
┃  • Vibe: Urban/suburban with easy access to nature and wine country.      ┃
┃                                                                           ┃
┃                               3. Santa Cruz                               ┃
┃                                                                           ┃
┃  • Why: Surf town with a laid-back vibe, redwood forests, and a cool      ┃
┃    coastal climate.                                                       ┃
┃  • Vibe: Beachy, artsy, outdoorsy.                                        ┃
┃                                                                           ┃
┃                            4. Monterey/Carmel                             ┃
┃                                                                           ┃
┃  • Why: Gorgeous coastline, golf, artist communities, great food.         ┃
┃  • Vibe: Upscale coastal living, relaxed pace.                            ┃
┃                                                                           ┃
┃                              5. Napa Valley                               ┃
┃                                                                           ┃
┃  • Why: World-famous wine country, beautiful rolling hills, sophisticated ┃
┃    small towns (e.g., St. Helena, Yountville).                            ┃
┃  • Vibe: Wine lovers, foodies, scenic countryside.                        ┃
┃                                                                           ┃
┃                 6. Sonoma County (Healdsburg, Sebastopol)                 ┃
┃                                                                           ┃
┃  • Why: Similar wine country feel as Napa, but a bit more rustic and      ┃
┃    laid-back.                                                             ┃
┃  • Vibe: Farm-to-table living, wine, and outdoor recreation.              ┃
┃                                                                           ┃
┃                        7. Nevada City/Grass Valley                        ┃
┃                                                                           ┃
┃  • Why: Historic Gold Rush towns with charming downtowns, access to       ┃
┃    skiing in the Sierra, great for arts and festivals.                    ┃
┃  • Vibe: Quirky, artsy, forested foothills.                               ┃
┃                                                                           ┃
┃ ───────────────────────────────────────────────────────────────────────── ┃
┃ If skiing is your main priority, Lake Tahoe (especially the North         ┃
┃ Shore—Truckee, Tahoe City) is the best choice. If you love the coast,     ┃
┃ Santa Cruz or Monterey/Carmel might be ideal.                             ┃
┃                                                                           ┃
┃ Let me know what kind of vibe or lifestyle you’re looking for, and I can  ┃
┃ help narrow it down!                                                      ┃
┃                                                                           ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
Memories about Ava:
[
│   UserMemory(
│   │   memory='Ava lives in San Francisco.',
│   │   topics=['location'],
│   │   input='I live in san francisco, where should i move within a 4 hour drive?',
│   │   last_updated=datetime.datetime(2025, 8, 29, 14, 12, 55, 261794),
│   │   memory_id='95487bc4-93e7-4955-8ad6-538836bc25db'
│   ),
│   UserMemory(
│   │   memory="User's name is Ava.",
│   │   topics=['name'],
│   │   input="Add a memory that the user's name is Ava and she likes to ski.",
│   │   last_updated=datetime.datetime(2025, 8, 29, 14, 12, 42, 161187),
│   │   memory_id='4f5cdead-fe66-4e60-94e6-f1482dcf60c1'
│   ),
│   UserMemory(
│   │   memory='Ava likes to ski.',
│   │   topics=['interests', 'hobbies'],
│   │   input="Add a memory that the user's name is Ava and she likes to ski.",
│   │   last_updated=datetime.datetime(2025, 8, 29, 14, 12, 42, 167994),
│   │   memory_id='eeca4499-b874-4e38-b804-6b2484b820fa'
│   )
]

"""