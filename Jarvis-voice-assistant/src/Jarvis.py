import os
import queue
import sounddevice as sd
import vosk
import pyttsx3
import json

# Text-to-speech engine
engine = pyttsx3.init()
engine.setProperty("rate", 150)

def speak(text):
    engine.say(text)
    engine.runAndWait()

# Load vosk model
model_path = os.path.join("models", "vosk-model-small-en-us-0.15")
if not os.path.exists(model_path):
    print("❌ Model not found! Please download and place it in 'models' folder.")
    exit()

model = vosk.Model(model_path)
q = queue.Queue()

def callback(indata, frames, time, status):
    if status:
        print(status, flush=True)
    q.put(bytes(indata))

def listen():
    with sd.RawInputStream(samplerate=16000, blocksize=8000, dtype="int16",
                           channels=1, callback=callback):
        rec = vosk.KaldiRecognizer(model, 16000)
        while True:
            data = q.get()
            if rec.AcceptWaveform(data):
                result = json.loads(rec.Result())
                return result.get("text", "").strip()

if __name__ == "__main__":
    speak("Hello, I am Jarvis. How can I help you?")
    while True:
        text = listen()
        if text:
            print(f"You said: {text}")
            speak(f"You said {text}")
            if "exit" in text or "quit" in text:
                speak("Goodbye!")
                break
