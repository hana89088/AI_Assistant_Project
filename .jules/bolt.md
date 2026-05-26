## 2026-05-26 - Broadcast JSON Serialization Overhead
**Learning:** Broadcasting to multiple WebSockets with `asyncio.gather(*[client.send(json.dumps(msg)) for client in clients])` causes redundant O(N) JSON serialization overhead for identical payloads.
**Action:** Always extract `json.dumps()` outside the broadcast loop/comprehension to serialize exactly once, then distribute the resulting string.
