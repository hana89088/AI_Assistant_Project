## 2025-02-27 - Blocking I/O Event Loop Lag
**Learning:** Blocking file I/O writes for ~20MB TTS audio files in the Python backend introduces up to 90ms of event loop lag, freezing WebSocket broadcasts and other async operations.
**Action:** Always wrap file writes in `asyncio.to_thread` when saving audio or other large files within `async def` methods to maintain <1ms event loop latency.
