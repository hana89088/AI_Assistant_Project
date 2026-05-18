## 2024-05-18 - JSON Serialization in Broadcasts
**Learning:** In async applications handling WebSockets, performing JSON serialization inside `asyncio.gather` list comprehensions causes O(N) redundant CPU work, which can block the event loop during large broadcasts.
**Action:** Always extract `json.dumps()` out of broadcast loops to compute it exactly once. Additionally, use `return_exceptions=True` in `asyncio.gather` to prevent one client's disconnection error from failing the entire broadcast awaitable.
