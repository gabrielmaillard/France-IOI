num_books = int(input())
new_order = [0] * num_books
for i in range(num_books):
    new_order[num_books - i - 1] = input()
for i in new_order:
    print(i)