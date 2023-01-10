from heapq import heappop, heappush

def get_adjacent_squares(square, matrix, visited):
    x, y = square
    result = []
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        if 0 <= x + dx < len(matrix) and 0 <= y + dy < len(matrix[0]) and matrix[x + dx][y + dy] != 1 and (x + dx, y + dy) not in visited:
            result.append((x + dx, y + dy))
    return result


def a_star(matrix):
    start, end = None, None
    rows, cols = len(matrix), len(matrix[0])
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 2:
                start = (i, j)
            elif matrix[i][j] == 3:
                end = (i, j)
    if not start or not end:
        raise ValueError('Invalid matrix: no start or end square')

    heap = []
    heappush(heap, (0, start))
    visited = set()
    path = {}
    while heap:
        cost, square = heappop(heap)
        if square == end:
            path_reversed = []
            while square != start:
                path_reversed.append(square)
                square = path[square]
            path_reversed.append(start)
            return list(reversed(path_reversed))
        visited.add(square)
        for adj_square in get_adjacent_squares(square, matrix, visited):
            path[adj_square] = square
            heappush(heap, (cost + 1, adj_square))
    raise ValueError('No path found')


import matplotlib.pyplot as plt

def plot_matrix_with_path(matrix, path):
    rows, cols = len(matrix), len(matrix[0])

    walls = [[matrix[i][j] == 1 for j in range(cols)] for i in range(rows)]

    path_matrix = [[0 for _ in range(cols)] for _ in range(rows)]

    for square in path:
        x, y = square
        path_matrix[x][y] = 1


    fig, ax = plt.subplots()
    ax.imshow(path_matrix, cmap='gray', interpolation='nearest', vmin=0, vmax=1)
    ax.imshow(walls, cmap='binary', interpolation='nearest', alpha=0.5)


    for i in range(len(path) - 1):
        x1, y1 = path[i]
        x2, y2 = path[i + 1]
        ax.add_artist(plt.Arrow(y1, x1, y2 - y1, x2 - x1, width=0.3, color='gray'))

    plt.show()
import random

def generate_matrix():
    matrix = [[0 for _ in range(16)] for _ in range(16)]
    for _ in range(100):
        x, y = random.randint(0, 15), random.randint(0, 15)
        matrix[x][y] = 1
    print("enter cordnets for start")
    x, y = int(input("input x: ")), int(input("y: "))
    matrix[x][y] = 2
    print("enter cordnets for end")
    x, y = int(input("input x: ")), int(input("y: "))
    matrix[x][y] = 3

    return matrix


matrix = generate_matrix()
path = a_star(matrix)
plot_matrix_with_path(matrix, path)
