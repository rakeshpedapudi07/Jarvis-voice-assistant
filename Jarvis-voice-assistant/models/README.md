# Models Folder

This folder contains the speech recognition models used by the Jarvis voice assistant.

## Download Instructions

We use the [Vosk](https://alphacephei.com/vosk) offline speech recognition model.

### Small English Model (Recommended for faster performance)
```bash
wget https://alphacephei.com/vosk/models/vosk-model-small-en-us-0.15.zip
unzip vosk-model-small-en-us-0.15.zip
mv vosk-model-small-en-us-0.15 vosk_model
rm vosk-model-small-en-us-0.15.zip
