## 2024-05-24 - WebSocket Broadcast O(N) Bottlenecks

**Learning:** When broadcasting messages to multiple WebSocket clients or processing commands for all active clients sequentially (e.g., using a `for` loop), the application experiences an O(N) performance bottleneck. Redundant JSON serialization inside the broadcast loop and sequential awaiting of external API calls per client significantly degrade performance as the number of clients increases.

**Action:** Always pre-serialize JSON messages outside the broadcast loop. Utilize `asyncio.gather` with `return_exceptions=True` to concurrently process and broadcast to all active clients, effectively changing the latency from O(N) to O(1) relative to connection count.
