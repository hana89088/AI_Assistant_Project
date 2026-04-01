## 2024-04-01 - Avoid O(N) Processing in WebSockets
**Learning:** Sequential processing of external API calls (e.g., OpenAI, TTS) within a `for client in clients` loop in a WebSocket broadcast handler can cause severe O(N) latency bottlenecks as the number of clients increases.
**Action:** Always use `asyncio.gather` for concurrent processing when broadcasting messages that require external API interaction to maintain O(1) latency relative to the connection count.

## 2024-04-01 - PyAudio Microphone Stream Latency
**Learning:** Repeatedly initializing the PyAudio microphone stream (`with self.microphone as source:`) inside a continuous `while` loop adds significant latency to voice recognition processing.
**Action:** Initialize the microphone stream block outside of the continuous listening loop to keep the stream open and avoid initialization overhead on every iteration.
