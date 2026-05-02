## 2024-05-24 - Audio Stream Re-initialization Latency
**Learning:** Initializing PyAudio microphone streams (`with self.microphone as source:`) inside a continuous `while` loop introduces significant latency because the stream is repeatedly opened and closed.
**Action:** Always initialize long-running audio streams outside the `while` loop and only perform the listen operations inside the loop.
