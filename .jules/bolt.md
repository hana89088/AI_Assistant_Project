## 2025-02-28 - Avoid O(N) WebSocket external API bottlenecks
**Learning:** In WebSocket broadcast loops, making external API calls sequentially (like `get_ai_response` or `generate` TTS) creates O(N) latency that drastically slows down the application as clients scale. Additionally, redundant JSON serialization within list comprehensions wastes CPU cycles.
**Action:** Always use `asyncio.gather` for concurrent processing of independent tasks across clients, and extract identical serialization (e.g., `json.dumps(message)`) outside of loops to evaluate it exactly once.
