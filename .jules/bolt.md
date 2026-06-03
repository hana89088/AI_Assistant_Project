## 2024-05-24 - Redundant JSON Serialization in Broadcasts
**Learning:** Computing `json.dumps` inside a list comprehension for WebSocket broadcasts scales O(N) with the number of clients, causing redundant serialization overhead that can introduce latency under load.
**Action:** Always extract JSON serialization outside of broadcast loops to compute it exactly once, making the serialization cost O(1) relative to connection count.
