def print_N(N, M):
    if N <= M:
        print(N, end=" ")
        print_N(N+1, M)
N, M = map(int, input().split(" "))
print_N(N, M)