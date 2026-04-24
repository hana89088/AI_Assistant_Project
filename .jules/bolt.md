## 2024-05-24 - Extracting Serialization from Broadcast Loops
**Learning:** In WebSocket broadcast functions (e.g., `broadcast` in `src/python/main.py`), performing JSON serialization inside a list comprehension for `asyncio.gather` causes O(N) serialization overhead relative to connection count.
**Action:** Always compute identical serialized payloads outside the loop exactly once for O(1) serialization performance.
