import sys

def is_valid_move(x, y, L, C):
    return 0 <= x < L and 0 <= y < C

def bfs(maze, L, C, start):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    queue = [(start[0], start[1])]
    maze[start[0]][start[1]] = 'X'
    while queue:
        current = queue.pop(0)
        for direction in directions:
            new_x, new_y = current[0] + direction[0], current[1] + direction[1]
            if is_valid_move(new_x, new_y, L, C) and maze[new_x][new_y] == '.':
                queue.append((new_x, new_y))
                maze[new_x][new_y] = 'X'

def count_inaccessible_cells(L, C, maze):
    start = (1, 0)
    bfs(maze, L, C, start)
    inaccessible_count = sum(row.count('.') for row in maze)
    return inaccessible_count

L, C = map(int, input().split())
maze = [list(sys.stdin.readline()) for _ in range(L)]
result = count_inaccessible_cells(L, C, maze)
print(result)
