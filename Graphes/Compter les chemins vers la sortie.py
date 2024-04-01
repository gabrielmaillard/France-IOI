import sys

sys.setrecursionlimit(1000000000)

num_lines, num_columns = map(int, input().split())
labyrinth = []
for _ in range(num_lines):
    labyrinth.append(list(input()))

possible_paths = 0

def paths(current_x, current_y):
    global possible_paths
    
    if current_x == num_columns - 2 and current_y == num_lines - 1:
        possible_paths += 1
        return

    temp = labyrinth[current_y][current_x]
    labyrinth[current_y][current_x] = "#"  # Marquer la case comme visitée
    
    movements = [(0, -1), (0, 1), (1, 0), (-1, 0)]
    for movement in movements:
        new_y = movement[0] + current_y
        new_x = movement[1] + current_x
        if 0 <= new_y < num_lines and 0 <= new_x < num_columns and labyrinth[new_y][new_x] == ".":
            paths(new_x, new_y)

    labyrinth[current_y][current_x] = temp

paths(0, 1)
print(possible_paths)