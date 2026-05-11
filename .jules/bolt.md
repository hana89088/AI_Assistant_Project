## 2024-05-18 - Extract JSON serialization out of broadcast loops
**Learning:** In WebSocket broadcast loops, serializing the message payload (e.g., `json.dumps()`) inside the comprehension/loop results in O(N) redundant string computations.
**Action:** Always extract JSON serialization or any constant computation outside the broadcast loop so it's computed exactly once. Also, using `return_exceptions=True` with `asyncio.gather` prevents a single disconnected client from failing the entire broadcast.
