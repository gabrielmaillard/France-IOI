size = int(input())
string = input()
num_open = 0
answer = 1
for c in string:
    if c == "(":
        num_open += 1
    elif c == ")":
        num_open -= 1
   
    if num_open < 0:
        answer = 0
if num_open > 0:
    answer = 0
print(answer)