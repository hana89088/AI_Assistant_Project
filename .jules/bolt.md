## 2026-07-04 - O(N) JSON Serialization in Async Broadcast
**Learning:** In `main.py`, the WebSocket `broadcast` method was serializing the identical message payload for every single connected client `[client.send(json.dumps(message)) for client in self.clients]`. This results in redundant O(N) serialization overhead on the main event loop, causing unnecessary lag as the client count scales.
**Action:** Extract JSON serialization outside of broadcast loops and compute it exactly once before `asyncio.gather`, leveraging Python's immutable strings for safe, zero-copy sharing across tasks.
