# Brett Bittola
# 3/4/2024
# CS 325 Graph Algorithms

def Prims(G):
    s = 0
    V = len(G)
    visited = set()
    MST = []

    dist = [99999] * V
    prev = [None] * V

    dist[s] = 0
    prev[s] = None

    while len(visited) < V:
        smallest = 99999
        current_node = s
        for v in range(V):
            if v not in visited:
                if dist[v] < smallest:
                    smallest = dist[v]
                    current_node = v

        visited.add(current_node)

        if prev[current_node] is not None:
            MST.append((prev[current_node], current_node, G[current_node][prev[current_node]]))

        for v in range(V):
            if G[current_node][v] != 0:
                if v not in visited:
                    if G[current_node][v] < dist[v]:
                        dist[v] = G[current_node][v]
                        prev[v] = current_node

    return MST

# Adapted from Prim's pseudocode in exploration in Module 8.1 and
# https://reintech.io/blog/python-prims-algorithm-tutorial
