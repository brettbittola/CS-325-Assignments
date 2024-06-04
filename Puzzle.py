# Brett Bittola
# 3/3/2024
# CS 325 Graph Algorithms


import heapq


def solve_puzzle(Board, Source, Destination):
    """Finds the shortest path between a source and destination"""
    distances = {(row, col): float('infinity') for row in range(len(Board)) for col in range(len(Board[0]))}
    distances[Source] = 0
    directions = {'R': (0, 1), 'L': (0, -1), 'U': (-1, 0), 'D': (1, 0)}
    visited = {}
    path = []
    path_moves = ''
    pq = [(0, Source)]

    if Source == Destination:
        return [Destination], path_moves

    while len(pq) > 0:
        current_distance, (row, column) = heapq.heappop(pq)
        if (row, column) == Destination:
            while (row, column) != Source:
                path.append((row, column))
                row, column = visited[(row, column)]
            path.append(Source)
            path.reverse()

            for i in range(1, len(path)):
                row, column = path[i]
                previous_row, previous_column = path[i - 1]
                for direction, (x, y) in directions.items():
                    if row == previous_row + x:
                        if column == previous_column + y:
                            path_moves += direction
                            break

            return path, path_moves

        if current_distance > distances[(row, column)]:
            continue

        for move, (x, y) in directions.items():
            new_row, new_column = row + x, column + y
            if 0 <= new_row < len(Board):
                if 0 <= new_column < len(Board[0]):
                    if Board[new_row][new_column] == '-':
                        new_effort = current_distance + 1
                        if new_effort < distances[new_row, new_column]:
                            distances[new_row, new_column] = new_effort
                            heapq.heappush(pq, (new_effort, (new_row, new_column)))
                            visited[(new_row, new_column)] = (row, column)

    if not path:
        return None

    return path, path_moves


# adapted from the Djikstra's algorithm in Module 7.3 and from my MinPuzzle.py assignment from last week
