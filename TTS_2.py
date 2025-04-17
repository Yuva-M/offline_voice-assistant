import subprocess

def speak_espeak(text, voice='en-us+f3', speed=140, pitch=50, amplitude=150):
    """
   Use eSpeak NG to convert text to speech on Windows.

    """
    try:
         subprocess.run([
        r"C:/Program Files/eSpeak NG/espeak-ng.exe",  # full path
        "-v", voice,
        "-s", str(speed),
        "-p", str(pitch),
        "-a", str(amplitude),
        text
        ])
    except FileNotFoundError:
        print("Error: espeak-ng executable not found. Make sure it's in your PATH.")

# Example usage
speak_espeak("Hello, i am an offline ai voice assistant.")
