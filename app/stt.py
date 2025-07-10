# app/stt.py

import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env
load_dotenv()

# Fetch API key
api_key = os.getenv("OPENAI_API_KEY")
print("🔑 OPENAI_API_KEY loaded:", api_key is not None)

# Initialize the OpenAI client
client = OpenAI(api_key=api_key)
print("🤖 OpenAI client initialized:", hasattr(client, "audio"))

def transcribe_persian(audio_path: str) -> str:
    """
    Transcribe a Persian audio file to text using OpenAI Whisper.
    """
    with open(audio_path, "rb") as audio_file:
        # Use the new client-based interface
        # response_format="text" returns a plain string
        transcript_text = client.audio.transcriptions.create(
            model="whisper-1",
            file=audio_file,
            response_format="text",
            language="fa"
        )
    return transcript_text


if __name__ == "__main__":
    transcript = transcribe_persian("../assets/inputs/Shaab Haye Namaki 2.m4a")
    print("📝 Transcript:\n", transcript)
