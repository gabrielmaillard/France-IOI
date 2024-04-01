num_books = int(input())

for i in range(num_books):
    title = input()
    modified_title = "".join(title.split(" "))

    reversed = ""
    for i in range(-1, -len(modified_title)-1, -1):
        reversed += modified_title[i]
    
    if (reversed.upper() == modified_title.upper()):
        print(title)