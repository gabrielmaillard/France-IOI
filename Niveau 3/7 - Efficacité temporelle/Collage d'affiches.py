import sys
requests = int(input())
array = []
for i in range(requests):
    request=sys.stdin.readline()
    if request == "Q\n":
        print (len(array))
    else :
        size = int(request[2:])
        while len(array) !=0 and array[-1]<= size:
            del array[-1]
        array.append(size)