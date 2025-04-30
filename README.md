# 🚛 Task 1: Maximum Flow in Logistics Network

## Goal

Model a logistics network and compute the **maximum flow** using the **Edmonds-Karp algorithm**.

## Graph Description

- **Terminals → Warehouses → Stores**
- Shared warehouses: Warehouse 2 and 3 receive goods from both Terminal 1 and Terminal 2.
- Total: 20 nodes, with specific edge capacities.

## Edge Capacities

| From        | To          | Capacity |
| ----------- | ----------- | -------- |
| Terminal 1  | Warehouse 1 | 25       |
| Terminal 1  | Warehouse 2 | 20       |
| Terminal 1  | Warehouse 3 | 15       |
| Terminal 2  | Warehouse 2 | 10       |
| Terminal 2  | Warehouse 3 | 15       |
| Terminal 2  | Warehouse 4 | 30       |
| Warehouse 1 | Store 1     | 15       |
| Warehouse 1 | Store 2     | 10       |
| Warehouse 1 | Store 3     | 20       |
| Warehouse 2 | Store 4     | 15       |
| Warehouse 2 | Store 5     | 10       |
| Warehouse 2 | Store 6     | 25       |
| Warehouse 3 | Store 7     | 20       |
| Warehouse 3 | Store 8     | 15       |
| Warehouse 3 | Store 9     | 10       |
| Warehouse 4 | Store 10    | 20       |
| Warehouse 4 | Store 11    | 10       |
| Warehouse 4 | Store 12    | 15       |
| Warehouse 4 | Store 13    | 5        |
| Warehouse 4 | Store 14    | 10       |

## Output

A table of actual flows:
`Terminal Store Flow (units) Terminal 1 Store 1 X Terminal 1 Store 2 Y ... Terminal 2 Store 14 Z`

## Analysis Questions

1. Which terminals provide the most flow?
2. What are the bottlenecks?
3. Which stores receive the least goods?
4. How can flow to those stores be increased?

## Requirements

- Use **Edmonds-Karp** to compute max flow.
- Graph must be modeled exactly as described.
- Return actual flow values per terminal-store path.

# 📊 Task 2: OOBTree vs Dict for Range Queries

## Goal

Compare the performance of `OOBTree` and Python `dict` for **range queries** on product data.

## Input

CSV file: `generated_items_data.csv`

Each row includes:

- `ID` (int)
- `Name` (str)
- `Category` (str)
- `Price` (float)

## Requirements

1. Store data in both:
   - `BTrees.OOBTree.OOBTree`
   - Python `dict`
2. Implement:
   - `add_item_to_tree(data)`
   - `add_item_to_dict(data)`
   - `range_query_tree(min_price, max_price)`
   - `range_query_dict(min_price, max_price)`
3. Perform **100 range queries** using `timeit`.

## Expected Output Format

`Total range_query time for OOBTree: X.XXXXXX seconds`
`Total range_query time for Dict: X.XXXXXX seconds`

## Performance Expectations

- `OOBTree` should be faster for range queries due to its sorted structure.
- `dict` uses linear search → slower for large datasets.
