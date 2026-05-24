## 2024-05-24 - Redundant JSON Serialization in WebSocket Broadcasts
**Learning:** In shared/broadcast WebSocket scenarios with multiple clients, inline serialization within a list comprehension (e.g., `[client.send(json.dumps(msg)) for client in clients]`) causes O(N) redundant string formatting, leading to unnecessary CPU load. Also `asyncio.gather` without `return_exceptions=True` can cause a single dropped connection to terminate the entire broadcast.
**Action:** Always extract `json.dumps()` before broadcasting to active connections and use `return_exceptions=True` in `asyncio.gather`.
