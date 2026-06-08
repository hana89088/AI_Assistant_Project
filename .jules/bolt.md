## 2024-05-24 - Broadcast Serialization Overhead
**Learning:** In the Python backend's WebSocket broadcast logic, serializing JSON inside the `asyncio.gather` list comprehension causes O(N) redundant serializations and blocks the event loop for each client.
**Action:** Always serialize the payload exactly once before passing it to broadcast loops or list comprehensions, and use `return_exceptions=True` in `asyncio.gather` to prevent one failing connection from dropping the broadcast.
