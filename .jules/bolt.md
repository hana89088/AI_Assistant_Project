## 2025-04-02 - Continuous PyAudio Stream Bottleneck
**Learning:** In continuous audio processing loops (like a `while` loop for voice recognition), re-initializing the microphone stream (`with self.microphone as source:`) on every iteration creates a significant I/O bottleneck and latency. It should be opened once outside the `while` loop.
**Action:** Always inspect loops that continuously poll hardware or network resources to ensure the resource initialization/connection is performed outside the loop, rather than repeatedly inside it.
