import sys
sys.setrecursionlimit(100000)
sequence = sys.stdin.readline()

def indent(string, index, indentation):
    if string[index] == '{' and string[index-1] == '{':
        indentation += 3
    elif string[index] == '}' and string[index-1] == '}':
        indentation -= 3
    sys.stdout.write((indentation * " ") + string[index]+"\n")
    if index+2 < len(string):
        indent(string, index+1, indentation)

indent(sequence, 0, 0)