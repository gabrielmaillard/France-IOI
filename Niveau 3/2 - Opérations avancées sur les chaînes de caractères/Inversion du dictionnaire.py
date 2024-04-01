num_words = int(input())

words_first_language = []
words_second_language = []

for _ in range(num_words):
    word1, word2 = input().split()
    words_first_language.append(word1)
    words_second_language.append(word2)

reversed_words = []

for i in range(num_words):
    reversed_words.append((words_second_language[i], words_first_language[i]))

reversed_words.sort(key=lambda x: x[0])

for word in reversed_words:
    print(word[0], word[1])