## 2025-03-01 - O(N) JSON Serialization in WebSocket Broadcasts
**Learning:** Performing `json.dumps()` inside a list comprehension for WebSocket broadcasts scales poorly (O(N)), acting as a codebase-specific performance bottleneck for large client sets.
**Action:** Always extract JSON serialization outside of broadcast loops to compute it exactly once (O(1)).
