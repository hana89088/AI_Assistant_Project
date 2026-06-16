## 2024-06-16 - O(N) Serialization Overhead in WebSocket Broadcast
**Learning:** Calling `json.dumps(message)` inside a list comprehension for broadcasting to multiple WebSocket clients recalculates the JSON string redundantly, introducing O(N) serialization overhead relative to connection count.
**Action:** Always compute JSON serialization exactly once before iterating over clients when broadcasting a shared message. Additionally, use `return_exceptions=True` with `asyncio.gather` so one failing client doesn't propagate the error and fail the entire broadcast awaitable.
