def sum(square):
    return sum(square[0])

def diagonals(square, sum_):
    sum1 = 0
    sum2 = 0
    n = len(square)
    for i in range(n):
        sum1 += square[i][i]
        sum2 += square[i][n - 1 - i]
    return sum1 == sum2 == sum_

def columns(square, sum_):
    for j in range(len(square)):
        sum = 0
        for i in range(len(square)):
            sum += square[i][j]
        if sum != sum_:
            return False
    return True

def lines(square):
    for row in square:
        somme_ = sum(row)
        if somme_ != sum:
            return False
    return True

def create_square(N):
    square = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        line = input().split(" ")
        for j in range(N):
            square[i][j] = int(line[j])
    return square

def magical_shape(square):
    num_already_used = set()
    for row in square:
        for column in row:
            if 1 <= column <= len(square) ** 2 and column not in num_already_used:
                num_already_used.add(column)
            else:
                return False
    return True

def main():
    N = int(input())
    square = create_square(N)
    sum = sum(square)
    if lines(square, sum) and diagonals(square, sum) and columns(square, sum) and magical_shape(square):
        print("yes")
    else:
        print("no")
main()