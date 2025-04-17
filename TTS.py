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

# Save the audio to a .wav file
sd.play( final_audio, samplerate=24000)
sd.wait()
