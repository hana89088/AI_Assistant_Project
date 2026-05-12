## 2024-10-24 - Event Loop Blocking File I/O
**Learning:** Blocking file I/O operations (like saving ~20MB TTS audio files) within asyncio functions can introduce significant event loop lag (up to 90ms), breaking responsiveness for real-time applications like WebSockets.
**Action:** Always wrap file I/O operations in `asyncio.to_thread` when operating within the main event loop to ensure they are handled by a background thread and do not block the loop.
