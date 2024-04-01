sentence = "".join(input().split(" "))
array = [0] * 26
length_sentence = 0
for letter in sentence:
    if (letter.isalpha()):
        array[ord(letter.upper()) - 65] += 1
        length_sentence += 1
for i in range(26):
    print(array[i]/length_sentence)