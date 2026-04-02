## 2024-03-24 - Avoiding PyAudio Stream Initialization Latency
**Learning:** In `src/python/main.py`, initializing the PyAudio stream (`with self.microphone as source:`) inside a continuous `while` loop (like `voice_recognition_loop`) introduces significant startup latency (0.5-2 seconds) on every iteration. The context manager creates and destroys the stream each time, rather than keeping a single stream open.
**Action:** Always place the microphone context manager outside of the continuous listening loop to keep the stream open, maintaining low latency between consecutive voice commands.
