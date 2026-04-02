## 2024-04-02 - O(N) Broadcast Processing Bottleneck
**Learning:** Sequential processing in broadcast events across connected clients can create an O(N) bottleneck, causing noticeable latency with many connected clients, especially when awaiting multiple sequential network calls per client.
**Action:** When handling WebSocket broadcasts that involve awaitable actions (like `get_ai_response` and `send_response` per client), map the work into tasks and use `asyncio.gather` for concurrent processing to maintain O(1) perceived latency.
