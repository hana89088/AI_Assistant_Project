## 2024-04-02 - PyAudio Initialization Overhead
**Learning:** In continuous listening applications using `speech_recognition` and `pyaudio`, repeatedly initializing the `Microphone` source block inside a `while` loop (e.g., `with self.microphone as source:`) creates significant hardware allocation and OS-level latency, dramatically slowing down response times between queries.
**Action:** Always initialize the PyAudio stream outside of the continuous listening loop to keep the microphone stream open continuously, removing the latency overhead.

## 2024-04-02 - Testing the Python backend without audio devices
**Learning:** Headless test environments won't have default input devices. Code that tests the logic paths of `pyaudio` blocks will hit `OSError: No Default Input Device Available`.
**Action:** For basic sanity checks without full mocks, test execution will fail on audio device allocation, which is an expected failure state when validating syntax and imports.
