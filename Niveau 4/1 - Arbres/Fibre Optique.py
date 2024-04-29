import sys
from collections import deque

def max_disconnected(edges, num_computers):
    neighbors = [[] for _ in range(num_computers)]
    connected_cables = [0] * num_computers
    connected_pcs = [1] * num_computers

    # Building the adjacency list
    for i in range(num_computers - 1):
        computer, neighbor = map(int, edges[i].split())

        neighbors[computer].append(neighbor)
        neighbors[neighbor].append(computer)

        connected_cables[computer] += 1
        connected_cables[neighbor] += 1

    leaves = deque()

    # Gathering leaves
    for computer in range(num_computers):
        if connected_cables[computer] == 1:
            leaves.append(computer)

    max_disconnected = 0

    # Calculating the maximum
    while leaves:
        computer = leaves.popleft()
        max_disconnected = max(max_disconnected, min(connected_pcs[computer], num_computers - connected_pcs[computer]))

        for neighbor in neighbors[computer]:
            connected_cables[neighbor] -= 1
            connected_pcs[neighbor] += connected_pcs[computer]

            if connected_cables[neighbor] == 1:
                leaves.append(neighbor)

    return max_disconnected

N = int(input())
edges = [edge.strip() for edge in sys.stdin]

sys.stdout.write(str(max_disconnected(edges, N)))
