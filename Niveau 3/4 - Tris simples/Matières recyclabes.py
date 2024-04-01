elements = []
for i in range(int(input())):
    elements.append(input())
print(
    *(str(el) for el in sorted(elements)),
    sep="\n"
)