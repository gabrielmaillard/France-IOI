import sys

N = int(sys.stdin.readline().strip())
codeVersCode = [0] + list(map(int, sys.stdin.readline().split()))

def trouverRecipiantCommun(code1, code2):
    parcourus = set()
    
    while code1 != 0 or code2 != 0:
        if code1 != 0:
            if code1 in parcourus:
                return code1
            parcourus.add(code1)
            code1 = codeVersCode[code1]
        if code2 != 0:
            if code2 in parcourus:
                return code2
            parcourus.add(code2)
            code2 = codeVersCode[code2]
    
    return 0

R = int(sys.stdin.readline().strip())

for _ in range(R):
    code1, code2 = map(int, sys.stdin.readline().split())
    resultat = trouverRecipiantCommun(code1, code2)
    sys.stdout.write(str(resultat) + "\n")