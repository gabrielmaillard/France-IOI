import sys

def order_verification(N, paths):
    graph = {}
    in_degree = [0] * (N + 1)

    for a, b in paths:
        if a not in graph:
            graph[a] = []
        graph[a].append(b)
        in_degree[b] += 1

    queue = [i for i in range(1, N + 1) if in_degree[i] == 0]

    ordre = []

    while queue:
        intersection = queue.pop(0)
        ordre.append(intersection)

        if intersection in graph:
            for neighbour in graph[intersection]:
                in_degree[neighbour] -= 1
                if in_degree[neighbour] == 0:
                    queue.append(neighbour)

    if any(in_degree[1:]):
        return -1
    else:
        return ordre

N, A = map(int, input().split())
paths = [tuple(map(int, sys.stdin.readline().split())) for _ in range(A)]

result = order_verification(N, paths)
if result == -1:
    print("-1")
else:
    print(" ".join(map(str, result)))