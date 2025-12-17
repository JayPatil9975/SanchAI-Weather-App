from langchain_openai import ChatOpenAI
from langchain.agents import initialize_agent, AgentType
from app.tools import get_weather
from app.config import OPENROUTER_API_KEY, OPENROUTER_MODEL

llm = ChatOpenAI(
    api_key=OPENROUTER_API_KEY,
    base_url="https://openrouter.ai/api/v1",
    model=OPENROUTER_MODEL,
)

agent = initialize_agent(
    tools=[get_weather],
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
)

def ask_weather_agent(query: str) -> str:
    return agent.run(query)
