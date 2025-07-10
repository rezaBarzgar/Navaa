# main.py

import os
import gradio as gr
from app.pipeline import generate_podcast_from_audio

OUTPUT_DIR = "assets/outputs"
os.makedirs(OUTPUT_DIR, exist_ok=True)


def process_audio(input_audio):
    # input_audio is now a filepath
    input_path = input_audio

    # define output
    output_path = os.path.join(OUTPUT_DIR, "podcast.wav")

    # run pipeline
    generate_podcast_from_audio(input_path, output_path)

    return output_path


iface = gr.Interface(
    fn=process_audio,
    inputs=gr.Audio(label="Upload Persian Voice Note", type="filepath"),
    outputs=gr.Audio(label="Generated Podcast", type="filepath"),
    title="Navaa: Persian Podcast Generator",
    description="Upload a Persian voice note; Navaa will transcribe, translate, script, and synthesize a polished Persian podcast.",
)

if __name__ == "__main__":
    iface.launch(share=True)
