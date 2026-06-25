## 2026-06-25 - Redundant Serialization in Async Loops
**Learning:** In WebSocket broadcasts, putting `json.dumps()` inside the `[client.send(...) for client in clients]` list comprehension causes the message to be redundantly serialized O(N) times instead of once, creating a CPU bottleneck as connection count grows.
**Action:** Always compute identical serialized payloads or expensive transformations outside the loop/list comprehension before passing them to `asyncio.gather()`.
