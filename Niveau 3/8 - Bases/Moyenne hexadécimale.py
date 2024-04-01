N = int(input(), 16)
s = 0
for i in range(N):
    s += int(input(), 16)
print(hex(int(s/N))[2:].upper())