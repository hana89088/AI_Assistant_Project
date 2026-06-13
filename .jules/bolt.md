## 2024-06-13 - Redundant JSON Serialization in Broadcasts
**Learning:** The Python backend was previously computing `json.dumps(message)` inside the list comprehension for `asyncio.gather` when handling WebSocket broadcasts. This caused a redundant O(N) serialization overhead relative to connection count.
**Action:** Extract JSON serialization outside the broadcast loop to compute it exactly once, and use `return_exceptions=True` in `asyncio.gather` to prevent one client's error from propagating.
