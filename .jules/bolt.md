## 2024-05-23 - Event Loop Lag from Blocking File I/O
**Learning:** Blocking file writes for large (e.g., ~20MB) TTS files introduce up to 90ms of event loop lag, significantly impacting concurrent WebSocket handling.
**Action:** Always offload large file I/O operations to `asyncio.to_thread` to maintain event loop responsiveness.
