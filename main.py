#!/usr/bin/env python3
import os
import argparse
import logging
from app.stt import transcribe_persian
from app.translator import translate_to_english
from app.script_gen import generate_script
from app.tts import generate_audio


def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(
        description="Generate a Persian podcast from an input voice note."
    )
    parser.add_argument(
        "--filename", "-f",
        required=True,
        help="Name of the audio file located in assets/inputs/ (e.g., input.wav)"
    )
    args = parser.parse_args()

    # Define paths
    input_path = os.path.join("assets", "inputs", args.filename)
    if not os.path.isfile(input_path):
        print(f"Error: Input file '{input_path}' not found.")
        return

    base_name = os.path.splitext(args.filename)[0]
    output_dir = os.path.join("assets", "outputs", base_name)
    os.makedirs(output_dir, exist_ok=True)

    # Configure logging
    log_file = os.path.join(output_dir, "process.log")
    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format="%(asctime)s %(levelname)s: %(message)s"
    )
    logging.info(f"Started processing '{args.filename}'")

    try:
        # Step 1: Speech-to-text
        stt_text = transcribe_persian(input_path)
        stt_file = os.path.join(output_dir, "stt.txt")
        with open(stt_file, "w", encoding="utf-8") as f:
            f.write(stt_text)
        logging.info(f"STT completed, text saved to {stt_file}")

        # Step 2: Translation
        eng_text = translate_to_english(stt_text)
        trans_file = os.path.join(output_dir, "translation.txt")
        with open(trans_file, "w", encoding="utf-8") as f:
            f.write(eng_text)
        logging.info(f"Translation completed, text saved to {trans_file}")

        # Step 3: Script generation
        script_text = generate_script(eng_text)
        script_file = os.path.join(output_dir, "script.txt")
        with open(script_file, "w", encoding="utf-8") as f:
            f.write(script_text)
        logging.info(f"Script generated, saved to {script_file}")

        # Step 4: Text-to-speech
        audio_out = os.path.join(output_dir, f"{base_name}_podcast.wav")
        generate_audio(script_text, audio_out)
        logging.info(f"TTS completed, audio saved to {audio_out}")

        print(f"Processing complete. All outputs saved to '{output_dir}'.")
        logging.info("Processing finished successfully.")

    except Exception as e:
        logging.error(f"Error during processing: {e}", exc_info=True)
        print(f"An error occurred: {e}. Check the log at '{log_file}' for details.")


if __name__ == "__main__":
    main()
