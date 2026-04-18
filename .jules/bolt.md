## 2024-05-24 - PyAudio Stream Latency
**Learning:** Initializing PyAudio microphone streams (`with self.microphone as source:`) inside a continuous processing loop causes significant latency due to hardware initialization overhead on each iteration.
**Action:** Always initialize the microphone stream context outside of the continuous processing `while` loop.