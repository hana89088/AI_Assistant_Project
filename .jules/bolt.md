## 2024-04-02 - O(N) Latency Bottleneck in WebSocket Broadcasts
**Learning:** In the Python backend, broadcasting voice commands to multiple clients triggers individual OpenAI and ElevenLabs API calls. Performing these sequentially in a `for` loop causes O(N) latency, severely degrading performance for later clients.
**Action:** Use `asyncio.gather` to process external API calls concurrently across all clients, restoring O(1) latency relative to the connection count.
