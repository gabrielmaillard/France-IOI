import sys

def smallest_sequence_length(num_days, num_groups, groups):
    MAX_GROUPS = 100001

    group_occurrences = [0] * MAX_GROUPS
    present_groups = 0
    window_start = 0
    best_length = float('inf')

    for window_end in range(num_days):
        group = groups[window_end]
        group_occurrences[group] += 1

        if group_occurrences[group] == 1:
            present_groups += 1
        
        while present_groups == num_groups:
            window_length = window_end - window_start + 1
            best_length = min(best_length, window_length)
            start_group = groups[window_start]
            group_occurrences[start_group] -= 1

            if group_occurrences[start_group] == 0:
                present_groups -= 1

            window_start += 1
    
    return str(best_length)

def main():
    num_days, num_groups = map(int, sys.stdin.readline().split())
    groups = list(map(int, sys.stdin.readline().split()))
    result = smallest_sequence_length(num_days, num_groups, groups)
    sys.stdout.write(result)

main()
