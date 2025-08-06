# Common Error Fixes for AI Assistant Setup

## 1. PowerShell Execution Policy Error

If you're getting an error when trying to run `setup_environment.ps1`, it's likely due to PowerShell's execution policy.

### Fix:

1. **Open PowerShell as Administrator** (Right-click on PowerShell and select "Run as Administrator")

2. **Set Execution Policy** - Run one of these commands:
   ```powershell
   # Option 1: Allow only for current session
   Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process

   # Option 2: Allow for current user (recommended)
   Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

   # Option 3: Allow for all users (requires admin)
   Set-ExecutionPolicy -ExecutionPolicy RemoteSigned
   ```

3. **Run the setup script**:
   ```powershell
   cd C:\Users\tuan\AI_Assistant_Project
   .\setup_environment.ps1
   ```

## 2. Missing Administrator Privileges

If you see "This script needs to be run as Administrator", make sure to:
1. Right-click on PowerShell
2. Select "Run as Administrator"
3. Navigate to the project directory and run the script again

## 3. Chocolatey Installation Issues

If Chocolatey fails to install:
1. Make sure you have internet connection
2. Try installing manually from https://chocolatey.org/install
3. Or use this command in Admin PowerShell:
   ```powershell
   Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
   ```

## 4. Python Package Installation Errors

If Python packages fail to install:

### For PyAudio specifically:
```powershell
# Download the appropriate wheel file for your Python version
# Visit: https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio
# Or try:
pip install pipwin
pipwin install pyaudio
```

### For other packages:
```powershell
# Upgrade pip first
python -m pip install --upgrade pip

# Install packages one by one to identify issues
python -m pip install openai
python -m pip install speechrecognition
python -m pip install websockets
# etc...
```

## 5. Unity-related Errors

If Unity Hub doesn't install:
1. Download manually from https://unity.com/download
2. Install Unity 2022.3 LTS version

## 6. Node.js/npm Errors

If npm commands fail:
```powershell
# Verify Node.js installation
node --version
npm --version

# Clear npm cache if needed
npm cache clean --force

# Install packages with verbose output
npm install -g electron --verbose
```

## 7. WebSocket Connection Errors

If the Python backend can't start:
1. Check if port 8080 is already in use:
   ```powershell
   netstat -ano | findstr :8080
   ```
2. Change the port in `.env` file if needed

## 8. Missing .env File

Create the `.env` file manually:
```powershell
Copy-Item .env.example .env
notepad .env
```
Then add your API keys.

## Quick Troubleshooting Commands

```powershell
# Check installed software
choco list --local-only

# Check Python installation
python --version
pip --version

# Check Node.js installation  
node --version
npm --version

# Check if Git is installed
git --version

# List project structure
tree /F
```

## Manual Installation Alternative

If the automated script fails, you can install components manually:

1. **Python**: https://www.python.org/downloads/
2. **Node.js**: https://nodejs.org/
3. **Git**: https://git-scm.com/
4. **VS Code**: https://code.visualstudio.com/
5. **Unity Hub**: https://unity.com/download
6. **Blender**: https://www.blender.org/download/

Then create the project structure and install packages manually as shown in the README.
