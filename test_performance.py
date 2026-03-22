import sys
import unittest
import asyncio
import time
from unittest.mock import MagicMock, AsyncMock, patch

# Mock dependencies before importing main
sys.modules['speech_recognition'] = MagicMock()
sys.modules['websockets'] = MagicMock()
sys.modules['dotenv'] = MagicMock()
sys.modules['openai'] = MagicMock()
sys.modules['elevenlabs'] = MagicMock()

import src.python.main as main_module
from src.python.main import AIAssistant

class TestAIAssistantPerformance(unittest.IsolatedAsyncioTestCase):
    async def test_process_voice_command_concurrency(self):
        assistant = AIAssistant()

        # Create 5 dummy clients
        num_clients = 5
        for i in range(num_clients):
            mock_client = AsyncMock()
            mock_client.send = AsyncMock()
            assistant.clients.add(mock_client)

        # Mock get_ai_response to simulate a 0.5 second API latency
        async def mock_get_ai_response(command, websocket):
            await asyncio.sleep(0.5)
            return {"text": "dummy response", "emotion": "neutral"}

        assistant.get_ai_response = mock_get_ai_response

        # Mock send_response as a quick operation
        async def mock_send_response(response, websocket):
            pass

        assistant.send_response = mock_send_response

        # Mock broadcast so it doesn't try to send via websockets
        async def mock_broadcast(msg):
            pass

        assistant.broadcast = mock_broadcast

        # Time the processing
        start_time = time.time()
        await assistant.process_voice_command("test command")
        end_time = time.time()

        duration = end_time - start_time

        # If processed sequentially, it would take > 2.5 seconds (0.5 * 5)
        # If concurrent, it should take ~0.5 seconds
        self.assertLess(duration, 1.0, f"Processing took {duration:.2f} seconds, expected < 1.0s (indicating concurrent execution)")
        self.assertGreaterEqual(duration, 0.5, f"Processing took {duration:.2f} seconds, expected >= 0.5s")

if __name__ == '__main__':
    unittest.main()
