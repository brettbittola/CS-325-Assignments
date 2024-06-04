# Brett Bittola
# 2/26/2024
# CS 325 Graph Algorithms

import heapq


def minEffort(puzzle):
    """Finds the minimum effort of 3D traversal using Djikstra's algorithm"""
    distances = {(row, col): float('infinity') for row in range(len(puzzle)) for col in range(len(puzzle[0]))}
    distances[starting_vertex] = 0
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    visited = []
    pq = [(0, starting_vertex)]

    while len(pq) > 0:
        current_distance, (row, column) = heapq.heappop(pq)
        visited.append((row, column))

        if current_distance > distances[(row, column)]:
            continue

        for x, y in directions:
            new_row, new_column = row + x, column + y
            if 0 <= new_row < len(puzzle):
                if 0 <= new_column < len(puzzle[0]):
                    new_effort = current_distance + 1
                    if new_effort < distances[new_row, new_column]:
                        distances[new_row, new_column] = new_effort
                        heapq.heappush(pq, (new_effort, (new_row, new_column)))

    return distances[(len(puzzle) - 1, len(puzzle[0]) - 1)]

# adapted from the Djikstra's algorithm in Module 7.3
