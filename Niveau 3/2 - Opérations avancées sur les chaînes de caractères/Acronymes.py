def check_title(title, acronym):
    title = title.upper().split(" ")
    if not len(acronym) == len(title):
        return False
    initials = list(acronym)
    for i in range(len(initials)):
        if not initials[i] == title[i][0]:
            return False
    
    return True
acronym = input().upper()
num_books = int(input())
for line in range(num_books):
    title = input()
    if check_title(title, acronym):
        print(title.title())