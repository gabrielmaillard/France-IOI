num_episodes, max_duration = map(int, input().split())
durations = list(map(int, input().split()))

start_parser = 0
end_parser = 0
total_duration = durations[0]

if total_duration < max_duration:
    max_result = 1
else:
    max_result = 0

while end_parser < num_episodes - 1:
    if total_duration + durations[end_parser + 1] <= max_duration:
        end_parser += 1
        total_duration += durations[end_parser]
        max_current = end_parser - start_parser + 1
        if max_current > max_result:
            max_result = max_current
    else:
        total_duration -= durations[start_parser]
        start_parser += 1

print(max_result)
