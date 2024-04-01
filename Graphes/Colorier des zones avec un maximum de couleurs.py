import sys

def is_valid(x, y, n, m):
    return 0 <= x < n and 0 <= y < m

def dfs(x, y, color, image, visited):
    visited[x][y] = True
    image[x][y] = color

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if is_valid(nx, ny, len(image), len(image[0])) and not visited[nx][ny] and image[nx][ny] == '.':
            dfs(nx, ny, color, image, visited)

def count_colors(image):
    n, m = len(image), len(image[0])
    visited = [[False] * m for _ in range(n)]
    color_count = 0

    for i in range(n):
        for j in range(m):
            if not visited[i][j] and image[i][j] == '.':
                color_count += 1
                dfs(i, j, color_count, image, visited)

    return color_count

n, m = map(int, input().split())
image = [list(sys.stdin.readline()) for _ in range(n)]

result = count_colors(image)

print(result)
