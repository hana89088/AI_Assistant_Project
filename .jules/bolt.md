## 2024-05-15 - [Avoid repeated stream initialization latency in PyAudio]
**Learning:** Initializing the PyAudio microphone stream using `with self.microphone as source:` inside a continuous processing loop (`while self.is_listening:`) introduces significant latency because the stream is repeatedly opened and closed.
**Action:** Move the continuous `while` loop inside the `with` block so the stream is initialized only once outside the loop.
