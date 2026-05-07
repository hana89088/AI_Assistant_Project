## 2024-05-07 - Blocking File I/O Lag in Async Python Backend
**Learning:** Benchmarking reveals that synchronous file writes (e.g., saving ~20MB TTS audio files) within async functions block the main event loop, introducing up to 90ms of lag per operation.
**Action:** Always offload blocking file writes to a background thread using `asyncio.to_thread` to maintain application responsiveness and keep average lag <1ms.
