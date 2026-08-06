import requests

def get_books(subject, page):
    url = "https://openlibrary.org/search.json"
    params = {"subject": subject, "page": page}

    try:
        response = requests.get(url, params=params, timeout=5)
        response.raise_for_status()  # catch 4xx/5xx
        data = response.json()
    except Exception as e:
        print(f"API call failed: {e}")
        return []  # do not crash script

    books = []
    for doc in data.get("docs", []):
        books.append({
            "title": doc.get("title"),
            "author": doc.get("author_name", ["Unknown"])[0],
            "first_publish_year": doc.get("first_publish_year"),
            "rating": doc.get("ratings_average")  # may be None
        })

    return books


if __name__ == "__main__":
    books = get_books("science", 1)

    for b in books[:5]:
        print(
            f"{b['title']} — {b['author']} "
            f"(Year: {b['first_publish_year']}, Rating: {b['rating']})"
        )
