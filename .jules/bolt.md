## 2026-04-25 - Extracted JSON serialization from broadcast loop
**Learning:** Serializing JSON inside a broadcast list comprehension causes redundant O(N) CPU overhead, scaling poorly with connection count.
**Action:** Always serialize broadcast messages exactly once before fanning out to clients.
