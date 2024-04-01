def numberLove(firstname):
    sum = 0
    for letter in firstname:
        sum += ord(letter) - 65
    
    if sum < 10:
        return sum
    
    while sum >= 10:
        sum = sum([int(i) for i in str(sum)])
    
    return sum
            

for num_love in [numberLove(firstname) for firstname in input().split(" ")]:
    print(num_love, end=" ")