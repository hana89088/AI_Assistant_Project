# AI Assistant Development Environment Setup Script for Windows
# Run this script as Administrator

Write-Host "AI Assistant Development Environment Setup" -ForegroundColor Green
Write-Host "=========================================" -ForegroundColor Green

# Check if running as Administrator
if (-NOT ([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole] "Administrator"))
{
    Write-Host "This script needs to be run as Administrator. Exiting..." -ForegroundColor Red
    exit 1
}

# Install Chocolatey if not installed
if (!(Test-Path "$env:ProgramData\chocolatey\choco.exe")) {
    Write-Host "Installing Chocolatey..." -ForegroundColor Yellow
    Set-ExecutionPolicy Bypass -Scope Process -Force
    [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072
    iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
}

# Install required software via Chocolatey
Write-Host "`nInstalling required software..." -ForegroundColor Yellow

# Development tools
choco install git -y
choco install python -y
choco install nodejs -y
choco install vscode -y
choco install unity-hub -y

# Optional but recommended
Write-Host "`nInstalling optional tools..." -ForegroundColor Yellow
choco install blender -y
choco install obs-studio -y
choco install ffmpeg -y

# Refresh environment variables
$env:Path = [System.Environment]::GetEnvironmentVariable("Path","Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path","User")

# Install Python packages
Write-Host "`nInstalling Python packages..." -ForegroundColor Yellow
python -m pip install --upgrade pip
python -m pip install openai
python -m pip install speechrecognition
python -m pip install pyaudio
python -m pip install websockets
python -m pip install langchain
python -m pip install elevenlabs
python -m pip install numpy
python -m pip install opencv-python
python -m pip install pillow

# Install Node.js packages globally
Write-Host "`nInstalling Node.js packages..." -ForegroundColor Yellow
npm install -g electron
npm install -g @vue/cli
npm install -g create-react-app

# Create project structure
Write-Host "`nCreating project structure..." -ForegroundColor Yellow
$projectPath = "C:\Users\$env:USERNAME\AI_Assistant_Project"

# Create directories
$directories = @(
    "$projectPath\src",
    "$projectPath\src\python",
    "$projectPath\src\unity",
    "$projectPath\src\electron",
    "$projectPath\assets",
    "$projectPath\assets\models",
    "$projectPath\assets\voices",
    "$projectPath\assets\animations",
    "$projectPath\docs",
    "$projectPath\config",
    "$projectPath\tests"
)

foreach ($dir in $directories) {
    if (!(Test-Path $dir)) {
        New-Item -ItemType Directory -Path $dir -Force
        Write-Host "Created: $dir" -ForegroundColor Green
    }
}

# Download Live2D Cubism SDK (manual step required)
Write-Host "`nNOTE: Live2D Cubism SDK needs to be downloaded manually from:" -ForegroundColor Cyan
Write-Host "https://www.live2d.com/en/download/cubism-sdk/" -ForegroundColor White
Write-Host "Extract it to: $projectPath\libs\Live2D" -ForegroundColor White

# Create initial configuration files
Write-Host "`nCreating configuration files..." -ForegroundColor Yellow

# Create .gitignore
$gitignore = @"
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
venv/
.env

# Unity
[Ll]ibrary/
[Tt]emp/
[Oo]bj/
[Bb]uild/
[Bb]uilds/
[Ll]ogs/
[Uu]ser[Ss]ettings/
*.pidb.meta
*.pdb.meta
*.mdb.meta

# Node
node_modules/
dist/
*.log
npm-debug.log*

# API Keys and Secrets
config/secrets.json
*.key
*.pem

# OS
.DS_Store
Thumbs.db

# IDE
.vscode/
.idea/
*.swp
*.swo
"@

$gitignore | Out-File -FilePath "$projectPath\.gitignore" -Encoding UTF8

# Create requirements.txt
$requirements = @"
openai==1.3.0
speechrecognition==3.10.0
pyaudio==0.2.11
websockets==11.0.3
langchain==0.0.350
elevenlabs==0.2.27
numpy==1.24.3
opencv-python==4.8.1.78
pillow==10.1.0
pydantic==2.5.0
python-dotenv==1.0.0
asyncio==3.4.3
aiohttp==3.9.1
"@

$requirements | Out-File -FilePath "$projectPath\requirements.txt" -Encoding UTF8

# Create package.json for Electron app
$packageJson = @"
{
  "name": "ai-assistant-3d",
  "version": "1.0.0",
  "description": "AI Assistant with 3D Anime Model",
  "main": "main.js",
  "scripts": {
    "start": "electron .",
    "build": "electron-builder",
    "dev": "electron . --dev"
  },
  "keywords": ["ai", "assistant", "3d", "anime"],
  "author": "Your Name",
  "license": "MIT",
  "devDependencies": {
    "electron": "^27.0.0",
    "electron-builder": "^24.6.4"
  },
  "dependencies": {
    "socket.io-client": "^4.5.4",
    "axios": "^1.6.2"
  }
}
"@

$packageJson | Out-File -FilePath "$projectPath\src\electron\package.json" -Encoding UTF8

# Create environment template
$envTemplate = @"
# AI API Keys
OPENAI_API_KEY=your_openai_api_key_here
ELEVENLABS_API_KEY=your_elevenlabs_api_key_here

# Application Settings
APP_PORT=3000
WEBSOCKET_PORT=8080

# Voice Settings
VOICE_ACTIVATION_KEYWORD=Hey Assistant
TTS_VOICE_ID=default

# Model Settings
MODEL_PATH=assets/models/character.model3.json
"@

$envTemplate | Out-File -FilePath "$projectPath\.env.example" -Encoding UTF8

# Create README
$readme = @"
# AI Assistant with 3D Anime Model

## Setup Instructions

1. **Install Unity**
   - Open Unity Hub
   - Install Unity 2022.3 LTS

2. **Configure API Keys**
   - Copy `.env.example` to `.env`
   - Add your API keys

3. **Install Python Dependencies**
   ```bash
   cd AI_Assistant_Project
   python -m venv venv
   .\venv\Scripts\activate
   pip install -r requirements.txt
   ```

4. **Install Node Dependencies**
   ```bash
   cd src/electron
   npm install
   ```

5. **Download Live2D SDK**
   - Visit https://www.live2d.com/en/download/cubism-sdk/
   - Extract to `libs/Live2D`

## Running the Project

1. Start the Python backend:
   ```bash
   python src/python/main.py
   ```

2. Open Unity project in `src/unity`

3. Run Electron app:
   ```bash
   cd src/electron
   npm start
   ```

## Project Structure
- `/src/python` - AI backend and voice processing
- `/src/unity` - 3D character rendering
- `/src/electron` - Desktop application
- `/assets` - Models, voices, and animations
- `/config` - Configuration files
- `/docs` - Documentation
"@

$readme | Out-File -FilePath "$projectPath\README.md" -Encoding UTF8

Write-Host "`nSetup complete!" -ForegroundColor Green
Write-Host "Project created at: $projectPath" -ForegroundColor Cyan
Write-Host "`nNext steps:" -ForegroundColor Yellow
Write-Host "1. Open Unity Hub and create a new 3D project in $projectPath\src\unity" -ForegroundColor White
Write-Host "2. Download Live2D SDK and extract to $projectPath\libs\Live2D" -ForegroundColor White
Write-Host "3. Get your API keys from OpenAI and ElevenLabs" -ForegroundColor White
Write-Host "4. Copy .env.example to .env and add your API keys" -ForegroundColor White
Write-Host "5. Check the README.md for detailed instructions" -ForegroundColor White
