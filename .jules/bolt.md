## 2024-05-24 - Broadcast JSON Serialization Overhead
**Learning:** In the Python backend's WebSocket broadcast system, `json.dumps(message)` was placed inside the list comprehension for `asyncio.gather`. This caused the exact same message to be serialized O(N) times for N connected clients, creating unnecessary CPU overhead on the event loop.
**Action:** Always extract JSON serialization out of broadcast loops to compute it exactly once before fanning out network sends.
