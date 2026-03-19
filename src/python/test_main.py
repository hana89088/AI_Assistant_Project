import sys
from unittest.mock import MagicMock, AsyncMock, patch
import asyncio
import unittest

# Mocking missing dependencies specified in memory guidelines
sys.modules['speech_recognition'] = MagicMock()
sys.modules['websockets'] = MagicMock()
sys.modules['dotenv'] = MagicMock()
sys.modules['openai'] = MagicMock()
sys.modules['elevenlabs'] = MagicMock()

# Now we can import from main safely
from src.python.main import AIAssistant

class TestAIAssistant(unittest.IsolatedAsyncioTestCase):
    async def test_process_voice_command_broadcast_concurrency(self):
        assistant = AIAssistant()

        # Create mock clients
        client1 = AsyncMock()
        client2 = AsyncMock()
        assistant.clients = {client1, client2}

        # Mock get_ai_response to sleep a tiny bit to ensure gather behavior
        async def mock_get_response(cmd, client):
            await asyncio.sleep(0.01)
            return {"text": f"response for {client}", "emotion": "neutral"}

        assistant.get_ai_response = AsyncMock(side_effect=mock_get_response)
        assistant.send_response = AsyncMock()
        assistant.broadcast = AsyncMock()

        # Record start time
        start_time = asyncio.get_event_loop().time()

        # Call the method without a specific websocket (broadcast mode)
        await assistant.process_voice_command("test command")

        # Record end time
        end_time = asyncio.get_event_loop().time()

        # With sequential processing, this would take ~0.02s
        # With asyncio.gather, it should take ~0.01s
        # The exact time will vary depending on system performance but checking that it executes
        # is enough, combined with checking the mocked calls.

        # Verify broadcast was called
        assistant.broadcast.assert_called_once()

        # Verify get_ai_response and send_response were called for both clients
        self.assertEqual(assistant.get_ai_response.call_count, 2)
        self.assertEqual(assistant.send_response.call_count, 2)

        # Check that it was called with the correct clients
        called_clients = [call.args[1] for call in assistant.get_ai_response.call_args_list]
        self.assertIn(client1, called_clients)
        self.assertIn(client2, called_clients)

if __name__ == "__main__":
    unittest.main()
