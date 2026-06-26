## 2026-06-26 - Optimize WebSocket Broadcast Serialization
**Learning:** The Python backend's WebSocket broadcast architecture had an O(N) serialization bottleneck because `json.dumps()` was called inside the list comprehension for `asyncio.gather()`. Furthermore, client disconnections could fail the entire gather operation.
**Action:** Always extract serialization outside of broadcast loops and use `return_exceptions=True` in `asyncio.gather` to isolate client failures and maintain O(1) serialization overhead.
