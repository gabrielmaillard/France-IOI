nbIterations = int(input())
sentence = "= 0"
def changeO(nbIterations, sentence):
    if nbIterations > 0:
        sentence = sentence.replace("0", "(0 + 0)")
        sentence = changeO(nbIterations - 1, sentence)
    return sentence
print("0", changeO(nbIterations, sentence))