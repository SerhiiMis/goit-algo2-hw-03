import networkx as nx

def build_logistics_graph():
    G = nx.DiGraph()

    # Edges from terminals to warehouses
    G.add_edge("Terminal1", "Warehouse1", capacity=25)
    G.add_edge("Terminal1", "Warehouse2", capacity=20)
    G.add_edge("Terminal1", "Warehouse3", capacity=15)
    G.add_edge("Terminal2", "Warehouse2", capacity=10)
    G.add_edge("Terminal2", "Warehouse3", capacity=15)
    G.add_edge("Terminal2", "Warehouse4", capacity=30)

    # Edges from warehouses to stores
    G.add_edge("Warehouse1", "Store1", capacity=15)
    G.add_edge("Warehouse1", "Store2", capacity=10)
    G.add_edge("Warehouse1", "Store3", capacity=20)
    G.add_edge("Warehouse2", "Store4", capacity=15)
    G.add_edge("Warehouse2", "Store5", capacity=10)
    G.add_edge("Warehouse2", "Store6", capacity=25)
    G.add_edge("Warehouse3", "Store7", capacity=20)
    G.add_edge("Warehouse3", "Store8", capacity=15)
    G.add_edge("Warehouse3", "Store9", capacity=10)
    G.add_edge("Warehouse4", "Store10", capacity=20)
    G.add_edge("Warehouse4", "Store11", capacity=10)
    G.add_edge("Warehouse4", "Store12", capacity=15)
    G.add_edge("Warehouse4", "Store13", capacity=5)
    G.add_edge("Warehouse4", "Store14", capacity=10)

    # Add super source and sink
    G.add_edge("SuperSource", "Terminal1", capacity=float("inf"))
    G.add_edge("SuperSource", "Terminal2", capacity=float("inf"))

    for i in range(1, 15):
        G.add_edge(f"Store{i}", "SuperSink", capacity=float("inf"))

    return G

def extract_terminal_store_flows(flow_dict):
    result = []

    for terminal in ["Terminal1", "Terminal2"]:
        visited = set()
        queue = [(terminal, float('inf'))]

        while queue:
            current, min_capacity = queue.pop()

            if current.startswith("Store"):
                result.append((terminal, current, min_capacity))
                continue

            for neighbor, flow in flow_dict[current].items():
                if flow > 0 and (current, neighbor) not in visited:
                    visited.add((current, neighbor))
                    new_capacity = min(min_capacity, flow)
                    queue.append((neighbor, new_capacity))

    unique_flows = {}
    for terminal, store, flow in result:
        key = (terminal, store)
        unique_flows[key] = unique_flows.get(key, 0) + flow

    return [(t, s, f) for (t, s), f in unique_flows.items()]

def print_results():
    G = build_logistics_graph()
    flow_value, flow_dict = nx.maximum_flow(G, "SuperSource", "SuperSink")
    flows = extract_terminal_store_flows(flow_dict)

    print(f"🔁 Maximum total flow: {flow_value} units\n")
    print("📦 Terminal → Store Flow Table:")
    print(f"{'Terminal':<12} {'Store':<10} {'Flow':>5}")
    for terminal, store, flow in sorted(flows):
        print(f"{terminal:<12} {store:<10} {flow:>5}")

if __name__ == "__main__":
    print_results()
