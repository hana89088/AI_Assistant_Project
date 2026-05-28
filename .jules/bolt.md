## 2024-05-24 - Extract JSON Serialization from Broadcast Loops
**Learning:** In WebSocket broadcast scenarios, running `json.dumps()` inside the client iteration loop creates an O(N) serialization overhead where N is the number of connected clients. If there are many clients, this unnecessary redundant computation can cause event loop lag.
**Action:** Always extract JSON serialization outside of the broadcast loop so the payload is serialized exactly once (O(1)). Also, use `return_exceptions=True` with `asyncio.gather` so one failing socket doesn't crash the entire broadcast operation.
