## 2024-05-24 - Event Loop Blocking File I/O
**Learning:** Blocking file writes (like saving generated TTS audio) in `async` functions can introduce significant event loop lag (up to 90ms for ~20MB files). This blocks all other asynchronous operations, degrading responsiveness for all clients.
**Action:** Always offload synchronous file I/O within async functions using `await asyncio.to_thread()`.
