import time
from src.python.main import AIAssistant
import asyncio

async def test_broadcast_perf():
    assistant = AIAssistant()
    # Create dummy clients
    class DummyWebsocket:
        def __init__(self, idx):
            self.idx = idx
            self.remote_address = f"127.0.0.1:{10000+idx}"
            self.sent_messages = []

        async def send(self, message):
            # simulate network latency
            await asyncio.sleep(0.001)
            self.sent_messages.append(message)

    # Add clients
    for i in range(100):
        assistant.clients.add(DummyWebsocket(i))

    message = {
        "type": "test",
        "data": "x" * 1024 # 1kb
    }

    start = time.time()
    await assistant.broadcast(message)
    end = time.time()

    print(f"Broadcast to 100 clients took {end-start:.4f} seconds")

asyncio.run(test_broadcast_perf())
