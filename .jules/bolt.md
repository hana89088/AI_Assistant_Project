## 2024-04-02 - PyAudio Microphone Stream Instantiation Bottleneck
**Learning:** Initializing the PyAudio stream (`with self.microphone as source:`) inside a continuous `while` loop introduces severe blocking latency and drops audio chunks due to repeated initialization and teardown of the audio resource.
**Action:** Always initialize long-running audio or hardware streams *outside* of their continuous processing loops to ensure real-time performance and prevent overhead.
