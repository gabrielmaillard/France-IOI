letters = "".join(input().upper().split(" "))

array = [0] * 26

for letter in letters:
    array[ord(letter) - 65] += 1

max = 0

for i in range(26):
    if (array[i] > array[max]):
        max = i

print(chr(max + 65))