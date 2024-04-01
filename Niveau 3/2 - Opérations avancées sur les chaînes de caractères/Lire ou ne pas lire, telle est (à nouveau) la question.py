def check_in_list(list, title):
    for book in list:
        if (book != 0) and (book > title):
            return False
    
    return True
num_books = int(input())
read_books = [0] * num_books
for book in range(num_books):
    title = input()
    if check_in_list(read_books, title):
        print(title)
        read_books[book] = title