import sys
import os
from unittest.mock import MagicMock, AsyncMock

# Mock dependencies before importing main
sys.modules["speech_recognition"] = MagicMock()
sys.modules["websockets"] = MagicMock()
sys.modules["websockets.exceptions"] = MagicMock()
sys.modules["dotenv"] = MagicMock()
sys.modules["openai"] = MagicMock()
sys.modules["elevenlabs"] = MagicMock()

import unittest
import json
from unittest.mock import patch

# Add src/python to path
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from main import AIAssistant

class TestAIAssistant(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        # We need to mock the microphone and recognizer that are initialized in __init__
        with patch('speech_recognition.Recognizer'), patch('speech_recognition.Microphone'):
            self.assistant = AIAssistant()

    def test_ai_assistant_initialization(self):
        self.assertEqual(len(self.assistant.clients), 0)
        self.assertEqual(len(self.assistant.conversation_history), 0)
        self.assertFalse(self.assistant.is_listening)

    def test_analyze_emotion(self):
        self.assertEqual(self.assistant.analyze_emotion("I am so happy and excited!"), "happy")
        self.assertEqual(self.assistant.analyze_emotion("I am sorry and sad."), "sad")
        self.assertEqual(self.assistant.analyze_emotion("Hmm, let me think about it."), "thinking")
        self.assertEqual(self.assistant.analyze_emotion("Wow! That is amazing!"), "surprised")
        self.assertEqual(self.assistant.analyze_emotion("Hello, how can I help you?"), "neutral")

    async def test_broadcast(self):
        mock_client1 = AsyncMock()
        mock_client2 = AsyncMock()
        self.assistant.clients.add(mock_client1)
        self.assistant.clients.add(mock_client2)

        message = {"type": "test", "content": "hello"}
        await self.assistant.broadcast(message)

        # Check if send was called for each client
        # Note: asyncio.gather is used, so we just check if they were called
        mock_client1.send.assert_called_once_with(json.dumps(message))
        mock_client2.send.assert_called_once_with(json.dumps(message))

    @patch("openai.ChatCompletion.create")
    async def test_get_ai_response_success(self, mock_create):
        # Configure mock
        mock_response = MagicMock()
        mock_response.choices = [MagicMock()]
        mock_response.choices[0].message.content = "I am very happy to see you!"
        mock_create.return_value = mock_response

        response = await self.assistant.get_ai_response("Hello")

        self.assertEqual(response["text"], "I am very happy to see you!")
        self.assertEqual(response["emotion"], "happy")
        self.assertEqual(len(self.assistant.conversation_history), 2)
        self.assertEqual(self.assistant.conversation_history[0], {"role": "user", "content": "Hello"})
        self.assertEqual(self.assistant.conversation_history[1], {"role": "assistant", "content": "I am very happy to see you!"})

    @patch("openai.ChatCompletion.create")
    async def test_get_ai_response_error(self, mock_create):
        mock_create.side_effect = Exception("API Error")

        response = await self.assistant.get_ai_response("Hello")

        self.assertIn("sorry", response["text"])
        self.assertEqual(response["emotion"], "neutral")

if __name__ == "__main__":
    unittest.main()
