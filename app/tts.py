# app/tts.py

import os
from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs

# Load .env and initialize ElevenLabs client
load_dotenv()
client = ElevenLabs(api_key=os.getenv("ELEVENLABS_API_KEY"))

def generate_audio(text: str, output_path: str, voice_id: str = "cgSgspJ2msm6clMCkdW9") -> str:
    """
    Synthesize Persian script to an MP3 file using ElevenLabs’ TTS API.
    """
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # This returns a generator of byte-chunks
    audio_stream = client.text_to_speech.convert(
        text=text,
        voice_id=voice_id,
        model_id="eleven_multilingual_v2",
        output_format="mp3_44100_128"
    )

    # Stream the chunks into the output file
    with open(output_path, "wb") as f:
        for chunk in audio_stream:
            f.write(chunk)

    return output_path

if __name__ == "__main__":
    sample = "سلام! این یک تست تولید پادکست با صدای الون لبز است."
    out = "../assets/outputs/test_navaa_eleven.mp3"
    path = generate_audio(sample, out)
    print(f"✅ Generated ElevenLabs audio at: {path}")
