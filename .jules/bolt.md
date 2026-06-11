## 2024-05-24 - Async Event Loop Blocked by File I/O
**Learning:** Benchmarking reveals that blocking file writes for ~20MB audio files in the backend introduce up to 90ms of event loop lag, blocking other concurrent tasks like WebSocket handling.
**Action:** Always offload blocking file I/O operations in async paths to `asyncio.to_thread` to maintain event loop responsiveness, reducing lag to <1ms.
