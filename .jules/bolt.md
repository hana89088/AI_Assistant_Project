## 2024-05-24 - Broadcast WebSocket Optimization
**Learning:** Found an O(N) redundant JSON serialization problem in Python WebSocket broadcasting. `json.dumps` is called once per client in a list comprehension inside `asyncio.gather`. When broadcasting to many clients, this introduces redundant serialization overhead. Using `asyncio.gather` with `return_exceptions=True` handles disconnections robustly but the serialization overhead remains.
**Action:** Extract the JSON serialization outside the loop or list comprehension so it's calculated exactly once, then send that same serialized string to all connected clients.
## 2024-05-24 - Event Loop Lag from Synchronous File I/O
**Learning:** Found a critical performance bottleneck specific to this architecture. Saving large TTS audio files (~20MB) using synchronous `open().write()` blocks the Python async event loop for up to 90ms, causing latency in real-time WebSocket communication.
**Action:** Always offload synchronous file I/O operations (like writing audio files) to a separate thread using `asyncio.to_thread` in Python backend components to maintain <1ms event loop latency.
