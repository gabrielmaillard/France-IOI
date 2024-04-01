sentence = input()
def reversed_sentence(phrase):
    if len(phrase) > 0:
        print(phrase[-1], end="")
        reversed_sentence(phrase[0:-1])
reversed_sentence(sentence)