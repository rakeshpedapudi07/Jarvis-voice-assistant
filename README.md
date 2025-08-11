# Jarvis-voice-assistant
An offline Python-based voice assistant using Vosk for speech recognition and pyttsx3 for text-to-speech.
Features
🎙️ Offline speech recognition (no internet required)

🗣️ Natural voice responses using pyttsx3

🛠️ Modular design with a src/ folder for clean code organization

📂 Easy to customize commands and functionality

Installation
bash
Copy
Edit
# Clone the repository
git clone https://github.com/YOUR_USERNAME/Jarvis-voice-assistant.git
cd Jarvis-voice-assistant

# Install dependencies
pip install -r requirements.txt

# Download Vosk model (e.g., small English model)
mkdir models
cd models
wget https://alphacephei.com/vosk/models/vosk-model-small-en-us-0.15.zip
unzip vosk-model-small-en-us-0.15.zip
mv vosk-model-small-en-us-0.15 vosk_model
cd ..
Usage
bash
Copy
Edit
python src/Jarvis.py
Then, simply speak to interact with Jarvis.

Requirements
Python 3.8+

Vosk

pyttsx3

pyaudio

All dependencies are in requirements.txt.
