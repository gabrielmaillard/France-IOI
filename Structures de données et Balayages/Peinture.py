num_quantities, target_quantity = map(int, input().split())
pots = list(map(int, input().split()))

pot_index = 0
pot_second_index = num_quantities - 1

answer = "NON"

while pot_index <= pot_second_index:
    quantity_to_find = target_quantity - pots[pot_index]

    while pots[pot_second_index] > quantity_to_find and pot_second_index > 0:
        pot_second_index -= 1
    
    if pot_second_index == 0:
        break

    if pots[pot_second_index] == quantity_to_find:
        answer = "OUI"
        break
    else:
        pot_index += 1

print(answer)