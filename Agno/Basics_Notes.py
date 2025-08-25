from dotenv import load_dotenv 
from elevenlabs import stream
from elevenlabs.client import ElevenLabs
from elevenlabs import play 
import os
load_dotenv()
elevenlabs=ElevenLabs(
    api_key="sk_f053be0f1226add5fbaeef750f25e8f012988713e2421011",
)
"""
e.g
one object is calling another objects method

class TextToSpeech:
    def convert(self, text):
        return f"Audio for: {text}"

class ElevenLabs:
    def __init__(self):
        self.text_to_speech = TextToSpeech()

# Now, use it like this:
elevenlabs = ElevenLabs()
audio = elevenlabs.text_to_speech.convert("Hello world")
"""
audio=elevenlabs.text_to_speech.stream( 
        text="Hi Titly... [giggles] You always make me smile. Do you miss me? [sighs] I miss you a lot, but I try not to show my feelings to you. [laughs] funny that I always think may that one day come and you will come back to me",
            voice_id="JBFqnCBsd6RMkjVDRZzb",
    model_id="eleven_multilingual_v2",
    output_format="mp3_44100_128",
            )
stream(audio)

for chunk in audio:
    print(chunk)