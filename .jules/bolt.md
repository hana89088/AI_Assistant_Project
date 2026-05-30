## 2024-10-24 - O(N) Serialization Overhead in Broadcast
**Learning:** Found a codebase-specific anti-pattern where JSON serialization was performed inside a list comprehension during WebSocket broadcasts, causing O(N) serialization overhead.
**Action:** Always extract JSON serialization and other constant computations out of broadcast loops to compute exactly once, and use `return_exceptions=True` in `asyncio.gather` for robustness.
