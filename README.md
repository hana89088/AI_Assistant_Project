# AI Assistant with 3D Anime Model

## Setup Instructions

1. **Install Unity**
   - Open Unity Hub
   - Install Unity 2022.3 LTS

2. **Configure API Keys**
   - Copy .env.example to .env
   - Add your API keys

3. **Install Python Dependencies**
   ash
   cd AI_Assistant_Project
   python -m venv venv
   .\\venv\\Scripts\\activate
   pip install -r requirements.txt
   `

4. **Install Node Dependencies**
   ash
   cd src/electron
   npm install
   `

5. **Download Live2D SDK**
   - Visit https://www.live2d.com/en/download/cubism-sdk/
   - Extract to libs/Live2D

## Running the Project

1. Start the Python backend:
   ash
   python src/python/main.py
   `

2. Open Unity project in src/unity

3. Run Electron app:
   ash
   cd src/electron
   npm start
   `

### Running Without a GUI

For a simple text or voice chat interface without Unity or Electron, run:

```
python src/python/cli_chat.py
```

Follow the prompts to talk by typing or using your microphone. Responses are
printed in the terminal and, when an ElevenLabs API key is configured, also
spoken aloud.

## Project Structure
- /src/python - AI backend and voice processing
- /src/unity - 3D character rendering
- /src/electron - Desktop application
- /assets - Models, voices, and animations
- /config - Configuration files
- /docs - Documentation
