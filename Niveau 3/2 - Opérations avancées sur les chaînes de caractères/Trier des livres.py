num_books = int(input())
books = [0] * num_books
for i in range(num_books):
    books[i] = input()
books.sort()
for j in range(num_books):
    print(books[j])