def find_maze_path(maze):

    rows = len(maze)
    cols = len(maze[0])

    visited = [[False] * cols for _ in range(rows)]
    path = []

    def solve(r, c):
        if (r < 0 or r >= rows or
            c < 0 or c >= cols or
            maze[r][c] == 0 or visited[r][c]):
            return False
        visited[r][c] = True
        path.append((r, c))
        if r == rows - 1 and c == cols - 1:
            return True
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for dr, dc in directions:
            if solve(r + dr, c + dc):
                return True
        path.pop()
        return False
    if solve(0, 0):
        return path
    else:
        return None

maze = [
    [1, 0, 0, 0],
    [1, 1, 0, 1],
    [0, 1, 1, 1],
    [0, 0, 0, 1]
]

result = find_maze_path(maze)
if result:
    print("Path found!")
    print("Coordinates:")
    for position in result:
        print(position)
else:
    print("No valid path exists!")