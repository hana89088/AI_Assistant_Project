## 2024-05-24 - PyAudio Stream Initialization Latency
**Learning:** Re-initializing the PyAudio microphone stream (`with self.microphone as source:`) inside a continuous listening `while` loop causes significant processing latency overhead.
**Action:** Always wrap the entire continuous listening `while` loop inside a single `with self.microphone as source:` context block to avoid repeated hardware stream initialization.
