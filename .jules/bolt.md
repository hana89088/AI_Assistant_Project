## 2026-04-02 - Continuous Audio Processing Latency with PyAudio
**Learning:** In PyAudio-based continuous voice recognition loops (like `voice_recognition_loop`), re-opening the microphone stream (`with self.microphone as source:`) continuously inside the `while` loop introduces significant latency, overhead, and frame drops.
**Action:** Always initialize PyAudio microphone streams outside of the continuous processing `while` loop to maintain the audio stream state and ensure real-time performance.
