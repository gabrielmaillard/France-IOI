import sys

sys.setrecursionlimit(10000000)

def dfs(s, e):
    global counter
    low_visit[e], last_visit[e] = counter, counter
    counter += 1
    for i in range(len(connections[e])):
        if last_visit[connections[e][i]] == -1:
            dfs(e, connections[e][i])
            low_visit[e] = min(low_visit[e], low_visit[connections[e][i]])
            if low_visit[connections[e][i]] == last_visit[connections[e][i]]:
                paths.append((e, connections[e][i]))
        elif connections[e][i] != s:
            low_visit[e] = min(low_visit[e], last_visit[connections[e][i]])

nb_intersections, nb_paths = map(int, input().split())
connections = [[] for _ in range(nb_intersections + 1)]
low_visit = [-1] * (nb_intersections + 1)
last_visit = [-1] * (nb_intersections + 1)
paths = []
counter = 0

for _ in range(nb_paths):
    intersection1, intersection2 = map(int, sys.stdin.readline().split())
    connections[intersection1].append(intersection2)
    connections[intersection2].append(intersection1)

for i in range(1, nb_intersections + 1):
    if last_visit[i] == -1:
        dfs(i, i)

paths.sort()

blocked_paths = []
for bridge in paths:
    blocked_paths.append((min(bridge), max(bridge)))

print(len(blocked_paths))
sys.stdout.write("\n".join(["{} {}".format(path[0], path[1]) for path in blocked_paths]))
