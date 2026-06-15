## 2024-05-30 - Prevent Redundant JSON Serialization in Broadcasts
**Learning:** In WebSocket broadcast operations, serializing JSON payloads inside a loop over active connections creates an O(N) overhead that scales poorly as client count increases.
**Action:** Always extract static payload serialization out of client iteration loops, computing it exactly once.
