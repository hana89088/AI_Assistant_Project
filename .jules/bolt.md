## 2026-03-27 - Optimization of PyAudio Stream Initialization
**Learning:** The continuous initialization of the  context manager within the  loop caused latency. Wrapping the  loop inside the single context manager optimizes the stream setup time and prevents dropped audio frames.
**Action:** Initialize resources (like microphone streams or large configurations) once outside of continuous execution loops when writing data acquisition or recognition pipelines.
## 2024-05-15 - Optimization of PyAudio Stream Initialization
**Learning:** The continuous initialization of the `with self.microphone as source:` context manager within the `while` loop caused latency. Wrapping the `while` loop inside the single context manager optimizes the stream setup time and prevents dropped audio frames.
**Action:** Initialize resources (like microphone streams or large configurations) once outside of continuous execution loops when writing data acquisition or recognition pipelines.
