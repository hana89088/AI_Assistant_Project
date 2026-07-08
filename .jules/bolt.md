## 2026-07-08 - Optimize WebSocket Broadcast Serialization
**Learning:** In Python, string serialization operations (like `json.dumps()`) inside list comprehensions or loops that target multiple identical receivers scale linearly O(N), which becomes a bottleneck in high-throughput real-time systems.
**Action:** Always pre-calculate invariant message serialization outside the loop/comprehension when broadcasting to multiple clients.
