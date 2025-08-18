"""Utilities for translating Persian text to English using LangGraph."""

from typing import TypedDict
from dotenv import load_dotenv
from langgraph.graph import StateGraph, START, END
from langchain_openai import ChatOpenAI

# Load environment variables
load_dotenv()

# Define the state for the translation graph
class TranslationState(TypedDict):
    persian_text: str
    english_text: str

# Initialize model using LangChain's OpenAI wrapper
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.0)

def _translate(state: TranslationState) -> TranslationState:
    """LangGraph node to translate Persian to English."""
    prompt = (
        "You are a professional translator. "
        "Translate the following Persian text into clear, natural English:\n\n"
        f"{state['persian_text']}\n\n"
        "English translation:"
    )
    result = llm.invoke(prompt)
    return {"english_text": result.content.strip(), "persian_text": state["persian_text"]}

# Build the translation graph
builder = StateGraph(TranslationState)
builder.add_node("translator", _translate)
builder.add_edge(START, "translator")
builder.add_edge("translator", END)
translation_graph = builder.compile()

def translate_to_english(persian_text: str) -> str:
    """Translate Persian text to English using the LangGraph pipeline."""
    final_state = translation_graph.invoke({"persian_text": persian_text})
    return final_state["english_text"]


if __name__ == "__main__":
    sample = "این یک متن آزمایشی است."
    result = translate_to_english(sample)
    print("Translation:", result)
