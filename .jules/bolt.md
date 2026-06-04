
## 2024-05-18 - Avoid redundant JSON serialization in Python WebSocket broadcast
**Learning:** In the Python backend, using `json.dumps()` inside a list comprehension for `asyncio.gather(*[client.send(...)])` causes the same object to be redundantly serialized O(N) times where N is the number of clients, wasting CPU cycles and potentially blocking the event loop for large payloads.
**Action:** Always serialize the payload exactly once before the loop and pass the serialized string to the send calls. Additionally, ensure `return_exceptions=True` is used with `gather` so single client errors do not crash the entire broadcast.
