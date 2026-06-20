## 2024-06-20 - Redundant JSON Serialization in WebSocket Broadcasts
**Learning:** In the Python backend, the WebSocket broadcast loop was serializing the same message payload for every connected client. This O(N) serialization overhead can become a CPU bottleneck as the number of clients scales, unnecessarily blocking the asyncio event loop.
**Action:** Always compute json.dumps exactly once before the asyncio.gather loop during broadcasts to maintain O(1) serialization overhead.
