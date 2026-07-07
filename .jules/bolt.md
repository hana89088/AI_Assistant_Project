## 2026-07-07 - Python Broadcast JSON Serialization Overhead
**Learning:** In `src/python/main.py`, calling `json.dumps(message)` inside the list comprehension for `asyncio.gather` during WebSocket broadcasts causes redundant O(N) serialization overhead, unnecessarily consuming CPU resources proportional to the number of connected clients.
**Action:** Always extract JSON serialization out of broadcast loops to compute it exactly once. This is safe and maintains O(1) serialization latency since strings are immutable in Python.
