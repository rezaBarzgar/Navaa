# app/translator.py

import os
from dotenv import load_dotenv
from openai import OpenAI

# Load .env
load_dotenv()

# Initialize OpenAI client (reuse your API key)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def translate_to_english(persian_text: str) -> str:
    """
    Translate Persian text to English, preserving technical meaning.
    """
    # Build a clear translation prompt
    prompt = (
        "You are a professional translator. "
        "Translate the following Persian text into clear, natural English:\n\n"
        f"{persian_text}\n\n"
        "English translation:"
    )

    # Call the chat completion API
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",      # or "gpt-4" if you have access
        messages=[
            {"role": "system", "content": "You translate Persian to English."},
            {"role": "user",   "content": prompt}
        ],
        temperature=0.0             # deterministic output
    )

    # Extract and return the translation
    return response.choices[0].message.content.strip()


if __name__ == '__main__':
    sample = "این یک متن آزمایشی است."
    result = translate_to_english(sample)
    print("Translation:", result)