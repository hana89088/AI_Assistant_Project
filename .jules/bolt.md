## 2024-03-21 - [PyAudio stream initialization in loops]
**Learning:** Re-opening a PyAudio stream (using `with self.microphone as source:`) on every iteration inside a `while` loop is a significant performance anti-pattern that introduces excessive latency for continuous audio processing.
**Action:** Always move the initialization of the PyAudio stream (`with` statement) outside the continuous processing `while` loop to maintain an open stream and minimize processing delays.
