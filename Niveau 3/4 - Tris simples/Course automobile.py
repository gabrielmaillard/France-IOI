def min_pass(num_cars, arrival_order):
    array_arrival_order = list(arrival_order)
    array_position = list(range(1, num_cars + 1))
    array_ideal = [1, 2, 3, 4]
    moves = []
    
    is_swapped = True
    while is_swapped:
        is_swapped = False
        for index in range(len(array_arrival_order) - 1):
            if array_arrival_order[index] > array_arrival_order[index + 1]:
                array_arrival_order[index], array_arrival_order[index + 1] = array_arrival_order[index + 1], array_arrival_order[index]
                array_position[index], array_position[index + 1] = array_position[index + 1], array_position[index]
                moves.append((array_arrival_order[index + 1], array_arrival_order[index]))
                is_swapped = True
    return moves
def main():
    num_cars = int(input())
    arrival_order = list(map(int, input().split()))
    moves = min_pass(num_cars, arrival_order)
    print(len(moves))
    for move in moves:
        print(" ".join(map(str, move)))
main()