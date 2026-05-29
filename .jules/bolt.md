## 2024-05-24 - WebSocket Broadcast Serialization
**Learning:** The Python backend's `broadcast` method was serializing the same dictionary to JSON O(N) times (once per client) inside an `asyncio.gather` list comprehension, which wastes CPU cycles as the payload is identical for all recipients.
**Action:** Always extract `json.dumps()` or similar serialization out of loops when broadcasting the same payload to multiple clients to ensure O(1) serialization overhead.
