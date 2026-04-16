## 2024-04-16 - Initial
**Learning:** Initial setup
**Action:** None

## 2024-04-16 - PyAudio Stream Latency
**Learning:** Re-initializing PyAudio streams (`with self.microphone as source:`) inside a continuous listening `while` loop introduces significant audio processing latency.
**Action:** Always initialize the microphone stream exactly once outside of the continuous processing loop to maintain low-latency audio capture.
