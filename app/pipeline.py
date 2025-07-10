from app import stt, translator, script_gen, tts


def generate_podcast_from_audio(audio_path: str, output_path: str):
    """
        Main pipeline to generate podcast audio from input Persian voice.
    """
    persian_text = stt.transcribe_persian(audio_path)

    english_text = translator.translate_to_english(persian_text)

    podcast_script = script_gen.generate_script(english_text)

    tts.generate_audio(podcast_script, output_path)

    return output_path