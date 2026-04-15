## 2026-04-15 - WebSocket Broadcast Bottlenecks
**Learning:** In the Python backend, broadcasting messages or processing external API calls (like OpenAI) sequentially across connected WebSocket clients creates an O(N) latency bottleneck where N is the number of connections. Additionally, computing `json.dumps()` inside broadcast comprehensions causes redundant serialization overhead.
**Action:** Always use `asyncio.gather` for concurrent API calls and message sending across clients to maintain O(1) latency. Extract `json.dumps()` out of broadcast loops to serialize exactly once.
