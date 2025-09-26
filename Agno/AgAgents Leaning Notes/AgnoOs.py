from dotenv import load_dotenv
from agno.agent import Agent
from agno.db.sqlite import SqliteDb
from agno.models.openai import OpenAIChat
from agno.os import AgentOS
from agno.tools.mcp import MCPTools
import os
load_dotenv()
# os.environ['OPENAI_API_KEY']=os.getenv("OPENAI_API_KEY")
agno_agent=Agent(
    name="Agno Agent",
    model=OpenAIChat(id='gpt-4.1-nano'),
    db=SqliteDb(db_file='tmp3/agno.db'),
    tools=[MCPTools(transport="streamable-http", url="https://docs.agno.com/mcp")],
    add_history_to_context=True,
    markdown=True,
    
    
)
agent_os=AgentOS(agents=[agno_agent])
app=agent_os.get_app()
if __name__ == "__main__":
    # Default port is 7777; change with port=...
    agent_os.serve(app="AgnoOs:app", reload=True)