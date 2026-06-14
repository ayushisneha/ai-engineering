# MINI PROJECT - Async Dashboard API

A function that does the following in parallel:
- Fetches all users
- Creates account summary of each user
- Max 3 DB connection allowed (semaphore)
- Any user operation fails -> rest should continue to work