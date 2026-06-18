## 2024-05-28 - O(N) JSON Serialization Overhead in Broadcasts
**Learning:** In the Python backend WebSocket broadcasts, calculating `json.dumps()` inside the list comprehension for `client.send()` causes redundant O(N) serialization, needlessly consuming CPU and potentially blocking the async event loop.
**Action:** Always extract JSON serialization outside broadcast loops to compute it exactly once, making the serialization overhead O(1) relative to the connection count.
