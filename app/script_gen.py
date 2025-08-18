"""Generate podcast scripts in Persian using LangGraph."""

from typing import TypedDict
from dotenv import load_dotenv
from langgraph.graph import StateGraph, START, END
from langchain_openai import ChatOpenAI

# Load environment variables
load_dotenv()

class ScriptState(TypedDict):
    english_text: str
    script_text: str

llm = ChatOpenAI(model="gpt-4.1-mini", temperature=0.7)

def _write_script(state: ScriptState) -> ScriptState:
    """LangGraph node to expand English concepts into a Persian script."""
    prompt = (
        "You are an expert podcast writer. add interesting, correct information to the key concepts. "
        "Write engaging podcast scripts in Persian (Farsi). "
        "Your answer is going to be used as a script for a text to speech model. Avoid any tags like [music] or [host].\n\n"
        f"Here are the key concepts in English:\n\n{state['english_text']}\n\n"
        "Now draft a Persian podcast script (~300–500 words) with an introduction, body, and conclusion, in a warm, conversational tone."
    )
    result = llm.invoke(prompt)
    return {"script_text": result.content.strip(), "english_text": state["english_text"]}

# Build the script-generation graph
builder = StateGraph(ScriptState)
builder.add_node("writer", _write_script)
builder.add_edge(START, "writer")
builder.add_edge("writer", END)
script_graph = builder.compile()

def generate_script(english_text: str) -> str:
    """Generate a Persian podcast script from English key concepts."""
    final_state = script_graph.invoke({"english_text": english_text})
    return final_state["script_text"]


if __name__ == "__main__":
    sample_concepts = (
        "The importance of sleep; tips for better rest; how to track your sleep quality."
    )
    generated = generate_script(sample_concepts)
    print("📝 Generated Podcast Script (Persian):\n")
    print(generated)
