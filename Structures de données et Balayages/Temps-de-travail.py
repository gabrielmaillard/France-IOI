import sys

num_intervals = int(sys.stdin.readline())
intervals = [tuple(map(int, sys.stdin.readline().split())) for _ in range(num_intervals)]

intervals.sort(key=lambda x: x[0])

total_time = 0
previous_end = -1

for interval in intervals:
    start, end = interval
    if start <= previous_end:
        if end > previous_end:
            total_time += end - previous_end
            previous_end = end
    else:
        total_time += end - start
        previous_end = end

sys.stdout.write(str(total_time))