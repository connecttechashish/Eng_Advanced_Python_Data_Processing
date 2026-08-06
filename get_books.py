import time
import requests
import asyncio

SUBJECTS = ["science", "history", "art", "math", "biology", "technology"]

def fetch_count(subject):
    """Sync API call to get result count."""
    try:
        resp = requests.get(
            "https://openlibrary.org/search.json",
            params={"subject": subject},
            timeout=5
        )
        resp.raise_for_status()
        data = resp.json()
        return data.get("numFound", 0)
    except Exception as e:
        print(f"Error fetching {subject}: {e}")
        return 0


# -------------------------
# SYNC VERSION
# -------------------------
def sync_fetch():
    start = time.perf_counter()
    results = {sub: fetch_count(sub) for sub in SUBJECTS}
    elapsed = time.perf_counter() - start
    return results, elapsed


# -------------------------
# ASYNC VERSION
# -------------------------
async def async_fetch():
    start = time.perf_counter()

    # Run sync function in threads concurrently
    tasks = [
        asyncio.to_thread(fetch_count, sub)
        for sub in SUBJECTS
    ]

    counts = await asyncio.gather(*tasks)
    results = dict(zip(SUBJECTS, counts))

    elapsed = time.perf_counter() - start
    return results, elapsed


# -------------------------
# MAIN
# -------------------------
if __name__ == "__main__":
    # Sync
    sync_results, sync_time = sync_fetch()
    print("SYNC RESULTS:", sync_results)
    print(f"Sync time: {sync_time:.2f} seconds\n")

    # Async
    async_results, async_time = asyncio.run(async_fetch())
    print("ASYNC RESULTS:", async_results)
    print(f"Async time: {async_time:.2f} seconds\n")

    print("Async is faster:", async_time < sync_time)
