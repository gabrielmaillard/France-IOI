def max_current(list_, list_length, sub_list_length):
    max_sum = sum(list_[:sub_list_length])
    sum_current = max_sum
    for i in range(sub_list_length, list_length):
        sum_current = sum_current - list_[i - sub_list_length] + list_[i]
        if sum_current > max_sum:
            max_sum = sum_current
    
    return max_sum

def main():
    sub_list_length, list_length = map(int, input().split(" "))
    list_ = list(map(int, input().split(" ")))
    print(max_current(list_, list_length, sub_list_length))

main()
