## 2024-05-01 - Avoid sequential processing in WebSocket Broadcasts
**Learning:** During broadcast operations to multiple WebSocket clients, looping sequentially to perform expensive operations (like JSON serialization or API calls) causes an O(N) latency bottleneck.
**Action:** Extract computation exactly once outside the loop (like `json.dumps(message)`), and use `asyncio.gather` to concurrently process external API calls or send responses for all clients simultaneously.
