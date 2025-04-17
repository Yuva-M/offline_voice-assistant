from STT import record_audio, transcribe_audio
from assistant import query_llm
from TTS_2 import speak_espeak

def main():
    print("=== Full Pipeline: Voice Input -> AI Assistant -> Speech Output ===")
    print("Press Enter to record your query. Type 'exit' and press Enter to quit.\n")
    
    while True:
        user_command = input("Press Enter to record or type 'exit': ").strip().lower()
        if user_command == "exit":
            print("Exiting the pipeline. Goodbye!")
            break

        try:
            # Record user's voice input (duration set to 5 seconds, adjust as needed)
            audio, fs = record_audio(duration=5)
            # Transcribe the recorded voice to text
            transcription = transcribe_audio(audio, fs)
            
            if not transcription:
                print("No transcription detected. Please try again.\n")
                continue
            
            print("You (transcribed):", transcription)
            
            # Send transcribed text to the AI assistant and get the response
            response = query_llm(transcription)
            print("Assistant:", response, "\n")
            
            # Convert the assistant's text response to speech using eSpeak NG
            speak_espeak(response)
            
        except KeyboardInterrupt:
            print("\nExiting the pipeline (KeyboardInterrupt).")
            break
        except Exception as e:
            print(f"An error occurred: {e}\n")

if __name__ == "__main__":
    main()
