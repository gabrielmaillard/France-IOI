def print_binary(number):
    if number > 1:
        print_binary(number // 2)
    print(number % 2,end="")
T = int(input())
for i in range(1, T+1):
    for j in range(1, T+1):
        print_binary(i*j)
        print("\t", end="")
    print()