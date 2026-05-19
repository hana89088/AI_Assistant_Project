## 2024-05-18 - WebSocket Broadcast Optimization
**Learning:** In `src/python/main.py`, the `AIAssistant.broadcast` method previously serialized the JSON message inside the loop, causing redundant O(N) serialization. Additionally, missing `return_exceptions=True` on `asyncio.gather` meant one disconnected client could fail the whole broadcast.
**Action:** When broadcasting data to multiple clients, serialize payloads outside the loop exactly once (O(1)) and use `return_exceptions=True` to ensure fault-tolerance.
