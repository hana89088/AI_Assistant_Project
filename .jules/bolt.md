## 2025-03-05 - WebSocket Broadcast Optimization
**Learning:** In the Python backend, `json.dumps` was being called inside a list comprehension for every connected client during broadcasts, introducing redundant O(N) serialization overhead.
**Action:** Extract JSON serialization outside the loop so it computes exactly once per broadcast. Use `return_exceptions=True` in `asyncio.gather` to prevent one failing connection from breaking the entire awaitable.
