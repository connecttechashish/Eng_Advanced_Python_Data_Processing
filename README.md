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