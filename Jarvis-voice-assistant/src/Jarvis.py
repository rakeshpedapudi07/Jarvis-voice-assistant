import whisper
import sounddevice as sd
import numpy as np
import pyttsx3

model = whisper.load_model("small")  
tts = pyttsx3.init()

def speak(text):
    print(f"Jarvis: {text}")
    tts.say(text)
    tts.runAndWait()

def listen():
    duration = 5  
    sr = 16000
    print("🎤 Listening...")
    audio = sd.rec(int(duration * sr), samplerate=sr, channels=1, dtype=np.float32)
    sd.wait()
    return np.squeeze(audio)

while True:
    audio_data = listen()
    result = model.transcribe(audio_data, fp16=False)
    text = result['text'].strip()
    
    if text:
        print(f"You said: {text}")
        if "stop" in text.lower():
            speak("Goodbye!")
            break
        elif "open google" in text.lower():
            speak("Opening Google")
        else:
            speak(f"You said {text}")

