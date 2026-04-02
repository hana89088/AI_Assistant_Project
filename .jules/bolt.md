## 2024-04-02 - PyAudio Stream Latency Optimization
**Learning:** PyAudio microphone streams (`with self.microphone as source:`) incur significant latency if opened and closed repeatedly. In continuous audio processing loops (like `voice_recognition_loop`), initializing the stream inside the loop creates significant overhead.
**Action:** Initialize the PyAudio microphone stream outside of the continuous processing `while` loop to maintain low latency and avoid "port already in use" or other overhead issues.
