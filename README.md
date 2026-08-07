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





### Chunked Revenue + Memory Reduction
This script streams sales.csv in chunks to compute total revenue by genre without loading the full file. It also takes one chunk, converts numeric columns to float32 and the genre column to category, and prints memory usage before and after to show the reduction.

### Run
```bash
python stream_file.py
```

### Output - Chunked Revenue + Memory Reduction
Revenue by genre: {'Biography': 90250648.46, 'Children': 89690096.86, 'Fiction': 90348684.3, 'History': 90321844.77000001, 'Mystery': 89818082.31, 'Romance': 90431882.32, 'Sci-Fi': 89920073.19999999, 'Self-Help': 89879284.97}
Memory before: 15,746,342 bytes
Memory after:  12,572,135 bytes
Reduction:     3,174,207 bytes