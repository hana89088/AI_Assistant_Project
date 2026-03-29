## 2024-05-18 - [Optimize AI Broadcast Loop]
**Learning:** Sequential execution of external API calls in a broadcast loop creates an O(N) performance bottleneck.
**Action:** Always use `asyncio.gather` for concurrent processing when handling WebSocket broadcasts that involve external API calls to maintain O(1) latency relative to connection count.