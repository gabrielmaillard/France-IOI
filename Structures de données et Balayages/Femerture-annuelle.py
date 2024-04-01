import sys

def main():
    schedule = []
    year_duration, num_festivals = map(int, sys.stdin.readline().split())

    for i in range(num_festivals):
        festival_start, festival_end = map(int, sys.stdin.readline().split())
        if festival_start < festival_end:
            schedule.append((festival_start, festival_end))
        else:
            schedule.append((festival_start, year_duration))
            schedule.append((0, festival_end))

    schedule.sort()
    max_idle_period = schedule[0][0]
    end_parser = schedule[0][1]

    for festival in schedule:
        if festival[0] <= end_parser and festival[1] >= end_parser:
            end_parser = festival[1]
        elif festival[0] > end_parser:
            new_gap = festival[0] - end_parser
            if max_idle_period < new_gap:
                max_idle_period = new_gap
            end_parser = festival[1]

    gap_between_seasons_festivals = year_duration + schedule[0][0] - end_parser
    
    if max_idle_period < gap_between_seasons_festivals:
        max_idle_period = gap_between_seasons_festivals

    sys.stdout.write(str(max_idle_period))

main()
