## 2024-03-20 - [Redundant JSON Serialization in Broadcast]
**Learning:** In asyncio applications, doing operations like `json.dumps(message)` inside a list comprehension for `asyncio.gather(*[client.send(...) for client in clients])` creates unnecessary O(N) CPU overhead. Python loops these synchronously before giving them to the event loop.
**Action:** Always extract and cache computations like JSON serialization to an O(1) operation *before* generating the list of coroutines for multiple clients.
