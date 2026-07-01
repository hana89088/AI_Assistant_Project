## 2026-07-01 - Redundant JSON Serialization in Broadcasts
**Learning:** In Python, computing JSON serialization inside a broadcast loop (e.g., inside an `asyncio.gather` list comprehension) causes redundant O(N) serialization overhead, which scales poorly with connection count.
**Action:** Always extract `json.dumps()` or similar expensive serialization operations outside the loop to compute them exactly once (O(1)) before broadcasting to multiple clients.
