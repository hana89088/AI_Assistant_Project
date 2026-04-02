## 2024-04-02 - Initial Journal\n**Learning:** Started journal\n**Action:** Will log critical learnings.
## 2024-04-02 - PyAudio and Threaded I/O Latency
**Learning:** In continuous listening applications using `speech_recognition`, initializing `with self.microphone as source` inside a `while` loop forces PyAudio to repeatedly open and close the stream. This blocking system-level call adds significant latency per cycle and can drop audio. Furthermore, standard file `open().write()` inside async loops blocks the main event thread handling WebSockets.
**Action:** Always initialize audio hardware streams outside the polling loop. Always offload standard synchronous file I/O to background threads via `asyncio.to_thread` in async heavy backends.
