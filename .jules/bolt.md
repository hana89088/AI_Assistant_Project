## 2024-05-24 - Broadcast JSON Serialization Overhead
**Learning:** In WebSocket broadcasts, calling `json.dumps` inside a list comprehension for `asyncio.gather` causes redundant O(N) serialization overhead, which can lag the event loop when many clients are connected.
**Action:** Always extract JSON serialization out of broadcast loops to compute it exactly once, and use `return_exceptions=True` with `asyncio.gather` so one failing client doesn't abort the broadcast.
