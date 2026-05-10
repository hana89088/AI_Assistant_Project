## 2024-05-24 - O(N) to O(1) Latency in WebSocket Broadcasts
**Learning:** Using sequential `await` calls in a loop for external API requests (like OpenAI completions) during broadcasts introduces O(N) latency, creating severe performance bottlenecks. Furthermore, computing `json.dumps()` inside a broadcast comprehension needlessly serializes the same data N times.
**Action:** Always use `asyncio.gather` (preferably with `return_exceptions=True` to avoid cascading failures) to process client-specific async tasks concurrently, and pre-calculate JSON serialization before the broadcast loop.
