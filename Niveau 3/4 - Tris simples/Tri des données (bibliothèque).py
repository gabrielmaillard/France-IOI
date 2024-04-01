import sys
input()
line = [i for i in map(int, input().split(" "))]
line.sort()
sys.stdout.write(" ".join(map(str, line)))