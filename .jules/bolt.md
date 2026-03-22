## 2024-03-22 - O(N) Broadcast Bottleneck
**Learning:** The `process_voice_command` method in this application's architecture processes connected WebSocket clients sequentially during broadcast commands. Because it waits for the AI API response for each client one by one, performance degrades at O(N) relative to the number of clients connected.
**Action:** When handling WebSocket broadcasts that involve external API calls or blocking operations per client, use `asyncio.gather` to perform them concurrently and maintain O(1) latency relative to connection count.
