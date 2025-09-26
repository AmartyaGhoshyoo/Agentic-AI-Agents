
from agents import Agent,ModelSettings, function_tool,Runner
@function_tool
def get_weather(city:str)->str:
    return f'The weather in the {city} is sunny'

agent=Agent(
    name="Haiku Agent",
    instructions="Always respond in haiku form",
    model='gpt-4.1-mini',
    tools=[get_weather]
)
async def main():
    result=await Runner.run(agent, "Tell me weather in chittagong")
    print(dir(result))
    print(result.final_output )
if __name__=='__main__':
    import asyncio
    asyncio.run(main())
