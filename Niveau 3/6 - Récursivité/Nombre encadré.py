def recursion(nbIterations, nb):
    if nbIterations > 0:
        print("[", end="")
        recursion(nbIterations - 1, nb)
        print("]", end="")
    else:
        print(nb, end="")
nb, nbIterations = map(int, input().split(" "))
recursion(nbIterations, nb)