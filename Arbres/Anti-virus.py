import sys

def hauteurNoeud(arbre, noeud):
    p = 0
    while noeud != 0:
        noeud = arbre[noeud-1]
        p += 1
    return p

def parcoursRecursif(phrase, combinaisons, position):
    if position >= len(phrase):
        return
    
    for r in range(len(combinaisons)):
        if phrase[position] == "?":
            for i in range(1, 10):
                combinaisons.append(combinaisons[r]+str(i))
            if position != 0:
                combinaisons[r] += "0"
            else:
                combinaisons.pop(r)
        else:
            combinaisons[r] += phrase[position]
    
    parcoursRecursif(phrase, combinaisons, position + 1)
    return combinaisons

def main():
    N = int(sys.stdin.readline())
    phrase = list(map(int, sys.stdin.readline().split()))
    recherche = sys.stdin.readline()
    combinaisons = [""]
    combinaisons = parcoursRecursif(recherche, combinaisons, 0)
    possibilitesTPP = [[] for _ in range(N+1)]
    
    for i in combinaisons:
        if int(i) <= len(phrase):
            possibilitesTPP[hauteurNoeud(phrase, int(i))].append(int(i))
    
    for possibilites in possibilitesTPP:
        for possibilite in possibilites:
            sys.stdout.write(str(possibilite)+" ")

main()