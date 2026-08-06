import requests

def get_books(subject, page):
    url = "https://openlibrary.org/search.json"
    params = {"subject": subject, "page": page}

    try:
        resp = requests.get(url, params=params, timeout=5)
        resp.raise_for_status()
        data = resp.json()
    except Exception as e:
        print(f"API call failed on page {page}: {e}")
        return []

    books = []
    for doc in data.get("docs", []):
        books.append({
            "title": doc.get("title"),
            "author": doc.get("author_name", ["Unknown"])[0],
            "first_publish_year": doc.get("first_publish_year"),
            "rating": doc.get("ratings_average")
        })

    return books


def full_load(subject, page_cap=5):
    """Loop pages until empty or cap reached."""
    all_books = []
    newest_year = 0

    for page in range(1, page_cap + 1):
        page_books = get_books(subject, page)
        if not page_books:
            print(f"Stopping: empty page at {page}")
            break

        all_books.extend(page_books)

        # Track watermark (max publish year)
        for b in page_books:
            year = b.get("first_publish_year") or 0
            if year > newest_year:
                newest_year = year

    return all_books, newest_year


def incremental_load(subject, watermark):
    """Pull only books newer than the watermark."""
    new_books = []
    page = 1

    while True:
        page_books = get_books(subject, page)
        if not page_books:
            break

        for b in page_books:
            year = b.get("first_publish_year") or 0
            if year > watermark:
                new_books.append(b)

        page += 1

    return new_books


if __name__ == "__main__":
    # --- FULL LOAD ---
    books, watermark = full_load("science", page_cap=5)
    print(f"Full load count: {len(books)}")
    print(f"Watermark (newest publish year): {watermark}")

    print("\nSample full-load books:")
    for b in books[:5]:
        print(f"{b['title']} — {b['author']} ({b['first_publish_year']})")

    # --- INCREMENTAL RUN ---
    inc_books = incremental_load("science", watermark)
    print(f"\nIncremental new books found: {len(inc_books)}")

    for b in inc_books[:5]:
        print(f"{b['title']} — {b['author']} ({b['first_publish_year']})")
