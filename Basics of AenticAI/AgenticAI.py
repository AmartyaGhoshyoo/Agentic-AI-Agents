# Rag only used to augment the data from the knowledge base but here Agentic ai do task automatically make decision
# Rag works on defined pipeline, like we have to explicitly define how we want to retreive(vectorDB.as_retriever()) and it can't do by itself we also have to give the embedding and then only it will able to fetch relevant data from the vectordatabase
"""
 RAG, which typically relies on pre-existing data (such as a vector database) and uses embeddings for document retrieval,
 Agentic AI can autonomously decide when to use a tool like a web search API to gather real-time information.
 
 It can make decision which agent to call for the query given and retrive data ,it can use multiple subagents to retrieve data, handles more complext workflow
 We don't have to manually invoke any tools , where in RAG we are performing one specific task that is retrieve relevant data from the vectorDB with embeddings
 but in AgenticAI , agents can automatically decide which subagent to call and retrieve data even without embedding like normal keyword based searches,It can also work with vector embeddings if we create such agent with the tools 
 In RAG it will only perform how it is defined , can't make any decision based on the query, suppose for an great example if we give a query it will go and search vectordatabase where we saved the data from the webiste using web scrapper or maybe uploaded data except this it can't do anything 
 but in AgenticAI , it is built in such a way it understands the query and calls the agents like searching web sites or maybe vectorDB by itself and fetchs data and gets summarize response using model in itself, no human interpretion like in RAG we need to mannually store data in vectorDB then only it can fetch ,
 but here we just declare the agents , and it will automatically understand and works based on the query , In Rag there is no such option that it can work like that way
 
 to conclusion if a query needs real time data RAG can't fetch from website by itself ,it only depends on the pre-existing database and unless we update that vector database manually, 
 where as Agentic ai does it automatically no human interpretation 
 
# Agentic AI 
 
Relation Between Tools, Agent, and Model
Model (Brain 🧠)

The core intelligence that understands, reasons, and generates responses.
Example: Gemini, GPT-4, LLaMA.
Without a model, the agent has no intelligence.
Agent (Orchestrator 🤖)

Manages interactions between the model and tools.
Decides when to use a tool and when to rely on the model’s own knowledge.
Example: phi.agent.Agent.
Tools (External Helpers 🔧)

API calls, databases, or functions the agent can use to fetch real-time data.
Example: Google Search API, NewsAPI, Database Query Function.
The agent must be programmed to call tools when needed.

Breakdown of How It Works
1️⃣ User asks a question → The agent passes it to the model.
2️⃣ Model decides:

If it knows the answer, it responds without using tools.
If it realizes it needs external data, it triggers the agent to call a tool.
3️⃣ Agent executes the tool call and returns the response to the model.
4️⃣ Model processes the tool’s output and formats the final answer for the user.
Why Won’t the Agent Use Tools Automatically?
❌ The agent does not force tool execution. It simply waits for the model’s decision.
✅ If the model fails to recognize the need for tools, the agent remains idle.

This is why some Gemini models fail to use tools—they don’t "realize" they should!

How They Work Together
Agent takes input → Model processes or decides if a tool is needed → Agent calls the tool if necessary → Final response is generated.
🔹 The agent does not make the decision on its own.
🔹 It waits for the model's response to determine whether a tool should be used.
🔹 If the model requests a tool, the agent executes it and returns the result.
""" 

from phi.agent import Agent  # Phidata is a Python framework designed for building data and AI applications. It helps in managing data workflows, machine learning models, and cloud infrastructure.
from phi.model.groq import Groq # this Groq offer open source model libraries with limited calls 
from phi.tools.yfinance import YFinanceTools # interacting with the stock
from phi.tools.duckduckgo import DuckDuckGo # Serach in the web
from dotenv import load_dotenv
import os 
load_dotenv()
Groq.api_key=os.getenv("GROQ_API_KEY")
# Web Search Agent 
web_search_agent=Agent(
    name="Web Search Agent", # Name of the agent 
    role="Search the web for the infromation",# It gets concatenate with the query 
    model=Groq(id='llama-3.1-8b-instant'),# the model which will generate the response , Groq provides this free open source models
    tools=[DuckDuckGo()],# we can give mutliple web search tools , so when we give any query it takes the query and concatenate with role and tool gets the result from the web search, and fed into the model
    instructions=["Always include the sources"],
    show_tool_calls=True, # Show tools that are basically used show in the terminal what tools are being used 
    markdown=True,
)

# Agentic AI
finance_agent=Agent(
    name='Finance Agent',
    model=Groq(id="llama-3.1-8b-instant"),
    tools=[
        YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True,company_news=True)
    ],    
    instructions=["Use tables to display the data"],
    show_tool_calls=True,
    markdown=True,
)

# Combining the agents
"""
Here this multiagent decide which subagents to call or it can call both of them if needed based on the query ,
so what happens here based on the query if both the agent gets called then web searching will take the query +role+toolsduckduckgo) response+ instruction then feed it in it's own model to get an response 
same for the Yfinance generates response 
the those response are conactenate together and feed again to the multiagent model to yeild more generous or effective response 

"""
multi_ai_agent=Agent(
    team=[web_search_agent,finance_agent],
    instructions=['Always include the sources','Use table to display the data'],
    model=Groq(id='llama-3.1-8b-instant'),
    show_tool_calls=True,
    markdown=True,
)
# msg=input("Enter your query: ")
multi_ai_agent.print_response('Delhi news today',stream=True)

"""
    MORE CLEAR KNOWLEDGE ABOUT RAG AND AGENTIC AI
    
    RAG (Retrieval-Augmented Generation):
Manual Data Storage:

In RAG, you need to manually store data in a vector database (like FAISS or Pinecone) before you can perform retrieval. This data could be pre-processed, like from web scraping or uploading files.
The retrieval process works by converting both the query and the stored data into embeddings and searching for the most relevant matches. The retrieved data is then used to augment the generation process.
Specific Data Usage:

RAG is typically more task-specific. It operates in environments where the data has been pre-organized and embedded. For example, if you're searching for documents on a particular subject (like medical texts or financial data), those documents need to be pre-stored and indexed in the vector database.
This can limit the system to specific topics or datasets unless you continuously expand the vector database with new data.
Limited to Pre-Stored Data:

The system can only retrieve what has already been indexed in the vector database. If the data isn't there, the system can’t fetch it, meaning it can't handle broad queries or real-time data retrieval (like the latest news) unless explicitly provided in the database.
Agentic AI:
Dynamic Tool Usage:

Agentic AI doesn’t rely on a fixed vector database or pre-stored data. Instead, it uses agents and tools that can access real-time data from multiple sources like web search tools, APIs, and databases.
For example, agents like the web_search_agent can autonomously query the web using tools like DuckDuckGo, Google, or other sources. It can also make use of specialized agents for tasks like stock price retrieval or weather forecasting.
Broader and Flexible:

Agentic AI is much more flexible and adaptable. It doesn't need data to be stored in a vector database beforehand. The agents can call on tools for real-time data retrieval, allowing it to access a wide variety of sources and handle broader tasks. For example, one agent might use a web search tool, while another agent fetches financial data, and yet another pulls information from a knowledge base or API.
It can handle varied, real-time queries, making it much more versatile and not restricted to pre-encoded data or embeddings.
Autonomous Decision-Making:

Agentic AI can autonomously decide which agent or tool to invoke depending on the task. For instance, if the user query is about stock prices, the finance_agent might be invoked. If it's a general knowledge query, the web_search_agent might be triggered.
It is not restricted to querying a fixed dataset; instead, it adapts by leveraging the right tool for the right task at the moment.
Key Differences:
Data Source:

RAG relies on pre-processed and indexed data in a vector database (embedding-based search).
Agentic AI can access real-time data from multiple sources via agents and tools (e.g., web search, APIs, databases).
Flexibility:

RAG is typically narrower in scope, as it depends on data that has been specifically uploaded and stored.
Agentic AI is broader in scope, with the ability to retrieve data from varied sources as needed, allowing it to handle more diverse and dynamic queries.
Autonomy:

RAG requires a manual setup of data storage and indexing.
Agentic AI can automatically decide which tools or agents to use for a given query, making it more autonomous and adaptive.
Conclusion:
RAG is ideal for tasks where you have a specific, fixed dataset that needs to be queried repeatedly, like a knowledge base or specialized corpus.
Agentic AI, on the other hand, is much more dynamic, allowing for real-time, flexible queries across a broad range of topics and tools. It doesn't require pre-indexing or fixed datasets, and it can autonomously decide which tool or agent to invoke to handle various tasks.
Thus, while RAG operates within the confines of a pre-stored, indexed dataset, Agentic AI is far more adaptive and resourceful, able to pull in data from a wide variety of sources as needed.
    
    
    
    
    """
    
