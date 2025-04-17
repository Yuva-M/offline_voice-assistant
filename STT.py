import numpy as np
import sounddevice as sd
import whisper

# Load Whisper model once (consider using "base" or "tiny" for Raspberry Pi)
print("Loading Whisper model...")
whisper_model = whisper.load_model("base")  # or "tiny" for faster performance on low-power devices

def record_audio(duration=5, fs=16000):
    """
    Record audio from the microphone for a specified duration.
    Returns the recorded audio as a NumPy array and the sample rate.
    """
    print("Recording... Speak now!")
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype="float32")
    sd.wait()  # Wait until recording is finished
    return np.squeeze(audio), fs

def transcribe_audio(audio, fs):
    """
    Transcribe the recorded audio using Whisper.
    """
    print("Transcribing...")
    # Whisper expects a WAV-like float32 mono array with sample rate of 16000
    result = whisper_model.transcribe(audio, language="en", fp16=False)
    transcript = result.get("text", "").strip()
    print("Transcription:", transcript)
    return transcript

def main():
    print("Offline Voice-to-Text using Whisper + sounddevice")
    print("Press Enter to record (Ctrl+C to quit)\n")

    while True:
        try:
            input("Press Enter to start recording...")
            audio, fs = record_audio(duration=5)
            transcribe_audio(audio, fs)
            print()
        except KeyboardInterrupt:
            print("\nExiting...")
            break

if __name__ == "__main__":
    main()
