# 📘 README — Sync vs Async API Calls

This script compares **synchronous** API calls vs **asynchronous** calls using `asyncio.gather` and `asyncio.to_thread`. It fetches the result count for several Open Library subjects and prints both timings to show that async is faster.

### What it does
- Makes multiple API calls **one at a time** (sync)
- Makes the same calls **concurrently** (async)
- Times both approaches
- Prints results + timing comparison

You can explore asyncio gather or asyncio.to_thread.

### Requirements
```bash
pip install requests
```

### Run
```bash
python sync_async.py
```

###Output - Sync vs Async API Calls
SYNC RESULTS: {'science': 585042, 'history': 3491139, 'art': 600172, 'math': 1043, 'biology': 56550, 'technology': 167663}
Sync time: 17.43 seconds

Error fetching history: HTTPSConnectionPool(host='openlibrary.org', port=443): Read timed out. (read timeout=5)
ASYNC RESULTS: {'science': 585042, 'history': 0, 'art': 600172, 'math': 1043, 'biology': 56550, 'technology': 167663}
Async time: 6.36 seconds

Async is faster: True