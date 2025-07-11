# Navaa: Persian Podcast Generator

Navaa transforms your Persian voice notes into polished, full-length podcast episodes using OpenAI's suite of APIs in a simple, automated pipeline.

## Technologies Used

* **Python 3.9+** for scripting and orchestration
* **OpenAI API**

  * Whisper for speech-to-text (STT)
  * gpt-4o-mini for translation (Persian → English) and script generation
  * gpt-4o-mini-tts for text-to-speech (TTS)
* **python-dotenv** to manage environment variables securely
* **Logging** via Python's `logging` module

## Pipeline Flow

1. **Speech-to-Text**: Transcribe Persian audio notes into text with Whisper.
2. **Translation**: Translate the Persian transcript into English for clearer LLM understanding.
3. **Script Generation**: Use GPT to draft a conversational Persian podcast script (intro, body, conclusion).
4. **Text-to-Speech**: Synthesize the final Persian script into high-fidelity audio.

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/Navaa.git
cd Navaa
```

### 2. Install Dependencies

```bash
python -m venv venv
source venv/bin/activate      # macOS/Linux
# or venv\\Scripts\\activate   # Windows
pip install -r requirements.txt
```

### 3. Configure Your API Key

1. Create a file named `.env` in the project root.
2. Add your OpenAI key:

   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   ```

### 4. Prepare Your Input

Place your Persian audio file(s) into the `assets/inputs/` directory. For example:

```
assets/inputs/myvoice.wav
```

### 5. Run the Pipeline

Run the CLI tool with your filename (and optional output directory name):

```bash
python main.py --filename myvoice.wav [--outputname podcast_episode1]
```

* **--filename** (`-f`): Name of the input file in `assets/inputs/`.
* **--outputname** (`-o`): (Optional) Custom folder name under `assets/outputs/`. Defaults to the input file base name.

### 6. Inspect Outputs

After successful processing, check:

```
assets/outputs/{outputname}/
├── process.log         # Detailed processing log
├── stt.txt             # Whisper transcript
├── translation.txt     # English translation
├── script.txt          # Generated podcast script (Persian)
└── {outputname}_podcast.wav  # Final podcast audio
```

