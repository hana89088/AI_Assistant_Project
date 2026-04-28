## 2024-05-15 - [Avoid PyAudio Stream Reinitialization Latency]
**Learning:** Initializing PyAudio microphone streams repeatedly inside a `while` loop (`with self.microphone as source:`) introduces significant latency because opening and closing the audio device stream is a slow operation.
**Action:** Always wrap the continuous listening loop (`while`) inside a single `with self.microphone as source:` block to keep the stream open continuously.
