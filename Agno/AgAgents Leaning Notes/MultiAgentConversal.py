from agno.team import Team
from agno.agent import Agent
from agno.models.openai import OpenAIChat


# Define the main conversational agent
user_agent = Agent(
    name="User Interaction Agent",
    role="Talk with the user, decide whether to answer directly or call another agent",
    model=OpenAIChat(id="gpt-4.1-mini")  # you can replace with another model
)


# Define specialist agents
news_agent = Agent(
    name="News Agent",
    role="Provide the latest news updates",
    model=OpenAIChat(id="gpt-4.1-mini")
)

weather_agent = Agent(
    name="Weather Agent",
    role="Provide the weather forecast for the next 7 days",
    model=OpenAIChat(id="gpt-4.1-mini")
)


# Build a team where the main agent can call others if needed
team = Team(
    name="Conversation Team",
    members=[user_agent, news_agent, weather_agent],
    entry_agent=user_agent,  # Always start with the user-facing agent
)


# Example usage

# Synchronous execution
result = team.run("Can you tell me the weather in Tokyo?")
print(result)

# Asynchronous execution
# (only works inside async functions or event loops)
# result = await team.arun("What is the latest world news?")
# print(result)
