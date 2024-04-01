import sys
sys.stdin.readline()
available_densities = set(map(int, sys.stdin.readline().split()))
for q in range(int(sys.stdin.readline())):
    if int(sys.stdin.readline()) in available_densities:
        sys.stdout.write("1\n")
    else:
        sys.stdout.write("0\n")