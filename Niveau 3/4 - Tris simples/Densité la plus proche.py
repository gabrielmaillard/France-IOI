import sys
import bisect
def objetLePlusProche(available_densities, asked_density):
    index = bisect.bisect_left(available_densities, asked_density)
    
    if index == 0:
        return available_densities[0]
    if index == len(available_densities):
        return available_densities[-1]
    
    left_diff = asked_density - available_densities[index - 1]
    right_diff = available_densities[index] - asked_density
    
    if left_diff <= right_diff:
        return available_densities[index - 1]
    else:
        return available_densities[index]

def main():
    sys.stdin.readline()
    available_densities = sorted(map(int, sys.stdin.readline().split()))
    for q in range(int(sys.stdin.readline())):
        asked_density = int(sys.stdin.readline())
        nearest_density = objetLePlusProche(available_densities, asked_density)
        sys.stdout.write(str(nearest_density) + "\n")

main()