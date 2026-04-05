## 2024-05-24 - WebSocket Broadcast O(N) Processing Latency
**Learning:** In `src/python/main.py`, the `process_voice_command` loops over clients doing sequential `await get_ai_response(...)` and `await send_response(...)` for a shared microphone broadcast, meaning each additional client adds linear latency to the broadcast.
**Action:** Use `asyncio.gather` with concurrent tasks instead of a sequential loop when broadcasting or processing independent requests to multiple clients to maintain O(1) latency.

## 2024-05-24 - Synchronous File I/O Blocking Event Loop
**Learning:** `send_response` uses `with open(audio_path, 'wb') as f: f.write(audio)`, which is blocking. In a busy async application, disk I/O should be wrapped with `asyncio.to_thread` to prevent stalling the main event loop.
**Action:** Use `asyncio.to_thread` for `open` and `write` or use an asynchronous library like `aiofiles` for file I/O within async functions.

## 2024-05-24 - Unnecessary Repeated JSON Serialization
**Learning:** `broadcast` encodes JSON inside a list comprehension (`[client.send(json.dumps(message)) for client in self.clients]`). This recomputes `json.dumps` for every client unnecessarily.
**Action:** Extract serialization logic before the loop and share the serialized payload across all send calls to save CPU cycles.
