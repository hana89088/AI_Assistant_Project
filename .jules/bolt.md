## 2024-06-21 - WebSocket Broadcast Serialization
**Learning:** In Python's asyncio, calling `json.dumps()` inside a broadcast loop (like `[client.send(json.dumps(message)) for client in self.clients]`) introduces redundant O(N) serialization overhead that can block the event loop when the number of connected clients grows.
**Action:** Always extract JSON serialization outside of broadcast loops to compute it exactly once, preventing unnecessary CPU usage and event loop latency.
