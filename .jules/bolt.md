## 2024-05-23 - JSON Serialization in WebSocket Broadcasts
**Learning:** Found an O(N) serialization bottleneck in `src/python/main.py`. The `json.dumps(message)` was inside the list comprehension of `asyncio.gather` for WebSocket broadcasts, causing the same message to be serialized redundantly for every connected client.
**Action:** Extract JSON serialization out of broadcast loops to compute it exactly once, and use `return_exceptions=True` in `asyncio.gather` to prevent one client disconnection from failing the entire broadcast.
