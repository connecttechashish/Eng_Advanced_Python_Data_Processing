import pandas as pd

def stream_revenue(csv_path):
    """Stream sales.csv in chunks and aggregate revenue by genre."""
    genre_totals = {}

    for chunk in pd.read_csv(csv_path, chunksize=50_000):
        # assume columns: genre, price, quantity
        chunk["revenue"] = chunk["price"] * chunk["quantity"]

        for genre, rev in chunk.groupby("genre")["revenue"].sum().items():
            genre_totals[genre] = genre_totals.get(genre, 0) + rev

    return genre_totals


def shrink_memory_one_chunk(csv_path):
    """Load one chunk, shrink memory, and report before/after usage."""
    chunk = next(pd.read_csv(csv_path, chunksize=50_000))

    before = chunk.memory_usage(deep=True).sum()

    # shrink numeric columns
    chunk["price"] = chunk["price"].astype("float32")
    chunk["quantity"] = chunk["quantity"].astype("float32")

    # shrink categorical column
    chunk["genre"] = chunk["genre"].astype("category")

    after = chunk.memory_usage(deep=True).sum()

    return before, after


if __name__ == "__main__":
    print("aaa Revenue by genre:")

    csv_path = "sales.csv"

    totals = stream_revenue(csv_path)
    print("Revenue by genre:", totals)

    before, after = shrink_memory_one_chunk(csv_path)
    print(f"Memory before: {before:,} bytes")
    print(f"Memory after:  {after:,} bytes")
    print(f"Reduction:     {before - after:,} bytes")
