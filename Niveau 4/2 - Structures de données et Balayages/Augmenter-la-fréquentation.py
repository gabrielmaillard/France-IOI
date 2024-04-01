num_shows = int(input())
shows = []

for _ in range(num_shows):
    duration, visits = map(int, input().split())
    shows.append((duration, visits))

shows.sort()
max_average_visits = 0
total_sum = 0
chosen_duration_limit = 0

for i in range(num_shows):
    total_sum += shows[i][1]
    
    if max_average_visits <= total_sum / (i + 1):
        max_average_visits = total_sum / (i + 1)
        chosen_duration_limit = shows[i][0]

print(chosen_duration_limit)