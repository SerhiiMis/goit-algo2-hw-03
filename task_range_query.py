import csv
import random
import timeit
from BTrees.OOBTree import OOBTree

# ---------- Load CSV ----------
def load_items_from_csv(file_path):
    items = []
    with open(file_path, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            items.append({
                "ID": int(row["ID"]),
                "Name": row["Name"],
                "Category": row["Category"],
                "Price": float(row["Price"])
            })
    return items

# ---------- Data Structures ----------
def add_item_to_tree(tree, item):
    tree[item["ID"]] = item

def add_item_to_dict(dct, item):
    dct[item["ID"]] = item

# ---------- Range Queries ----------
def range_query_tree(tree, min_price, max_price):
    return [item for _, item in tree.items() if min_price <= item["Price"] <= max_price]

def range_query_dict(dct, min_price, max_price):
    return [item for item in dct.values() if min_price <= item["Price"] <= max_price]

# ---------- Benchmarking ----------
def benchmark_query(func, structure, queries):
    def wrapped():
        for min_price, max_price in queries:
            func(structure, min_price, max_price)
    return timeit.timeit(wrapped, number=1)

# ---------- Main ----------
def main():
    items = load_items_from_csv("generated_items_data.csv")

    tree = OOBTree()
    dct = {}

    for item in items:
        add_item_to_tree(tree, item)
        add_item_to_dict(dct, item)

    # Create 100 random range queries
    prices = [item["Price"] for item in items]
    min_prices = random.choices(prices, k=100)
    max_prices = [p + random.uniform(10, 100) for p in min_prices]
    queries = list(zip(min_prices, max_prices))

    time_tree = benchmark_query(range_query_tree, tree, queries)
    time_dict = benchmark_query(range_query_dict, dct, queries)

    print(f"Total range_query time for OOBTree: {time_tree:.6f} seconds")
    print(f"Total range_query time for Dict: {time_dict:.6f} seconds")

if __name__ == "__main__":
    main()
