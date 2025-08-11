import whisper
import sounddevice as sd
import numpy as np
import pyttsx3

model = whisper.load_model("small") 
tts = pyttsx3.init()

def speak(text: str):
    """Speak the given text aloud."""
    print(f"Jarvis: {text}")
    tts.say(text)
    tts.runAndWait()

def listen(duration: int = 5, sr: int = 16000) -> np.ndarray:
    """Record audio for a given duration and return it as a numpy array."""
    print("🎤 Listening...")
    audio = sd.rec(int(duration * sr), samplerate=sr, channels=1, dtype=np.float32)
    sd.wait()
    return np.squeeze(audio)

def process_command(text: str) -> bool:
    """
    Process the recognized text and perform actions.
    Returns False if the assistant should stop, True otherwise.
    """
    if "stop" in text.lower():
        speak("Goodbye!")
        return False
    elif "open google" in text.lower():
        speak("Opening Google")
       
    else:
        speak(f"You said {text}")
    return True

def main():
    """Main loop for Jarvis Voice Assistant."""
    while True:
        audio_data = listen()
        result = model.transcribe(audio_data, fp16=False)
        text = result['text'].strip()

        if text:
            print(f"You said: {text}")
            if not process_command(text):
                break

if __name__ == "__main__":
    main()
