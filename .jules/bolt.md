## 2024-05-18 - AsyncIO Event Loop Lag from File Writes
**Learning:** Blocking file I/O operations (like saving TTS audio with `open().write()`) in `asyncio` loops introduce severe event loop lag. Benchmarking revealed up to 90ms lag for ~20MB files.
**Action:** Always wrap blocking file writes in `asyncio.to_thread()` in the Python backend to maintain low latency for WebSocket connections, reducing average lag to <1ms.
## 2024-05-18 - WebSocket Broadcast JSON Serialization Overhead
**Learning:** In the Python backend, performing `json.dumps(message)` inside a list comprehension for `asyncio.gather` causes O(N) serialization overhead, which can cause event loop lag when broadcasting to many clients.
**Action:** Extract JSON serialization outside the loop when broadcasting identical payloads to multiple clients to ensure O(1) serialization performance.
