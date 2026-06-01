## 2024-05-24 - Extracting Serialization out of Broadcast Loops
**Learning:** In WebSocket broadcast scenarios, calculating `json.dumps(message)` inside a list comprehension causes O(N) redundant serializations, which unnecessarily blocks the Python event loop.
**Action:** Always pre-calculate JSON serialization outside the loop and pass the serialized string to each client connection to achieve O(1) serialization cost.
