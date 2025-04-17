

# AI Voice Assistant Pipeline

This repository contains an offline AI voice assistant that seamlessly integrates three core components:

1. **Speech-to-Text (STT)**: Captures voice input and transcribes it to text using Whisper.
2. **Language Model Assistant**: Processes text input using a local LLM (Llama 3.2) via Ollama.
3. **Text-to-Speech (TTS)**: Converts the assistant's text responses back to speech using eSpeak NG.

---

## Components Overview

### 1. STT Module (`STT.py`)

- **Library**: [OpenAI Whisper](https://github.com/openai/whisper) (offline)
- **Audio I/O**: [`sounddevice`](https://pypi.org/project/sounddevice/) & NumPy
- **Functionality**:
  - Records audio (default 5 seconds at 16 kHz).
  - Transcribes the recorded NumPy audio array via Whisper.

### 2. Assistant Module (`assistant.py`)

- **Tool**: [Ollama CLI](https://ollama.com) with `llama3.2` model
- **Functionality**:
  - Wraps the Ollama CLI in Python (`subprocess`) to send prompts.
  - Prepends a system prompt instructing the assistant to use simple, concise, human-like language.
  - Receives and returns the model's text output.

### 3. TTS Module (`TTS_2.py`)

- **Engine**: [eSpeak NG](https://github.com/espeak-ng/espeak-ng) (offline)
- **Voice**: Mbrola female voice (`us-mbrola-1`) for more natural tone
- **Invocation**: Calls `espeak-ng.exe` via `subprocess` with configurable parameters:
  - `-v` voice variant
  - `-s` speed (wpm)
  - `-p` pitch
  - `-a` amplitude

### 4. Main Pipeline (`main.py`)

- **Flow**:
  1. Prompt user to record voice (or type `exit`).
  2. Capture and transcribe audio via `STT.py`.
  3. Send transcription to `assistant.py` and get a response.
  4. Play the assistant's response via `TTS_2.py`.
- **Loop**: Continues until the user types `exit` or triggers a keyboard interrupt.

---

## Installation

### System Requirement: eSpeak NG

- Ensure **eSpeak NG** is installed on your system:
  - **Windows**: [Download the MSI installer](https://github.com/espeak-ng/espeak-ng/releases) and install it.
  - **Linux / Raspberry Pi**: Use the following command:
    ```bash
    sudo apt install espeak-ng
    ```

---
1. **Clone the repository**:

   ```bash
   git clone https://github.com/your-username/your-repo.git
   cd your-repo
   ```

2. **Create and activate a virtual environment**:

   ```bash
   python3 -m venv venv
   source venv/bin/activate      # Linux/macOS
   venv\Scripts\activate.bat   # Windows
   ```

3. **Install Python dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Install system packages** (for Linux/Raspberry Pi):

   ```bash
   sudo apt update
   sudo apt install ffmpeg espeak-ng libespeak1
   ```

5. **Ensure Ollama & Llama 3.2** are installed and available in your PATH.

---

## Usage

Run the main pipeline script:

```bash
python main.py
```

- Press **Enter** to record your query (default 5 seconds).
- Speak your question into the microphone.
- The assistant transcribes, processes, and responds out loud.
- Type `exit` and press **Enter** to quit.

---

## File Structure

```
├── STT.py          # Speech-to-text module (Whisper)
├── assistant.py    # LLM assistant module (Ollama + Llama 3.2)
├── TTS_2.py        # Text-to-speech module (eSpeak NG)
├── main.py         # Orchestrates the full pipeline
├── requirements.txt# Python dependencies
└── README.md       # Project documentation
```

---

## Customization

- **Note on Robotic Voices**: The current eSpeak NG TTS output may sound robotic. For a more natural voice, consider using [hexgrad/Kokoro-82M](https://github.com/hexgrad/kokoro). Refer to the following code snippet:

```python
from kokoro import KPipeline
import soundfile as sf
import sounddevice as sd
import numpy as np

# Initialize Kokoro pipeline (American English)
pipeline = KPipeline(lang_code='a')

# Input text
text = '''
In this tutorial, we explain how to download, install, and run locally 
Kokoro on Windows computer. Kokoro is an open-weight text to speech model 
or briefly TTS model. Its main advantages is that it is lightweight, 
however, at the same time it delivers comparably quality to larger models. 
Due to its relatively small number of parameters it is faster and 
more cost-efficient than larger models.
In this tutorial, we will thoroughly explain all the steps you 
need to perform in order to run the model. 
In a practical application, you would use this model to develop 
a personal AI assistant, or to enable a computer to communicate with humans.
'''

# Generate speech
generator = pipeline(text, voice='af_heart', speed=1)

# Combine all audio segments into one array
all_audio = []
for i, (gs, ps, audio) in enumerate(generator):
    all_audio.append(audio)

# Concatenate audio segments
final_audio = np.concatenate(all_audio)

# Play audio directly
sd.play(final_audio, samplerate=24000)
sd.wait()
```

- **Change STT model**: In `STT.py`, switch `whisper.load_model("base")` to `"tiny"` or other sizes.
- **Adjust TTS voice/params**: In `TTS_2.py`, modify the `voice`, `speed`, `pitch`, and `amplitude` defaults.
- **System prompt**: In `assistant.py`, tweak `DEFAULT_PROMPT` for different assistant behavior.

---
