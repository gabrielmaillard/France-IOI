num_targets = int(input())
targets = list(map(int, input().split()))

num_lots = int(input())
lots = list(map(int, input().split()))

lot_index = 0

for target in targets:
    while (lot_index < num_lots) and lots[lot_index] <= target:
        lot_index += 1
    print(lots[lot_index - 1], end=" ")
