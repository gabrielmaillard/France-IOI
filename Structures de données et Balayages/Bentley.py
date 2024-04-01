def max_sublist_sum(N, array):
    max_local_sum = max_global_sum = array[0]

    for element in array[1:]:
        max_local_sum = max(element, max_local_sum + element)
        max_global_sum = max(max_global_sum, max_local_sum)

    return max_global_sum

N = int(input())
array = list(map(int, input().split()))

result = max_sublist_sum(N, array)

if result == -1:
    print(0)
else:
    print(result)
