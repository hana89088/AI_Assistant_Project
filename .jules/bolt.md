## 2026-06-30 - Blocking file writes stall the event loop
**Learning:** Benchmarking file I/O in the Python backend revealed that blocking writes for large TTS audio files introduce up to 90ms of lag on the main asyncio event loop, causing delays in processing other WebSocket messages.
**Action:** Always offload large file I/O operations in async methods to a separate thread using `asyncio.to_thread` to maintain event loop responsiveness.
