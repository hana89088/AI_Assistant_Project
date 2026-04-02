## 2024-04-02 - O(N) Latency Spike in Broadcast Processing
**Learning:** Sequential processing of external API calls in a broadcast loop causes an O(N) latency bottleneck.
**Action:** Use asyncio.gather for concurrent processing to achieve O(1) latency relative to connection count.
