## 2024-05-24 - PyAudio Stream Initialization Latency
**Learning:** Initializing PyAudio microphone streams (`with self.microphone as source:`) inside a continuous processing `while` loop causes severe latency due to the overhead of repeatedly opening and closing the hardware audio stream.
**Action:** Always initialize the audio stream context manager outside of continuous processing loops to maintain a single, persistent audio connection.
