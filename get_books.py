import time
import math
import os
from concurrent.futures import ProcessPoolExecutor

GENRES = ["science", "history", "art", "math", "biology", "technology"]

def heavy_score(genre):
    """CPU-heavy scoring function."""
    total = 0
    for i in range(300_000):
        total += math.sqrt(i) * math.sin(i)
    return genre, total


# -------------------------
# SERIAL VERSION
# -------------------------
def run_serial():
    start = time.perf_counter()
    results = dict(heavy_score(g) for g in GENRES)
    elapsed = time.perf_counter() - start
    return results, elapsed


# -------------------------
# PARALLEL VERSION
# -------------------------
def run_parallel():
    start = time.perf_counter()
    with ProcessPoolExecutor() as pool:
        out = pool.map(heavy_score, GENRES)
    results = dict(out)
    elapsed = time.perf_counter() - start
    return results, elapsed


# -------------------------
# MAIN
# -------------------------
if __name__ == "__main__":
    print(f"CPU cores detected: {os.cpu_count()}")

    serial_results, serial_time = run_serial()
    parallel_results, parallel_time = run_parallel()

    print(f"\nSerial time:   {serial_time:.2f} sec")
    print(f"Parallel time: {parallel_time:.2f} sec")

    print("\nResults identical:", serial_results == parallel_results)
    print("Parallel faster:", parallel_time < serial_time)
