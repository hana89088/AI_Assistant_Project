## 2024-05-24 - JSON Serialization in WebSocket Broadcasts
**Learning:** The Python backend's `broadcast` function was serializing the same dictionary to JSON O(N) times (once per connected client) inside an `asyncio.gather` list comprehension. This creates an unnecessary CPU bottleneck.
**Action:** Always extract `json.dumps()` calls outside of broadcast loops to compute the string exactly once, reducing serialization overhead to O(1).
