'''
Agno is a python framework for building multi-agent systems with shared memory,
knowledge and reasoning.
Shared memory in Agno means multiple agents (not just one) can access and update the same memory space so they can collaborate and build on each other’s work.

Why needed? In multi-agent setups, you might have:
    A data retriever agent,
    A reasoning/planner agent,
    An execution agent.

    If each kept its own memory, they’d work in silos. Shared memory lets them see the same facts and history.
What it stores: User facts, previous steps, tool outputs, conclusions, decisions, etc.
How it’s different from simple memory: Simple memory is private to one agent. Shared memory is global or scoped to a team of agents.

Example flow:
    Agent A (Research) finds: “The YOLOv5 server needs GPU.” → stores in shared memory.
    Agent B (Deployment) reads it and decides to launch a GPU-backed EC2 instance.
    Agent C (Reporter) uses the same memory to explain the plan to the user.
In Agno, shared memory is typically implemented via a database, vector store, or in-memory store (Redis) that all agents can read/write.
'''
import os
from dotenv import load_dotenv
load_dotenv()
from agno.agent import Agent
from agno.models.anthropic import Claude
from agno.models.google import Gemini
from agno.tools.reasoning import ReasoningTools
from agno.tools.yfinance import YFinanceTools
# os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")
reasoning_agent=Agent(
    model=Gemini(id='gemini-2.5-flash'),
    # model=Claude(id="claude-sonnet-4-20250514"),
    tools=[
        ReasoningTools(add_instructions=True),
        YFinanceTools(stock_price=True,analyst_recommendations=True,company_info=True,company_news=True),
        
    ],
    instructions="Use tables to dsiplay data",
    markdown=True,
    debug_mode=True,
    )

reasoning_agent.print_response('What is the stock price of Apple?',stream=True)

'''
TERMINAL 

DEBUG **** Agent ID: 3926f977-d17d-4b1c-aba2-675fc36ffb0f ****              
DEBUG *** Session ID: 000e304c-f7ff-4fe8-98d7-8b1250a84bf8 ***              
DEBUG Processing tools for model                                            
DEBUG Added tool think from reasoning_tools                                 
DEBUG Added tool analyze from reasoning_tools                               
DEBUG Added tool get_current_stock_price from yfinance_tools                
DEBUG Added tool get_company_info from yfinance_tools                       
DEBUG Added tool get_analyst_recommendations from yfinance_tools            
DEBUG Added tool get_company_news from yfinance_tools                       
DEBUG  Agent Run Start: bc187310-d889-49bd-aa2d-ec03700c0795 *              
DEBUG ------------- Google Response Stream Start -------------              
DEBUG --------------- Model: gemini-2.5-flash ----------------              
DEBUG ======================== system ========================              
DEBUG <instructions>                                                        
      Use tables to dsiplay data                                            
      </instructions>                                                       
                                                                            
      <additional_information>                                              
      - Use markdown to format your answers.                                
      </additional_information>                                             
                                                                            
      <reasoning_instructions>                                              
      You have access to the `think` and `analyze` tools to work through    
      problems step-by-step and structure your thought process. You must    
      ALWAYS `think` before making tool calls or generating a response.     
                                                                            
      1. **Think** (scratchpad):                                            
          - Purpose: Use the `think` tool as a scratchpad to break down     
      complex problems, outline steps, and decide on immediate actions      
      within your reasoning flow. Use this to structure your internal       
      monologue.                                                            
          - Usage: Call `think` before making tool calls or generating a    
      response. Explain your reasoning and specify the intended action      
      (e.g., "make a tool call", "perform calculation", "ask clarifying     
      question").                                                           
                                                                            
      2. **Analyze** (evaluation):                                          
          - Purpose: Evaluate the result of a think step or a set of tool   
      calls. Assess if the result is expected, sufficient, or requires      
      further investigation.                                                
          - Usage: Call `analyze` after a set of tool calls. Determine the  
      `next_action` based on your analysis: `continue` (more reasoning      
      needed), `validate` (seek external confirmation/validation if         
      possible), or `final_answer` (ready to conclude).                     
          - Explain your reasoning highlighting whether the result is       
      correct/sufficient.                                                   
                                                                            
      ## IMPORTANT GUIDELINES                                               
      - **Always Think First:** You MUST use the `think` tool before making 
      tool calls or generating a response.                                  
      - **Iterate to Solve:** Use the `think` and `analyze` tools           
      iteratively to build a clear reasoning path. The typical flow is      
      `Think` -> [`Tool Calls` if needed] -> [`Analyze` if needed] -> ... ->
      `final_answer`. Repeat this cycle until you reach a satisfactory      
      conclusion.                                                           
      - **Make multiple tool calls in parallel:** After a `think` step, you 
      can make multiple tool calls in parallel.                             
      - **Keep Thoughts Internal:** The reasoning steps (thoughts and       
      analyses) are for your internal process only. Do not share them       
      directly with the user.                                               
      - **Conclude Clearly:** When your analysis determines the             
      `next_action` is `final_answer`, provide a concise and accurate final 
      answer to the user.                                                   
      </reasoning_instructions>                                             
DEBUG ========================= user =========================              
DEBUG What is the stock price of Apple?                                     
DEBUG ====================== assistant =======================              
DEBUG Tool Calls:                                                           
        - ID: '1d5d8ee7-6357-4e6f-9b45-ff902fb00ba9'                        
          Name: 'get_current_stock_price'                                   
          Arguments: 'symbol: AAPL'                                         
DEBUG **********************  METRICS  ***********************              
DEBUG * Tokens:                      input=1104, output=60, total=1164      
DEBUG * Time:                        2.4083s                                
DEBUG * Tokens per second:           24.9136 tokens/s                       
DEBUG * Time to first token:         2.4077s                                
DEBUG **********************  METRICS  ***********************              
DEBUG Running: get_current_stock_price(symbol=AAPL)                         
DEBUG Fetching current price for AAPL                                       
DEBUG ========================= tool =========================              
DEBUG Tool call Id: 1d5d8ee7-6357-4e6f-9b45-ff902fb00ba9                    
DEBUG 230.4900                                                              
DEBUG ********************  TOOL METRICS  ********************              
DEBUG * Time:                        0.9099s                                             
DEBUG ***************************  TOOL METRICS  **************************              
DEBUG ============================= assistant =============================              
DEBUG Tool Calls:                                                                        
        - ID: '1350ca16-9088-42fc-a100-137bd03da68c'                                     
          Name: 'think'                                                                  
          Arguments: 'thought: The user asked for the stock price of Apple. I have       
      successfully retrieved the current stock price for AAPL., title: Initial Stock     
      Price Retrieval, confidence: 1, action: Present the stock price to the user.'      
DEBUG *****************************  METRICS  *****************************              
DEBUG * Tokens:                      input=1149, output=57, total=1206                   
DEBUG * Time:                        1.0734s                                             
DEBUG * Tokens per second:           53.1003 tokens/s                                    
DEBUG * Time to first token:         1.0713s                                             
DEBUG *****************************  METRICS  *****************************              
DEBUG Running: think(...)                                                                
DEBUG Thought about Initial Stock Price Retrieval                                        
DEBUG ================================ tool ===============================              
DEBUG Tool call Id: 1350ca16-9088-42fc-a100-137bd03da68c                                 
DEBUG Step 1:                                                                            
      Title: Initial Stock Price Retrieval                                               
      Reasoning: The user asked for the stock price of Apple. I have successfully        
      retrieved the current stock price for AAPL.                                        
      Action: Present the stock price to the user.                                       
      Confidence: 1.0                                                                    
DEBUG ***************************  TOOL METRICS  **************************              
DEBUG * Time:                        0.0056s                                             
DEBUG ***************************  TOOL METRICS  **************************              
DEBUG ============================= assistant =============================              
DEBUG Tool Calls:                                                                        
        - ID: '50235c5b-fc2f-433b-ae83-6b70012430b8'                                     
          Name: 'analyze'                                                                
          Arguments: 'result: Stock price for Apple (AAPL) is $230.49, next_action:      
      final_answer, analysis: The stock price has been successfully retrieved. I can now 
      present the information to the user as a final answer., title: Analyze Stock Price 
      Retrieval'                                                                         
DEBUG *****************************  METRICS  *****************************              
DEBUG * Tokens:                      input=1274, output=69, total=1343                   
DEBUG * Time:                        1.4744s                                             
DEBUG * Tokens per second:           46.8000 tokens/s                                    
DEBUG * Time to first token:         1.4696s                                             
DEBUG *****************************  METRICS  *****************************              
DEBUG Running: analyze(...)                                                              
DEBUG Analyzed Analyze Stock Price Retrieval                                             
DEBUG ================================ tool ===============================              
DEBUG Tool call Id: 50235c5b-fc2f-433b-ae83-6b70012430b8                                 
DEBUG Step 1:                                                                            
      Title: Initial Stock Price Retrieval                                               
      Reasoning: The user asked for the stock price of Apple. I have successfully        
      retrieved the current stock price for AAPL.                                        
      Action: Present the stock price to the user.                                       
      Confidence: 1.0                                                                    
                                                                                         
      Step 2:                                                                            
      Title: Analyze Stock Price Retrieval                                               
      Reasoning: The stock price has been successfully retrieved. I can now present the  
      information to the user as a final answer.                                         
      Action: None                                                                       
      Confidence: 0.8                                                                    
DEBUG ***************************  TOOL METRICS  **************************              
DEBUG * Time:                        0.0052s                                             
DEBUG ***************************  TOOL METRICS  **************************              
DEBUG ============================= assistant =============================              
DEBUG The current stock price of Apple (AAPL) is $230.49.                                
DEBUG *****************************  METRICS  *****************************              
DEBUG * Tokens:                      input=1465, output=18, total=1483                   
DEBUG * Time:                        0.8507s                                             
DEBUG * Tokens per second:           21.1600 tokens/s                                    
DEBUG * Time to first token:         0.7036s                                             
DEBUG *****************************  METRICS  *****************************              
DEBUG --------------------- Google Response Stream End --------------------              
DEBUG Added RunResponse to Memory                                                        
DEBUG ******** Agent Run End: bc187310-d889-49bd-aa2d-ec03700c0795 ********              
┏━ Message ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                                                                                       ┃
┃ What is the stock price of Apple?                                                     ┃
┃                                                                                       ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
┏━ Reasoning step 1 ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                                                                                       ┃
┃ Initial Stock Price Retrieval                                                         ┃
┃ Action: Present the stock price to the user.                                          ┃
┃                                                                                       ┃
┃                                                                                       ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
┏━ Reasoning step 2 ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                                                                                       ┃
┃ Analyze Stock Price Retrieval                                                         ┃
┃ Stock price for Apple (AAPL) is $230.49                                               ┃
┃                                                                                       ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
┏━ Tool Calls ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                                                                                       ┃
┃ • get_current_stock_price(symbol=AAPL)                                                ┃
┃ • think(thought=The user asked for the stock price of Apple. I have successfully      ┃
┃ retrieved the current stock price for AAPL., title=Initial Stock Price Retrieval,     ┃
┃ confidence=1, action=Present the stock price to the user.)                            ┃
┃ • analyze(result=Stock price for Apple (AAPL) is $230.49, next_action=final_answer,   ┃
┃ analysis=The stock price has been successfully retrieved. I can now present the       ┃
┃ information to the user as a final answer., title=Analyze Stock Price Retrieval)      ┃
┃                                                                                       ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
┏━ Response (6.9s) ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                                                                                       ┃
┃ The current stock price of Apple (AAPL) is $230.49.                                   ┃
┃                                                                                       ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛


'''
'''
What are Agents?
Agents are AI programs that operate autonomously.

Traditional software follows a pre-programmed sequence of steps. Agents dynamically determine their course of action using a machine learning model, its core components are:
Model: controls the flow of execution. It decides whether to reason, act or respond.
Tools: enable an Agent to take actions and interact with external systems.
Instructions: are how we program the Agent, teaching it how to use tools and respond.
Agents also have memory, knowledge, storage and the ability to reason:
Reasoning: enables Agents to “think” before responding and “analyze” the results of their actions (i.e. tool calls), this improves reliability and quality of responses.
Knowledge: is domain-specific information that the Agent can search at runtime to make better decisions and provide accurate responses (RAG). Knowledge is stored in a vector database and this search at runtime pattern is known as Agentic RAG/Agentic Search.
Storage: is used by Agents to save session history and state in a database. Model APIs are stateless and storage enables us to continue conversations from where they left off. This makes Agents stateful, enabling multi-turn, long-term conversations.
Memory: gives Agents the ability to store and recall information from previous interactions, allowing them to learn user preferences and personalize their responses.


'''