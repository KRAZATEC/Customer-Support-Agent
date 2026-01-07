from typing import TypedDict
from langchain_groq import ChatGroq
from langgraph.graph import StateGraph, END

class AgentState(TypedDict):
    user_input: str
    sentiment: str
    response: str

def build_agent(groq_api_key: str):

    llm = ChatGroq(
        groq_api_key=groq_api_key,
        model_name="llama-3.1-8b-instant"
    )

    # -------- Nodes --------

    def analyze_sentiment(state: AgentState):
        sentiment = llm.invoke(
            f"Analyze sentiment (positive, neutral, negative): {state['user_input']}"
        ).content
        return {"sentiment": sentiment}

    def generate_response(state: AgentState):
        response = llm.invoke(
            f"""
            You are a professional customer support agent.
            User sentiment: {state['sentiment']}
            User query: {state['user_input']}
            Answer clearly and helpfully.
            """
        ).content
        return {"response": response}

    # -------- Graph --------

    builder = StateGraph(AgentState)
    builder.add_node("sentiment", analyze_sentiment)
    builder.add_node("response", generate_response)

    builder.set_entry_point("sentiment")
    builder.add_edge("sentiment", "response")
    builder.add_edge("response", END)

    return builder.compile()
