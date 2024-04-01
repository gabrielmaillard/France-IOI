L, N = map(int, input().split())
X_points = list(map(int, input().split()))
X_points.sort()

max_reachable_point = X_points[0] + L
start_parser = 0
end_parser = 0
num_points = 0
maximum = 1

while end_parser < N and start_parser + 1 < N:
    while end_parser < N and X_points[end_parser] <= max_reachable_point:
        num_points += 1
        end_parser += 1

    if num_points > maximum:
        maximum = num_points

    max_reachable_point += X_points[start_parser + 1] - X_points[start_parser]
    start_parser += 1
    num_points -= 1

print(maximum)
