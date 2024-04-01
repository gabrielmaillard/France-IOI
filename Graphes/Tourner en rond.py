import sys

def main():
    nbIntersections,nbSentiers = map(int, sys.stdin.readline.split())
    sentiers = [[] for _ in range(nbIntersections + 1)]

    for _ in range(nbSentiers):
        srce,dest = map(int, input().split())
        sentiers[srce].append(dest)
    
    AUCUNE = 0
    EN_COURS = 1
    MARQUE = 2
    marques = [AUCUNE]*(nbIntersections + 1)

    sys.setrecursionlimit(nbIntersections + 50)
    
    def rechercherCycle(srce):
        nonlocal marques
        marques[srce] = EN_COURS
        for dest in sentiers[srce]:
            if marques[dest] == AUCUNE:
                rechercherCycle(dest)
            elif marques[dest] == EN_COURS:
                print("OUI")
                exit(0)
        marques[srce] = MARQUE
    for intersection in range(1,nbIntersections + 1):
        if marques[intersection] == AUCUNE:
            rechercherCycle(intersection)
    print("NON")

main()