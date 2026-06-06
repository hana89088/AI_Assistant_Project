
## 2024-05-24 - Async Event Loop Lag from Audio File I/O
**Learning:** Blocking file I/O writes for generated TTS audio (~20MB) introduce up to 90ms of event loop lag in the async WebSocket backend.
**Action:** Always wrap file I/O operations in `asyncio.to_thread()` when handling large audio payloads to maintain real-time responsiveness (<1ms lag).
