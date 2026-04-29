## 2025-02-23 - Concurrent Broadcasts & JSON Optimization
**Learning:** Sequential external API calls in broadcast loops create O(N) latency bottlenecks. JSON serialization inside list comprehensions for broadcast messages also adds unnecessary CPU overhead.
**Action:** Use `asyncio.gather` (with `return_exceptions=True`) for concurrent processing of external API calls in broadcasts, and always compute JSON serialization exactly once outside of broadcast loops to maintain O(1) latency relative to connection count.
