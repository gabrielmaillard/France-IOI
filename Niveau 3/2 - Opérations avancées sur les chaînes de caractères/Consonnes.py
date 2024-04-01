vowels = [
    "A", "E", "I", "O", "U", "Y"
]

for i in range(ord("A"), ord("Z") + 1):
    if chr(i) not in vowels:
        print(chr(i).lower(), end=" ")