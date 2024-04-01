base, nbC = map(int, input().split(" "))
chiffres = input().split(" ")
nbDecimal = 0
for chiffre in chiffres:
    nbDecimal = (nbDecimal * base) + int(chiffre)
print(nbDecimal)