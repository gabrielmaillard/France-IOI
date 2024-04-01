nB10 = 0
nB2 = input()
for i in range(0, len(nB2)):
    if nB2[len(nB2)-1-i] == "1":
        nB10 += 2**i
print(nB10)