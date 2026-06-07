"""
AI Assistant Backend - Main Application
Handles voice recognition, AI processing, and communication with Unity frontend
"""

import asyncio
import json
import os
import sys
from datetime import datetime
import speech_recognition as sr
import websockets
from dotenv import load_dotenv
from openai import AsyncOpenAI
from elevenlabs import generate, set_api_key
import threading
import queue
import logging
import uuid
from typing import Dict, Any

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Configuration
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
ELEVENLABS_API_KEY = os.getenv('ELEVENLABS_API_KEY')
WEBSOCKET_PORT = int(os.getenv('WEBSOCKET_PORT', 8080))
VOICE_ACTIVATION_KEYWORD = os.getenv('VOICE_ACTIVATION_KEYWORD', 'Hey Assistant').lower()
TTS_VOICE_ID = os.getenv('TTS_VOICE_ID', 'default')

# Initialize OpenAI async client
openai_client = AsyncOpenAI(api_key=OPENAI_API_KEY)

# Set ElevenLabs API key
if ELEVENLABS_API_KEY:
    set_api_key(ELEVENLABS_API_KEY)

class AIAssistant:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        self.is_listening = False
        self.clients = set()
        self.client_states = {}  # Dict to hold per-client state like conversation history
        self.message_queue = queue.Queue()
        
    async def handle_client(self, websocket, path):
        """Handle WebSocket client connections"""
        self.clients.add(websocket)
        self.client_states[websocket] = {"conversation_history": []}
        logger.info(f"Client connected: {websocket.remote_address}")
        
        try:
            await websocket.send(json.dumps({
                "type": "connection",
                "message": "Connected to AI Assistant"
            }))
            
            async for message in websocket:
                data = json.loads(message)
                await self.process_client_message(data, websocket)
                
        except websockets.exceptions.ConnectionClosed:
            pass
        finally:
            self.clients.remove(websocket)
            if websocket in self.client_states:
                del self.client_states[websocket]
            logger.info(f"Client disconnected: {websocket.remote_address}")
            
    async def process_client_message(self, data, websocket):
        """Process messages from Unity/Electron client"""
        message_type = data.get('type')
        
        if message_type == 'text_input':
            # Process text input from UI
            text = data.get('text')
            response = await self.get_ai_response(text, websocket)
            await self.send_response(response, websocket)
            
        elif message_type == 'start_listening':
            self.start_voice_recognition()
            
        elif message_type == 'stop_listening':
            self.stop_voice_recognition()
            
    async def broadcast(self, message):
        """Broadcast message to all connected clients"""
        if self.clients:
            # Serialize JSON exactly once to avoid redundant O(N) overhead
            serialized_message = json.dumps(message)
            await asyncio.gather(
                *[client.send(serialized_message) for client in self.clients],
                return_exceptions=True
            )
            
    def start_voice_recognition(self):
        """Start continuous voice recognition"""
        if not self.is_listening:
            self.is_listening = True
            thread = threading.Thread(target=self.voice_recognition_loop)
            thread.daemon = True
            thread.start()
            logger.info("Voice recognition started")
            
    def stop_voice_recognition(self):
        """Stop voice recognition"""
        self.is_listening = False
        logger.info("Voice recognition stopped")
        
    def voice_recognition_loop(self):
        """Continuous voice recognition loop"""
        with self.microphone as source:
            self.recognizer.adjust_for_ambient_noise(source)
            
        while self.is_listening:
            try:
                with self.microphone as source:
                    # Listen for audio with timeout
                    audio = self.recognizer.listen(source, timeout=1, phrase_time_limit=5)
                    
                try:
                    # Recognize speech using Google Speech Recognition
                    text = self.recognizer.recognize_google(audio)
                    logger.info(f"Recognized: {text}")
                    
                    # Check for activation keyword
                    if VOICE_ACTIVATION_KEYWORD in text.lower():
                        # Remove activation keyword and process
                        command = text.lower().replace(VOICE_ACTIVATION_KEYWORD, '').strip()
                        if command:
                            asyncio.run_coroutine_threadsafe(
                                self.process_voice_command(command),
                                asyncio.get_event_loop()
                            )
                            
                except sr.UnknownValueError:
                    pass  # Could not understand audio
                except sr.RequestError as e:
                    logger.error(f"Speech recognition error: {e}")
                    
            except sr.WaitTimeoutError:
                pass  # Timeout, continue listening
                
    async def process_voice_command(self, command, websocket=None):
        """Process voice command for a specific client or broadcast if none specified"""
        logger.info(f"Processing command: {command}")
        
        status_msg = {
            "type": "status",
            "status": "processing",
            "message": "Processing your request..."
        }
        
        if websocket:
            await websocket.send(json.dumps(status_msg))
            response = await self.get_ai_response(command, websocket)
            await self.send_response(response, websocket)
        else:
            await self.broadcast(status_msg)
            # If no specific client, we'll process it for all active clients
            # This is a bit tricky for a shared mic, but works for broadcast
            for client in list(self.clients):
                response = await self.get_ai_response(command, client)
                await self.send_response(response, client)
        
    async def get_ai_response(self, user_input: str, websocket) -> Dict[str, Any]:
        """Get response from OpenAI"""
        try:
            if websocket not in self.client_states:
                self.client_states[websocket] = {"conversation_history": []}

            history = self.client_states[websocket]["conversation_history"]

            # Add to conversation history
            history.append({"role": "user", "content": user_input})
            
            # Keep conversation history manageable
            if len(history) > 10:
                history = history[-10:]
            
            # Get response from OpenAI
            response = await openai_client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a friendly and helpful AI assistant with an anime personality. Be enthusiastic and supportive."},
                    *history
                ],
                temperature=0.7,
                max_tokens=150
            )
            
            ai_response = response.choices[0].message.content
            
            # Add to conversation history
            history.append({"role": "assistant", "content": ai_response})
            self.client_states[websocket]["conversation_history"] = history
            
            # Analyze emotion for animation
            emotion = self.analyze_emotion(ai_response)
            
            return {
                "text": ai_response,
                "emotion": emotion
            }
            
        except Exception as e:
            logger.error(f"Error getting AI response: {e}")
            return {
                "text": "I'm sorry, I encountered an error processing your request.",
                "emotion": "neutral"
            }
            
    def analyze_emotion(self, text):
        """Simple emotion analysis for animation triggers"""
        text_lower = text.lower()
        
        if any(word in text_lower for word in ['happy', 'great', 'wonderful', 'awesome', 'excited']):
            return 'happy'
        elif any(word in text_lower for word in ['sorry', 'sad', 'unfortunately']):
            return 'sad'
        elif any(word in text_lower for word in ['hmm', 'think', 'maybe', 'perhaps']):
            return 'thinking'
        elif any(word in text_lower for word in ['!', 'wow', 'amazing']):
            return 'surprised'
        else:
            return 'neutral'
            
    async def send_response(self, response: Dict[str, Any], websocket):
        """Send response to a specific client and generate TTS"""
        msg = {
            "type": "response",
            "text": response['text'],
            "emotion": response['emotion'],
            "timestamp": datetime.now().isoformat()
        }
        
        if websocket:
            await websocket.send(json.dumps(msg))
        else:
            await self.broadcast(msg)

        # Generate TTS if ElevenLabs is configured
        if ELEVENLABS_API_KEY:
            try:
                # Use to_thread since generate is synchronous
                audio = await asyncio.to_thread(
                    generate,
                    text=response['text'],
                    voice=TTS_VOICE_ID,
                    model="eleven_monolingual_v1"
                )
                
                # Save audio to unique file to avoid race conditions
                audio_filename = f"temp_audio_{uuid.uuid4().hex}.mp3"
                audio_path = os.path.join(os.getcwd(), audio_filename)

                with open(audio_path, 'wb') as f:
                    f.write(audio)
                    
                audio_msg = {
                    "type": "audio",
                    "path": audio_path
                }

                # Send audio path to client
                if websocket:
                    await websocket.send(json.dumps(audio_msg))
                else:
                    await self.broadcast(audio_msg)
                
            except Exception as e:
                logger.error(f"TTS generation error: {e}")
                
async def main():
    """Main application entry point"""
    assistant = AIAssistant()
    
    # Start WebSocket server
    logger.info(f"Starting WebSocket server on port {WEBSOCKET_PORT}")
    async with websockets.serve(assistant.handle_client, "localhost", WEBSOCKET_PORT):
        logger.info("AI Assistant backend is running...")
        
        # Start voice recognition by default
        assistant.start_voice_recognition()
        
        # Keep the server running
        await asyncio.Future()
        
if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Shutting down AI Assistant...")
        sys.exit(0)
