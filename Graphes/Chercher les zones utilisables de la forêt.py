import sys
sys.setrecursionlimit(1000000000)

N, A = map(int, input().split())

connections = [[] for _ in range(N+1)]

for _ in range(A):
    i1, i2, s = map(int, input().split())
    connections[i1].append(i2)
    connections[i2].append(i1)

visited = set()

def traverse_node(node, visited):
    n = 1
    visited.add(node)
    for sub_node in connections[node]:
        if sub_node not in visited:
            n += traverse_node(sub_node, visited)
    return n

n = 0
qtyMax = 0

for i in range(1, N+1):
    if i not in visited:
        n += 1
        qty = traverse_node(i, visited)
        if qty > qtyMax:
            qtyMax = qty

print(n, qtyMax)