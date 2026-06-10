## 2024-06-10 - WebSocket Broadcast Optimization
**Learning:** In the Python backend's `broadcast` function, JSON serialization inside the list comprehension for `asyncio.gather` causes redundant O(N) serialization overhead relative to connection count.
**Action:** Always compute JSON serialization exactly once outside of broadcast loops and use `return_exceptions=True` with `asyncio.gather` to maintain O(1) latency and prevent fast-failing.
