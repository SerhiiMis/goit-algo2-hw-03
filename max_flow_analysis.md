# 📊 Logistics Network — Max Flow Analysis Report

## ✅ Maximum Flow Result

- **Total Maximum Flow:** 115 units
- Computed using the **Edmonds-Karp algorithm**
- Graph modeled with terminals, warehouses, and stores using real capacity constraints

---

## 🗃️ Terminal → Store Flow Table

| Terminal  | Store   | Flow |
| --------- | ------- | ---- |
| Terminal1 | Store1  | 15   |
| Terminal1 | Store2  | 10   |
| Terminal1 | Store4  | 15   |
| Terminal1 | Store5  | 10   |
| Terminal1 | Store6  | 5    |
| Terminal1 | Store7  | 15   |
| Terminal1 | Store8  | 10   |
| Terminal2 | Store10 | 20   |
| Terminal2 | Store11 | 10   |
| Terminal2 | Store4  | 10   |
| Terminal2 | Store5  | 10   |
| Terminal2 | Store6  | 5    |
| Terminal2 | Store7  | 15   |
| Terminal2 | Store8  | 10   |

---

## 🔍 Analysis

### 1. Which terminals provide the most flow?

- **Terminal 1:** 80 units
- **Terminal 2:** 35 units

✅ Terminal 1 is the primary supplier due to better access to high-output warehouses.

---

### 2. Which routes have the lowest capacity and how does this affect the total flow?

- Low-capacity routes:
  - Terminal2 → Warehouse2: 10
  - Warehouse4 → Store13: 5
  - Warehouse4 → Store14: 10
  - Warehouse2 → Store5: 10

🔧 These routes act as bottlenecks, especially limiting Terminal2's ability to supply more stores.

---

### 3. Which stores received the least goods? Can we increase their supply?

**Stores with no flow:**

- Store3
- Store9
- Store12
- Store13
- Store14

💡 To increase their supply:

- Add capacity to connections like:
  - Warehouse1 → Store3
  - Warehouse3 → Store9
  - Warehouse4 → Store12–14
- Increase input capacity to **Warehouse4**

---

### 4. Are there bottlenecks that could be removed?

Yes. Key bottlenecks include:

- Terminal2 → Warehouse2 (only 10 units)
- Warehouse4 has high demand but limited input (only from Terminal2)
- Shared warehouses (Warehouse2 and Warehouse3) are overloaded

📈 Improving terminal connections and warehouse outputs would increase total flow and coverage.

---
