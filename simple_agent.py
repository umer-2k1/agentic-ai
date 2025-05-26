from langchain.tools import Tool
from langchain.agents import initialize_agent, AgentType
from langchain_groq import ChatGroq
import os


os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGSMITH_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = os.getenv("LANGSMITH_TRACING_V2", "true")
os.environ["LANGCHAIN_PROJECT"] = os.getenv("LANGSMITH_PROJECT")

llm = ChatGroq(model="meta-llama/llama-4-scout-17b-16e-instruct")


def calculator_tool(input: str) -> str:
    try:
        return str(eval(input))
    except Exception as e:
        return f"Error: {str(e)}"

def weather_tool(input: str) -> str:
    city = input.strip()
    return f"The temperature in {city} is 18°C."  # Hardcoded for demo

def search_tool(input: str) -> str:
    return f"Search results for '{input}': LangChain is a framework for developing LLM-powered apps."



tools = [
    Tool(
        name="Calculator",
        func=calculator_tool,
        description="Useful for solving math expressions. Input should be a valid Python expression like '3 * 5'."
    ),
    Tool(
        name="Weather",
        func=weather_tool,
        description="Gives current temperature of a city. Input should be a city name like 'London'."
    ),
    Tool(
        name="Search",
        func=search_tool,
        description="Search general knowledge queries."
    ),
]


agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
)

print(agent.run("What is 3 times the temperature in Paris right now?"))