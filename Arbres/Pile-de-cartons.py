import sys

nbCartons = int(sys.stdin.readline())
arbre = []

for i in range(nbCartons+1):
    arbre.append(list(map(int, sys.stdin.readline().split()))[1:])

def parcourirTotaliteArbre(arbreGlobal, arbrePetit):
    for noeud in arbrePetit:
        sys.stdout.write("A "+str(noeud)+"\n")
        parcourirTotaliteArbre(arbreGlobal, arbreGlobal[noeud])
        sys.stdout.write("R "+str(noeud)+"\n")

parcourirTotaliteArbre(arbre, arbre[0])