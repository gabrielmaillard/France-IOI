word = input()
speech = input().split(" ")
total = 0
for word_speech in speech:
    if word_speech.upper() == word.upper():
        total += 1
print(total)