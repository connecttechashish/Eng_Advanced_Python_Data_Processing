# 📘 README — Serial vs Parallel CPU Scoring

This script compares **serial** CPU-heavy scoring with **parallel** execution using `ProcessPoolExecutor`. It runs a per‑genre scoring function both ways, times them, prints core count, and confirms results match.

### What it does
- Serial scoring (one genre at a time)  
- Parallel scoring (across CPU cores)  
- Timed comparison  
- Identical results check  
- Core count printed  
- Parallel faster on multi‑core machines  

### Run
```bash
python get_books.py
```

### Output - Sync vs Async API Calls
SYNC RESULTS: {'science': 585042, 'history': 3491139, 'art': 600172, 'math': 1043, 'biology': 56550, 'technology': 167663}
Sync time: 17.43 seconds

Error fetching history: HTTPSConnectionPool(host='openlibrary.org', port=443): Read timed out. (read timeout=5)
ASYNC RESULTS: {'science': 585042, 'history': 0, 'art': 600172, 'math': 1043, 'biology': 56550, 'technology': 167663}
Async time: 6.36 seconds

Async is faster: True

### Output - Serial vs Parallel CPU Scoring
CPU cores detected: 12

Serial time:   0.53 sec
Parallel time: 0.49 sec

Results identical: True
Parallel faster: True