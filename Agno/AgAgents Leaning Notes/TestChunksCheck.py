import lancedb
from rich.console import Console
from rich.markdown import Markdown
# open your db
db = lancedb.connect("Agentic -AI- Agents/Agno/AgAgents Leaning Notes/tmp/lancedb")
tbl = db.open_table("agno_docs")

# convert to Arrow to inspect
arrow_tbl = tbl.to_arrow()

# list available column names
print("Columns:", arrow_tbl.column_names)

# show 2 rows so we see the actual data

print(arrow_tbl.slice(0, 2).to_pandas()['payload'][0])
table=arrow_tbl.slice(0, 2).to_pandas()
print(table.columns)
"""

Columns: ['vector', 'id', 'payload']
                                              vector  ...                                            payload
0  [-0.061864853, 0.019188544, 0.038239732, -0.00...  ...  {"name": "llms-full.txt", "meta_data": {"url":...
1  [-0.03169194, -0.0049816864, 0.010063823, -0.0...  ...  {"name": "llms-full.txt", "meta_data": {"url":...




Columns: ['vector', 'id', 'payload']
0    {"name": "llms-full.txt", "meta_data": {"url":...
1    {"name": "llms-full.txt", "meta_data": {"url":...
Name: payload, dtype: object
Index(['vector', 'id', 'payload'], dtype='object')





Columns: ['vector', 'id', 'payload']
{"name": "llms-full.txt", "meta_data": {"url": "https://docs.agno.com/llms-full.txt", "chunk": 1, "chunk_size": 4989}, "content": "# Agent API Source: https://docs.agno.com/agent-api/introduction A robust, production-ready application for serving Agents as an API. Welcome to the Simple Agent API: a robust, production-ready application for serving Agents as an API. It includes: * A FastAPI server for handling API requests. * A PostgreSQL database for storing Agent sessions, knowledge, and memories. * A set of pre-built Agents to use as a starting point. <Snippet file=\"simple-agent-api-setup.mdx\" /> <Snippet file=\"create-simple-agent-api-codebase.mdx\" /> <Snippet file=\"simple-agent-api-dependency-management.mdx\" /> <Snippet file=\"simple-agent-api-production.mdx\" /> ## Additional Information Congratulations on running your Agent API. * Read how to [use workspaces with your Agent API](/workspaces/introduction) # A beautiful UI for your Agents Source: https://docs.agno.com/agent-ui/introduction A beautiful, open-source interface for interacting with AI agents <Frame> <img height=\"200\" src=\"https://mintcdn.com/agno/0omqNXZ9CSqcNU7_/images/agent-ui.png?maxW=1788&auto=format&n=0omqNXZ9CSqcNU7_&q=85&s=2ac21c49e63cb721e47d850de3a16dfa\" style={{ borderRadius: '8px' }} width=\"1788\" height=\"936\" data-path=\"images/agent-ui.png\" srcset=\"https://mintcdn.com/agno/0omqNXZ9CSqcNU7_/images/agent-ui.png?w=280&maxW=1788&auto=format&n=0omqNXZ9CSqcNU7_&q=85&s=19a4278316a2d20edda1955b380f8e94 280w, https://mintcdn.com/agno/0omqNXZ9CSqcNU7_/images/agent-ui.png?w=560&maxW=1788&auto=format&n=0omqNXZ9CSqcNU7_&q=85&s=f24fea4df5b5c48a559d936bd999531f 560w, https://mintcdn.com/agno/0omqNXZ9CSqcNU7_/images/agent-ui.png?w=840&maxW=1788&auto=format&n=0omqNXZ9CSqcNU7_&q=85&s=004ec817fa2c1109af208e54f536cbf8 840w, https://mintcdn.com/agno/0omqNXZ9CSqcNU7_/images/agent-ui.png?w=1100&maxW=1788&auto=format&n=0omqNXZ9CSqcNU7_&q=85&s=edfbc774026679322648cec6c31d84ce 1100w, https://mintcdn.com/agno/0omqNXZ9CSqcNU7_/images/agent-ui.png?w=1650&maxW=1788&auto=format&n=0omqNXZ9CSqcNU7_&q=85&s=516418b211c22f73945a3f0a15cf2620 1650w, https://mintcdn.com/agno/0omqNXZ9CSqcNU7_/images/agent-ui.png?w=2500&maxW=1788&auto=format&n=0omqNXZ9CSqcNU7_&q=85&s=33b3c7a3ca53ad48163efb2c56cc9692 2500w\" data-optimize=\"true\" data-opv=\"2\" /> </Frame> Agno provides a beautiful UI for interacting with your agents, completely open source, free to use and build on top of. It's a simple interface that allows you to chat with your agents, view their memory, knowledge, and more. <Note> No data is sent to [agno.com](https://app.agno.com), all agent data is stored locally in your sqlite database. </Note> The Open Source Agent UI is built with Next.js and TypeScript. After the success of the [Agent Playground](/introduction/playground), the community asked for a self-hosted alternative and we delivered! # Get Started with Agent UI To clone the Agent UI, run the following command in your terminal: ```bash npx create-agent-ui@latest ``` Enter `y` to create a new project, install dependencies, then run the agent-ui using: ```bash cd agent-ui && npm run dev ``` Open [http://localhost:3000](http://localhost:3000) to view the Agent UI, but remember to connect to your local agents. <Frame> <img height=\"200\" src=\"https://mintcdn.com/agno/0omqNXZ9CSqcNU7_/images/agent-ui-homepage.png?maxW=2892&auto=format&n=0omqNXZ9CSqcNU7_&q=85&s=daebe1abaf86b143c9cfcabaf32a7a72\" style={{ borderRadius: '8px' }} width=\"2892\" height=\"1616\" data-path=\"images/agent-ui-homepage.png\" srcset=\"https://mintcdn.com/agno/0omqNXZ9CSqcNU7_/images/agent-ui-homepage.png?w=280&maxW=2892&auto=format&n=0omqNXZ9CSqcNU7_&q=85&s=4e507b28e357108977ea5ffe5de0ef2b 280w, https://mintcdn.com/agno/0omqNXZ9CSqcNU7_/images/agent-ui-homepage.png?w=560&maxW=2892&auto=format&n=0omqNXZ9CSqcNU7_&q=85&s=debd33c21875cada22a9f272c627da4a 560w, https://mintcdn.com/agno/0omqNXZ9CSqcNU7_/images/agent-ui-homepage.png?w=840&maxW=2892&auto=format&n=0omqNXZ9CSqcNU7_&q=85&s=cf0784f29a9fc9ec6b10279019afaa7a 840w, https://mintcdn.com/agno/0omqNXZ9CSqcNU7_/images/agent-ui-homepage.png?w=1100&maxW=2892&auto=format&n=0omqNXZ9CSqcNU7_&q=85&s=08fa68e1460a9405ffd1d0d48c34559e 1100w, https://mintcdn.com/agno/0omqNXZ9CSqcNU7_/images/agent-ui-homepage.png?w=1650&maxW=2892&auto=format&n=0omqNXZ9CSqcNU7_&q=85&s=d3476ca56a89baa19999f0d51cda38a4 1650w, https://mintcdn.com/agno/0omqNXZ9CSqcNU7_/images/agent-ui-homepage.png?w=2500&maxW=2892&auto=format&n=0omqNXZ9CSqcNU7_&q=85&s=548c52a4ae23591081f6124b93791804 2500w\" data-optimize=\"true\" data-opv=\"2\" /> </Frame> <br /> <Accordion title=\"Clone the repository manually\" icon=\"github\"> You can also clone the repository manually ```bash git clone https://github.com/agno-agi/agent-ui.git ``` And run the agent-ui using ```bash cd agent-ui && pnpm install && pnpm dev ``` </Accordion> ## Connect to Local Agents The Agent UI needs to connect to a playground server, which you can run locally or on any cloud provider. Let's start with a local playground server. Create a file `playground.py` ```python playground.py from agno.agent import Agent from", "usage": {"prompt_tokens": 1769, "total_tokens": 1769}}
Index(['vector', 'id', 'payload'], dtype='object')



"""