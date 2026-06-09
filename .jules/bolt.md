## 2025-02-24 - Redundant JSON Serialization in WebSocket Broadcasts
**Learning:** In the Python backend, computing `json.dumps()` inside a list comprehension for `asyncio.gather` during WebSocket broadcasts causes redundant O(N) serialization overhead, which can stutter the asyncio event loop when dealing with many concurrent connections.
**Action:** Always compute JSON serialization exactly once before broadcasting to multiple WebSocket clients to achieve O(1) serialization overhead.
