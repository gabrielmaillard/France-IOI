O = int(input())
array = []
for i in range(O):
    qty, date = map(int, input().split(" "))
    if qty>0:
        for j in range(qty):
            array.append(date)
    else:
        for j in range(-qty):
            array.pop(0)
print(sorted(array)[0])