# 📘 README — Script (Pagination + Incremental)

This script performs a **full load** of books using pagination and then an **incremental load** using a watermark.

### How it works
- Loops pages until empty or page cap  
- Collects all books (full load)  
- Tracks watermark = newest publish year  
- Incremental run fetches only books newer than the watermark

### Requirements
```bash
pip install requests
```

### Run
```bash
python ingest.py
```