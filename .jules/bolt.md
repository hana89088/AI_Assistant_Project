## 2024-05-18 - PyAudio Stream Initialization Latency
**Learning:** Initializing PyAudio streams (via `with self.microphone as source:`) continuously inside a `while` loop introduces significant latency, blocking continuous recognition loops in `speech_recognition`.
**Action:** Always initialize long-running audio streams outside the `while` processing loop.
