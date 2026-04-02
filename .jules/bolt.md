## 2024-05-24 - Avoid Sequential Execution in WebSocket Broadcasts

**Learning:** In backend operations that require sending distinct external API calls for multiple connected clients (like generating a unique AI response or custom TTS audio for each WebSocket client), iterating sequentially creates an O(N) latency bottleneck. As client count increases, the time to complete a single user action degrades severely.

**Action:** Whenever handling operations across multiple clients that perform external API calls or other non-trivial async tasks, execute them concurrently using `asyncio.gather()`. This maintains an O(1) time complexity relative to the number of clients, bounded only by the underlying connection pool/rate limits.