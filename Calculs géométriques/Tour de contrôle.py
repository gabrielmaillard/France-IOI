import math
import sys

def distance(point_A, point_B):
    abs = point_A[0] - point_B[0]
    ord = point_A[1] - point_B[1]

    return math.sqrt(abs**2+ord**2)

A0, A1 = map(int, input().split())
point_A = (A0, A1)

N = int(input())

distance_min = float("inf")

x_min = 0
y_min = 0

for _ in range(N):
    B0, B1 = map(int, sys.stdin.readline().split())
    new_distance = distance(point_A, (B0, B1))
    if new_distance < distance_min:
        distance_min = new_distance
        x_min = B0
        y_min = B1

print(x_min, y_min)