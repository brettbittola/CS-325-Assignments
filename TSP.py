# Brett Bittola
# CS 325
# 3/11/2024
# Traveling Salesman Problem

def solve_tsp(G):
    """Traveling Salesman Problem using nearest-neighbor heuristic"""
    V = len(G)
    visited = [0]
    path = [0]

    while len(visited) < V:
        smallest = 99999
        current_node = path[-1]
        next_node = None

        for v in range(V):
            if v not in visited:
                if G[current_node][v] != 0 and G[current_node][v] < smallest:
                    smallest = G[current_node][v]
                    next_node = v

        if next_node is not None:
            visited.append(next_node)
            path.append(next_node)

    path.append(0)
    return path
