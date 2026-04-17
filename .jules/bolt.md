## 2024-05-24 - PyAudio Stream Initialization Latency
**Learning:** Initializing the PyAudio microphone stream inside a continuous `while` loop introduces significant, repeated latency due to audio device initialization overhead, severely impacting real-time voice processing.
**Action:** Always wrap the continuous `while` loop inside the `with microphone as source:` context block to keep the audio stream open persistently.
