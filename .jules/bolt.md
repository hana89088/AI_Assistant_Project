## 2024-05-05 - Extract JSON Serialization from Broadcast Loop
**Learning:** In a WebSocket server that broadcasts messages to multiple clients, serializing the message to JSON inside the broadcast loop (e.g., inside a list comprehension) means the server wastes CPU cycles repeating the same JSON serialization operation for every client. Extracting the `json.dumps()` call outside the loop makes the serialization O(1) instead.
**Action:** Always serialize broadcast payloads exactly once before the broadcast loop, and pass the pre-serialized string to the WebSocket `send()` method.
