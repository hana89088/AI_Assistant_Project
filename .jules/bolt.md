## 2024-04-06 - WebSocket Broadcast Serialization Bottleneck
**Learning:** Found O(N) performance bottleneck in WebSocket broadcasts where `json.dumps()` was being called inside a list comprehension for `asyncio.gather`. In Python's `asyncio`, this blocks the event loop N times for the exact same serialization work.
**Action:** Always pre-serialize payloads before iterating over multiple WebSocket clients to ensure O(1) serialization overhead and maintain predictable event loop execution times.
