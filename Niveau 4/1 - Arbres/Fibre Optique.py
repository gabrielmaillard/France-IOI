import sys
from collections import deque

def max_deconnectes(arcs, nb_ordis):
    voisins = [[] for _  in range(nb_ordis)]
    cables_connectes = [0] * nb_ordis
    pc_connectes = [1] * nb_ordis

    # Construction de la liste d'adjacence
    for i in range(nb_ordis - 1):
        ordi, voisin = map(int, arcs[i].split())
        
        voisins[ordi].append(voisin)
        voisins[voisin].append(ordi)
        
        cables_connectes[ordi] += 1
        cables_connectes[voisin] += 1
    
    feuilles = deque()

    # Récupération des feuilles
    for ordi in range(nb_ordis):
        if cables_connectes[ordi] == 1:
            feuilles.append(ordi)
    
    maximum_deconnectes = 0
    
    # Calcul du maximum
    while feuilles:
        ordi = feuilles.popleft()
        maximum_deconnectes = max(maximum_deconnectes, min(pc_connectes[ordi], nb_ordis - pc_connectes[ordi]))

        for voisin in voisins[ordi]:
            cables_connectes[voisin] -= 1
            pc_connectes[voisin] += pc_connectes[ordi]

            if cables_connectes[voisin] == 1:
                feuilles.append(voisin)
    
    return maximum_deconnectes

N = int(input())
arcs = [arc.strip() for arc in sys.stdin]

sys.stdout(str(max_deconnectes(arcs, N)))