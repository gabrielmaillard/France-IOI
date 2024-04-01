L = int(input())
letters = list(input())
N = int(input())

def generate_words(start_word, letter_list, target_length):
    for index, letter in enumerate(letter_list):
        new_word = start_word + letter
        new_letters = letter_list[:index] + letter_list[index+1:]

        if len(new_word) == target_length:
            print(new_word)
        else:
            generate_words(new_word, new_letters, target_length)

T = 1
for i in range(L - N + 1, L + 1):
    T *= i
print(T)
generate_words("", letters, N)
