## 2024-05-15 - Optimize WebSocket broadcast and shared mic concurrency
**Learning:** In shared microphone scenarios with multiple connected WebSockets, sequential `await` calls in loops create an O(N) performance bottleneck for external API latency. Also, serializing JSON inside a broadcast loop does redundant work.
**Action:** Extract `json.dumps` outside broadcast loops to compute it exactly once, and use `asyncio.gather(..., return_exceptions=True)` to process independent client API requests concurrently and prevent single-client failures from propagating.
