## 2024-03-23 - [Continuous Audio Processing Latency]
**Learning:** Initializing the PyAudio microphone stream (`with self.microphone as source:`) inside a continuous `while` loop introduces significant latency (hundreds of ms per iteration) and can cause the assistant to miss audio chunks entirely due to the overhead of repeatedly opening and closing the device stream.
**Action:** Always wrap the continuous `while` processing loop inside the stream's context manager (i.e., `with self.microphone as source:` encompassing the loop) to initialize the PyAudio stream exactly once and reuse it.
