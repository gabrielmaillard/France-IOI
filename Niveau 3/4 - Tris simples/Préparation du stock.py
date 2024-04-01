def insert_element(list, element, list_index):
    if len(list) == 0:
        list_index.append(0)
        list.append(element)
        return [list, list_index]
    if element <= list[0]:
        list.insert(0, element)
        list_index.append(0)
        return [list, list_index]
    elif element > list[len(list) - 1]:
        list.insert(len(list), element)
        list_index.append(len(list)-1)
        return [list, list_index]
    done = False
    i = 0
    while not done:
        if list[i] < element <= list[i+1]:
            done = True
            list.insert(i+1, element)
            list_index.append(i+1)
            return [list, list_index]
        i += 1
def main():
    N, M = map(int, input().split(" "))
    if N > 0:
        initial_stock = [int(i) for i in input().split(" ")]
    else:
        input()
        initial_stock = []
    trays = [int(i) for i in input().split(" ")]
    list_index = []
    for tray in trays:
        request = insert_element(initial_stock, tray, list_index)
        trays = request[0]
        list_index = request[1]
    print(" ".join(map(str, list_index)))
    print(" ".join(map(str, trays)))
main()