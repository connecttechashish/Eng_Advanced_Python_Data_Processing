
# 📘 README — Script 1 (get_books)

This script calls the **Open Library Search API** and returns a list of book dictionaries.  
It uses `requests` with a timeout and safe error handling.

### How it works
- `get_books(subject, page)` calls the API  
- Extracts title, author, publish year, rating  
- Returns a list of dicts  
- Running the script prints a few sample books

### Requirements
```bash
pip install requests
```

### Run
```bash
python main.py
```
