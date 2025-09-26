import asyncio
from agents import Agent, Runner
from agents.extensions.memory.sqlalchemy_session import SQLAlchemySession
from sqlalchemy.ext.asyncio import create_async_engine

engine = create_async_engine(
    "postgresql+asyncpg://agentuser:agentpass@localhost:5432/agents"
)
async def main(message):
    # In your application, you would use your existing engine

    agent = Agent("Assistant")
    session = SQLAlchemySession(
        "user-456",
        engine=engine,
        create_tables=True,  # Auto-create tables for the demo
    )

    result = await Runner.run(agent,message, session=session)
    print("Bot: ",result.final_output)

if __name__ == "__main__":
    while True:
        query=input('User: ')
        asyncio.run(main(query))
        if query=='exit':
            break
    
    
    
#     import asyncio
# from agents import Agent, Runner
# from agents.extensions.memory.sqlalchemy_session import SQLAlchemySession
# from sqlalchemy.ext.asyncio import create_async_engine

# async def main():
#     # Connect to PostgreSQL running in Docker
#     engine = create_async_engine(
#         "postgresql+asyncpg://agentuser:agentpass@localhost:5432/agents"
#     )

#     agent = Agent("Assistant")
#     session = SQLAlchemySession(
#         "user-123",
#         engine=engine,
#         create_tables=True,  # Auto-create the tables if they don't exist
#     )

#     result = await Runner.run(agent, "Hello, remember me?", session=session)
#     print(result.final_output)

#     # Clean up
#     await engine.dispose()

# if __name__ == "__main__":
#     asyncio.run(main())
