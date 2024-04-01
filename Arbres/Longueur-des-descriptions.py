import sys

def construire_arbre(produits):
    arbre = {0: []}
    for produit, container in enumerate(produits, 1):
        if container not in arbre:
            arbre[container] = []
        arbre[container].append(produit)
    return arbre

def hauteur_arbre(arbre, noeud):
    pile = [(noeud, 1)]
    hauteur_max = 0
    while pile:
        noeud, hauteur = pile.pop()
        if noeud in arbre:
            for fils in arbre[noeud]:
                pile.append((fils, hauteur + 1))
        hauteur_max = max(hauteur_max, hauteur)
    return hauteur_max

def main():
    sys.stdin.readline()
    produits = list(map(int, sys.stdin.readline().split()))
    arbre = construire_arbre(produits)
    print(hauteur_arbre(arbre, 0)-1)

main()