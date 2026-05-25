## 2024-05-24 - WebSocket Broadcast Serialization Bottleneck
**Learning:** In the Python backend, computing `json.dumps(message)` inside the `asyncio.gather` list comprehension for WebSocket broadcasts causes an O(N) redundant serialization overhead that can block the event loop for a large number of clients.
**Action:** Always compute serialization once outside of broadcast loops and pass the pre-serialized string to the client send methods. Use `return_exceptions=True` in `asyncio.gather` to prevent one client failure from crashing the entire broadcast.
