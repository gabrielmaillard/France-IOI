def scan(list, occurrences):
    for c in list:
        occurrences[c-1] += 1
        if occurrences[c-1] == 2:
            return c
    return -1
def main():
    size = int(input())
    list = list(map(int, input().split(" ")))
    occurrences = [0] * 1000000
    print(scan(list, occurrences))
main()