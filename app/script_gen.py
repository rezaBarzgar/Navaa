# app/script_gen.py

import os
from dotenv import load_dotenv
from openai import OpenAI

# Load env and init client
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_script(english_text: str) -> str:
    """
    Take the English key-concepts and produce a flowing, conversational
    podcast script in PERSIAN. The script should include an intro, a
    body covering each point, and a conclusion.
    """
    messages = [
        dict(role="system", content=(
            "You are an expert podcast writer. "
            "add interesting, correct information to the key concepts."
            "Write engaging podcast scripts in Persian (Farsi)."
            "your answer is going to use as a script for a text to speech model. avoid any tags like [music] or [host]"
        )),
        {
            "role": "user",
            "content": (
                f"Here are the key concepts in English:\n\n{english_text}\n\n"
                "Now draft a Persian podcast script (~300–500 words) "
                "with an introduction, body, and conclusion, in a warm, "
                "conversational tone."
                "your answer is going to use as a script for a text to speech model. avoid any tags like [music] or [host]"
            )
        }
    ]

    response = client.chat.completions.create(
        model="gpt-4.1-mini",   # or "gpt-4" if available
        messages=messages,
        temperature=0.7,
        max_tokens=1500
    )
    return response.choices[0].message.content.strip()


if __name__ == "__main__":
    # Quick test of the script generator
    sample_concepts = (
        "The importance of sleep; tips for better rest; "
        "how to track your sleep quality."
    )
    generated = generate_script(sample_concepts)
    print("📝 Generated Podcast Script (Persian):\n")
    print(generated)