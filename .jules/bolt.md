## 2026-07-06 - JSON Serialization in WebSocket Broadcasts
**Learning:** The Python backend was calling `json.dumps()` individually for each connected client inside the `asyncio.gather` loop during WebSocket broadcasts. This caused O(N) redundant JSON serialization overhead.
**Action:** Extract the JSON serialization outside the loop so it's computed exactly once, passing the resulting immutable string to all clients.
