import sys

def main():
    num_days, num_periods = map(int, sys.stdin.readline().split())
    visitors_per_day = list(map(int, sys.stdin.readline().split()))

    cumulative_sum = [0] * (num_days + 1)
    for i in range(1, num_days + 1):
        cumulative_sum[i] = cumulative_sum[i - 1] + visitors_per_day[i - 1]

    for _ in range(num_periods):
        start_day, end_day = map(int, sys.stdin.readline().split())
        total_visitors = cumulative_sum[end_day] - cumulative_sum[start_day - 1]
        print(total_visitors)

main()
