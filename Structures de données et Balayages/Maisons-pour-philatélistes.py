import sys

sys.stdin.readline()

def find_closest_distance(houses):
    sorted_houses = sorted(houses)
    closest_pair = min(((sorted_houses[i], sorted_houses[i + 1]) for i in range(len(sorted_houses) - 1)), key=lambda pair: pair[1] - pair[0])
    return abs(closest_pair[1] - closest_pair[0])

house_positions = list(map(int, sys.stdin.readline().split()))
result = find_closest_distance(house_positions)
sys.stdout.write(str(result))
