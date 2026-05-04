## 2024-11-20 - AI Broadcast O(N) Latency Fix
**Learning:** Sequential external API calls inside broadcast loops cause O(N) latency scaling with connected clients. JSON serialization within list comprehensions for broadcast also adds redundant processing overhead.
**Action:** Use `asyncio.gather` for concurrent processing of external API calls in broadcast scenarios, and extract JSON serialization outside of broadcast loops to compute exactly once.
