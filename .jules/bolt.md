## 2024-05-24 - Optimize WebSocket broadcast serialization
**Learning:** During WebSocket broadcasts, calling `json.dumps()` inside a list comprehension for `asyncio.gather` serializes the identical message once per client. This creates redundant O(N) serialization overhead, which can bottleneck the event loop as connection count grows.
**Action:** Extract JSON serialization out of broadcast loops to compute it exactly once. Additionally, use `return_exceptions=True` with `asyncio.gather` for concurrent client operations to prevent one disconnection error from failing the entire awaitable.
