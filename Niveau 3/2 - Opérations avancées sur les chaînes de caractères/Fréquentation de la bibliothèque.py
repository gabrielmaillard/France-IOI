sum = 0
try:
    while True:
        numbers = input().split(" ")
        for number in numbers:
            sum += int(number)
except:
    pass
print(sum)