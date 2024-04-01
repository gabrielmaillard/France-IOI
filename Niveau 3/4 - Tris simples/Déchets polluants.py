N, M = map(int, input().split(" "))
dangerous_products = [int(i) for i in input().split(" ")]
def trier(list, M):
    for _ in range(M):
        max_pollution = -1
        max_index = -1
        for i in range(len(list)):
            if list[i] > max_pollution:
                max_pollution = list[i]
                max_index = i
        if max_index != -1:
            print(max_pollution, end=" ")
            list[max_index] = 0
trier(dangerous_products, M)