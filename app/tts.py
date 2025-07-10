# app/tts.py

import os
from dotenv import load_dotenv
from openai import OpenAI

# Load .env and initialize OpenAI client
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_audio(text: str, output_path: str, voice: str = "alloy") -> str:
    """
    Synthesize the given Persian script into a WAV audio file at output_path
    using OpenAI’s Text-to-Speech API.
    """
    model = "gpt-4o-mini-tts"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Stream the TTS response into the file
    with client.audio.speech.with_streaming_response.create(
        model="gpt-4o-mini-tts",
        voice=voice,
        input=text,
        response_format="mp3"
    ) as response:
        response.stream_to_file(output_path+f"_{model}_{voice}.mp3")

    return output_path

if __name__ == "__main__":
    sample = "سلام! این یک تست صدا است."
    out = "../assets/outputs/test_navaa_openai"
    print("Generating…")
    path = generate_audio(sample, out)
    print(f"✅ Generated OpenAI TTS audio at: {path}")
