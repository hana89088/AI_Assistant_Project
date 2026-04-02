## 2025-02-23 - Avoid O(N) WebSockets API and Serialization Bottlenecks
**Learning:** Sequential processing in broadcast methods, especially those involving external API calls (like OpenAI/ElevenLabs) or JSON serialization within comprehensions for multiple WebSocket clients, leads to O(N) latency relative to connection counts, severely degrading responsiveness.
**Action:** Always use `asyncio.gather` for concurrent processing across multiple clients and extract JSON serialization out of broadcast loops to compute it exactly once.
