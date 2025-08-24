# AI Assistant with 3D Anime Model

## Setup Instructions

1. **Install Unity**
   - Open Unity Hub
   - Install Unity 2022.3 LTS

2. **Configure API Keys**
   - Copy .env.example to .env
   - Add your API keys
   - Choose the AI provider with `AI_PROVIDER` (`openai`, `gemini`, or `mcp`)

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

## AI Provider Configuration

The assistant can use different AI backends. Set the `AI_PROVIDER` value in
your `.env` file to choose between:

- `openai` (default) – uses `OPENAI_API_KEY`
- `gemini` – requires `GEMINI_API_KEY`
- `mcp` – uses an OpenAI-compatible endpoint with `MCP_API_KEY` and `MCP_API_BASE`

## Project Structure
- /src/python - AI backend and voice processing
- /src/unity - 3D character rendering
- /src/electron - Desktop application
- /assets - Models, voices, and animations
- /config - Configuration files
- /docs - Documentation
