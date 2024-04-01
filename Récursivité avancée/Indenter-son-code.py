import sys
sys.setrecursionlimit(100000)
sequence = sys.stdin.readline()

def indenter(chaine, index, indentation):
    if chaine[index] == '{' and chaine[index-1] == '{':
        indentation += 3
    elif chaine[index] == '}' and chaine[index-1] == '}':
        indentation -= 3
    sys.stdout.write((indentation * " ") + chaine[index]+"\n")
    if index+2 < len(chaine):
        indenter(chaine, index+1, indentation)

indenter(sequence, 0, 0)