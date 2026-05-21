## 2024-05-24 - JSON Serialization Overhead in Broadcasts
**Learning:** Computing JSON serialization inside WebSocket broadcast loops creates redundant O(N) CPU overhead, and unhandled disconnection errors in `asyncio.gather` can fail the entire broadcast for all clients.
**Action:** Always compute expensive serialization operations before broadcast loops and use `return_exceptions=True` in `asyncio.gather` to isolate client errors.
