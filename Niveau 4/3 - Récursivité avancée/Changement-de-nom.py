L = int(input())
letters = list(input())
N = int(input())

def generate_words(start_word, letter_list, target_length):
    for letter in letter_list:
        temp_word = start_word + letter

        if len(temp_word) == target_length:
            print(temp_word)
        else:
            generate_words(temp_word, letter_list, target_length)

print(L**N)
generate_words("", letters, N)
