## 2024-05-24 - Broadcast Serialization Overhead
**Learning:** In the Python backend (`src/python/main.py`), `asyncio.gather` for broadcasting to WebSocket clients performs JSON serialization inside a list comprehension. This means the same message is serialized N times for N clients, causing an O(N) serialization overhead.
**Action:** Extract JSON serialization outside the loop so it only happens once.
